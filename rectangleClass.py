
# Topic: Custom Classes in Python

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


if __name__ == "__main__":
    r = Rectangle(15, 5)

    for item in r:
        print(item)
        
    
'''
Output:

{'length': 15}  
{'width': 5}

'''        
