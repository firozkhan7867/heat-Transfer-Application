

def compositeslab(noOfWalls,nTemp,nThermal,nLength,series,parallel,ambTemp1,ambTemp2,heatCoef1,heatCoef2,crossSecion,checkhrate,checkutemp,checkxtemp,xvalue):
	# Resistance for Series Connection
	def R_series(L,K,A,H,n_walls):
		Res = lambda i : L[i]/(K[i]*A)
		Resistances=[]
		for i in range(n_walls):
			Resistances.append(Res(i))
		if H[0]>1 and H[1]>1:
			Resistances.append(1/(H[0]*A))
			Resistances.append(1/(H[1]*A))
		return sum(Resistances)

	# Resistance for Parallel Connection	
	def R_parallel(L,K,A,H,n_walls):
		Res = lambda i : L[i]/(K[i]*A)
		Resistances=[]
		for i in range(n_walls):
			Resistances.append(Res(i))
		if H[0]>1 and H[1]>1:
			Resistances.append(1/(H[0]*A))
			Resistances.append(1/(H[1]*A))
		Overall_resistance=0
		for i in range(n_walls+2):
			Overall_resistance+=1/Resistances[i]
		return 1/Overall_resistance


	# Finding Unknown Temperatures
	def Temp(T,T_amb,H,K,index,L,n,A):
		Res = lambda i : L[i]/(K[i]*A)
		if index== 0:
			return T[1]+(T[-2]-T[-1])*(Res(1)/Res(0))
		if index==n:
			return T[-2]+(T[-2]-T[-3])*(Res(-1)/Res(-2))
		return ((Res(index)*T[index-1])+(Res(index-1)*T[index+1]))/(Res(index)+Res(index-1))

	# Finding Temperatures at some Distance,say x
	def Find_Temp(T,L,x):
		x1=x
		index=0
		while x>0 and index<len(L):
			dis=x
			x-=L[index]
			index+=1
		x=dis
		t1=T[index-1]
		t2=T[index]
		l=L[index-1]
		t_x=t1-((x/l)*(t1-t2))
		return t_x
		# print("Temperature at x = " + str(x1) + " is " + str(t_x)+' *C')


	############################################        START          ############################################
	n_walls = int(noOfWalls)
	print()
	a=1     # for unknown temps
	T=nTemp    # temperatures
	L=nLength   # lengths
	K=nThermal  # thermal conductivities
	H=[-1,-1]  # heat transfer coefs
	T_amb = [-1,-1]  # ambients temperatures 
	Area = -1  #area
	output={}
	# print('Enter '+str(n_walls+1)+' Temperatures(enter -1 if unknown)')
	# print('      '+str(n_walls)+' Thermal conductivites(no unknown values)')
	# print('      '+str(n_walls)+' Lengths(no  unknown values)')
	# print()

	# Temperatures input
	# print('TEMPS : ')
	# for i in range(n_walls+1):
	# 	T.append(float(input('Enter T_'+str(i+1)+' in *C : ')))
	# 	if T[i] ==-1 and a==1:
	# 		a-=1
	# 	elif T[i] == -1 and a==0:
	# 		print('Cannot be more than 1 unknown Temperature')
	# 		T[i] = float(input('Please enter T_'+str(i+1)+' in *C : '))
	# print()
				
	# Lengths input
	# print('LENGTHS : ')	
	# for i in range(n_walls):
	# 	L.append(-1)
	# 	while L[i]<=0:
	# 			L[i] = float(input('Enter L_'+str(i+1)+' in meters : '))
	# print()
		
	# Thermal conductivities input
	# print('THERMAL CONDUCTIVITY : ')
	# for i in range(n_walls):
	# 	K.append(-1)
	# 	while K[i]<=0:
	# 			K[i] = float(input('Enter K_'+str(i+1)+' in W/mK : '))
	# print()


	# Heat transfer coefs inputs
	# print('HEAT TRANSFER COEFS (enter 1 if not considered)')
	while H[0]<0 or H[1]<0:
		H[0]=float(heatCoef1)
		H[1]=float(heatCoef2)
	# print()

	# Ambients temperatures input
	# print('AMBIENT TEMPERATURES : ')
	while  (-1 in T_amb):
		T_amb[0] = float(ambTemp1)
		T_amb[1] = float(ambTemp2)
		# if -1 in T_amb:
		# 	print('Please Enter Both Temperatures !!!')
	# print()
		
	# Area input
	while Area<=0:
		Area = float(crossSecion)
	# print()

	# Type of Connection(parallel/series) and calculation of resistance of system
	if n_walls !=1:
		if series==True:
			R = R_series(L,K,Area,H,n_walls)
		elif parallel==True:
			R = R_parallel(L,K,Area,H,n_walls)
	else:
		R = L[0]/(K[0]*Area)	
						
	# Unknown temperature	
	f=0
	if -1 in T:
		f=1
		index=T.index(-1)
		ind=index
		T[index] = Temp(T,T_amb,H,K,index,L,n_walls,Area)


	# Calculation of rate of heat transfer(heat loss), Q
	if checkhrate==True:
		del_t = T[0]-T[-1]
		Q = del_t/R
		output['hrate']=Q

	# Calculating heat flux
	#q = Q/Area
	if checkxtemp==True:
		output['xTemp']=Find_Temp(T,L,xvalue)
	if checkutemp==True:
		output['uTemp']=T[ind]
	return output
	# Printing unknown temperatures
	# if f==1:
	# 	print('Temperature of wall '+str(ind+1)+', T_'+str(ind+1)+' :',T[ind],'*C')
	# 	print()

	# # Print Thermal Resistance
	# print('Thermal Resistance, R =',R,'K/W')
	# print()

	# # Print Heat Transfer rate
	# print('Rate of Heat transfer, Q =',Q,' W')
	# print()

	# # Print Heat Flux
	# print('Heat Flux, q =',q,'W/m^2')
	# print()

	# Temp at some distance
	# res=input("Do you need temperature at any distance,say x (y/n): ")
	# while not res.lower().startswith('n'):
	# 	x=float(input("Enter distance x in meters : "))
	# 	Find_Temp(T,L,x)
	# 	print()
	# 	res=input("Do you need temperature at any distance,say x (y/n): ")
	# print()
