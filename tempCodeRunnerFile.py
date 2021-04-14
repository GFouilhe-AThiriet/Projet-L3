
fig.canvas.mpl_connect('button_press_event', onclick)

anim = FuncAnimation(fig, animate, interval=100, frames=1)#change frames if it lags ??

plt.draw()