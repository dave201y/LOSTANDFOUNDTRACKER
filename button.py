# button.py
# A simple button widget implemented better than Zelle's text example


from graphics2 import *
import time

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it.
    
    instance variables:
    rect (Rectangle): the rectangle representing the button
    label (Text): the text on the button
    active (bool): indicates whether the button will react to clicks(True)
    """

    def __init__(self, center, width, height, words, color = 'lightgray'):
        """
        Creates a rectangular button, eg:
        button = Button(Point(30,25), 20, 10, 'Quit')
        that is not activated
        
        Params:
        center (Points): the center point of the button
        width (int): the width of the button in pixels
        height (int): the height of the button in pixels
        words (str): the words to go on the button
        color (str): the color of the button
        """ 
        point1, point2 = self._calculate_corner_points(center, width, height)
        
        # create the instance variables
        self.rect = Rectangle(point1,point2)
        self.rect.setFill(color)
        self.label = Text(center, words)
        self.active = True
        self.deactivate()           # change after deactivate method
        
    def _calculate_corner_points(self, center, width, height):
        # calculate the points the rectangle needs
        # from the center, width and height
        halfWidth = width/2.0
        halfHeight = height/2.0
        centerX = center.getX()
        centerY = center.getY()
        xMin = centerX - halfWidth
        xMax = centerX + halfWidth
        yMin = centerY - halfHeight
        yMax = centerY + halfHeight
        point1 = Point(xMin, yMin)
        point2 = Point(xMax, yMax)
        return point1, point2

    def draw(self,window):
        """
        Draws the button on the window
        Params:
        window (GraphWin): window where the button is drawn
        """
        self.rect.draw(window)
        self.label.draw(window)
        pass

    def undraw(self):
        """
        Undraws the button
        """
        self.rect.undraw()
        self.label.undraw()
        pass

    def getLabel(self):
        """
        gets the words on the button
        
        Returns:
        the words on the button
        """
#        word = self.label.getText()
#        return word
        return self.label.getText()
       

    def setLabel(self, newText):
        """
        Sets the label's string of this button to the specified string.
        
        newText (str): the new words to be used for the button's label
        """
        self.label.setText(newText)
      
    
    def isActive(self):
        """"
        Tells true/false is the button is activated (ie. accepting clicks)
        
        Returns:
        True if the button is activated, otherwise False
        """
#        if self.active == True:
#            return True
#        else:
#            return False
        return self.active
       

    def activate(self):
        """
        Sets this button to 'active'.
        """
        self.label.setFill('black')
        self.active = True
        self.rect.setWidth(5)
        
            
        
    
    def deactivate(self):
        
        """
        Sets this button to 'inactive'.
        """
        self.active = False
        self.rect.setWidth(1)
        self.label.setFill('darkgrey')
        
       
    def isClicked(self, point):
        """
        Determines if the button was clicked
        
        Returns:
        True if button active and point is inside
        """
        if self.active:
            left_edge = self.rect.getP1().getX()
            right_edge = self.rect.getP2().getX()
            top_edge = self.rect.getP1().getY()
            bottom_edge = self.rect.getP2().getY()
            
            
            xIsGood = left_edge < point.getX() < right_edge
            yIsGood = top_edge < point.getY() < bottom_edge
            
            if xIsGood and yIsGood:
                return True
            else:
                return False
                
            
            
            
        else:
            return False
      
    def move(self, dx, dy):
        """
        Move the button by offsets dx and dy
        
        Params:
        dx (int): pixels to move horizontally
        dy (int): pixels to move vertically
        """
        self.rect.move(dx, dy)
        self.label.move(dx, dy)


    def __str__(self):
        """
        Creates and returns a string/text version of this button
        
        Returns:
        a string/text version of this button
        """
        corner1 = self.rect.getP1()
        text = "A button with top left corner at: " + str(corner1.getX()) \
               + "," + str(corner1.getY())
        text = text + " with label= " + self.label.getText()
        return text

def main():
    # text code to see if we're on track!
    window = GraphWin("Testing Buttons", 400, 400)
    window.setBackground('white')
    
    myButton = Button(Point(200, 200), 100, 30, "Click Me", 'red')
    print(myButton)
    myButton.draw(window)
    time.sleep(2)
#   myButton.undraw()
    
    print(myButton.getLabel())
    myButton.setLabel("Click Here")

    print(myButton.isActive())
    myButton.activate()
    time.sleep(2)
#    myButton.deactivate()
    
    click = window.getMouse()
    if myButton.isClicked(click):
        window.setBackground('red')

#    myButton.deactivate()

    myButton.move(50, 50)
    click = window.getMouse()
    
    if myButton.isClicked(click):
        window.setBackground('blue')
        myButton.undraw()
        
if __name__ == '__main__':
    main()








