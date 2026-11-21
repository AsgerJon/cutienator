"""
QPointerEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QInputEvent, QPointingDevicePointerType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QEventPoint, QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPointerEvent(QInputEvent):
  """
  The cute side of Qt's QPointerEvent: a plain Python object standing in
  front of one C++ QPointerEvent.

  It is built on the cute 'QInputEvent', as Qt's QPointerEvent is built on
  Qt's QInputEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPointerEvent that has a ritual and that Python can
  call so far, 17 names in all: 'clone', 'pointingDevice', 'pointerType',
  'setTimestamp', 'pointCount', 'pointById', 'allPointsGrabbed',
  'isBeginEvent', 'isUpdateEvent', 'isEndEvent', 'allPointsAccepted',
  'setAccepted', 'exclusiveGrabber', 'setExclusiveGrabber',
  'clearPassiveGrabbers', 'addPassiveGrabber', 'removePassiveGrabber'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointerEvent::~QPointerEvent()': the destructor: Python never
    removes a C++ QPointerEvent.

  What has no ritual
  ------------------

  12 of the 30 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 3 protected; 2 forbidden; 1 declared and nowhere to be found; 1
  a template; 1 private.

  What to expect
  --------------

  - The C++ QPointerEvent is created at the first use, not by
    'QPointerEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPointerEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointerEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QPointerEvent]:
    """
    Calls Qt's 'QPointerEvent *QPointerEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#clone

    Returns
    -------

    Optional[QPointerEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointerEvent *QPointerEvent::clone() const
    address = self.uglySide.call('ritual_ZNK13QPointerEvent5cloneEv')
    return QPointerEvent._cuteAt(address)

  def pointingDevice(self) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice *QPointerEvent::pointingDevice()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#pointingDevice

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice *QPointerEvent::pointingDevice() const
    address = self.uglySide.call(
        'ritual_ZNK13QPointerEvent14pointingDeviceEv',
    )
    from . import QPointingDevice
    return QPointingDevice._cuteAt(address)

  def pointerType(self) -> QPointingDevice.PointerType:
    """
    Calls Qt's 'QPointingDevice::PointerType QPointerEvent::pointerType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#pointerType

    Returns
    -------

    QPointingDevice.PointerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPointingDevice.PointerType(number)' gives.
    """
    #  QPointingDevice::PointerType QPointerEvent::pointerType() const
    return QPointingDevicePointerType(self.uglySide.call(
        'ritual_ZNK13QPointerEvent11pointerTypeEv',
    ))

  def pointCount(self) -> int:
    """
    Calls Qt's 'qsizetype QPointerEvent::pointCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#pointCount
    """
    #  qsizetype QPointerEvent::pointCount() const
    return self.uglySide.call('ritual_ZNK13QPointerEvent10pointCountEv')

  def allPointsGrabbed(self) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::allPointsGrabbed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#allPointsGrabbed
    """
    #  bool QPointerEvent::allPointsGrabbed() const
    return self.uglySide.call(
        'ritual_ZNK13QPointerEvent16allPointsGrabbedEv',
    )

  def isBeginEvent(self) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::isBeginEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#isBeginEvent
    """
    #  bool QPointerEvent::isBeginEvent() const
    return self.uglySide.call('ritual_ZNK13QPointerEvent12isBeginEventEv')

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::isUpdateEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#isUpdateEvent
    """
    #  bool QPointerEvent::isUpdateEvent() const
    return self.uglySide.call('ritual_ZNK13QPointerEvent13isUpdateEventEv')

  def isEndEvent(self) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::isEndEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#isEndEvent
    """
    #  bool QPointerEvent::isEndEvent() const
    return self.uglySide.call('ritual_ZNK13QPointerEvent10isEndEventEv')

  def allPointsAccepted(self) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::allPointsAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#allPointsAccepted
    """
    #  bool QPointerEvent::allPointsAccepted() const
    return self.uglySide.call(
        'ritual_ZNK13QPointerEvent17allPointsAcceptedEv',
    )

  @overload(QEventPoint)
  def exclusiveGrabber(self, point: QEventPoint) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPointerEvent::exclusiveGrabber(const QEventPoint
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#exclusiveGrabber

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPointerEvent::exclusiveGrabber(const QEventPoint &point)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QPointerEvent16exclusiveGrabberERK11QEventPoint',
        self._valueOf(point),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimestamp(self, timestamp: int) -> None:
    """
    Calls Qt's 'void QPointerEvent::setTimestamp(quint64 timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#setTimestamp

    Parameters
    ----------

    timestamp : int
      Passed on as it is.
    """
    #  void QPointerEvent::setTimestamp(quint64 timestamp)
    self.uglySide.call('ritual_ZN13QPointerEvent12setTimestampEy', timestamp)

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QPointerEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QPointerEvent::setAccepted(bool accepted)
    self.uglySide.call('ritual_ZN13QPointerEvent11setAcceptedEb', accepted)

  @overload(QEventPoint, QObject)
  @overload(QEventPoint, NoneType)
  def setExclusiveGrabber(
      self,
      point: QEventPoint,
      exclusiveGrabber: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QPointerEvent::setExclusiveGrabber(const QEventPoint
    &point, QObject *exclusiveGrabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#setExclusiveGrabber

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    exclusiveGrabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPointerEvent::setExclusiveGrabber(const QEventPoint &point,
    #      QObject *exclusiveGrabber)
    self.uglySide.call(
        'ritual_ZN13QPointerEvent19setExclusiveGrabberERK11QEventPointP7QOb'
        'ject',
        self._valueOf(point), self._addressOf(exclusiveGrabber),
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

  @overload(int)
  def pointById(self, id: int) -> Optional[QEventPoint]:
    """
    Calls Qt's 'QEventPoint *QPointerEvent::pointById(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointerevent.html#pointById

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QEventPoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventPoint *QPointerEvent::pointById(int id)
    address = self.uglySide.call('ritual_ZN13QPointerEvent9pointByIdEi', id)
    from . import QEventPoint
    return QEventPoint._cuteAt(address)

  @overload(QEventPoint)
  def clearPassiveGrabbers(self, point: QEventPoint) -> None:
    """
    Calls Qt's 'void QPointerEvent::clearPassiveGrabbers(const QEventPoint
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#clearPassiveGrabbers

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QPointerEvent::clearPassiveGrabbers(const QEventPoint &point)
    self.uglySide.call(
        'ritual_ZN13QPointerEvent20clearPassiveGrabbersERK11QEventPoint',
        self._valueOf(point),
    )

  @overload(QEventPoint, QObject)
  @overload(QEventPoint, NoneType)
  def addPassiveGrabber(
      self,
      point: QEventPoint,
      grabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::addPassiveGrabber(const QEventPoint
    &point, QObject *grabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#addPassiveGrabber

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointerEvent::addPassiveGrabber(const QEventPoint &point,
    #      QObject *grabber)
    return self.uglySide.call(
        'ritual_ZN13QPointerEvent17addPassiveGrabberERK11QEventPointP7QObje'
        'ct',
        self._valueOf(point), self._addressOf(grabber),
    )

  @overload(QEventPoint, QObject)
  @overload(QEventPoint, NoneType)
  def removePassiveGrabber(
      self,
      point: QEventPoint,
      grabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QPointerEvent::removePassiveGrabber(const QEventPoint
    &point, QObject *grabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointerevent.html#removePassiveGrabber

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPointerEvent::removePassiveGrabber(const QEventPoint &point,
    #      QObject *grabber)
    return self.uglySide.call(
        'ritual_ZN13QPointerEvent20removePassiveGrabberERK11QEventPointP7QO'
        'bject',
        self._valueOf(point), self._addressOf(grabber),
    )
