import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(numUsers):
            self.addUser(f'{i}')
        # Create friendships
        possible_friendships = []
        for user in self.users:
            for friend in range(user+1, self.lastID+1):
                possible_friendships.append((user, friend))

        random.shuffle(possible_friendships)
        for friendship in range(avgFriendships*numUsers//2):
            friendship_pair = possible_friendships[friendship]
            self.addFriendship(friendship_pair[0], friendship_pair[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # bfs
        queue = deque()
        queue.append([userID])
        while len(queue) > 0:
            path = queue.popleft()
            vertex = path[-1]
            if vertex not in visited:
                visited[vertex] = path
                for friendship in self.friendships[vertex]:
                    path_new = path[:]
                    path_new.append(friendship)
                    queue.append(path_new)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
