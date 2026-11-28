"""
QQmlTableInstanceModelIncubationTask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlTableInstanceModelIncubationTask to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QQmlIncubator
from . import QQDMIncubationTask

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


class QQmlTableInstanceModelIncubationTask(QQDMIncubationTask):
  """
  The cute side of Qt's QQmlTableInstanceModelIncubationTask: a plain Python
  object standing in front of one C++ QQmlTableInstanceModelIncubationTask.

  It is built on the cute 'QQDMIncubationTask', as Qt's
  QQmlTableInstanceModelIncubationTask is built on Qt's QQDMIncubationTask,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTableInstanceModelIncubationTask that has a
  ritual and that Python can call so far, 2 names in all: 'statusChanged',
  'setInitialState'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'QQDMIncubationTask.

  What to expect
  --------------

  - The C++ QQmlTableInstanceModelIncubationTask is created at the first use,
    not by 'QQmlTableInstanceModelIncubationTask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTableInstanceModelIncubationTask.
  - Each name of Qt's QQmlTableInstanceModelIncubationTask that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QQmlTableInstanceModelIncubationTask'

  #  A C++ QQmlTableInstanceModelIncubationTask Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTableInstanceModelIncubationTask'

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
  def setInitialState(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModelIncubationTask::setInitialState(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodelincubationtask.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTableInstanceModelIncubationTask::setInitialState(QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN36QQmlTableInstanceModelIncubationTask15setInitialStateEP'
        '7QObject',
        self._addressOf(object, 'QObject'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlTableInstanceModelIncubationTask::
    QQmlTableInstanceModelIncubationTask(QQmlTableInstanceModel
    *tableInstanceModel, QQmlDelegateModelItem *modelItemToIncubate,
    IncubationMode mode)': leans on
    'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModelItem*,
    QObject*, QQmlDelegateModel::DelegateModelAccess)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTableInstanceModelIncubationTask.__init__' has no cute "
        "function yet. Qt's "
        "'QQmlTableInstanceModelIncubationTask::QQmlTableInstanceModelIncuba"
        "tionTask(QQmlTableInstanceModel *tableInstanceModel, "
        "QQmlDelegateModelItem *modelItemToIncubate, IncubationMode mode)': "
        "leans on "
        "'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModel"
        "Item*, QObject*, QQmlDelegateModel::DelegateModelAccess)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
  def statusChanged(self, status: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModelIncubationTask::statusChanged(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodelincubationtask.html

    Parameters
    ----------

    status : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQmlTableInstanceModelIncubationTask::statusChanged(Status
    #      status)
    ritual = (
        'ritual_ZN36QQmlTableInstanceModelIncubationTask13statusChangedEN13'
        'QQmlIncubator6StatusE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QQmlTableInstanceModelIncubationTask13statusChang'
          'edEN13QQmlIncubator6StatusE')
    self.uglySide.call(ritual, status.value)
