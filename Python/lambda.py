people = [
  {"name": "harry", "house": "gryffindor"},
  {"name": "cho", "house": "ravenclaw"},
  {"name": "draco", "house": "slytherin"}
]


def f(person):
  return person["house"]


people.sort(key=f)

people.sort(key=lambda person: person["name"])

print("check out")

print(people)
