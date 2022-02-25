

base = 16                       # Establishes hexadecimal as the base
power_dict = {

}                               # creates the dictionary to hold powers of 16 that the user's chosen number will be compared against

dividend = int(input("Choose a number to convert to Hex "))     # The user's number, converted from string to integer

scope = len(str(dividend))                  # Sets the variable for range to equal the place value of the chosen number, measured as a string.
                                            # should work for bases 10 and up.
print(scope)

for i in range(scope):                      # generates entries for power dictionary by iterating equal to the scope which is also used as the exponent value
    power_dict[i] = base ** i               # because indices in dict's start at 0.
print(power_dict)


def checker(dividend):                      # Compares user selection to base 16 exponents in dictionary and chooses the correct one to divide by. Iterates through dict.
    for j in power_dict:
        if dividend < power_dict[j]:        # If at any point the dividend becomes smaller than the dict entry value, it means we iterated over the correct value by
            return power_dict[j - 1]        # one step. Sets the value back one step, returns it, and ends the loop.
        elif dividend == power_dict[j]:     # If the user chooses an exact exponent of 16 like 256. A contingency case.
            return power_dict[j]            # Struggled here. Realized I didn't need to create a local variable "divisor = power_dict[i]" and could just return a result.
        else:
            pass                            # Numbers much smaller than the dividend can be skipped.
                                            # Because the divisor is sorting between smaller (yes) and much smaller (no) it seemed prudent to compare transitions
                                            # rather than the numbers themselves. So this function looks for the moment the dict value switches from being
divisor = checker(dividend)                 # smaller than the dividend to being larger, the chooses the proximate smaller value.


def divider(dividend, divisor):             # Carries out the procedure for converting a dividend to hex, as I first learned it.
    storage = []                            # creates a list to put the quotients (and final remainder) into -- the numerical answer.
    while divisor > 1:                      # iterates process until divisor equals 1, the equivalent of 16^0, at which point it appends the remainder rather than quotient.
        storage.append(dividend // divisor) # divides and rounds down to eliminate floats, since conversion to hex is by list of whole numbers.
        dividend = dividend % divisor       # updates the value of dividend to equal the remainder for the next iteration
        divisor = divisor // 16             # steps down the value of the exponent one step for the next iteration.
        if divisor == 1:                    # ends loop when divisor equals 16^0
            storage.append(dividend)
    return storage                          # returns result


q_list = divider(dividend, divisor)


def converter(list):                        # Converts numerical list to alpha numerical list
    conversion = []                         # creates empty list to store answer
    for k in list:                          # iterates through list
        if k < 10:                          # i for i with values 0 - 9 that remain numerical in hex
            conversion.append(k)
        elif k == 10:                       # converts values to numeric hex equivalents.
            conversion.append("A")
        elif k == 11:
            conversion.append("B")
        elif k == 12:
            conversion.append("C")
        elif k == 13:
            conversion.append("D")
        elif k == 14:
            conversion.append("E")
        else:
            conversion.append("F")
    print(conversion)


converter(q_list)
