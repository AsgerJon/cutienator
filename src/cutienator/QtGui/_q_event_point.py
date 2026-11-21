"""
QEventPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qeventpoint.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QEventPointState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QSizeF
  from . import QPointingDevice, QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QEventPoint: a plain Python object standing in front
  of one C++ QEventPoint.

  C++ hands a QEventPoint around as a copy, so every C++ QEventPoint behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QEventPoint that has a ritual and that Python can
  call so far, 38 names in all: 'position', 'pressPosition', 'grabPosition',
  'lastPosition', 'scenePosition', 'scenePressPosition', 'sceneGrabPosition',
  'sceneLastPosition', 'globalPosition', 'globalPressPosition',
  'globalGrabPosition', 'globalLastPosition', 'normalizedPosition', 'pos',
  'startPos', 'scenePos', 'startScenePos', 'screenPos', 'startScreenPos',
  'startNormalizedPos', 'normalizedPos', 'lastPos', 'lastScenePos',
  'lastScreenPos', 'lastNormalizedPos', 'velocity', 'state', 'device', 'id',
  'timestamp', 'lastTimestamp', 'pressTimestamp', 'timeHeld', 'pressure',
  'rotation', 'ellipseDiameters', 'isAccepted', 'setAccepted'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QEventPoint::operator==(const QEventPoint &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QEventPoint::operator!=(const QEventPoint &other) const': an
    operator, which is not reflected yet.
  - Qt's 'QEventPoint::~QEventPoint()': the destructor: Python removes its
    C++ QEventPoint by it, and has no other use for it.
  - Qt's 'QPointingDeviceUniqueId QEventPoint::uniqueId() const': gives
    'QPointingDeviceUniqueId', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 52 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QEventPoint is created at the first use, not by
    'QEventPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QEventPoint back gives a copy the ritual made for
    Python, in a new cute QEventPoint.
  """

  #  The enums Qt writes inside QEventPoint, and the names Qt has for the
  #  combinations of its flags enums.
  State = QEventPointState
  States = QEventPointState

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventPoint'

  #  Qt's '~QEventPoint()'. Naming it makes this a value class: Python owns
  #  every C++ QEventPoint behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QEventPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::position() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pressPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::pressPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#pressPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::pressPosition() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint13pressPositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def grabPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::grabPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#grabPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::grabPosition() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint12grabPositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::lastPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::lastPosition() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint12lastPositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::scenePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#scenePosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::scenePosition() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint13scenePositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePressPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::scenePressPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#scenePressPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::scenePressPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint18scenePressPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def sceneGrabPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::sceneGrabPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#sceneGrabPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::sceneGrabPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint17sceneGrabPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def sceneLastPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::sceneLastPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#sceneLastPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::sceneLastPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint17sceneLastPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::globalPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#globalPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::globalPosition() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint14globalPositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalPressPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::globalPressPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#globalPressPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::globalPressPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint19globalPressPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalGrabPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::globalGrabPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#globalGrabPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::globalGrabPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint18globalGrabPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalLastPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::globalLastPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#globalLastPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::globalLastPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint18globalLastPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def normalizedPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::normalizedPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#normalizedPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::normalizedPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint18normalizedPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::pos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint3posEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::startPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#startPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::startPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint8startPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::scenePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::scenePos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint8scenePosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startScenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::startScenePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#startScenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::startScenePos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint13startScenePosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::screenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#screenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::screenPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint9screenPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startScreenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::startScreenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#startScreenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::startScreenPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint14startScreenPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startNormalizedPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::startNormalizedPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpoint.html#startNormalizedPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::startNormalizedPos() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint18startNormalizedPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def normalizedPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::normalizedPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#normalizedPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::normalizedPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint13normalizedPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::lastPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::lastPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint7lastPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::lastScenePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastScenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::lastScenePos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint12lastScenePosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScreenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::lastScreenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastScreenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::lastScreenPos() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint13lastScreenPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastNormalizedPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEventPoint::lastNormalizedPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastNormalizedPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEventPoint::lastNormalizedPos() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint17lastNormalizedPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def velocity(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QEventPoint::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#velocity

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QEventPoint::velocity() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint8velocityEv')
    from . import QVector2D
    return QVector2D._cuteOwning(address)

  def state(self) -> State:
    """
    Calls Qt's 'State QEventPoint::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QEventPoint::state() const
    return QEventPoint.State(self.uglySide.call(
        'ritual_ZNK11QEventPoint5stateEv',
    ))

  def device(self) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'const QPointingDevice *QEventPoint::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#device

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPointingDevice *QEventPoint::device() const
    address = self.uglySide.call('ritual_ZNK11QEventPoint6deviceEv')
    from . import QPointingDevice
    return QPointingDevice._cuteAt(address)

  def id(self) -> int:
    """
    Calls Qt's 'int QEventPoint::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#id
    """
    #  int QEventPoint::id() const
    return self.uglySide.call('ritual_ZNK11QEventPoint2idEv')

  def timestamp(self) -> int:
    """
    Calls Qt's 'ulong QEventPoint::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#timestamp
    """
    #  ulong QEventPoint::timestamp() const
    return self.uglySide.call('ritual_ZNK11QEventPoint9timestampEv')

  def lastTimestamp(self) -> int:
    """
    Calls Qt's 'ulong QEventPoint::lastTimestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#lastTimestamp
    """
    #  ulong QEventPoint::lastTimestamp() const
    return self.uglySide.call('ritual_ZNK11QEventPoint13lastTimestampEv')

  def pressTimestamp(self) -> int:
    """
    Calls Qt's 'ulong QEventPoint::pressTimestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#pressTimestamp
    """
    #  ulong QEventPoint::pressTimestamp() const
    return self.uglySide.call('ritual_ZNK11QEventPoint14pressTimestampEv')

  def timeHeld(self) -> float:
    """
    Calls Qt's 'qreal QEventPoint::timeHeld() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#timeHeld
    """
    #  qreal QEventPoint::timeHeld() const
    return self.uglySide.call('ritual_ZNK11QEventPoint8timeHeldEv')

  def pressure(self) -> float:
    """
    Calls Qt's 'qreal QEventPoint::pressure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#pressure
    """
    #  qreal QEventPoint::pressure() const
    return self.uglySide.call('ritual_ZNK11QEventPoint8pressureEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QEventPoint::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#rotation
    """
    #  qreal QEventPoint::rotation() const
    return self.uglySide.call('ritual_ZNK11QEventPoint8rotationEv')

  def ellipseDiameters(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QEventPoint::ellipseDiameters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#ellipseDiameters

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QEventPoint::ellipseDiameters() const
    address = self.uglySide.call(
        'ritual_ZNK11QEventPoint16ellipseDiametersEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QEventPoint::isAccepted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#isAccepted
    """
    #  bool QEventPoint::isAccepted() const
    return self.uglySide.call('ritual_ZNK11QEventPoint10isAcceptedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setAccepted(self, accepted: bool = True) -> None:
    """
    Calls Qt's 'void QEventPoint::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QEventPoint::setAccepted(bool accepted)
    self.uglySide.call('ritual_ZN11QEventPoint11setAcceptedEb', accepted)

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
  @overload(int)
  @overload(int, QPointingDevice)
  @overload(int, NoneType)
  def __init__(
      self,
      id: int = -1,
      device: Optional[QPointingDevice] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QEventPoint::QEventPoint(int id, const
    QPointingDevice *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#QEventPoint

    Parameters
    ----------

    id : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventPoint::QEventPoint(int id, const QPointingDevice *device)
    self._noteCreation(QEventPoint, lambda: Rituals.call(
        'ritual_ZN11QEventPointC1EiPK15QPointingDevice',
        id, self._addressOf(device),
    ))

  @overload(int, State, QPointF, QPointF)
  def __init__(
      self,
      pointId: int,
      state: State,
      scenePosition: QPointF,
      globalPosition: QPointF,
  ) -> None:
    """
    Notes what was given, for Qt's 'QEventPoint::QEventPoint(int pointId,
    State state, const QPointF &scenePosition, const QPointF
    &globalPosition)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#QEventPoint

    Parameters
    ----------

    pointId : int
      Passed on as it is.

    state : State
      Passed on as its number.

    scenePosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QEventPoint::QEventPoint(int pointId, State state, const QPointF
    #      &scenePosition, const QPointF &globalPosition)
    self._noteCreation(QEventPoint, lambda: Rituals.call(
        'ritual_ZN11QEventPointC1EiNS_5StateERK7QPointFS3_',
        pointId, state.value, self._valueOf(scenePosition),
        self._valueOf(globalPosition),
    ))

  @overload(THIS)
  def __init__(self, other: QEventPoint) -> None:
    """
    Notes what was given, for Qt's 'QEventPoint::QEventPoint(const
    QEventPoint &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeventpoint.html#QEventPoint

    Parameters
    ----------

    other : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  QEventPoint::QEventPoint(const QEventPoint &other)
    self._noteCreation(QEventPoint, lambda: Rituals.call(
        'ritual_ZN11QEventPointC1ERKS_', self._valueOf(other),
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
