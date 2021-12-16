# -*- coding: utf-8 -*-
"""
Created on Sat Dec 8 

@author: vigilbushido
"""

def main():
    my_string = ("extra words on the left we don't want to include Incident was discovered on surface_web"
                 "and triggered by the rule: PII - Date of Birth. For additional context please see full "
                 "alert details at https://cloud.linuxservers.com/alerts/163761506/\"")

    my_string_edited = "Incident" + my_string.partition('Incident')[2]
    x = my_string_edited.partition('\n')[0]

    my_string_prefix_removed = "Incident" + my_string.partition('Incident')[2]
    my_string_suffix_removed = my_string_prefix_removed.partition('For additional')[0]
    

    print(my_string + '\n')
    print(my_string_prefix_removed + '\n')
    print(my_string_suffix_removed + '\n')
    print(type(my_string_suffix_removed))

    
if __name__ == "__main__":
    main()