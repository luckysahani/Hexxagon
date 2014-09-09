import pygame,sys,os,time
from pygame.locals import *
from sys import exit

windowres = (600, 350)
screen = pygame.display.set_mode(windowres)
screen.fill((0,0,250))	                        
pygame.display.set_caption("	Hexxagon-By Lucky Sahani	")
hex=pygame.image.load("im1.png")
obj1=pygame.image.load("im8.png")
obj2=pygame.image.load("im9.png")
obj3=pygame.image.load("im7.png")
obj4=pygame.image.load("im10.png")
obj5=pygame.image.load("im12.png")
obj6=pygame.image.load("im14.png")
obj7=pygame.image.load("im20.png")
obj8=pygame.image.load("im15.png")
obj9=pygame.image.load("im16.png")
obj10=pygame.image.load("im18.png")
obj11=pygame.image.load("im19.png")
obj12=pygame.image.load("im24.png")
obj13=pygame.image.load("exit.png")
z1=z2=0
mousex = mousey = 0
hexlist1=["empty"]
hexlist2=["empty"]
hexlist3=["empty"]
hexdict1={}
k5=0
max1=0
k6=0

templist1=[(520,80),(280,260),(40,80)]
templist2=[(40,200),(280,20),(520,200)]
templist3,templist4=templist1,templist2
pygame.mouse.set_pos([450, 350])
pygame.init()
global player
player=1
y1=0
y11=1
tempvar=0
tempx=tempy=0
#pygame.mixer.music.init()
#pygame.mixer.init()
#pygame.mixer.music.load("abc.mp3")
#pygame.mixer.music.set_volume(1)
#pygame.mixer.music.play(-1)

	

def main():
	screen.blit(obj6,(0,0))
	hexlistlev1()
	start2()
	pygame.event.wait()
	while True:
		mousex,mousey=pygame.mouse.get_pos()	
		#print mousex,mousey		
		#pygame.display.flip()
		(x,y,z)=pygame.mouse.get_pressed()
		tempx=mousex
		tempy=mousey
		pygame.display.flip()
		pygame.event.get()
		eventexit()
		#pygame.event.wait()
		#pygame.event.wait()
		if x==1 :
			if mousey>155 and mousey<190:
				main1()
			elif mousey>220 and mousey<255 :
				main2()
			elif dist(275,315,mousex,mousey)<100:
				print mousex,mousey				
				info()
			elif mousey>280 and mousex>520:
				sys.exit()
def main1():
	while True:
		screen.blit(obj8,(0,0))
		mousex,mousey=pygame.mouse.get_pos()
		#print mousex,mousey
		eventexit()
		screen.blit(obj9,(480,100))
		screen.blit(obj10,(0,100))
		#pygame.display.flip()
		#print mousex,mousey
		pygame.display.flip()
		pygame.event.get()
		pygame.event.wait()
		(x,y,z)=pygame.mouse.get_pressed()
		if(x==1):
			if (mousex<100 and mousey<200 and mousey>100) or (mousey>40 and mousey<130 and mousex<460  and mousex>110):
				main1a()
			elif (dist(mousex,mousey,530,150)<2500) or (mousey>140 and mousey<230 and mousex<460  and mousex>110):
				main1b()

