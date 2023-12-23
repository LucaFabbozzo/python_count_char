from pprint import pprint

# 1. Remove withespace from a string and return a list with the remaining characters.(use list comprehension)
# 2. Count in a dictionary how many characters in a string are repeated
# 3. Sort the keys of a dictionary by their value and return a list containing tuples [("a", 3), ("b", 2),("c", 4), ("d", 4)]
# 4. from a list of tuples, return those with the highest value [("a", 3), ("b", 2),("c", 4), ("d", 4)] -> [("c", 4), ("d", 4)]
# 5. Create a message that says: The characters that are repeated the most with 4 repetitions are: - C / - D (these characters must be with a capital letter)
# 6. Combine the solution from the previous exercises to find the most repeated characters in a string


string = "Hello world this is my string"


def remove_spaces(text):
    return [char for char in text if char != " "]



def character_count(list):
    chars_dict = {}
    for char in list:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict



def order(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse= True
    )



def greatest_tuples(list):
    max = list[0][1]
    answer = {}
    for orden in list:
        if max > orden[1]:
            break
        answer[orden[0]] = orden[1]
    return answer


def create_message(dict):
    message = "what is repeatet the most are: \n"
    for key, val in dict.items():
        message += f"-{key} with {val} repetitions \n"
    return message


without_spaces = remove_spaces(string)
counted = character_count(without_spaces)
organized = order(counted)
greater = greatest_tuples(organized)
message = create_message(greater)



pprint(counted, width=1)
print(organized)
print(greater)
print(message)