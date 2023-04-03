import numpy as np
import math

def starting(_map):
	row=0
	column=0
	start=[]
	for area in _map:
		for point in area:
			if _map[row][column]==0:
				start=[row,column]
				break
			column=column+1
		column=0
		row=row+1
	return start



def find_pos(_map):
	_map=_map
	pos=[]
	bag=[]
	row=0
	column=0
	for _rowm in _map:
		for _colm in _rowm:
			bag=[row,column]
			pos.append(bag)
			column=column+1
			

		row=row+1
		column=0
	
	for item in list(pos):
		if type(_map[item[0]][item[1]])==str:
			#print(_map[item[0]][item[1]])
			pos.remove(item)

	return pos

def move(_map):
	_map1=_map
	unvisited_p=find_pos(_map)
	#print(unvisited_p)
	current_p=starting(_map)
	#print(current_p)
	dist_fix=0
	dist_comp=0
	temp_dest=[]

	#initiateRandom_pos
	for pos in unvisited_p:
		if pos!=current_p:
			dist_fix=np.subtract(pos,current_p)
			dist_fix=math.sqrt(((dist_fix[0])**2)+((dist_fix[1])**2))
			break

	for pos in unvisited_p:

		if pos!=current_p:
			dist_comp=np.subtract(pos,current_p)
			dist_comp=math.sqrt((dist_comp[0]**2)+(dist_comp[1]**2))

			if dist_comp<dist_fix:
				temp_dest=[]
				temp_dest.append(pos)i
				p_comp=pos
			elif dist_comp==dist_fix:
				temp_dest.append(pos)
		else:
			continue
	
	print(temp_dest)
	

_map=[
['A','A','A','A','A','A','A','A','A','A','A','A','A','A'],
['A',0,5,5,5,5,5,5,5,5,5,5,5,'A'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 5, 'A', 'A', 'A', 'A', 5, 'A'],
['A', 5, 5, 5, 5, 5, 'A', 5, 'A', 5, 5, 5, 5, 'A'],
['A', 'A', 'A', 'A', 'A', 5, 'A', 5, 'A', 5, 'A', 'A', 'A', 'A'],
['A', 5, 5, 5, 5, 5, 'A', 5, 'A', 5, 5, 5, 5, 'A'],
['A', 5, 'A', 'A', 'A', 'A', 'A', 5, 'A', 'A', 'A', 'A', 5, 'A'],
['A', 5, 5, 5, 5, 5, 5, 5, 'A', 5, 5, 5, 5, 'A'],
['A', 'A', 'A', 'A', 'A', 5, 'A', 5, 'A', 5, 'A', 'A', 'A', 'A'],
['A', 5, 5, 5, 5, 5, 'A', 5, 'A', 5, 5, 5, 5, 'A'],
['A', 5, 'A', 'A', 'A', 'A', 'A', 5, 'A', 'A', 'A', 'A', 5, 'A'],
['A', 5, 'A', 5, 5, 5, 'A', 5, 5, 5, 'A', 5, 5, 'A'],
['A', 5, 5, 5, 'A', 5, 5, 5, 'A', 5, 5, 5, 'A', 'A'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
]
row=0
column=0



move(_map)

