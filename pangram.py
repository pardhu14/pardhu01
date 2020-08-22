import string
def pangram(str):
     alp="abcdefghijklmnopqrstuwxyz"
     for char in alp:
            if char not in str.lower():
                  return False
     else:
            return True
            
string="The quick brown fox jumps over the lazy dog"
if(pangram(string)==True):
     print("yes")
else:
     print("no")
