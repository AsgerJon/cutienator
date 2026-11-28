"""
Qt3DCore::SyncTaskRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/task_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::SyncTaskRunnable to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SyncTaskRunnable(Qt3DCore.RunnableInterface):
  """
  The cute side of Qt's Qt3DCore::SyncTaskRunnable: a plain Python object
  standing in front of one C++ Qt3DCore::SyncTaskRunnable.

  It is built on the cute 'Qt3DCore::RunnableInterface', as Qt's
  Qt3DCore::SyncTaskRunnable is built on Qt's Qt3DCore::RunnableInterface,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::SyncTaskRunnable that has a ritual and
  that Python can call so far, 8 names in all: 'isRequired', 'run',
  'setPooler', 'setReserved', 'reserved', 'id', 'setId', 'type'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::SyncTaskRunnable::SyncTaskRunnable(
    QAbstractAspectJobManager::JobFunction func, void *arg, QAtomicInt
    *atomicCount)': takes a type Python has no way to hand over yet.
  - Qt's 'Qt3DCore::SyncTaskRunnable::~SyncTaskRunnable()': the destructor:
    Python never removes a C++ Qt3DCore::SyncTaskRunnable.

  What to expect
  --------------

  - The C++ Qt3DCore::SyncTaskRunnable is created at the first use, not by
    'Qt3DCore::SyncTaskRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::SyncTaskRunnable.
  - Each name of Qt's Qt3DCore::SyncTaskRunnable that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::SyncTaskRunnable'

  #  A C++ Qt3DCore::SyncTaskRunnable Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_SyncTaskRunnable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::SyncTaskRunnable::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#isRequired
    """
    #  bool Qt3DCore::SyncTaskRunnable::isRequired() const
    ritual = 'ritual_ZNK8Qt3DCore16SyncTaskRunnable10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore16SyncTaskRunnable10isRequiredEv'
    return self.uglySide.call(ritual)

  def type(self) -> Qt3DCore.RunnableInterface.RunnableType:
    """
    Calls Qt's 'RunnableType Qt3DCore::SyncTaskRunnable::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#type

    Returns
    -------

    Qt3DCore.RunnableInterface.RunnableType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.RunnableInterface.RunnableType(number)' gives.
    """
    #  RunnableType Qt3DCore::SyncTaskRunnable::type() const
    ritual = 'ritual_ZNK8Qt3DCore16SyncTaskRunnable4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore16SyncTaskRunnable4typeEv'
    return Qt3DCore.RunnableInterface.RunnableType(self.uglySide.call(
        ritual,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QThreadPooler'])
  @overload(NoneType)
  def setPooler(self, pooler: Optional[Qt3DCore.QThreadPooler]) -> None:
    """
    Calls Qt's 'void Qt3DCore::SyncTaskRunnable::setPooler(QThreadPooler
    *pooler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#setPooler

    Parameters
    ----------

    pooler : Optional[Qt3DCore.QThreadPooler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::SyncTaskRunnable::setPooler(QThreadPooler *pooler)
    ritual = (
        'ritual_ZN8Qt3DCore16SyncTaskRunnable9setPoolerEPNS_13QThreadPooler'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore16SyncTaskRunnable9setPoolerEPNS_13QThread'
          'PoolerE')
    self.uglySide.call(ritual, self._addressOf(pooler))

  @overload(bool)
  def setReserved(self, reserved: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::SyncTaskRunnable::setReserved(bool reserved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#setReserved

    Parameters
    ----------

    reserved : bool
      Passed on as it is.
    """
    #  void Qt3DCore::SyncTaskRunnable::setReserved(bool reserved)
    ritual = 'ritual_ZN8Qt3DCore16SyncTaskRunnable11setReservedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16SyncTaskRunnable11setReservedEb'
    self.uglySide.call(ritual, reserved)

  @overload(int)
  def setId(self, id: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::SyncTaskRunnable::setId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#setId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void Qt3DCore::SyncTaskRunnable::setId(int id)
    ritual = 'ritual_ZN8Qt3DCore16SyncTaskRunnable5setIdEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16SyncTaskRunnable5setIdEi'
    self.uglySide.call(ritual, id)

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
    Qt's 'Qt3DCore::SyncTaskRunnable::SyncTaskRunnable(
    QAbstractAspectJobManager::JobFunction func, void *arg, QAtomicInt
    *atomicCount)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.SyncTaskRunnable.__init__' has no cute function yet. "
        "Qt's "
        "'Qt3DCore::SyncTaskRunnable::SyncTaskRunnable(QAbstractAspectJobMan"
        "ager::JobFunction func, void *arg, QAtomicInt *atomicCount)': "
        "takes a type Python has no way to hand over yet.")

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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::SyncTaskRunnable::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#run
    """
    #  void Qt3DCore::SyncTaskRunnable::run()
    ritual = 'ritual_ZN8Qt3DCore16SyncTaskRunnable3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16SyncTaskRunnable3runEv'
    self.uglySide.call(ritual)

  def reserved(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::SyncTaskRunnable::reserved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#reserved
    """
    #  bool Qt3DCore::SyncTaskRunnable::reserved()
    ritual = 'ritual_ZN8Qt3DCore16SyncTaskRunnable8reservedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16SyncTaskRunnable8reservedEv'
    return self.uglySide.call(ritual)

  def id(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::SyncTaskRunnable::id()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-synctaskrunnable.html#id
    """
    #  int Qt3DCore::SyncTaskRunnable::id()
    ritual = 'ritual_ZN8Qt3DCore16SyncTaskRunnable2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16SyncTaskRunnable2idEv'
    return self.uglySide.call(ritual)
