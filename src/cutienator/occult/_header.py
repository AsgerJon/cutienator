"""Header reads what one Qt class declares, by way of the compiler."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import subprocess
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import Build, Declaration

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Declarations = Tuple[Declaration, ...]
  Member = Tuple[str, Dict[str, Any]]


class Header:
  """
  Reads what one Qt class declares, and gives one 'Declaration' per
  function. It does not read the header itself: it has the compiler read
  it and write down what it found.

    header = Header()
    header.setClassName('QObject')
    for declaration in header.getDeclarations():
      print(declaration)   # void QObject::setParent(QObject *parent)

  Terms
  -----

  - A header is one of Qt's text files saying what a class has, as
    '/usr/include/qt6/QtCore/qobject.h'.
  - The compiler here is 'clang++', the one that also builds the
    rituals. It can write out what it read, as JSON.

  You provide
  -----------

  - 'setClassName': the Qt class to read, as 'QObject'. Required.

  Found for you
  -------------

  - 'getQtModule': the part of Qt the class belongs to, as 'QtCore'.
  - 'getCommand': the 'clang++' command that does the reading.
  - 'getDeclarations': the declarations themselves.
  - 'getParents': the classes this class is built on.
  - 'getSignalNames', 'getSlotNames', 'getPropertyNames': what Qt's own
    summary of the header says the class has.
  - 'getTypes': every C++ type the functions take or give back.
  - 'getRecords', 'getClassRecord', 'getMembers', 'getSummaryRecord':
    everything that was read, untouched.

  What to expect
  --------------

  - The compiler runs once, at the first 'getDeclarations', which takes
    a few seconds. The answer is kept; a later call costs nothing.
  - Every function the class itself declares is given: public,
    protected and private, templates included. Functions the class
    inherits from a parent class are not; read the parent for those.
  - Whether a function is a signal or a slot is not in what the
    compiler reports. That, and the properties of the class, come from
    the summary of each header that Qt installs itself.
  - Nothing that is read is thrown away. 'getRecords', 'getClassRecord',
    'getMembers' and 'getSummaryRecord' give it all, untouched.
  - Two things are in a header and not in what is read. Comments: the
    compiler does not report them. And a Qt macro as it is written: the
    compiler reports what the macro stands for.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def findQtModule(className: str) -> str:
    """
    Gives the part of Qt a class belongs to, as 'QtCore' for 'QObject'.

    Found by looking through Qt's header folder for the one part
    holding a header named exactly as the class.

    Raises
    ------

    LookupError
      No part of Qt has a header of that name, so Qt has no such class;
      or more than one has, which is not expected to happen.
    """
    folder = Build.getQtHeaderFolder()
    found = [
        module for module in sorted(os.listdir(folder))
        if os.path.isfile(os.path.join(folder, module, className))
    ]
    if len(found) != 1:
      infoSpec = """Expected exactly one part of Qt to have a header named
      '%s' in '%s', but found: %s."""
      listed = ', '.join(found) or 'none'
      info = infoSpec % (className, folder, listed)
      raise LookupError(' '.join(info.split()))
    return found[0]

  @staticmethod
  def _splitFunctionType(functionType: str) -> Tuple[str, bool]:
    """
    Takes apart the type the compiler reports for a function.

    Parameters
    ----------

    functionType : str
      As 'QObject *() const': what it gives, what it takes between
      brackets, and then 'const' when it leaves its object unchanged.

    Returns
    -------

    Tuple[str, bool]
      What the function gives, as 'QObject *', and whether it is const.

    Raises
    ------

    ValueError
      The text has no pair of brackets holding what the function takes.
    """
    close = functionType.rfind(')')
    depth, start = 0, -1
    for index in range(close, -1, -1):
      if functionType[index] == ')':
        depth += 1
      elif functionType[index] == '(':
        depth -= 1
        if depth == 0:
          start = index
          break
    if close < 0 or start < 0:
      infoSpec = """Expected the type of a function, as 'int (int)', but
      received '%s'."""
      raise ValueError(' '.join((infoSpec % functionType).split()))
    given = functionType[:start].strip()
    const = 'const' in functionType[close + 1:].split()
    return given, const

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What the compiler calls each kind of member function.
  __member_kinds__ = {
      'CXXConstructorDecl': 'constructor',
      'CXXDestructorDecl': 'destructor',
      'CXXMethodDecl': 'method',
  }

  #  Fallback Variables

  #  Private Variables
  __class_name__ = None  # type: Optional[str]
  __read_declarations__ = None  # type: Optional[Declarations]
  __read_parents__ = None  # type: Optional[Tuple[str, ...]]
  __read_summary__ = None  # type: Optional[Dict[str, Tuple[str, ...]]]
  __read_records__ = None  # type: Optional[Tuple[Dict[str, Any], ...]]
  __read_class_record__ = None  # type: Optional[Dict[str, Any]]
  __read_members__ = None  # type: Optional[Tuple[Member, ...]]
  __read_summary_record__ = None  # type: Optional[Dict[str, Any]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getClassName(self) -> str:
    """
    Gives the Qt class this header reads.

    Provided by you, through 'setClassName'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setClassName' has not been called on this header.
    """
    if self.__class_name__ is None:
      raise MissingVariable(self, '__class_name__', str)
    return self.__class_name__

  def getQtModule(self) -> str:
    """
    Gives the part of Qt the class belongs to, as 'QtCore'.

    Found for you, by 'findQtModule', from the class name you set.

    Raises
    ------

    LookupError
      Qt has no class of that name.
    """
    return self.findQtModule(self.getClassName())

  def getCommand(self) -> Tuple[str, ...]:
    """
    Gives the exact 'clang++' command that reads the header, without
    running it.

    Found for you. The command is handed one line of C++ to read,
    '#include <QtCore/QObject>', which pulls the header in.

    Returns
    -------

    Tuple[str, ...]
      One argument per entry: 'clang++', then
      '-x c++ -std=c++17', to read C++ of the 2017 standard;
      '-fPIC', which Qt's headers insist on;
      '-fsyntax-only', to read and check but compile nothing;
      '-I' with the folder of Qt's headers;
      '-Xclang -ast-dump=json', to write what was read as JSON;
      '-Xclang -ast-dump-filter=' with the class name, to write only
      what has that name in it;
      '-', to read the one line of C++ handed to it.
    """
    className = self.getClassName()
    return (
        'clang++', '-x', 'c++', '-std=c++17', '-fPIC', '-fsyntax-only',
        '-I%s' % Build.getQtHeaderFolder(),
        '-Xclang', '-ast-dump=json',
        '-Xclang', '-ast-dump-filter=%s' % className, '-',
    )

  def _createDeclarations(self, ) -> None:
    """Runs the compiler and turns what it reports into declarations."""
    className = self.getClassName()
    include = '#include <%s/%s>\n' % (self.getQtModule(), className)
    reported = self._run(*self.getCommand(), feed=include)
    records = self._decodeRecords(reported)
    record = self._findClassRecord(records)
    parents = [base['type']['qualType'] for base in record.get('bases', ())]
    #  Everything is kept: all the compiler wrote, the record of the
    #  class, and each of its members with who may use it.
    self.__read_records__ = (*records,)
    self.__read_class_record__ = record
    self.__read_parents__ = (*parents,)
    members = []
    access = 'private'
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
        continue
      members.append((access, member))
    self.__read_members__ = (*members,)
    declarations = []
    for access, raw in members:
      member, kind = raw, raw.get('kind')
      if member.get('isImplicit'):
        continue
      template = kind == 'FunctionTemplateDecl'
      if template:
        inner = [
            entry for entry in member.get('inner', ())
            if entry.get('kind') in self.__member_kinds__
        ]
        if len(inner) != 1:
          continue
        member, kind = inner[0], inner[0]['kind']
      if kind not in self.__member_kinds__:
        continue
      made = self._makeDeclaration(member, access, template, raw)
      declarations.append(made)
    self.__read_declarations__ = (*declarations,)

  def getDeclarations(self, **kwargs) -> Declarations:
    """
    Gives one 'Declaration' per function the class declares, in the
    order the header declares them.

    Found for you: the compiler is run at the first call, and the answer
    kept. You pass nothing; the keyword is for the method's own use.

    Returns
    -------

    Declarations
      A 'Tuple[Declaration, ...]'. For 'QObject' it holds 80.

    Raises
    ------

    MissingVariable
      'setClassName' has not been called on this header.

    LookupError
      Qt has no class of that name.

    FileNotFoundError
      'clang++' or 'qmake6' is not installed.

    RuntimeError
      The compiler failed to read the header; its message is included.
    """
    if self.__read_declarations__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createDeclarations()
      return self.getDeclarations(_recursion=True)
    return self.__read_declarations__

  def getRecords(self) -> Tuple[Dict[str, Any], ...]:
    """
    Gives everything the compiler wrote, untouched: one record for each
    thing with the class name in its own name.

    Found for you, at the same reading as 'getDeclarations'. Besides
    the class itself this holds its relatives, as 'QObjectData' and
    'QObjectList' for 'QObject'. Nothing the compiler reported is left
    out of it.

    Returns
    -------

    Tuple[Dict[str, Any], ...]
      The records as the compiler wrote them, in JSON turned into
      Python: dicts, lists, text and numbers.
    """
    self.getDeclarations()
    return self.__read_records__

  def getClassRecord(self) -> Dict[str, Any]:
    """
    Gives everything the compiler reported for the class itself,
    untouched.

    Found for you, at the same reading as 'getDeclarations'. Every
    other getter here is worked out from this record, so what none of
    them covers yet is still in here.
    """
    self.getDeclarations()
    return self.__read_class_record__

  def getMembers(self) -> Tuple[Member, ...]:
    """
    Gives every member of the class, in the order the header has them,
    whatever kind it is: functions, but also attributes, classes
    declared inside the class, friends and variables.

    Found for you, at the same reading as 'getDeclarations', which
    gives only the functions among these.

    Returns
    -------

    Tuple[Member, ...]
      One 'Tuple[str, Dict[str, Any]]' per member: who may use it,
      'public', 'protected' or 'private', and the untouched record of
      it. The 'kind' entry of a record says what the member is.
    """
    self.getDeclarations()
    return self.__read_members__

  def getSummaryRecord(self) -> Dict[str, Any]:
    """
    Gives everything Qt's own summary says about the class, untouched.

    Found for you, from the summary file. The names 'getSignalNames',
    'getSlotNames' and 'getPropertyNames' give are taken from it; it
    also holds what each signal takes, and the getter, the setter and
    the signal behind each property. It is empty for a class the
    summary does not mention, as every class not built on 'QObject'.
    """
    self._getSummary()
    return self.__read_summary_record__

  def getParents(self) -> Tuple[str, ...]:
    """
    Gives the classes this class is built on, by name.

    Found for you, from what the compiler reports. It is empty for a
    class built on nothing, as 'QObject'; 'QWidget' gives 'QObject' and
    'QPaintDevice'.
    """
    self.getDeclarations()
    return self.__read_parents__

  def getSummaryFile(self) -> str:
    """
    Gives the path of Qt's own summary of the headers of this part of
    Qt, as '/usr/lib/qt6/metatypes/qt6core_metatypes.json'.

    Found for you. Qt installs one such file per part. It says which
    functions are signals and slots, and which properties a class has.
    """
    folder = self._run('qmake6', '-query', 'QT_INSTALL_ARCHDATA').strip()
    name = 'qt6%s_metatypes.json' % self.getQtModule()[2:].lower()
    return os.path.join(folder, 'metatypes', name)

  def _createSummary(self, ) -> None:
    """Reads what Qt's own summary says about the class."""
    summaryFile = self.getSummaryFile()
    if not os.path.isfile(summaryFile):
      infoSpec = """Qt's summary of its headers was expected at '%s', and
      there is no such file."""
      raise FileNotFoundError(' '.join((infoSpec % summaryFile).split()))
    with open(summaryFile) as file:
      units = json.load(file)
    className = self.getClassName()
    found = dict(signals=(), slots=(), properties=())
    kept = dict()  # type: Dict[str, Any]
    for unit in units:
      for entry in unit.get('classes', ()):
        if entry.get('qualifiedClassName') != className:
          continue
        kept = entry
        for key in found:
          names = [item['name'] for item in entry.get(key, ())]
          found[key] = (*dict.fromkeys(names),)
    self.__read_summary__ = found
    self.__read_summary_record__ = kept

  def _getSummary(self, **kwargs) -> Dict[str, Tuple[str, ...]]:
    if self.__read_summary__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createSummary()
      return self._getSummary(_recursion=True)
    return self.__read_summary__

  def getSignalNames(self) -> Tuple[str, ...]:
    """
    Gives the name of each signal of the class, as 'destroyed'.

    Found for you, from Qt's own summary of the header. It is empty for
    a class with no signals, which every class not built on 'QObject'
    is.
    """
    return self._getSummary()['signals']

  def getSlotNames(self) -> Tuple[str, ...]:
    """
    Gives the name of each slot of the class, as 'deleteLater'.

    Found for you, from Qt's own summary of the header.
    """
    return self._getSummary()['slots']

  def getPropertyNames(self) -> Tuple[str, ...]:
    """
    Gives the name of each property of the class, as 'objectName'.

    Found for you, from Qt's own summary of the header. A property is a
    named value Qt knows about, with a getter, and often a setter and a
    signal, behind it.
    """
    return self._getSummary()['properties']

  def getTypes(self) -> Dict[str, int]:
    """
    Gives every C++ type the functions of the class take or give back,
    and how many times each appears.

    Worked out from the declarations. Private functions and templates
    are left out, since neither gets a ritual. Each of these types
    needs an answer to the question of what it is in Python.

    Returns
    -------

    Dict[str, int]
      The type as C++ writes it, and its count, most used first.
    """
    counts = dict()  # type: Dict[str, int]
    for declaration in self.getDeclarations():
      if declaration.getAccess() == 'private':
        continue
      if declaration.getKind() == 'template':
        continue
      types = [cppType for _, cppType in declaration.getTakes()]
      types.append(declaration.getGives())
      for cppType in types:
        counts[cppType] = counts.get(cppType, 0) + 1
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return dict(ordered)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setClassName(self, className: str) -> None:
    """
    Tells the header which Qt class to read.

    Required before 'getDeclarations'. Calling it again reads another
    class and forgets what was read before.

    Parameters
    ----------

    className : str
      The class by Qt's own name, as 'QObject'.

    Raises
    ------

    TypeException
      'className' is not text.
    """
    if not isinstance(className, str):
      raise TypeException('className', className, str)
    self.__class_name__ = className
    self.__read_declarations__ = None
    self.__read_parents__ = None
    self.__read_summary__ = None
    self.__read_records__ = None
    self.__read_class_record__ = None
    self.__read_members__ = None
    self.__read_summary_record__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which class is read, or that none is set yet."""
    clsName = type(self).__name__
    if self.__class_name__ is None:
      return '<%s still waiting for: setClassName>' % clsName
    return "<%s of the class '%s'>" % (clsName, self.__class_name__)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _run(*command: str, **kwargs: Any) -> str:
    """
    Runs one program to its end and gives what it printed.

    Parameters
    ----------

    *command : str
      The program, then each of its arguments.

    **kwargs
      feed : str, optional
        Text for the program to read.

    Raises
    ------

    FileNotFoundError
      The program is not installed on this machine.

    RuntimeError
      The program ran and reported a failure; its message is included.
    """
    try:
      done = subprocess.run(
          command, input=kwargs.get('feed'), capture_output=True,
          text=True,
      )
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program '%s' is needed and is not installed."""
      raise FileNotFoundError(infoSpec % command[0]) from fileNotFoundError
    if done.returncode:
      infoSpec = """The program '%s' failed: %s"""
      raise RuntimeError(infoSpec % (command[0], done.stderr.strip()))
    return done.stdout

  @staticmethod
  def _decodeRecords(reported: str) -> List[Dict[str, Any]]:
    """
    Turns what the compiler wrote into Python, leaving nothing out.

    The compiler writes several JSON documents one after another, one
    for each thing with the class name in its own name.
    """
    records = []
    decoder, index = json.JSONDecoder(), 0
    while index < len(reported):
      if reported[index].isspace():
        index += 1
        continue
      record, index = decoder.raw_decode(reported, index)
      records.append(record)
    return records

  def _findClassRecord(
      self,
      records: List[Dict[str, Any]],
  ) -> Dict[str, Any]:
    """
    Finds, among the records the compiler wrote, that of the class
    itself, where it is defined in full.

    Raises
    ------

    LookupError
      The compiler reported no full definition of the class.
    """
    className = self.getClassName()
    for record in records:
      named = record.get('name') == className
      isClass = record.get('kind') == 'CXXRecordDecl'
      if named and isClass and record.get('completeDefinition'):
        return record
    infoSpec = """The compiler reported no definition of the class '%s'
    in its own header."""
    raise LookupError(' '.join((infoSpec % className).split()))

  def _makeDeclaration(
      self,
      member: Dict[str, Any],
      access: str,
      template: bool,
      raw: Dict[str, Any],
  ) -> Declaration:
    """Fills one declaration in from one member the compiler reported."""
    className = self.getClassName()
    kind = self.__member_kinds__[member['kind']]
    given, const = self._splitFunctionType(member['type']['qualType'])
    if kind == 'constructor':
      given = '%s *' % className
    elif kind == 'method' and member.get('storageClass') == 'static':
      kind = 'static method'
    taken = [
        (entry.get('name', ''), entry['type']['qualType'])
        for entry in member.get('inner', ())
        if entry.get('kind') == 'ParmVarDecl'
    ]
    where = member.get('loc', {})
    line = where.get('line', where.get('expansionLoc', {}).get('line'))
    declaration = Declaration()
    declaration.setClassName(className)
    declaration.setFunctionName(member['name'])
    declaration.setKind('template' if template else kind)
    declaration.setTakes(*taken)
    declaration.setGives(given)
    declaration.setAccess(access)
    declaration.setVirtual(bool(member.get('virtual', False)))
    declaration.setConst(const)
    declaration.setHeaderLine(line)
    declaration.setCompilerName(member.get('mangledName'))
    defaults = [
        entry for entry in member.get('inner', ())
        if entry.get('kind') == 'ParmVarDecl' and 'init' in entry
    ]
    declaration.setDefaultCount(len(defaults))
    declaration.setInline(bool(member.get('inline', False)))
    declaration.setDeleted(bool(member.get('explicitlyDeleted', False)))
    declaration.setPure(bool(member.get('pure', False)))
    declaration.setSignal(member['name'] in self.getSignalNames())
    declaration.setSlot(member['name'] in self.getSlotNames())
    declaration.setRawRecord(raw)
    return declaration

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def named(self, functionName: str) -> Declarations:
    """
    Gives the declarations of one function name, as 'setParent'.

    Returns
    -------

    Declarations
      A 'Tuple[Declaration, ...]': empty when the class declares no
      function of that name, and of several when it is overloaded.
    """
    return (*(
        declaration for declaration in self.getDeclarations()
        if declaration.getFunctionName() == functionName
    ),)
