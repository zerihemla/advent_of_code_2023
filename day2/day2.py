

MAX_GREEN = 13
MAX_BLUE = 14
MAX_RED = 12


cur_game_num = 0
valid_game_sum = 0
invalid_game_sum = 0
color_power_sum = 0

max_seen_green = 0
max_seen_blue = 0
max_seen_red = 0



input_file_string = "input.txt"


def increment_counters(invalid_game, game_num):
	global invalid_game_sum, valid_game_sum
	if invalid_game == True:
		invalid_game_sum += game_num
	else:
		valid_game_sum += game_num


def is_game_valid(rounds_list):
	invalid_game = False	
	
	max_red_seen = 0
	max_green_seen = 0
	max_blue_seen = 0

	for cur_round in rounds_list:
		shown_list = cur_round.split(",")
		red_count = 0
		blue_count = 0
		green_count = 0

		for shown in shown_list:
			print(shown)
			

			if "red" in shown:
				red_count = int(shown.replace(" red", ""))

			elif "blue" in shown:
				blue_count = int(shown.replace(" blue", ""))

			elif "green" in shown:
				green_count = int(shown.replace(" green", ""))

			else:
				print(f"FOUDND SOMETHING BAD IN SHOWN! {shown}")

		print(f"red: {red_count} blue: {blue_count} green: {green_count}")	
		print("\n")



		if red_count > MAX_RED:
			invalid_game = True

		if blue_count > MAX_BLUE:
			invalid_game = True

		if green_count > MAX_GREEN:
			invalid_game = True

		if red_count > max_red_seen:
			max_red_seen = red_count

		if blue_count > max_blue_seen:
			max_blue_seen = blue_count

		if green_count > max_green_seen:
			max_green_seen = green_count

	return invalid_game, max_red_seen, max_blue_seen, max_green_seen



def parse_line(line):
	game_string = line.split(":")[0]
	rounds_strings = line.split(":")[1]
	rounds_list = rounds_strings.split(";")

	game_int = int(game_string.replace("Game ", ""))

	return game_int, rounds_list


def parse_whole_file():
	lines = []
	with open(input_file_string, "r") as file:
		lines = [line.rstrip('\n') for line in file]
	return lines




def main():
	global invalid_game_sum, valid_game_sum, color_power_sum
	lines = parse_whole_file()
	for line in lines:
		max_red_seen = 0
		max_green_seen = 0
		max_blue_seen = 0
		game_num, rounds_list = parse_line(line)
		invalid_game, max_red_seen, max_blue_seen, max_green_seen = is_game_valid(rounds_list)
		increment_counters(invalid_game, game_num)
		color_power_sum += (max_red_seen * max_blue_seen * max_green_seen)

	print(f"Invalid Game Sum: {invalid_game_sum}   Valid Game Sum: {valid_game_sum}")
	print(f"Color Power Sum: {color_power_sum}")




if __name__ == "__main__":
	main()