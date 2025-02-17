import csv
from datetime import datetime

# A class called InventoryOput that will output the inventory
class InventoryOput:
  
  def __init__(self, list_item):
    self.list_item = list_item
    
  # full function will create a file alphabetically sorted by manufacturer
  # DOES WORK AS ITS SUPPOSED TO BUT PLEASE CHANGE USE OF LAMBDA TO A LIST ITERATION
  def full(self):
    with open('FullInventory.csv', w) as file:
      its = self.list_item
      
      # CHANGE USAGE OF LAMBDA TO A LIST AND/OR DICTIONARY ITERATION FOR LINES 18 TO 26
      # CHANGE FUNCTION TO USE ONLY LIST OR DICTIONARY IRETATION ONLY IF NEEDED

      # (DO NOT USE LAMBDA, ITEMGETTER, DATABASES, AND/OR PANDA)
      keys = sorted(its.keys(), key=lambda x: its[x]['manufacturer'])
      for it in keys:
        id = it
        manufacturer_name = its[it]['manufacturer']
        i_type = its[it]['item_type']
        price = its[it]['price']
        date_service = its[it]['service_date']
        broken = its[it]['damaged']
        file.write(f'{id}, {manufacturer_name}, {i_type}, {price}, {date_service}, {broken}')
        
  # by_type function will create a file that will sort items by their item ID which is in a variable called id
  # CHANGE FUNCTION TO USE ONLY LIST OR DICTIONARY IRETATION ONLY IF NEEDED

  # (DO NOT USE LAMBDA, ITEMGETTER, DATABASES, AND/OR PANDA)
  # CHANGE FOR LINES 31 TO 50 ONLY IF NEEDED
  def by_type(self):
    its = self.list_item
    types = []
    keys = sorted(its.keys())
    for it in its:
      it_type = its[it]['item_type']
      if it_type not in types:
        types.append(it_type)
    for type in types:
      file_name = type.capitalize() + 'LaptopInventory.csv'
      with open(file_name, 'w') as file:
        for it in keys:
          id = it
          manufacturer_name = its[it]['manufacturer']
          price = its[it]['price']
          date_service = its[it]['service_date']
          broken = its[it]['damaged']
          i_type = its[it]['item_type']
          if type == it_type:
            file.write(f'{id}, {manufacturer_name}, {price}, {date_service}, {broken}')
            
  # past_service function will create a csv file for expired items
  # CHANGE FUNCTION TO USE ONLY LIST OR DICTIONARY IRETATION ONLY IF NEEDED

  # (DO NOT USE LAMBDA, ITEMGETTER, DATABASES, AND/OR PANDA)
  # CHANGE FOR LINES 55 TO 69 ONLY IF NEEDED
  def past_service(self):
    its = self.list_item
    keys = sorted(items.keys(), key=lambda x: datetime.strptime(its[x]['past_service'], '%m/%d/%Y').date(), reverse=True)
    with open('PastServiceDateInventory.csv', 'w') as file:
      for it in keys:
        id = it
        manufacturer_name = its[it]['manufacturer']
        i_type = its[it]['item_type']
        price = its[it]['price']
        date_service = its[it]['service_date']
        broken = its[it]['damaged']
        today = datetime.now().date()
        service_expiration = datetime.strptime(date_service, '%m/%d/%Y').date
        if service expiration < today:
          file.write(f'{id}, {manufacturer_name}, {i_type}, {price}, {date_service}, {broken}')
  
  # broken function will items that are damaged and will also be sorted by highest to lowest price
  # CHANGE FUNCTION TO USE ONLY LIST OR DICTIONARY IRETATION ONLY IF NEEDED

  # (DO NOT USE LAMBDA, ITEMGETTER, DATABASES, AND/OR PANDAS)
  # CHANGE FOR LINES 74 TO 86 ONLY IF NEEDED
  def broken(self):
    its = self.list_item
    keys = sorted(its.keys(), key=lambda x: its[x]['price'], reverse=True)
    with open('DamagedInventory.csv', 'w') as file:
      for it in keys:
        id = it
        manufacturer_name = its[it]['manufacturer']
        i_type = its[it]['item_type']
        price = its[it]['price']
        date_service = its[it]['service_date']
        broken = its[it]['damaged']
        if broken:
          file.write(f'{id}, {manufacturer_name}, {i_type}, {price}, {date_service}')
          
# main driver code is below AND NEEDS TO BE MODIFIED IN ORDER TO WORK PROPERLY
# MODIFY LINES 90 TO 123 ONLY IF NEEDED
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
  inventory.by_type()
  inventory.past_service()
  inventory.broken()
