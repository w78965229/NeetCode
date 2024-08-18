'''
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

'''


def isAnagram( s, t) :
    '''解法一'''
    # set_s = set(s)
    # set_t = set(t)
    #
    # if set_s != set_t:
    #     return False
    #
    # for i in set_s:
    #     if s.count(i) != t.count(i):
    #         return False
    #
    # return True
    '''解法二'''
    if len(s) != len(t):
        return False

    countS={}
    countT={}
    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i],0)

        countT[t[i]] = 1+countT.get(t[i],0)

    return countT == countS


def main():
    s = "x"
    t = "xx"

    flag=isAnagram(s,t)
    print(f"flag='{flag}'")
if __name__ == "__main__":
    main()


