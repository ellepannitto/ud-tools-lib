import argparse

def levelchecker(level):

	level = int(level)
	if level < 1 or level > 5:
		raise argparse.ArgumentTypeError(f"'{level}' is not a valid option. "
								   		"It must be an integer between 1 and 5 (included)")
	return level