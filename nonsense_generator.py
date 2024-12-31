import random
import string
from typing import List, Optional, Union, Dict

# Generate some randome Nonsense pine(ish), someewhat done..
# does not match types to values quite yet..
# Example output (mildly formatted):

"""
// @description lao jcej sbctml
import inqejfc/vlbdykj/2 as uogqncx
// @type syb fpoaob oaj nuxa
type bprdtmj
  float field1 = 19.21155548403434 // @field lpsyz ijt vyqj
  matrix<string> field2 // @field umibzf nstn tcwnuq
  matrix<color> field3 // @field mfs zfnzesy nfvc wdg
// @type iqatsv kbik nzqo zcwwy
type pycu
  array<color> field1 // @field xqnm qmc gftref ksu tfuuh gkb
  array<string> field2 // @field vxkw pcs kbca skduco zmyuwuf
  float field3 = na // @field dax ujf oexgkg kyxtpmh
// @type tlbwb xdaztdf nnjopm stfy dac
type mwunyeq
  color field1 = "djqagl umclv oshchgc uikf riyaptc rzabpq gadtd" // @field kdrjxo ywmxy otjsz
  bool field2 = 20.707827775405885 // @field gsxngsk peghgpa amwzk wcjfw flhjado icl
// @type xcvnmra ejzuxsz engif lackkfg aziyf urxi wcbujr
type ghwkk
  matrix<float> field1 // @field vbsvjc bwwwcn auzalbp
  matrix<bool> field2 // @field euw tuz hheu ihj cfckwf cgse hmt
var matrix<int> jqxndb = "cxgxkr opmh zkg noras" // fzfddlr nxovu vguuhu
varip int vryx // uwgvfpv hkh bsfj
var float shof = 96.46662304390122 // ufeb nrcj dqx nqf rup stltod utoz
varip matrix<int> ods // adnuws dpmsu xxbudu jyzc
varip matrix<bool> kxtfncn // xmprxx adf uenc jfkkxg govnzng vcw wgohmx
int shsy = True // fmskg uicjer yiq myrihc ymvbr
array<color> tbpvy = False // nmmza bfxa kavzg pwnwge pgcqln tqof azn
yoeim(array<bool> presdjr, array<bool> vmzq, array<bool> bdfhkj, color rkar = 48.5094107480144) => array<bool>
    ta.rsi(na)
    for zws = 1 to 4
        color vpkhrhq = na // uiiu ynjnxqo lcooto rbz ivjmm
        var array<string> mpfwjb = na // qumly kieny acbj azi ensojag

    ta.ema("vmm xjc dtjdhj", "dfamjkf lby ifh abxwzm bftjywi", 72.37393217201567)
    ta.macd(17, 32)
    if shsy >= vryx
        ta.rsi(na, 91)
        var array<color> dkcw = True // nwgz pqikgex ypumopp bcqmo
    else
        yoeim()
        varip matrix<color> ofdrpz // zfwjao mcan jenqrhc
    ta.rsi(24.195863006282625, 13)
    array.new_bool()
    if tbpvy >= mpfwjb
        ta.macd(35, "oozpvo luikps yosjs myqkm nod zwkvrk avcc")
    array.new_bool()

array<float> vrrico = na // xucrn jvezw xawix wgykory djnmkc
while na <= vryx
    yoeim(89, na, na)
    ta.rsi()
    yoeim()

var int eutz = 70.09686797968986 // yvoyg rhoxvsj vpqpn vlfmm
array<float> ajvsz = "vgbm jbdx hmekk epzd yikdnu hjm" // spnrv kozhz rjmkms fgmwp aquq liguzt
ta.sma()
ta.rsi()
var matrix<float> zlk = na // zzxdnd rofbt eraiw mnpfwy
ta.sma(na)
while dkcw >= shof
    matrix<bool> jwfjsp = na // fdtplpt lvxotq daakshq kmkxabv dbfkth
    yoeim(na)

ta.rsi(34.360012416378495)
for qeme = 4 to 9
    ta.rsi(True, 89.70521924407251)

for zedaupo = 5 to 9
    varip array<int> ondh // ydgocib gri buryc

if vrrico < mpfwjb
    matrix<float> ztha = na // mmiqj oxjlicl lmeistb are
    ta.ema(13.665086899159572, "ptrtp ivz egyw znyur ukgljjv")
else
    var array<string> elc = False // izeehv wymshdi gemp fkrib dvsoqc fni asi
    var string wvl = 18.264199572403108 // jdv ycsszs oiwhwi
    varip matrix<string> jav // kyg cjuxbe xldwyyv xwohad
array<int> teabx = 25 // dfoc uigwp kbkepu lbdfjk jgjz yzfdig
var int vzqrnh = 34 // bvsk tnurokp oeazq

"""

