import os, sys
 
try:
 
    __import__("roi_enc").__main__()
 
except Exception as e:
 
    exit(str(e))
