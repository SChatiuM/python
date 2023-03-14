import turtle

#region def

def dragon_curve(level,n):
    if(n==13): return level
    newlevel=''
    for i in level:
        if(i=='+'): newlevel=newlevel+'+'
        elif(i=='-'): newlevel=newlevel+'-'
        elif(i=='F'): newlevel=newlevel+'F'
        elif(i=='X'): newlevel=newlevel+'X+YF+'
        elif(i=='Y'): newlevel=newlevel+'-FX-Y'
    level=newlevel
    return dragon_curve(level,n+1)

def serpinski_triangle(level,n):
    if(n==9): return level  #n=7 in original
    newlevel=''
    for i in level:
        if(i=='+'): newlevel=newlevel+'+'
        elif(i=='-'): newlevel=newlevel+'-'
        elif(i=='F'): newlevel=newlevel+'F-G+F+G-F'
        elif(i=='G'): newlevel=newlevel+'GG'
    level=newlevel
    return serpinski_triangle(level,n+1)

def mine_fraktal(level,n):
    if(n==20): return level
    newlevel=''
    for i in level:
        if(i=='+'): newlevel=newlevel+'+'
        if(i=='-'): newlevel=newlevel+'-'
        if(i=='X'): newlevel=newlevel+'X+YF'
        if(i=='Y'): newlevel=newlevel+'-FX-Y'
    level=newlevel
    return mine_fraktal(level,n+1)


#endregion def

#region global

way_dragon=dragon_curve('FX',1)
way_triangle=serpinski_triangle('F-G-G',1)
way_mine=mine_fraktal('FX+FX+FX',1)

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)

#endregion global

#region main

answ=input("Drawing triangle (t) or dragon (d) or mine (m)?:\t")
if(answ=='d' or answ=='D'):
    for i in way_dragon:
        if(i=='-'): t.left(90)
        elif(i=='+'): t.right(90)
        else: t.forward(3)
if(answ=='t' or answ=='T'):
    for i in way_triangle:
        if(i=='-'): t.left(120)
        elif(i=='+'): t.right(120)
        else: t.forward(5) #5 in original
if(answ=='m' or answ=='M'):
    for i in way_mine:
        if(i=='-'): t.left(90)
        if(i=='+'): t.right(90)
        else: t.forward(5)


turtle.exitonclick()

#endregion main
