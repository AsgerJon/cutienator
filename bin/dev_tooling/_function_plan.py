"""FunctionPlan is how one ritual of a class of Qt becomes one function
of its cute class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import keyword
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import RitualGenerator
from .class_tables import (
    BINARY_OPERATORS, IN_PLACE_OPERATORS, PYTHON_NUMBERS, UNARY_OPERATORS)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]


class FunctionPlan:
  """
  How one ritual of a class of Qt becomes one function of its cute
  class: the name the function has in Python, how each of its arguments
  looks there and what the ritual is handed for it, what it gives, the
  section of the class body it stands in, and the signatures it takes.
  'findFunction' works it out:

    functionPlan = FunctionPlan()
    functionPlan.setPlan(plan)    # one plan of 'RitualGenerator'
    functionPlan.setViewer(classGenerator)
    functionPlan.findFunction()   # the function, or why there is none

  What depends on other classes, as whether a class the function names
  has a cute class and how the body names it, is asked of the
  'ClassGenerator' writing the class, the viewer, and what the file
  then needs, the viewer is told. Which of the functions of one name
  keeps which call, and in which order they are stacked, depends on the
  others of that name, and the viewer decides it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _findSection(function: Record) -> str:
    """Gives the section of the class body a function stands in."""
    plan = function['plan']
    if function.get('operator') is not None:
      return 'Python API'
    if function['kind'] == 'constructor':
      return 'CONSTRUCTORS'
    if function['kind'] == 'static method':
      return 'STATIC METHODS'
    name = plan['name']
    if name.startswith('set') and name[3:4].isupper():
      return 'SETTERS'
    if 'const' in plan['words'] and function['gives']['kind'] != 'nothing':
      return 'GETTERS'
    return 'PUBLIC METHODS'

  @staticmethod
  def _createSignatures(function: Record) -> None:
    """
    Gives a function its signatures: the full call first decided, then
    one for each call that leaves out what Qt fills in, and one more
    for each place None is taken. A signature naming a late class is
    one of them as any other.
    """
    parameters = function['parameters']
    fewest = len(parameters)
    for parameter in reversed(parameters):
      if parameter['default'] is None:
        break
      fewest -= 1
    signatures = []  # type: List[Tuple[str, ...]]
    keys = []  # type: List[Tuple[str, ...]]
    for count in range(fewest, len(parameters) + 1):
      built = [((), ())]  # type: List[Tuple[Tuple, Tuple]]
      for parameter in parameters[:count]:
        #  The class of an enum has two names where Qt names its
        #  combinations apart, and a class of Qt may be written as
        #  'THIS'. What a signature takes goes by the class itself.
        entry = parameter['entry']
        entries = [(entry, parameter.get('key', entry))]
        if parameter['nullable']:
          entries.append(('NoneType', 'NoneType'))
        built = [
            ((*shown, text), (*known, key))
            for shown, known in built for text, key in entries
        ]
      signatures.extend(shown for shown, _ in built)
      keys.extend(known for _, known in built)
    function['signatures'] = signatures
    function['signatureKeys'] = keys

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __ritual_plan__ = None  # type: Optional[Record]
  __viewer__ = None  # type: Any

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getPlan(self) -> Record:
    """
    Gives the plan of the ritual, as 'RitualGenerator.getWritten' gives
    it.

    Provided by you, through 'setPlan'.

    Raises
    ------

    MissingVariable
      'setPlan' has not been called.
    """
    if self.__ritual_plan__ is None:
      raise MissingVariable(self, '__ritual_plan__', dict)
    return self.__ritual_plan__

  def getViewer(self) -> Any:
    """
    Gives the 'ClassGenerator' of the cute class the function is of.

    Provided by you, through 'setViewer'.

    Raises
    ------

    MissingVariable
      'setViewer' has not been called.
    """
    if self.__viewer__ is None:
      raise MissingVariable(self, '__viewer__', object)
    return self.__viewer__

  def getParts(self) -> Record:
    """
    Gives what the ritual is made of, as its plan has it: 'name', the
    name Qt gives the function, as 'resize' or 'operator+'; 'kind', as
    'method', 'static method', 'constructor', 'friend' or 'destructor';
    'declared', the function as Qt declares it; 'ritualName';
    'arguments', the names of its arguments; 'operator', whether it is
    an operator.
    """
    plan = self.getPlan()
    names = (*(argument['name'] for argument in plan['arguments']),)
    return dict(
        name=plan['name'], kind=plan['kind'], declared=plan['function'],
        ritualName=plan['ritualName'], arguments=names,
        operator=plan['name'].startswith('operator'))

  def getPythonName(self) -> Optional[str]:
    """
    Gives the name the function has in Python, whether or not it gets
    one: '__init__' for a constructor, else the name Qt gives it, with
    an underscore after a word of Python, as 'raise_'. None for a
    destructor, for an operator and for one of Qt's own inner workings,
    named 'qt_...': nothing stands in for those when they are left out.
    """
    plan = self.getPlan()
    kind, name = plan['kind'], plan['name']
    if kind == 'destructor':
      return None
    if name.startswith('operator') or name.startswith('qt_'):
      return None
    if kind == 'constructor':
      return '__init__'
    return '%s_' % name if keyword.iskeyword(name) else name

  def findFunction(self) -> Any:
    """
    Works out the function of the ritual.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the ritual gets no function. Else the
      function, as 'ClassGenerator.getFunctions' gives it, before the
      viewer weighs it against the other functions of its name:
      'pythonName', 'plan', 'kind', 'parameters', 'gives', 'operator',
      'selfPassed', 'inPlace', 'section', 'signatures' and
      'signatureKeys'.
    """
    function = self._planFunction()
    if isinstance(function, str):
      return function
    function['section'] = self._findSection(function)
    self._createSignatures(function)
    return function

  def _planFunction(self) -> Any:
    """
    Works out the function of one ritual: its name, its arguments and
    what it gives, in Python.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the ritual gets no function. Else the
      function, as 'ClassGenerator.getFunctions' gives it, with its
      section and signatures still to be decided.
    """
    viewer, plan = self.getViewer(), self.getPlan()
    kind, name = plan['kind'], plan['name']
    if kind == 'destructor':
      if viewer.getDeleteRitual() is None:
        return 'the destructor: Python never removes a C++ %s' % (
            viewer.getClassName(),)
      infoSpec = """the destructor: Python removes its C++ %s by it, and
      has no other use for it"""
      return ' '.join((infoSpec % viewer.getClassName()).split())
    operator = None  # type: Optional[Record]
    if name.startswith('operator'):
      operator = self._planOperator()
      if isinstance(operator, str):
        return operator
    if name.startswith('qt_'):
      return "one of Qt's own inner workings"
    static = kind != 'method'
    parameters = []  # type: List[Record]
    arguments = [*plan['arguments']]
    selfPassed = ''
    if operator is not None and operator['selfIndex'] is not None:
      #  Qt writes the operator as a function of no object, and hands it
      #  the object as an argument. In Python that argument is 'self'.
      taken = dict(arguments.pop(operator['selfIndex']), name='self')
      own = self._planParameter(taken, True)
      if isinstance(own, str):
        return own
      selfPassed = own['passed']
    while arguments:
      argument = arguments.pop(0)
      passing = argument['passing']
      following = arguments[0]['passing']['kind'] if arguments else ''
      if passing['kind'] == 'number address':
        if following == 'texts address':
          #  The texts a program was started with, and how many they
          #  are, are one argument in Python: a list of them.
          texts = arguments.pop(0)
          helper = 'CuteMixin' if static and kind != 'constructor' else (
              'self')
          infoSpec = """The texts the program was started with, as
          'sys.argv'. Passed on as Qt takes them: how many they are,
          and where the first one is."""
          parameters.append(dict(
              name=texts['name'], kind='texts', late=False,
              nullable=False, default=None, entry='list',
              annotation='list',
              passed='*%s._startTextsOf(%s)' % (helper, texts['name']),
              words=' '.join(infoSpec.split()),
          ))
          continue
      parameter = self._planParameter(
          argument, static and kind != 'constructor')
      if isinstance(parameter, str):
        return parameter
      parameter['argument'] = argument
      parameters.append(parameter)
    gives = None  # type: Optional[Record]
    if kind != 'constructor':
      gives = self._planGiving(static)
      if isinstance(gives, str):
        return gives
    pythonName = '__init__' if kind == 'constructor' else name
    if operator is not None:
      pythonName = operator['pythonName']
    if keyword.iskeyword(pythonName):
      pythonName = '%s_' % pythonName
    #  What Qt fills in, from the last argument backwards for as long as
    #  it can be said in Python.
    for parameter in reversed(parameters):
      argument = parameter.get('argument')
      if argument is None or argument['default'] is None:
        break
      default = viewer.getDefaultValue(argument, parameter).findPython()
      if default is None:
        break
      parameter['default'] = default
    for parameter in parameters:
      #  C++ lets nothing be given wherever an address is taken.
      if parameter['kind'] in ('address', 'chars'):
        parameter['nullable'] = True
    return dict(
        pythonName=pythonName, plan=plan, kind=kind,
        parameters=parameters, gives=gives, operator=operator,
        selfPassed=selfPassed, inPlace=plan.get('inPlace', False),
    )

  def _planParameter(self, argument: Record, static: bool) -> Any:
    """
    Says how one argument of a Qt function looks in Python.

    Parameters
    ----------

    argument : Record
      The argument as the plan of the ritual has it.

    static : bool
      Whether the function is called on no object, so that it has no
      'self' to reach a helper through.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the function cannot be written for
      this argument. Else a record: 'name', 'kind', 'entry' (what
      stands for it in a signature), 'annotation', 'passed' (what the
      ritual is handed), 'words' (what its docstring says) and 'late'.
    """
    viewer = self.getViewer()
    passing, name = argument['passing'], argument['name']
    if keyword.iskeyword(name):
      name = '%s_' % name
    kind = passing['kind']
    helper = 'CuteMixin' if static else 'self'
    record = dict(
        name=name, kind=kind, late=False, nullable=False, default=None,
    )
    if kind == 'number':
      number = passing['className']
      if number == 'char':
        return 'takes a single letter as C has it'
      annotation = PYTHON_NUMBERS.get(number, 'int')
      return dict(
          record, entry=annotation, annotation=annotation, passed=name,
          words='Passed on as it is.',
      )
    if kind in ('text', 'view'):
      words = 'Passed on as it is: a QString is made of it for the call.'
      return dict(
          record, kind='text', entry='str', annotation='str',
          passed=name, words=words,
      )
    if kind == 'chars':
      return dict(
          record, entry='str', annotation='str',
          passed='%s._bytesOf(%s)' % (helper, name),
          words='Passed on as the bytes of the text.',
      )
    if kind in ('enum', 'flags'):
      plain = argument['plain']
      if kind == 'flags':
        enumName = passing['className'][len('QFlags<'):-1]
      else:
        enumName = plain
      found = viewer.getCuteName(enumName).findEnumEntry(kind == 'flags')
      if found is None:
        infoSpec = """names the enum '%s', whose class cannot be named
        here"""
        return ' '.join((infoSpec % enumName).split())
      if found['owner']:
        viewer._note('classes', found['owner'])
      return dict(
          record, entry=found['entry'], annotation=found['shown'],
          passed='%s.value' % name, words='Passed on as its number.',
          enumGenerator=found['generator'], key='enum %s' % enumName,
      )
    if kind == 'map':
      found = viewer._findMap(passing['mapped'])
      if isinstance(found, str):
        return 'names %s' % found
      infoSpec = """Passed on as a map of Qt: Qt reads the C++ map,
      which stays Python's own. A dict of Python is made into one
      first, and refused when a key or a value does not fit."""
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed='%s._valueOf(%s)' % (helper, name),
          words=' '.join(infoSpec.split()), late=found['late'],
          lateName=found['lateName'], className=found['className'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='map %s' % found['entry'],
      )
    if kind == 'list':
      found = viewer._findList(passing['listed'])
      if isinstance(found, str):
        return 'names %s' % found
      infoSpec = """Passed on as a list of Qt: Qt reads the C++ list,
      which stays Python's own. A list or tuple of Python is made into
      one first, and refused when an element does not fit."""
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed='%s._valueOf(%s)' % (helper, name),
          words=' '.join(infoSpec.split()), late=found['late'],
          lateName=found['lateName'], className=found['className'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='list %s' % found['className'],
      )
    if kind in ('address', 'value'):
      if kind == 'address':
        pointed = argument['plain'][:-2]
        if pointed.startswith('const '):
          pointed = pointed[6:]
      else:
        pointed = passing['className']
      found = viewer.getCuteName(pointed).findClassEntry()
      if isinstance(found, str):
        return found
      if found is None:
        return "names '%s', which has no cute class yet" % pointed
      #  A class other classes are built on beside another is named, so
      #  that the address is that of its part of the object.
      isPart = viewer._isCute(pointed) and (
          viewer._keyOf(pointed) in viewer._getPartNames())
      part = ", '%s'" % pointed if isPart else ''
      if kind == 'address':
        passed = '%s._addressOf(%s%s)' % (helper, name, part)
        words = 'Passed on as the address of its C++ object.'
      else:
        passed = '%s._valueOf(%s%s)' % (helper, name, part)
        infoSpec = """Passed on as a value: Qt reads the C++ %s, which
        stays Python's own."""
        words = ' '.join((infoSpec % pointed).split())
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed=passed, words=words, late=found['late'],
          className=pointed, bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='class %s' % pointed,
      )
    if kind == 'number address':
      return 'takes a number to change where it is'
    return 'takes a type Python has no way to hand over yet'

  def _planGiving(self, static: bool) -> Any:
    """
    Says how what a Qt function gives looks in Python.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the function cannot be written for
      what it gives. Else a record: 'kind', 'annotation', 'words'
      (what the docstring says under 'Returns', or ''), and for a class
      'name' and 'late'.
    """
    viewer, plan = self.getViewer(), self.getPlan()
    giving = plan['giving']
    kind = giving['kind']
    if kind == 'nothing':
      return dict(kind=kind, annotation='None', words='')
    if kind == 'number':
      annotation = PYTHON_NUMBERS.get(giving['className'], 'int')
      if giving['className'] == 'char':
        return 'gives a single letter as C has it'
      return dict(kind=kind, annotation=annotation, words='')
    if kind in ('text', 'view'):
      words = 'The text Qt gave back.'
      return dict(kind='text', annotation='str', words=words)
    if kind == 'chars':
      viewer._note('typing', 'Optional')
      words = 'The text Qt gave back. None when Qt gave back no text.'
      return dict(kind=kind, annotation='Optional[str]', words=words)
    if kind in ('enum', 'flags'):
      written = RitualGenerator._stripReadOnly(giving['written'])
      tables = viewer.getRitualGenerator()._getTypeTables()
      plain = viewer.getRitualGenerator()._followAliases(written)
      if kind == 'flags':
        enumName = giving['className'][len('QFlags<'):-1]
      else:
        enumName = plain if plain in tables['enums'] else written
      found = viewer.getCuteName(enumName).findEnumEntry(kind == 'flags')
      if found is None:
        infoSpec = """gives the enum '%s', whose class cannot be named
        here"""
        return ' '.join((infoSpec % enumName).split())
      if found['owner']:
        viewer._note('classes', found['owner'])
      if kind == 'enum':
        infoSpec = """The member standing for the number Qt gave back.
        For a number Qt gives no name it is the member without a name
        that '%s(number)' gives."""
        words = ' '.join((infoSpec % found['shown']).split())
      else:
        words = 'The value standing for the combination Qt gave back.'
      maker = found['entry']
      if found.get('own'):
        #  An enum of this class, and the name Qt has for the
        #  combinations of a flags enum of it, are bound in the body of
        #  the class alone, so a function reaches them through the class.
        maker = '%s.%s' % (viewer.getDottedName(), maker)
      return dict(
          kind=kind, annotation=found['shown'], words=words,
          entry=found['entry'], maker=maker,
      )
    if kind == 'map':
      found = viewer._findMap(giving['mapped'])
      if isinstance(found, str):
        return 'gives %s' % found
      infoSpec = """A new cute map around the copy Qt gave back. Python
      owns it."""
      return dict(
          kind=kind, annotation=found['name'], name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    if kind == 'list':
      found = viewer._findList(giving['listed'])
      if isinstance(found, str):
        return 'gives %s' % found
      infoSpec = """A new cute list around the copy Qt gave back. Python
      owns it."""
      return dict(
          kind=kind, annotation=found['name'], name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    if kind in ('address', 'value'):
      if kind == 'address':
        pointed = viewer.getRitualGenerator()._followAliases(
            giving['written'])
        pointed = pointed[:-2] if pointed.endswith(' *') else pointed
        if pointed.startswith('const '):
          pointed = pointed[6:]
        pointed = viewer.getRitualGenerator()._followAliases(pointed)
      else:
        pointed = giving['className']
      found = viewer.getCuteName(pointed).findClassEntry()
      if isinstance(found, str):
        return found.replace('names', 'gives', 1)
      if found is None:
        return "gives '%s', which has no cute class yet" % pointed
      if kind == 'value' and not viewer._canBeOwned(pointed):
        infoSpec = """gives a value of '%s', which Python cannot own: no
        ritual removes one"""
        return ' '.join((infoSpec % pointed).split())
      if kind == 'address':
        viewer._note('typing', 'Optional')
        annotation = 'Optional[%s]' % found['name']
        infoSpec = """The cute object standing for what Qt gave back.
        None when Qt gave back no object."""
      else:
        annotation = found['name']
        infoSpec = """A new cute %s around the copy Qt gave back. Python
        owns it."""
        infoSpec = infoSpec % pointed
      return dict(
          kind=kind, annotation=annotation, name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    return 'gives a type Python has no way to take yet'

  def _planOperator(self) -> Any:
    """
    Says which name Python has for an operator of Qt, and which of its
    arguments is the object in Python.

    Python has solved operators already, and the cute class goes by
    it: 'a + b' asks 'a.__add__(b)', and when that gives
    'NotImplemented' it asks 'b.__radd__(a)'. An operator Qt writes
    with 'friend' inside the class is a function of no object, taking
    both sides as arguments. Where the class stands first it is the
    plain name, and where it stands second the name Python asks the
    right side for.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when Python has no name for the operator.
      Else 'pythonName': the name, as '__add__'; and 'selfIndex': the
      place of the argument that is 'self' in Python, or None for an
      operator Qt writes as a function of the object.
    """
    viewer, plan = self.getViewer(), self.getPlan()
    kind, symbol = plan['kind'], plan['name'][len('operator'):].strip()
    count, className = len(plan['arguments']), viewer.getClassName()
    binary, unary = BINARY_OPERATORS, UNARY_OPERATORS
    noName = 'an operator Python has no name for'
    if kind == 'friend':
      own = [
          argument['passing'].get('kind') == 'value'
          and argument['passing'].get('className') == className
          for argument in plan['arguments']
      ]
      if count == 1 and own[0] and symbol in unary:
        return dict(pythonName=unary[symbol], selfIndex=0)
      if count != 2 or symbol not in binary:
        return noName
      if own[0]:
        return dict(pythonName=binary[symbol][0], selfIndex=0)
      if own[1]:
        return dict(pythonName=binary[symbol][1], selfIndex=1)
      return 'an operator between other classes, written inside this one'
    if kind != 'method':
      return noName
    if symbol == '=':
      return 'assignment: Python binds a name and has no operator for it'
    if symbol in IN_PLACE_OPERATORS and count == 1:
      if not plan.get('inPlace', False):
        return noName
      name = IN_PLACE_OPERATORS[symbol]
      return dict(pythonName=name, selfIndex=None)
    if count == 1 and symbol in binary:
      return dict(pythonName=binary[symbol][0], selfIndex=None)
    if count == 0 and symbol in unary:
      return dict(pythonName=unary[symbol], selfIndex=None)
    if symbol == '[]' and count == 1:
      return dict(pythonName='__getitem__', selfIndex=None)
    if symbol == '()':
      return dict(pythonName='__call__', selfIndex=None)
    if symbol == 'bool' and count == 0:
      return dict(pythonName='__bool__', selfIndex=None)
    return noName

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setPlan(self, plan: Record) -> None:
    """
    Sets the plan of the ritual, as 'RitualGenerator.getWritten' gives
    it.

    Raises
    ------

    TypeException
      The plan is not a dict.
    """
    if not isinstance(plan, dict):
      raise TypeException('plan', plan, dict)
    self.__ritual_plan__ = plan

  def setViewer(self, viewer: Any) -> None:
    """Sets the 'ClassGenerator' of the cute class the function is of."""
    self.__viewer__ = viewer
