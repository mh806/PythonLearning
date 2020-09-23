def greet(person, first_time=False):
    if first_time:
        return "First time, Welcome " + person
    return "Hello " + person


def greet_all(people):
    for person in people:
        print(greet(person, False))


friends = ["Bob", "William", "Huang"]
greet_all(friends)
# greet_all("William", "Huang", "Mengjia")
