#!/usr/bin/python
import pexpect
import sys

lines = ["|-| | |","| |-| |","| | |-|"]
goal =  ["x      ","  x    ","    x  ","      x "]
goal_point = 0
cross_buf = []
get_lines = []

def list_append(lines,i):
	lines.append(prc.buffer[i]+prc.buffer[i+1]+prc.buffer[i+2]+prc.buffer[i+3]+prc.buffer[i+4]+prc.buffer[i+5]+prc.buffer[i+6])

def list_getter(buf,point,line_list):
	if(line_list[0] == goal[0]): point = 1
	elif(line_list[0] == goal[1]): point = 2
	elif(line_list[0] == goal[2]): point = 3
	else: point = 4

	for i in range(1,6):
		if(line_list[i] == lines[0]): buf.append(0)
 	        elif(line_list[i] == lines[1]): buf.append(1)
   	        elif(line_list[i] == lines[2]): buf.append(2)

#	print("goal_point:" + str(point))
#	print(buf)
	return point

def solver(prc):
#	counter = 1
	while True:
		try:
			prc.expect("/100\r\n1 2 3 4")
			#print(prc.buffer)
			get_lines = []
			cross_buf = []

			list_append(get_lines,47)
			list_append(get_lines,38)
			list_append(get_lines,29)
			list_append(get_lines,20)
			list_append(get_lines,11)
			list_append(get_lines,2)
			print(get_lines)

			ans = list_getter(cross_buf,goal_point,get_lines)

		#	print("goal_point:" + str(goal_point))
		#	print(cross_buf)


			for i in range(0,5):
				#print(i)
				if(cross_buf[i] == (ans-2)):
					ans = ans - 1
				elif(cross_buf[i] == (ans-1)):
					ans = ans + 1

		#	print("ans:" + str(ans))

			prc.expect("INPUT:")
			prc.sendline(str(ans))
		#	prc.expect("SUCCSESS!")

		#	prc.expect("FLAG")
#			print("counter:" + str(counter))
#			counter = counter + 1

		except:
			print("BREAK!")
#			pass
			break


#prc = pexpect.spawn("python target.py")
#prc.logfile = sys.stdout


#prc = pexpect.spawn("python target.py")
prc = pexpect.spawn("python target.py")
prc.logfile = sys.stdout

solver(prc)
#	prc.expect(r".*")
#	print(prc.after)
#	prc.expect(pexpect.EOF)

