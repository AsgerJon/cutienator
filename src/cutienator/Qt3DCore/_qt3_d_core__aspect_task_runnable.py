"""
Qt3DCore::AspectTaskRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/task_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::AspectTaskRunnable to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AspectTaskRunnable(Qt3DCore.RunnableInterface):
  """
  The cute side of Qt's Qt3DCore::AspectTaskRunnable: a plain Python object
  standing in front of one C++ Qt3DCore::AspectTaskRunnable.

  It is built on the cute 'Qt3DCore::RunnableInterface', as Qt's
  Qt3DCore::AspectTaskRunnable is built on Qt's Qt3DCore::RunnableInterface,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::AspectTaskRunnable that has a ritual and
  that Python can call so far, 8 names in all: 'isRequired', 'run',
  'setPooler', 'setReserved', 'reserved', 'id', 'setId', 'type'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::AspectTaskRunnable::~AspectTaskRunnable()': the
    destructor: Python never removes a C++ Qt3DCore::AspectTaskRunnable.

  What to expect
  --------------

  - The C++ Qt3DCore::AspectTaskRunnable is created at the first use, not by
    'Qt3DCore::AspectTaskRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::AspectTaskRunnable.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::AspectTaskRunnable'

  #  A C++ Qt3DCore::AspectTaskRunnable Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_AspectTaskRunnable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::AspectTaskRunnable::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#isRequired
    """
    #  bool Qt3DCore::AspectTaskRunnable::isRequired() const
    ritual = 'ritual_ZNK8Qt3DCore18AspectTaskRunnable10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore18AspectTaskRunnable10isRequiredEv'
    return self.uglySide.call(ritual)

  def type(self) -> Qt3DCore.RunnableInterface.RunnableType:
    """
    Calls Qt's 'RunnableType Qt3DCore::AspectTaskRunnable::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#type

    Returns
    -------

    Qt3DCore.RunnableInterface.RunnableType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.RunnableInterface.RunnableType(number)' gives.
    """
    #  RunnableType Qt3DCore::AspectTaskRunnable::type() const
    ritual = 'ritual_ZNK8Qt3DCore18AspectTaskRunnable4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore18AspectTaskRunnable4typeEv'
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
    Calls Qt's 'void Qt3DCore::AspectTaskRunnable::setPooler(QThreadPooler
    *pooler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#setPooler

    Parameters
    ----------

    pooler : Optional[Qt3DCore.QThreadPooler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::AspectTaskRunnable::setPooler(QThreadPooler *pooler)
    ritual = (
        'ritual_ZN8Qt3DCore18AspectTaskRunnable9setPoolerEPNS_13QThreadPool'
        'erE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore18AspectTaskRunnable9setPoolerEPNS_13QThre'
          'adPoolerE')
    self.uglySide.call(ritual, self._addressOf(pooler))

  @overload(bool)
  def setReserved(self, reserved: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::AspectTaskRunnable::setReserved(bool
    reserved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#setReserved

    Parameters
    ----------

    reserved : bool
      Passed on as it is.
    """
    #  void Qt3DCore::AspectTaskRunnable::setReserved(bool reserved)
    ritual = 'ritual_ZN8Qt3DCore18AspectTaskRunnable11setReservedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18AspectTaskRunnable11setReservedEb'
    self.uglySide.call(ritual, reserved)

  @overload(int)
  def setId(self, id: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::AspectTaskRunnable::setId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#setId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void Qt3DCore::AspectTaskRunnable::setId(int id)
    ritual = 'ritual_ZN8Qt3DCore18AspectTaskRunnable5setIdEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18AspectTaskRunnable5setIdEi'
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

  @overload(WAIT['Qt3DCore.QSystemInformationService'])
  @overload(NoneType)
  def __init__(
      self,
      service: Optional[Qt3DCore.QSystemInformationService],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::AspectTaskRunnable::AspectTaskRunnable(
    QSystemInformationService *service)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html

    Parameters
    ----------

    service : Optional[Qt3DCore.QSystemInformationService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DCore::AspectTaskRunnable::AspectTaskRunnable(
    #      QSystemInformationService *service)
    self._noteCreation(AspectTaskRunnable, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore18AspectTaskRunnableC1EPNS_25QSystemInformationS'
        'erviceE',
        self._addressOf(service),
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::AspectTaskRunnable::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#run
    """
    #  void Qt3DCore::AspectTaskRunnable::run()
    ritual = 'ritual_ZN8Qt3DCore18AspectTaskRunnable3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18AspectTaskRunnable3runEv'
    self.uglySide.call(ritual)

  def reserved(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::AspectTaskRunnable::reserved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#reserved
    """
    #  bool Qt3DCore::AspectTaskRunnable::reserved()
    ritual = 'ritual_ZN8Qt3DCore18AspectTaskRunnable8reservedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18AspectTaskRunnable8reservedEv'
    return self.uglySide.call(ritual)

  def id(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::AspectTaskRunnable::id()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-aspecttaskrunnable.html#id
    """
    #  int Qt3DCore::AspectTaskRunnable::id()
    ritual = 'ritual_ZN8Qt3DCore18AspectTaskRunnable2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore18AspectTaskRunnable2idEv'
    return self.uglySide.call(ritual)
