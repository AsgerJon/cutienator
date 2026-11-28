"""
QPointingDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpointingdevice_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPointingDevicePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QInputDevice, QInputDevicePrivate, QPointingDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QEventPoint, QPointerEvent, QPointingDeviceUniqueId
  from . import QTouchEvent, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QObject = WAIT['QObject']
  QPointerEvent = WAIT['QPointerEvent']
  QPointingDeviceUniqueId = WAIT['QPointingDeviceUniqueId']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPointingDevicePrivate(QInputDevicePrivate):
  """
  The cute side of Qt's QPointingDevicePrivate: a plain Python object
  standing in front of one C++ QPointingDevicePrivate.

  It is built on the cute 'QInputDevicePrivate', as Qt's
  QPointingDevicePrivate is built on Qt's QInputDevicePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPointingDevicePrivate that has a ritual and that
  Python can call so far, 19 names in all: 'q_func', 'sendTouchCancelEvent',
  'queryPointById', 'pointById', 'removePointById', 'firstActiveTarget',
  'firstActiveWindow', 'firstPointExclusiveGrabber', 'setExclusiveGrabber',
  'removeExclusiveGrabber', 'addPassiveGrabber', 'setPassiveGrabberContext',
  'removePassiveGrabber', 'clearPassiveGrabbers', 'removeGrabber', 'get',
  'tabletDevice', 'queryTabletDevice', 'pointingDeviceById'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPointingDevice *QPointingDevicePrivate::q_func() const':
    takes in Python what 'QPointingDevice *QPointingDevicePrivate::q_func()'
    takes.
  - Qt's 'QPointingDevicePrivate::~QPointingDevicePrivate()': the destructor:
    Python never removes a C++ QPointingDevicePrivate.
  - Qt's 'const QPointingDevicePrivate *QPointingDevicePrivate::get(const
    QPointingDevice *q)': takes in Python what 'QPointingDevicePrivate
    *QPointingDevicePrivate::get(QPointingDevice *q)' takes.

  What to expect
  --------------

  - The C++ QPointingDevicePrivate is created at the first use, not by
    'QPointingDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPointingDevicePrivate.
  """

  #  The classes Qt writes inside QPointingDevicePrivate, each a class in
  #  here as in C++.

  class EventPointData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPointingDevicePrivate::EventPointData: a plain
    Python object standing in front of one C++
    QPointingDevicePrivate::EventPointData.

    C++ hands a QPointingDevicePrivate::EventPointData around as a copy, so
    every C++ QPointingDevicePrivate::EventPointData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QPointingDevicePrivate::EventPointData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPointingDevicePrivate::EventPointData::~EventPointData()': the
      destructor: Python removes its C++
      QPointingDevicePrivate::EventPointData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QPointingDevicePrivate::EventPointData is created at the first
      use, not by 'QPointingDevicePrivate::EventPointData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPointingDevicePrivate::EventPointData back gives a
      copy the ritual made for Python, in a new cute
      QPointingDevicePrivate::EventPointData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPointingDevicePrivate::EventPointData'

    #  Qt's '~QPointingDevicePrivate::EventPointData()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QPointingDevicePrivate::EventPointData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QPointingDevicePrivate14EventPointDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(EventPointData, QObject, QObject)
  @overload(EventPointData, QObject, NoneType)
  @overload(EventPointData, NoneType, QObject)
  @overload(EventPointData, NoneType, NoneType)
  @overload(NoneType, QObject, QObject)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def setPassiveGrabberContext(
      epd: Optional[EventPointData],
      grabber: Optional[QObject],
      context: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool
    QPointingDevicePrivate::setPassiveGrabberContext(EventPointData *epd,
    QObject *grabber, QObject *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html

    Parameters
    ----------

    epd : Optional[EventPointData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointingDevicePrivate::setPassiveGrabberContext(EventPointData
    #      *epd, QObject *grabber, QObject *context)
    return Rituals.call(
        'ritual_ZN22QPointingDevicePrivate24setPassiveGrabberContextEPNS_14'
        'EventPointDataEP7QObjectS3_',
        CuteMixin._addressOf(epd), CuteMixin._addressOf(grabber, 'QObject'),
        CuteMixin._addressOf(context, 'QObject'),
    )

  @staticmethod
  @overload(QPointingDevice)
  @overload(NoneType)
  def get(q: Optional[QPointingDevice]) -> Optional[QPointingDevicePrivate]:
    """
    Calls Qt's 'QPointingDevicePrivate
    *QPointingDevicePrivate::get(QPointingDevice *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdeviceprivate.html#get

    Parameters
    ----------

    q : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPointingDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointingDevicePrivate *QPointingDevicePrivate::get(QPointingDevice
    #      *q)
    address = Rituals.call(
        'ritual_ZN22QPointingDevicePrivate3getEP15QPointingDevice',
        CuteMixin._addressOf(q),
    )
    return QPointingDevicePrivate._cuteAt(address)

  @staticmethod
  @overload(
      QInputDevice.DeviceType, QPointingDevice.PointerType,
      QPointingDeviceUniqueId,
  )
  def tabletDevice(
      deviceType: QInputDevice.DeviceType,
      pointerType: QPointingDevice.PointerType,
      uniqueId: QPointingDeviceUniqueId,
  ) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice
    *QPointingDevicePrivate::tabletDevice(QInputDevice::DeviceType
    deviceType, QPointingDevice::PointerType pointerType,
    QPointingDeviceUniqueId uniqueId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#tabletDevice

    Parameters
    ----------

    deviceType : QInputDevice.DeviceType
      Passed on as its number.

    pointerType : QPointingDevice.PointerType
      Passed on as its number.

    uniqueId : QPointingDeviceUniqueId
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own.

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice
    #      *QPointingDevicePrivate::tabletDevice(QInputDevice::DeviceType
    #      deviceType, QPointingDevice::PointerType pointerType,
    #      QPointingDeviceUniqueId uniqueId)
    address = Rituals.call(
        'ritual_ZN22QPointingDevicePrivate12tabletDeviceEN12QInputDevice10D'
        'eviceTypeEN15QPointingDevice11PointerTypeE23QPointingDeviceUniqueI'
        'd',
        deviceType.value, pointerType.value, CuteMixin._valueOf(uniqueId),
    )
    return QPointingDevice._cuteAt(address)

  @staticmethod
  @overload(
      QInputDevice.DeviceType, QPointingDevice.PointerType,
      QPointingDeviceUniqueId,
  )
  @overload(
      QInputDevice.DeviceType, QPointingDevice.PointerType,
      QPointingDeviceUniqueId, QInputDevice.Capabilities,
  )
  @overload(
      QInputDevice.DeviceType, QPointingDevice.PointerType,
      QPointingDeviceUniqueId, QInputDevice.Capabilities, int,
  )
  def queryTabletDevice(
      deviceType: QInputDevice.DeviceType,
      pointerType: QPointingDevice.PointerType,
      uniqueId: QPointingDeviceUniqueId,
      capabilities: QInputDevice.Capabilities = (
          QInputDevice.Capabilities.NULL),
      systemId: int = 0,
  ) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice
    *QPointingDevicePrivate::queryTabletDevice(QInputDevice::DeviceType
    deviceType, QPointingDevice::PointerType pointerType,
    QPointingDeviceUniqueId uniqueId, QInputDevice::Capabilities
    capabilities, qint64 systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#queryTabletDevice

    Parameters
    ----------

    deviceType : QInputDevice.DeviceType
      Passed on as its number.

    pointerType : QPointingDevice.PointerType
      Passed on as its number.

    uniqueId : QPointingDeviceUniqueId
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own.

    capabilities : QInputDevice.Capabilities
      Passed on as its number. May be left out, as in Qt: it is then
      QInputDevice.Capabilities.NULL.

    systemId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice
    #      *QPointingDevicePrivate::queryTabletDevice(QInputDevice::
    #      DeviceType deviceType, QPointingDevice::PointerType pointerType,
    #      QPointingDeviceUniqueId uniqueId, QInputDevice::Capabilities
    #      capabilities, qint64 systemId)
    address = Rituals.call(
        'ritual_ZN22QPointingDevicePrivate17queryTabletDeviceEN12QInputDevi'
        'ce10DeviceTypeEN15QPointingDevice11PointerTypeE23QPointingDeviceUn'
        'iqueId6QFlagsINS0_10CapabilityEEx',
        deviceType.value, pointerType.value, CuteMixin._valueOf(uniqueId),
        capabilities.value, systemId,
    )
    return QPointingDevice._cuteAt(address)

  @staticmethod
  @overload(int)
  def pointingDeviceById(systemId: int) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice
    *QPointingDevicePrivate::pointingDeviceById(qint64 systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#pointingDeviceById

    Parameters
    ----------

    systemId : int
      Passed on as it is.

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice
    #      *QPointingDevicePrivate::pointingDeviceById(qint64 systemId)
    address = Rituals.call(
        'ritual_ZN22QPointingDevicePrivate18pointingDeviceByIdEx', systemId,
    )
    return QPointingDevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointingDevicePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def queryPointById(self, id: int) -> Optional[EventPointData]:
    """
    Calls Qt's 'EventPointData *QPointingDevicePrivate::queryPointById(int
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#queryPointById

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[EventPointData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EventPointData *QPointingDevicePrivate::queryPointById(int id) const
    address = self.uglySide.call(
        'ritual_ZNK22QPointingDevicePrivate14queryPointByIdEi', id,
    )
    return QPointingDevicePrivate.EventPointData._cuteAt(address)

  @overload(int)
  def pointById(self, id: int) -> Optional[EventPointData]:
    """
    Calls Qt's 'EventPointData *QPointingDevicePrivate::pointById(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#pointById

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[EventPointData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EventPointData *QPointingDevicePrivate::pointById(int id) const
    address = self.uglySide.call(
        'ritual_ZNK22QPointingDevicePrivate9pointByIdEi', id,
    )
    return QPointingDevicePrivate.EventPointData._cuteAt(address)

  def firstActiveTarget(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPointingDevicePrivate::firstActiveTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#firstActiveTarget

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPointingDevicePrivate::firstActiveTarget() const
    address = self.uglySide.call(
        'ritual_ZNK22QPointingDevicePrivate17firstActiveTargetEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def firstActiveWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QPointingDevicePrivate::firstActiveWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#firstActiveWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QPointingDevicePrivate::firstActiveWindow() const
    address = self.uglySide.call(
        'ritual_ZNK22QPointingDevicePrivate17firstActiveWindowEv',
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  def firstPointExclusiveGrabber(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPointingDevicePrivate::firstPointExclusiveGrabber()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPointingDevicePrivate::firstPointExclusiveGrabber() const
    address = self.uglySide.call(
        'ritual_ZNK22QPointingDevicePrivate26firstPointExclusiveGrabberEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointerEvent, QEventPoint, QObject)
  @overload(QPointerEvent, QEventPoint, NoneType)
  @overload(NoneType, QEventPoint, QObject)
  @overload(NoneType, QEventPoint, NoneType)
  def setExclusiveGrabber(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
      exclusiveGrabber: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QPointingDevicePrivate::setExclusiveGrabber(const
    QPointerEvent *event, const QEventPoint &point, QObject
    *exclusiveGrabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#setExclusiveGrabber

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    exclusiveGrabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPointingDevicePrivate::setExclusiveGrabber(const QPointerEvent
    #      *event, const QEventPoint &point, QObject *exclusiveGrabber)
    self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate19setExclusiveGrabberEPK13QPointe'
        'rEventRK11QEventPointP7QObject',
        self._addressOf(event), self._valueOf(point),
        self._addressOf(exclusiveGrabber, 'QObject'),
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

  @overload(
      str, int, QInputDevice.DeviceType, QPointingDevice.PointerType,
      QInputDevice.Capabilities, int, int,
  )
  @overload(
      str, int, QInputDevice.DeviceType, QPointingDevice.PointerType,
      QInputDevice.Capabilities, int, int, str,
  )
  @overload(
      str, int, QInputDevice.DeviceType, QPointingDevice.PointerType,
      QInputDevice.Capabilities, int, int, str, QPointingDeviceUniqueId,
  )
  def __init__(
      self,
      name: str,
      id: int,
      type: QInputDevice.DeviceType,
      pType: QPointingDevice.PointerType,
      caps: QInputDevice.Capabilities,
      maxPoints: int,
      buttonCount: int,
      seatName: str = '',
      uniqueId: Optional[QPointingDeviceUniqueId] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPointingDevicePrivate::QPointingDevicePrivate(const QString &name,
    qint64 id, QInputDevice::DeviceType type, QPointingDevice::PointerType
    pType, QPointingDevice::Capabilities caps, int maxPoints, int
    buttonCount, const QString &seatName, QPointingDeviceUniqueId uniqueId)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#QPointingDevicePrivate

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    id : int
      Passed on as it is.

    type : QInputDevice.DeviceType
      Passed on as its number.

    pType : QPointingDevice.PointerType
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
    """
    #  QPointingDevicePrivate::QPointingDevicePrivate(const QString &name,
    #      qint64 id, QInputDevice::DeviceType type,
    #      QPointingDevice::PointerType pType, QPointingDevice::Capabilities
    #      caps, int maxPoints, int buttonCount, const QString &seatName,
    #      QPointingDeviceUniqueId uniqueId)
    if uniqueId is None:
      from . import QPointingDeviceUniqueId
      uniqueId = QPointingDeviceUniqueId()
    self._noteCreation(QPointingDevicePrivate, lambda: Rituals.call(
        'ritual_ZN22QPointingDevicePrivateC1ERK7QStringxN12QInputDevice10De'
        'viceTypeEN15QPointingDevice11PointerTypeE6QFlagsINS3_10CapabilityE'
        'EiiS2_23QPointingDeviceUniqueId',
        name, id, type.value, pType.value, caps.value, maxPoints,
        buttonCount, seatName, self._valueOf(uniqueId),
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

  def q_func(self) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'QPointingDevice *QPointingDevicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpointingdeviceprivate.html#q_func

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointingDevice *QPointingDevicePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate6q_funcEv',
    )
    return QPointingDevice._cuteAt(address)

  @overload(QTouchEvent)
  @overload(NoneType)
  def sendTouchCancelEvent(self, cancelEvent: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QPointingDevicePrivate::sendTouchCancelEvent(QTouchEvent
    *cancelEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#sendTouchCancelEvent

    Parameters
    ----------

    cancelEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPointingDevicePrivate::sendTouchCancelEvent(QTouchEvent
    #      *cancelEvent)
    self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate20sendTouchCancelEventEP11QTouchE'
        'vent',
        self._addressOf(cancelEvent),
    )

  @overload(int)
  def removePointById(self, id: int) -> None:
    """
    Calls Qt's 'void QPointingDevicePrivate::removePointById(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#removePointById

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QPointingDevicePrivate::removePointById(int id)
    self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate15removePointByIdEi', id,
    )

  @overload(QPointerEvent, QObject)
  @overload(QPointerEvent, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def removeExclusiveGrabber(
      self,
      event: Optional[QPointerEvent],
      grabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QPointingDevicePrivate::removeExclusiveGrabber(const
    QPointerEvent *event, const QObject *grabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#removeExclusiveGrabber

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointingDevicePrivate::removeExclusiveGrabber(const
    #      QPointerEvent *event, const QObject *grabber)
    return self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate22removeExclusiveGrabberEPK13QPoi'
        'nterEventPK7QObject',
        self._addressOf(event), self._addressOf(grabber, 'QObject'),
    )

  @overload(QPointerEvent, QEventPoint, QObject)
  @overload(QPointerEvent, QEventPoint, NoneType)
  @overload(NoneType, QEventPoint, QObject)
  @overload(NoneType, QEventPoint, NoneType)
  def addPassiveGrabber(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
      grabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QPointingDevicePrivate::addPassiveGrabber(const
    QPointerEvent *event, const QEventPoint &point, QObject *grabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#addPassiveGrabber

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointingDevicePrivate::addPassiveGrabber(const QPointerEvent
    #      *event, const QEventPoint &point, QObject *grabber)
    return self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate17addPassiveGrabberEPK13QPointerE'
        'ventRK11QEventPointP7QObject',
        self._addressOf(event), self._valueOf(point),
        self._addressOf(grabber, 'QObject'),
    )

  @overload(QPointerEvent, QEventPoint, QObject)
  @overload(QPointerEvent, QEventPoint, NoneType)
  @overload(NoneType, QEventPoint, QObject)
  @overload(NoneType, QEventPoint, NoneType)
  def removePassiveGrabber(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
      grabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QPointingDevicePrivate::removePassiveGrabber(const
    QPointerEvent *event, const QEventPoint &point, QObject *grabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#removePassiveGrabber

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointingDevicePrivate::removePassiveGrabber(const QPointerEvent
    #      *event, const QEventPoint &point, QObject *grabber)
    return self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate20removePassiveGrabberEPK13QPoint'
        'erEventRK11QEventPointP7QObject',
        self._addressOf(event), self._valueOf(point),
        self._addressOf(grabber, 'QObject'),
    )

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def clearPassiveGrabbers(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void QPointingDevicePrivate::clearPassiveGrabbers(const
    QPointerEvent *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#clearPassiveGrabbers

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QPointingDevicePrivate::clearPassiveGrabbers(const QPointerEvent
    #      *event, const QEventPoint &point)
    self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate20clearPassiveGrabbersEPK13QPoint'
        'erEventRK11QEventPoint',
        self._addressOf(event), self._valueOf(point),
    )

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def removeGrabber(
      self,
      grabber: Optional[QObject],
      cancel: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QPointingDevicePrivate::removeGrabber(QObject *grabber,
    bool cancel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceprivate.html#removeGrabber

    Parameters
    ----------

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cancel : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPointingDevicePrivate::removeGrabber(QObject *grabber, bool
    #      cancel)
    self.uglySide.call(
        'ritual_ZN22QPointingDevicePrivate13removeGrabberEP7QObjectb',
        self._addressOf(grabber, 'QObject'), cancel,
    )
