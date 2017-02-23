

import xmltodict
import re


class Parser():
    def __init__(self):
        pass

    def parse_struct(self,xml):
        try:
            doc = xmltodict.parse(xml)
            keys=doc.keys()
            for key in keys:
                keys_level2=doc[key].keys()
                for key_level2 in keys_level2:
                    if re.search(r'Body',key_level2):
                        return doc[key][key_level2]
        except BaseException:
            pass
        return None
        

        
    
