Hello from pygamer.{the creator of this module}

#-- project discription--
    it's an simple project that can help you create awsome gui.
#-------------------------

#-- contains --
    Two files -_
                |
                V
        1) window.py
        2) tools.py
description about files is contained within them as comment
#-------------------

#----------support -------------------
consider supporting by suscribing my channel on 
youtube:->https://www.youtube.com/channel/UCNj9jZBVxRWm7TA5g2K7XtA
#--------------------------------------

#------This version contains---------------

@featurs-
        |
        V
1)Now functions can be called with arguments through buttons
2)importing module gives an Hello message from developer
3)You can use your own font.

#---------------------------------------------

@ 1)-
    |
    V
Example:
def Take_input(args):#Input must be taken as a list
        print(args[0])#you can then target a specific argument      
        # by indexing method as above


#------an example of whole module-------
import pygamergui
from pygamergui import tools,window
from rich import print,inspect
def b1test(args):
    t1.text="use"
def b2test(args):
    t1.text="hello"


b1=tools.simple_button(target=b1test,
                  text='use',
                  fg='white',
                  w=75,
                  h=50,
                  color=(0,175,250),
                  args=[1]
                  )

b2=tools.simple_button(target=b2test,
                  fg='white',
                  text="hello",
                  w=100,
                  h=50,
                  color=(0,175,250)
                  )

t1=tools.text("what to use??")

r1=tools.button_radio(radius=30,color='cyan')

s1=tools.slider(300,
                550,
                h=10,
                corner_round=10,
                color='purple',
                t1_align='side',
                text_size=20,
                )

def update():
    b1.show_no_anemi(200,400,window=windowm,corner_round_level=10)
    b2.show_color_change(300,400,window=windowm,corner_round_level=10)

    t1.show(windowm,175,175)

    r1.show(windowm,300,300)

    a=s1.show(windowm)
windowm=window.app(title='test',bgcolor=(40,40,40),target=update,update_rate=10)
windowm.run()
#---------------------------------------------------------------------------
