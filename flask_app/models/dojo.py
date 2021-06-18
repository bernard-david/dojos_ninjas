from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT first_name, last_name, age FROM ninjas JOIN dojos ON dojos.id=ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = results
        return dojo

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results[0]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(new_dojo)s, NOW(), NOW())"
        dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return dojo_id