# --- Constants and Data Structures ---
KEYWORDS = ["if", "else", "for", "while", "switch"]
OPERATORS = ["+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "%=", ":="]
BUILT_IN_FUNCTIONS = ["ta.sma", "ta.ema", "ta.rsi", "ta.macd"]
CONTROL_STRUCTURES = ["if", "for", "while", "switch"]
INDENTATION = "    "  # 4 spaces for indentation


class Import:
    """Represents an import statement with user, script, version, and optional alias."""

    def __init__(self, user: str, script: str, version: int, alias: Optional[str] = None):
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
        desc_str = f" // @field {self.description}" if self.description else ""
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
        self.annotation: Optional[Annotation] = Annotation("param", description) if description else None

    def __str__(self) -> str:
        """Returns the parameter definition as a string.

        :return: The formatted parameter definition.
        """
        if self.storage_type:
            if self.storage_type.modifier in ["matrix", "array"]:
                return f"{self.storage_type} {self.name}"
            dv = f" = {self.default_value}" if self.default_value else ""
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
        self.annotation: Optional[Annotation] = Annotation("type", description) if description else None

    def __str__(self) -> str:
        """Returns the UDT definition as a string.

        :return: The formatted UDT definition.
        """
        type_desc = f"// @type {self.description}\n" if self.description else ""
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
        body: Optional[List[str]] = None,
        description: Optional[str] = None,
    ):
        """Initializes a Function object.

        :param name: The name of the function.
        :param parameters: The list of Parameters for the function.
        :param return_value: The ReturnValue of the function.
        :param body: The body of the function, a list of code lines.
        :param description: The description of the function, if any.
        """
        self.name: str = name
        self.parameters: List[Parameter] = parameters
        self.return_value: ReturnValue = return_value
        self.body: Optional[List[str]] = body
        self.description: Optional[str] = description
        self.annotations: List[Annotation] = [p.annotation for p in parameters if p.annotation]

    def __str__(self) -> str:
        """Returns the function definition as a string.

        :return: The formatted function definition.
        """
        param_str = ", ".join(str(p) for p in self.parameters)
        body_str = ""
        if self.body:
            indented_body = [f"{INDENTATION}{line}" for line in self.body]  # Indent each line
            body_str = "\n" + "\n".join(indented_body) + "\n"

        return f"{self.name}({param_str}) => {self.return_value}{body_str}"


class Variable:
    """Represents a variable declaration."""

    def __init__(
        self,
        name: str,
        storage_type: StorageType,
        value: Optional[str] = None,
        is_var: bool = False,
        is_varip: bool = False,
        description: Optional[str] = None,
    ):
        """Initializes a Variable object.

        :param name: The name of the variable.
        :param storage_type: The StorageType of the variable.
        :param value: The initial value of the variable, if any.
        :param is_var: True if the variable is declared with 'var', False otherwise.
        :param is_varip: True if the variable is declared with 'varip', False otherwise.
        :param description: The description of the variable, if any.
        """
        self.name: str = name
        self.storage_type: StorageType = storage_type
        self.value: Optional[str] = value
        self.is_var: bool = is_var
        self.is_varip: bool = is_varip
        self.description: Optional[str] = description

    def __str__(self) -> str:
        """Returns the variable declaration as a string.

        :return: The formatted variable declaration.
        """
        var_prefix = ""
        if self.is_var:
            var_prefix = "var "
        elif self.is_varip:
            var_prefix = "varip "
        value_str = f" = {self.value}" if self.value else ""
        desc_str = f" // {self.description}" if self.description else ""
        return f"{var_prefix}{self.storage_type} {self.name}{value_str}{desc_str}"


