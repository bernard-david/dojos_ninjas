from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT ninjas.id , first_name, last_name, age, ninjas.created_at, ninjas.updated_at, dojos.id as dojo_id, name, dojos.created_at as dojo_created_at, dojos.updated_at as dojo_updated_at FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id;"
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query)
    #     ninjas = []
    #     for result in results:
    #         ninja = cls(result)
    #         dojo_data = {
    #             "id": result['dojo_id'],
    #             "name": result['name'],
    #             "created_at": result['created_at'],
    #             "updated_at": result['updated_at']
    #         }
    #         ninja.dojo = dojo.Dojo(dojo_data)
    #         ninjas.append(ninja)
    #     return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_name)s, NOW(), NOW())"
        ninja_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        return ninja_id
