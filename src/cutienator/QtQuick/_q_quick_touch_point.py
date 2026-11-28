"""
QQuickTouchPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickTouchPoint to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from ..QtGui import QPointingDeviceUniqueId, QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointingDeviceUniqueId = WAIT['QPointingDeviceUniqueId']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTouchPoint(QObject):
  """
  The cute side of Qt's QQuickTouchPoint: a plain Python object standing in
  front of one C++ QQuickTouchPoint.

  It is built on the cute 'QObject', as Qt's QQuickTouchPoint is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTouchPoint that has a ritual and that Python
  can call so far, 52 names in all: 'metaObject', 'tr', 'pointId',
  'setPointId', 'uniqueId', 'setUniqueId', 'x', 'y', 'setPosition',
  'ellipseDiameters', 'setEllipseDiameters', 'pressure', 'setPressure',
  'rotation', 'setRotation', 'velocity', 'setVelocity', 'area', 'setArea',
  'isQmlDefined', 'inUse', 'setInUse', 'pressed', 'setPressed', 'startX',
  'setStartX', 'startY', 'setStartY', 'previousX', 'setPreviousX',
  'previousY', 'setPreviousY', 'sceneX', 'setSceneX', 'sceneY', 'setSceneY',
  'pressedChanged', 'pointIdChanged', 'uniqueIdChanged', 'xChanged',
  'yChanged', 'ellipseDiametersChanged', 'pressureChanged',
  'rotationChanged', 'velocityChanged', 'areaChanged', 'startXChanged',
  'startYChanged', 'previousXChanged', 'previousYChanged', 'sceneXChanged',
  'sceneYChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTouchPoint::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTouchPoint::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 57 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTouchPoint is created at the first use, not by
    'QQuickTouchPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTouchPoint.
  - Qt tells when it has removed the C++ QQuickTouchPoint. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuickTouchPoint::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#tr

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
    #  QString QQuickTouchPoint::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickTouchPoint2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTouchPoint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTouchPoint::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTouchPoint::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickTouchPoint10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pointId(self) -> int:
    """
    Calls Qt's 'int QQuickTouchPoint::pointId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#pointId
    """
    #  int QQuickTouchPoint::pointId() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint7pointIdEv')

  def uniqueId(self) -> QPointingDeviceUniqueId:
    """
    Calls Qt's 'QPointingDeviceUniqueId QQuickTouchPoint::uniqueId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#uniqueId

    Returns
    -------

    QPointingDeviceUniqueId
      A new cute QPointingDeviceUniqueId around the copy Qt gave back. Python
      owns it.
    """
    #  QPointingDeviceUniqueId QQuickTouchPoint::uniqueId() const
    address = self.uglySide.call('ritual_ZNK16QQuickTouchPoint8uniqueIdEv')
    from ..QtGui import QPointingDeviceUniqueId
    return QPointingDeviceUniqueId._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#x
    """
    #  qreal QQuickTouchPoint::x() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#y
    """
    #  qreal QQuickTouchPoint::y() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint1yEv')

  def ellipseDiameters(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickTouchPoint::ellipseDiameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#ellipseDiameters

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickTouchPoint::ellipseDiameters() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickTouchPoint16ellipseDiametersEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def pressure(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::pressure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#pressure
    """
    #  qreal QQuickTouchPoint::pressure() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint8pressureEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#rotation
    """
    #  qreal QQuickTouchPoint::rotation() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint8rotationEv')

  def velocity(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickTouchPoint::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#velocity

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickTouchPoint::velocity() const
    address = self.uglySide.call('ritual_ZNK16QQuickTouchPoint8velocityEv')
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def area(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTouchPoint::area() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#area

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTouchPoint::area() const
    address = self.uglySide.call('ritual_ZNK16QQuickTouchPoint4areaEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isQmlDefined(self) -> bool:
    """
    Calls Qt's 'bool QQuickTouchPoint::isQmlDefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#isQmlDefined
    """
    #  bool QQuickTouchPoint::isQmlDefined() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint12isQmlDefinedEv')

  def inUse(self) -> bool:
    """
    Calls Qt's 'bool QQuickTouchPoint::inUse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#inUse
    """
    #  bool QQuickTouchPoint::inUse() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint5inUseEv')

  def pressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickTouchPoint::pressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#pressed
    """
    #  bool QQuickTouchPoint::pressed() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint7pressedEv')

  def startX(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::startX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#startX
    """
    #  qreal QQuickTouchPoint::startX() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint6startXEv')

  def startY(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::startY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#startY
    """
    #  qreal QQuickTouchPoint::startY() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint6startYEv')

  def previousX(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::previousX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#previousX
    """
    #  qreal QQuickTouchPoint::previousX() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint9previousXEv')

  def previousY(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::previousY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#previousY
    """
    #  qreal QQuickTouchPoint::previousY() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint9previousYEv')

  def sceneX(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::sceneX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#sceneX
    """
    #  qreal QQuickTouchPoint::sceneX() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint6sceneXEv')

  def sceneY(self) -> float:
    """
    Calls Qt's 'qreal QQuickTouchPoint::sceneY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#sceneY
    """
    #  qreal QQuickTouchPoint::sceneY() const
    return self.uglySide.call('ritual_ZNK16QQuickTouchPoint6sceneYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPointId(self, id: int) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPointId(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPointId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setPointId(int id)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint10setPointIdEi', id)

  @overload(QPointingDeviceUniqueId)
  def setUniqueId(self, id: QPointingDeviceUniqueId) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setUniqueId(const
    QPointingDeviceUniqueId &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setUniqueId

    Parameters
    ----------

    id : QPointingDeviceUniqueId
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own.
    """
    #  void QQuickTouchPoint::setUniqueId(const QPointingDeviceUniqueId &id)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint11setUniqueIdERK23QPointingDeviceUnique'
        'Id',
        self._valueOf(id),
    )

  @overload(QPointF)
  def setPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPosition(QPointF pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTouchPoint::setPosition(QPointF pos)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint11setPositionE7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QSizeF)
  def setEllipseDiameters(self, d: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setEllipseDiameters(const QSizeF &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#setEllipseDiameters

    Parameters
    ----------

    d : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickTouchPoint::setEllipseDiameters(const QSizeF &d)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint19setEllipseDiametersERK6QSizeF',
        self._valueOf(d),
    )

  @overload(float)
  def setPressure(self, pressure: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPressure(qreal pressure)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPressure

    Parameters
    ----------

    pressure : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setPressure(qreal pressure)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint11setPressureEd', pressure,
    )

  @overload(float)
  def setRotation(self, r: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setRotation(qreal r)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setRotation

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setRotation(qreal r)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint11setRotationEd', r)

  @overload(QVector2D)
  def setVelocity(self, velocity: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setVelocity(const QVector2D
    &velocity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setVelocity

    Parameters
    ----------

    velocity : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickTouchPoint::setVelocity(const QVector2D &velocity)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint11setVelocityERK9QVector2D',
        self._valueOf(velocity),
    )

  @overload(QRectF)
  def setArea(self, area: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setArea(const QRectF &area)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setArea

    Parameters
    ----------

    area : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTouchPoint::setArea(const QRectF &area)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint7setAreaERK6QRectF', self._valueOf(area),
    )

  @overload(bool)
  def setInUse(self, inUse: bool) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setInUse(bool inUse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setInUse

    Parameters
    ----------

    inUse : bool
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setInUse(bool inUse)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint8setInUseEb', inUse)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint10setPressedEb', pressed)

  @overload(float)
  def setStartX(self, startX: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setStartX(qreal startX)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setStartX

    Parameters
    ----------

    startX : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setStartX(qreal startX)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint9setStartXEd', startX)

  @overload(float)
  def setStartY(self, startY: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setStartY(qreal startY)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setStartY

    Parameters
    ----------

    startY : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setStartY(qreal startY)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint9setStartYEd', startY)

  @overload(float)
  def setPreviousX(self, previousX: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPreviousX(qreal previousX)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPreviousX

    Parameters
    ----------

    previousX : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setPreviousX(qreal previousX)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint12setPreviousXEd', previousX,
    )

  @overload(float)
  def setPreviousY(self, previousY: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setPreviousY(qreal previousY)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setPreviousY

    Parameters
    ----------

    previousY : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setPreviousY(qreal previousY)
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint12setPreviousYEd', previousY,
    )

  @overload(float)
  def setSceneX(self, sceneX: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setSceneX(qreal sceneX)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setSceneX

    Parameters
    ----------

    sceneX : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setSceneX(qreal sceneX)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint9setSceneXEd', sceneX)

  @overload(float)
  def setSceneY(self, sceneY: float) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::setSceneY(qreal sceneY)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#setSceneY

    Parameters
    ----------

    sceneY : float
      Passed on as it is.
    """
    #  void QQuickTouchPoint::setSceneY(qreal sceneY)
    self.uglySide.call('ritual_ZN16QQuickTouchPoint9setSceneYEd', sceneY)

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
  @overload(bool)
  def __init__(self, qmlDefined: bool = True) -> None:
    """
    Notes what was given, for Qt's 'QQuickTouchPoint::QQuickTouchPoint(bool
    qmlDefined)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#QQuickTouchPoint

    Parameters
    ----------

    qmlDefined : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  QQuickTouchPoint::QQuickTouchPoint(bool qmlDefined)
    self._noteCreation(QQuickTouchPoint, lambda: Rituals.call(
        'ritual_ZN16QQuickTouchPointC1Eb', qmlDefined,
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

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#pressedChanged
    """
    #  void QQuickTouchPoint::pressedChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint14pressedChangedEv')

  def pointIdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::pointIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#pointIdChanged
    """
    #  void QQuickTouchPoint::pointIdChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint14pointIdChangedEv')

  def uniqueIdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::uniqueIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#uniqueIdChanged
    """
    #  void QQuickTouchPoint::uniqueIdChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint15uniqueIdChangedEv')

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#xChanged
    """
    #  void QQuickTouchPoint::xChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#yChanged
    """
    #  void QQuickTouchPoint::yChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint8yChangedEv')

  def ellipseDiametersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::ellipseDiametersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#ellipseDiametersChanged
    """
    #  void QQuickTouchPoint::ellipseDiametersChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickTouchPoint23ellipseDiametersChangedEv',
    )

  def pressureChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::pressureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#pressureChanged
    """
    #  void QQuickTouchPoint::pressureChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint15pressureChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#rotationChanged
    """
    #  void QQuickTouchPoint::rotationChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint15rotationChangedEv')

  def velocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::velocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#velocityChanged
    """
    #  void QQuickTouchPoint::velocityChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint15velocityChangedEv')

  def areaChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::areaChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktouchpoint.html#areaChanged
    """
    #  void QQuickTouchPoint::areaChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint11areaChangedEv')

  def startXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::startXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#startXChanged
    """
    #  void QQuickTouchPoint::startXChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint13startXChangedEv')

  def startYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::startYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#startYChanged
    """
    #  void QQuickTouchPoint::startYChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint13startYChangedEv')

  def previousXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::previousXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#previousXChanged
    """
    #  void QQuickTouchPoint::previousXChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint16previousXChangedEv')

  def previousYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::previousYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#previousYChanged
    """
    #  void QQuickTouchPoint::previousYChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint16previousYChangedEv')

  def sceneXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::sceneXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#sceneXChanged
    """
    #  void QQuickTouchPoint::sceneXChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint13sceneXChangedEv')

  def sceneYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTouchPoint::sceneYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktouchpoint.html#sceneYChanged
    """
    #  void QQuickTouchPoint::sceneYChanged()
    self.uglySide.call('ritual_ZN16QQuickTouchPoint13sceneYChangedEv')
