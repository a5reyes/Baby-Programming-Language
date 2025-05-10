# COMP 340
# Albert Reyes
# github - a5reyes
import re
def decipher(babyExp):
    srcCode = ""
    res_nums = []
    final_nums = []
    babyWords = {"pee": "+", "gah":"-", "milk": "*", "heh":"/", 
                 "mama":"(", "dada":")"}
    # removing whitespaces
    babyExp = "".join(babyExp.split())
    # find operator in expression in order of appearance in baby
    ops = [val for key, val in babyWords.items() if key in babyExp]
    if ops:
        # find operator value in babyWords
        keys = [key for op in ops for key, value in babyWords.items() if value == op]
        # split terms in expression by operator-keys while keeping operator-keys in expression
        pattern = "(" + "|".join(map(re.escape, keys)) + ")"
        problem = re.split(pattern, babyExp)
        problem = [x for x in problem if x.strip()]
        # split jammed parts
        new_problem = []
        for word in problem:
            mod = False
            for key in keys:
                if key in word and word != key:
                    parts = re.split(f"({re.escape(key)})", word)
                    new_problem.extend([p for p in parts if p])
                    mod = True
                    break
            if not mod:
                new_problem.append(word)
        # removing empty strings from problem caused by splitting jammed parts
        problem = [x for x in new_problem if x.strip()]
        # if babyWord-number is multiple digits
        for i, value in enumerate(problem):
                if value.count("b") > 1:
                    # find sub-babyword that start with 'b' and go until next 'b'
                    split_parts = re.findall(r'b[^b]*', value)
                    # replace current babyword with all of its split sub-babyword parts
                    problem[i:i+1] = split_parts 
        # index_dict is a dictionary used like a position-character tracker for each term, their index and their char 
        index_dict = {(index, value): None for index, value in enumerate(problem)}
        # add the operator and its index to position-character tracker
        for (i, v), val in index_dict.items():
            if v in babyWords.keys():
                index_dict[(i, v)] = babyWords[v]
        # converter - problem is babyExp turned into list
        for value in problem:
            if value in babyWords.keys():
                continue
            # creating dictionary for word so we can count 'b' letters and 'a' letters
            word_dict = {index: letter for index, letter in enumerate(value)}
            for key, value in word_dict.items():
                if value == "b":
                    res = 0
                else:
                    # length of word - 'b' letter
                    try:
                        res += ((len(word_dict)) - key)
                    except:
                        raise ValueError("Must input more than one num with operator")
                res_nums.append(res)
        # getting length of word which is the first element right to elements that equal 0 (aka letter 'b')
        for res_num in range(len(res_nums)):
            if res_nums[res_num] == 0:
                if res_num + 1 < len(res_nums):
                    final_nums.append(res_nums[res_num + 1])
                # if last element equals 0 aka equals 'b' letter, then, its a double digit number
                else:
                    final_nums.append(0)
        # updating none values from index_dictionary with the list of numbers
        for num in final_nums:
            for (i, v), val in index_dict.items():
                if index_dict[(i, v)] == None:
                    index_dict[(i, v)] = num
                    break
        # adding values from index_dictionary to srcCode string 
        for (i, v), val in index_dict.items():
            if index_dict[(i,v)] == None:
                index_dict[(i,v)] = 0
            srcCode += str(index_dict[(i,v)])
        return srcCode

    # single number entered
    else:        
        separator = "b"
        escaped_sep = re.escape(separator)
        pattern = f"({escaped_sep})"
        problem = re.split(pattern, babyExp)
        for i, value in enumerate(problem):
                if value.count("b") > 1:
                    split_parts = re.findall(r'b[^b]*', value)
                    problem[i:i+1] = split_parts 
        problem = [x for x in problem if x.strip()]
        for value in problem:
            if value in babyWords.keys():
                continue
            word_dict = {index: letter for index, letter in enumerate(value)}
            for key, value in word_dict.items():
                if value == "b":
                    res = 0
                else:
                    try:
                        res += (len(word_dict) - key)
                    except:
                        raise ValueError("Must input more than one num with operator") 
                res_nums.append(res)
        for res_num in range(len(res_nums)):
            if res_nums[res_num] == 0:
                if res_num + 1 < len(res_nums):
                    final_nums.append(res_nums[res_num + 1])
                else:
                    final_nums.append(0)
        if final_nums == []:
            final_nums = [0]
        srcCode = "".join([str(final_num) for final_num in final_nums])
        return srcCode