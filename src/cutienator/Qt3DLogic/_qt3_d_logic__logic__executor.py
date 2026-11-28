"""
Qt3DLogic::Logic::Executor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/6.12.0/Qt3DLogic/private/executor_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DLogic::Logic::Executor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Executor(QObject):
  """
  The cute side of Qt's Qt3DLogic::Logic::Executor: a plain Python object
  standing in front of one C++ Qt3DLogic::Logic::Executor.

  It is built on the cute 'QObject', as Qt's Qt3DLogic::Logic::Executor is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::Logic::Executor that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject', 'setScene'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DLogic::Logic::Executor::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DLogic::Logic::Executor::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void Qt3DLogic::Logic::Executor::processLogicFrameUpdates(const
    QList<Qt3DCore::QNodeId> &nodeIds, float dt)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 not a gap; 1 leans on 'Qt3DLogic; 1
  leans on 'vtable for Qt3DLogic.

  What to expect
  --------------

  - The C++ Qt3DLogic::Logic::Executor is created at the first use, not by
    'Qt3DLogic::Logic::Executor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::Logic::Executor.
  - Qt tells when it has removed the C++ Qt3DLogic::Logic::Executor. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DLogic::Logic::Executor that has no cute function
    yet, '__init__', 'processLogicFrameUpdates', holds a function that raises
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
  __qt_class__ = 'Qt3DLogic::Logic::Executor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DLogic::Logic::Executor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-executor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DLogic::Logic::Executor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DLogic5Logic8Executor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Executor::setScene(Qt3DCore::QScene
    *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-executor.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::Executor::setScene(Qt3DCore::QScene *scene)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic8Executor8setSceneEPN8Qt3DCore6QSceneE',
        self._addressOf(scene),
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
    Qt's 'Qt3DLogic::Logic::Executor::Executor(QObject *parent)': leans on
    'vtable for Qt3DLogic::Logic::Executor', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DLogic.Logic.Executor.__init__' has no cute function yet. Qt's "
        "'Qt3DLogic::Logic::Executor::Executor(QObject *parent)': leans on "
        "'vtable for Qt3DLogic::Logic::Executor', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
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

  @staticmethod
  def processLogicFrameUpdates(*__, **_) -> Never:
    """
    Qt's 'void Qt3DLogic::Logic::Executor::processLogicFrameUpdates(const
    QList<Qt3DCore::QNodeId> &nodeIds, float dt)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DLogic.Logic.Executor.processLogicFrameUpdates' has no cute "
        "function yet. Qt's 'void "
        "Qt3DLogic::Logic::Executor::processLogicFrameUpdates(const "
        "QList<Qt3DCore::QNodeId> &nodeIds, float dt)': takes a type Python "
        "has no way to hand over yet.")
