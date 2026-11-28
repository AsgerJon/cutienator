"""
QQuickHandlerPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickHandlerPoint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QSizeF
  from ..QtGui import QEventPoint, QPointerEvent, QPointingDevice
  from ..QtGui import QPointingDeviceUniqueId, QVector2D
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHandlerPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickHandlerPoint: a plain Python object standing in
  front of one C++ QQuickHandlerPoint.

  C++ hands a QQuickHandlerPoint around as a copy, so every C++
  QQuickHandlerPoint behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickHandlerPoint that has a ritual and that Python
  can call so far, 16 names in all: 'id', 'pressedButtons', 'modifiers',
  'pressPosition', 'scenePressPosition', 'sceneGrabPosition', 'position',
  'scenePosition', 'velocity', 'rotation', 'pressure', 'ellipseDiameters',
  'uniqueId', 'device', 'localize', 'reset'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickHandlerPoint::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickHandlerPoint::~QQuickHandlerPoint()': the destructor: Python
    removes its C++ QQuickHandlerPoint by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickHandlerPoint is created at the first use, not by
    'QQuickHandlerPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickHandlerPoint back gives a copy the ritual made
    for Python, in a new cute QQuickHandlerPoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHandlerPoint'

  #  Qt's '~QQuickHandlerPoint()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickHandlerPoint behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickHandlerPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'int QQuickHandlerPoint::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#id
    """
    #  int QQuickHandlerPoint::id() const
    return self.uglySide.call('ritual_ZNK18QQuickHandlerPoint2idEv')

  def pressedButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickHandlerPoint::pressedButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#pressedButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickHandlerPoint::pressedButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint14pressedButtonsEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QQuickHandlerPoint::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QQuickHandlerPoint::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint9modifiersEv',
    ))

  def pressPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickHandlerPoint::pressPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#pressPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickHandlerPoint::pressPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint13pressPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePressPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickHandlerPoint::scenePressPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#scenePressPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickHandlerPoint::scenePressPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint18scenePressPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def sceneGrabPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickHandlerPoint::sceneGrabPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#sceneGrabPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickHandlerPoint::sceneGrabPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint17sceneGrabPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickHandlerPoint::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickHandlerPoint::position() const
    address = self.uglySide.call('ritual_ZNK18QQuickHandlerPoint8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickHandlerPoint::scenePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#scenePosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickHandlerPoint::scenePosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint13scenePositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def velocity(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickHandlerPoint::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#velocity

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickHandlerPoint::velocity() const
    address = self.uglySide.call('ritual_ZNK18QQuickHandlerPoint8velocityEv')
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickHandlerPoint::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#rotation
    """
    #  qreal QQuickHandlerPoint::rotation() const
    return self.uglySide.call('ritual_ZNK18QQuickHandlerPoint8rotationEv')

  def pressure(self) -> float:
    """
    Calls Qt's 'qreal QQuickHandlerPoint::pressure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#pressure
    """
    #  qreal QQuickHandlerPoint::pressure() const
    return self.uglySide.call('ritual_ZNK18QQuickHandlerPoint8pressureEv')

  def ellipseDiameters(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickHandlerPoint::ellipseDiameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#ellipseDiameters

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickHandlerPoint::ellipseDiameters() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHandlerPoint16ellipseDiametersEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def uniqueId(self) -> QPointingDeviceUniqueId:
    """
    Calls Qt's 'QPointingDeviceUniqueId QQuickHandlerPoint::uniqueId()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#uniqueId

    Returns
    -------

    QPointingDeviceUniqueId
      A new cute QPointingDeviceUniqueId around the copy Qt gave back. Python
      owns it.
    """
    #  QPointingDeviceUniqueId QQuickHandlerPoint::uniqueId() const
    address = self.uglySide.call('ritual_ZNK18QQuickHandlerPoint8uniqueIdEv')
    from ..QtGui import QPointingDeviceUniqueId
    return QPointingDeviceUniqueId._cuteOwning(address)

  def device(self) -> Optional[QPointingDevice]:
    """
    Calls Qt's 'QPointingDevice *QQuickHandlerPoint::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#device

    Returns
    -------

    Optional[QPointingDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointingDevice *QQuickHandlerPoint::device() const
    address = self.uglySide.call('ritual_ZNK18QQuickHandlerPoint6deviceEv')
    from ..QtGui import QPointingDevice
    return QPointingDevice._cuteAt(address)

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
    'QQuickHandlerPoint::QQuickHandlerPoint()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhandlerpoint.html#QQuickHandlerPoint
    """
    #  QQuickHandlerPoint::QQuickHandlerPoint()
    self._noteCreation(QQuickHandlerPoint, lambda: Rituals.call(
        'ritual_ZN18QQuickHandlerPointC1Ev',
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

  @overload(QQuickItem)
  @overload(NoneType)
  def localize(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickHandlerPoint::localize(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#localize

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickHandlerPoint::localize(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN18QQuickHandlerPoint8localizeEP10QQuickItem',
        self._addressOf(item),
    )

  @overload()
  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickHandlerPoint::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#reset
    """
    #  void QQuickHandlerPoint::reset()
    self.uglySide.call('ritual_ZN18QQuickHandlerPoint5resetEv')

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def reset(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void QQuickHandlerPoint::reset(const QPointerEvent *event,
    const QEventPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#reset

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QQuickHandlerPoint::reset(const QPointerEvent *event, const
    #      QEventPoint &point)
    self.uglySide.call(
        'ritual_ZN18QQuickHandlerPoint5resetEPK13QPointerEventRK11QEventPoi'
        'nt',
        self._addressOf(event), self._valueOf(point),
    )

  @overload(QList[WAIT['QQuickHandlerPoint']])
  def reset(self, points: QList[QQuickHandlerPoint]) -> None:
    """
    Calls Qt's 'void QQuickHandlerPoint::reset(const
    QList<QQuickHandlerPoint> &points)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhandlerpoint.html#reset

    Parameters
    ----------

    points : QList[QQuickHandlerPoint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickHandlerPoint::reset(const QList<QQuickHandlerPoint>
    #      &points)
    self.uglySide.call(
        'ritual_ZN18QQuickHandlerPoint5resetERK5QListIS_E',
        self._valueOf(points),
    )


#  Qt's 'QList<QQuickHandlerPoint>': the list of QQuickHandlerPoint, which
#  'QList[QQuickHandlerPoint]' gives. It is made here, so that there is one
#  as soon as there can be a QQuickHandlerPoint.
QList.createKind(
    QQuickHandlerPoint, 'value',
    make='ritual_list_make_QQuickHandlerPoint',
    add='ritual_list_add_QQuickHandlerPoint',
    size='ritual_list_size_QQuickHandlerPoint',
    at='ritual_list_at_QQuickHandlerPoint',
    drop='ritual_list_drop_QQuickHandlerPoint',
)
