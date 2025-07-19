# encoding: utf-8
# Author: Miguel Martínez López
#
# Uncomment the next line to see my email
# print("Author's email: ", "61706c69636163696f6e616d656469646140676d61696c2e636f6d".decode("hex"))


try:
    from Tkinter import Frame
    from Tkconstants import HORIZONTAL, VERTICAL
except ImportError:
    from tkinter import Frame
    from tkinter.constants import HORIZONTAL, VERTICAL

class Handle(Frame):
    def __init__(self, panedwindow, sash_index, disallow_dragging=False, on_click=None, **kw):
        Frame.__init__(self, panedwindow, **kw)

        self._sash_index = sash_index

        self._center = int(self["width"]/2), int(self["height"]/2)

        if disallow_dragging:
            if on_click:
                self.bind('<Button-1>', lambda event: on_click())
        else:
            self.bind('<Button-1>', self._initiate_motion)
            self.bind('<ButtonRelease-1>', self._release_dragging)

    def _initiate_motion(self, event) :
        self._dx = event.x
        self._dy = event.y

        self.bind('<Motion>', self._on_dragging)

    @property
    def sash_index(self):
        return self._sash_index

    def _release_dragging(self, event):
        self.unbind('<Motion>')

    def _on_dragging(self):
        raise NotImplementedError

class Vertical_Handle(Handle):
    def _on_dragging(self, event):
        y = event.y_root - self.master.winfo_rooty() - self._dy
        
        if y < self._center[1]:
            y = self._center[1]

        self.place_configure(y=y)        
        self.master.sash_place(self._sash_index, 1, y)

class Horizontal_Handle(Handle):
    def _on_dragging(self, event):
        x = event.x_root - self.master.winfo_rootx() - self._dx

        if x < self._center[0]:
            x = self._center[0]

        self.place_configure(x=x)
        self.master.sash_place(self._sash_index, x, 1)

def use_beautiful_handle(panedwindow, color="gray", size=60, disallow_dragging=False, on_click=None):

    panedwindow["showhandle"] = False

    orient = panedwindow["orient"]
    str_panedwindow = str(panedwindow)

    handle_list = []

    if orient == VERTICAL:    
        width= size
        height = 2*panedwindow["sashpad"]
        
        if disallow_dragging:
            cursor = "hand1"
        else:
            cursor = "sb_v_double_arrow"

        handle_class = Vertical_Handle
        def configure(sash_index):
            x,y = panedwindow.sash_coord(sash_index)
            handle_list[sash_index].place(y=y)
    else:
        width = 2*panedwindow["sashpad"]
        height = size
        
        if disallow_dragging:
            cursor = "hand2"
        else:
            cursor = "sb_h_double_arrow"
        
        handle_class = Horizontal_Handle
        def configure(sash_index):
            x,y = panedwindow.sash_coord(sash_index)
            handle_list[sash_index].place(x=x)

    list_of_panes = [panedwindow.nametowidget(tcl_obj.string) for tcl_obj in panedwindow.panes()]
    
    for i in range(len(list_of_panes)-1):
        
        handle = handle_class(panedwindow, i, bg=color, height=height, width=width, cursor = cursor, disallow_dragging=disallow_dragging, on_click=on_click)
        handle.place(relx=0.5, anchor="c")

        handle_list.append(handle)

        list_of_panes[i].bind("<Configure>", lambda event, sash_index=i: configure(sash_index))
        list_of_panes[i+1].bind("<Configure>", lambda event, sash_index=i: configure(sash_index))

        
if __name__ == "__main__":
    try:
        from Tkinter import PanedWindow, Frame, Tk
    except ImportError:
        from tkinter import PanedWindow, Frame, Tk

    root = Tk()
    panedwindow = PanedWindow(root, orient="vertical", sashpad = 3)
    panedwindow.pack(fill="both", expand=True)
    
    
    for color in ("red", "blue","green"):
        frame = Frame(panedwindow, width=200, height=200, bg=color)
        panedwindow.add(frame, stretch="always")
    
    use_beautiful_handle(panedwindow)
    root.mainloop()
