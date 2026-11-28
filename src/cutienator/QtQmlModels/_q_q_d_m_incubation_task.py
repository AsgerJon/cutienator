"""
QQDMIncubationTask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQDMIncubationTask to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QQmlIncubator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQDMIncubationTask(QQmlIncubator):
  """
  The cute side of Qt's QQDMIncubationTask: a plain Python object standing in
  front of one C++ QQDMIncubationTask.

  It is built on the cute 'QQmlIncubator', as Qt's QQDMIncubationTask is
  built on Qt's QQmlIncubator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQDMIncubationTask that has a ritual and that Python
  can call so far, 2 names in all: 'statusChanged', 'setInitialState'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlListCompositor.

  What to expect
  --------------

  - The C++ QQDMIncubationTask is created at the first use, not by
    'QQDMIncubationTask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQDMIncubationTask.
  - Each name of Qt's QQDMIncubationTask that has no cute function yet,
    '__init__', 'initializeRequiredProperties', holds a function that raises
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
  __qt_class__ = 'QQDMIncubationTask'

  #  A C++ QQDMIncubationTask Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQDMIncubationTask'

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

  @overload(QObject)
  @overload(NoneType)
  def setInitialState(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQDMIncubationTask::setInitialState(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqdmincubationtask.html#setInitialState

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQDMIncubationTask::setInitialState(QObject *a0)
    ritual = 'ritual_ZN18QQDMIncubationTask15setInitialStateEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQDMIncubationTask15setInitialStateEP7QObject'
    self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))

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
    Qt's 'QQDMIncubationTask::QQDMIncubationTask(QQmlDelegateModelPrivate *l,
    IncubationMode mode)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQDMIncubationTask.__init__' has no cute function yet. Qt's "
        "'QQDMIncubationTask::QQDMIncubationTask(QQmlDelegateModelPrivate "
        "*l, IncubationMode mode)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QQmlIncubator.Status)
  def statusChanged(self, a0: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void QQDMIncubationTask::statusChanged(Status a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqdmincubationtask.html#statusChanged

    Parameters
    ----------

    a0 : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQDMIncubationTask::statusChanged(Status a0)
    self.uglySide.call(
        'ritual_ZN18QQDMIncubationTask13statusChangedEN13QQmlIncubator6Stat'
        'usE',
        a0.value,
    )

  @staticmethod
  def initializeRequiredProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModelItem
    *modelItemToIncubate, QObject *object,
    QQmlDelegateModel::DelegateModelAccess access)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    type 'const RequiredPropertiesAndTarget' does not provide a call
    operator.
    """
    raise NotImplementedError(
        "'QQDMIncubationTask.initializeRequiredProperties' has no cute "
        "function yet. Qt's 'void "
        "QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModelI"
        "tem *modelItemToIncubate, QObject *object, "
        "QQmlDelegateModel::DelegateModelAccess access)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: type 'const RequiredPropertiesAndTarget' does not "
        "provide a call operator.")
