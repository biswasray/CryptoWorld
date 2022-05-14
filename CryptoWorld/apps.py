from django.apps import AppConfig
class MyAppConfig(AppConfig):
    name = 'CryptoWorld'
    verbose_name = "My Application"
    def ready(self):
        print("Server start")