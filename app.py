import tkinter
from tkintermapview import TkinterMapView
from main import extract_lang_long
import pandas as pd
address = pd.read_csv('places.csv')

root_tk = tkinter.Tk()
root_tk.geometry('800x800')
root_tk.title("Site Acquisition Map")

map_widget = TkinterMapView(root_tk, width=600, height=800, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(39.809860, -98.555183, marker=True)
#marker.set_text("USA")

for _, place in address.iterrows():
    map_widget.set_marker(place['latitude'], place['longitude'], text = place['cities'])
map_widget.set_zoom(4)


map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")


map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)


def left_click_event(coordinates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)


map_widget.add_left_click_map_command(left_click_event)


#map_widget.set_address("Topasgatan 28", marker=True)

root_tk.mainloop()