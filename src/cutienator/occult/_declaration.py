"""Declaration is one function as a Qt header declares it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Argument = Tuple[str, str]


class Declaration:
  """
  One function as a Qt header declares it: which class it belongs to,
  its name, its type signature, and what kind of function it is.

    for declaration in header.getDeclarations():
      print(declaration)     # void QObject::setParent(QObject *parent)
      declaration.getTakes() # (('parent', 'QObject *'),)
      declaration.getGives() # 'void'

  Terms
  -----

  - The type signature is the types the function takes, in order, and
    the type it gives back, written as C++ writes them: 'QObject *',
    'int', 'void'.
  - The kind is one of 'constructor', 'destructor', 'method',
    'static method' and 'template'.
  - The access is who may call the function: 'public', 'protected' or
    'private'.

  You provide
  -----------

  Nothing. A 'Header' fills each declaration in, through the setters,
  from what the compiler reports. You read it.

  What to expect
  --------------

  - Everything here comes from the header, except whether a function
    is a signal or a slot, which comes from Qt's own summary of the
    header.
  - Types are kept as text, exactly as C++ writes them. Nothing here
    says what a type becomes in Python.
  - Reading a value its setter was never given raises
    'MissingVariable', naming it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __known_kinds__ = (
      'constructor', 'destructor', 'method', 'static method', 'template',
  )
  __known_accesses__ = ('public', 'protected', 'private')

  #  Fallback Variables

  #  Private Variables
  __class_name__ = None  # type: Optional[str]
  __function_name__ = None  # type: Optional[str]
  __function_kind__ = None  # type: Optional[str]
  __taken_arguments__ = None  # type: Optional[Tuple[Argument, ...]]
  __given_type__ = None  # type: Optional[str]
  __access_level__ = None  # type: Optional[str]
  __is_virtual__ = None  # type: Optional[bool]
  __is_const__ = None  # type: Optional[bool]
  __header_line__ = None  # type: Optional[int]
  __has_header_line__ = False
  __compiler_name__ = None  # type: Optional[str]
  __has_compiler_name__ = False
  __default_count__ = None  # type: Optional[int]
  __is_inline__ = None  # type: Optional[bool]
  __is_deleted__ = None  # type: Optional[bool]
  __is_pure__ = None  # type: Optional[bool]
  __is_signal__ = None  # type: Optional[bool]
  __is_slot__ = None  # type: Optional[bool]
  __raw_record__ = None  # type: Optional[Dict[str, Any]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getClassName(self) -> str:
    """
    Gives the class the function belongs to, as 'QObject'.

    Filled in by the 'Header', from the class it was asked to read.
    """
    if self.__class_name__ is None:
      raise MissingVariable(self, '__class_name__', str)
    return self.__class_name__

  def getFunctionName(self) -> str:
    """
    Gives Qt's own name for the function, as 'setParent'.

    Filled in by the 'Header'. A constructor is named as its class,
    'QObject', and a destructor with a tilde in front, '~QObject', which
    is how C++ names them. Several declarations of one class share a
    name when the function is overloaded.
    """
    if self.__function_name__ is None:
      raise MissingVariable(self, '__function_name__', str)
    return self.__function_name__

  def getKind(self) -> str:
    """
    Gives what kind of function this is.

    Filled in by the 'Header'.

    Returns
    -------

    str
      'constructor': creates an object of the class.
      'destructor': destroys one.
      'method': called on an object.
      'static method': called on the class itself, with no object.
      'template': a pattern the compiler fills in per type, so there is
      no single function to call.
    """
    if self.__function_kind__ is None:
      raise MissingVariable(self, '__function_kind__', str)
    return self.__function_kind__

  def getTakes(self) -> Tuple[Argument, ...]:
    """
    Gives what the function takes, in order.

    Filled in by the 'Header'. The object a method is called on is not
    among them; C++ does not write it in the declaration.

    Returns
    -------

    Tuple[Argument, ...]
      One 'Tuple[str, str]' per argument: its name, which is '' when the
      header gives it none, and its type as C++ writes it. It is empty
      for a function taking nothing.
    """
    if self.__taken_arguments__ is None:
      raise MissingVariable(self, '__taken_arguments__', tuple)
    return self.__taken_arguments__

  def getGives(self) -> str:
    """
    Gives the type the function gives back, as C++ writes it.

    Filled in by the 'Header'. 'void' means nothing comes back. For a
    constructor it is the class with a star, as 'QObject *': the address
    of the new object. For a destructor it is 'void'.
    """
    if self.__given_type__ is None:
      raise MissingVariable(self, '__given_type__', str)
    return self.__given_type__

  def getAccess(self) -> str:
    """
    Gives who may call the function: 'public', 'protected' or 'private'.

    Filled in by the 'Header'. Public is for everyone, protected for
    subclasses only, and private for Qt's own use.
    """
    if self.__access_level__ is None:
      raise MissingVariable(self, '__access_level__', str)
    return self.__access_level__

  def isVirtual(self) -> bool:
    """
    Says whether a subclass may replace the function, in which case C++
    calls the replacement.

    Filled in by the 'Header'.
    """
    if self.__is_virtual__ is None:
      raise MissingVariable(self, '__is_virtual__', bool)
    return self.__is_virtual__

  def isConst(self) -> bool:
    """
    Says whether the function promises not to change the object it is
    called on.

    Filled in by the 'Header'.
    """
    if self.__is_const__ is None:
      raise MissingVariable(self, '__is_const__', bool)
    return self.__is_const__

  def getHeaderLine(self) -> Optional[int]:
    """
    Gives the line of the header the function is declared on.

    Filled in by the 'Header'.

    Returns
    -------

    Optional[int]
      The line number, counted from 1. For a function the header does
      not write out itself but gets from a Qt macro, as 'tr', it is the
      line the macro stands on. None when the compiler reports no line.
    """
    if not self.__has_header_line__:
      raise MissingVariable(self, '__header_line__', int)
    return self.__header_line__

  def getDefaultCount(self) -> int:
    """
    Gives how many of the last arguments may be left out of a call,
    because the header gives them a value to fall back on.

    Filled in by the 'Header'. 'QObject(QObject *parent = nullptr)'
    gives 1: it may be called with one argument or with none.
    """
    if self.__default_count__ is None:
      raise MissingVariable(self, '__default_count__', int)
    return self.__default_count__

  def isInline(self) -> bool:
    """
    Says whether the header holds the body of the function, in which
    case Qt's shared object may have no name for it.

    Filled in by the 'Header'.
    """
    if self.__is_inline__ is None:
      raise MissingVariable(self, '__is_inline__', bool)
    return self.__is_inline__

  def isDeleted(self) -> bool:
    """
    Says whether the header declares the function only to forbid it, as
    Qt does for copying a 'QObject'. Such a function cannot be called.

    Filled in by the 'Header'.
    """
    if self.__is_deleted__ is None:
      raise MissingVariable(self, '__is_deleted__', bool)
    return self.__is_deleted__

  def isPure(self) -> bool:
    """
    Says whether the function is virtual with no body of its own, so
    that a subclass must supply it.

    Filled in by the 'Header'.
    """
    if self.__is_pure__ is None:
      raise MissingVariable(self, '__is_pure__', bool)
    return self.__is_pure__

  def isSignal(self) -> bool:
    """
    Says whether the function is a signal: one whose body Qt writes, and
    which notifies everything connected to it when called.

    Filled in by the 'Header', from Qt's own summary of the header.
    """
    if self.__is_signal__ is None:
      raise MissingVariable(self, '__is_signal__', bool)
    return self.__is_signal__

  def isSlot(self) -> bool:
    """
    Says whether the function is a slot: an ordinary method that Qt can
    also call by its name.

    Filled in by the 'Header', from Qt's own summary of the header.
    """
    if self.__is_slot__ is None:
      raise MissingVariable(self, '__is_slot__', bool)
    return self.__is_slot__

  def getRawRecord(self) -> Dict[str, Any]:
    """
    Gives everything the compiler reported for this function, untouched.

    Filled in by the 'Header'. Every other getter here is worked out
    from this record. It is kept whole so that nothing found in the
    header is lost: what no getter covers yet is still in here, such as
    the value an argument falls back on.

    Returns
    -------

    Dict[str, Any]
      The record as the compiler wrote it, in JSON turned into Python:
      dicts, lists, text and numbers. For a template it is the record of
      the whole template.
    """
    if self.__raw_record__ is None:
      raise MissingVariable(self, '__raw_record__', dict)
    return self.__raw_record__

  def getCompilerName(self) -> Optional[str]:
    """
    Gives the compiler's own name for the function, the scrambled one,
    as '_ZN7QObject9setParentEPS_'.

    Filled in by the 'Header'. The class, the function and the types it
    takes are packed into it, so no two functions share one, not even
    functions Qt gives the same name. It is the name the function has
    in Qt's shared object, when it is in there at all.

    Returns
    -------

    Optional[str]
      The name, or None for a template, which is a pattern and no single
      function.
    """
    if not self.__has_compiler_name__:
      raise MissingVariable(self, '__compiler_name__', str)
    return self.__compiler_name__

  def getRitualName(self) -> str:
    """
    Gives the name of the ritual for this function: the name Python
    passes to 'Rituals.call', and the name the ritual has in its ritual
    file.

    Worked out as 'ritual' followed by the compiler's own name:
    'ritual_ZN7QObject9setParentEPS_'. It is a key and nothing more.
    It has the types packed into it, so overloaded functions get
    different names. Nobody types it or needs to read it; 'str' of the
    declaration is the readable form.

    Raises
    ------

    LookupError
      The function is a template. A template is no single function, so
      it has no ritual.
    """
    compilerName = self.getCompilerName()
    if compilerName is None:
      infoSpec = """'%s' is a template, which is a pattern and no single
      function, so it has no ritual."""
      raise LookupError(' '.join((infoSpec % (self,)).split()))
    return 'ritual%s' % compilerName

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setClassName(self, className: str) -> None:
    """Called by the 'Header' with the class the function belongs to."""
    if not isinstance(className, str):
      raise TypeException('className', className, str)
    self.__class_name__ = className

  def setFunctionName(self, functionName: str) -> None:
    """Called by the 'Header' with Qt's own name for the function."""
    if not isinstance(functionName, str):
      raise TypeException('functionName', functionName, str)
    self.__function_name__ = functionName

  def setKind(self, kind: str) -> None:
    """
    Called by the 'Header' with the kind of function.

    Raises
    ------

    ValueError
      'kind' is not one of the five kinds 'getKind' lists.
    """
    if kind not in self.__known_kinds__:
      infoSpec = """The kind of a function is one of %s, but received
      '%s'."""
      known = ', '.join("'%s'" % known for known in self.__known_kinds__)
      raise ValueError(' '.join((infoSpec % (known, kind)).split()))
    self.__function_kind__ = kind

  def setTakes(self, *arguments: Argument) -> None:
    """
    Called by the 'Header' with what the function takes.

    Parameters
    ----------

    *arguments : Argument
      One 'Tuple[str, str]' per argument, in order: its name, or '' when
      the header gives none, and its type as C++ writes it. Called with
      nothing for a function that takes nothing.
    """
    for argument in arguments:
      if not isinstance(argument, tuple) or len(argument) != 2:
        raise TypeException('argument', argument, tuple)
      for part in argument:
        if not isinstance(part, str):
          raise TypeException('argument', argument, tuple)
    self.__taken_arguments__ = (*arguments,)

  def setGives(self, givenType: str) -> None:
    """Called by the 'Header' with the type the function gives back."""
    if not isinstance(givenType, str):
      raise TypeException('givenType', givenType, str)
    self.__given_type__ = givenType

  def setAccess(self, access: str) -> None:
    """
    Called by the 'Header' with who may call the function.

    Raises
    ------

    ValueError
      'access' is not 'public', 'protected' or 'private'.
    """
    if access not in self.__known_accesses__:
      infoSpec = """The access of a function is 'public', 'protected' or
      'private', but received '%s'."""
      raise ValueError(' '.join((infoSpec % (access,)).split()))
    self.__access_level__ = access

  def setVirtual(self, virtual: bool) -> None:
    """Called by the 'Header': may a subclass replace the function?"""
    if not isinstance(virtual, bool):
      raise TypeException('virtual', virtual, bool)
    self.__is_virtual__ = virtual

  def setConst(self, const: bool) -> None:
    """Called by the 'Header': does it leave its object unchanged?"""
    if not isinstance(const, bool):
      raise TypeException('const', const, bool)
    self.__is_const__ = const

  def setDefaultCount(self, defaultCount: int) -> None:
    """Called by the 'Header': how many last arguments may be left out."""
    if isinstance(defaultCount, bool) or not isinstance(defaultCount, int):
      raise TypeException('defaultCount', defaultCount, int)
    self.__default_count__ = defaultCount

  def setInline(self, inline: bool) -> None:
    """Called by the 'Header': does the header hold the body?"""
    if not isinstance(inline, bool):
      raise TypeException('inline', inline, bool)
    self.__is_inline__ = inline

  def setDeleted(self, deleted: bool) -> None:
    """Called by the 'Header': is it declared only to forbid it?"""
    if not isinstance(deleted, bool):
      raise TypeException('deleted', deleted, bool)
    self.__is_deleted__ = deleted

  def setPure(self, pure: bool) -> None:
    """Called by the 'Header': must a subclass supply the body?"""
    if not isinstance(pure, bool):
      raise TypeException('pure', pure, bool)
    self.__is_pure__ = pure

  def setSignal(self, signal: bool) -> None:
    """Called by the 'Header': is the function a signal?"""
    if not isinstance(signal, bool):
      raise TypeException('signal', signal, bool)
    self.__is_signal__ = signal

  def setSlot(self, slot: bool) -> None:
    """Called by the 'Header': is the function a slot?"""
    if not isinstance(slot, bool):
      raise TypeException('slot', slot, bool)
    self.__is_slot__ = slot

  def setRawRecord(self, rawRecord: Dict[str, Any]) -> None:
    """Called by the 'Header' with all the compiler reported for it."""
    if not isinstance(rawRecord, dict):
      raise TypeException('rawRecord', rawRecord, dict)
    self.__raw_record__ = rawRecord

  def setCompilerName(self, compilerName: Optional[str]) -> None:
    """
    Called by the 'Header' with the compiler's own name for the
    function, or with None for a template.
    """
    if compilerName is not None and not isinstance(compilerName, str):
      raise TypeException('compilerName', compilerName, str)
    self.__compiler_name__ = compilerName
    self.__has_compiler_name__ = True

  def setHeaderLine(self, headerLine: Optional[int]) -> None:
    """
    Called by the 'Header' with the line the function is declared on,
    or with None when the compiler reports no line for it.
    """
    if headerLine is not None and not isinstance(headerLine, int):
      raise TypeException('headerLine', headerLine, int)
    self.__header_line__ = headerLine
    self.__has_header_line__ = True

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """
    Writes the declaration out as C++ would, on one line, as
    'void QObject::setParent(QObject *parent)'.
    """
    taken = []
    for name, cppType in self.getTakes():
      if not name:
        taken.append(cppType)
      elif cppType.endswith(('*', '&')):
        taken.append('%s%s' % (cppType, name))
      else:
        taken.append('%s %s' % (cppType, name))
    words = []
    if self.isVirtual():
      words.append('virtual')
    if self.getKind() == 'static method':
      words.append('static')
    owner = '%s::%s' % (self.getClassName(), self.getFunctionName())
    text = '%s(%s)' % (owner, ', '.join(taken))
    if self.getKind() not in ('constructor', 'destructor'):
      given = self.getGives()
      joint = '' if given.endswith(('*', '&')) else ' '
      text = '%s%s%s' % (given, joint, text)
    if self.isConst():
      text = '%s const' % text
    return ' '.join((*words, text))

  def __repr__(self) -> str:
    """Gives the declaration as '__str__' does, between brackets."""
    return '<%s: %s>' % (type(self).__name__, str(self))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
