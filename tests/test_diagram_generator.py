import base64
import os
from unittest import TestCase

from specifipy.parsers.diagram_generator import DiagramGenerator


class DiagramGeneratorTest(TestCase):
    base_path = os.path.dirname(__file__)
    test_results_path = f"{base_path}/results/"

    def tearDown(self) -> None:
        for f in os.listdir(self.test_results_path):
            os.remove(f"{self.test_results_path}" + f)

    def __load_test_file_old_python(self):
        path = f"{self.base_path}/examples/complex_number_old_python.py"
        return self.__load_file(path)

    def __load_test_file_modern_python(self):
        path = f"{self.base_path}/examples/simple_addition_modern_python.py"
        return self.__load_file(path)

    def __load_django_models_file(self):
        path = f"{self.base_path}/examples/models.py"
        return self.__load_file(path)

    def __load_file(self, path):
        with open(f"{path}") as source_code:
            fetched_source = source_code.read()
        return fetched_source

    def test_can_create_diagram_for_file(self):
        # @:given There's a class with Python code in it
        fetched_source: str = self.__load_test_file_old_python()
        current_dir = os.path.dirname(__file__)

        # @:when Diagrams generator is run
        diagram_generator = DiagramGenerator()
        diagram_generator.generate_diagram(
            fetched_source,
            "complex_number_old_python.py",
            base_path=f"{current_dir}/results/",
        )

        # @:then Generated diagram matches the example
        example_file_content: bytes
        generated_file_content: bytes
        with open(
            f"{current_dir}/examples/diagrams/complex_number_old_python.py.png", "rb"
        ) as example_file:
            example_file_content = base64.b64encode(bytes(example_file.read()))
        with open(
            f"{current_dir}/results/complex_number_old_python.py.png", "rb"
        ) as generated_file:
            generated_file_content = base64.b64encode(bytes(generated_file.read()))

        self.assertEqual(example_file_content, generated_file_content)

    def test_can_generate_diagram_for_modern_python(self):
        # @:given There's a class with Python code in it
        fetched_source: str = self.__load_test_file_modern_python()
        current_dir = os.path.dirname(__file__)

        # @:when Diagrams generator is run
        diagram_generator = DiagramGenerator()
        diagram_generator.generate_diagram(
            fetched_source,
            "simple_addition_modern_python.py",
            base_path=f"{current_dir}/results/",
        )

        # @:then Generated diagram matches the example
        example_file_content: bytes
        generated_file_content: bytes
        with open(
            f"{current_dir}/examples/diagrams/simple_addition_modern_python.py.png",
            "rb",
        ) as example_file:
            example_file_content = base64.b64encode(bytes(example_file.read()))
        with open(
            f"{current_dir}/results/simple_addition_modern_python.py.png", "rb"
        ) as generated_file:
            generated_file_content = base64.b64encode(bytes(generated_file.read()))

        self.assertEqual(example_file_content, generated_file_content)

    def test_can_generate_diagram_for_django_model(self):
        # @:given There's a class with Python code in it
        fetched_source: str = self.__load_django_models_file()
        current_dir = os.path.dirname(__file__)

        # @:when Diagrams generator is run
        diagram_generator = DiagramGenerator()
        diagram_generator.generate_diagram(
            fetched_source, "models.py", base_path=f"{current_dir}/results/"
        )

        # @:then Generated diagram matches the example
        example_file_content: bytes
        generated_file_content: bytes
        with open(
            f"{current_dir}/examples/diagrams/models.py.png", "rb"
        ) as example_file:
            example_file_content = base64.b64encode(bytes(example_file.read()))
        with open(f"{current_dir}/results/models.py.png", "rb") as generated_file:
            generated_file_content = base64.b64encode(bytes(generated_file.read()))

        self.assertEqual(example_file_content, generated_file_content)
