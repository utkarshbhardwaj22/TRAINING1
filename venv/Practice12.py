"""

**kwargs-> keyword arguments
**anyName -> it can be of any name
It is of type Dictionaries

"""
def employee(**utk):
    print(utk)
    print(type(utk))

#employee(name="Utkarsh", section="D3ITB", urn=1706904, email="utkarsh2000bhard@gmail.com")

def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))


show(10,"kin",20,30,40,50,name="Utkarsh", section="D3ITB", urn=1706904, email="utkarsh2000bhard@gmail.com")


