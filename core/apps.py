from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
<<<<<<< HEAD
=======
    
    def ready(self):
        from . import signals
>>>>>>> 93a9b19... Long Time no C
