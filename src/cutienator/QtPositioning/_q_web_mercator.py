"""
QWebMercator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qwebmercator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWebMercator to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDoubleVector2D, QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector2D = WAIT['QDoubleVector2D']
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QWebMercator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebMercator: a plain Python object standing in front
  of one C++ QWebMercator.

  C++ hands a QWebMercator around as a copy, so every C++ QWebMercator behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebMercator that has a ritual and that Python can
  call so far, 4 names in all: 'coordToMercator', 'mercatorToCoord',
  'coordinateInterpolation', 'realmod'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebMercator::~QWebMercator()': the destructor: Python removes its
    C++ QWebMercator by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QWebMercator is created at the first use, not by
    'QWebMercator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebMercator back gives a copy the ritual made for
    Python, in a new cute QWebMercator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoCoordinate)
  def coordToMercator(coord: QGeoCoordinate) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D QWebMercator::coordToMercator(const
    QGeoCoordinate &coord)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebmercator.html#coordToMercator

    Parameters
    ----------

    coord : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QWebMercator::coordToMercator(const QGeoCoordinate
    #      &coord)
    address = Rituals.call(
        'ritual_ZN12QWebMercator15coordToMercatorERK14QGeoCoordinate',
        CuteMixin._valueOf(coord),
    )
    from . import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @staticmethod
  @overload(QDoubleVector2D)
  def mercatorToCoord(mercator: QDoubleVector2D) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QWebMercator::mercatorToCoord(const
    QDoubleVector2D &mercator)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebmercator.html#mercatorToCoord

    Parameters
    ----------

    mercator : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QWebMercator::mercatorToCoord(const QDoubleVector2D
    #      &mercator)
    address = Rituals.call(
        'ritual_ZN12QWebMercator15mercatorToCoordERK15QDoubleVector2D',
        CuteMixin._valueOf(mercator),
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @staticmethod
  @overload(QGeoCoordinate, QGeoCoordinate, float)
  def coordinateInterpolation(
      from_: QGeoCoordinate,
      to: QGeoCoordinate,
      progress: float,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QWebMercator::coordinateInterpolation(const
    QGeoCoordinate &from, const QGeoCoordinate &to, qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebmercator.html#coordinateInterpolation

    Parameters
    ----------

    from_ : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    to : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QWebMercator::coordinateInterpolation(const
    #      QGeoCoordinate &from, const QGeoCoordinate &to, qreal progress)
    address = Rituals.call(
        'ritual_ZN12QWebMercator23coordinateInterpolationERK14QGeoCoordinat'
        'eS2_d',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(to), progress,
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  def realmod(a: float, b: float) -> float:
    """
    Calls Qt's 'double QWebMercator::realmod(const double a, const double
    b)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebmercator.html#realmod

    Parameters
    ----------

    a : float
      Passed on as it is.

    b : float
      Passed on as it is.
    """
    #  double QWebMercator::realmod(const double a, const double b)
    return Rituals.call('ritual_ZN12QWebMercator7realmodEdd', a, b)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebMercator'

  #  Qt's '~QWebMercator()'. Naming it makes this a value class: Python owns
  #  every C++ QWebMercator behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QWebMercatorD1Ev'

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
