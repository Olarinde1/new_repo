# from tkinter import *
# import requests
# import json
# from PIL import ImageTk,Image
# from tkinter import filedialog
# root = Tk()
# root.title('Polymath Tech')
# root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
# root.geometry("600x100")
# # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=B2846DAB-AC34-4757-8A67-811D1CEE145D


# def zipLookup():
    
#     try:
#         api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zip_code.get()) + "&distance=5&API_KEY=B2846DAB-AC34-4757-8A67-811D1CEE145D")
#         api = json.loads(api_requests.content)
#         city = api[0]['ReportingArea']
#         quality = api[0]['AQI']
#         category = api[0]['Category']['Name']

#         if category == "Moderate":
#             weather_color = '#FFFF00'
#         elif category== "Good":
#             weather_color = "#0c0"
#         elif category== "Unhealthy for Sensitive Groups":
#             weather_color = "#ff9900"
#         elif category== "Unhealthy":
#             weather_color = "#FF0000"
#         elif category== "Very Unhealthy":
#             weather_color = "#990066"
#         elif category== "Harzardous":
#             weather_color = "#660000"
        
        


#         root.configure(background=weather_color)
        
#         mylabel = Label(root, text= city + " Air Quality "+ str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
#         mylabel.grid(row=1, column=0, columnspan=2)

#     except Exception as e:
#         api = "Error...."

# zip_code = Entry(root)
# zip_code.grid(row=0, column=0,stick=W+E+N+S)

# zipButton = Button(root, text='Lookup Zipcode', command=zipLookup)
# zipButton.grid(row=0, column=1, stick=W+E+N+S)

# root.mainloop()
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()