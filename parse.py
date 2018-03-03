in_file = open("watch-history.html", "r")

vids = 0

line = in_file.readline()
while line != "":
	if "https://www.youtube.com/watch" in line:
		break
	line = in_file.readline()

in_file.close()

refs = line.split("href")
outstring = ""
for i in range(1, len(refs)):
	link = refs[i][2:45]
	outstring += link + "\n"
	vids+=1

print("You've watched:",vids,"videos!")

out_file = open("history.txt", 'wb')
out_file.write(bytes(outstring, "UTF-8"))

out_file.close()
