from  typing import *;
from math import *



def newton_cots(function:Callable[[float], float], start:float, end:float)->float:
    range_length:float = abs(start-end);
    step:float = range_length/3;

    x1 = start; 
    x2 = x1 + step;
    x3 = x2 + step;
    x4 = end;
    
    f1=function(x1);
    f2=function(x2);
    f3=function(x3);
    f4=function(x4);

    output = (3*step/8) * (f1 + 3*f2 + 3*f3 + f4);
    return output





if __name__ == "__main__":
    def f(x):
        return x*(e**x);



    o = newton_cots(f, 0, 1);
    print(o);