def main1a():
	#main()
	pygame.event.wait()	
	player=1
	start()
	displayhexagon()
	hexlistlev1()	
	while True:
		getallok()	
		eventexit()
		mousex,mousey=pygame.mouse.get_pos()		
		pygame.display.flip()
		(x,y,z)=pygame.mouse.get_pressed()
		tempx=mousex
		tempy=mousey
		is_score()
		is_end()
		pygame.display.flip()
		if if_nomove1()==True:
			player=2
		if if_nomove2()==True:
			player=1
		if player==1:
			if x==1:
				is_mainmenu(mousex,mousey)				
				#print mousex,mousey
				p1=re_select(tempx,tempy,player)			
				if (is_inside()==True and p1==1):
					if is_valid(mousex,mousey)==True:
						is_possible(mousex,mousey)
						pygame.event.get()
						pygame.event.wait()
						x9,y9,z9=pygame.mouse.get_pressed()
						mousex,mousey=pygame.mouse.get_pos()
						h1,h2=mousex,mousey
						pygame.display.flip()
						while True:
							pygame.event.wait()						
							(x9,y9,z9)=pygame.mouse.get_pressed()
							if x9==1:
								h1,h2=pygame.mouse.get_pos()
								break
						if x9==1:
							if is_inside()==True:
								if is_valid(mousex,mousey):
									if is_check(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1	(tempx,tempy),nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2) )==True and not_playerhex(nearestcentrexcoordinates1	(h1,h2),nearestcentreycoordinates1(h1,h2))==True:
										if (player==1)==True:
											pygame.event.wait()
											addlist1(nearestcentrexcoordinates1	(tempx,tempy),nearestcentreycoordinates1(tempx,tempy))
											addlist3(nearestcentrexcoordinates1	(h1,h2),nearestcentreycoordinates1(h1,h2))
											displayhex1()
											player=2
											getallok()
											is_end()
											pygame.display.flip()
											pygame.display.update()
										#clock.tick()	
				#colourchange() 
				pygame.event.wait()	
			pygame.display.flip()
			
		elif (player==2) and len(templist1)>0 :
			(x,y,z)=pygame.mouse.get_pressed()			
			if x==1:
				mousex,mousey=pygame.mouse.get_pos()			
				is_mainmenu(mousex,mousey)			
			max1=0			
			max2=50
			tempr2=0
			for i3 in range(9):
				x3=(i3*60)+40
				for j3 in range(f(i3)):
					y3=20+(30*j3)+abs(i3-4)*15	
					if ((x3,y3) in templist2) :
						mousex,mousey=x3,y3
						tempx,tempy=x3,y3
						p1=re_select(mousex,mousey,player)			
						pygame.event.get()
						#pygame.event.wait()
						h1,h2=nearestcentrexcoordinates1(mousex,mousey),nearestcentreycoordinates1(mousex,mousey)
						pygame.display.flip()
						tempr=0	
						for i in range(9):
							x=(i*60)+40
							for j in range(f(i)):
								y=20+(30*j)+abs(i-4)*15
								if  (dist(mousex,mousey,x,y)==900) or (dist(mousex,mousey,x,y)==3825) or (dist(mousex,mousey,x,y)==3600) or (dist(mousex,mousey,x,y)==5625) or (dist(mousex,mousey,x,y)==15300)==True or ((dist(mousex,mousey,x,y)==14400)==True and (abs(mousex-x)==120)) :
									tempr=0	
									if ((x,y) in templist1 or (x,y) in templist2):
										k6=1
									else:
										k6=0
									if is_check(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1	(tempx,tempy),nearestcentrexcoordinates1(x,y),nearestcentreycoordinates1(x,y) )==True:
										k7=0
									else:
										k7=1
									if  (((dist(h1,h2,x,y)==900) or (dist(h1,h2,x,y)==3825)) and k6==0 and k7==0):
										tempr=1
										for i1 in range(9):
											x1=(i1*60)+40
											for j1 in range(f(i1)):
												y1=20+(30*j1)+abs(i1-4)*15
												for (x1,y1) in templist1:
													if  (dist(x,y,x1,y1)==900) or (dist(x,y,x1,y1)==3825):
														tempr=tempr+1
														
									elif  ((dist(h1,h2,x,y)==3600) or (dist(h1,h2,x,y)==5625) or (dist(h1,h2,x,y)==15300)==True or ((dist(h1,h2,x,y)==14400)==True and (abs(h1-x)==120)) and k6==0 and k7==0) :
										tempr=0
										for i1 in range(9):
											x1=(i1*60)+40
											for j1 in range(f(i1)):
												y1=20+(30*j1)+abs(i1-4)*15
												for (x1,y1) in templist1:
													if  (dist(x,y,x1,y1)==900) or (dist(x,y,x1,y1)==3825):
														tempr=tempr+1
									for i4 in range(9):
										x4=(i4*60)+40
										for j4 in range(f(i4)):
											y4=20+(30*j4)+abs(i4-4)*15
											for (x4,y4) in templist1:
												if  (((dist(x3,y3,x4,y4)==900) or (dist(x3,y3,x4,y4)==3825))):
													tempr2=1
													for i5 in range(9):
														x5=(i5*60)+40
														for j5 in range(f(i5)):
															y5=20+(30*j5)+abs(i5-4)*15
															for (x5,y5) in templist2:
																if  (((dist(x3,y3,x4,y4)==900) or (dist(x3,y3,x4,y4)==3825))):
																	tempr2=tempr2+1
												elif  ((dist(x3,y3,x4,y4)==3600) or (dist(x3,y3,x4,y4)==5625) or (dist(x3,y3,x4,y4)==15300)==True or ((dist(x3,y3,x4,y4)==14400)==True and (abs(x3-x4)==120)) ) :
													tempr2=0
													for i5 in range(9):
														x5=(i5*60)+40
														for j5 in range(f(i5)):
															y5=20+(30*j5)+abs(i5-4)*15
															for (x5,y5) in templist2:
																if  (((dist(x3,y3,x4,y4)==900) or (dist(x3,y3,x4,y4)==3825))):
																	tempr2=tempr2+1
									if(((2*tempr)-tempr2)>max1) and ((x,y) not in templist1) and ((x,y) not in templist2):
										max1=(2*tempr)-tempr2
										z1=x
										z2=y
										tempx1=x3
										tempy1=y3
			
			
									
			if  ((dist(z1,z2,tempx1,tempy1)==3600) or (dist(z1,z2,tempx1,tempy1)==5625) or (dist(z1,z2,tempx1,tempy1)==15300)==True or ((dist(z1,z2,tempx1,tempy1)==14400)==True and (abs(z1-tempx1)==120))) :
				y3=templist2.index((tempx1,tempy1))
				templist2.pop(y3)
			#pygame.event.wait()
			templist2.append((z1,z2))
			addlist4(z1,z2)
			player=1
			getallok()
			is_end()
			pygame.display.flip()
			pygame.display.update()
		elif player==2:
			(x,y,z)=pygame.mouse.get_pressed()			
			if x==1:
				mousex,mousey=pygame.mouse.get_pos()			
				is_mainmenu(mousex,mousey)	
			

