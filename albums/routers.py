class AlbumsRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on albums models to 'albumsdb'"
        if model._meta.app_label == 'albums':
            return 'albumsdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on albums models to 'albumsdb'"
        if model._meta.app_label == 'albums':
            return 'albumsdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in albums app"
        if obj1._meta.app_label == 'albums' and obj2._meta.app_label == 'albums':
            return True
        # Allow if neither is albums app
        elif 'albums' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'albumsdb' or model._meta.app_label == "albums":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True