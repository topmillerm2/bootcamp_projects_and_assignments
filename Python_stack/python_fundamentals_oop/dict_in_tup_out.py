my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def dic_in_tup_out(itm):
    new_list = []
    for key in itm:
        # print key
        # print itm[key]
        tup= key, itm[key]
        new_list.append(tup)
    print new_list    
dic_in_tup_out(my_dict)
