# CPT Framework Foundation
import importlib

from compatibilitytest.core.exceptions import ImproperlyConfigured
from . import global_settings


class Settings:
    """Project settings handler"""

    def __init__(self, settings_module):
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))

        self.settings_module = settings_module
        mod = importlib.import_module(self.settings_module)

        tuple_settings = (
            "PLATFORMS",
        )
        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                if (setting in tuple_settings and
                        not isinstance(setting_value, (list, tuple))):
                    raise ImproperlyConfigured(
                        "The %s setting must be a list or a tuple. " % setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)
        if not self.PLATFORMS:
            raise ImproperlyConfigured(
                "The PLATFORMS setting must not be empty.")

    def is_overridden(self, setting):
        """
        check setting is overridden
        """
        return setting in self._explicit_settings

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self.settings_module,
        }
