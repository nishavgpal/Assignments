

credentials={}

class DBoperations (object):
    def db_call_register(self, name, password):
        credentials[name] = password
        return True