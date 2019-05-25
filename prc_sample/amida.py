#!/usr/bin/python
import random
import sys

lines = ["|---|   |   |   |","|   |---|   |   |","|   |   |---|   |","|   |   |   |---|"]
goal =  ["x                ","    x            ","        x        ","                x"]

lines1 = ["|-| | |","| |-| |","| | |-|"]
goal1 =  ["x      ","  x    ","    x  ","      x "]


cross_buf = []
counter = 1
title = "\
\n\
    ______   __       __  ______  _______    ______  \n\
   /      \ /  \     /  |/      |/       \  /      \ \n\
  /$$$$$$  |$$  \   /$$ |$$$$$$/ $$$$$$$  |/$$$$$$  |\n\
  $$ |__$$ |$$$  \ /$$$ |  $$ |  $$ |  $$ |$$ |__$$ |\n\
  $$    $$ |$$$$  /$$$$ |  $$ |  $$ |  $$ |$$    $$ |\n\
  $$$$$$$$ |$$ $$ $$/$$ |  $$ |  $$ |  $$ |$$$$$$$$ |\n\
  $$ |  $$ |$$ |$$$/ $$ | _$$ |_ $$ |__$$ |$$ |  $$ |\n\
  $$ |  $$ |$$ | $/  $$ |/ $$   |$$    $$/ $$ |  $$ |\n\
  $$/   $$/ $$/      $$/ $$$$$$/ $$$$$$$/  $$/   $$/ \n\
\n\
\n\
\n\
   __    __  __    __     _____  ______              \n\
  /  |  /  |/  |  /  |   /     |/      |             \n\
  $$ | /$$/ $$ |  $$ |   $$$$$ |$$$$$$/              \n\
  $$ |/$$/  $$ |  $$ |      $$ |  $$ |               \n\
  $$  $$<   $$ |  $$ | __   $$ |  $$ |               \n\
  $$$$$  \  $$ |  $$ |/  |  $$ |  $$ |               \n\
  $$ |$$  \ $$ \__$$ |$$ \__$$ | _$$ |_              \n\
  $$ | $$  |$$    $$/ $$    $$/ / $$   |             \n\
  $$/   $$/  $$$$$$/   $$$$$$/  $$$$$$/              \n\
  						\n\
\n\
ex)\n\
1 2 3 4\n\
| |-| |\n\
| | |-|\n\
|-| | |\n\
|-| | |\n\
x\n\
INPUT:1"

print(title)

def create_lines(buf):
	for i in range(6):
		cross = random.randrange(4)
		print(lines[cross])
		buf.append(cross)


def create_lines1(buf):
        for i in range(5):
                cross = random.randrange(3)
                print(lines1[cross])
                buf.append(cross)




def amida():

	cross_buf=[]
	print(str(counter) + "/100")
#	counter = counter + 1
	print("1   2   3   4   5")
	create_lines(cross_buf)
	goal_point = random.randrange(1,6)
	print(goal[goal_point-2])

#	print(goal_point)
	ans = goal_point
	for i in range(5,-1,-1):
#		print(i)

		if(cross_buf[i] == (ans-2)):
			ans = ans - 1
		elif(cross_buf[i] == (ans-1)):
			ans = ans + 1

#	print(cross_buf)
#	print(ans)
	print("INPUT:")
	in_ans = input()
	if(in_ans == ans):
		print("SUCCSESS!")
	else:
		print("FAILED!")
		exit()

def amida1():

        cross_buf=[]
        print(str(counter) + "/100")
#       counter = counter + 1
        print("1 2 3 4")
        create_lines1(cross_buf)
        goal_point = random.randrange(1,5)
        print(goal1[goal_point-1])

#       print(goal_point)
        ans = goal_point
        for i in range(4,-1,-1):
#               print(i)

                if(cross_buf[i] == (ans-2)):
                        ans = ans - 1
                elif(cross_buf[i] == (ans-1)):
                        ans = ans + 1

#       print(cross_buf)
#       print(ans)
        print("INPUT:")
        in_ans = input()
        if(in_ans == ans):
                print("SUCCSESS!")
        else:
                print("FAILED!")
                exit()




for i in range(100):
	if counter >= 50:
		amida()
	else:
		amida1()
	counter = counter + 1
#amida()

print("FLAG{DAMMY}")

