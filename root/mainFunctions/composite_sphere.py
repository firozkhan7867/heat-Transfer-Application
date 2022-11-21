
def compositesSpherelab(noOfWalls,nTemp,nThermal,nradii,ambTemp1,ambTemp2,heatCoef1,heatCoef2,checkhrate,checkutemp,checkxtemp,xvalue):
	pi=(22/7)

	# Resistance for Series Connection
	def R_series(K,r,H,n_walls):
		Res = lambda i : (1/(4*pi*K[i]))*((1/r[i])-(1/r[i]))
		Resistances=[]
		for i in range(n_walls):
			Resistances.append(Res(i))
		if H[0]>1:
			Resistances.append((1/(4*pi))*(1/(H[0]*(r[0]**2))))
		if H[1]>1:
			Resistances.append((1/(4*pi))*(1/(H[1]*(r[-1]**2))))
		return sum(Resistances)

	# Resistance for Parallel Connection	
	def R_parallel(K,r,H,n_walls):
		Res = lambda i : (1/(4*pi*K[i]))*((1/r[i])-(1/r[i+1]))
		Resistances=[]
		for i in range(n_walls):
			Resistances.append(Res(i))
		if H[0]>1:
			Resistances.append((1/(4*pi))*(1/(H[0]*(r[0]**2))))
		if H[1]>1:
			Resistances.append((1/(4*pi))*(1/(H[1]*(r[-1]**2))))
		Overall_resistance=0
		for i in range(n_walls+2):
			Overall_resistance+=1/Resistances[i]
		return 1/Overall_resistance


	# Finding Unknown Temperatures
	def Temp(T,T_amb,H,K,index,n,r,Q):
		Res = lambda i : (1/(4*pi*K[i]))*((1/r[i])-(1/r[i+1])) if i>=0 else (1/(4*pi*K[i]))*((1/r[i-1])-(1/r[i]))
		if index==n:
			return Q*Res(-1)-T[index-1]
		elif T_amb[0]>0 and T_amb[1]>0:
			return T[index+1]+(Q*Res(index))
		if index== 0:
			return T[1]+(T[1]-T[2])*(Res(0)/Res(1))
		if index==n:
			return T[-2]+(T[-2]-T[-3])*(Res(-1)/Res(-2))
		return (T[index-1]+(T[index+1]-T[index])*(Res(index-1)/Res(index)))

	# Finding Temperatures at some Distance,say x
	def Find_Temp(T,r,x):
		x1=x
		index=0
		while x1>0 and index<len(r):
			x1-=r[index]
			index+=1
		index=index-2
		t_r = T[index] - (T[index]-T[index+1])*(((1/r[index])-(1/x))/((1/r[index])-(1/r[index+1])))
		# print("Temperature at r = " + str(x) + " is " + str(t_r))





	############################################        START          ############################################
	n_layers = int(noOfWalls)
	a=1     # for unknown temps
	T=nTemp    # temperatures
	r=nradii    # radiuses
	K=nThermal   # thermal conductivities
	H=[-1,-1]  # heat transfer coefs
	T_amb = [-1,-1]  # ambients temperatures 
	output={}

	# print('Enter '+str(n_layers+1)+' Temperatures(enter -1 if unknown)')
	# print('      '+str(n_layers+1)+' Radiuses(no  unknown values)')
	# print('      '+str(n_layers)+' Thermal conductivites(no unknown values)')
	# print()

	# Temperatures input
	# print('TEMPS : ')
	# for i in range(n_layers+1):
	# 	T.append(float(input('Enter T_'+str(i+1)+' in *C : ')))
	# 	if T[i] ==-1 and a==1:
	# 		a-=1
	# 	elif T[i] == -1 and a==0:
	# 		print('Cannot be more than 1 unknown Temperature')
	# 		T[i] = float(input('Please enter T_'+str(i+1)+' : '))
	# print()	

	# # Radiuses input
	# print('RADIUSES : ')	
	# for i in range(n_layers+1):
	# 	r.append(-1)
	# 	while r[i]<=0:
	# 			r[i] = float(input('Enter radius_'+str(i+1)+' in meters : '))
	# print()	

	# # Thermal conductivities input
	# print('THERMAL CONDUCTIVITY : ')
	# for i in range(n_layers):
	# 	K.append(-1)
	# 	while K[i]<=0 and K:
	# 		K[i] = float(input('Enter K_'+str(i+1)+' in W/mK: '))
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
	# 	if -1 in T_amb:
	# 		print('Please Enter Both Temperatures !!!')
	# print()	



	# Type of Connection(parallel/series) and calculation of resistance of system
	if n_layers !=1:
		R = R_series(K,r,H,n_layers)
			
				# R = R_parallel(K,r,H,n_layers)
	else:
		R = (1/(4*pi*K[0]))*((1/r[0])-(1/r[1]))

				

	# Calculation of rate of heat transfer(heat loss), Q
	if H[0]!=1 and H[1]!=1:
		del_t = T_amb[0]-T_amb[1] 
	else:
		del_t = T[0]-T[-1]
	Q = del_t/R
	if checkhrate==True:
		output['hrate']=Q
	# Unknown temperature
	f=0		
	if (-1 in T) and n_layers>1:
		f=1
		index=T.index(-1)
		ind=index
		T[index] = Temp(T,T_amb,H,K,index,n_layers,r,Q)

	if checkxtemp==True:
		output['xtemp']=Find_Temp(T,r,xvalue)
	if checkutemp==True:
		output['utemp']=T[ind]
	return output


# # Calculating heat flux
# Area = 4*pi*r[-1]**2
# q = Q/Area


# #os.system('cls')
# print('RESULTS : ')
# print()

# # Printing unknown temperatures
# if f==1:
# 	print('Temperature of wall '+str(ind+1)+', T_'+str(ind+1)+' :',T[ind])
# print()

# # Print Thermal Resistance
# print('Thermal Resistance, R =',R,'K/W')
# print()

# # Print Heat Transfer rate
# print(R)
# print('Rate of Heat transfer, Q =',Q,' W')
# print()

# # Print Heat Flux
# print('Heat Flux of system, q =',q,'W/m^2')
# print()

# # Temp at some distance
# res=input("Do you need temperature at any distance,say r (y/n): ")
# while not res.lower().startswith('n'):
# 	x=float(input("Enter distance r in meters : "))
# 	Find_Temp(T,r,x)
# 	res=input("Do you need temperature at any distance,say x (y/n): ")
# 	print()


# print('ENDING PROGRAM :)')