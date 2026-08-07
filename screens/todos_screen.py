"from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from controllers.todo_controller import TodoController

class TodoItem(OneLineIconListItem):
    def __init__(self, todo_data: dict, **kwargs):
        super().__init__(**kwargs)
        self.todo_data = todo_data
        self.text = f"{'✅' if todo_data['is_done'] else '⬜'} {todo_data['task']}"
        
    def on_release(self):
        # Panggil controller untuk toggle
        self.parent_screen.todo_ctrl.toggle_todo(
            self.todo_data['id'], 
            self.todo_data['is_done']
        )
        self.parent_screen.refresh_list()

class TodosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todo_ctrl = TodoController()
        
    def on_enter(self, *args):
        Clock.schedule_once(self.refresh_list, 0.1)
        
    def refresh_list(self, dt=None):
        container = self.ids.todo_container
        container.clear_widgets()
        
        result = self.todo_ctrl.get_all()
        if result["success"]:
            for todo in result["data"]:
                item = TodoItem(todo)
                item.parent_screen = self
                container.add_widget(item)
                
    def show_add_dialog(self):
        self.dialog = MDDialog(
            title="Tambah Tugas Baru",
            type="custom",
            content_cls=MDTextField(hint_text="Nama tugas", mode="rectangle"),
            buttons=[
                MDFlatButton(text="BATAL", on_release=self.close_dialog),
                MDFlatButton(text="SIMPAN", on_release=self.save_todo)
            ]
        )
        self.dialog.open()
        
    def save_todo(self, instance):
        task_text = self.dialog.content_cls.text
        result = self.todo_ctrl.create_todo(task_text)
        
        if result["success"]:
            self.close_dialog()
            self.refresh_list()
        else:
            # Tampilkan error (Tim C: integrasikan dengan Toast/Snackbar)
            print(result["error"])
            
    def close_dialog(self, *args):
        self.dialog.dismiss()from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from controllers.todo_controller import TodoController

class TodoItem(OneLineIconListItem):
    def __init__(self, todo_data: dict, **kwargs):
        super().__init__(**kwargs)
        self.todo_data = todo_data
        self.text = f"{'✅' if todo_data['is_done'] else '⬜'} {todo_data['task']}"
        
    def on_release(self):
        # Panggil controller untuk toggle
        self.parent_screen.todo_ctrl.toggle_todo(
            self.todo_data['id'], 
            self.todo_data['is_done']
        )
        self.parent_screen.refresh_list()

class TodosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todo_ctrl = TodoController()
        
    def on_enter(self, *args):
        Clock.schedule_once(self.refresh_list, 0.1)
        
    def refresh_list(self, dt=None):
        container = self.ids.todo_container
        container.clear_widgets()
        
        result = self.todo_ctrl.get_all()
        if result["success"]:
            for todo in result["data"]:
                item = TodoItem(todo)
                item.parent_screen = self
                container.add_widget(item)
                
    def show_add_dialog(self):
        self.dialog = MDDialog(
            title="Tambah Tugas Baru",
            type="custom",
            content_cls=MDTextField(hint_text="Nama tugas", mode="rectangle"),
            buttons=[
                MDFlatButton(text="BATAL", on_release=self.close_dialog),
                MDFlatButton(text="SIMPAN", on_release=self.save_todo)
            ]
        )
        self.dialog.open()
        
    def save_todo(self, instance):
        task_text = self.dialog.content_cls.text
        result = self.todo_ctrl.create_todo(task_text)
        
        if result["success"]:
            self.close_dialog()
            self.refresh_list()
        else:
            # Tampilkan error (Tim C: integrasikan dengan Toast/Snackbar)
            print(result["error"])
            
    def close_dialog(self, *args):
        self.dialog.dismiss()
