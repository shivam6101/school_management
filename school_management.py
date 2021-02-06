from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory
<<login>login>:
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#9400D3')
            Rectangle:
                size:self.size
                pos:self.pos
        Image:
            pos_hint:{'x':.0,'y':.3}
            size_hint:.3,.5
            source:'kisspng-computer-icons-login-tilted-planet-ltd-user-login-interface-5ad895a8725044.4591044515241435284682.png'
                
        Label:
            text:'STUDENT DATABASE'
            color:0,0,0,1
            bold:True
            pos_hint:{'x':0,'y':.9}          
            size_hint:1,.1
            font_size:30

        
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C0C0C0')
                Rectangle:
                    size:self.size
                    pos:self.pos
          
        FloatLayout:
            size_hint:.6,.54
            pos_hint:{'x':.35,'y':.257}
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C0C0C0')
                Rectangle:
                    size:self.size
                    pos:self.pos
                
            FloatLayout:                   
                pos_hint:{'x':.14,'y':.62}
                Label:
                    text:'USER LOGIN'
                    bold:True
                    font_size:24
                    text_size: self.size
                    pos_hint:{'x':-.02,'y':.22}
                    color:0,0,0,1
                Label:
                    text:"User Name"
                    font_size:20
                    text_size: self.size
                    pos_hint:{'x':.14,'y':.1}
                    color:0,0,0,1
                TextInput:
                    size_hint_y:.1
                    size_hint_x:.31
                    pos_hint:{'x':.135,'y':.0}  
                    multiline:False
                    background_color:0,0,0,0
                Label:
                    text:'__________________________'
                    text_size: self.size
                    pos_hint:{'x':.14,'y':.022}
                    font_size:17
                    color:0,0,0,1
                
                Label:
                    text:"Password"
                    font_size:20
                    text_size: self.size
                    pos_hint:{'x':.14,'y':-.22}

                    color:0,0,0,1
                TextInput:
                    size_hint_y:.1
                    size_hint_x:.31
                    focus:True
                    pos_hint:{'x':.135,'y':-.32}  
                    multiline:False
                    background_color:0,0,0,0
                Label:
                    text:'__________________________'
                    text_size: self.size
                    pos_hint:{'x':.14,'y':-.3}
                    font_size:17
                    color:0,0,0,1
                Button:
                    text:'LOG IN'
                    pos_hint:{'x':.23,'y':-.52}
                    size_hint:.2,.15
                    background_color:get_color_from_hex('#9400D3')
                    on_press:
                        root.manager.current='classes'

#########################################################################################################33
<<main>main>:
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#9400D3')
            Rectangle:
                size:self.size
                pos:self.pos            
        Label:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C0C0C0')
                Rectangle:
                    size:self.size
                    pos:self.pos
        ImageButton:  
            pos_hint:{'x':.0,'y':.9} 
            size_hint:.1,.1
            source:'green-arrow-png-16641.png'     
            on_press:
                root.manager.current='classes'
        ImageButton:  
            pos_hint:{'x':.05,'y':.7} 
            size_hint:.15,.15
            source:'PinClipart.com_school-owl-clipart_393977.png'
            on_press:
                root.manager.current='nursery'
            

