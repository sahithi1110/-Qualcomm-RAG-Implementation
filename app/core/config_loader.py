from pathlib import Path
import yaml


def load_settings(settings_path: str = "config/settings.yaml") -> dict:
    settings_file = Path(settings_path)

    if not settings_file.exists():
        raise FileNotFoundError(f"Settings file not found: {settings_path}")

    with settings_file.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
