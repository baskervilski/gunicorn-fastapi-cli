import importlib
from gunicorn.app.base import BaseApplication
import yaml
import logging

logger = logging.getLogger(__name__)


def load_config(filename):
    with open(filename) as cfg_file:
        return yaml.safe_load(cfg_file)


class CustomGunicorn(BaseApplication):
    __config_file_key = "config_file"
    __app_key = "wsgi_app"

    def __init__(self, **kwargs):
        self._options = {}

        self.config_file = kwargs.pop(self.__config_file_key, None)
        if self.config_file:
            logger.info(f"Config file: {self.config_file}")
            cfg_dict = load_config(self.config_file)["server"]
            logger.info(f"Config file options: {cfg_dict}")
            self._options = cfg_dict

        logger.info(f"**kwargs: {kwargs}")
        # We give precedence to options passed as init params
        # over those specified in the config file
        self._options.update(kwargs)
        self.application = None

        super().__init__()

    def load_config(self):
        # Default load_config from gunicorn customization documentation
        # we didn't change anything here
        config = {
            key: value
            for key, value in self._options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """Here we load the WSGI App"""
        module_name, app_name = self._options[self.__app_key].split(":")
        module = importlib.import_module(module_name)
        self.application = getattr(module, app_name)
        return self.application
