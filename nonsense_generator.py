import random
import string
from typing import List, Optional, Union, Dict

# Generate some randome Nonsense pine(ish), someewhat done..
# does not match types to values quite yet..  
# Example output (mildly formatted):

'''
// @description zfedqzu drfpx okbcqig jpge pyhgs gjdnpp
import cxdxcfy/ghutofm/10 as nsz
import ntzar/eaaa/8                                                                             
import gjhmm/qippnct/4                                                                          
import pma/auci/10 as qjfev                                                                     
import bsn/fxjs/5                                                                               
// @type hrux pgze zequet otdvvbs                                                               
type clybb                                                                                      
   color  field1= na // @field otktg fcaaeu pgnip                                                
   string field2= "lcgy yrlikj tux jza pla ulllteu mdjlszm" // @field iusppcf okhzzfk yoktc nhqthk
// @type fbwa owwon ulqdce
type jlcp
   matrix<string> field1// @field qqixtf gpfnoj qnrzi oxlaou anyrb tso ljzbldy
   array<string>  field2// @field ryvkuj xzquwo rvpkk vor
   array<color>   field3// @field irqui kpbpwhz dzq zehi
// @type rfjcaka bfdh bozcd kmxyxan
type coamvfn
   float field1= na // @field rtk bukoq efzvhf gzunu
omre()                                                                                                                                      => array<int>
mdqcsp(array<bool> ylrhct, array<string> qoyjayo)                                                                                           => int
dijue(array<string> vnkb, matrix<string> wksoy, matrix<float> tsl, matrix<float> zwlmz)                                                     => array<float>
hwdl()                                                                                                                                      => matrix<color>
xyql()                                                                                                                                      => array<string>
eekezw(string bzqj = 34.934035950472776, array<bool> wifm)                                                                                  => int
qeos(matrix<string> fnzoxi, matrix<string> kobdok)                                                                                          => bool
tvkyn(float rbdomeh = "mseupo utqd hfnz", array<float> zhofmcv, string bkgkfo = "jxd sqaptk mmdr", array<string> vmbhh, array<string> unpv) => float
'''

class Import:
    """Represents an import statement with user, script, version, and optional alias."""

    def __init__(
        self, user: str, script: str, version: int, alias: Optional[str] = None
    ):
        """Initializes an Import object.

        :param user: The username of the script owner.
        :param script: The name of the script to import.
        :param version: The version number of the script.
        :param alias: An optional alias for the imported script.
        """
        self.user: str = user
        self.script: str = script
        self.version: int = version
        self.alias: Optional[str] = alias

    def __str__(self) -> str:
        """Returns the import statement as a string.

        :return: The import statement.
        """
        base_import = f"import {self.user}/{self.script}/{self.version}"
        return f"{base_import} as {self.alias}" if self.alias else base_import

class StorageType:
    """
    Defines a storage type with a base type and optional modifiers like array or matrix.
    """

    def __init__(self, base_type: str, modifier: Optional[str] = None):
        """Initializes a StorageType object.

        :param base_type: The base type (e.g., "int", "float", "string").
        :param modifier: The modifier, if any ("array" or "matrix").
        """
        self.base_type: str = base_type
        self.modifier: Optional[str] = modifier

    def __str__(self) -> str:
        """Returns the storage type as a string.

        :return: The formatted storage type.
        """
        if self.modifier == "array":
            return f"array<{self.base_type}>"
        return f"matrix<{self.base_type}>" if self.modifier == "matrix" else self.base_type

    @staticmethod
    def random():
        """Generates a random storage type.

        :return: A randomly generated StorageType.
        """
        base_type = random.choice(["bool", "int", "float", "color", "string"])
        modifier = random.choice([None, "array", "matrix"])
        return StorageType(base_type, modifier)

class Annotation:
    """Represents an annotation with a tag and description."""

    def __init__(self, tag: str, description: str):
        """Initializes an Annotation object.

        :param tag: The annotation tag (e.g., "param", "return").
        :param description: The description of the annotated element.
        """
        self.tag: str = tag
        self.description: str = description

    def __str__(self) -> str:
        """Returns the annotation as a string.

        :return: The formatted annotation.
        """
        return f"// @{self.tag} {self.description}"

