"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        alphabet = 26
        numbers = 10
        result = 1
        c = 0
        for x in range(0,3):
            if str[x]!=".":
                c+=1
        alphabet -= c
        
        for x in range(0,3):
            if str[x] == ".":
                result *= alphabet
                alphabet -= 1
        
        k=0   
        for x in range(3,7):
            if str[x]!=".":
                k+=1
        numbers -= k
        for x in range(3,7):
            if str[x]==".":
                result *= numbers
                numbers -= 1
        return result

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()