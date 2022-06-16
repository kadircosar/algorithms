# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5


def parse_int(string):
    number = []
    dict_numbers_0 = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                      "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
                      "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
                      "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50",
                      "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90"}
    a_subset = [value for key, value in dict_numbers_0.items() if int(value) < 10]
    if string == "one million":
        return 1000000

    def set_number(numbers_1):
        if len(numbers_1) == 1:
            if len(numbers_1[0].split("-")) != 2:
                number.append(dict_numbers_0[numbers_1[0]])
            else:
                number.append(dict_numbers_0[numbers_1[0].split("-")[0]][0])
                number.append(dict_numbers_0[numbers_1[0].split("-")[1]])
        else:
            if numbers_1[1] == "hundred":
                number.append(dict_numbers_0[numbers_1[0]])
                if len(numbers_1) >= 3:
                    if len(numbers_1[2].split("-")) != 2:
                        if dict_numbers_0[numbers_1[2]] in a_subset:
                            number.append("0" + dict_numbers_0[numbers_1[2]])
                        else:
                            number.append(dict_numbers_0[numbers_1[2]])
                    else:
                        number.append(dict_numbers_0[numbers_1[2].split("-")[0]][0])
                        number.append(dict_numbers_0[numbers_1[2].split("-")[1]])
                else:
                    number.append("00")

    numbers = string.split()

    while 1:
        if "and" in numbers:
            numbers.remove("and")
        else:
            break

    if "thousand" in numbers:
        a = numbers[:numbers.index("thousand")]
        if not numbers[numbers.index("thousand") + 1:]:
            list_loop = [a]
        else:
            b = numbers[numbers.index("thousand")+1:]
            list_loop = [a, b]
        for elem in list_loop:
            if "hundred" not in numbers[numbers.index("thousand") + 1:]:
                number.append("00")
            set_number(elem)
        if not numbers[numbers.index("thousand") + 1:]:
            number.append("000")
        return int("".join(number))
    else:
        set_number(numbers)
        return int("".join(number))