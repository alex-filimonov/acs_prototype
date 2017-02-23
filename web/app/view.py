################################################
###############################################

import re
import sys

class View():

    def __init__(self):
        self.shema_dir=""
        self.Controller=""
        self.Action=""
        self.content=""

    def http_header(self):
        print("Content-Type: text/html;charset=utf-8\r\n\r\n")

    def view_error(self,error):
        print("Content-Type: text/html;charset=utf-8\r\n\r\n")
