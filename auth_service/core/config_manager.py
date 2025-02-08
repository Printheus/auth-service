import importlib


class ConfigManager:
    def __init__(self) -> None:
        mod = importlib.import_module("core.config")
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)


    @property
    def db_conf(self):
        return self.DATABASE

conf = ConfigManager()