<<classes>classes>:
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#9400D3')
            Rectangle:
                size:self.size
                pos:self.pos            
        Label:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C0C0C0')
                Rectangle:
                    size:self.size
                    pos:self.pos
                    
        Image:
            pos_hint:{'x':.4,'y':.9}
            size_hint:.3,.1
            source:'class4b.png'

        ImageButton:  
            pos_hint:{'x':.0,'y':.9} 
            size_hint:.1,.1
            source:'green-arrow-png-16641.png'     
            on_press:
                root.manager.current='login'
        ImageButton:  
            pos_hint:{'x':.05,'y':.7} 
            size_hint:.15,.15
            source:'PinClipart.com_school-owl-clipart_393977.png'
            on_press:
                root.manager.current='nursery'
        Label:
            text:'Nursery' 
            pos_hint:{'x':.1,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.2,'y':.7} 
            size_hint:.15,.15
            source:'58c5804509e8bc1b42c7793f (1).png'    
        Label:
            text:'First' 
            pos_hint:{'x':.26,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.35,'y':.7} 
            size_hint:.15,.15
            source:'PinClipart.com_laundry-line-clipart_914581.png'    
        Label:
            text:'Second' 
            pos_hint:{'x':.4,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.5,'y':.7} 
            size_hint:.15,.15
            source:'58c5801409e8bc1b42c7793d.png'    
        Label:
            text:'Third' 
            pos_hint:{'x':.56,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.65,'y':.7} 
            size_hint:.15,.15
            source:'number4_PNG15037.png'    
        Label:
            text:'Fourth' 
            pos_hint:{'x':.71,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.8,'y':.7} 
            size_hint:.15,.15
            source:'number5_PNG15064.png'    
        Label:
            text:'Fifth' 
            pos_hint:{'x':.865,'y':.66}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17

        ImageButton:  
            pos_hint:{'x':.05,'y':.4} 
            size_hint:.15,.15
            source:'clipart-numbers-six-15.png'    
        Label:
            text:'Sixth' 
            pos_hint:{'x':.1,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.2,'y':.4} 
            size_hint:.15,.15
            source:'number7_PNG18642.png'    
        Label:
            text:'Seventh' 
            pos_hint:{'x':.25,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.35,'y':.4} 
            size_hint:.15,.15
            source:'number8_PNG18676.png'    
        Label:
            text:'Eighth' 
            pos_hint:{'x':.4,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.5,'y':.4} 
            size_hint:.15,.15
            source:'MRT_Singapore_Destination_9.png'    
        Label:
            text:'Ninth' 
            pos_hint:{'x':.56,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.65,'y':.4} 
            size_hint:.15,.15
            source:'PinClipart.com_copyright-free-clip-art_1267787.png'    
        Label:
            text:'Tenth' 
            pos_hint:{'x':.71,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        ImageButton:  
            pos_hint:{'x':.8,'y':.4} 
            size_hint:.15,.15
            source:'red-rounded-with-number-11-md.png'    
        Label:
            text:'Eleventh' 
            pos_hint:{'x':.85,'y':.36}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17

        ImageButton:  
            pos_hint:{'x':.05,'y':.1} 
            size_hint:.15,.15
            source:'366933.png'    
        Label:
            text:'Tweleve' 
            pos_hint:{'x':.1,'y':.06}
            text_size:self.size
            bold:True
            color:0,0,0,1
            font_size:17
        
<<nursery>nursery>:
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#9400D3')
            Rectangle:
                pos:self.pos
                size:self.size
        BoxLayout:
            size_hint:.3,.9
            pos_hint:{'x':0}
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#e5e5e5')
                Rectangle:
                    pos:self.pos
                    size:self.size
            BoxLayout:
                ScrollView:
                    bar_width:10
                    scroll_type:['bars']    
                    FloatLayout:
                        Label:
                            text:'SEARCH STUDENTS'
                            color:0,0,0,1
                            font_size:24
                            bold:True
                            pos_hint:{'x':.02,'y':.9}
                            text_size:self.size
                        Label:
                            text:'Student Detail'
                            color:get_color_from_hex('#808080')
                            font_size:17
                            bold:True
                            pos_hint:{'x':.02,'y':.8}
                            text_size:self.size
                        Label:
                            text:'Name'
                            color:0,0,0,1
                            font_size:15
                            pos_hint:{'x':.2,'y':.7}
                            text_size:self.size
                        CheckBox:  
                            size_hint_x: .10
                            size_hint_y: .10
                            color:0,0,0,1
                            background_color:0,0,0,1
                            pos_hint:{'x':.07,'y':.664}
                            
                        TextInput:
                            pos_hint:{'x':.19,'y':.66}
                            size_hint:.65,.05
                            font_size:12
                            multiline:False
                            background_color:0,0,0,0
                        Label:
                            text:'_____________________________'
                            pos_hint:{'x':.2,'y':.66}
                            color:0,0,0,1
                            text_size:self.size

                        Label:
                            text:'Roll No'
                            color:0,0,0,1
                            font_size:15
                            pos_hint:{'x':.2,'y':.58}
                            text_size:self.size
                        CheckBox:  
                            size_hint_x: .10
                            size_hint_y: .10
                            color:0,0,0,1
                            background_color:0,0,0,1
                            pos_hint:{'x':.07,'y':.544}
                        TextInput:
                            pos_hint:{'x':.19,'y':.54}
                            size_hint:.65,.05
                            font_size:12
                            background_color:0,0,0,0
                            multiline:False
                        Label:
                            text:'_____________________________'
                            pos_hint:{'x':.2,'y':.54}
                            color:0,0,0,1
                            text_size:self.size

                        Label:
                            text:'D.O.B'
                            color:0,0,0,1
                            font_size:15
                            pos_hint:{'x':.2,'y':.46}
                            text_size:self.size
                        CheckBox:  
                            size_hint_x: .10
                            size_hint_y: .10
                            color:0,0,0,1
                            background_color:0,0,0,1
                            pos_hint:{'x':.07,'y':.424}
                        TextInput:
                            pos_hint:{'x':.19,'y':.42}
                            size_hint:.65,.05
                            font_size:12
                            background_color:0,0,0,0
                            multiline:False
                        Label:
                            text:'_____________________________'
                            pos_hint:{'x':.2,'y':.42}
                            color:0,0,0,1
                            text_size:self.size

                        Label:
                            text:'Mobile'
                            color:0,0,0,1
                            font_size:15
                            pos_hint:{'x':.2,'y':.34}
                            text_size:self.size
                        CheckBox:  
                            size_hint_x: .10
                            size_hint_y: .10
                            color:0,0,0,1
                            background_color:0,0,0,1
                            pos_hint:{'x':.07,'y':.304}
                        TextInput:
                            pos_hint:{'x':.19,'y':.3}
                            size_hint:.68,.05
                            font_size:12
                            background_color:0,0,0,0
                            multiline:False
                        Label:
                            text:'_____________________________'
                            pos_hint:{'x':.2,'y':.3}
                            color:0,0,0,1
                            text_size:self.size

                            

                            
                        


                
        BoxLayout:
            size_hint:.6,.9
            pos_hint:{'x':.32}
            ScrollView:
                bar_width:10
                scroll_type:['bars']
                GridLayout:
                    id:container
                    size_hint_x:.97
                    size_hint_y:None
                    cols:3
                    row_default_height:200
                    height:self.minimum_height
    
        Label:
            pos_hint:{'x':0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C0C0C0')
                Rectangle:
                    size:self.size
                    pos:self.pos
        ImageButton:  
            pos_hint:{'x':.0,'y':.9} 
            size_hint:.1,.1
            source:'green-arrow-png-16641.png'     
            on_press:
                root.manager.current='classes'
        Image:
            pos_hint:{'x':.4,'y':.9}
            size_hint:.3,.1
            source:'nursery_7968.png' 
        ImageButton:  
            pos_hint:{'x':.92,'y':.06} 
            size_hint:.1,.1
            source:'icons8-add-user-male-48.png'     
            on_press:
                container.add_widget(F.custom())





<<custom@BoxLayout>custom@BoxLayout>:
    TextInput:
        read_only:True



''')
class SimplePopup(Popup):
    pass
class login(Screen):
    pass
class main(Screen):
    pass
class classes(Screen):
    pass
class nursery(Screen):
    pass
class ImageButton(ButtonBehavior,Image):
	pass
class imageButton(ButtonBehavior,Image,Popup):
	pass
class scrollview(Screen):
    pass

sm=ScreenManager()
sm.add_widget(login(name='login'))

sm.add_widget(classes(name='classes'))
sm.add_widget(nursery(name='nursery'))
sm.add_widget(main(name='main'))
class main(App):
    def build(self):
        return sm
if __name__=='__main__':
    main().run()