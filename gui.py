from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.uix.button import Button
import math
import numpy as np
import pickle
from translate_ import Translate

'''
To examine the letter, ``show`` function of test_plot.py can be used.
See the documentation of the function to know more.
Import the following if calling show()

from test_plot import show
'''

#Change screen color to White
Window.clearcolor = (1, 1, 1, 1)
#Initialised pixel value data of all the six boxes.
input_data = np.zeros([6, 1024], np.int32)
#variable to count number of boxes utilized
no_of_boxes = 0

def get_word(lang, pred):
    '''
    Converts the estimator's predicted labels into a word of the chosen language.

    Parameters
    ----------
    lang: The input language of type str.
          The string follows the ISO standard names or RFC3066 code for language code.
          Codes available at http://www.i18nguy.com/unicode/language-identifiers.html

    pred: The predictions of the input images.
          Converts collection o labels into a word.

    Returns
    -------
    word: The word of the desired input language.
    '''
    word = ''
    english_order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #ADD hindi_order
    for ans in pred:
        if lang == 'en':
            word= word + english_order[int(ans)-1]
    return word


class DrawPencil(Widget):
    '''
    Takes care of the movement of pointer and records the pixels moved and store it into the input_data.
    '''
    pencil_active=BooleanProperty(True)
    def on_touch_down(self, touch):
        if not self.pencil_active:
            return
        with self.canvas:
            Color(0,0,0,1)
            touch.ud["line1"] = Line( points = (touch.x, touch.y), width=3)

    def on_touch_move(self, touch):
        if 'line1' in touch.ud:
            global no_of_boxes, input_data
            touch.ud["line1"].points += [touch.x, touch.y]
            '''
            Records the movement of pointer to input_data.
            '''
            for x in range(-2 + int(touch.x), 2 + int(touch.x)):
                for y in range(-2 + int(touch.y), 2 + int(touch.y)):
                    if (x - int(touch.x))*(x - int(touch.x)) + (y - int(touch.y))*(y - int(touch.y)) < 2*2 :
                        if y > 0.6*self.height and y < 0.7*self.height:
                            relative_x = (x*32*12)/(self.width)
                            pixel_number_x = math.floor(relative_x % 32)
                            box_number = math.floor(relative_x/32)
                            no_of_boxes = (box_number+1)/2
                            pixel_number_y = math.floor(((y - 0.6*self.height)*32)/(0.1*self.height))
                            if box_number%2 == 1:
                                input_data[(box_number-1)/2][32*(31-pixel_number_y) + pixel_number_x] = 255

class MainScreen(Screen):
    def predict_inputs(self):
        '''
        Predict the translation of input word and display the final result.
        '''
        ans = np.zeros(int(no_of_boxes))
        if self.ids.from_language.text == 'English':
            pickle_in = open('english_without_processing_2.pickle','rb')
        if self.ids.from_language.text == 'Hindi':
            pickle_in = open('hindi.pickle', 'rb')
        mlp=pickle.load(pickle_in)
        prediction = mlp.predict(input_data[0:int(no_of_boxes)][:])
        print(prediction)
        if self.ids.from_language.text == 'English':
            convert_from = 'en'
        if self.ids.from_language.text == 'Hindi':
            convert_from = 'hi'
        if self.ids.to_language.text == 'English':
            convert_to = 'en'
        if self.ids.to_language.text == 'Hindi':
            convert_to = 'hi'

        input_word = get_word('en', prediction)
        output_word = Translate(input_word, convert_to, convert_from)
        self.ids.output_one.text = output_word

    def draw_rectangle(self):
        '''
        Draws 6 rectangles when Start button is pressed.
        '''
        #Clears input_data to zero on Start Button Press
        input_data.fill(0)
        #Clears output of the translation.
        self.ids.output_one.text = ' '
        #Draws rectangle when 'Press is submitted'
        with self.canvas:
            Color(0,0,0,1)
            Rectangle_list = []
            for i in range(0,6):
                Rectangle_list.append(Line(points = (((2*i+1)*self.width/12, self.height*0.7),((2*i+2)*self.width/12, self.height*0.7)), width=2))
                Rectangle_list.append(Line(points = (((2*i+1)*self.width/12, self.height*0.6),((2*i+2)*self.width/12, self.height*0.6)), width=2))
                Rectangle_list.append(Line(points = (((i+1)*self.width/12, self.height*0.7),((i+1)*self.width/12, self.height*0.6)), width=2))
                Rectangle_list.append(Line(points = (((i+7)*self.width/12, self.height*0.7),((i+7)*self.width/12, self.height*0.6)), width=2))


class ScreenManagement(ScreenManager):
    pass

presentaion = Builder.load_file("gui_features.kv")

class TranslateApp(App):
    def build(self):
            return presentaion

if __name__=="__main__":
    TranslateApp().run()
