def log (func):
    def inner (* args, ** kwargs):
        with open ("log", "a", encoding="utf-8") as f:
            f.write (func .__name__) #Every time a function is called, the name of the called function is written to the file
            ret=func (* args, ** kwargs)
        return ret
    return inner
@log
def shoplist_add ():#Two functions have different functions
  print ("Add an item")
@log
def shoplist_del ():
  print ("Remove an item")
shoplist_add()
shoplist_del()