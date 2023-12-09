# Developed by: Nemanja Radojkovic, www.linkedin.com/in/radojkovic

from gunicorn.app.base import BaseApplication
import logging

logger = logging.getLogger(__name__)


class CustomGunicorn(BaseApplication):
    def __init__(self, app, **options):
        self.options = options.copy()
        self.application = app

        super().__init__()

    def load_config(self):
        # Default load_config from gunicorn customization documentation
        # we didn't change anything here
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
