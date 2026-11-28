"""
QQuickUntypedDeferredPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdeferredpointer_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickUntypedDeferredPointer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuickUntypedDeferredPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickUntypedDeferredPointer: a plain Python object
  standing in front of one C++ QQuickUntypedDeferredPointer.

  What exists
  -----------

  Every function of Qt's QQuickUntypedDeferredPointer that has a ritual and
  that Python can call so far, 5 names in all: 'clearDeferredState',
  'wasExecuted', 'setExecuted', 'isExecuting', 'setExecuting'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlComponentPrivate::DeferredState
    *QQuickUntypedDeferredPointer::deferredState() const': gives
    'std::vector<QQmlComponentPrivate::ConstructionState>', which has no cute
    class yet.
  - Qt's 'QQuickUntypedDeferredPointer::QQuickUntypedDeferredPointer(void
    *v)': names 'void', which has no cute class yet.
  - Qt's 'QQuickUntypedDeferredPointer
    &QQuickUntypedDeferredPointer::operator=(void *v)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QQuickUntypedDeferredPointer::~QQuickUntypedDeferredPointer()': the
    destructor: Python never removes a C++ QQuickUntypedDeferredPointer.
  - Qt's 'void *QQuickUntypedDeferredPointer::data() const': gives 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQuickUntypedDeferredPointer is created at the first use, not by
    'QQuickUntypedDeferredPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUntypedDeferredPointer.
  - Each name of Qt's QQuickUntypedDeferredPointer that has no cute function
    yet, 'data', 'deferredState', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUntypedDeferredPointer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def wasExecuted(self) -> bool:
    """
    Calls Qt's 'bool QQuickUntypedDeferredPointer::wasExecuted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html#wasExecuted
    """
    #  bool QQuickUntypedDeferredPointer::wasExecuted() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickUntypedDeferredPointer11wasExecutedEv',
    )

  def isExecuting(self) -> bool:
    """
    Calls Qt's 'bool QQuickUntypedDeferredPointer::isExecuting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html#isExecuting
    """
    #  bool QQuickUntypedDeferredPointer::isExecuting() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickUntypedDeferredPointer11isExecutingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setExecuted(self) -> None:
    """
    Calls Qt's 'void QQuickUntypedDeferredPointer::setExecuted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html#setExecuted
    """
    #  void QQuickUntypedDeferredPointer::setExecuted()
    self.uglySide.call(
        'ritual_ZN28QQuickUntypedDeferredPointer11setExecutedEv',
    )

  @overload(bool)
  def setExecuting(self, b: bool) -> bool:
    """
    Calls Qt's 'bool QQuickUntypedDeferredPointer::setExecuting(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html#setExecuting

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  bool QQuickUntypedDeferredPointer::setExecuting(bool b)
    return self.uglySide.call(
        'ritual_ZN28QQuickUntypedDeferredPointer12setExecutingEb', b,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickUntypedDeferredPointer::QQuickUntypedDeferredPointer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html
    """
    #  QQuickUntypedDeferredPointer::QQuickUntypedDeferredPointer()
    self._noteCreation(QQuickUntypedDeferredPointer, lambda: Rituals.call(
        'ritual_ZN28QQuickUntypedDeferredPointerC1Ev',
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

  def clearDeferredState(self) -> None:
    """
    Calls Qt's 'void QQuickUntypedDeferredPointer::clearDeferredState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuntypeddeferredpointer.html
    """
    #  void QQuickUntypedDeferredPointer::clearDeferredState()
    self.uglySide.call(
        'ritual_ZN28QQuickUntypedDeferredPointer18clearDeferredStateEv',
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'void *QQuickUntypedDeferredPointer::data() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickUntypedDeferredPointer.data' has no cute function yet. Qt's "
        "'void *QQuickUntypedDeferredPointer::data() const': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def deferredState(*__, **_) -> Never:
    """
    Qt's 'QQmlComponentPrivate::DeferredState
    *QQuickUntypedDeferredPointer::deferredState() const': gives
    'std::vector<QQmlComponentPrivate::ConstructionState>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickUntypedDeferredPointer.deferredState' has no cute function "
        "yet. Qt's 'QQmlComponentPrivate::DeferredState "
        "*QQuickUntypedDeferredPointer::deferredState() const': gives "
        "'std::vector<QQmlComponentPrivate::ConstructionState>', which has "
        "no cute class yet.")
