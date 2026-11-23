"""
QInputDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qinputdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDevice(QObject):
  """
  The cute side of Qt's QInputDevice: a plain Python object standing in front
  of one C++ QInputDevice.

  It is built on the cute 'QObject', as Qt's QInputDevice is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputDevice that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'name', 'type',
  'capabilities', 'hasCapability', 'systemId', 'seatName',
  'availableVirtualGeometry', 'seatNames', 'primaryKeyboard'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputDevice::~QInputDevice()': the destructor: Python never
    removes a C++ QInputDevice.

  What has no ritual
  ------------------

  15 of the 29 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 4 forbidden; 2 a signal; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QInputDevice is created at the first use, not by
    'QInputDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputDevice.
  - Qt tells when it has removed the C++ QInputDevice. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QInputDevice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags, scoped=True):
    """
    The flags enum 'QInputDevice::Capability' of Qt, with the 16 names Qt
    gives in it. Qt names the type of its combinations
    'QInputDevice::Capabilities'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    NULL = 0x0
    Position = 0x1
    Area = 0x2
    Pressure = 0x4
    Velocity = 0x8
    NormalizedPosition = 0x20
    MouseEmulation = 0x40
    PixelScroll = 0x80
    Scroll = 0x100
    Hover = 0x200
    Rotation = 0x400
    XTilt = 0x800
    YTilt = 0x1000
    TangentialPressure = 0x2000
    ZPosition = 0x4000
    All = 0x7fffffff

  Capabilities = Capability

  class DeviceType(CuteFlags, scoped=True):
    """
    The flags enum 'QInputDevice::DeviceType' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QInputDevice::DeviceTypes'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Unknown = 0x0
    Mouse = 0x1
    TouchScreen = 0x2
    TouchPad = 0x4
    Puck = 0x8
    Stylus = 0x10
    Airbrush = 0x20
    Keyboard = 0x1000
    AllDevices = 0x7fffffff

  DeviceTypes = DeviceType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QInputDevice::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QInputDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def seatNames() -> QStringList:
    """
    Calls Qt's 'QStringList QInputDevice::seatNames()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#seatNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QInputDevice::seatNames()
    address = Rituals.call('ritual_ZN12QInputDevice9seatNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload()
  @overload(str)
  def primaryKeyboard(seatName: str = '') -> Optional[QInputDevice]:
    """
    Calls Qt's 'const QInputDevice *QInputDevice::primaryKeyboard(const
    QString &seatName)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#primaryKeyboard

    Parameters
    ----------

    seatName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QInputDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QInputDevice *QInputDevice::primaryKeyboard(const QString
    #      &seatName)
    address = Rituals.call(
        'ritual_ZN12QInputDevice15primaryKeyboardERK7QString', seatName,
    )
    return QInputDevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputDevice'

  #  A C++ QInputDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QInputDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInputDevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QInputDevice10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QInputDevice::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDevice::name() const
    return self.uglySide.call('ritual_ZNK12QInputDevice4nameEv')

  def type(self) -> DeviceType:
    """
    Calls Qt's 'DeviceType QInputDevice::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#type

    Returns
    -------

    DeviceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DeviceType(number)'
      gives.
    """
    #  DeviceType QInputDevice::type() const
    return QInputDevice.DeviceType(self.uglySide.call(
        'ritual_ZNK12QInputDevice4typeEv',
    ))

  def capabilities(self) -> Capabilities:
    """
    Calls Qt's 'Capabilities QInputDevice::capabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#capabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QInputDevice::capabilities() const
    return QInputDevice.Capabilities(self.uglySide.call(
        'ritual_ZNK12QInputDevice12capabilitiesEv',
    ))

  @overload(Capability)
  def hasCapability(self, cap: Capability) -> bool:
    """
    Calls Qt's 'bool QInputDevice::hasCapability(Capability cap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#hasCapability

    Parameters
    ----------

    cap : Capability
      Passed on as its number.
    """
    #  bool QInputDevice::hasCapability(Capability cap) const
    return self.uglySide.call(
        'ritual_ZNK12QInputDevice13hasCapabilityENS_10CapabilityE',
        cap.value,
    )

  def systemId(self) -> int:
    """
    Calls Qt's 'qint64 QInputDevice::systemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#systemId
    """
    #  qint64 QInputDevice::systemId() const
    return self.uglySide.call('ritual_ZNK12QInputDevice8systemIdEv')

  def seatName(self) -> str:
    """
    Calls Qt's 'QString QInputDevice::seatName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#seatName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDevice::seatName() const
    return self.uglySide.call('ritual_ZNK12QInputDevice8seatNameEv')

  def availableVirtualGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QInputDevice::availableVirtualGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevice.html#availableVirtualGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QInputDevice::availableVirtualGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputDevice24availableVirtualGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QInputDevice::QInputDevice(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#QInputDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QInputDevice::QInputDevice(QObject *parent)
    self._noteCreation(QInputDevice, lambda: Rituals.call(
        'ritual_ZN12QInputDeviceC1EP7QObject', self._addressOf(parent),
    ))

  @overload(str, int, DeviceType)
  @overload(str, int, DeviceType, str)
  @overload(str, int, DeviceType, str, QObject)
  @overload(str, int, DeviceType, str, NoneType)
  def __init__(
      self,
      name: str,
      systemId: int,
      type: DeviceType,
      seatName: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QInputDevice::QInputDevice(const QString
    &name, qint64 systemId, DeviceType type, const QString &seatName, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevice.html#QInputDevice

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    systemId : int
      Passed on as it is.

    type : DeviceType
      Passed on as its number.

    seatName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QInputDevice::QInputDevice(const QString &name, qint64 systemId,
    #      DeviceType type, const QString &seatName, QObject *parent)
    self._noteCreation(QInputDevice, lambda: Rituals.call(
        'ritual_ZN12QInputDeviceC1ERK7QStringxNS_10DeviceTypeES2_P7QObject',
        name, systemId, type.value, seatName, self._addressOf(parent),
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
