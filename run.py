import os, sys
 
try:
 
    __import__("roi_enc").main()
 
except Exception as e:
 
    exit(str(e))
