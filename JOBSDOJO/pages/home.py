from flet import *


class Home(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page  # Store the page reference
        self.page.horizontal_alignment = CrossAxisAlignment.START
        self.page.vertical_alignment = MainAxisAlignment.START
        self.r = Row(wrap=True, scroll="always", expand=True,alignment=MainAxisAlignment.CENTER)
        for i in range(100):
            self.r.controls.append(
                Card(
            content=Container( 
                
                content=Column(
                    controls=[
                        Text(f"item{i}",size=50,weight=50,color="#002147",text_align=TextAlign.CENTER),
                        ListTile(
                            leading =CircleAvatar(
                                background_image_src="./assets/download.png",
                                content=Text("FF"),
                            ),
                            title=Text("The Enchanted Nightingale"),
                            subtitle=Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                            on_click=lambda e: print("Clickable without Ink clicked!"),
                        ),
                        Row(
                            [TextButton("Buy tickets"), TextButton("Listen")],
                            alignment=MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=1200,
                padding=10,
                on_click=lambda e: print("Clickable without Ink clicked!"),
            )
        )
            )
    
        self.finalcard=Card(
            color="#002147",
            adaptive=True,
            content=Container(
                content=Column(
                    [
                        ListTile(
                            leading=Icon(icons.EMAIL_OUTLINED),
                            title=Text("Subscribe to Our Newsletter",color="white"),
                            subtitle=Text(
                                "Enter Your Email.."
                            ),
                        ),
                        Row(
                            [Container(),
                                TextField(color="white",label="Email",adaptive=True,autofocus=True,width=380,border_width=2)],                
                        ),
                        TextButton("Save")
                    ]
                ),
                width=400,
                height=200,
               
                
            )
        )


        self.railghana = NavigationBar(
            bgcolor="#002147",
            shadow_color="pink",
            indicator_color="red",
            surface_tint_color="white",
            label_behavior=NavigationBarLabelBehavior.ALWAYS_SHOW,
        destinations=[
            
           
            NavigationDestination(icon=icons.WORK, label="Jobs",bgcolor="white"),
            NavigationDestination(icon=icons.NEWSPAPER, label="News"),
            NavigationDestination(icon=icons.SPORTS, label="Sports"),
            NavigationDestination(
                icon=icons.LOCAL_MOVIES,
                label="Entertainment",
            ),
            
        ]
    )
        self.rail_hori = Column([
            
            NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        height=100,
        #indicator_shape=OutlinedBorder.
        # extended=True,
     

        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
        group_alignment=-0.9,
        
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )])
        
        self.expand = True
        self.bgcolor = 'white'
        self.content = Tabs(
            overlay_color="blue",
            divider_color="#002147",
            indicator_color="#002147",
            tabs=[
                
                Tab(
                   
                    
                    tab_content= 
                        Row(
                            [
                                Text("GHANA"),
                                 Image(
                                    src=f"./assets/download.png",
                                width=30,
                                height=30,
                            fit=ImageFit.CONTAIN,
                            
                                ),
                            
                            ]            
                            
                        ),
                             
                    content=Container(
                        Column(
                            alignment=MainAxisAlignment.START,
                            controls=[
                               
                               self.railghana,
                               
                               Row([
                               self.rail_hori,
                               VerticalDivider(width=1,thickness=2),
                               self.r,
                               VerticalDivider(width=1,thickness=2),
                               self.finalcard,
                            ],
                            width=1600,
                          height=1200,
                          adaptive=True,
                          expand=True,
                          auto_scroll=True
                            ),
                              
                              
                               
                              
                            ]
                        )
                    )
                ),
                Tab(
                    #text="KENYA",
                    tab_content=Row(
                    [
                            Text("KENYA"),
                            Image(
                                    src=f"./assets/kenya.png",
                                width=30,
                                height=30,
                            fit=ImageFit.CONTAIN,
                            
                                )
                    ]

                    ),
                    content=Container(
                        Column(
                            horizontal_alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                               
                            ]
                        )
                    )
                ),
                Tab(
                    tab_content=Row(
                    [
                            Text("NIGERIA"),
                            Image(
                                    src=f"./assets/nigeria.png",
                                width=30,
                                height=30,
                            fit=ImageFit.CONTAIN,
                            
                                )
                    ]

                    ),
                    content=Container(
                        Column(
                            horizontal_alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                               
                            ]
                        )
                    )
                ),
                Tab(
                    tab_content=Row(
                    [
                            Text("SOUTH AFRICA"),
                            Image(
                                    src=f"./assets/SA.png",
                                width=30,
                                height=30,
                            fit=ImageFit.CONTAIN,
                            
                                )
                    ]

                    ),
                    content=Container(
                        Column(
                            horizontal_alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                               
                            ]
                        )
                    )
                ),
                Tab(
                    text="LIVE SCORE",
                    icon=icons.SPORTS_SCORE,
                    content=Container(
                        Column(
                            horizontal_alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                               
                            ]
                        )
                    )
                ),
                
            ]
        )





        
