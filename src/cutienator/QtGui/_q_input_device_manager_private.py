"""
QInputDeviceManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinputdevicemanager_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QInputDeviceManagerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QInputDeviceManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDeviceManagerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QInputDeviceManagerPrivate: a plain Python object
  standing in front of one C++ QInputDeviceManagerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QInputDeviceManagerPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QInputDeviceManagerPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'get',
  'deviceCount', 'setDeviceCount'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QInputDeviceManager *QInputDeviceManagerPrivate::q_func()
    const': takes in Python what 'QInputDeviceManager
    *QInputDeviceManagerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QInputDeviceManagerPrivate is created at the first use, not by
    'QInputDeviceManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputDeviceManagerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QInputDeviceManager)
  @overload(NoneType)
  def get(
      mgr: Optional[QInputDeviceManager],
  ) -> Optional[QInputDeviceManagerPrivate]:
    """
    Calls Qt's 'QInputDeviceManagerPrivate
    *QInputDeviceManagerPrivate::get(QInputDeviceManager *mgr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanagerprivate.html#get

    Parameters
    ----------

    mgr : Optional[QInputDeviceManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QInputDeviceManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDeviceManagerPrivate
    #      *QInputDeviceManagerPrivate::get(QInputDeviceManager *mgr)
    address = Rituals.call(
        'ritual_ZN26QInputDeviceManagerPrivate3getEP19QInputDeviceManager',
        CuteMixin._addressOf(mgr),
    )
    return QInputDeviceManagerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputDeviceManagerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QInputDeviceManager.DeviceType)
  def deviceCount(self, type: QInputDeviceManager.DeviceType) -> int:
    """
    Calls Qt's 'int
    QInputDeviceManagerPrivate::deviceCount(QInputDeviceManager::DeviceType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanagerprivate.html#deviceCount

    Parameters
    ----------

    type : QInputDeviceManager.DeviceType
      Passed on as its number.
    """
    #  int QInputDeviceManagerPrivate::deviceCount(QInputDeviceManager::
    #      DeviceType type) const
    return self.uglySide.call(
        'ritual_ZNK26QInputDeviceManagerPrivate11deviceCountEN19QInputDevic'
        'eManager10DeviceTypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QInputDeviceManager.DeviceType, int)
  def setDeviceCount(
      self,
      type: QInputDeviceManager.DeviceType,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    QInputDeviceManagerPrivate::setDeviceCount(QInputDeviceManager::
    DeviceType type, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanagerprivate.html#setDeviceCount

    Parameters
    ----------

    type : QInputDeviceManager.DeviceType
      Passed on as its number.

    count : int
      Passed on as it is.
    """
    #  void QInputDeviceManagerPrivate::setDeviceCount(QInputDeviceManager::
    #      DeviceType type, int count)
    self.uglySide.call(
        'ritual_ZN26QInputDeviceManagerPrivate14setDeviceCountEN19QInputDev'
        'iceManager10DeviceTypeEi',
        type.value, count,
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

  def q_func(self) -> Optional[QInputDeviceManager]:
    """
    Calls Qt's 'QInputDeviceManager *QInputDeviceManagerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanagerprivate.html#q_func

    Returns
    -------

    Optional[QInputDeviceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDeviceManager *QInputDeviceManagerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QInputDeviceManagerPrivate6q_funcEv',
    )
    return QInputDeviceManager._cuteAt(address)
