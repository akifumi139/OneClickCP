import bpy

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
        row.prop(scene, "self_rename")
        
        row =layout.row()
        row.prop(scene, "file_name")
        
        row =layout.row()
        row.prop(scene, "overwrite")
        
        row =layout.row()
        row.prop(scene, "description")
        
        row =layout.row()
        row.label(text = "description" ,icon="DOCUMENTS")
        
        row = layout.row()
        self.layout.operator("save.button",icon= 'GREASEPENCIL')

class Save_OT_button(bpy.types.Operator):
    bl_label = "Save"
    bl_idname = "save.button"

    def execute(self, context):
        print("pushed")
        return{'FINISHED'}
    
regist_classes = (
    CheckPoint_PT_ui,
    Save_OT_button
)    
        
def register():
    bpy.types.Scene.self_rename = bpy.props.BoolProperty(
        name="Self rename",
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