from diagrams import Diagram, Edge
from diagrams.custom import Custom

param_icon = "../../../resources/icons/param_icon.png"
function_icon = "../../../resources/icons/function_icon.png"
class_icon = "../../../resources/icons/class_icon.png"
dotted_line = Edge(style="dotted")

with Diagram("complex_number_old_python.py", show=False):
    class_BaseClassForTest = Custom('BaseClassForTest', class_icon)
    class_SomeTest = Custom('SomeTest', class_icon)
    class_ComplexNumber = Custom('ComplexNumber', class_icon)
    func___init___ComplexNumber = Custom('__init__', function_icon)
    param_self___init___ComplexNumber = Custom('self', param_icon)
    param_real___init___ComplexNumber = Custom('real', param_icon)
    param_imag___init___ComplexNumber = Custom('imag', param_icon)
    func_add_ComplexNumber = Custom('add', function_icon)
    param_self_add_ComplexNumber = Custom('self', param_icon)
    param_num_add_ComplexNumber = Custom('num', param_icon)
    class_BaseClassForTest >> dotted_line >> class_SomeTest
    class_SomeTest >> dotted_line >> class_ComplexNumber
    func___init___ComplexNumber >> class_ComplexNumber
    param_self___init___ComplexNumber >> func___init___ComplexNumber
    param_real___init___ComplexNumber >> func___init___ComplexNumber
    param_imag___init___ComplexNumber >> func___init___ComplexNumber
    func_add_ComplexNumber >> class_ComplexNumber
    param_self_add_ComplexNumber >> func_add_ComplexNumber
    param_num_add_ComplexNumber >> func_add_ComplexNumber
