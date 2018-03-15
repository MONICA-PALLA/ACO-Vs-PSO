from numpy import *
import matplotlib.pyplot as plt


def cityReadSACO():
	x,y=loadtxt('city_data.txt', unpack = True)
	order=loadtxt('Data.txt')
	print order
	#print x
	#print y
	'''order1[]
	x1[]
	y1[]'''
	x1=[]
	y1=[]
    
	for RK in order:
		x1.append(x[int(RK)])
		y1.append(y[int(RK)])
	x1.append(x[int(order[0])])
	y1.append(y[int(order[0])])
	plt.figure('S-ACO', (8,6), 80, 'w', 'k')	
	plt.plot(x1,y1, marker='x', linestyle = '--', color = 'r', label = 'S-ACO')
	for RK in range(len(order)):
		plt.text(x1[RK],y1[RK],order[RK])
	plt.show() 
'''
def cityReadElitist():
	x,y=loadtxt('city_data_elitist.txt', unpack = True)
	order=loadtxt('Data_elitist.txt')
	print order
	#print x
	#print y
	order1[]
	x1[]
	y1[]
	x1=[]
	y1=[]
	for RK in order:
		x1.append(x[int(RK)])
		y1.append(y[int(RK)])
	x1.append(x[int(order[0])])
	y1.append(y[int(order[0])])	
	plt.figure('EAS', (8,6), 80, 'w', 'k')
	plt.plot(x1,y1, marker='x', linestyle = '--', color = 'r',label = 'EAS')
	for RK in range(len(order)):
		plt.text(x1[RK],y1[RK],order[RK])
	plt.show() 

def cityReadRank():
	x,y=loadtxt('city_data_rank.txt', unpack = True)
	order=loadtxt('Data_rank.txt')
	print order
	#print x
	#print y
	order1[]
	x1[]
	y1[]
	x1=[]
	y1=[]
	for RK in order:
		x1.append(x[int(RK)])
		y1.append(y[int(RK)])
	x1.append(x[int(order[0])])
	y1.append(y[int(order[0])])
	plt.figure('Rank-Based ACO', (8,6), 80, 'w', 'k')	
	plt.plot(x1,y1, marker='x', linestyle = '--', color = 'r',label = 'Rank')
	for RK in range(len(order)):
		plt.text(x1[RK],y1[RK],order[RK])
	plt.show() 
'''	 
def main():
    cityReadSACO()
   # cityReadElitist()
   # cityReadRank()	


if __name__=="__main__":
	main()
