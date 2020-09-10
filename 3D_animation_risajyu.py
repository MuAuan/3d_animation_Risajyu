from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

def genxy(n,fx,fy,fxc=0,fyc=0):
    phi = 0
    sk = 0
    while phi < 360:  #50*np.pi
        yield np.array([phi,fx*np.cos(2*phi/3)+fxc, fy*np.sin(3*phi/2)+fyc])
        sk += 1
        #print(fx,fy, sk, phi)
        phi += 36*5/n  #50*np.pi/n
def genxy0(n,fx,fy,fxc=0,fyc=0):
    phi = 0
    sk = 0
    while phi < 360:  #50*np.pi
        yield np.array([0,fx*np.cos(2*phi/3)+fxc, fy*np.sin(3*phi/2)+fyc])
        sk += 1
        phi += 36*5/n  #50*np.pi/n
        
def update(num, data, line):
    line.set_data(data[:2,num-200 :num])
    line.set_3d_properties(data[2,num-200 :num])
    ax.set_xlim3d([0+data[0,num-200], 36+data[0,num-200]])
    ax.set_xticklabels([])
    ax.grid(False)
def update2(num, data1,data2, line1,line2):
    #print(num)
    line1.set_data(data1[:2,num-200 :num])
    line1.set_3d_properties(data1[2,num-200 :num])
    line2.set_data(data1[0,num],data2[1:2,0 :200])
    line2.set_3d_properties(data2[2,0 :200])
    ax.set_xlim3d([0+data1[0,num-200], 36+data1[0,num-200]])
    ax.set_xticklabels([])
    ax.grid(False)    
    
N = 960
dataz0 = np.array(list(genxy0(N,fx=1,fy=1,fxc=0,fyc=0))).T
linez0, = ax.plot(dataz0[0, 0:1], dataz0[1, 0:1], dataz0[2, 0:1])
datay = np.array(list(genxy(N,fx=0,fy=1,fxc=-2,fyc=0))).T
liney, = ax.plot(datay[0, 0:1], datay[1, 0:1], datay[2, 0:1])
datax = np.array(list(genxy(N,fx=1,fy=0,fxc=0,fyc=-2))).T
linex, = ax.plot(datax[0, 0:1], datax[1, 0:1], datax[2, 0:1])
dataz = np.array(list(genxy(N,fx=1,fy=1,fxc=0,fyc=0))).T
linez, = ax.plot(dataz[0, 0:1], dataz[1, 0:1], dataz[2, 0:1])


# Setting the axes properties
ax.set_xlim3d([20, 70.0])
ax.set_xlabel('Z')

ax.set_ylim3d([-2.0, 2.0])
ax.set_ylabel('X')

ax.set_zlim3d([-2.0, 2.0])
ax.set_zlabel('Y')
elev=20. 
azim=35.
ax.view_init(elev, azim)

frames =200
s=180
for n in range(frames): #frames
    s+=1
    num = s%800+200
    update(num,datax,linex)
    update(num,datay,liney)
    update2(num,dataz,dataz0,linez,linez0)
    plt.pause(0.001)
    plt.savefig('./sin_wave/'+str(n)+'.png'.format(elev, azim))

from PIL import Image,ImageFilter
images = []
for n in range(0,frames,2):
    exec('a'+str(n)+'=Image.open("./sin_wave/'+str(n)+'.png")')
    images.append(eval('a'+str(n)))
images[0].save('./sin_wave/sin_wave_el{}_az{}.gif'.format(elev, azim),
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop=0)    
               
