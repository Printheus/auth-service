import importlib


class ConfigManager:
    def __init__(self) -> None:
        mod = importlib.import_module("auth_service.core.config")
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)


    @property
    def db_conf(self):
        return self.DATABASE

    @property 
    def private_key(self):
        with open(self.PRIVATE_KEY, "r") as pk_file:
            pk = pk_file.read()
        return pk
    @property 
    def public_key(self):
        with open(self.PUBLIC_KEY, "r") as pk_file:
            pk = pk_file.read()
        return pk


conf = ConfigManager()