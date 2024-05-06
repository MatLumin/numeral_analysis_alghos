import math
from typing import *


def simpson_method(f:Callable[[float], float],  start:float, end:float, step:float)->float:
	sum:float = 0.0;
	range_devided_by_step:float = (end-start)/step;
	sum += f(start);
	sum += f(end);
	last_x :float = start;
	last_x += step;
	n = 1;
	while last_x <= end:
		is_n_odd = n % 2.0 != 0.0;
		coef:float = [2.0, 4.0][is_n_odd];
		f_n:float = f(last_x) ;
		print(f"{f_n}*{coef}");
		sum += f_n * coef;
		n += 1;
		last_x += step;
	sum = sum * (step/3);
	return sum;
		
		
		
if __name__ == "__main__":
	def f(x):
		return math.sqrt(x);
		
		
	print(simpson_method(f, 1, 1.3, 0.05));
	

		
