class AuthRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on auth models to 'authdb'"
        if model._meta.app_label == 'auth':
            return 'authdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on auth models to 'authdb'"
        if model._meta.app_label == 'auth':
            return 'authdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in auth app"
        if obj1._meta.app_label == 'auth' and obj2._meta.app_label == 'auth':
            return True
        # Allow if neither is auth app
        elif 'auth' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'authdb' or model._meta.app_label == "auth":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True