def main1b():
	#pygame.event.wait()	
	player=1
	start()
	displayhexagon()
	hexlistlev1()	
	while True:
		getallok()	
		eventexit()
		mousex,mousey=pygame.mouse.get_pos()		
		pygame.display.flip()
		(x,y,z)=pygame.mouse.get_pressed()
		tempx=mousex
		tempy=mousey
		is_score()
		is_end()
		pygame.display.flip()
		if if_nomove1()==True:
			player=2
		if if_nomove2()==True:
			player=1
		if player==1:
			if x==1:
				is_mainmenu(mousex,mousey)				
				#print mousex,mousey
				p1=re_select(tempx,tempy,player)			
				if (is_inside()==True and p1==1):
					if is_valid(mousex,mousey)==True:
						is_possible(mousex,mousey)
						pygame.event.get()
						pygame.event.wait()
						x9,y9,z9=pygame.mouse.get_pressed()
						mousex,mousey=pygame.mouse.get_pos()
						h1,h2=mousex,mousey
						pygame.display.flip()
						while True:
							pygame.event.wait()						
							(x9,y9,z9)=pygame.mouse.get_pressed()
							if x9==1:
								h1,h2=pygame.mouse.get_pos()
								break
						if x9==1:
							if is_inside()==True:
								if is_valid(mousex,mousey):
									if is_check(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1	(tempx,tempy),nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2) )==True and not_playerhex(nearestcentrexcoordinates1	(h1,h2),nearestcentreycoordinates1(h1,h2))==True:
										if (player==1)==True:
											pygame.event.wait()
											addlist1(nearestcentrexcoordinates1	(tempx,tempy),nearestcentreycoordinates1(tempx,tempy))
											addlist3(nearestcentrexcoordinates1	(h1,h2),nearestcentreycoordinates1(h1,h2))
											displayhex1()
											player=2
											getallok()
											is_end()
											pygame.display.flip()
											pygame.display.update()
										#clock.tick()	
				#colourchange() 
				pygame.event.wait()	
			pygame.display.flip()
			
		elif (player==2) and len(templist1)>0 :
			(x,y,z)=pygame.mouse.get_pressed()			
			if x==1:
				mousex,mousey=pygame.mouse.get_pos()			
				is_mainmenu(mousex,mousey)			
			max1=0			
			
			for i3 in range(9):
				x3=(i3*60)+40
				for j3 in range(f(i3)):
					y3=20+(30*j3)+abs(i3-4)*15	
					if ((x3,y3) in templist2) :
						mousex,mousey=x3,y3
						tempx,tempy=x3,y3
						p1=re_select(mousex,mousey,player)			
						pygame.event.get()
						#pygame.event.wait()
						h1,h2=nearestcentrexcoordinates1(mousex,mousey),nearestcentreycoordinates1(mousex,mousey)
						pygame.display.flip()
						tempr=0	
						for i in range(9):
							x=(i*60)+40
							for j in range(f(i)):
								y=20+(30*j)+abs(i-4)*15
								if  (dist(mousex,mousey,x,y)==900) or (dist(mousex,mousey,x,y)==3825) or (dist(mousex,mousey,x,y)==3600) or (dist(mousex,mousey,x,y)==5625) or (dist(mousex,mousey,x,y)==15300)==True or ((dist(mousex,mousey,x,y)==14400)==True and (abs(mousex-x)==120)) :
									tempr=0	
									if ((x,y) in templist1 or (x,y) in templist2):
										k6=1
									else:
										k6=0
									if is_check(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1	(tempx,tempy),nearestcentrexcoordinates1(x,y),nearestcentreycoordinates1(x,y) )==True:
										k7=0
									else:
										k7=1
									if  (((dist(h1,h2,x,y)==900) or (dist(h1,h2,x,y)==3825)) and k6==0 and k7==0):
										tempr=1
										for i1 in range(9):
											x1=(i1*60)+40
											for j1 in range(f(i1)):
												y1=20+(30*j1)+abs(i1-4)*15
												for (x1,y1) in templist1:
													if  (dist(x,y,x1,y1)==900) or (dist(x,y,x1,y1)==3825):
														tempr=tempr+1
														
									elif  ((dist(h1,h2,x,y)==3600) or (dist(h1,h2,x,y)==5625) or (dist(h1,h2,x,y)==15300)==True or ((dist(h1,h2,x,y)==14400)==True and (abs(h1-x)==120)) and k6==0 and k7==0) :
										tempr=0
										for i1 in range(9):
											x1=(i1*60)+40
											for j1 in range(f(i1)):
												y1=20+(30*j1)+abs(i1-4)*15
												for (x1,y1) in templist1:
													if  (dist(x,y,x1,y1)==900) or (dist(x,y,x1,y1)==3825):
														tempr=tempr+1
									if(tempr>max1) and ((x,y) not in templist1) and ((x,y) not in templist2):
										max1=tempr
										z1=x
										z2=y
										tempx1=x3
										tempy1=y3
			if  ((dist(z1,z2,tempx1,tempy1)==3600) or (dist(z1,z2,tempx1,tempy1)==5625) or (dist(z1,z2,tempx1,tempy1)==15300)==True or ((dist(z1,z2,tempx1,tempy1)==14400)==True and (abs(z1-tempx1)==120))) :
				y3=templist2.index((tempx1,tempy1))
				templist2.pop(y3)
			#pygame.event.wait()
			templist2.append((z1,z2))
			addlist4(z1,z2)
			player=1
			getallok()
			is_end()
			pygame.display.flip()
			pygame.display.update()
		elif player==2:
			(x,y,z)=pygame.mouse.get_pressed()			
			if x==1:
				mousex,mousey=pygame.mouse.get_pos()			
				is_mainmenu(mousex,mousey)	
			
			
