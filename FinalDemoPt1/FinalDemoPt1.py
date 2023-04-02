import csv
from datetime import datetime

class InventoryOput:
  
  def __init__(self, list_item):
    self.list_item = list_item
    
  def full(self):
    
# main driver code is below
if __name__ == '__main__':
  its = {}
  files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
  for file in files:
    with open(file, 'r') as csv_f:
      csv_re = csv.reader(csv_f, delimiter=',')
      for line in csv_re:
        id = lin[0]
        if file == files[0]:
          its[id] = {}
          manufacturer_name = line[1]
          i_type = line[2]
          broken = line[3]
          # Continue other lines ABOVE another time
        elif file = files[1]:
          price = line[1]
          # Continue other lines ABOVE another time
        elif file = files[2]:
          date_service = line[1]
