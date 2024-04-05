# Group Members: Karla Arias, Helen Pena and Ryan Ramirez.
import flet as ft
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

#main variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0
r1 = 0
r2 = 0

matplotlib.use("svg") #render format
def main(page: ft.Page):
  page.title = "Vector Calculator"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.padding = 20
  page.theme_mode = ft.ThemeMode.LIGHT
  page.scroll = ft.ScrollMode.ALWAYS
  page.update()

  page_title = ft.Text(
    "Vector Calculator", 
    size = 24,
    weight = ft.FontWeight.W_700, # bold
    color = ft.colors.BLACK,
  )

  page_description = ft.Text(
    "Vector calculator is a very useful tool that allows you to perform various operations with vectors. In this one you will find sum of vectors and difference between two vectors. Choose an option in the dropdown list below to get started.", 
    size = 12, 
    weight = ft.FontWeight.W_400, #regular
    color = ft.colors.BLACK, 
  )

  menu_title = ft.Text(
    "Operations List: ", 
    size = 12, 
    weight = ft.FontWeight.W_700,
    color = ft.colors.BLACK, 
  )

  m_option1 = "Vector addition"
  m_option2 = "Vector difference"

  vector1_label = ft.Text(
    "A", 
    size=13, 
    weight=ft.FontWeight.W_700,
    color=ft.colors.RED, 
  )

  vector2_label = ft.Text(
    "B", 
    size=13, 
    weight = ft.FontWeight.W_700, 
    color = ft.colors.BLUE, 
  )

  real_numb_pattern = r"^-?\d*\.?\d*$" #my brothers help

  entry_filter = ft.InputFilter(
      allow = True,
      regex_string = real_numb_pattern,
      replacement_string = ""
  )
  
  vector_info = ft.Text(
    "Type the components for the vectors in the text fields below",
    size = 12, 
    weight = ft.FontWeight.W_400,
    color = ft.colors.BLACK,
    width=350
  )

  vector1_x = ft.TextField(
    label = "x₁-value", 
    hint_text= "0",
    input_filter = entry_filter,
    width=150,
    height= 50,
  )

  vector1_y = ft.TextField(
    label = "y₁-value", 
    hint_text= "0",
    input_filter = entry_filter,
    width=150,
    height= 50,
  )

  vector2_x = ft.TextField(
    label = "x₂-value", 
    hint_text= "0",
    input_filter = entry_filter,
    width=150,
    height= 50,
  )

  vector2_y = ft.TextField(
    label = "y₂-value", 
    hint_text= "0",
    input_filter = entry_filter,
    width=150,
    height= 50,
  )

  vector2 = ft.Row()

  def dropdown_changed(e):  #tomar la opcion que el usario escogio
    option = menu_options.value

    if option != None :
      if option == m_option1 or option == m_option2:
        vector2.controls = [vector2_label, vector2_x, vector2_y]
        page.update()
      else:
        vector2.controls = None # Hide controls
        page.update()
    else:
      vector2.controls = None
      page.update()
  

  menu_options = ft.Dropdown(
    width = 230,
    height= 50,
    hint_text = "Choose an option",
    text_size = 13,
    options=[
      ft.dropdown.Option(m_option1),
      ft.dropdown.Option(m_option2),
    ],
    on_change= dropdown_changed,
  )

  output_description = ft.Text(
      "", 
      size = 12, 
      weight = ft.FontWeight.W_400,
      color = ft.colors.BLACK,
  )

  vector_a = ft.Text(
    size= 14,
    weight=ft.FontWeight.W_400,
    color=ft.colors.BLACK
  )

  vector_b = ft.Text(
    size= 14,
    weight=ft.FontWeight.W_400,
    color=ft.colors.BLACK
  )

  operation = ft.Text(
    size= 14,
    weight=ft.FontWeight.W_400,
    color=ft.colors.BLACK
  )

  operation_result = ft.TextField(
    read_only=True,
    border=ft.InputBorder.UNDERLINE,
    filled=True,
    text_size=14,
    multiline=True,
    min_lines=1,
    text_style=ft.TextStyle(
      size=14,
      weight=ft.FontWeight.W_500
    )
  )

  #Functions
  def submit_clicked(e):
    global x1, y1, x2, y2, r1, r2
    try: x1 = float(vector1_x.value)
    except: x1 = 0
    try: y1 = float(vector1_y.value)
    except: y1 = 0
    try: x2 = float(vector2_x.value)
    except: x2 = 0
    try: y2 = float(vector2_y.value)
    except: y2 = 0

    option = menu_options.value # getting user selection

    if option == m_option1:
      if x1 != 0 or y1 != 0:
        r1 = x1 + x2
        r2 = y1 + y2
        output_description.value = "Sum of the vectors A and B"
        vector_a.value = f"A ⟨{x1}, {y1}⟩"
        vector_b.value = f"B ⟨{x2}, {y2}⟩"
        operation.value = f"A + B = ⟨{x1}, {y1}⟩ + ⟨{x2}, {y2}⟩"
        operation_result.value = f"A + B = ⟨{r1}, {r2}⟩"

    elif option == m_option2:
      if x1 != 0 or y1 != 0:
        x2 = -1 * x2
        y2 = -1 * y2
        r1 = x1 + x2
        r2 = y1 + y2
        output_description.value = "Difference of the vectors A and B"
        vector_a.value = f"A ⟨{x1}, {y1}⟩"
        vector_b.value = f"B ⟨{x2}, {y2}⟩"
        operation.value = f"A - B = ⟨{x1}, {y1}⟩ - ⟨{x2}, {y2}⟩"
        operation_result.value = f"A - B = ⟨{r1}, {r2}⟩"

    load_chart(False) # Calling the graph of the vectors
    page.update()
  
  def clear_clicked(e):
    global x1, y1, x2, y2
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    menu_options.value = None
    vector1_x.value = None
    vector1_y.value = None
    vector2_x.value = None
    vector2_y.value = None
    output_description.value = None
    vector_a.value = None
    vector_b.value = None
    operation.value = None
    operation_result.value = None
    dropdown_changed(e)
    load_chart(False)
    page.update()

  # Buttons
  btn_submit = ft.ElevatedButton(
    text = "Submit", 
    icon = "check_rounded",
    bgcolor = ft.colors.BLUE, 
    color = ft.colors.WHITE,
    width = 150,
    height = 40,
    on_click =  submit_clicked,
  )

  btn_clear = ft.ElevatedButton(
    text= "Clear",
    icon="clear_rounded",
    bgcolor=ft.colors.GREY_500,
    color = ft.colors.WHITE,
    width= 150,
    height=40,
    on_click= clear_clicked,
  )

  #Creating the plane y the axis
  fig, ax = plt.subplots()
  def load_chart(e):

    if e == False:
      plt.cla()

    #chart
    global x1, y1, x2, y2

    #Graphing the Vectors
    ax.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='r', label='A')
    ax.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='b', label='B')
    
    # Graphing Result
    option = menu_options.value
    if option and (x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0):
        if option == m_option1 or option == m_option2:
          ax.quiver(0, 0, r1, r2, angles='xy', scale_units='xy', scale=1, color='g', label='Result')

    #Setting the axis
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

    # Set the limits of the Cartesian plane
    # Min and max values (all vectors)
    all_x = [0, x1, x2, r1]
    all_y = [0, y1, y2, r2]

    max_x = max(all_x)
    min_x = min(all_x)
    max_y = max(all_y)
    min_y = min(all_y)

    # Range to adjust limits
    range_x = max_x - min_x
    range_y = max_y - min_y
    range_max = max(range_x, range_y)

    if range_max < 5:
        range_max = 5

    xlim1 = min_x - 0.1 * range_max # %10 buffer 
    xlim2 = max_x + 0.1 * range_max
    ylim1 = min_y - 0.1 * range_max
    ylim2 = max_y + 0.1 * range_max

    ax.set_xlim(xlim1, xlim2)
    ax.set_ylim(ylim1, ylim2)
    ax.set_aspect('equal', adjustable='box')

    # Show the grid
    ax.grid(True)

    # Set labels and title
    plt.title('Cartesian Plane')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

  load_chart(True)


  output_title = ft.Text(
    "Output", 
    size=14, 
    weight=ft.FontWeight.W_700,
    color=ft.colors.BLACK,
  )

  result = ft.Container(
    content=ft.Column(
      [
      output_title,
      output_description,
      vector_a,
      vector_b,
      operation,
      operation_result
      ],
      spacing=20),
    width=700, 
    height=300, 
    bgcolor= ft.colors.BLUE_ACCENT_100,
    border_radius= 5,
    padding=ft.padding.all(20),
  )

  #Page layout
  page.add(
    ft.Container(
      content = ft.Column([
        page_title,
        page_description,
        ft.Container(width=700,height=20,),
        ft.Row([
          ft.Row([
            menu_title, menu_options
          ]),
        ], 
          spacing = 40,
          run_spacing = 10,
        ),

        ft.Row([
          ft.Column([
            vector_info,
              ft.Row([
                vector1_label, vector1_x, vector1_y
              ]),
              vector2,
              ft.Container(
                content = ft.Row([
                btn_submit, btn_clear
                ]),
                margin= ft.margin.only(left=20, top=20)
              )], 
              spacing = 20,
            ),
          ft.Column([
            ft.Container(
               # Show the Cartesian plane
              content= MatplotlibChart(fig, expand=True, transparent=True),
              width=400,
              height=300,
            )
          ]),
        ]), 
        result, 
        
        ],
        spacing= 10, 
        width = 700, 
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ), 
    )
  )

ft.app(target=main) 

#SPECIFIC REFERENCES: (we think this is all, maybe will need to add later)
#https://flet.dev/docs/controls/dropdown/
#https://flet.dev/blog/matplotlib-and-plotly-charts/
#https://flet.dev/docs/controls/textfield/
#https://flet.dev/docs/controls/radio
#https://flet.dev/docs/controls/elevatedbutton
#https://flet.dev/docs/controls/icon/
#https://www.w3schools.com/python/default.asp 
#https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/ 
#what you provided to us + help of my brother (karla)