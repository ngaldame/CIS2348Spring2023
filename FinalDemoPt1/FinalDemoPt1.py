import csv
from datetime import datetime

# A class called InventoryOput that will output the inventory
class InventoryOput:
  
  def __init__(self, list_item):
    self.list_item = list_item
    
  # full function will create a file alphabetically sorted by manufacturer
  # PLEASE CHANGE USE OF LAMBDA TO A LIST ITERATION
  def full(self):
    with open('FullInventory.csv', w) as file:
      its = self.list_item
      
      # CHANGE USAGE OF LAMBDA TO A LIST AND/OR DICTIONARY ITERATION FOR LINES 18 TO 26
      # (DO NOT USE PANDAS, ITEMGETTER, DATABASES, OR LAMBDA)
      keys = sorted(its.keys(), key=lambda x: its[x]['manufacturer'])
      for it in keys:
        id = it
        manufacturer_name = its[it]['manufacturer']
        i_type = its[it]['item_type']
        price = its[it]['price']
        date_service = its[it]['service_date']
        broken = its[it]['damaged']
        file.write(f'{id}, {manufacturer_name}, {i_type}, {price} {date_service}, {broken}')
        
        
# main driver code is below
if __name__ == '__main__':
  # A empty dictionary called its to store the items in inventory
  its = {}
  
  # files contains all the csv files
  files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
  
  # read, delimit, and strip whitespace from files
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
          its[id]['manufacturer'] = manufacturer_name.strip()
          its[id]['item_type'] = i_type.strip()
          its[id]['damaged'] = broken.strip()
        elif file = files[1]:
          price = line[1]
          its[id]['price'] = price
        elif file = files[2]:
          date_service = line[1]
          its[id]['service_date'] = service_date
          
  # Create an object of the InventoryOutput class and create the output files
  inventory = InventoryOput()
  inventory.full()
