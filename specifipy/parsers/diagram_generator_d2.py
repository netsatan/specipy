from py_d2 import D2Connection, D2Diagram, D2Shape
from py_d2.shape import Shape

from specifipy.parsers.generic_parser import GenericParser
from specifipy.parsers.results import ParsingResult
from specifipy.parsers.structure.code_structure_definitions import (
    ClassStructureDefinition,
    FieldStructureDefinition,
    FunctionStructureDefinition,
    TypeAnnotatedFieldStructureDefinition,
)


class DiagramGenerator(GenericParser):
    def __generate_class_definition_d2(
        self,
        class_element: ClassStructureDefinition,
        fields: list[D2Shape] = None,
        methods: list[D2Shape] = None,
    ) -> D2Shape:
        fields = [] if fields is None else fields
        methods = [] if methods is None else methods
        result_shape = D2Shape(
            name=class_element.name, shape=Shape.classs, shapes=fields + methods
        )
        return result_shape

    def __generate_field_definition_d2(
        self, class_function_element: FieldStructureDefinition
    ) -> D2Shape:
        if isinstance(class_function_element, TypeAnnotatedFieldStructureDefinition):
            result_shape = D2Shape(
                name=class_function_element.name,
                label=f"'{class_function_element.type_annotation}'",
            )
        else:
            result_shape = D2Shape(name=class_function_element.name)

        return result_shape

    def __generate_class_function_definition_d2(
        self, method_element: FunctionStructureDefinition
    ) -> D2Shape:
        if method_element.return_type:
            result_shape = D2Shape(
                name=f"{method_element.name}({', '.join([x for x in method_element.params])})",
                label=f"'{method_element.return_type}'",
            )
        else:
            result_shape = D2Shape(
                name=f"{method_element.name}({', '.join([x for x in method_element.params])})"
            )
        return result_shape

    def generate_diagram(
        self, source_file_content: str, source_file_name: str, base_path: str = None
    ):
        parsing_result: ParsingResult = self.parse(source_file_content)
        elements_to_generate = []
        link_to_generate = []

        class_element: ClassStructureDefinition
        for class_element in parsing_result.classes:
            class_functions = [
                self.__generate_class_function_definition_d2(x)
                for x in parsing_result.functions
                if x.parent_class == class_element.name
            ]
            class_fields = [
                self.__generate_field_definition_d2(x)
                for x in parsing_result.class_fields
                if x.parent_class == class_element
            ]
            elements_to_generate.append(
                self.__generate_class_definition_d2(
                    class_element, fields=class_fields, methods=class_functions
                )
            )
            if class_element.inherits_from:
                link_to_generate.append(
                    D2Connection(
                        shape_1=class_element.name, shape_2=class_element.inherits_from
                    )
                )
        diagram = D2Diagram(shapes=elements_to_generate, connections=link_to_generate)
        print(f"{source_file_name}, diagram '{diagram}'")
        if str(diagram) is not None and str(diagram) != "":
            with open(
                f"{base_path if base_path else ''}{source_file_name}.d2",
                "w",
                encoding="utf-8",
            ) as output_file:
                output_file.write("direction: up\n")
                output_file.write(str(diagram))
