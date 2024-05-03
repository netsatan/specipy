# Specifipy
### Python package for auto-generating code diagrams
<img height="150" src="./docs/OIG3.jpeg" width="150"/>

## What is that? 
Specifipy helps you *visually* understand code. It generates **UML code diagrams** 
for your object-oriented programs showing you the inheritance, interfaces, fields, methods and
functions. Assuming you need to provide a very detailed documentation of your OO software, see if the
things make sense or not, you're going through some kind of audit - it might prove useful.

## How to use that? 
### Scanning directory and generating diagrams for all files
Import the `specifipy` class you need. If you want to recursively scan the directory (probably 
the most common usecase) just follow these steps:
```python
from specifipy.file_scanners.directory_scanner import DirectoryScanner
d = DirectoryScanner("/path/to/your/src/directory")
d.make_diagrams()
```

This will create all the diagrams for all the files that contain Python classes right in your working dir. You can, of
course, provide the directory in `make_diagrams` to have the output file wherever you wish.

### Using Java?
In such case, you'll need to provide additional arguments, like this:
```python
from specifipy.file_scanners.directory_scanner import DirectoryScanner
from specifipy.parsers.generic_parser import FileType
d = DirectoryScanner("/path/to/your/src/directory", FileType.JAVA)
d.make_diagrams()
```

### In-place diagram generation
If you want to generate diagram in-place, for a single file, you can just load its context into a string and
then provide it directly to the `DiagramGenerator`, like this:
```python
from specifipy.parsers.diagram_generator_d2 import DiagramGenerator

diagram_generator = DiagramGenerator()
diagram_generator.generate_diagram(
    file_contents_str,
    "complex_number_old_python.py",
    base_path=f"./diagrams/",
)
```

Of course, you can provide as `file_contents_str` any valid code however you'd like, not only from a file.

### Available parsers
Currently, there are two parsers available - one for Java and one for Python:
![](./docs/parsers.svg)

### Diagram example
The complete diagram for the below code:
```python
class BaseClassForTest:
    pass


class SomeTest(BaseClassForTest):
    pass


class ComplexNumber(SomeTest):
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """

    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.

        Parameters:
           @:param real (int): The real part of complex number.
           @:param imag (int): The imaginary part of complex number.
        """
        self.real = real

    def add(self, num):
        """
        The function to add two Complex Numbers.

        Parameters:
            num (ComplexNumber): The complex number to be added.

        Returns:
            ComplexNumber: A complex number which contains the sum.
        """

        re = self.real + num.real
        im = self.imag + num.imag

        return ComplexNumber(re, im)

```
...looks something like this:
![Example 1](./tests/examples/diagrams/complex_number_old_python.py.png)

or for the code:
```python
class MathOperation:
    pass


class Addition(MathOperation):

    type_annotated_field_in_class: int
    not_annotated_field = 0


    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def sum_numbers(self) -> int:
        running_sum: int = 0
        for number in self.numbers:
            running_sum += number

        return running_sum

```
it'll be something closer to this:
![Example 2](./tests/examples/diagrams/simple_addition_modern_python.py.png)


And here's this exact codebase (including examples above):
![Codebase example](./tests/examples/diagrams/d2.svg)

---
So, in reality you get a d2 file (or a set of d2 files, depending on the `collect_files` parameter). 
Your actual output follows the d2 specification:
```d2
direction: up
BaseClassForTest: {
  shape: class
}
SomeTest: {
  shape: class
}
ComplexNumber: {
  __init__(self, real, imag): 'None'
  add(self, num): 'None'
  shape: class
}
SomeTest -> BaseClassForTest
ComplexNumber -> SomeTest
```

If you're generating Java code, the dotted line is used to indicate implemented interface instead of class inheritance,
and private fields and methods are marked accordingly.

---
If you like this project, and it helped you in any way, I'll be thrilled to know that! I like to write software that's 
actually useful.
