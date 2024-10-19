# Singleton Pattern - Defines the configuration manager class with a static method to access the unique instance

class ConfigurationManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigurationManager._instance is None:
            ConfigurationManager._instance = ConfigurationManager()
        return ConfigurationManager._instance

    def __init__(self):
        # Initialize configuration settings
        self.settings = {
            "language": "English",
            "theme": "Dark",
            "timezone": "UTC"
        }

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value


# Client Code
if __name__ == "__main__":
    # Access the configuration manager
    config_manager1 = ConfigurationManager.get_instance()
    config_manager2 = ConfigurationManager.get_instance()

    # Both instances point to the same object
    print(config_manager1 is config_manager2)  # Output: True

    # Get and set configuration settings
    config_manager1.set_setting("timezone", "GMT+1")
    print(config_manager2.get_setting("timezone"))  # Output: GMT+1
