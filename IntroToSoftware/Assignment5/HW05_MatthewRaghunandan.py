def list_copy(lst):
    return [element for element in lst] #go through each element and add to new list

def list_intersect(l1, l2):
    return [element for element in l1 if element in l2] #go through each element in l1 and check if it is in l2

def list_difference(l1, l2):
    return [element for element in l1 if element not in l2] #go through each element in l1 and check if it is not in l2

def remove_vowels(string):
    return ' '.join([word for word in string.split() if word[0].lower() not in 'aeiou']) #go through each word in the string and check if the first letter is a vowel

def check_pwd(password):
    return (
        len([c for c in password if c.isupper()]) >= 2 and
        len([c for c in password if c.islower()]) >= 1 and
        password[0].isdigit()
    ) # check if there are at least 2 uppercase letters, 1 lowercase letter, and the first character is a digit

def reorder(l):
    sorted_list = []
    for i in l:
        # Find the position where element i should be inserted
        for j in range(len(sorted_list)):
            if i < sorted_list[j]:
                sorted_list.insert(j, i)
                break
        else:
            # If not inserted, append to the end of the list
            sorted_list.append(i)
    return sorted_list 
