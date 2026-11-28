"""
QV4::Compiler::ControlFlow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilercontrolflow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::Compiler::ControlFlow to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ControlFlow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::ControlFlow: a plain Python object
  standing in front of one C++ QV4::Compiler::ControlFlow.

  C++ hands a QV4::Compiler::ControlFlow around as a copy, so every C++
  QV4::Compiler::ControlFlow behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::ControlFlow that has a ritual and
  that Python can call so far, 5 names in all: 'unwindTarget', 'label',
  'hasLoop', 'requiresUnwind', 'loopLabel'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Compiler::ControlFlow::ControlFlow(Codegen *cg, Type type)':
    names 'QV4::Compiler::Codegen', which has no cute class yet.
  - Qt's 'QV4::Compiler::ControlFlow::~ControlFlow()': the destructor: Python
    removes its C++ QV4::Compiler::ControlFlow by it, and has no other use
    for it.
  - Qt's 'BytecodeGenerator *QV4::Compiler::ControlFlow::generator() const':
    gives 'Moth::BytecodeGenerator', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 3 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QV4::Compiler::ControlFlow is created at the first use, not by
    'QV4::Compiler::ControlFlow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::ControlFlow back gives a copy the
    ritual made for Python, in a new cute QV4::Compiler::ControlFlow.
  - Each name of Qt's QV4::Compiler::ControlFlow that has no cute function
    yet, '__init__', 'generator', 'getUnwindTarget', 'parentUnwindHandler',
    'unwindHandler', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QV4::Compiler::ControlFlow, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'QV4::Compiler::ControlFlow::Type' of Qt, with the 5 names Qt
    gives in it.
    """

    Loop = Kee[int](0)
    With = Kee[int](1)
    Block = Kee[int](2)
    Finally = Kee[int](3)
    Catch = Kee[int](4)

  class UnwindType(CuteNum):
    """
    The enum 'QV4::Compiler::ControlFlow::UnwindType' of Qt, with the 3 names
    Qt gives in it.
    """

    Break = Kee[int](0)
    Continue = Kee[int](1)
    Return = Kee[int](2)

  #  The classes Qt writes inside QV4::Compiler::ControlFlow, each a class in
  #  here as in C++.

  class UnwindTarget(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::ControlFlow::UnwindTarget: a plain
    Python object standing in front of one C++
    QV4::Compiler::ControlFlow::UnwindTarget.

    C++ hands a QV4::Compiler::ControlFlow::UnwindTarget around as a copy, so
    every C++ QV4::Compiler::ControlFlow::UnwindTarget behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QV4::Compiler::ControlFlow::UnwindTarget yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Compiler::ControlFlow::UnwindTarget::~UnwindTarget()': the
      destructor: Python removes its C++
      QV4::Compiler::ControlFlow::UnwindTarget by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::ControlFlow::UnwindTarget is created at the
      first use, not by 'QV4::Compiler::ControlFlow::UnwindTarget(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::ControlFlow::UnwindTarget back gives
      a copy the ritual made for Python, in a new cute
      QV4::Compiler::ControlFlow::UnwindTarget.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::ControlFlow::UnwindTarget'

    #  Qt's '~QV4::Compiler::ControlFlow::UnwindTarget()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Compiler::ControlFlow::UnwindTarget behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV48Compiler11ControlFlow12UnwindTargetD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::ControlFlow'

  #  A C++ QV4::Compiler::ControlFlow Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QV4_Compiler_ControlFlow'

  #  The functions Qt calls itself that QV4::Compiler::ControlFlow is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getUnwindTarget': (
          'BytecodeGenerator::Label '
          'QV4::Compiler::ControlFlow::getUnwindTarget(UnwindType, const '
          'QString &)',
      ),
      'unwindHandler': (
          'BytecodeGenerator::ExceptionHandler '
          '*QV4::Compiler::ControlFlow::unwindHandler()',
      ),
  }

  #  The functions Qt calls itself that QV4::Compiler::ControlFlow is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'label': (
          ('_ZNK3QV48Compiler11ControlFlow5labelEv',
           ('address', 'text', ''),
           ()),
      ),
      'requiresUnwind': (
          ('_ZN3QV48Compiler11ControlFlow14requiresUnwindEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Qt's '~QV4::Compiler::ControlFlow()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::Compiler::ControlFlow behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler11ControlFlowD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def label(self) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::ControlFlow::label() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflow.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::ControlFlow::label() const
    ritual = 'ritual_ZNK3QV48Compiler11ControlFlow5labelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK3QV48Compiler11ControlFlow5labelEv'
    return self.uglySide.call(ritual)

  def hasLoop(self) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::ControlFlow::hasLoop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflow.html#hasLoop
    """
    #  bool QV4::Compiler::ControlFlow::hasLoop() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler11ControlFlow7hasLoopEv',
    )

  def loopLabel(self) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::ControlFlow::loopLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflow.html#loopLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::ControlFlow::loopLabel() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler11ControlFlow9loopLabelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QV4::Compiler::ControlFlow::ControlFlow(Codegen *cg, Type type)':
    names 'QV4::Compiler::Codegen', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlow.__init__' has no cute function yet. Qt's "
        "'QV4::Compiler::ControlFlow::ControlFlow(Codegen *cg, Type type)': "
        "names 'QV4::Compiler::Codegen', which has no cute class yet.")

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

  @overload(UnwindType)
  @overload(UnwindType, str)
  def unwindTarget(self, type: UnwindType, label: str = '') -> UnwindTarget:
    """
    Calls Qt's 'UnwindTarget
    QV4::Compiler::ControlFlow::unwindTarget(UnwindType type, const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflow.html#unwindTarget

    Parameters
    ----------

    type : UnwindType
      Passed on as its number.

    label : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    UnwindTarget
      A new cute QV4::Compiler::ControlFlow::UnwindTarget around the copy Qt
      gave back. Python owns it.
    """
    #  UnwindTarget QV4::Compiler::ControlFlow::unwindTarget(UnwindType type,
    #      const QString &label)
    address = self.uglySide.call(
        'ritual_ZN3QV48Compiler11ControlFlow12unwindTargetENS1_10UnwindType'
        'ERK7QString',
        type.value, label,
    )
    return QV4.Compiler.ControlFlow.UnwindTarget._cuteOwning(address)

  def requiresUnwind(self) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::ControlFlow::requiresUnwind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflow.html#requiresUnwind
    """
    #  bool QV4::Compiler::ControlFlow::requiresUnwind()
    ritual = 'ritual_ZN3QV48Compiler11ControlFlow14requiresUnwindEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN3QV48Compiler11ControlFlow14requiresUnwindEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def generator(*__, **_) -> Never:
    """
    Qt's 'BytecodeGenerator *QV4::Compiler::ControlFlow::generator() const':
    gives 'Moth::BytecodeGenerator', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlow.generator' has no cute function yet. "
        "Qt's 'BytecodeGenerator *QV4::Compiler::ControlFlow::generator() "
        "const': gives 'Moth::BytecodeGenerator', which has no cute class "
        "yet.")

  @staticmethod
  def getUnwindTarget(*__, **_) -> Never:
    """
    Qt's 'BytecodeGenerator::Label
    QV4::Compiler::ControlFlow::getUnwindTarget(UnwindType a0, const QString
    &a1)': the compiler refuses its ritual as it would be written here: use
    of undeclared identifier 'BytecodeGenerator'; did you mean
    'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlow.getUnwindTarget' has no cute function "
        "yet. Qt's 'BytecodeGenerator::Label "
        "QV4::Compiler::ControlFlow::getUnwindTarget(UnwindType a0, const "
        "QString &a1)': the compiler refuses its ritual as it would be "
        "written here: use of undeclared identifier 'BytecodeGenerator'; "
        "did you mean 'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.")

  @staticmethod
  def parentUnwindHandler(*__, **_) -> Never:
    """
    Qt's 'BytecodeGenerator::ExceptionHandler
    *QV4::Compiler::ControlFlow::parentUnwindHandler()': the compiler refuses
    its ritual as it would be written here: use of undeclared identifier
    'BytecodeGenerator'; did you mean
    'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlow.parentUnwindHandler' has no cute "
        "function yet. Qt's 'BytecodeGenerator::ExceptionHandler "
        "*QV4::Compiler::ControlFlow::parentUnwindHandler()': the compiler "
        "refuses its ritual as it would be written here: use of undeclared "
        "identifier 'BytecodeGenerator'; did you mean "
        "'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.")

  @staticmethod
  def unwindHandler(*__, **_) -> Never:
    """
    Qt's 'BytecodeGenerator::ExceptionHandler
    *QV4::Compiler::ControlFlow::unwindHandler()': the compiler refuses its
    ritual as it would be written here: use of undeclared identifier
    'BytecodeGenerator'; did you mean
    'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlow.unwindHandler' has no cute function yet. "
        "Qt's 'BytecodeGenerator::ExceptionHandler "
        "*QV4::Compiler::ControlFlow::unwindHandler()': the compiler "
        "refuses its ritual as it would be written here: use of undeclared "
        "identifier 'BytecodeGenerator'; did you mean "
        "'CuteQV4_Compiler_ControlFlow::BytecodeGenerator'?.")
