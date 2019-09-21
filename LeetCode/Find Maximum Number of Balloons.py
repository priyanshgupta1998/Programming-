https://leetcode.com/contest/weekly-contest-154/problems/maximum-number-of-balloons/


Q. Find Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.


Sol:--> 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #Using hash counter 
        hash = {'b':0, 'a':0, 'l':0 , 'o':0, 'n':0};
        for i in text:
            if hash.get(i) != None:
                hash[i] += 1
        #print(hash)
        num = hash.get('b');
        
        if num >= hash.get('a'):
            num = hash.get('a')
        
        if num >= hash.get('l')//2:
            num = hash.get('l')//2;
        
        if num >= hash.get('o')//2:
            num = hash.get('o')//2;
        
        if num >= hash.get('n'):
            num = hash.get('n');
        
        return num
