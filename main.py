'''
Workshop problem for the Chipy 2017 Spring Mentorship Program.
April 20, 2017
'''

from operator import itemgetter
from collections import deque


class TeamBuilder(object):
    def __init__(self):
        self.people = {}

    def add_person(self):
        '''
        Add a person to the people dictionary.
        '''
        try:
            person, lines = input('add a <person> <lines of code>: ').split()
            self.people[person] = int(lines)
        except ValueError:
            print("Incorrect format. Person not added. Please enter this person again.")

    def create_teams(self):
        '''
         Sort people by lines of code and then pop 2 people from each end to form a team.
         If there are less than for people they will be a one team. This will make try
         to make groups of 4 by poping two people from the left and the right. If there
         are less than 5 people in the deque, the people will make a group.
         This should avoid having a group of one if there are more than 4 people.
        '''
        sorted_people = sorted(self.people.items(), key=itemgetter(1))
        d = deque((i[0] for i in sorted_people))
        teams = []
        while len(d) > 5:
            teams.append([d.popleft(), d.popleft(), d.pop(), d.pop()])
        if d:
            teams.append(list(d))
        return teams

if __name__ == '__main__':
    t = TeamBuilder()
    while input('Add another person(Y/N): ').lower()[0] == 'y':
        t.add_person()

    print(t.create_teams())
    