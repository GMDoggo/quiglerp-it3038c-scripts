import requests

response = requests.get("http://localhost:3000")
widget_data = response.json()

if widget_data:
        for widget in widget_data:
            widget_name = widget["name"]
            widget_color = widget["color"]
            
            if widget_name and widget_color:
                print(f"{widget_name.capitalize()} is {widget_color}.")

