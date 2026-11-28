"""
QGeoCoordinatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoCoordinatePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCoordinatePrivate(QSharedData):
  """
  The cute side of Qt's QGeoCoordinatePrivate: a plain Python object standing
  in front of one C++ QGeoCoordinatePrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoCoordinatePrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoCoordinatePrivate around as a copy, so every C++
  QGeoCoordinatePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCoordinatePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'get'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCoordinatePrivate::~QGeoCoordinatePrivate()': the destructor:
    Python removes its C++ QGeoCoordinatePrivate by it, and has no other use
    for it.
  - Qt's 'void QGeoCoordinatePrivate::atDistanceAndAzimuth(const
    QGeoCoordinate &coord, qreal distance, qreal azimuth, double *lon, double
    *lat)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QGeoCoordinatePrivate is created at the first use, not by
    'QGeoCoordinatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCoordinatePrivate back gives a copy the ritual
    made for Python, in a new cute QGeoCoordinatePrivate.
  - Each name of Qt's QGeoCoordinatePrivate that has no cute function yet,
    'atDistanceAndAzimuth', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoCoordinate)
  @overload(NoneType)
  def get(c: Optional[QGeoCoordinate]) -> Optional[QGeoCoordinatePrivate]:
    """
    Calls Qt's 'const QGeoCoordinatePrivate *QGeoCoordinatePrivate::get(const
    QGeoCoordinate *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinateprivate.html#get

    Parameters
    ----------

    c : Optional[QGeoCoordinate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoCoordinatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGeoCoordinatePrivate *QGeoCoordinatePrivate::get(const
    #      QGeoCoordinate *c)
    address = Rituals.call(
        'ritual_ZN21QGeoCoordinatePrivate3getEPK14QGeoCoordinate',
        CuteMixin._addressOf(c),
    )
    return QGeoCoordinatePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCoordinatePrivate'

  #  Qt's '~QGeoCoordinatePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoCoordinatePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QGeoCoordinatePrivateD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCoordinatePrivate::QGeoCoordinatePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateprivate.html#QGeoCoordinatePrivate
    """
    #  QGeoCoordinatePrivate::QGeoCoordinatePrivate()
    self._noteCreation(QGeoCoordinatePrivate, lambda: Rituals.call(
        'ritual_ZN21QGeoCoordinatePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCoordinatePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCoordinatePrivate::QGeoCoordinatePrivate(const QGeoCoordinatePrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateprivate.html#QGeoCoordinatePrivate

    Parameters
    ----------

    other : QGeoCoordinatePrivate
      Passed on as a value: Qt reads the C++ QGeoCoordinatePrivate, which
      stays Python's own.
    """
    #  QGeoCoordinatePrivate::QGeoCoordinatePrivate(const
    #      QGeoCoordinatePrivate &other)
    self._noteCreation(QGeoCoordinatePrivate, lambda: Rituals.call(
        'ritual_ZN21QGeoCoordinatePrivateC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def atDistanceAndAzimuth(*__, **_) -> Never:
    """
    Qt's 'void QGeoCoordinatePrivate::atDistanceAndAzimuth(const
    QGeoCoordinate &coord, qreal distance, qreal azimuth, double *lon, double
    *lat)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QGeoCoordinatePrivate.atDistanceAndAzimuth' has no cute function "
        "yet. Qt's 'void QGeoCoordinatePrivate::atDistanceAndAzimuth(const "
        "QGeoCoordinate &coord, qreal distance, qreal azimuth, double *lon, "
        "double *lat)': takes a number to change where it is.")
