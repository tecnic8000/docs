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
import os
import platform

class HELLO_OT_ButtonOperator(bpy.types.Operator):
    """Prints Hello World"""
    bl_idname = "hello.button_operator"
    bl_label = "Hello World"

    def execute(self, context):
        print("Hello, World!")
        return {'FINISHED'}
    
class SET_CONFIG(bpy.types.Operator):
    bl_idname = "button.setconfig"
    bl_label = "SET CONFIG"
    # 0:mac local, 1:mac cloud, 2:win local, 3:win cloud
    def execute(self, context):
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
        try:
            if platform.system() == "Darwin":
                shutil.copy(startup[0], startup[1])
                shutil.copy(userpref[0], userpref[1])
                print("CONFIG SET FROM MAC")
            if platform.system() == "Windows":
                shutil.copy(startup[2], startup[3])
                shutil.copy(userpref[2], userpref[3])
                print("CONFIG SET FROM WIN")
            bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text='CLOUD CONFIG UPDATED'))
        except FileNotFoundError:
            print('FILE NOT FOUND----')
        except PermissionError:
            print("Permission denied. Please check your file permissions.")
        except Exception as e:
            print('UNKNOW ERROR OCCURED {e}')
        return {"SET FINISHED"}


class HELLO_PT_Panel(bpy.types.Panel):
    """Creates a Panel in the Sidebar"""
    bl_label = "Hello Panel"
    bl_idname = "HELLO_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SYS"

    def draw(self, context):
        layout = self.layout
        layout.operator("hello.button_operator", text="Hello World1")
        layout.operator("button.setconfig",text="SET CONFIG1")
    
        

classes = [HELLO_OT_ButtonOperator, HELLO_PT_Panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
