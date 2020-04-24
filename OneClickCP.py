import bpy,os,datetime

class CheckPoint_PT_SaveCP (bpy.types.Panel):
    bl_label = 'Save CP'
    bl_idname ='Save_PT_cp'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'OneClick'


    def draw(self, context):
        layout = self.layout        
        scene = context.scene
        
        row = layout.row()
        row.prop(scene, 'named')
        
        row = layout.row()
        row.prop(scene, 'file_name')
        
        row = layout.row()
        row.label(text = 'description' ,icon='DOCUMENTS')
        
        row = layout.row()
        row.prop(scene, 'description')
        
        row = layout.row()
        self.layout.operator('save.button',icon= 'GREASEPENCIL')
        
        

class Save_OT_button(bpy.types.Operator):
    bl_label = 'Save'
    bl_idname = 'save.button'

    def execute(self, context):
        save_func()
        return{'FINISHED'}
    
regist_classes = (
    CheckPoint_PT_SaveCP,
    Save_OT_button
)    


def register():
    bpy.types.Scene.named = bpy.props.BoolProperty(
        name = 'named',
        default = False)
    bpy.types.Scene.file_name = bpy.props.StringProperty(name='File name',
                             default = '',
                             maxlen = 1024,)
    bpy.types.Scene.description =  bpy.props.StringProperty(name = '',
                             default = 'description',
                             maxlen = 1024,)

    for regist_cls in regist_classes:
        bpy.utils.register_class(regist_cls)


def unregister():
    for regist_cls in regist_classes:
        bpy.utils.unregister_class(regist_cls)
   
if __name__ == '__main__':
    register()


def save_func():
    file_path = bpy.data.filepath
    folder_path = os.path.splitext(bpy.data.filepath)[0] + '_blender'
    print(folder_path)
    
    if(file_path == ''):
        print('Please save the file you are working on and then execute')
        return

    try:
        os.mkdir(folder_path )
        f = open(folder_path + '/cp_version.txt', 'w')
        f.close()
    except FileExistsError as e:
        print(e.strerror)
    
    if(bpy.context.scene.named):
        save_name = bpy.context.scene.file_name
        
    else:
        file_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        save_name = file_name
    
    version = str(int (sum( [1 for _ in open(folder_path + '/cp_version.txt')] ) / 5 ) + 1)
    save_name = save_name + '_ver' + version
    
    dt_now = datetime.datetime.now().strftime('%Y_%_m_%d%H:%M:%S')
    
    f = open(folder_path + '/cp_version.txt', 'a')
    
    f.write('title  :' + save_name + '\n')
    f.write('time   :' + dt_now + '\n')

    if(bpy.context.scene.description != ''):
        f.write('comment:' + bpy.context.scene.description + '\n')
        
    f.write('\n\n')
    f.close()
    
    bpy.ops.wm.save_as_mainfile(copy = True,filepath = folder_path + '/' + save_name + '.blend')
