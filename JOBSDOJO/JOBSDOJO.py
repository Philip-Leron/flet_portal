#from flet import Page,UserControl, app, View
from pages.forgotpassword import ForgotPassword
from pages.login import Login
from pages.signup import SignUp
from pages.home import Home
from flet import *
class Main(UserControl):
    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.page.title="JOBSDOJO.COM -- Jobs & More Portal"
        self.page.horizontal_alignment=MainAxisAlignment.CENTER
        self.page.vertical_alignment=CrossAxisAlignment.CENTER
        #self.page.alignment=MainAxisAlignment.CENTER
        self.page.window_width=1800
        self.page.window_height=1000
        self.page.window_center=True
        self.page.padding=30
        
        self.init_helper()
    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/')
        
    def on_route_change(self, route):
        newpage ={
            "/":Home,
            "/login":Login,
            "/signup":SignUp,
            "/forgotpassword":ForgotPassword
        }[self.page.route](self.page)
        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [newpage]
            )
        )
app(target=Main,assets_dir='assets')