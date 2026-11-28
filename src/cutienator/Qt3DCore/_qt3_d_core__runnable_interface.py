"""
Qt3DCore::RunnableInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/task_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::RunnableInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QRunnable
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RunnableInterface(QRunnable):
  """
  The cute side of Qt's Qt3DCore::RunnableInterface: a plain Python object
  standing in front of one C++ Qt3DCore::RunnableInterface.

  It is built on the cute 'QRunnable', as Qt's Qt3DCore::RunnableInterface is
  built on Qt's QRunnable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::RunnableInterface that has a ritual and
  that Python can call so far, 8 names in all: 'isRequired', 'run', 'id',
  'setId', 'setReserved', 'reserved', 'setPooler', 'type'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::RunnableInterface::~RunnableInterface()': the destructor:
    Python never removes a C++ Qt3DCore::RunnableInterface.

  What to expect
  --------------

  - The C++ Qt3DCore::RunnableInterface is created at the first use, not by
    'Qt3DCore::RunnableInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::RunnableInterface.
  """

  #  The enums Qt writes inside Qt3DCore::RunnableInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RunnableType(CuteNum, scoped=True):
    """
    The enum 'Qt3DCore::RunnableInterface::RunnableType' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    AspectTask = Kee[int](0)
    SyncTask = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::RunnableInterface'

  #  A C++ Qt3DCore::RunnableInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_RunnableInterface'

  #  The functions Qt calls itself that Qt3DCore::RunnableInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isRequired': (
          ('_ZNK8Qt3DCore17RunnableInterface10isRequiredEv',
           ('bool', 'number', ''),
           ()),
      ),
      'id': (
          ('_ZN8Qt3DCore17RunnableInterface2idEv',
           ('int', 'number', ''),
           ()),
      ),
      'setId': (
          ('_ZN8Qt3DCore17RunnableInterface5setIdEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setReserved': (
          ('_ZN8Qt3DCore17RunnableInterface11setReservedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'reserved': (
          ('_ZN8Qt3DCore17RunnableInterface8reservedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setPooler': (
          ('_ZN8Qt3DCore17RunnableInterface9setPoolerEPNS_13QThreadPoolerE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QThreadPooler'),
           )),
      ),
      'type': (
          ('_ZNK8Qt3DCore17RunnableInterface4typeEv',
           ('int', 'enum',
            'Qt3DCore:Qt3DCore.RunnableInterface.RunnableType'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::RunnableInterface::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#isRequired
    """
    #  bool Qt3DCore::RunnableInterface::isRequired() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore17RunnableInterface10isRequiredEv',
    )

  def type(self) -> RunnableType:
    """
    Calls Qt's 'RunnableType Qt3DCore::RunnableInterface::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#type

    Returns
    -------

    RunnableType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RunnableType(number)'
      gives.
    """
    #  RunnableType Qt3DCore::RunnableInterface::type() const
    return RunnableInterface.RunnableType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore17RunnableInterface4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setId(self, id: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::RunnableInterface::setId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#setId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void Qt3DCore::RunnableInterface::setId(int id)
    self.uglySide.call('ritual_ZN8Qt3DCore17RunnableInterface5setIdEi', id)

  @overload(bool)
  def setReserved(self, reserved: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::RunnableInterface::setReserved(bool
    reserved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#setReserved

    Parameters
    ----------

    reserved : bool
      Passed on as it is.
    """
    #  void Qt3DCore::RunnableInterface::setReserved(bool reserved)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore17RunnableInterface11setReservedEb', reserved,
    )

  @overload(WAIT['Qt3DCore.QThreadPooler'])
  @overload(NoneType)
  def setPooler(self, pooler: Optional[Qt3DCore.QThreadPooler]) -> None:
    """
    Calls Qt's 'void Qt3DCore::RunnableInterface::setPooler(QThreadPooler
    *pooler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#setPooler

    Parameters
    ----------

    pooler : Optional[Qt3DCore.QThreadPooler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::RunnableInterface::setPooler(QThreadPooler *pooler)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore17RunnableInterface9setPoolerEPNS_13QThreadPoole'
        'rE',
        self._addressOf(pooler),
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
    Calls Qt's 'void Qt3DCore::RunnableInterface::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#run
    """
    #  void Qt3DCore::RunnableInterface::run()
    self.uglySide.call('ritual_ZN8Qt3DCore17RunnableInterface3runEv')

  def id(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::RunnableInterface::id()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#id
    """
    #  int Qt3DCore::RunnableInterface::id()
    return self.uglySide.call('ritual_ZN8Qt3DCore17RunnableInterface2idEv')

  def reserved(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::RunnableInterface::reserved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-runnableinterface.html#reserved
    """
    #  bool Qt3DCore::RunnableInterface::reserved()
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore17RunnableInterface8reservedEv',
    )
