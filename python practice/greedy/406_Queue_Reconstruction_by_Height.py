# 406. Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
import copy


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        print people
        people = sorted(people, key=lambda x: -x[0])
        print people
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


    def reconstructQueue2(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people is None or people == []:
            return []
        temp_people = copy.deepcopy(people)
        people = list(enumerate(people))
        rst = []
        while people:
            choice = min([item for item in people if item[1][1] == 0], key=lambda x: x[1][0])
            rst.append(temp_people[choice[0]])
            people.remove(choice)
            for person in people:
                if person[1][0] <= choice[1][0]:
                    person[1][1] -= 1
        return rst


print Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