class Loop:
    """Represents a loop (for or while) structure."""

    def __init__(
        self,
        loop_type: str,
        condition: Optional[str] = None,
        body: Optional[List[str]] = None,
    ):
        """Initializes a Loop object.

        :param loop_type: The type of loop ("for" or "while").
        :param condition: The loop condition (for while loops).
        :param body: The body of the loop, a list of code lines.
        """
        self.loop_type: str = loop_type
        self.condition: Optional[str] = condition
        self.body: Optional[List[str]] = body

    def __str__(self) -> str:
        """Returns the loop structure as a string.

        :return: The formatted loop structure.
        """
        body_str = ""
        if self.body:
            indented_body = [f"{INDENTATION}{line}" for line in self.body]
            body_str = "\n" + "\n".join(indented_body) + "\n"

        if self.loop_type == "for":
            return f"for {self.condition}{body_str}"
        elif self.loop_type == "while":
            return f"while {self.condition}{body_str}"
        else:
            return ""


class Conditional:
    """Represents an if-else statement."""

    def __init__(
        self,
        condition: str,
        if_body: List[str],
        else_body: Optional[List[str]] = None,
    ):
        """Initializes a Conditional object.

        :param condition: The condition for the if statement.
        :param if_body: The body of the if block, a list of code lines.
        :param else_body: The body of the else block, if any, a list of code lines.
        """
        self.condition: str = condition
        self.if_body: List[str] = if_body
        self.else_body: Optional[List[str]] = else_body

    def __str__(self) -> str:
        """Returns the if-else statement as a string.

        :return: The formatted if-else statement.
        """
        if_body_str = "\n".join([f"{INDENTATION}{line}" for line in self.if_body])
        else_body_str = ""
        if self.else_body:
            else_body_str = "\n".join([f"{INDENTATION}{line}" for line in self.else_body])
            return f"if {self.condition}\n{if_body_str}\nelse\n{else_body_str}"
        return f"if {self.condition}\n{if_body_str}"


class Script:
    """Represents a complete script."""

    def __init__(
        self,
        name: str,
        imports: List[Import],
        udts: List[UDT],
        functions: List[Function],
        variables: List[Variable],
        body: List[str],
        description: Optional[str] = None,
    ):
        """Initializes a Script object.

        :param name: The name of the script.
        :param imports: The list of Imports used in the script.
        :param udts: The list of UDTs defined in the script.
        :param functions: The list of Functions defined in the script.
        :param body: The main body of the script, a list of code lines.
        :param description: The description of the script, if any.
        """
        self.name: str = name
        self.imports: List[Import] = imports
        self.udts: List[UDT] = udts
        self.functions: List[Function] = functions
        self.variables: List[Variable] = variables
        self.body: List[str] = body
        self.description: Optional[str] = description
        self.annotation: Optional[Annotation] = Annotation("description", description) if description else None

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
        script_code_content += "\n".join([str(variable) for variable in self.variables])
        script_code_content += "\n"
        script_code_content += "\n".join([str(func) for func in self.functions])
        script_code_content += "\n"
        script_code_content += "\n".join(self.body)
        script_code_content += "\n"
        return script_code_content


