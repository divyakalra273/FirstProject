# class Student:
#
#     def __init__(self, roll, name, age):
#         self.roll = roll
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "{}\t{}\t{}".format(self.roll, self.name, self.age)
#
#
# s1 = Student(101, "John", 22)
# s2 = Student(311, "Jen", 24)
# s3 = Student(432, "Jim", 27)
# s4 = Student(191, "Jack", 19)
# s5 = Student(715, "Joe", 21)


# print(id(s1))
class Team:
    def __init__(self,year, teamName, matches, won, lost, tied, abandoned, points, netRunRate, forScore, againstScore):
        self.year=year
        self.teamName = teamName
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.netRunRate = netRunRate
        self.forScore = forScore
        self.againstScore = againstScore

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.year,self.teamName, self.matches, self.won, self.lost, self.tied,
                                                        self.abandoned, self.points, self.netRunRate, self.forScore,
                                                        self.againstScore)


    def readOrders(self):
        file = open("IPL-TEAMS-2019", "r")
        lines = file.readlines()  # List of Lines
        # print(lines)
        # print(type(lines))
        for line in lines:
            data = line.split(",")
        team = Team(data[1], data[2], int(data[3]))
        # order.oid = int(data[0])
        team.showOrderDetails()

        file.close()

from HashTable import HashTable
hTable = HashTable(15)
# hTable.put(s1)
# hTable.put(s2)
# hTable.put(s3)
# hTable.put(s4)
# hTable.put(s5)

# hTable.iterate()
