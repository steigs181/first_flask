# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    DB = 'first_flask'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # CRUD METHODS

    # CREATE
    @classmethod
    def save (cls, data):
        query = """ 
                INSERT INTO friends (first_name, last_name, occupation)
                VALUES (%(first_name)s, %(last_name)s, %(occupation)s)
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    #READ 
    @classmethod
    def get_one(cls, id):
        query = """
                SELECT * FROM friends WHERE ID = %(id)s
        """
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM friends;
                """
        all_friends = []
        results = connectToMySQL(cls.DB).query_db(query)
        for row in results:
            all_friends.append(cls(row))
        return all_friends

    # UPDATE 
    @classmethod
    def update(cls,data):
        query = """
                UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(idk)s
                """
        results = connectToMySQL(cls.DB).query_db(query)
        return results
        
    # DELETE
    @classmethod
    def delete(cls, id):
        query = """
                DELETE FROM friends
                WHERE ID = %(id)s
                """
        results = connectToMySQL(cls.DB).query_db(query, {'id': id})
        return results