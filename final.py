class StateMachine:
    def __init__(self):
        self.min=0
        self.max=0
        self.startState = None
        self.li=0
        self.lift_inside=[]
        self.lup=0
        self.ldown=[]
        self.last=0
        self.last_floor_b4trans=0
        self.count=0
        self.d=0
        self.lfinal=[]

    def add_states(self,initial,listup,listdown,liftinside,max_floors):
        self.li=initial
        self.lift_inside=liftinside
        self.lup=listup
        self.ldown=listdown
        self.last=initial
        self.last_floor_b4trans=initial
        self.max=max_floors
        self.min=1
        self.lfinal=[initial]


    def run(self,state):

        max1,min1=1,self.max
        for i in self.lup+self.lift_inside+self.ldown:
            d=i-self.li
            if max1<d:
                max1=i
        for i in self.ldown+self.lift_inside:
            d=i-self.li
            if min1>d:
                min1=i
        self.max=max(self.max,max1,self.li)
        self.min=min(self.min,min1,self.li)
        ##print self.max,self.min
        self.state=state
        self.assign_states()

    def assign_states(self):
        if self.state=="UP":
            self.state="UP"
            self.moveup()
        elif self.state=="DOWN":
            self.state="DOWN"
            self.movedown()
        else:
            print "WRONG STATE CALLED"


    def moveup(self):
        #print self.li,
        #print "up"
        last=self.last
        d=0
        l=[]
        for i in range(self.last,self.max+1):
            self.last_floor_b4trans=i
            if i in self.lift_inside or i in self.lup:
                d+=abs(i-last)
                last=i
                if i==self.li and i==self.lfinal[len(self.lfinal)-1]:
                    if i in self.lup:
                        self.lup.remove(i)
                    if i in self.lift_inside:
                        self.lift_inside.remove(i)
                    continue
                else:
                    l.append(i)
                if i in self.lup:
                    self.lup.remove(i)
                if i in self.lift_inside:
                    self.lift_inside.remove(i)
                if self.lift_inside==[] and self.lup==[] and self.ldown==[i]:
                    self.ldown.remove(i)
            if i==self.max and i in self.ldown:
                #d+=self.max-last
                #last=self.max
                #l.append(self.max)
                self.ldown.remove(i)
        #print self.lup,self.ldown,self.lift_inside
        self.last=last
        #print self.last
        #print d,l
        self.d+=d
        self.lfinal+=l
        self.count+=1

        #print self.d,self.lfinal

        if self.count<=2:
            self.Halt()
            self.state="DOWN"
            self.movedown()
    

    def movedown(self):
        #print "down"
        #print self.li,
        l=[]
        d=0
        last=self.last
        #print self.last_floor_b4trans
        for i in range(self.last,self.min-1,-1):
            self.last_floor_b4trans=i
            if i in self.lift_inside or i in self.ldown:
                d+=(last-i)
                last=i
                if i==self.li and i==self.lfinal[len(self.lfinal)-1]:
                    if i in self.ldown:
                        self.ldown.remove(i)
                    if i in self.lift_inside:
                        self.lift_inside.remove(i)
                    continue
                else:
                    l.append(i)
                    if i in self.ldown:
                        self.ldown.remove(i)
                    if i in self.lift_inside:
                        self.lift_inside.remove(i)
                    if self.lift_inside==[] and self.ldown==[] and self.lup==[i]:
                        self.lup.remove(i)
        
            if i==self.min and i in self.lup:
                self.lup.remove(i)
        #print self.lup,self.ldown,self.lift_inside
        self.last=last
        #print d,l
        self.d+=d
        self.lfinal+=l
        self.count+=1

        #print self.d,self.lfinal

        if self.count<=2:
            self.Halt()
            self.state="UP"
            self.moveup()

    def Halt(self):
        if self.state=="UP":
            self.lfinal+=["UP TO DOWN"]
        else:
            self.lfinal+=["DOWN TO UP"]


    


'''def chk1(self):
    d21,l21=self.movedown()
    d22,l22=self.moveup()
    d23,l23=self.movedown()
    #print d21+d22+d23,l21+l22+l23
    self.li=2
    self.lift_inside=[1,3]
    self.lup=[3,4]
    self.ldown=[]
    self.last=2
    self.last_floor_b4trans=2
    return d21+d22+d23,[self.li]+l21+l22+l23

def chk2(self):
    d21,l21=self.moveup()
    d22,l22=self.movedown()
    d23,l23=self.moveup()
    #print l21,l22,l23
    #print d21+d22+d23,l21+l22+l23
    return d21+d22+d23,[self.li]+l21+l22+l23'''

l1up,l1down,l2up,l2down=[],[],[],[]
print "Enter number of floors"
maxfloors=int(raw_input())
print "Enter the value of initial floor"
l1i=int(raw_input())
print "Enter the inside pressed buttons"
l1ift_inside=raw_input().split()
l2ift_inside=[]
for i in l1ift_inside:
    l2ift_inside.append(int(i))

for i in range(0,len(l1ift_inside)):
    l1ift_inside[i]=int(l1ift_inside[i])
   
print "Enter the floors along with U or D"  
l1=raw_input().split()
for i in l1:
    if i[1]=="U":
        l1up.append(int(i[0]))
        l2up.append(int(i[0]))
    elif i[1]=="D":
        l1down.append(int(i[0]))
        l2down.append(int(i[0]))
#print ldown,lup,lift_inside,li

m1 = StateMachine()
m1.add_states(l1i,l1up,l1down,l1ift_inside,maxfloors)
#print m1.ldown
m1.run("UP")


m2 = StateMachine()
m2.add_states(l1i,l2up,l2down,l2ift_inside,maxfloors)
#print m2.ldown
m2.run("DOWN")



if m1.d<=m2.d:
    for i in m1.lfinal:
        print str(i)+">-",
else:
    for i in m2.lfinal:
        print str(i)+">-",