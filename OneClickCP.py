import bpy,os,datetime

class CheckPoint_PT_ui (bpy.types.Panel):
    bl_label = "Check Point"
    bl_idname ="CheckPoint_PT_ui"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'OneClick'

    def draw(self, context):
        layout = self.layout        
        scene = context.scene
        
        row =layout.row()
        row.prop(scene, "named")
        
        row =layout.row()
        row.prop(scene, "file_name")
        
        row =layout.row()
        row.label(text = "description" ,icon="DOCUMENTS")
        
        row =layout.row()
        row.prop(scene, "description")
        
        row = layout.row()
        self.layout.operator("save.button",icon= 'GREASEPENCIL')
        
        #row.prop(scene, "overwrite")
        

class Save_OT_button(bpy.types.Operator):
    bl_label = "Save"
    bl_idname = "save.button"

    def execute(self, context):
        save_func()
        return{'FINISHED'}
    
regist_classes = (
    CheckPoint_PT_ui,
    Save_OT_button
)    
        
def register():
    bpy.types.Scene.named = bpy.props.BoolProperty(
        name="named",
        default = False)
    bpy.types.Scene.file_name = bpy.props.StringProperty(name="File name",
                             default="",
                             maxlen=1024,)
    bpy.types.Scene.description =  bpy.props.StringProperty(name="",
                             default="description",
                             maxlen=1024,)
    bpy.types.Scene.overwrite = bpy.props.BoolProperty(
        name="Overwrite",
        default = False)
    for regist_cls in regist_classes:
        bpy.utils.register_class(regist_cls)
   
def unregister():
    for regist_cls in regist_classes:
        bpy.utils.unregister_class(regist_cls)
   
if __name__ == "__main__":
    register()




def save_func():
    
    filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
    if(filename==''):
        print("Please save the file you are working on and then execute")
        return
    
    
    foldername= filename+'_blend'

    try:
        os.mkdir(foldername)
        f = open(foldername+"/cp_version.txt", "w")
        f.close()
    except FileExistsError as e:
        print(e.strerror)
    
    
    if(bpy.context.scene.named):
        path=bpy.context.scene.file_name+dt_now+".blend"
    else:
        dt_now = datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S')
        path="filename"+dt_now+".blend"

    f = open(foldername+"/cp_version.txt", "a")
    
    f.write(path+" : ")
    if(bpy.context.scene.description != ""):
        f.write(bpy.context.scene.description)
        
    f.write("\n\n")
    f.close()
    
    bpy.ops.wm.save_as_mainfile(copy=True,filepath=foldername+"/"+path)
