# Artificial Intelligence - Simulated Annealing
In this example I use simulated annealing to find minimum value from F(x,y), where

```
F(x,y) = -abs(math.sin(x)*math.cos(y)*math.exp(abs(1-math.sqrt(x**2 + y**2)/math.pi)))
```
The minimum value that I get from MATLAB is `-19.2085` , so i use this in accuracy function 
