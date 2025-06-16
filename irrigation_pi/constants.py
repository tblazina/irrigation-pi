"""Constants for irrigation_pi package."""

from pathlib import Path

DEBIAN_PACKAGES: list[str] = [
    "nginx",
]

PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent.resolve()
VIRTUAL_ENVIRONMENT_PATH: Path = PROJECT_ROOT_PATH / ".venv"
BACKEND_PATH: Path = PROJECT_ROOT_PATH / "backend"
FRONTEND_PATH: Path = PROJECT_ROOT_PATH / "frontend"
DATABASE_PATH: Path = BACKEND_PATH / "sqlite_db" / "backend.db"

APPLICATION_CONFIGURATION_PATH: Path = PROJECT_ROOT_PATH / "config.toml"

NGINX_CONFIG_PATH: Path = Path("/etc/nginx/sites-available/irrigation-pi")
NGINX_CONFIG_ACTIVATION_PATH: Path = Path("/etc/nginx/sites-enabled/irrigation-pi")
NGINX_DEFAULT_CONFIG_ACTIVATION_PATH: Path = Path("/etc/nginx/sites-enabled/default")

SYSTEMD_CONFIG_PATH: Path = Path("/etc/systemd/system/irrigation-pi.service")

APPLICATION_USER: str = PROJECT_ROOT_PATH.owner()
APPLICATION_USER_GROUP: str = PROJECT_ROOT_PATH.group()

HOST: str = "baeulipi.local"
PORT: str = "80"

NETWORKMANAGER_CONFIG_FILE: Path = Path("/etc/NetworkManager/NetworkManager.conf")
WIFI_HOTSPOT_CONNECTION_NAME: str = "Irrigation-Pi"
