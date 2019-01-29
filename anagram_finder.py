# Anagram finder:
#
# Given a word, finds all words in a dictionary that can be constructed by re-arranging 
# the word's letters. By word, we mean a sequence of characters that does not contain whitespace.
# The letters are not case sensitive in the input, but the case should be maintained in the output.
# The dictionary is specified as a string which contains arbitrary number of words.
#

from typing import Iterable
from itertools import permutations


# This is the words dictionary, do not modify
WORDS_DICTIONARY = """
    bal
    lab   blab alba baal Bala ranged ranged
    pole lope Opel Olpe
    bear bare danger garden
        ranged
"""

class AnagramFinder:
    
    # TODO implement
    # feel free to change the API if it makes sense      

    def find_anagrams(self, word: str) -> Iterable[str]:
        test = WORDS_DICTIONARY.split(' ')
        test.remove('\n')
        test.remove('')
        test_final = [x.split('\n')[0] for x in test if x]
        
        # Converting all words of the cleaned word dictionary to lower case
        test_lower = [x.lower() for x in test_final]
        
        # Creating another Dictionary to match the lower case words to the actual words of Words Dictionary
        test_dict = {x.lower() : x for x in test_final}
        
        # Anagram Algorithm
        ans = [] # To store the anagrams
        
        for i in test_lower:
            
            if i == word: # Neglect the same word
                continue
            
            if len(i) == len(word):
                
                i_list = [x for x in i]
                i_list.sort()
                word_list = [x for x in word]
                word_list.sort()
                
                if i_list == word_list:
                    ans.append(test_dict[i])
                    
            else:
                continue
            
        # Sort the Anagrams Alphabetically    
        ans.sort()
        
        return list(set(ans)) # To ensure same anagrams are not repeated

        
def test_anagram_finder():
    finder = AnagramFinder()

    result1 = sorted(finder.find_anagrams("bal"))
    test1 = result1 == ["lab"]

    if test1:
        print("test1 passed")
    else:
        print("test1 failed", result1)

    result2 = sorted(finder.find_anagrams("danger"))
    test2 = result2 == ["garden", "ranged"]

    if test2:
        print("test2 passed")
    else:
        print("test2 failed", result2)

    result3 = sorted(finder.find_anagrams("lope"))
    test3 = result3 == ["Olpe", "Opel", "pole"]

    if test3:
        print("test3 passed")
    else:
        print("test3 failed", result3)


test_anagram_finder()
