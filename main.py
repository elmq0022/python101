from operator import itemgetter
from collections import deque


class TeamBuilder(object):
    def __init__(self):
        self.people = {}

    def addPerson(self):
        try:
            person, lines = input('add a <person> <lines of code>: ').split()
            self.people[person] = int(lines) 
        except:
            print("Incorrect format. Person not added please enter again.")

    def create_teams(self):
        sorted_people = sorted(self.people.items(), key=itemgetter(1))
        d = deque((i[0] for i in sorted_people))

        teams = []
        while len(d) > 4:
            teams.append([d.popleft(), d.popleft(), d.pop(), d.pop()])
        if d:
            teams.append(list(d))

        return teams

if __name__ == '__main__':
    t = TeamBuilder()
    while input('Add another person(Y/N): ').lower()[0] == 'y':
        t.addPerson()

    print(t.create_teams())
    