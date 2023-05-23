file = 'trap_stepdis'

fig = openfig(file);
ax = fig.CurrentAxes
g_array = ax.Children
xdata = g_array(1).XData
ydata = g_array(1).YData


writematrix(xdata, [file, '_dataX.csv'])
writematrix(ydata, [file, '_dataY.csv'])