from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'
    ready_has_run = False
    count = 0 
    
    def ready(self):
        if self.ready_has_run:return 
        self.count += 1
        print(self.count)
        print("Django has stareted!")
        ready_has_run = True