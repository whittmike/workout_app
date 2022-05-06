import kivy

from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

import random



# -- =============================================================================

def get_workout(wo_type, wo_type_not, rest_chance, rest_chance_mod):

    

    # --- if no input for rest chance is detected

    if(rest_chance == '' or not rest_chance.isdigit()):

        rest_chance = '100'

    

    # --- all workout lists

    ub_dic = {'merkins':[20,40], 'burpees':[15,30], 'overhead press':[20,40], 'curls':[20,60], 'dips':[20,60], 'skull crushers':[20,50], 'bent over rows':[20,60]}

    lb_dic = {'squats':[20,60], 'split lunges':[15,30], 'thrusters':[15,30], 'box jump':[15,30]}

    cb_dic = {'big boy situps':[20,60], 'starfish crunches':[15,40], 'flutter kicks':[20,60], 'mountain climbers':[20,60]}

    all_dic = dict(ub_dic)

    all_dic.update(lb_dic)

    all_dic.update(cb_dic)

    

    # --- rest chance redefine

    if(wo_type == 'all'):

        rest_chance = int(int(rest_chance)*rest_chance_mod)

    else:

        rest_chance = int(rest_chance)

    

    # --- setup to see if we get rest

    is_rest = 0

    rest_lst = list(range(1, rest_chance))

    magic_number = 1

    rest_number = random.choice(rest_lst)

    

    # --- see if we get rest

    if(rest_number == magic_number):

        is_rest = 1

        

    # --- get workout

    if(wo_type == 'upper'):

        # --- get workout type

        str_out_01 = random.choice([i for i in list(ub_dic.keys()) if i != wo_type_not.split('\n')[0]])

        # --- get workout amount

        str_out_02 = str(random.choice(list(range(ub_dic[str_out_01][0], ub_dic[str_out_01][1]))))

        # --- final output

        str_out = str_out_01 + '\nx' + str_out_02

        

    if(wo_type == 'lower'):

        # --- get workout type

        str_out_01 = random.choice([i for i in list(lb_dic.keys()) if i != wo_type_not.split('\n')[0]])

        # --- get workout amount

        str_out_02 = str(random.choice(list(range(lb_dic[str_out_01][0], lb_dic[str_out_01][1]))))

        # --- final output

        str_out = str_out_01 + '\nx' + str_out_02

        

    if(wo_type == 'core'):

        # --- get workout type

        str_out_01 = random.choice([i for i in list(cb_dic.keys()) if i != wo_type_not.split('\n')[0]])

        # --- get workout amount

        str_out_02 = str(random.choice(list(range(cb_dic[str_out_01][0], cb_dic[str_out_01][1]))))

        # --- final output

        str_out = str_out_01 + '\nx' + str_out_02

        

    if(wo_type == 'all'):

        # --- get workout type

        str_out_01 = random.choice([i for i in list(all_dic.keys()) if i != wo_type_not.split('\n')[0]])

        # --- get workout amount

        str_out_02 = str(random.choice(list(range(all_dic[str_out_01][0], all_dic[str_out_01][1]))))

        # --- final output

        str_out = str_out_01 + '\nx' + str_out_02

        

    if(is_rest == 1):

        str_out = 'REST!!!'

    

    # --- return output

    return(str_out)



# -- =============================================================================

