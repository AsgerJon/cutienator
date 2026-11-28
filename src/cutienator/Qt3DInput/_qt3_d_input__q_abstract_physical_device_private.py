"""
Qt3DInput::QAbstractPhysicalDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QAbstractPhysicalDevicePrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAbstractPhysicalDevicePrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DInput::QAbstractPhysicalDevicePrivate: a plain
  Python object standing in front of one C++
  Qt3DInput::QAbstractPhysicalDevicePrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DInput::QAbstractPhysicalDevicePrivate is built on Qt's
  Qt3DCore::QNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractPhysicalDevicePrivate that has a
  ritual and that Python can call so far, 3 names in all: 'q_func',
  'postAxisEvent', 'postButtonEvent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::QAbstractPhysicalDevicePrivate::
    ~QAbstractPhysicalDevicePrivate()': the destructor: Python never removes
    a C++ Qt3DInput::QAbstractPhysicalDevicePrivate.
  - Qt's 'const QAbstractPhysicalDevice
    *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func() const': takes in
    Python what 'QAbstractPhysicalDevice
    *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractPhysicalDevicePrivate is created at the first
    use, not by 'Qt3DInput::QAbstractPhysicalDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAbstractPhysicalDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractPhysicalDevicePrivate'

  #  A C++ Qt3DInput::QAbstractPhysicalDevicePrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAbstractPhysicalDevicePrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAbstractPhysicalDevicePrivate::
    QAbstractPhysicalDevicePrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceprivate.html
    """
    #  Qt3DInput::QAbstractPhysicalDevicePrivate::
    #      QAbstractPhysicalDevicePrivate()
    self._noteCreation(QAbstractPhysicalDevicePrivate, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput30QAbstractPhysicalDevicePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DInput.QAbstractPhysicalDevice]:
    """
    Calls Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceprivate.html

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevice
    #      *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput30QAbstractPhysicalDevicePrivate6q_funcEv',
    )
    return Qt3DInput.QAbstractPhysicalDevice._cuteAt(address)

  @overload(int, float)
  def postAxisEvent(self, axis: int, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDevicePrivate::postAxisEvent(int axis, qreal
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceprivate.html

    Parameters
    ----------

    axis : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAbstractPhysicalDevicePrivate::postAxisEvent(int
    #      axis, qreal value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput30QAbstractPhysicalDevicePrivate13postAxisEvent'
        'Eid',
        axis, value,
    )

  @overload(int, float)
  def postButtonEvent(self, button: int, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDevicePrivate::postButtonEvent(int button,
    qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceprivate.html

    Parameters
    ----------

    button : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAbstractPhysicalDevicePrivate::postButtonEvent(int
    #      button, qreal value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput30QAbstractPhysicalDevicePrivate15postButtonEve'
        'ntEid',
        button, value,
    )