def main2() :
	
	global mousex,mousey   
	player=1         
	start()	
	displayhexagon()
	hexlistlev1()
	#hexlistlev2()
	while True:
		getallok()		
		eventexit()
		mousex,mousey=pygame.mouse.get_pos()		
		pygame.display.flip()
		(x,y,z)=pygame.mouse.get_pressed()
		tempx=mousex
		tempy=mousey
		is_score()
		is_end()
		pygame.display.flip()
		if if_nomove1()==True:
			player=2
		if if_nomove2()==True:
			player=1
		if x==1:
			is_mainmenu(mousex,mousey)
			p1=re_select(tempx,tempy,player)			
			if (is_inside()==True and p1==1):
				if is_valid(mousex,mousey)==True:
					is_possible(mousex,mousey)
					pygame.event.get()
					pygame.event.wait()
					x9,y9,z9=pygame.mouse.get_pressed()
					mousex,mousey=pygame.mouse.get_pos()
					h1,h2=mousex,mousey
					pygame.display.flip()
					while True:
						pygame.event.wait()						
						(x9,y9,z9)=pygame.mouse.get_pressed()
						if x9==1:
							h1,h2=pygame.mouse.get_pos()
							break
					if x9==1:
						if is_inside()==True:
							if is_valid(mousex,mousey):
								if is_check(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1(tempx,tempy),nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2) )==True and not_playerhex(nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2))==True:
									if (player==1)==True:
										pygame.event.wait()
										addlist1(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1(tempx,tempy))
										addlist3(nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2))
										displayhex1()
										player=2
										getallok()
										is_end()
										pygame.display.flip()
										pygame.display.update()
									else :
										pygame.event.wait()
										addlist2(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1(tempx,tempy))
										addlist4(nearestcentrexcoordinates1(h1,h2),nearestcentreycoordinates1(h1,h2))
										displayhex2()
										player=1
										getallok()
										is_end()
										pygame.display.flip()
										pygame.display.update()
										#print templist1,templist2
			#clock.tick()	
			#colourchange() 
			pygame.event.wait()	
		pygame.display.flip()