class MyGridLayout(GridLayout):

	

    # Initialize infinite keywords

    def __init__(self, **kwargs):

        

        # Call grid layout constructor

        super(MyGridLayout, self).__init__(**kwargs)

        

        # bottom col

        self.cols = 1

        

        # ---------------------------------------- [ first grid ] -----

        # Define the first grid layout for this App -- row_default_height=100

        self.grid_01 = GridLayout()

        

        # Set number of columns in our new top_grid

        self.grid_01.cols = 2

        

        # Add upper body button

        self.grid_01.ub_lab = Label(text = "", font_size = 44)

        self.grid_01.ub_button = Button(text ="UPPER", font_size = 54)

        self.grid_01.ub_button.bind(on_press = self.ub_fun)

        # add both as widget

        self.grid_01.add_widget(self.grid_01.ub_lab)

        self.grid_01.add_widget(self.grid_01.ub_button)

        

        # Add lower body button

        self.grid_01.lb_lab = Label(text = "", font_size = 44)

        self.grid_01.lb_button = Button(text ="LOWER", font_size = 54)

        self.grid_01.lb_button.bind(on_press = self.lb_fun)

        # add both as widgets

        self.grid_01.add_widget(self.grid_01.lb_lab)

        self.grid_01.add_widget(self.grid_01.lb_button)

        

        # Add core body button

        self.grid_01.cb_lab = Label(text = "", font_size = 44)

        self.grid_01.cb_button = Button(text ="CORE", font_size = 54)

        self.grid_01.cb_button.bind(on_press = self.cb_fun)

        # add both as widgets

        self.grid_01.add_widget(self.grid_01.cb_lab)

        self.grid_01.add_widget(self.grid_01.cb_button)

        

        # Add all body button

        self.grid_01.f3_lab = Label(text = "", font_size = 44)

        self.grid_01.f3_button = Button(text ="ALL", font_size = 54)

        self.grid_01.f3_button.bind(on_press = self.f3_fun)

        # add both as widgets

        self.grid_01.add_widget(self.grid_01.f3_lab)

        self.grid_01.add_widget(self.grid_01.f3_button)

        

        # Add the new top_grid to our appf3

        self.add_widget(self.grid_01)

        

        # ---------------------------------------- [ second grid ] -----

        # Define the first grid layout for this App

        self.grid_02 = GridLayout(size_hint_y = 0.18)

        

        # Set number of columns in our new top_grid

        self.grid_02.cols = 3

        

        # Add upper body button

        self.grid_02.list_lab = Label(text = "1:100\nREST", font_size = 44)

        self.grid_02.list_but = Button(text = "SUBMIT", font_size = 54)

        self.grid_02.list_but.bind(on_press = self.rest_chance_fun)

        self.grid_02.list_txt = TextInput(font_size = 44)

        # add widgets

        self.grid_02.add_widget(self.grid_02.list_lab)

        self.grid_02.add_widget(self.grid_02.list_txt)

        self.grid_02.add_widget(self.grid_02.list_but)

                

        # Add the new top_grid to our app

        self.add_widget(self.grid_02)

        

        # ---------------------------------------- [ bottom grid ] -----

        # clear workout button

        self.clear_button_01 = Button(text = "CLEAR WORKOUTS", font_size = 64, size_hint_y = 0.25)

        self.clear_button_01.bind(on_press = self.clear_wo)

        self.add_widget(self.clear_button_01)        

        

    # ---------------------------------------- [ tob grid function ] -----

    # --- upper body function

    def ub_fun(self, instance):

        # randomly chosen option

        ub_out_txt = get_workout(wo_type = "upper", wo_type_not = self.grid_01.ub_lab.text, rest_chance = self.grid_02.list_txt.text, rest_chance_mod = 1)

        # set to label 

        self.grid_01.ub_lab.text = ub_out_txt

    

    # --- lower body function

    def lb_fun(self, instance):

        # randomly chosen option

        lb_out_txt = get_workout(wo_type = "lower", wo_type_not = self.grid_01.lb_lab.text, rest_chance = self.grid_02.list_txt.text, rest_chance_mod = 1)

        # set to label 

        self.grid_01.lb_lab.text = lb_out_txt

    

    # --- core function

    def cb_fun(self, instance):

        # randomly chosen option

        cb_out_txt = get_workout(wo_type = "core", wo_type_not = self.grid_01.cb_lab.text, rest_chance = self.grid_02.list_txt.text, rest_chance_mod = 1)

        # set to label 

        self.grid_01.cb_lab.text = cb_out_txt

    

    # --- core function

    def f3_fun(self, instance):

        # randomly chosen option

        f3_out_txt = get_workout(wo_type = "all", wo_type_not = self.grid_01.f3_lab.text, rest_chance = self.grid_02.list_txt.text, rest_chance_mod = 0.50)

        # set to label 

        self.grid_01.f3_lab.text = f3_out_txt

        

    def rest_chance_fun(self, instance):

        # --- define rest chance 

        rest_chance = self.grid_02.list_txt.text

        # --- what to do if improper input

        if(rest_chance == '' or not rest_chance.isdigit()):

            rest_chance = '100'

        # --- reformat text        

        self.grid_02.list_lab.text = f"1:{rest_chance}\nREST"

    

    # --- clear all workouts function

    def clear_wo(self, instance):

        # clear workouts

        self.grid_01.ub_lab.text = ''

        self.grid_01.lb_lab.text = ''

        self.grid_01.cb_lab.text = ''

        self.grid_01.f3_lab.text = ''

        

# -- =============================================================================

class MyApp(App):

	def build(self):

		return MyGridLayout()



# -- =============================================================================

if __name__ == '__main__':

	MyApp().run()
