import random as rand
import webbrowser

in_file = open("history.txt", 'r')

links = []

line = in_file.readline()
while line != "":
	links.append(line)
	line = in_file.readline()

in_file.close()

seed = rand.randint(0, len(links))

webbrowser.open_new_tab(links[seed])
