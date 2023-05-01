import bpy
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Set Frame",
    "author": "Matt Carrier",
    "version": (1, 1),
    "blender": (1, 5, 0),
    "location": "Sequencer > Sidebar > Export Helper",
    "description": "Set the frame range start and end to the start and end of the actively selected clip",
    "category": "Sequencer",
    "wiki_url": "",
    "warning": ""
}
    # "location": "Sequencer > Sidebar > Export Utils",

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

_classes = [
    PANEL_CUSTOM_UI,
    BUTTON_CUSTOM
]

def register():
    for cls in _classes:
        register_class(cls)

def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    print("Running script")
    register()
else:
    print("Starting addon")
    register()
