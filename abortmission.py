#These functions are in the wrong order and aren't working the way they need to.
#See implementation in stats.py for correct structure



def dictionary_sort_helper(dict_sortie_h): #necessary for .sort in dictionary_sort function
          #must return a key
          ds_dict_h = garbo #character_dictionary()
          dict_sortie_h = []

          for key in ds_dict_h:
               if str.isalpha(key) == True:
                    dict_sortie_h.append({key})
          
          return dict_sortie_h

          #for ih in range (0,len(dict_sortie_h)):
               #print (dict_sortie_h[ih])    #utterly scuffed
#di_so_he_res= dictionary_sort_helper(helper)

     

def dictionary_sort():
     ds_dict = garbo #character_dictionary()
     dict_sortie = []
     
     for key in ds_dict:
          if str.isalpha(key) == True:
               dict_sortie.append({key: ds_dict[key]})
     
          
          
    
          
     dict_sortie.sort(reverse=True, key= dictionary_sort_helper)
     print (dict_sortie)