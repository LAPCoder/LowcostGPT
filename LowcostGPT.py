################################################################################
# INCLUDES (yes, I know it's import)                                           #
################################################################################
import os
import random

################################################################################
# VARIABLES & CONSTANTS                                                        #
################################################################################
LANGUAGES = [i.removesuffix(".txt") for i in next(os.walk("./lang"), (None, None, []))[2]]
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

################################################################################
# FUNCTIONS                                                                    #
################################################################################
def get_random_code():
	with open("./lang/" + random.choice(next(os.walk("./lang"), (None, None, []))[2]), 'r') as file:
		lines = [line for line in file]
	code = []
	line: str
	acc_count = 0
	vars_name = ["undef_error_"+"".join(random.choices(CHARS, k=5))]
	for line in random.choices(lines, k=random.randint(10, 97)): # ChatGPT like to stop code generating just before 100 lines
		if not "$" in line:
			code.append(line)
			break
		start_search = 0
		tmp_var_name = None
		while True:
			start_search = line.find("$", start_search)
			if line[start_search+1] == "$":
				start_search += 1
				continue
			if line.find("$", start_search) == -1:
				break
			part = line[start_search+1:].partition("$")
			match part[0]:
				case "rand":
					char = random.choices(CHARS, k=random.randint(1, 50))
					line = line[:start_search] + "".join(char) + part[2]
					start_search += len(char) + 2
				case "num":
					num = random.randint(0, 4184155)
					line = line[:start_search] + str(num) + part[2]
					start_search += len(str(num)) + 2
				case "{":
					acc_count+=1
					line = line[:start_search] + "{" + part[2]
				case "var_decl":
					char = random.choices(CHARS, k=random.randint(1, 10))
					line = line[:start_search] + "".join(char) + part[2]
					start_search += len(char) + 2
					vars_name.append(char)
					tmp_var_name = char
				case "var":
					if tmp_var_name == None:
						char = random.choice(vars_name)
					else:
						char = tmp_var_name
					line = line[:start_search] + "".join(char) + part[2]
					start_search += len(char) + 2
				case _:
					start_search += 1
		code.append(line)
	code.append("}\n" * acc_count)
	return code

################################################################################
# MAIN                                                                         #
################################################################################
print("Hi! I'm LowcostGPT! What do you want to do?")
answer = ""
while answer == "":
	answer = input("> ")
print("Sorry but I'm no 'LowcostChat', so you can't gimme orders.")
print("I'll do something in", random.choice(LANGUAGES) + ".")
print("".join(get_random_code()), end="")
