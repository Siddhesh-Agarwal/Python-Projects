# Required Libraries
import tkinter as tk
from math import *

# Conversion Constants For Trigonometric Functions
global convert_constant
convert_constant = '1'
global inverse_convert_constant
inverse_convert_constant = '1'

# Button Design
btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': '#F0F8FF',
    'bg': 'gray12',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': 'gray12'
}

# defining class Calculator
class Calculator:
    def __init__(self, master):
        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = tk.StringVar()
        self.master = master

        top_frame = tk.Frame(master, width = 650, height = 20, bd = 4, relief = 'flat', bg = 'gray4')
        top_frame.pack(side = tk.TOP)

        bottom_frame = tk.Frame(master, width = 650, height = 470, bd = 2, relief = 'flat', bg = 'gray4')
        bottom_frame.pack(side = tk.BOTTOM)

        txt_display = tk.Entry(top_frame, font = ('arial', 36), relief = 'flat', bg = '#222222', fg = '#FFFFFF', textvariable = self.text_input, width = 60, bd = 4, justify = 'right')
        txt_display.pack()

        self.btn_del = tk.Button(bottom_frame, btn_params, text = "C", command = self.btn_clear)
        self.btn_del.configure(activebackground = "#B22222", bg = '#B22222', foreground = '#FFFFFF')
        self.btn_del.grid(row = 0, column = 1)

        self.btn_clear_all = tk.Button(bottom_frame, btn_params, text = "CE", command = self.btn_clear_all)
        self.btn_clear_all.configure(activebackground = "#B22222", bg = '#B22222', foreground = '#FFFFFF')
        self.btn_clear_all.grid(row = 0, column = 2)

        self.btn_reciprocal = tk.Button(bottom_frame, btn_params, text = "1/x", command = lambda: self.btn_click('1/'))
        self.btn_reciprocal.grid(row = 0, column = 3)

        self.btn_open_brack = tk.Button(bottom_frame, btn_params, text = "(", command = lambda: self.btn_click('('))
        self.btn_open_brack.grid(row = 0, column = 4)

        self.btn_close_brack = tk.Button(bottom_frame, btn_params, text = ")", command = lambda: self.btn_click(')'))
        self.btn_close_brack.grid(row = 0, column = 5)

        self.btn_clear = tk.Button(bottom_frame, btn_params, text = "AC", command = self.btn_clear_all)
        self.btn_clear.configure(activebackground = "#A5A5A5", bg = '#A5A5A5', foreground = 'black')
        self.btn_clear.grid(row = 0, column = 6)

        self.btn_change_sign = tk.Button(bottom_frame, btn_params, text = "+/-", command = self.change_signs)
        self.btn_change_sign.configure(activebackground = "#A5A5A5", bg = '#A5A5A5', foreground = 'black')
        self.btn_change_sign.grid(row = 0, column = 7)

        self.btn_change_sign = tk.Button(bottom_frame, btn_params, text = "%", command = self.change_signs)
        self.btn_change_sign.configure(activebackground = "#A5A5A5", bg = '#A5A5A5', foreground = 'black')
        self.btn_change_sign.grid(row = 0, column = 8)

        self.btn_div = tk.Button(bottom_frame, btn_params, text = "÷", command = lambda: self.btn_click('/'))
        self.btn_div.configure(activebackground = "#FB9F10", bg = '#FB9F10', foreground = '#FFFFFF')
        self.btn_div.grid(row = 0, column = 9)

        self.square = tk.Button(bottom_frame, btn_params, text = u"x\u00B2", command = lambda: self.btn_click('**2'))
        self.square.grid(row = 1, column = 1)

        self.cube = tk.Button(bottom_frame, btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 1, column = 2)

        self.btn_power = tk.Button(bottom_frame, btn_params, text = "x^y", command = lambda: self.btn_click('**'))
        self.btn_power.grid(row = 1, column = 3)

        self.btn_e_power = tk.Button(bottom_frame, btn_params, text = "e^x", command = lambda: self.btn_click('e**'))
        self.btn_e_power.grid(row = 1, column = 4)

        self.btn_10_power = tk.Button(bottom_frame, btn_params, text = "10^x", command = lambda: self.btn_click('10**'))
        self.btn_10_power.grid(row = 1, column = 5)

        self.btn_7 = tk.Button(bottom_frame, btn_params, text = "7", command = lambda: self.btn_click(7))
        self.btn_7.configure(activebackground = "#343434", bg = '#343434')
        self.btn_7.grid(row = 1, column = 6)

        self.btn_8 = tk.Button(bottom_frame, btn_params, text="8", command = lambda: self.btn_click(8))
        self.btn_8.configure(activebackground = "#343434", bg = '#343434')
        self.btn_8.grid(row = 1, column = 7)

        self.btn_9 = tk.Button(bottom_frame, btn_params, text = "9", command = lambda: self.btn_click(9))
        self.btn_9.configure(activebackground = "#343434", bg = '#343434')
        self.btn_9.grid(row = 1, column = 8)

        self.btn_mult = tk.Button(bottom_frame, btn_params, text = "x", command = lambda: self.btn_click('*'))
        self.btn_mult.configure(activebackground = "#FB9F10", bg = '#FB9F10', foreground = '#FFFFFF')
        self.btn_mult.grid(row = 1, column = 9)

        self.btn_Deg = tk.Button(bottom_frame, btn_params, text = "Deg", command = self.convert_deg)
        self.btn_Deg.grid(row = 2, column = 1)

        self.btn_Rad = tk.Button(bottom_frame, btn_params, text = "Rad", command = self.convert_rad)
        self.btn_Rad.grid(row = 2, column = 2)

        self.btn_sqrt = tk.Button(bottom_frame, btn_params, text="sqrt", command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row = 2, column = 3)

        self.btn_abs = tk.Button(bottom_frame, btn_params, text = "|x|", command = lambda: self.btn_click('abs('))
        self.btn_abs.grid(row = 2, column = 4)

        self.btn_fact = tk.Button(bottom_frame, btn_params, text = "x!", command = lambda: self.btn_click('factorial('))
        self.btn_fact.grid(row  =2, column = 5)
        
        self.btn_4 = tk.Button(bottom_frame, btn_params, text = "4", command = lambda: self.btn_click(4))
        self.btn_4.configure(activebackground = "#343434", bg = '#343434')
        self.btn_4.grid(row = 2, column = 6)

        self.btn_5 = tk.Button(bottom_frame, btn_params, text = "5", command = lambda: self.btn_click(5))
        self.btn_5.configure(activebackground = "#343434", bg = '#343434')
        self.btn_5.grid(row = 2, column = 7)

        self.btn_6 = tk.Button(bottom_frame, btn_params, text = "6", command = lambda: self.btn_click(6))
        self.btn_6.configure(activebackground = "#343434", bg = '#343434')
        self.btn_6.grid(row = 2, column = 8)

        self.btn_sub = tk.Button(bottom_frame, btn_params, text = "-", command = lambda: self.btn_click('-'))
        self.btn_sub.configure(activebackground = "#FB9F10", bg = '#FB9F10', foreground = '#FFFFFF')
        self.btn_sub.grid(row = 2, column = 9)

        self.btn_sin = tk.Button(bottom_frame, btn_params, text = "sin", command = lambda: self.btn_click(f'sin({convert_constant}*'))
        self.btn_sin.grid(row = 3, column = 1)

        self.btn_cos = tk.Button(bottom_frame, btn_params, text = "cos", command = lambda: self.btn_click(f'cos({convert_constant}*'))
        self.btn_cos.grid(row = 3, column = 2)

        self.btn_tan = tk.Button(bottom_frame, btn_params, text = "tan", command = lambda: self.btn_click(f'tan({convert_constant}*'))
        self.btn_tan.grid(row = 3, column = 3)

        self.btn_e = tk.Button(bottom_frame, btn_params, text = "e", command = lambda: self.btn_click('e'))
        self.btn_e.grid(row = 3, column = 4)
        
        self.btn_log = tk.Button(bottom_frame, btn_params, text = "log", command = lambda: self.btn_click('log('))
        self.btn_log.grid(row = 3, column = 5)

        self.btn_1 = tk.Button(bottom_frame, btn_params, text = "1", command = lambda: self.btn_click(1))
        self.btn_1.configure(activebackground = "#343434", bg = '#343434')
        self.btn_1.grid(row = 3, column = 6)

        self.btn_2 = tk.Button(bottom_frame, btn_params, text = "2", command = lambda: self.btn_click(2))
        self.btn_2.configure(activebackground = "#343434", bg = '#343434')
        self.btn_2.grid(row = 3, column = 7)
 
        self.btn_3 = tk.Button(bottom_frame, btn_params, text = "3", command = lambda: self.btn_click(3))
        self.btn_3.configure(activebackground = "#343434", bg = '#343434')
        self.btn_3.grid(row = 3, column = 8)

        self.btn_add = tk.Button(bottom_frame, btn_params, text = "+", command = lambda: self.btn_click('+'))
        self.btn_add.configure(activebackground = "#FB9F10", bg = '#FB9F10', foreground = '#FFFFFF')
        self.btn_add.grid(row = 3, column = 9)

        self.btn_sin_inverse = tk.Button(bottom_frame, btn_params, text = u"sin-\u00B9", command = lambda: self.btn_click(f'{inverse_convert_constant}*asin('))
        self.btn_sin_inverse.grid(row = 4, column = 1)

        self.btn_cos_inverse = tk.Button(bottom_frame, btn_params, text = u"cos-\u00B9", command = lambda: self.btn_click(f'{inverse_convert_constant}*acos('))
        self.btn_cos_inverse.grid(row = 4, column = 2)
        
        self.btn_tan_inverse = tk.Button(bottom_frame, btn_params, text = u"tan-\u00B9", command = lambda: self.btn_click(f'{inverse_convert_constant}*atan('))
        self.btn_tan_inverse.grid(row = 4, column = 3)

        self.btn_pi = tk.Button(bottom_frame, btn_params, text = "π", command = lambda: self.btn_click('pi'))
        self.btn_pi.grid(row = 4, column = 4)

        self.btn_ln = tk.Button(bottom_frame, btn_params, text = "ln", command = lambda: self.btn_click('log1p('))
        self.btn_ln.grid(row = 4, column = 5)

        self.btn_0 = tk.Button(bottom_frame, btn_params, text = "0", command = lambda: self.btn_click(0))
        self.btn_0.configure(activebackground = "#343434", bg = '#343434')
        self.btn_0.grid(row = 4, column = 6)

        self.btn_00 = tk.Button(bottom_frame, btn_params, text = "00", command = lambda: self.btn_click('00'))
        self.btn_00.configure(activebackground = "#343434", bg = '#343434')
        self.btn_00.grid(row = 4, column = 7)

        self.btn_dec = tk.Button(bottom_frame, btn_params, text = ".", command = lambda: self.btn_click('.'))
        self.btn_dec.configure(activebackground = "#343434", bg = '#343434')
        self.btn_dec.grid(row = 4, column = 8)

        self.btn_eq = tk.Button(bottom_frame, btn_params, text = "=", command = self.btn_equal)
        self.btn_eq.configure(activebackground = "#FB9F10", bg = '#FB9F10', foreground = '#FFFFFF')
        self.btn_eq.grid(row = 4, column = 9)

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    def convert_deg(self):
        global convert_constant, inverse_convert_constant
        convert_constant = 'pi/180'
        inverse_convert_constant = '180/pi'
        self.btn_Rad["foreground"] = 'white'
        self.btn_Deg["foreground"] = 'orange'

    def convert_rad(self):
        global convert_constant, inverse_convert_contant
        convert_constant = '1'
        inverse_convert_constant = '1'
        self.btn_Rad["foreground"] = 'orange'
        self.btn_Deg["foreground"] = 'white'

    def btn_clear_all(self):
        self.expression = ''
        self.text_input.set('')

    def btn_equal(self):
        try:
            self.sum_up = str(round(eval(self.expression),8))
            self.text_input.set(self.sum_up)
            self.expression = self.sum_up
        except:
            if self.expression.count('(') > self.expression.count(')'):
                self.expression += ')'
                self.expression = self.btn_equal()
            else:
                self.sum_up = 'Invalid Format'
                self.text_input.set(self.sum_up)
                self.expression = self.sum_up
                
# Driver
if __name__ == '__main__':
  root = tk.Tk()
  b = Calculator(root)
  root.title("Scientific Calculator")
  root.geometry("650x465")
  root.resizable(0, 0)
  root.mainloop()
