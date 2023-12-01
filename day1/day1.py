x
def read_digits(cur_dig):
    print("starting_read")
    length = len(cur_dig)
    ret_val = 0
    if length == 0:
        print("Huston, we have a problem!")
    elif length == 1:
        dig_val = int(cur_dig[0])
        ret_val = dig_val + (dig_val * 10)
    else:
        dig_val1 = int(cur_dig[0])
        dig_val0 = int(cur_dig[-1])
        ret_val = dig_val0 + (dig_val1 * 10)
    return ret_val

def strip_out_letters(line):
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    return digits

def sub_out_number_words(line):
    ret_line = line
    ret_line = ret_line.replace("eightwo", "82")
    ret_line = ret_line.replace("eighthree", "83")
    ret_line = ret_line.replace("twone", "21")
    ret_line = ret_line.replace("oneight", "18")
    ret_line = ret_line.replace("threeight", "38")
    ret_line = ret_line.replace("fiveight", "58")
    ret_line = ret_line.replace("nineight", "98")
    ret_line = ret_line.replace("one","1")
    ret_line = ret_line.replace("two","2")
    ret_line = ret_line.replace("three","3")
    ret_line = ret_line.replace("four","4")
    ret_line = ret_line.replace("five","5")
    ret_line = ret_line.replace("six","6")
    ret_line = ret_line.replace("seven","7")
    ret_line = ret_line.replace("eight","8")
    ret_line = ret_line.replace("nine","9")
    return ret_line



input_lines=[]

try:
    print("Copy and paste your input:")
    while True:
        line = input()
        input_lines.append(line)
        if line == "":
            break

    total_sum = 0
    for line in input_lines:
        current_num = 0
        if len(line) > 1:
            new_line = sub_out_number_words(line)
            print(f"line {line} newline {new_line}")
            digits = strip_out_letters(new_line)
            print(digits)
            reg_num = read_digits(digits)
            print(reg_num)
            total_sum += reg_num

    print(total_sum)

        
except:
    print(input_lines)
    print("Something Bad happened")
