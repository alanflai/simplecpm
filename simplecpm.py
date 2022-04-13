# simplecpm
# Simple python script for project's critical path evaluation.
# April 2022
# Credits:
# criticalpath python package (https://pypi.org/project/critical-path/)

import logging
from numpy import NaN
import pandas as pd
from criticalpath import Node


FILE_REFERENCE = "plan.xlsx"
graph = Node('project')

# Set logging level
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

# Excel's Workbook read
try:
    wb = pd.read_excel(FILE_REFERENCE,sheet_name="PERT")
except FileNotFoundError:
    logging.info("Error, input excel file doesn't exist!!")
except BaseException:
    logging.exception("Generic Error!")

# Get Excel's DataFrame rows and columns
row = get_row(wb.shape)
col = get_col(wb.shape)
logging.info("PERT excel's sheet Rows and columns: %s - %s" %(row,col))

# Network links list
links_list = []
for i in range(1,row):
    from_nodes_str = wb['Depend.'][i]
    to_node = wb['Id'][i]
    if isinstance(from_nodes_str,str):
        # print("%s) %s - %s" % (i, from_nodes_str, to_node ))
        for val in from_nodes_str.split(','):
            # logging.info(" from node: %s" % val)
            links_list.append([val.strip(),to_node])

nodes_id = wb['Id'].tolist()
nodes_duration = wb['Duration'].tolist()

# PERT nodes creation
pert_node = []

for i in range(len(nodes_id)):
    node_id = nodes_id[i]
    node_duration = nodes_duration[i]
    pert_node.append(graph.add(Node(node_id, duration=node_duration, lag=0)))

# PERT links 
for link in links_list:
    from_index = get_nodes_ref(nodes_id,link[0])
    to_index= get_nodes_ref(nodes_id,link[1])

    print("Node start: %s, Node end: %s - start id: %s, end_id: %s" % (link[0], link[1],from_index, to_index))

    from_obj = pert_node[from_index]
    to_obj = pert_node[to_index]
    p.link(from_obj, to_obj)

# Evaluate critical path
graph.update_all()
cpm = graph.get_critical_path()
print("critical path:", cpm)
print("Durata: %2d" % p.duration)
