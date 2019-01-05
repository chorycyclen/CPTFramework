import importlib

from crossplatformtesting.core.exceptions import ImproperlyConfigured


class Settings:
    def __init__(self, settings_module):
        self.SETTINGS_MODULE = settings_module
        mod = importlib.import_module(self.SETTINGS_MODULE)

        tuple_settings = (
            "PLATFORMS",
        )
        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                if (setting in tuple_settings and
                        not isinstance(setting_value, (list, tuple))):
                    raise ImproperlyConfigured("The %s setting must be a list or a tuple. " % setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)
        if not self.PLATFORMS:
            raise ImproperlyConfigured("The PLATFORMS setting must not be empty.")

