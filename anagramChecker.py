from collections import Counter

inp1 = input("Enter String: ")
inp2 = input("Enter String: ")

if Counter(inp1) == Counter(inp2):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
