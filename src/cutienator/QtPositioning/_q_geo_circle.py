"""
QGeoCircle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeocircle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGeoShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCirclePrivate, QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoCircle(QGeoShape):
  """
  The cute side of Qt's QGeoCircle: a plain Python object standing in front
  of one C++ QGeoCircle.

  It is built on the cute 'QGeoShape', as Qt's QGeoCircle is built on Qt's
  QGeoShape, and has everything that class has.

  C++ hands a QGeoCircle around as a copy, so every C++ QGeoCircle behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCircle that has a ritual and that Python can
  call so far, 9 names in all: 'setCenter', 'center', 'setRadius', 'radius',
  'translate', 'translated', 'extendCircle', 'toString', 'd_func'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCircle::~QGeoCircle()': the destructor: Python removes its C++
    QGeoCircle by it, and has no other use for it.
  - Qt's 'QGeoCircle &QGeoCircle::operator=(const QGeoCircle &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const QGeoCirclePrivate *QGeoCircle::d_func() const': takes in
    Python what 'QGeoCirclePrivate *QGeoCircle::d_func()' takes.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoCircle
    &circle)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoCircle &circle)':
    an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 21 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoCircle is created at the first use, not by 'QGeoCircle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCircle back gives a copy the ritual made for
    Python, in a new cute QGeoCircle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCircle'

  #  Qt's '~QGeoCircle()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoCircle behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QGeoCircleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoCircle::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoCircle::center() const
    address = self.uglySide.call('ritual_ZNK10QGeoCircle6centerEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QGeoCircle::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#radius
    """
    #  qreal QGeoCircle::radius() const
    return self.uglySide.call('ritual_ZNK10QGeoCircle6radiusEv')

  @overload(float, float)
  def translated(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> QGeoCircle:
    """
    Calls Qt's 'QGeoCircle QGeoCircle::translated(double degreesLatitude,
    double degreesLongitude) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#translated

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.

    Returns
    -------

    QGeoCircle
      A new cute QGeoCircle around the copy Qt gave back. Python owns it.
    """
    #  QGeoCircle QGeoCircle::translated(double degreesLatitude, double
    #      degreesLongitude) const
    address = self.uglySide.call(
        'ritual_ZNK10QGeoCircle10translatedEdd',
        degreesLatitude, degreesLongitude,
    )
    return QGeoCircle._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGeoCircle::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoCircle::toString() const
    return self.uglySide.call('ritual_ZNK10QGeoCircle8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setCenter(self, center: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCircle::setCenter(const QGeoCoordinate &center)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#setCenter

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCircle::setCenter(const QGeoCoordinate &center)
    self.uglySide.call(
        'ritual_ZN10QGeoCircle9setCenterERK14QGeoCoordinate',
        self._valueOf(center),
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QGeoCircle::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QGeoCircle::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN10QGeoCircle9setRadiusEd', radius)

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
    Notes what was given, for Qt's 'QGeoCircle::QGeoCircle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#QGeoCircle
    """
    #  QGeoCircle::QGeoCircle()
    self._noteCreation(QGeoCircle, lambda: Rituals.call(
        'ritual_ZN10QGeoCircleC1Ev',
    ))

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, float)
  def __init__(self, center: QGeoCoordinate, radius: float = -1.0) -> None:
    """
    Notes what was given, for Qt's 'QGeoCircle::QGeoCircle(const
    QGeoCoordinate &center, qreal radius)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#QGeoCircle

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    radius : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.
    """
    #  QGeoCircle::QGeoCircle(const QGeoCoordinate &center, qreal radius)
    self._noteCreation(QGeoCircle, lambda: Rituals.call(
        'ritual_ZN10QGeoCircleC1ERK14QGeoCoordinated',
        self._valueOf(center), radius,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCircle) -> None:
    """
    Notes what was given, for Qt's 'QGeoCircle::QGeoCircle(const QGeoCircle
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#QGeoCircle

    Parameters
    ----------

    other : QGeoCircle
      Passed on as a value: Qt reads the C++ QGeoCircle, which stays Python's
      own.
    """
    #  QGeoCircle::QGeoCircle(const QGeoCircle &other)
    self._noteCreation(QGeoCircle, lambda: Rituals.call(
        'ritual_ZN10QGeoCircleC1ERKS_', self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoCircle::QGeoCircle(const QGeoShape
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#QGeoCircle

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoCircle::QGeoCircle(const QGeoShape &other)
    self._noteCreation(QGeoCircle, lambda: Rituals.call(
        'ritual_ZN10QGeoCircleC1ERK9QGeoShape', self._valueOf(other),
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

  @overload(float, float)
  def translate(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoCircle::translate(double degreesLatitude, double
    degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoCircle::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN10QGeoCircle9translateEdd',
        degreesLatitude, degreesLongitude,
    )

  @overload(QGeoCoordinate)
  def extendCircle(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCircle::extendCircle(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#extendCircle

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCircle::extendCircle(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN10QGeoCircle12extendCircleERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def d_func(self) -> Optional[QGeoCirclePrivate]:
    """
    Calls Qt's 'QGeoCirclePrivate *QGeoCircle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircle.html#d_func

    Returns
    -------

    Optional[QGeoCirclePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCirclePrivate *QGeoCircle::d_func()
    address = self.uglySide.call('ritual_ZN10QGeoCircle6d_funcEv')
    from . import QGeoCirclePrivate
    return QGeoCirclePrivate._cuteAt(address)
