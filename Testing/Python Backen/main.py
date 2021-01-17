#- Location: Latitude and Longitude
#- Nitrogen: 550ppi
# Libraries Matlib, Pandas, Numpy
import csv

f = open('C:\Users\Eldar\Documents\GitHub\STS-Hacks\Testing\Python Backen\NO2_err.csv')

csv_f = csv.reader(f)

for row in csv_f:
    print row

f.close()