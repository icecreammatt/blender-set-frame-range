import bpy

print("Registering Custom Panel")

class BUTTON_CUSTOM(bpy.types.Operator):
    """Set the frame range start and end to the start and end of the actively selected clip"""
    bl_label = "Set Frame Range"
    bl_idname = "object.button_custom"

    def execute(self, context):
        ctx = bpy.context
        print("Active Strip Name Start:", ctx.active_sequence_strip.frame_final_start)
        print("Active Strip Name End:", ctx.active_sequence_strip.frame_final_end)
        start = ctx.active_sequence_strip.frame_final_start
        end = ctx.active_sequence_strip.frame_final_end
        ctx.scene.frame_start = int(start)
        ctx.scene.frame_end = int(end)
        return { 'FINISHED' }

class PANEL_CUSTOM_UI(bpy.types.Panel):
    bl_label = "Export Helpers"
    bl_idname = "OBJECT_PT_panel"
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Export Utils"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text = "Select")

        row = layout.row()
        row.scale_y = 2
        row.operator("object.button_custom", text = "Set frame range from selection", icon = "TRIA_RIGHT")

def register():
    bpy.utils.register_class(PANEL_CUSTOM_UI)
    bpy.utils.register_class(BUTTON_CUSTOM)

def unregister():
    bpy.utils.register_class(PANEL_CUSTOM_UI)
    bpy.utils.register_class(BUTTON_CUSTOM)

if __name__ == "__main__":
    register()