class Generator:
    """Generates random script components for testing."""

    def __init__(self):
        """Initializes the Generator with empty lists for tracking generated components."""
        self.generated_udt_names: List[str] = []
        self.generated_function_names: List[str] = []
        self.generated_variable_names: List[str] = []

    @staticmethod
    def random_word() -> str:
        """Generates a random word.

        :return: A random word.
        """
        return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 7)))

    def random_sentence(self, min_words: int = 3, max_words: int = 7) -> str:
        """Generates a random sentence.

        :param min_words: The minimum number of words in the sentence.
        :param max_words: The maximum number of words in the sentence.
        :return: A random sentence.
        """
        return " ".join(self.random_word() for _ in range(random.randint(min_words, max_words)))

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
        default_value = self.default_value() if storage_type.modifier is None else None
        description = self.random_sentence()
        return Field(name, storage_type, default_value, description)

    def udt(self) -> UDT:
        """Generates a random UDT.

        :return: A randomly generated UDT.
        """
        name = self.random_name()
        self.generated_udt_names.append(name)
        num_fields = random.randint(1, 5)
        fields = [self.udt_field(name, i) for i in range(1, num_fields + 1)]
        description = self.random_sentence()
        return UDT(name, fields, description)

    def parameter(self) -> Parameter:
        """Generates a random Parameter.

        :return: A randomly generated Parameter.
        """
        name = self.random_name()
        storage_type = self.storage_type()
        default_value = self.default_value() if storage_type.modifier is None else None
        description = self.random_sentence()
        return Parameter(name, storage_type, default_value, description)

    def return_value(self) -> ReturnValue:
        """Generates a random ReturnValue.

        :return: A randomly generated ReturnValue.
        """
        storage_type = self.storage_type()
        description = self.random_sentence()
        return ReturnValue(storage_type, description)

    def generate_function_body(self, return_storage_type: Optional[StorageType]) -> List[str]:
        """Generates a random function body.

        :param return_storage_type: The StorageType of the function's return value.
        :return: A list of code lines representing the function body.
        """
        body: List[str] = []
        num_lines = random.randint(1, 10)

        for _ in range(num_lines):
            line_type = random.choice(["variable", "control_structure", "function_call", "return"])

            if line_type == "variable":
                body.append(str(self.variable()))
            elif line_type == "control_structure":
                body.extend(str(self.control_structure()).split("\n"))  # Split into lines
            elif line_type == "function_call":
                body.append(self.generate_function_call())
            elif line_type == "return" and return_storage_type:
                if return_storage_type.modifier in ["array", "matrix"]:
                    body.append(f"{self.generate_empty_structure(return_storage_type)}")
                else:
                    body.append(f"{self.default_value()}")

        # Ensure the function returns a value if it's supposed to
        if return_storage_type and not any(line.startswith("return") for line in body):
            if return_storage_type.modifier in ["array", "matrix"]:
                body.append(f"{self.generate_empty_structure(return_storage_type)}")
            else:
                body.append(f"{self.default_value()}")

        return body

    def generate_empty_structure(self, storage_type: StorageType) -> str:
        """Generates an empty array or matrix based on the given storage type.

        :param storage_type: The StorageType of the structure to generate.
        :return: A string representing an empty array or matrix.
        """
        if storage_type.modifier == "array":
            return f"array.new_{storage_type.base_type}()"
        elif storage_type.modifier == "matrix":
            rows = random.randint(1, 5)
            cols = random.randint(1, 5)
            return f"matrix.new_{storage_type.base_type}({rows}, {cols})"
        else:
            return ""

    def function(self) -> Function:
        """Generates a random Function.

        :return: A randomly generated Function.
        """
        name = self.random_name()
        self.generated_function_names.append(name)

        num_params = random.randint(0, 5)
        parameters = [self.parameter() for _ in range(num_params)]

        return_value = self.return_value()
        body = self.generate_function_body(return_value.storage_type)

        description = self.random_sentence()
        return Function(name, parameters, return_value, body, description)

    def generate_function_call(self) -> str:
        """Generates a random function call.

        :return: A string representing a function call.
        """
        function_name = random.choice(self.generated_function_names + BUILT_IN_FUNCTIONS)
        num_args = random.randint(0, 3)  # Limit to 3 arguments for simplicity
        args = [self.default_value() for _ in range(num_args)]
        return f"{function_name}({', '.join(args)})"

    def variable(
        self,
    ) -> Variable:
        """Generates a random Variable.

        :return: A randomly generated Variable.
        """
        name = self.random_name()
        self.generated_variable_names.append(name)

        storage_type = self.storage_type()
        is_var = random.choice([True, False])
        is_varip = False if is_var else random.choice([True, False])
        value = self.default_value() if not is_varip else None
        description = self.random_sentence()
        return Variable(name, storage_type, value, is_var, is_varip, description)

    def generate_condition(self) -> str:
        """Generates a random condition for control structures.

        :return: A string representing a condition.
        """
        left_operand = random.choice(self.generated_variable_names + [self.default_value()])
        operator = random.choice(["<", ">", "<=", ">=", "==", "!="])
        right_operand = random.choice(self.generated_variable_names + [self.default_value()])
        return f"{left_operand} {operator} {right_operand}"

    def generate_for_loop(self) -> Loop:
        """Generates a random for loop.

        :return: A Loop object representing a for loop.
        """
        counter_variable = self.random_name()
        start_value = random.randint(0, 5)
        end_value = random.randint(start_value + 1, 10)
        condition = f"{counter_variable} = {start_value} to {end_value}"
        body = [str(self.variable()) if random.choice([True, False]) else self.generate_function_call() for _ in range(random.randint(1, 3))]  # Simple body for the loop
        return Loop("for", condition, body)

    def generate_while_loop(self) -> Loop:
        """Generates a random while loop.

        :return: A Loop object representing a while loop.
        """
        condition = self.generate_condition()
        body = [str(self.variable()) if random.choice([True, False]) else self.generate_function_call() for _ in range(random.randint(1, 3))]  # Simple body for the loop
        return Loop("while", condition, body)

    def generate_if_statement(self) -> Conditional:
        """Generates a random if-else statement.

        :return: A Conditional object representing an if-else statement.
        """
        condition = self.generate_condition()
        if_body = [str(self.variable()) if random.choice([True, False]) else self.generate_function_call() for _ in range(random.randint(1, 3))]  # Simple body for the if block
        else_body = [str(self.variable()) if random.choice([True, False]) else self.generate_function_call() for _ in range(random.randint(1, 3))] if random.choice([True, False]) else None  # Optional else block
        return Conditional(condition, if_body, else_body)

    def control_structure(self) -> Union[Loop, Conditional]:
        """Generates a random control structure (loop or if-else).

        :return: A Loop or Conditional object.
        """
        structure_type = random.choice(CONTROL_STRUCTURES)

        if structure_type == "for":
            return self.generate_for_loop()
        elif structure_type == "while":
            return self.generate_while_loop()
        else:
            return self.generate_if_statement()

        # TODO: switch (not implemented)

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

        # Generate imports
        num_imports = random.randint(0, 5)
        imports = [self.import_statement() for _ in range(num_imports)]

        # Generate UDTs
        num_udts = random.randint(0, 5)
        udts = [self.udt() for _ in range(num_udts)]

        # Generate variables
        num_variables = random.randint(0, 10)
        variables = [self.variable() for _ in range(num_variables)]

        # Generate functions
        num_functions = random.randint(1, 10)
        functions = [self.function() for _ in range(num_functions)]

        # Generate the main body of the script
        body: List[str] = []
        num_body_lines = random.randint(0, 20)
        for _ in range(num_body_lines):
            line_type = random.choice(["variable", "control_structure", "function_call"])
            if line_type == "variable":
                body.append(str(self.variable()))
            elif line_type == "control_structure":
                body.extend(str(self.control_structure()).split("\n"))
            elif line_type == "function_call":
                body.append(self.generate_function_call())

        description = self.random_sentence()
        return Script(name, imports, udts, functions, variables, body, description)


# Main execution
if __name__ == "__main__":
    generator = Generator()
    generated_script = generator.script()
    print(generated_script)
