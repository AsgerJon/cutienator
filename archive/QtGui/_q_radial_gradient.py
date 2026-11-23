"""
QRadialGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QRadialGradient(QGradient):
  """
  The cute side of Qt's QRadialGradient: a plain Python object standing in
  front of one C++ QRadialGradient.

  It is built on the cute 'QGradient', as Qt's QRadialGradient is built on
  Qt's QGradient, and has everything that class has.

  C++ hands a QRadialGradient around as a copy, so every C++ QRadialGradient
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRadialGradient that has a ritual and that Python
  can call so far, 10 names in all: 'center', 'setCenter', 'focalPoint',
  'setFocalPoint', 'radius', 'setRadius', 'centerRadius', 'setCenterRadius',
  'focalRadius', 'setFocalRadius'. It can be made from Python, in 7 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRadialGradient::~QRadialGradient()': the destructor: Python
    removes its C++ QRadialGradient by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRadialGradient is created at the first use, not by
    'QRadialGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRadialGradient back gives a copy the ritual made for
    Python, in a new cute QRadialGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRadialGradient'

  #  Qt's '~QRadialGradient()'. Naming it makes this a value class: Python
  #  owns every C++ QRadialGradient behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QRadialGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRadialGradient::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#center

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRadialGradient::center() const
    address = self.uglySide.call('ritual_ZNK15QRadialGradient6centerEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def focalPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QRadialGradient::focalPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#focalPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QRadialGradient::focalPoint() const
    address = self.uglySide.call('ritual_ZNK15QRadialGradient10focalPointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QRadialGradient::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#radius
    """
    #  qreal QRadialGradient::radius() const
    return self.uglySide.call('ritual_ZNK15QRadialGradient6radiusEv')

  def centerRadius(self) -> float:
    """
    Calls Qt's 'qreal QRadialGradient::centerRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#centerRadius
    """
    #  qreal QRadialGradient::centerRadius() const
    return self.uglySide.call('ritual_ZNK15QRadialGradient12centerRadiusEv')

  def focalRadius(self) -> float:
    """
    Calls Qt's 'qreal QRadialGradient::focalRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#focalRadius
    """
    #  qreal QRadialGradient::focalRadius() const
    return self.uglySide.call('ritual_ZNK15QRadialGradient11focalRadiusEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setCenter(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QRadialGradient::setCenter(const QPointF &center)'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#setCenter

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRadialGradient::setCenter(const QPointF &center)
    self.uglySide.call(
        'ritual_ZN15QRadialGradient9setCenterERK7QPointF',
        self._valueOf(center),
    )

  @overload(float, float)
  def setCenter(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QRadialGradient::setCenter(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#setCenter

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QRadialGradient::setCenter(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QRadialGradient9setCenterEdd', x, y)

  @overload(QPointF)
  def setFocalPoint(self, focalPoint: QPointF) -> None:
    """
    Calls Qt's 'void QRadialGradient::setFocalPoint(const QPointF
    &focalPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#setFocalPoint

    Parameters
    ----------

    focalPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRadialGradient::setFocalPoint(const QPointF &focalPoint)
    self.uglySide.call(
        'ritual_ZN15QRadialGradient13setFocalPointERK7QPointF',
        self._valueOf(focalPoint),
    )

  @overload(float, float)
  def setFocalPoint(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QRadialGradient::setFocalPoint(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#setFocalPoint

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QRadialGradient::setFocalPoint(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QRadialGradient13setFocalPointEdd', x, y)

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QRadialGradient::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qradialgradient.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QRadialGradient::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN15QRadialGradient9setRadiusEd', radius)

  @overload(float)
  def setCenterRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QRadialGradient::setCenterRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#setCenterRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QRadialGradient::setCenterRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QRadialGradient15setCenterRadiusEd', radius,
    )

  @overload(float)
  def setFocalRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QRadialGradient::setFocalRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#setFocalRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QRadialGradient::setFocalRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QRadialGradient14setFocalRadiusEd', radius,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient
    """
    #  QRadialGradient::QRadialGradient()
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1Ev',
    ))

  @overload(QPointF, float, QPointF)
  def __init__(
      self,
      center: QPointF,
      radius: float,
      focalPoint: QPointF,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(const
    QPointF &center, qreal radius, const QPointF &focalPoint)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.

    focalPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QRadialGradient::QRadialGradient(const QPointF &center, qreal radius,
    #      const QPointF &focalPoint)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1ERK7QPointFdS2_',
        self._valueOf(center), radius, self._valueOf(focalPoint),
    ))

  @overload(float, float, float, float, float)
  def __init__(
      self,
      cx: float,
      cy: float,
      radius: float,
      fx: float,
      fy: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(qreal
    cx, qreal cy, qreal radius, qreal fx, qreal fy)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    cx : float
      Passed on as it is.

    cy : float
      Passed on as it is.

    radius : float
      Passed on as it is.

    fx : float
      Passed on as it is.

    fy : float
      Passed on as it is.
    """
    #  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal radius,
    #      qreal fx, qreal fy)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1Eddddd', cx, cy, radius, fx, fy,
    ))

  @overload(QPointF, float)
  def __init__(self, center: QPointF, radius: float) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(const
    QPointF &center, qreal radius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  QRadialGradient::QRadialGradient(const QPointF &center, qreal radius)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1ERK7QPointFd',
        self._valueOf(center), radius,
    ))

  @overload(float, float, float)
  def __init__(self, cx: float, cy: float, radius: float) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(qreal
    cx, qreal cy, qreal radius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    cx : float
      Passed on as it is.

    cy : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal radius)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1Eddd', cx, cy, radius,
    ))

  @overload(QPointF, float, QPointF, float)
  def __init__(
      self,
      center: QPointF,
      centerRadius: float,
      focalPoint: QPointF,
      focalRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(const
    QPointF &center, qreal centerRadius, const QPointF &focalPoint, qreal
    focalRadius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    centerRadius : float
      Passed on as it is.

    focalPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    focalRadius : float
      Passed on as it is.
    """
    #  QRadialGradient::QRadialGradient(const QPointF &center, qreal
    #      centerRadius, const QPointF &focalPoint, qreal focalRadius)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1ERK7QPointFdS2_d',
        self._valueOf(center), centerRadius, self._valueOf(focalPoint),
        focalRadius,
    ))

  @overload(float, float, float, float, float, float)
  def __init__(
      self,
      cx: float,
      cy: float,
      centerRadius: float,
      fx: float,
      fy: float,
      focalRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRadialGradient::QRadialGradient(qreal
    cx, qreal cy, qreal centerRadius, qreal fx, qreal fy, qreal
    focalRadius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qradialgradient.html#QRadialGradient

    Parameters
    ----------

    cx : float
      Passed on as it is.

    cy : float
      Passed on as it is.

    centerRadius : float
      Passed on as it is.

    fx : float
      Passed on as it is.

    fy : float
      Passed on as it is.

    focalRadius : float
      Passed on as it is.
    """
    #  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal
    #      centerRadius, qreal fx, qreal fy, qreal focalRadius)
    self._noteCreation(QRadialGradient, lambda: Rituals.call(
        'ritual_ZN15QRadialGradientC1Edddddd',
        cx, cy, centerRadius, fx, fy, focalRadius,
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
