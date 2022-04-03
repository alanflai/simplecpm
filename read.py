# read.py
# The scripts reads an excel file content

import logging
from numpy import NaN
import pandas as pd
from criticalpath import Node


FILE_REFERENCE = "plan.xlsx"
p = Node('project')

logging.basicConfig(level=logging.INFO)

# get_row
# Parameters: 
# - tuple (row, column)
# Return the row values
def get_row(values):
    if type(values) is tuple:
        return values[0]
    else:
        return NaN

# get_row
# Parameters: 
# - tuple (row, column)
# Return the column values
def get_col(values):
    if type(values) is tuple:
        return values[1]
    else:
        return NaN

# get_nodes_ref
# Parameters:
# - list nodes_list
# - string node_id
# Return node_id string index inside nodes_list list
def get_nodes_ref(nodes_list, node_id):
    try:
        return nodes_list.index(node_id)
    except:
        logging.info("Error index %s" % node_id)
        return -1

# To open Workbook
try:
    wb = pd.read_excel(FILE_REFERENCE,sheet_name="PERT")
except FileNotFoundError:
    print("Error, input excel file doesn't exist!!")
except BaseException:
    logging.exception("Generic Error!")

row = get_row(wb.shape)
col = get_col(wb.shape)
# print("Rows and columns: %s - %s" %(row,col))

# Looping on 'Depend' column
links_list = []
for i in range(1,row):
    from_nodes_str = wb['Depend.'][i]
    to_node = wb['Id'][i]
    #print("%s) %s - %s" % (i, to_node , from_nodes_str))
    for val in from_nodes_str.split(','):
        # logging.info(" from node: %s" % val)
        links_list.append([val,to_node])

nodes_id = wb['Id'].tolist()
nodes_duration = wb['Duration'].tolist()

# Check get_nodes_ref function
print("Il riferimento di %s: %d" % ("1.3",get_nodes_ref(nodes_id,"1.3")))
print("Il riferimento di %s: %d" % ("1.6",get_nodes_ref(nodes_id,"1.6")))
print("Il riferimento di %s: %d" % ("1.8",get_nodes_ref(nodes_id,"1.8")))
print("Il riferimento di %s: %d" % ("1.15",get_nodes_ref(nodes_id,"1.15")))
print("Il riferimento di %s: %d" % ("1.17",get_nodes_ref(nodes_id,"1.17")))

# PERT nodes creation
pert_node = []

for i in range(len(nodes_id)):
    node_id = nodes_id[i]
    node_duration = nodes_duration[get_nodes_ref(nodes_id,node_id)]
    pert_node.append(p.add(Node(node_id, duration=node_duration, lag=0)))

# PERT links 
for link in links_list:
    from_index = get_nodes_ref(nodes_id,link[0])
    to_index= get_nodes_ref(nodes_id,link[1])

    logging.info("link[0]: %s, link[1]: %s - from index: %s, to_index: %s" % (link[0], link[1],from_index, to_index))

    from_obj = pert_node[from_index]
    to_obj = pert_node[to_index]
    p.link(from_obj, to_obj)

# Evaluate critical path
p.update_all()
cpm = p.get_critical_path()
print("critical path:", cpm)
print("Durata: %2d" % p.duration)