def is_mainmenu(x,y):
	if  dist(575,25,x,y)<400:
		while len(templist1) > 0 : templist1.pop()
		while len(templist2) > 0 : templist2.pop()
		main()
	
	
def change_player2(k1,k2):
	
	
	mousx=nearestcentrexcoordinates1(k1,k2)
	mousy=nearestcentreycoordinates1(k1,k2)	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15	
			if (x,y) in templist1 or (x,y) in templist2:
				m1=0
			elif  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
					print "player not changed"
					print x,y					
					return False
	return True	


def start2():
	while len(templist1) > 0 : templist1.pop()
	while len(templist2) > 0 : templist2.pop()
	screen.blit(obj13,(510,265))	
	templist1.append((520,80))
	templist1.append((280,260))
	templist1.append((40,80))
	templist2.append((40,200))
	templist2.append((280,20))
	templist2.append((520,200))


def change_player(player):
	if(player==1):
		return 2
	else:
		return 1
def is_end():
	if (len(templist1) + len(templist2))==61:
		font = pygame.font.Font(None, 26)		
		text1 = font.render("Game Over", 1, (10, 10, 10))
		screen.blit(text1, (200,300))
		if(len(templist1)>len(templist2)):		
			text2=font.render("Player 1 Wins!!!",1,(10,10,10))
			screen.blit(text2,(200,320))
		else :
			text3=font.render("Player 2 Wins!!!",1,(10,10,10))
			screen.blit(text3,(200,320))
	elif( len(templist1)==0):
		font = pygame.font.Font(None, 26)		
		text1 = font.render("Game Over", 1, (10, 10, 10))
		screen.blit(text1, (200,300))
		text3=font.render("Player 2 Wins!!!",1,(10,10,10))
		screen.blit(text3,(200,320))
		
	elif(len (templist2)==0):
		font = pygame.font.Font(None, 26)		
		text1 = font.render("Game Over", 1, (10, 10, 10))
		screen.blit(text1, (200,300))
		text2=font.render("Player 1 Wins!!!",1,(10,10,10))
		screen.blit(text2,(200,320))
		
	pygame.display.update()
	pygame.display.flip()

