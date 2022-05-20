from faker import Faker
from nameko.rpc import rpc

fake = Faker()


class PeopleListService:
    name = "peoplelist"

    @rpc
    def populate(self, number=20):
        names = []
        for _ in range(0, number):
            n = fake.name()
            names.append(n)
        return names
