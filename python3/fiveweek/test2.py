from string import *
def hp():
	return "Happy Birthday"

def hpty():
	print("{} to you!".format(hp()))

def say(person):
	# name=input("please to input your name:")
	hpty()
	hpty()
	print("{},dear {}!".format(hp(),person))
	hpty()
	print()

def main():
	say("Mike")
	say("Lily")
	say("Maya")

main()	