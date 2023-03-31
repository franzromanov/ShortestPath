import numpy as np
import math as m

def mauberak(_map):
	#mencariWC
	row=0
	column=0
	WCumum=[]
	for area in _map:
		for point in area:
			if _map[row][column]==0:
				WCumum=[row,column]
				break
			column=column+1
		column=0
		row=row+1
	return WCumum

def rumah_sakitjiwa(_map):
	#lokasi-lokasi rumah sakit jiwa
	posisi_rsj=[]
	bag=[]
	row=0
	column=0
	for _rowm in _map:
		for _colm in _rowm:
			bag=[row,column]
			posisi_rsj.append(bag)
			column=column+1
		row=row+1
		column=0
	return posisi_rsj

def hitler_MakanKetoprak(_map,start):
	_map1=_map
	posisi_rsj=rumah_sakitjiwa(_map1)
	MasukRSJ=[]
	RSJBaru=[]
	WCumum=start
	foodpos=[]
	branch=[]
	bag=[]
	endp=[]
	length=0
	column=0
	row=0
	rows=len(_map)
	cols=len(_map[0])
	food=0

	visited.append(current_pos)

	










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

for area in _map:
	for point in area:
		if _map[row][column]==8:
			_map[row][column]="A"
		column=column+1
	column=0
	row=row+1

for area in _map:
	print(area)

start=mauberak(_map)
hitler_MakanKetoprak(_map,start)

rows=len(_map)
cols=len(_map[0])

print(rows,cols)