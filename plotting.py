# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:13:26 2023

@author: ktwhi
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.animation import FuncAnimation
import planar as p

def gol(obj, time, frames, m, s, radius):
    faces = np.array(obj.mesh_list[0].faces)
    vertices = np.array(obj.vertices)
    kernel, face_values = p.generate_game_state(faces, len(vertices))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=30, azim=-60)
    ax.dist = 30
    ax.set_title('Lenia3d: An Lenia Extension')
    def update(frame):
        nonlocal face_values
        face_values = p.gol_update(face_values, kernel, m, s, radius)
        intensities = face_values
        ax.clear()
        mesh = ax.add_collection3d(art3d.Poly3DCollection(vertices[faces], facecolors=plt.cm.viridis(intensities)))
        return mesh,
    
    ani = FuncAnimation(fig, update, frames=time*frames, interval=1000/frames, repeat=True)
    plt.show()
from pywavefront import Wavefront
teapot_path = "C:/Users/ktwhi/OneDrive - University of Bristol/Python Scripts/Lenia3D/Net/teapot.obj"

teapot = Wavefront(teapot_path, collect_faces=True)
animate_mesh_gol(teapot,10,20,0.15,0.05,10)