"""
QV4::Moth::VME binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4vme_moth_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Moth::VME to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class VME(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Moth::VME: a plain Python object standing in
  front of one C++ QV4::Moth::VME.

  C++ hands a QV4::Moth::VME around as a copy, so every C++ QV4::Moth::VME
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::Moth::VME yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Moth::VME::~VME()': the destructor: Python removes its C++
    QV4::Moth::VME by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 4 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::Moth::VME is created at the first use, not by
    'QV4::Moth::VME(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Moth::VME back gives a copy the ritual made for
    Python, in a new cute QV4::Moth::VME.
  - Each name of Qt's QV4::Moth::VME that has no cute function yet, 'exec',
    'interpret', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QV4::Moth::VME, each a class in here as in
  #  C++.

  class ExecData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Moth::VME::ExecData: a plain Python object
    standing in front of one C++ QV4::Moth::VME::ExecData.

    C++ hands a QV4::Moth::VME::ExecData around as a copy, so every C++
    QV4::Moth::VME::ExecData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QV4::Moth::VME::ExecData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Moth::VME::ExecData::~ExecData()': the destructor: Python
      removes its C++ QV4::Moth::VME::ExecData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Moth::VME::ExecData is created at the first use, not by
      'QV4::Moth::VME::ExecData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Moth::VME::ExecData back gives a copy the
      ritual made for Python, in a new cute QV4::Moth::VME::ExecData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Moth::VME::ExecData'

    #  Qt's '~QV4::Moth::VME::ExecData()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Moth::VME::ExecData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV44Moth3VME8ExecDataD1Ev'

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
  __qt_class__ = 'QV4::Moth::VME'

  #  Qt's '~QV4::Moth::VME()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::Moth::VME behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV44Moth3VMED1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def exec(*__, **_) -> Never:
    """
    - Qt's 'void QV4::Moth::VME::exec(MetaTypesStackFrame *frame,
      ExecutionEngine *engine)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'qt_v4ResolvePendingBreakpointsHook'.
    - Qt's 'QV4::ReturnedValue QV4::Moth::VME::exec(JSTypesStackFrame *frame,
      ExecutionEngine *engine)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'qt_v4ResolvePendingBreakpointsHook'.
    """
    raise NotImplementedError(
        "'QV4.Moth.VME.exec' has no cute function yet. Qt's 'void "
        "QV4::Moth::VME::exec(MetaTypesStackFrame *frame, ExecutionEngine "
        "*engine)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qt_v4ResolvePendingBreakpointsHook'. Qt's "
        "'QV4::ReturnedValue QV4::Moth::VME::exec(JSTypesStackFrame *frame, "
        "ExecutionEngine *engine)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qt_v4ResolvePendingBreakpointsHook'.")

  @staticmethod
  def interpret(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QV4::Moth::VME::interpret(JSTypesStackFrame
    *frame, ExecutionEngine *engine, const char *codeEntry)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared label 'op_byte_Ret'.
    """
    raise NotImplementedError(
        "'QV4.Moth.VME.interpret' has no cute function yet. Qt's "
        "'QV4::ReturnedValue QV4::Moth::VME::interpret(JSTypesStackFrame "
        "*frame, ExecutionEngine *engine, const char *codeEntry)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared label 'op_byte_Ret'."
    )
