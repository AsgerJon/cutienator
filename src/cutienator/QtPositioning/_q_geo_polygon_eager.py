"""
QGeoPolygonEager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPolygonEager to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoPolygon, QGeoShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPolygonEager(QGeoPolygon):
  """
  The cute side of Qt's QGeoPolygonEager: a plain Python object standing in
  front of one C++ QGeoPolygonEager.

  It is built on the cute 'QGeoPolygon', as Qt's QGeoPolygonEager is built on
  Qt's QGeoPolygon, and has everything that class has.

  C++ hands a QGeoPolygonEager around as a copy, so every C++
  QGeoPolygonEager behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QGeoPolygonEager yet. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPolygonEager::~QGeoPolygonEager()': the destructor: Python
    removes its C++ QGeoPolygonEager by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoPolygonEager is created at the first use, not by
    'QGeoPolygonEager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPolygonEager back gives a copy the ritual made
    for Python, in a new cute QGeoPolygonEager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPolygonEager'

  #  Qt's '~QGeoPolygonEager()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoPolygonEager behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGeoPolygonEagerD1Ev'

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
    Notes what was given, for Qt's 'QGeoPolygonEager::QGeoPolygonEager()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygoneager.html#QGeoPolygonEager
    """
    #  QGeoPolygonEager::QGeoPolygonEager()
    self._noteCreation(QGeoPolygonEager, lambda: Rituals.call(
        'ritual_ZN16QGeoPolygonEagerC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, path: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygonEager::QGeoPolygonEager(const
    QList<QGeoCoordinate> &path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygoneager.html#QGeoPolygonEager

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoPolygonEager::QGeoPolygonEager(const QList<QGeoCoordinate> &path)
    self._noteCreation(QGeoPolygonEager, lambda: Rituals.call(
        'ritual_ZN16QGeoPolygonEagerC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    ))

  @overload(QGeoPolygon)
  def __init__(self, other: QGeoPolygon) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygonEager::QGeoPolygonEager(const
    QGeoPolygon &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygoneager.html#QGeoPolygonEager

    Parameters
    ----------

    other : QGeoPolygon
      Passed on as a value: Qt reads the C++ QGeoPolygon, which stays
      Python's own.
    """
    #  QGeoPolygonEager::QGeoPolygonEager(const QGeoPolygon &other)
    self._noteCreation(QGeoPolygonEager, lambda: Rituals.call(
        'ritual_ZN16QGeoPolygonEagerC1ERK11QGeoPolygon',
        self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygonEager::QGeoPolygonEager(const
    QGeoShape &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygoneager.html#QGeoPolygonEager

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoPolygonEager::QGeoPolygonEager(const QGeoShape &other)
    self._noteCreation(QGeoPolygonEager, lambda: Rituals.call(
        'ritual_ZN16QGeoPolygonEagerC1ERK9QGeoShape', self._valueOf(other),
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
