from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.uix.switch import Switch

import random


all_notes = ('do-1', 're-1', 'mi-1', 'fa-1', 'sol-1', 'la-1', 'si-1', 'do-2', 're-2', 'mi-2', 'fa-2', 'sol-2', 'la-2', 'si-2', 'do-3', 're-3', 'mi-3', 'fa-3', 'sol-3', 'la-3', 'si-3')
nota = ''

class Container(BoxLayout):

    right = 0
    wrong = 0


    def butt(self, x):
            self.do.disabled = x
            self.re.disabled = x
            self.mi.disabled = x
            self.fa.disabled = x
            self.sol.disabled = x
            self.la.disabled = x
            self.si.disabled = x
            
            
    def start(self):
        global nota
        x = all_notes[random.randrange(0, 21)]
        x1 = x.split('-')
        nota = x1[0]
        self.img.source = 'img/{}.jpg'.format(x)
        self.next.disabled = True
        self.butt(False)   
        self.otvet.color = 1, 1, 1, 1
        self.otvet.text = 'ваш ответ?'
        
        
    def check(self, slug):
        global nota
        if slug == nota:
            global right
            self.right += 1            
            self.rig.text = str(self.right)
            self.butt(True)
            self.next.disabled = False
            self.otvet.color = 1, 1, 1, 1
            self.otvet.text = 'правильно'
        else:
            global wrong
            self.wrong += 1  
            self.wro.text = str(self.wrong)
            self.butt(True)
            self.next.disabled = False
            self.otvet.color = 1, 0, 0, 1
            self.otvet.text = 'нет, это - {}'.format(nota)
            
        
        


class MyApp(App):
    def build(self):
        return Container()
  

if __name__ == '__main__':
    MyApp().run()