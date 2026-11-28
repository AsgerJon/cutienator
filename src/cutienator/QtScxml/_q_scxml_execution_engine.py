"""
QScxmlExecutionEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutionEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlExecutionEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlExecutionEngine: a plain Python object standing
  in front of one C++ QScxmlExecutionEngine.

  What exists
  -----------

  No function of Qt's QScxmlExecutionEngine yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 5 functions Qt declares: 2 forbidden; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QScxmlExecutionEngine is created at the first use, not by
    'QScxmlExecutionEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlExecutionEngine.
  - Each name of Qt's QScxmlExecutionEngine that has no cute function yet,
    'execute', 'step', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutionEngine'

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

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def __init__(self, stateMachine: Optional[QScxmlStateMachine]) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlExecutionEngine::QScxmlExecutionEngine(QScxmlStateMachine
    *stateMachine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutionengine.html#QScxmlExecutionEngine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlExecutionEngine::QScxmlExecutionEngine(QScxmlStateMachine
    #      *stateMachine)
    self._noteCreation(QScxmlExecutionEngine, lambda: Rituals.call(
        'ritual_ZN21QScxmlExecutionEngineC1EP18QScxmlStateMachine',
        self._addressOf(stateMachine),
    ))

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
  def execute(*__, **_) -> Never:
    """
    Qt's 'bool
    QScxmlExecutionEngine::execute(QScxmlExecutableContent::ContainerId ip,
    const QVariant &extraData)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'ContainerId'; did you mean 'QScxmlExecutableContent::ContainerId'?.
    """
    raise NotImplementedError(
        "'QScxmlExecutionEngine.execute' has no cute function yet. Qt's "
        "'bool "
        "QScxmlExecutionEngine::execute(QScxmlExecutableContent::ContainerId"
        " ip, const QVariant &extraData)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ContainerId'; did you mean "
        "'QScxmlExecutableContent::ContainerId'?.")

  @staticmethod
  def step(*__, **_) -> Never:
    """
    Qt's 'const QScxmlExecutableContent::InstructionId
    *QScxmlExecutionEngine::step(const QScxmlExecutableContent::InstructionId
    *ip, bool *ok)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'InstructionId'; did you mean 'QScxmlExecutableContent::InstructionId'?.
    """
    raise NotImplementedError(
        "'QScxmlExecutionEngine.step' has no cute function yet. Qt's 'const "
        "QScxmlExecutableContent::InstructionId "
        "*QScxmlExecutionEngine::step(const "
        "QScxmlExecutableContent::InstructionId *ip, bool *ok)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'InstructionId'; "
        "did you mean 'QScxmlExecutableContent::InstructionId'?.")
