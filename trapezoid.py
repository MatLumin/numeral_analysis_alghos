import math;
from typing import *;



def trapezoid(function:Callable[[float],float], start:float, end:float, step:float):


    f = function;

    sum = 0;
    f_start = f(start);
    f_end = f(end);
    
    print(f"f({start})=>", f_start);
    print(f"f({end})=>", f_end);

    last_x = start;
    last_x += step;
    while True:
        if last_x >= end:
            break
        current_f = f(last_x);
        print(f"f({last_x})=>", current_f);
        sum += current_f * 2;
        last_x += step;

    output = sum * (step/2);
    return output;




if __name__ == "__main__":
    def f(x):
        return math.e ** x;
    
    o = trapezoid(function=f, start=0.1, end=0.3, step=0.1);
    print(o);



