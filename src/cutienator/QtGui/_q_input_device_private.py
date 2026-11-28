"""
QInputDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinputdevice_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QInputDevicePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QInputDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDevicePrivate(QObjectPrivate):
  """
  The cute side of Qt's QInputDevicePrivate: a plain Python object standing
  in front of one C++ QInputDevicePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QInputDevicePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputDevicePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'registerDevice',
  'unregisterDevice', 'isRegistered', 'fromId',
  'setAvailableVirtualGeometry', 'setCapabilities', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QInputDevice *QInputDevicePrivate::q_func() const': takes in
    Python what 'QInputDevice *QInputDevicePrivate::q_func()' takes.
  - Qt's 'QInputDevicePrivate::~QInputDevicePrivate()': the destructor:
    Python never removes a C++ QInputDevicePrivate.
  - Qt's 'const QInputDevicePrivate *QInputDevicePrivate::get(const
    QInputDevice *q)': takes in Python what 'QInputDevicePrivate
    *QInputDevicePrivate::get(QInputDevice *q)' takes.

  What to expect
  --------------

  - The C++ QInputDevicePrivate is created at the first use, not by
    'QInputDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def registerDevice(dev: Optional[QInputDevice]) -> None:
    """
    Calls Qt's 'void QInputDevicePrivate::registerDevice(const QInputDevice
    *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html#registerDevice

    Parameters
    ----------

    dev : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QInputDevicePrivate::registerDevice(const QInputDevice *dev)
    Rituals.call(
        'ritual_ZN19QInputDevicePrivate14registerDeviceEPK12QInputDevice',
        CuteMixin._addressOf(dev),
    )

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def unregisterDevice(dev: Optional[QInputDevice]) -> None:
    """
    Calls Qt's 'void QInputDevicePrivate::unregisterDevice(const QInputDevice
    *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html#unregisterDevice

    Parameters
    ----------

    dev : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QInputDevicePrivate::unregisterDevice(const QInputDevice *dev)
    Rituals.call(
        'ritual_ZN19QInputDevicePrivate16unregisterDeviceEPK12QInputDevice',
        CuteMixin._addressOf(dev),
    )

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def isRegistered(dev: Optional[QInputDevice]) -> bool:
    """
    Calls Qt's 'bool QInputDevicePrivate::isRegistered(const QInputDevice
    *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html#isRegistered

    Parameters
    ----------

    dev : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QInputDevicePrivate::isRegistered(const QInputDevice *dev)
    return Rituals.call(
        'ritual_ZN19QInputDevicePrivate12isRegisteredEPK12QInputDevice',
        CuteMixin._addressOf(dev),
    )

  @staticmethod
  @overload(int)
  def fromId(systemId: int) -> Optional[QInputDevice]:
    """
    Calls Qt's 'const QInputDevice *QInputDevicePrivate::fromId(qint64
    systemId)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdeviceprivate.html#fromId

    Parameters
    ----------

    systemId : int
      Passed on as it is.

    Returns
    -------

    Optional[QInputDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QInputDevice *QInputDevicePrivate::fromId(qint64 systemId)
    address = Rituals.call(
        'ritual_ZN19QInputDevicePrivate6fromIdEx', systemId,
    )
    return QInputDevice._cuteAt(address)

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def get(q: Optional[QInputDevice]) -> Optional[QInputDevicePrivate]:
    """
    Calls Qt's 'QInputDevicePrivate *QInputDevicePrivate::get(QInputDevice
    *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdeviceprivate.html#get

    Parameters
    ----------

    q : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QInputDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDevicePrivate *QInputDevicePrivate::get(QInputDevice *q)
    address = Rituals.call(
        'ritual_ZN19QInputDevicePrivate3getEP12QInputDevice',
        CuteMixin._addressOf(q),
    )
    return QInputDevicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputDevicePrivate'

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

  @overload(QRect)
  def setAvailableVirtualGeometry(self, a: QRect) -> None:
    """
    Calls Qt's 'void QInputDevicePrivate::setAvailableVirtualGeometry(QRect
    a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html

    Parameters
    ----------

    a : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QInputDevicePrivate::setAvailableVirtualGeometry(QRect a)
    self.uglySide.call(
        'ritual_ZN19QInputDevicePrivate27setAvailableVirtualGeometryE5QRect',
        self._valueOf(a),
    )

  @overload(QInputDevice.Capabilities)
  def setCapabilities(self, c: QInputDevice.Capabilities) -> None:
    """
    Calls Qt's 'void
    QInputDevicePrivate::setCapabilities(QInputDevice::Capabilities c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html#setCapabilities

    Parameters
    ----------

    c : QInputDevice.Capabilities
      Passed on as its number.
    """
    #  void QInputDevicePrivate::setCapabilities(QInputDevice::Capabilities
    #      c)
    self.uglySide.call(
        'ritual_ZN19QInputDevicePrivate15setCapabilitiesE6QFlagsIN12QInputD'
        'evice10CapabilityEE',
        c.value,
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

  @overload(str, int, QInputDevice.DeviceType)
  @overload(str, int, QInputDevice.DeviceType, QInputDevice.Capabilities)
  @overload(
      str, int, QInputDevice.DeviceType, QInputDevice.Capabilities, str,
  )
  def __init__(
      self,
      name: str,
      winSysId: int,
      type: QInputDevice.DeviceType,
      caps: QInputDevice.Capabilities = QInputDevice.Capabilities.NULL,
      seatName: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QInputDevicePrivate::QInputDevicePrivate(const QString &name, qint64
    winSysId, QInputDevice::DeviceType type, QInputDevice::Capabilities caps,
    const QString &seatName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdeviceprivate.html#QInputDevicePrivate

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    winSysId : int
      Passed on as it is.

    type : QInputDevice.DeviceType
      Passed on as its number.

    caps : QInputDevice.Capabilities
      Passed on as its number. May be left out, as in Qt: it is then
      QInputDevice.Capabilities.NULL.

    seatName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QInputDevicePrivate::QInputDevicePrivate(const QString &name, qint64
    #      winSysId, QInputDevice::DeviceType type,
    #      QInputDevice::Capabilities caps, const QString &seatName)
    self._noteCreation(QInputDevicePrivate, lambda: Rituals.call(
        'ritual_ZN19QInputDevicePrivateC1ERK7QStringxN12QInputDevice10Devic'
        'eTypeE6QFlagsINS3_10CapabilityEES2_',
        name, winSysId, type.value, caps.value, seatName,
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

  def q_func(self) -> Optional[QInputDevice]:
    """
    Calls Qt's 'QInputDevice *QInputDevicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdeviceprivate.html#q_func

    Returns
    -------

    Optional[QInputDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDevice *QInputDevicePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QInputDevicePrivate6q_funcEv')
    return QInputDevice._cuteAt(address)
