import bpy
from bpy.types import Node
from mn_node_helper import AnimationNode
from mn_execution import nodePropertyChanged

class ToIntegerConversion(Node, AnimationNode):
	bl_idname = "ToIntegerConversion"
	bl_label = "To Integer"
	
	def init(self, context):
		self.inputs.new("GenericSocket", "Value")
		self.outputs.new("IntegerSocket", "Number")
		
	def execute(self, input):
		output = {}
		output["Number"] = int(input["Value"])
		return output
		
# register
################################
		
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)