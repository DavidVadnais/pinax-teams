from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pinax-teams")
except PackageNotFoundError:
    __version__ = "unknown"

default_app_config = "pinax.teams.apps.AppConfig"
