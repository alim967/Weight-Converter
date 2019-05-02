##weightproject.py
##This program will convert weight in pounds to grams, kilograms and ounces using graphical interface.
##Author: Abdul Alim
##Dated: April 28, 2019

from graphics import *

def convertGrams(pounds):
    if pounds >= 0:
        totalgrms = float(pounds * 453.6)
        return totalgrms
    else:
        print("Invalid input, please enter only the positive number on entry.")

def convertKilograms(pounds):
    if pounds >= 0:
        totalkilo = float(pounds * 0.4536)
        return totalkilo
    
def convertOunces(pounds):
    if pounds >= 0:
        totalouns = float(pounds * 16)
        return totalouns

def main():
    print("___________________________Welcome_________________________\n")
    print("This program will convert the weight from pounds to grams, kilograms and ounces\n")
    print('\nNote:"To close the program please enter any letter or negetive number."')
    win = GraphWin("",500,500)
    win.setBackground('gray')
    
    heading = Text(Point(250,40),"Weight Converter")
    heading.setFace('arial')
    heading.setSize(24)
    heading.setStyle('bold')
    heading.draw(win)
    
    
    Text(Point(140,150),"Grams").draw(win)
    grams = Entry(Point(250,180),30)
    grams.setFill('white')
    grams.setText("0.0")
    grams.draw(win)
    
    Text(Point(150,230),"Kilograms").draw(win)
    kilogrms = Entry(Point(250,260),30)
    kilogrms.setFill('white')
    kilogrms.setText("0.0")
    kilogrms.draw(win)
    
    Text(Point(140,310),"Ounces").draw(win)
    ounces = Entry(Point(250,340),30)
    ounces.setFill('white')
    ounces.setText("0.0")
    ounces.draw(win)
    
    lbs = Text(Point(410,100),"lb")
    lbs.setStyle('bold')
    lbs.draw(win)

    rect1 = Rectangle(Point(110,120), Point(390,80))
    rect1.setFill('white')
    rect1.draw(win)

    rect = Rectangle(Point(270,400), Point(390,360))
    rect.setFill('orange2')
    rect.setOutline('orange2')
    rect.draw(win)

    button = Text(Point(330,380),"Convert")
    button.setTextColor('white')
    button.draw(win)

    input1 = Entry(Point(250,100),30)
    input1.setFill('white')
    input1.draw(win)

    while True:
        '''I:enter weight in pounds; P: convert the weight into grams, kilograms and ounces; O: the converted weight in grams, kilograms, and ounces'''
        
        win.getMouse()
        pounds = eval(input1.getText())
        
        if pounds <= 0:
            invalid = Text(Point(250,420),"Invalid input,please enter only positive number.")
            invalid.setSize(14)
            invalid.setTextColor('red')
            invalid.draw(win)
        else:    
            totalgrms = convertGrams(pounds)
            totalkilo = convertKilograms(pounds)
            totalouns = convertOunces(pounds)
       
        grams.setText(round(totalgrms, 2))
        kilogrms.setText(round(totalkilo, 2))
        ounces.setText(round(totalouns,2))
    
        
main()
