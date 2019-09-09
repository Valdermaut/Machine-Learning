# Machine-Learning
matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB.
Each pyplot function makes some change to a figure: e.g., creates a figure, 
creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

f you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and 
automatically generates the x values for you. Since python ranges start with 0,
the default x vector has the same length as y but starts with 0. Hence the x data are [0,1,2,3].
