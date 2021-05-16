# make curl function
"""
curl w=nabla X U = i(dw/dy -dv/dz) - j ( dw/dx - dy/dz) + k ( dv/dx - du/dy)

curl is rotation 
 + : Counterclockwise
 - : clockwise
"""
import numpy as np
def curl2D(u,v,lon,lat):
  # cur in 2 dimension
  dx=len(lon)
  dy=len(lat)
  #i(dw/dy -dv/dz) - j ( dw/dx - dy/dz)
  du_dx,du_dy=np.gradient(u,dx,dy)
  dv_dx,dv_dy=np.gradient(v,dx,dy)

  zeta= dv_dx- du_dy
  return zeta

#curl3D code is based on https://stackoverflow.com/questions/30378676/calculate-curl-of-a-vector-field-in-python-and-plot-it-with-matplotlib
def curl3D(u,v,w,x,y,z):
  #curl in 3 dimension
  dx=len(x)
  dy=len(y)
  dz=len(z)

  #i(dw/dy -dv/dz) - j ( dw/dx - dy/dz) + k ( dv/dx - du/dy)
  dx_dx,dx_dy,dx_dz=np.gradient(u,dx,dy,dz)
  dy_dx,dy_dy,dy_dz=np.gradient(v,dx,dy,dz)
  dz_dx,dz_dy,dz_dz=np.gradient(z,dx,dy,dz)

  rotation_x=dz_dy-dy_dx
  rotation_y=dx_dz-dx_dz
  rotation_z=dy_dx-dx_dy

  total_rotation=rotation_x-rotation_y+rotation_z

  return rotation_x,rotation_y,rotation_z,total_rotation



