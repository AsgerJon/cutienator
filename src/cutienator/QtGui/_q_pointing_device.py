"""
QPointingDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QInputDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPointingDeviceUniqueId
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointingDeviceUniqueId = WAIT['QPointingDeviceUniqueId']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPointingDevice(QInputDevice):
  """
  The cute side of Qt's QPointingDevice: a plain Python object standing in
  front of one C++ QPointingDevice.

  It is built on the cute 'QInputDevice', as Qt's QPointingDevice is built on
  Qt's QInputDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPointingDevice that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'setType',
  'setCapabilities', 'setMaximumTouchPoints', 'pointerType', 'maximumPoints',
  'buttonCount', 'uniqueId', 'primaryPointingDevice'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointingDevice::~QPointingDevice()': the destructor: Python never
    removes a C++ QPointingDevice.

  What has no ritual
  ------------------

  13 of the 26 functions Qt declares: 4 forbidden; 3 takes or gives a type
  that cannot be passed yet; 3 private; 1 a template; 1 a signal; 1
  protected.

  What to expect
  --------------

  - The C++ QPointingDevice is created at the first use, not by
    'QPointingDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPointingDevice.
  - Qt tells when it has removed the C++ QPointingDevice. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPointingDevice, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class GrabTransition(CuteNum):
    """
    The enum 'QPointingDevice::GrabTransition' of Qt, with the 7 names Qt
    gives in it.
    """

    GrabPassive = Kee[int](1)
    UngrabPassive = Kee[int](2)
    CancelGrabPassive = Kee[int](3)
    OverrideGrabPassive = Kee[int](4)
    GrabExclusive = Kee[int](16)
    UngrabExclusive = Kee[int](32)
    CancelGrabExclusive = Kee[int](48)

  class PointerType(CuteFlags, scoped=True):
    """
    The flags enum 'QPointingDevice::PointerType' of Qt, with the 8 names Qt
    gives in it. Qt names the type of its combinations
    'QPointingDevice::PointerTypes'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Unknown = 0x0
    Generic = 0x1
    Finger = 0x2
    Pen = 0x4
    Eraser = 0x8
    Cursor = 0x10
    Palm = 0x20
    AllPointerTypes = 0x7fff

  PointerTypes = PointerType

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
    Calls Qt's 'QString QPointingDevice::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#tr

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
    #  QString QPointingDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QPointingDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  @overload(str)
  def primaryPointingDevice(seatName: str = '') -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice
    *QPointingDevice::primaryPointingDevice(const QString &seatName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdevice.html#primaryPointingDevice

    Parameters
    ----------

    seatName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice *QPointingDevice::primaryPointingDevice(const
    #      QString &seatName)
    address = Rituals.call(
        'ritual_ZN15QPointingDevice21primaryPointingDeviceERK7QString',
        seatName,
    )
    return QPointingDevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointingDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPointingDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPointingDevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QPointingDevice10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pointerType(self) -> PointerType:
    """
    Calls Qt's 'PointerType QPointingDevice::pointerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#pointerType

    Returns
    -------

    PointerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PointerType(number)'
      gives.
    """
    #  PointerType QPointingDevice::pointerType() const
    return QPointingDevice.PointerType(self.uglySide.call(
        'ritual_ZNK15QPointingDevice11pointerTypeEv',
    ))

  def maximumPoints(self) -> int:
    """
    Calls Qt's 'int QPointingDevice::maximumPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#maximumPoints
    """
    #  int QPointingDevice::maximumPoints() const
    return self.uglySide.call('ritual_ZNK15QPointingDevice13maximumPointsEv')

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int QPointingDevice::buttonCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#buttonCount
    """
    #  int QPointingDevice::buttonCount() const
    return self.uglySide.call('ritual_ZNK15QPointingDevice11buttonCountEv')

  def uniqueId(self) -> QPointingDeviceUniqueId:
    """
    Calls Qt's 'QPointingDeviceUniqueId QPointingDevice::uniqueId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#uniqueId

    Returns
    -------

    QPointingDeviceUniqueId
      A new cute QPointingDeviceUniqueId around the copy Qt gave back. Python
      owns it.
    """
    #  QPointingDeviceUniqueId QPointingDevice::uniqueId() const
    address = self.uglySide.call('ritual_ZNK15QPointingDevice8uniqueIdEv')
    from . import QPointingDeviceUniqueId
    return QPointingDeviceUniqueId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QInputDevice.DeviceType)
  def setType(self, devType: QInputDevice.DeviceType) -> None:
    """
    Calls Qt's 'void QPointingDevice::setType(DeviceType devType)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdevice.html#setType

    Parameters
    ----------

    devType : QInputDevice.DeviceType
      Passed on as its number.
    """
    #  void QPointingDevice::setType(DeviceType devType)
    self.uglySide.call(
        'ritual_ZN15QPointingDevice7setTypeEN12QInputDevice10DeviceTypeE',
        devType.value,
    )

  @overload(QInputDevice.Capabilities)
  def setCapabilities(self, caps: QInputDevice.Capabilities) -> None:
    """
    Calls Qt's 'void
    QPointingDevice::setCapabilities(QInputDevice::Capabilities caps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdevice.html#setCapabilities

    Parameters
    ----------

    caps : QInputDevice.Capabilities
      Passed on as its number.
    """
    #  void QPointingDevice::setCapabilities(QInputDevice::Capabilities caps)
    self.uglySide.call(
        'ritual_ZN15QPointingDevice15setCapabilitiesE6QFlagsIN12QInputDevic'
        'e10CapabilityEE',
        caps.value,
    )

  @overload(int)
  def setMaximumTouchPoints(self, c: int) -> None:
    """
    Calls Qt's 'void QPointingDevice::setMaximumTouchPoints(int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdevice.html#setMaximumTouchPoints

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QPointingDevice::setMaximumTouchPoints(int c)
    self.uglySide.call(
        'ritual_ZN15QPointingDevice21setMaximumTouchPointsEi', c,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPointingDevice::QPointingDevice(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdevice.html#QPointingDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPointingDevice::QPointingDevice(QObject *parent)
    self._noteCreation(QPointingDevice, lambda: Rituals.call(
        'ritual_ZN15QPointingDeviceC1EP7QObject', self._addressOf(parent),
    ))

  @overload(
      str, int, QInputDevice.DeviceType, PointerType,
      QInputDevice.Capabilities, int, int,
  )
  @overload(
      str, int, QInputDevice.DeviceType, PointerType,
      QInputDevice.Capabilities, int, int, str,
  )
  @overload(
      str, int, QInputDevice.DeviceType, PointerType,
      QInputDevice.Capabilities, int, int, str, QPointingDeviceUniqueId,
  )
  @overload(
      str, int, QInputDevice.DeviceType, PointerType,
      QInputDevice.Capabilities, int, int, str, QPointingDeviceUniqueId,
      QObject,
  )
  @overload(
      str, int, QInputDevice.DeviceType, PointerType,
      QInputDevice.Capabilities, int, int, str, QPointingDeviceUniqueId,
      NoneType,
  )
  def __init__(
      self,
      name: str,
      systemId: int,
      devType: QInputDevice.DeviceType,
      pType: PointerType,
      caps: QInputDevice.Capabilities,
      maxPoints: int,
      buttonCount: int,
      seatName: str = '',
      uniqueId: Optional[QPointingDeviceUniqueId] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPointingDevice::QPointingDevice(const
    QString &name, qint64 systemId, QInputDevice::DeviceType devType,
    PointerType pType, Capabilities caps, int maxPoints, int buttonCount,
    const QString &seatName, QPointingDeviceUniqueId uniqueId, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdevice.html#QPointingDevice

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    systemId : int
      Passed on as it is.

    devType : QInputDevice.DeviceType
      Passed on as its number.

    pType : PointerType
      Passed on as its number.

    caps : QInputDevice.Capabilities
      Passed on as its number.

    maxPoints : int
      Passed on as it is.

    buttonCount : int
      Passed on as it is.

    seatName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    uniqueId : Optional[QPointingDeviceUniqueId]
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own. May be left out, as in Qt: a new
      'QPointingDeviceUniqueId()' is then passed on.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPointingDevice::QPointingDevice(const QString &name, qint64 systemId,
    #      QInputDevice::DeviceType devType, PointerType pType, Capabilities
    #      caps, int maxPoints, int buttonCount, const QString &seatName,
    #      QPointingDeviceUniqueId uniqueId, QObject *parent)
    if uniqueId is None:
      from . import QPointingDeviceUniqueId
      uniqueId = QPointingDeviceUniqueId()
    self._noteCreation(QPointingDevice, lambda: Rituals.call(
        'ritual_ZN15QPointingDeviceC1ERK7QStringxN12QInputDevice10DeviceTyp'
        'eENS_11PointerTypeE6QFlagsINS3_10CapabilityEEiiS2_23QPointingDevic'
        'eUniqueIdP7QObject',
        name, systemId, devType.value, pType.value, caps.value, maxPoints,
        buttonCount, seatName, self._valueOf(uniqueId),
        self._addressOf(parent),
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
