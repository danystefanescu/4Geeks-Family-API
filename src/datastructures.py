from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {   
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [10, 14, 3]
            },
            {   
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return True

    def delete_member(self, id):
        holder = []
        for x in self._members:
            if x["id"] != id:
                holder.append(x)
        self._members = holder

    def get_member(self, id):
        for x in self._members:
            if x["id"] == id:
                return x    

    def get_all_members(self):
        return self._members
