import tkinter as tk
  
root = tk.Tk()
 
def button_callback(state):
    print('Button Callback', state)
      
class Button(tk.Button):
     
    def __init__(self, parent, active_color=None, **kwargs):
        self.active_color = active_color
        super().__init__(**kwargs)
         
        self.callback = kwargs['command'] if 'command' in kwargs else None
        self['command'] = self.change_color
        self.bg_color = self['bg']
        self.state = False
         
    def change_color(self):
        self.state = not self.state
        self['bg'] = self.active_color if self.state else self.bg_color
        if self.callback: self.callback(self.state)
  
Button(root, '#00ffff', text='one', command=button_callback).pack()
Button(root, '#90ee90', text='two').pack()
Button(root, text='three').pack()
  
root.mainloop()