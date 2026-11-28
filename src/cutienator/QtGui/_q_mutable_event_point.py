"""
QMutableEventPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qeventpoint_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMutableEventPoint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QEventPoint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QPointF
  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QMutableEventPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMutableEventPoint: a plain Python object standing in
  front of one C++ QMutableEventPoint.

  C++ hands a QMutableEventPoint around as a copy, so every C++
  QMutableEventPoint behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMutableEventPoint that has a ritual and that Python
  can call so far, 3 names in all: 'withTimeStamp', 'window', 'target'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMutableEventPoint::update(const QEventPoint &from,
    QEventPoint &to)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::detach(QEventPoint &p)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setId(QEventPoint &p, int arg)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setDevice(QEventPoint &p, const
    QPointingDevice *arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setTimestamp(QEventPoint &p, ulong t)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setPressTimestamp(QEventPoint &p, ulong
    arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setState(QEventPoint &p,
    QEventPoint::State arg)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QMutableEventPoint::setUniqueId(QEventPoint &p,
    QPointingDeviceUniqueId arg)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QMutableEventPoint::setPosition(QEventPoint &p, QPointF arg)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setScenePosition(QEventPoint &p, QPointF
    arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setGlobalPosition(QEventPoint &p, QPointF
    arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setGlobalPressPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setGlobalGrabPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setGlobalLastPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setEllipseDiameters(QEventPoint &p, QSizeF
    arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setPressure(QEventPoint &p, qreal arg)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setRotation(QEventPoint &p, qreal arg)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setVelocity(QEventPoint &p, QVector2D
    arg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setWindow(QEventPoint &p, QWindow *arg)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QMutableEventPoint::setTarget(QEventPoint &p, QObject *arg)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMutableEventPoint::~QMutableEventPoint()': the destructor: Python
    removes its C++ QMutableEventPoint by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMutableEventPoint is created at the first use, not by
    'QMutableEventPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMutableEventPoint back gives a copy the ritual made
    for Python, in a new cute QMutableEventPoint.
  - Each name of Qt's QMutableEventPoint that has no cute function yet,
    'detach', 'setDevice', 'setEllipseDiameters', 'setGlobalGrabPosition',
    'setGlobalLastPosition', 'setGlobalPosition', 'setGlobalPressPosition',
    'setId', 'setPosition', 'setPressTimestamp', 'setPressure',
    'setRotation', 'setScenePosition', 'setState', 'setTarget',
    'setTimestamp', 'setUniqueId', 'setVelocity', 'setWindow', 'update',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, QEventPoint.State, QPointF, QPointF, QPointF)
  def withTimeStamp(
      timestamp: int,
      pointId: int,
      state: QEventPoint.State,
      position: QPointF,
      scenePosition: QPointF,
      globalPosition: QPointF,
  ) -> QEventPoint:
    """
    Calls Qt's 'QEventPoint QMutableEventPoint::withTimeStamp(ulong
    timestamp, int pointId, QEventPoint::State state, QPointF position,
    QPointF scenePosition, QPointF globalPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutableeventpoint.html#withTimeStamp

    Parameters
    ----------

    timestamp : int
      Passed on as it is.

    pointId : int
      Passed on as it is.

    state : QEventPoint.State
      Passed on as its number.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QEventPoint
      A new cute QEventPoint around the copy Qt gave back. Python owns it.
    """
    #  QEventPoint QMutableEventPoint::withTimeStamp(ulong timestamp, int
    #      pointId, QEventPoint::State state, QPointF position, QPointF
    #      scenePosition, QPointF globalPosition)
    address = Rituals.call(
        'ritual_ZN18QMutableEventPoint13withTimeStampEmiN11QEventPoint5Stat'
        'eE7QPointFS2_S2_',
        timestamp, pointId, state.value, CuteMixin._valueOf(position,
        'QPointF'), CuteMixin._valueOf(scenePosition, 'QPointF'),
        CuteMixin._valueOf(globalPosition, 'QPointF'),
    )
    return QEventPoint._cuteOwning(address)

  @staticmethod
  @overload(QEventPoint)
  def window(p: QEventPoint) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QMutableEventPoint::window(const QEventPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutableeventpoint.html#window

    Parameters
    ----------

    p : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QMutableEventPoint::window(const QEventPoint &p)
    address = Rituals.call(
        'ritual_ZN18QMutableEventPoint6windowERK11QEventPoint',
        CuteMixin._valueOf(p),
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  @overload(QEventPoint)
  def target(p: QEventPoint) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMutableEventPoint::target(const QEventPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutableeventpoint.html#target

    Parameters
    ----------

    p : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMutableEventPoint::target(const QEventPoint &p)
    address = Rituals.call(
        'ritual_ZN18QMutableEventPoint6targetERK11QEventPoint',
        CuteMixin._valueOf(p),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMutableEventPoint'

  #  Qt's '~QMutableEventPoint()'. Naming it makes this a value class: Python
  #  owns every C++ QMutableEventPoint behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMutableEventPointD1Ev'

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

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::detach(QEventPoint &p)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.detach' has no cute function yet. Qt's 'void "
        "QMutableEventPoint::detach(QEventPoint &p)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setDevice(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setDevice(QEventPoint &p, const
    QPointingDevice *arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setDevice' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setDevice(QEventPoint &p, const "
        "QPointingDevice *arg)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setEllipseDiameters(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setEllipseDiameters(QEventPoint &p, QSizeF
    arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setEllipseDiameters' has no cute function yet. "
        "Qt's 'void QMutableEventPoint::setEllipseDiameters(QEventPoint &p, "
        "QSizeF arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGlobalGrabPosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setGlobalGrabPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setGlobalGrabPosition' has no cute function "
        "yet. Qt's 'void "
        "QMutableEventPoint::setGlobalGrabPosition(QEventPoint &p, QPointF "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGlobalLastPosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setGlobalLastPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setGlobalLastPosition' has no cute function "
        "yet. Qt's 'void "
        "QMutableEventPoint::setGlobalLastPosition(QEventPoint &p, QPointF "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGlobalPosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setGlobalPosition(QEventPoint &p, QPointF
    arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setGlobalPosition' has no cute function yet. "
        "Qt's 'void QMutableEventPoint::setGlobalPosition(QEventPoint &p, "
        "QPointF arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGlobalPressPosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setGlobalPressPosition(QEventPoint &p,
    QPointF arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setGlobalPressPosition' has no cute function "
        "yet. Qt's 'void "
        "QMutableEventPoint::setGlobalPressPosition(QEventPoint &p, QPointF "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setId(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setId(QEventPoint &p, int arg)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setId' has no cute function yet. Qt's 'void "
        "QMutableEventPoint::setId(QEventPoint &p, int arg)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setPosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setPosition(QEventPoint &p, QPointF arg)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setPosition' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setPosition(QEventPoint &p, QPointF "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPressTimestamp(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setPressTimestamp(QEventPoint &p, ulong
    arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setPressTimestamp' has no cute function yet. "
        "Qt's 'void QMutableEventPoint::setPressTimestamp(QEventPoint &p, "
        "ulong arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPressure(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setPressure(QEventPoint &p, qreal arg)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setPressure' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setPressure(QEventPoint &p, qreal arg)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRotation(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setRotation(QEventPoint &p, qreal arg)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setRotation' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setRotation(QEventPoint &p, qreal arg)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setScenePosition(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setScenePosition(QEventPoint &p, QPointF
    arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setScenePosition' has no cute function yet. "
        "Qt's 'void QMutableEventPoint::setScenePosition(QEventPoint &p, "
        "QPointF arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setState(QEventPoint &p,
    QEventPoint::State arg)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setState' has no cute function yet. Qt's 'void "
        "QMutableEventPoint::setState(QEventPoint &p, QEventPoint::State "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTarget(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setTarget(QEventPoint &p, QObject *arg)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setTarget' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setTarget(QEventPoint &p, QObject "
        "*arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTimestamp(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setTimestamp(QEventPoint &p, ulong t)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setTimestamp' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setTimestamp(QEventPoint &p, ulong t)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setUniqueId(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setUniqueId(QEventPoint &p,
    QPointingDeviceUniqueId arg)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setUniqueId' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setUniqueId(QEventPoint &p, "
        "QPointingDeviceUniqueId arg)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setVelocity(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setVelocity(QEventPoint &p, QVector2D
    arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setVelocity' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setVelocity(QEventPoint &p, QVector2D "
        "arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setWindow(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::setWindow(QEventPoint &p, QWindow *arg)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.setWindow' has no cute function yet. Qt's "
        "'void QMutableEventPoint::setWindow(QEventPoint &p, QWindow "
        "*arg)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void QMutableEventPoint::update(const QEventPoint &from,
    QEventPoint &to)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMutableEventPoint.update' has no cute function yet. Qt's 'void "
        "QMutableEventPoint::update(const QEventPoint &from, QEventPoint "
        "&to)': takes a type Python has no way to hand over yet.")
