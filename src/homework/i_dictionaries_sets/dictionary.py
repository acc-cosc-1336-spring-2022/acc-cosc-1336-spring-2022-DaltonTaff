#def get_p_distance(list1, list2):
 #   i = 0
  #  di = 0
   # while i < len(list1):
    #    if list1[i] != list2[i]:
     #       di += 1
      #  i += 1
    #p_dist = di / len(list1)
    #return p_dist

#def get_p_distance_matrix(list1):
 #   p_distance_matrix = []
  #  for r in list1:
   #     row = []
    #    for c in list1:
     #       row.append(get_p_distance(r,c))
      #  p_distance_matrix.append(row)
    #return p_distance_matrix

def add_inventory(wid, wid_name, quanity):
    if wid_name not in wid:
        wid[wid_name] = quanity
    else:
        wid[wid_name] += wid_name
def remove_inventory_widget(wid, wid_name):
    if wid_name in wid:
        del wid[wid_name]
        print('Deleted')
    else:
        print('Not found')
