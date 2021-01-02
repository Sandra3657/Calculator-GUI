import tkinter as tk


class Calculator:
    def __init__(self, master, width):
        self.master = master
        self.master.title("Calculator")
        self.width = width
        self.b_width = width // 4

        self.screen = tk.Text(self.master, state='disabled', width=self.width, height=self.width // 10, padx=5, pady=5)
        self.screen.grid(row=0, column=0, columnspan=4)
        self.screen.configure(state='normal')
        self.eqn = ''
        self.answer = ''

        b0 = self.button('0')
        b1 = self.button('1')
        b2 = self.button('2')
        b3 = self.button('3')
        b4 = self.button('4')
        b5 = self.button('5')
        b6 = self.button('6')
        b7 = self.button('7')
        b8 = self.button('8')
        b9 = self.button('9')
        b10 = self.button('+')
        b11 = self.button('-')
        b12 = self.button('*')
        b13 = self.button('/')
        b14 = self.button('=')
        b15 = self.button('C')

        button_list = [[b7, b8, b9, b10], [b4, b5, b6, b11], [b1, b2, b3, b12],
                       [b15, b0, b14, b13]]

        r = 1
        for row in button_list:
            c = 0
            for button in row:
                button.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def button(self, val):
        return tk.Button(self.master, text=val, width=self.b_width, command=lambda: self.click(val))

    def click(self, val):
        if val == '=':
            if self.eqn:
                self.answer = str(eval(self.eqn))
                print(self.answer)
                self.clear_screen()
                self.insert_text(self.answer)
        elif val == 'C':
            self.clear_screen()
        else:
            self.insert_text(val)

    def insert_text(self, val):
        self.screen.configure(state='normal')
        self.screen.insert(tk.END, val)
        self.eqn += val
        self.screen.configure(state='disabled')

    def clear_screen(self):
        self.eqn = ''
        self.screen.config(state='normal')
        self.screen.delete('1.0', tk.END)


root = tk.Tk()
gui = Calculator(root, 30)
root.mainloop()
