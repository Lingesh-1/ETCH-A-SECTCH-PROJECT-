import turtle as t
import random as r  



myscr=t.Screen()


myscr.setup(width=500,height=400)

israce=True
re= myscr.textinput(title='Make your Bet!!!',prompt='Which Turtle Will Win the RACE? Enter color:').lower()
print(re)



alla=[]








aamaico=['red','green','purple','blue','yellow','orange']


yp=[-70,-40,-10,20,50,80]


for i in range(0,6):
    aamais=t.Turtle(shape='turtle')
    aamais.color(aamaico[i])
    aamais.penup()
    aamais.goto(x=-240,y=yp[i])
    alla.append(aamais)






while israce:
    for i in alla:
        # rdis=
        if i.xcor()>230:
            israce=False
            # print(i.color())
            if re==i.pencolor():
                print(f"You Won!!! The {str(i.pencolor()).upper()} is the Winneerr!!")
            else:
                print(f"You Loss!!! The {str(i.pencolor()).upper()} is the Winneerr!!")
               
        i.forward(r.randint(0,11))
        

# red=t.Turtle()


# sha(red)
# red.color('red')
# co(red)


# red.goto(-240,-140)




# purple=t.Turtle()
# purple.color('purple')


# sha(purple)
# co(purple)


# purple.goto(-240,-80)




# orange=t.Turtle()
# orange.color('orange')


# sha(orange)
# co(orange)


# orange.goto(-240,-20)



# green=t.Turtle()
# green.color('green')


# sha(green)
# co(green)


# green.goto(-240,30)



# blue=t.Turtle()


# blue.color('blue')


# sha(blue)


# co(blue)


# blue.goto(-240,80)





# yellow=t.Turtle()

# yellow.color('yellow')


# sha(yellow)

# co(yellow)


# yellow.goto(-240,140)  

myscr.exitonclick()
