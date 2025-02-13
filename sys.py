bl_info = {
    "name": "Hello World Sidebar",
    "blender": (3, 0, 0),
    "category": "3D View",
    "author": "Your Name",
    "version": (1, 0),
    "location": "View3D > Sidebar > Hello Tab",
    "description": "Adds a sidebar tab with a Hello World button",
    "warning": "",
    "doc_url": "",
}

import bpy
import shutil
#import os
import platform
    
class SET_CONFIG(bpy.types.Operator):
    bl_idname = "button.setconfig"
    bl_label = "SET CONFIG"

    def execute(self, context):
        def setConfig(from1, to1):
            try:
                shutil.copy(from1, to1)
                print("CLOUD CONFIG --- UPDATED")
                bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text='CLOUD CONFIG UPDATED'))
            except FileNotFoundError:
                print('FILE NOT FOUND----')
            except PermissionError:
                print("Permission denied. Please check your file permissions.")
            except Exception as e:
                print('UNKNOW ERROR OCCURED {e}')
        startup = [ 
            "/Users/minhhoangtran/Library/Application Support/Blender/4.3/config/startup.blend",
            "/Users/minhhoangtran/Library/CloudStorage/OneDrive-Personal/Desktop/config1/config_blender/",
            r"C:\Users\djt_3\AppData\Roaming\Blender Foundation\Blender\4.3\config\startup.blend",
            r"C:\Users\djt_3\OneDrive\Desktop\config1\config_blender", 
        ]
        userpref = [
            "/Users/minhhoangtran/Library/Application Support/Blender/4.3/config/userpref.blend",
            "/Users/minhhoangtran/Library/CloudStorage/OneDrive-Personal/Desktop/config1/config_blender/",
            r"C:\Users\djt_3\AppData\Roaming\Blender Foundation\Blender\4.3\config\userpref.blend",
            r"C:\Users\djt_3\OneDrive\Desktop\config1\config_blender",
        ]
        if platform.system() == "Darwin":
            setConfig(startup[0],startup[1])
            setConfig(userpref[0],userpref[1])
        if platform.system() == "Windows":
            setConfig(startup[2],startup[3])
            setConfig(userpref[2],userpref[3])
        return {'FINISHED'}

class GET_CONFIG(bpy.types.Operator):
    bl_idname = "button.getconfig"
    bl_label = "GET CONFIG"

    def execute(self, context):
        def setConfig(from1, to1):
            try:
                shutil.copy(from1, to1)
                print("LOCAL CONFIG --- UPDATED")
                bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text='CLOUD CONFIG UPDATED'))
            except FileNotFoundError:
                print('FILE NOT FOUND----')
            except PermissionError:
                print("Permission denied. Please check your file permissions.")
            except Exception as e:
                print('UNKNOW ERROR OCCURED {e}')
        startup = [ 
            "/Users/minhhoangtran/Library/CloudStorage/OneDrive-Personal/Desktop/config1/config_blender/startup.blend",
            "/Users/minhhoangtran/Library/Application Support/Blender/4.3/config/",
            r"C:\Users\djt_3\OneDrive\Desktop\config1\config_blender\startup.blend",
            r"C:\Users\djt_3\AppData\Roaming\Blender Foundation\Blender\4.3\config",
        ]
        userpref = [
            "/Users/minhhoangtran/Library/CloudStorage/OneDrive-Personal/Desktop/config1/config_blender/userpref.blend",
            "/Users/minhhoangtran/Library/Application Support/Blender/4.3/config/",
            r"C:\Users\djt_3\OneDrive\Desktop\config1\config_blender\userpref.blend",
            r"C:\Users\djt_3\AppData\Roaming\Blender Foundation\Blender\4.3\config",
        ]
        if platform.system() == "Darwin":
            setConfig(startup[0],startup[1])
            setConfig(userpref[0],userpref[1])
        if platform.system() == "Windows":
            setConfig(startup[2],startup[3])
            setConfig(userpref[2],userpref[3])
        return {'FINISHED'}

# Creates a Panel in the Sidebar ---------------------------------------------        
class HELLO_PT_Panel(bpy.types.Panel):
    bl_label = "--- CONFIG ---"
    bl_idname = "HELLO_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "@_8000"

    def draw(self, context):
        layout = self.layout
        layout.operator("button.setconfig",text="--- config_SET1")
        layout.operator("button.getconfig",text="--- config_GET1")
        
classes = [GET_CONFIG, SET_CONFIG, HELLO_PT_Panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