def info():
	if True:
		screen.blit(obj12,(0,0))	
		#print "ksmk"
		#pygame.event.get()
		font = pygame.font.Font(None, 45)		
		text1 = font.render("Rules for Hexxagon ", 1, (110, 10, 110))
		screen.blit(text1, (150,0))
		font = pygame.font.Font(None, 23)
		text2=font.render("   The objective of the game is to have the majority of your colour discs",1,(0,220,210))
		text3=font.render("   on the board at the end of the game .A move consists of either a growth",1,(0,220,210))
		text4=font.render("    or a jump. A growth is when you select one of your pieces and place a ",1,(0,220,210))
		text5=font.render("   new piece in an empty adjacent space, including diagonally. A jump is",1,(0,220,210))
		text6=font.render("    when you select one of your pieces and move it to an empty space that",1,(0,220,210)) 
		text7=font.render("   is two position away. This includes diagonals and knights moves.Once ",1,(0,220,210))
		text8=font.render("   placed, any opponents pieces that are adjacent to the new piece (either",1,(0,220,210))
		text9=font.render("    through growth or jump) are flipped the to the moving player's colour.If",1,(0,220,210))
		text10=font.render(" you are unable to move on your turn,you are skipped.There is a chance that",1,(0,220,210))
		text11=font.render("that your opponent may be forced to make a move that will let you move again.",1,(0,220,210))
		screen.blit(text2,(0,130+40))
		screen.blit(text3,(0,140+40+5))
		screen.blit(text4,(0,150+40+10))
		screen.blit(text5,(0,160+40+15))
		screen.blit(text6,(0,170+40+20))
		screen.blit(text7,(0,180+40+25))
		screen.blit(text8,(0,190+40+30))
		screen.blit(text9,(0,200+40+35))
		screen.blit(text10,(0,210+40+40))
		screen.blit(text11,(0,220+40+45))
		screen.blit(obj7,(550,0))
		pygame.display.update()
	while True:
		#pygame.display.flip()
		#pygame.display.update()
		mousex,mousey=pygame.mouse.get_pos()
		#pygame.display.flip()
		#pygame.event.get()
		pygame.event.wait()
		#(x,y,z)=pygame.mouse.get_pressed()
		(x,y,z)=pygame.mouse.get_pressed()
		#print mousex,mousey
		if x==1:
			print mousex,mousey
			pygame.display.flip()
			pygame.event.get()
			pygame.event.wait()
			(x,y,z)=pygame.mouse.get_pressed()
			if(dist(mousex,mousey,575,25)<225):
				main()
def is_score():
	font = pygame.font.Font(None, 36)
	k1=len(templist1)
	text = font.render("= %d"%k1, 1, (10, 10, 10))
	screen.blit(text, (100,300))
	screen.blit(obj1,(60-5,300))
	screen.blit(obj2,(360,300+5))
	pygame.display.update
	font = pygame.font.Font(None,36)
	k2=len(templist2)
	text=font.render("= %d"%k2,1, (10,10,10))
	screen.blit(text,(400,300))
	screen.blit(obj1,(60-5,300))
	screen.blit(obj2,(360,300+5))
	pygame.display.update


def not_playerhex(k1,k2):
	if player==1:	
		if (k1,k2) in templist2 or (k1,k2) in templist1:
			return False
		else :
			return True 
	elif player==2:
		if (k1,k2) in templist1 or (k1,k2) in templibst2:
			return False
		else:
			return True
def re_select(tempx,tempy,player):
	if is_select(nearestcentrexcoordinates1(tempx,tempy),nearestcentreycoordinates1(tempx,tempy),player)==True:
		return 1
	else:
		return 0	

def is_select(x,y,player):
	if (player==1)==True:
		if (x,y) in templist1:
			return True
		else:
			return False
	elif (player==2)==True:
		if (x,y) in templist2:
			return True
		else:
			return False
		
def is_check(k31,k41,k11,k21):
	mousx=nearestcentrexcoordinates1(k11,k21)
	mousy=nearestcentreycoordinates1(k11,k21)	
	x=nearestcentrexcoordinates1(k31,k41)
	y=nearestcentreycoordinates1(k31,k41)		
	
	if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
		return True
	return False

