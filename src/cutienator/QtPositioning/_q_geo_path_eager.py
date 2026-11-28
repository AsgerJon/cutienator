"""
QGeoPathEager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPathEager to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoPath, QGeoShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPathEager(QGeoPath):
  """
  The cute side of Qt's QGeoPathEager: a plain Python object standing in
  front of one C++ QGeoPathEager.

  It is built on the cute 'QGeoPath', as Qt's QGeoPathEager is built on Qt's
  QGeoPath, and has everything that class has.

  C++ hands a QGeoPathEager around as a copy, so every C++ QGeoPathEager
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QGeoPathEager yet. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPathEager::~QGeoPathEager()': the destructor: Python removes
    its C++ QGeoPathEager by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoPathEager is created at the first use, not by
    'QGeoPathEager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPathEager back gives a copy the ritual made for
    Python, in a new cute QGeoPathEager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPathEager'

  #  Qt's '~QGeoPathEager()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoPathEager behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QGeoPathEagerD1Ev'

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
    Notes what was given, for Qt's 'QGeoPathEager::QGeoPathEager()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopatheager.html#QGeoPathEager
    """
    #  QGeoPathEager::QGeoPathEager()
    self._noteCreation(QGeoPathEager, lambda: Rituals.call(
        'ritual_ZN13QGeoPathEagerC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  @overload(QList[QGeoCoordinate], float)
  def __init__(
      self,
      path: QList[QGeoCoordinate],
      width: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoPathEager::QGeoPathEager(const
    QList<QGeoCoordinate> &path, const qreal &width)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopatheager.html#QGeoPathEager

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    width : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QGeoPathEager::QGeoPathEager(const QList<QGeoCoordinate> &path, const
    #      qreal &width)
    self._noteCreation(QGeoPathEager, lambda: Rituals.call(
        'ritual_ZN13QGeoPathEagerC1ERK5QListI14QGeoCoordinateERKd',
        self._valueOf(path), width,
    ))

  @overload(QGeoPath)
  def __init__(self, other: QGeoPath) -> None:
    """
    Notes what was given, for Qt's 'QGeoPathEager::QGeoPathEager(const
    QGeoPath &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopatheager.html#QGeoPathEager

    Parameters
    ----------

    other : QGeoPath
      Passed on as a value: Qt reads the C++ QGeoPath, which stays Python's
      own.
    """
    #  QGeoPathEager::QGeoPathEager(const QGeoPath &other)
    self._noteCreation(QGeoPathEager, lambda: Rituals.call(
        'ritual_ZN13QGeoPathEagerC1ERK8QGeoPath', self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoPathEager::QGeoPathEager(const
    QGeoShape &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopatheager.html#QGeoPathEager

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoPathEager::QGeoPathEager(const QGeoShape &other)
    self._noteCreation(QGeoPathEager, lambda: Rituals.call(
        'ritual_ZN13QGeoPathEagerC1ERK9QGeoShape', self._valueOf(other),
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
