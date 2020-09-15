'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import re
def count_th(word):
    # Start count of occurences of 'th'
    count = 0
    # TBC
    if len(word) < 2:
        return 0
      
    # identify the target            
    # set index for each letter
    elif 'th' in word:
        if word[0] == 't' and word[1] == 'h':
            count += 1
    # iterate through string & increment count
    return count_th(word[1:]) + count

    
    # target = 'th'
    # res = [i.start() for i in re.finditer(target, word)]
    # return res

    # target = 'th'
    # if word.count(target, 0, -1):
    #     count += 1
    # return count

    # search for the target 
    # total = word.count(target, 0, -1)
    # # increase the counter                 
    # # return total
    # count_th(total)

    # if word[:2] == "th":
    #     return 1 + count_th(word[2:])
    # else:
    #     return count_th(word[1:])
   
if __name__ == '__main__':
    word = "abcthefthghith"
    print(count_th(word))  
