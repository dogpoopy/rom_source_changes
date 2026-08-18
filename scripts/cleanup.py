import shutil
from pathlib import Path

import yaml


CONFIG_FILE = Path("roms_config.yaml")
DATA_DIR = Path("public/data")


def load_config():
    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main():
    config = load_config()

    allowed = {
        (rom["id"], branch)
        for rom in config.get("roms", [])
        for branch in rom.get("branches", [])
    }

    allowed_branches = {}

    for rom_id, branch in allowed:
        allowed_branches.setdefault(rom_id, set()).add(branch)

    if not DATA_DIR.exists():
        return

    for entry in DATA_DIR.iterdir():
        if entry.is_file():
            print(f"Removing stale file: {entry}")
            entry.unlink()
            continue

        if entry.is_dir() and entry.name not in allowed_branches:
            print(f"Removing stale ROM directory: {entry}")
            shutil.rmtree(entry)
            continue

        if not entry.is_dir():
            continue

        for file in entry.iterdir():
            if not file.is_file():
                if file.is_dir():
                    print(f"Removing unexpected directory: {file}")
                    shutil.rmtree(file)
                continue

            if file.suffix != ".json" or file.stem not in allowed_branches[entry.name]:
                print(f"Removing stale file: {file}")
                file.unlink()


if __name__ == "__main__":
    main()
