bl_info = {
    "name": "Set Frame Range",
    "author": "Matt Carrier",
    "version": (1, 2),
    "blender": (3, 5, 0),
    "location": "Sequencer > Sidebar > Export Helper",
    "description": "Set the frame range start and end to the start and end of the actively selected clip",
    "category": "Sequencer",
    "warning" : "",
    'support': 'COMMUNITY',
    "wiki_url" : "",
    "tracker_url" : "https://github.com/icecreammatt/blender-set-frame-range",
}

import bpy
from bpy.utils import register_class, unregister_class

def update_frame_range_to_selected_sequence():
    ctx = bpy.context
    active_sequence = ctx.active_sequence_strip

    print("Active Strip Name Start:", active_sequence.frame_final_start)
    print("Active Strip Name End:", active_sequence.frame_final_end)

    start = active_sequence.frame_final_start
    end = active_sequence.frame_final_end
    ctx.scene.frame_start = int(start)
    ctx.scene.frame_end = int(end)

class BUTTON_CUSTOM(bpy.types.Operator):
    """Set the frame range start and end to the start and end of the actively selected clip"""
    bl_label = "Set Frame Range"
    bl_idname = "object.button_custom"

    def execute(self, context):
        update_frame_range_to_selected_sequence()
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
    register()