class Field:
    """Represents a field within a User-Defined Type (UDT)."""

    def __init__(
        self,
        name: str,
        storage_type: StorageType,
        default_value: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """Initializes a Field object.

        :param name: The name of the field.
        :param storage_type: The StorageType of the field.
        :param default_value: The default value of the field, if any.
        :param description: The description of the field, if any.
        """
        self.name: str = name
        self.storage_type: StorageType = storage_type
        self.default_value: Optional[str] = default_value
        self.description: Optional[str] = description

    def __str__(self) -> str:
        """Returns the field definition as a string.

        :return: The formatted field definition.
        """
        default_str = f" = {self.default_value}" if self.default_value else ""
        desc_str = (
            f" // @field {self.description}" if self.description else ""
        )
        return f"  {self.storage_type} {self.name}{default_str}{desc_str}"

class Parameter:
    """Represents a function parameter."""

    def __init__(
        self,
        name: str,
        storage_type: Optional[StorageType] = None,
        default_value: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """Initializes a Parameter object.

        :param name: The name of the parameter.
        :param storage_type: The StorageType of the parameter, if any.
        :param default_value: The default value of the parameter, if any.
        :param description: The description of the parameter, if any.
        """
        self.name: str = name
        self.storage_type: Optional[StorageType] = storage_type
        self.default_value: Optional[str] = default_value
        self.description: Optional[str] = description
        self.annotation: Optional[Annotation] = (
            Annotation("param", description) if description else None
        )

    def __str__(self) -> str:
        """Returns the parameter definition as a string.

        :return: The formatted parameter definition.
        """
        if self.storage_type:
            if self.storage_type.modifier in ["matrix", "array"]:
                return f"{self.storage_type} {self.name}"
            dv = (
                f" = {self.default_value}"
                if self.default_value
                else ""
            )
            return f"{self.storage_type} {self.name}{dv}"
        return f"{self.name}"

class UDT:
    """Represents a User-Defined Type (UDT)."""

    def __init__(
        self,
        name: str,
        fields: List[Field],
        description: Optional[str] = None,
    ):
        """Initializes a UDT object.

        :param name: The name of the UDT.
        :param fields: The list of Fields that make up the UDT.
        :param description: The description of the UDT, if any.
        """
        self.name: str = name
        self.fields: List[Field] = fields
        self.description: Optional[str] = description
        self.annotation: Optional[Annotation] = (
            Annotation("type", description) if description else None
        )

    def __str__(self) -> str:
        """Returns the UDT definition as a string.

        :return: The formatted UDT definition.
        """
        type_desc = (
            f"// @type {self.description}\n" if self.description else ""
        )
        field_str = "\n".join(str(f) for f in self.fields)
        return f"{type_desc}type {self.name} \n{field_str}"

class ReturnValue:
    """Represents a function's return value."""

    def __init__(
        self,
        storage_type: Optional[StorageType] = None,
        description: Optional[str] = None,
    ):
        """Initializes a ReturnValue object.

        :param storage_type: The StorageType of the return value, if any.
        :param description: The description of the return value, if any.
        """
        self.storage_type: Optional[StorageType] = storage_type
        self.description: Optional[str] = description

    def __str__(self) -> str:
        """Returns the return value definition as a string.

        :return: The formatted return value definition.
        """
        return str(self.storage_type) if self.storage_type else ""

class Function:
    """Represents a function definition."""

    def __init__(
        self,
        name: str,
        parameters: List[Parameter],
        return_value: ReturnValue,
        description: Optional[str] = None,
    ):
        """Initializes a Function object.

        :param name: The name of the function.
        :param parameters: The list of Parameters for the function.
        :param return_value: The ReturnValue of the function.
        :param description: The description of the function, if any.
        """
        self.name: str = name
        self.parameters: List[Parameter] = parameters
        self.return_value: ReturnValue = return_value
        self.description: Optional[str] = description
        self.annotations: List[Annotation] = [
            p.annotation for p in parameters if p.annotation
        ]

    def __str__(self) -> str:
        """Returns the function definition as a string.

        :return: The formatted function definition.
        """
        param_str = ", ".join(str(p) for p in self.parameters)
        return f"{self.name}({param_str}) => {self.return_value}"

class Script:
    """Represents a complete script."""

    def __init__(
        self,
        name: str,
        imports: List[Import],
        udts: List[UDT],
        functions: List[Function],
        description: Optional[str] = None,
    ):
        """Initializes a Script object.

        :param name: The name of the script.
        :param imports: The list of Imports used in the script.
        :param udts: The list of UDTs defined in the script.
        :param functions: The list of Functions defined in the script.
        :param description: The description of the script, if any.
        """
        self.name: str = name
        self.imports: List[Import] = imports
        self.udts: List[UDT] = udts
        self.functions: List[Function] = functions
        self.description: Optional[str] = description
        self.annotation: Optional[Annotation] = (
            Annotation("description", description) if description else None
        )

    def __str__(self):
        """
        for testing, not a part of the script exactly, but could be to export it.
        """
        script_code_content = ""
        script_code_content += str(self.annotation) if self.annotation else ""
        script_code_content += "\n"
        script_code_content += "\n".join([str(imp) for imp in self.imports])
        script_code_content += "\n"
        script_code_content += "\n".join([str(udt) for udt in self.udts])
        script_code_content += "\n"
        script_code_content += "\n".join([str(func) for func in self.functions])
        script_code_content += "\n"
        return script_code_content

class Generator:
    """Generates random script components for testing."""

    def __init__(self):
        """Initializes the Generator with empty lists for tracking generated components."""
        self.generated_udt_names: List[str] = []
        self.generated_function_names: List[str] = []

    @staticmethod
    def random_word() -> str:
        """Generates a random word.

        :return: A random word.
        """
        return "".join(
            random.choice(string.ascii_lowercase)
            for _ in range(random.randint(3, 7))
        )

    def random_sentence(self, min_words: int = 3, max_words: int = 7) -> str:
        """Generates a random sentence.

        :param min_words: The minimum number of words in the sentence.
        :param max_words: The maximum number of words in the sentence.
        :return: A random sentence.
        """
        return " ".join(
            self.random_word() for _ in range(random.randint(min_words, max_words))
        )

    def random_name(self, prefix: Optional[str] = None) -> str:
        """Generates a random name, optionally with a prefix.

        :param prefix: An optional prefix for the name.
        :return: A random name.
        """
        name = self.random_word()
        return f"{prefix}.{name}" if prefix else name

    def storage_type(self) -> StorageType:
        """Generates a random StorageType.

        :return: A randomly generated StorageType.
        """
        return StorageType.random()

    def default_value(self) -> str:
        """Generates a random default value.

        :return: A random default value as a string.
        """
        value_type = random.choice(["INT", "FLOAT", "BOOL", "STRING", "NA"])
        if value_type == "INT":
            return str(random.randint(0, 100))
        if value_type == "FLOAT":
            return str(random.uniform(0, 100))
        if value_type == "BOOL":
            return str(random.choice([True, False]))
        if value_type == "STRING":
            return f'"{self.random_sentence()}"'
        return "na"

    def udt_field(
        self,
        udt_name: str,
        field_index: int,
    ) -> Field:
        """Generates a random Field for a UDT.

        :param udt_name: The name of the UDT the field belongs to.
        :param field_index: The index of the field within the UDT.
        :return: A randomly generated Field.
        """
        name = f"field{field_index}"
        storage_type = self.storage_type()
        default_value = (
            self.default_value()
            if storage_type.modifier is None
            else None
        )
        description = self.random_sentence()
        return Field(name, storage_type, default_value, description)

    def udt(self) -> UDT:
        """Generates a random UDT.

        :return: A randomly generated UDT.
        """
        name = self.random_name()
        self.generated_udt_names.append(name)
        num_fields = random.randint(1, 5)
        fields = [
            self.udt_field(name, i) for i in range(1, num_fields + 1)
        ]
        description = self.random_sentence()
        return UDT(name, fields, description)

    def parameter(
        self,
    ) -> Parameter:
        """Generates a random Parameter.

        :return: A randomly generated Parameter.
        """
        name = self.random_name()
        storage_type = self.storage_type()
        default_value = (
            self.default_value()
            if storage_type.modifier is None
            else None
        )
        description = self.random_sentence()
        return Parameter(name, storage_type, default_value, description)

    def return_value(self) -> ReturnValue:
        """Generates a random ReturnValue.

        :return: A randomly generated ReturnValue.
        """
        storage_type = self.storage_type()
        description = self.random_sentence()
        return ReturnValue(storage_type, description)

    def function(self) -> Function:
        """Generates a random Function.

        :return: A randomly generated Function.
        """
        name = self.random_name()
        self.generated_function_names.append(name)
        num_params = random.randint(0, 5)
        parameters = [self.parameter() for _ in range(num_params)]
        return_value = self.return_value()
        description = self.random_sentence()
        return Function(name, parameters, return_value, description)

    def import_statement(self) -> Import:
        """Generates a random Import statement.

        :return: A randomly generated Import.
        """
        user = self.random_name()
        script = self.random_name()
        version = random.randint(1, 10)
        alias = self.random_name() if random.choice([True, False]) else None
        return Import(user, script, version, alias)

    def script(self) -> Script:
        """Generates a random Script.

        :return: A randomly generated Script.
        """
        name = self.random_name()
        num_imports = random.randint(0, 5)
        imports = [self.import_statement() for _ in range(num_imports)]
        num_udts = random.randint(0, 5)
        udts = [self.udt() for _ in range(num_udts)]
        num_functions = random.randint(1, 10)
        functions = [self.function() for _ in range(num_functions)]
        description = self.random_sentence()
        return Script(name, imports, udts, functions, description)

# Main execution
if __name__ == "__main__":
    generator = Generator()
    generated_script = generator.script()
    print(generated_script)
