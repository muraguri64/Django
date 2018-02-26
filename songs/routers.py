class SongsRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on songs models to 'songsdb'"
        if model._meta.app_label == 'songs':
            return 'songsdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on songs models to 'songsdb'"
        if model._meta.app_label == 'songs':
            return 'songsdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in songs app"
        if obj1._meta.app_label == 'songs' and obj2._meta.app_label == 'songs':
            return True
        # Allow if neither is songs app
        elif 'songs' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'songsdb' or model._meta.app_label == "songs":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True