def addlist3(g1,g2):
	mousx=nearestcentrexcoordinates1(g1,g2)
	mousy=nearestcentreycoordinates1(g1,g2)	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15	
			if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) :
				if (x,y) in templist2:
					templist1.append((x,y))
					y2=templist2.index((x,y))
					templist2.pop(y2)
def addlist4(g1,g2):
	mousx=nearestcentrexcoordinates1(g1,g2)
	mousy=nearestcentreycoordinates1(g1,g2)	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15	
			if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) :
				if (x,y) in templist1:
					templist2.append((x,y))
					y2=templist1.index((x,y))
					templist1.pop(y2)

def if_nomove1():

	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			for i2 in range(9):
				mousx=(i2*60)+40
				for j2 in range(f(i2)):
					mousy=20+(30*j2)+abs(i2-4)*15
					for (x,y) in templist1:
						if((mousx,mousy) not in templist1 and (mousx,mousy) not in templist2) :						
							if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
								return False
	return True

def if_nomove2():

	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			for i2 in range(9):
				mousx=(i2*60)+40
				for j2 in range(f(i2)):
					mousy=20+(30*j2)+abs(i2-4)*15
					for (x,y) in templist2:
						if not((mousx,mousy) in templist1 or (mousx,mousy)  in templist2):						
							if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
								return False
	return True





	

def is_valid(k1,k2):
		
	mousx=nearestcentrexcoordinates1(k1,k2)
	mousy=nearestcentreycoordinates1(k1,k2)	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15	
			if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
				return True
	return False
def is_possible(g1,g2):
	mousx=nearestcentrexcoordinates1(g1,g2)
	mousy=nearestcentreycoordinates1(g1,g2)	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15	
			if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) :
				if (x,y) not in templist1 and (x,y) not in templist2:
					screen.blit(obj4,(x-30-5-2.5,y-20))
			elif (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
				if (x,y) not in templist1 and (x,y) not in templist2:
					screen.blit(obj5,(x-50+10+2.5,y-20))
	
def getallok():

	screen.blit(obj11,(0,0))
	displayhexagon()
	is_score()
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if (x,y) in templist1:
				screen.blit(obj1,(x-30+2.5,y-15+2.5))
			elif (x,y) in templist2:
				screen.blit(obj2,(x-20,y-10))
	is_end()


	
def is_inside():
	mousex,mousey=pygame.mouse.get_pos()
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15 :
				return True
	return False
def colourchange():
	if((1/1000)*pygame.time.get_ticks())%7==0:
		screen.fill((250,250,250))	
	elif((1/1000)*pygame.time.get_ticks())%7==1:  
		screen.fill((255,0,0))
	elif((1/1000)*pygame.time.get_ticks())%7==2:  
		screen.fill((0,255,0))
	elif((1/1000)*pygame.time.get_ticks())%7==3:  
		screen.fill((0,0,255))
	elif((1/1000)*pygame.time.get_ticks())%7==4:  
		screen.fill((0,0,0))
	elif((1/1000)*pygame.time.get_ticks())%7==5:  
		screen.fill((0,0,128))
	elif((1/1000)*pygame.time.get_ticks())%7==6:  
		screen.fill((255,200,200))
def start():
	screen.blit(obj1,(490+2.5,65+2.5))
	screen.blit(obj1,(250+2.5,245+2.5))
	screen.blit(obj1,(10+2.5,65+2.5))
	screen.blit(obj2,(490+5+5,180+5+5))
	screen.blit(obj2,(250+5+5,5+5))
	screen.blit(obj2,(10+5+5,180+5+5))

def addlist1(mousx,mousy):
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x1=(i*60)+40
		for j in range(f(i)):
			y1=20+(30*j)+abs(i-4)*15
			if abs(mousex-x1)<30 and abs(mousey-y1)<15 :
				templist1.append((x1,y1))
				x=x1
				y=y1
				
	if  (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)):
		y3=templist1.index((mousx,mousy))
		templist1.pop(y3)
		
	
