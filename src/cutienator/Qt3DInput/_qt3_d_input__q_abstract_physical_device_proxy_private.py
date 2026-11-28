"""
Qt3DInput::QAbstractPhysicalDeviceProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::QAbstractPhysicalDeviceProxyPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPhysicalDeviceProxyPrivate(Qt3DInput.QAbstractPhysicalDevicePrivate):
  """
  The cute side of Qt's Qt3DInput::QAbstractPhysicalDeviceProxyPrivate: a
  plain Python object standing in front of one C++
  Qt3DInput::QAbstractPhysicalDeviceProxyPrivate.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevicePrivate', as
  Qt's Qt3DInput::QAbstractPhysicalDeviceProxyPrivate is built on Qt's
  Qt3DInput::QAbstractPhysicalDevicePrivate, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractPhysicalDeviceProxyPrivate that
  has a ritual and that Python can call so far, 4 names in all: 'q_func',
  'setDevice', 'resetDevice', 'setStatus'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::
    ~QAbstractPhysicalDeviceProxyPrivate()': the destructor: Python never
    removes a C++ Qt3DInput::QAbstractPhysicalDeviceProxyPrivate.
  - Qt's 'const QAbstractPhysicalDeviceProxy
    *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func() const': takes
    in Python what 'QAbstractPhysicalDeviceProxy
    *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractPhysicalDeviceProxyPrivate is created at the
    first use, not by 'Qt3DInput::QAbstractPhysicalDeviceProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractPhysicalDeviceProxyPrivate'

  #  A C++ Qt3DInput::QAbstractPhysicalDeviceProxyPrivate Python makes is of
  #  a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAbstractPhysicalDeviceProxyPrivate'

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

  @overload(WAIT['Qt3DInput.QAbstractPhysicalDevice'])
  @overload(NoneType)
  def setDevice(
      self,
      device: Optional[Qt3DInput.QAbstractPhysicalDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setDevice(
    QAbstractPhysicalDevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxyprivate.html

    Parameters
    ----------

    device : Optional[Qt3DInput.QAbstractPhysicalDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setDevice(
    #      QAbstractPhysicalDevice *device)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate9setDevice'
        'EPNS_23QAbstractPhysicalDeviceE',
        self._addressOf(device),
    )

  @overload(Qt3DInput.QAbstractPhysicalDeviceProxy.DeviceStatus)
  def setStatus(
      self,
      status: Qt3DInput.QAbstractPhysicalDeviceProxy.DeviceStatus,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setStatus(
    QAbstractPhysicalDeviceProxy::DeviceStatus status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxyprivate.html

    Parameters
    ----------

    status : Qt3DInput.QAbstractPhysicalDeviceProxy.DeviceStatus
      Passed on as its number.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setStatus(
    #      QAbstractPhysicalDeviceProxy::DeviceStatus status)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate9setStatus'
        'ENS_28QAbstractPhysicalDeviceProxy12DeviceStatusE',
        status.value,
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

  @overload(str)
  def __init__(self, deviceName: str) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::
    QAbstractPhysicalDeviceProxyPrivate(const QString &deviceName)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxyprivate.html

    Parameters
    ----------

    deviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::
    #      QAbstractPhysicalDeviceProxyPrivate(const QString &deviceName)
    self._noteCreation(
        QAbstractPhysicalDeviceProxyPrivate, lambda: Rituals.call(
            'ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivateC1ERK7'
            'QString',
            deviceName,
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

  def q_func(self) -> Optional[Qt3DInput.QAbstractPhysicalDeviceProxy]:
    """
    Calls Qt's 'QAbstractPhysicalDeviceProxy
    *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxyprivate.html

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDeviceProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDeviceProxy
    #      *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate6q_funcEv',
    )
    return Qt3DInput.QAbstractPhysicalDeviceProxy._cuteAt(address)

  @overload(WAIT['Qt3DInput.QAbstractPhysicalDevice'])
  @overload(NoneType)
  def resetDevice(
      self,
      device: Optional[Qt3DInput.QAbstractPhysicalDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::resetDevice(
    QAbstractPhysicalDevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxyprivate.html

    Parameters
    ----------

    device : Optional[Qt3DInput.QAbstractPhysicalDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::resetDevice(
    #      QAbstractPhysicalDevice *device)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate11resetDev'
        'iceEPNS_23QAbstractPhysicalDeviceE',
        self._addressOf(device),
    )