def addlist2(mousx,mousy):
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x1=(i*60)+40
		for j in range(f(i)):
			y1=20+(30*j)+abs(i-4)*15
			if abs(mousex-x1)<30 and abs(mousey-y1)<15 :
				templist2.append((x1,y1))
				x=x1
				y=y1
				
	if  (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==15300)==True or ((dist(mousx,mousy,x,y)==14400)==True and (abs(mousx-x)==120)) :
		y3=templist2.index((mousx,mousy))		
		templist2.pop(y3)
		

				
	
def dist(x3,y3,a3,b3):
	return (((x3-a3)**2) + ((y3-b3)**2))
def displayhex1():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:	
				screen.blit(obj1,(x-30+2.5,y-15+2.5))
def displayhex2():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:	
				screen.blit(obj2,(x-20,y-10))
def displayhex3():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:	
				screen.blit(obj4,(x-30+2.5+40+10,y-15+2.5-5))
def displayhex4():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:	
				screen.blit(obj5,(x-30+2.5,y-15+2.5))
def eventexit():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
def printmousepos():
	mousex,mousey=pygame.mouse.get_pos()
	print mousex,mousey

def nearestcentrecoordinatesdisplay():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:
				print x
				print y					
def nearestcentrexcoordinates():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:
				return x
def nearestcentrexcoordinates1(x1,y1):
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(x1-x)<30 and abs(y1-y)<15:
				return x
def nearestcentreycoordinates1(x1,y1):
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(x1-x)<30 and abs(y1-y)<15:
				return y
def nearestcentreycoordinates():
	mousex,mousey=pygame.mouse.get_pos()	
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			if abs(mousex-x)<30 and abs(mousey-y)<15:
				return y
def f(i):
	if i<5:
		return i+5
	else:
		return 13-i
def displayhexagon():
	screen.blit(obj7,(550,0))	
	for i in range(9):
		x=i*60
		for j in range(f(i)):
			y=30*j+abs(i-4)*15
			screen.blit(hex,(x,y))

def hexlistlev1():
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			hexlist1.append((x,y))		

def hexfindi1():
	mousex,mousey=pygame.mouse.get_pos()
	mousx=nearestcentrexcoordinates()
	mousy=nearestcentreycoordinates()	
	for i in range(61):
		if hexlist1[i]==(mousx,mousy):
			return i
		      
def hexfindi1(l1,l2):	
	for i in range(61):
		if hexlist1[i]==(l1,l2):
			return i
			
def retallcenterx():
		for i in range(9):
			x=(i*60)+40
			for j in range(f(i)):
				y=20+(30*j)+abs(i-4)*15
				return x	

def retallcentery():
		for i in range(9):
			x=(i*60)+40
			for j in range(f(i)):
				y=20+(30*j)+abs(i-4)*15
				return y	
def hexlistlev2():
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			for i2 in range(9):
				mousx=(i2*60)+40
				for j2 in range(f(i2)):
					mousy=20+(30*j2)+abs(i2-4)*15
					if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) :
						hexlist2.append((hexfindi1(x,y),hexfindi1(mousx,mousy)))	
	hexlist2.pop(294)
	hexlist2.pop(290)
	hexlist2.pop(308)
	hexlist2.pop(308)
	hexlist2.pop(308)
	hexlist2.pop(307)
def hexlistlev3():
	for i in range(9):
		x=(i*60)+40
		for j in range(f(i)):
			y=20+(30*j)+abs(i-4)*15
			for i2 in range(9):
				mousx=(i2*60)+40
				for j2 in range(f(i2)):
					mousy=20+(30*j2)+abs(i2-4)*15
					if  (dist(mousx,mousy,x,y)==900) or (dist(mousx,mousy,x,y)==3825) or (dist(mousx,mousy,x,y)==3600) or (dist(mousx,mousy,x,y)==5625) or (dist(mousx,mousy,x,y)==14400) or (dist(mousx,mousy,x,y)==15300)==True :
						hexlist3.append((hexfindi1(x,y),hexfindi1(mousx,mousy)))
hexlistlev1()
hexlistlev2()
hexlistlev3()

#print hexlist3




main()


             
