"""
QGeoMercatorCoordinatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoMercatorCoordinatePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QGeoCoordinatePrivate


class QGeoMercatorCoordinatePrivate(QGeoCoordinatePrivate):
  """
  The cute side of Qt's QGeoMercatorCoordinatePrivate: a plain Python object
  standing in front of one C++ QGeoMercatorCoordinatePrivate.

  It is built on the cute 'QGeoCoordinatePrivate', as Qt's
  QGeoMercatorCoordinatePrivate is built on Qt's QGeoCoordinatePrivate, and
  has everything that class has.

  C++ hands a QGeoMercatorCoordinatePrivate around as a copy, so every C++
  QGeoMercatorCoordinatePrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QGeoMercatorCoordinatePrivate yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoMercatorCoordinatePrivate::~QGeoMercatorCoordinatePrivate()':
    the destructor: Python removes its C++ QGeoMercatorCoordinatePrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGeoMercatorCoordinatePrivate is created at the first use, not by
    'QGeoMercatorCoordinatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoMercatorCoordinatePrivate back gives a copy the
    ritual made for Python, in a new cute QGeoMercatorCoordinatePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMercatorCoordinatePrivate'

  #  Qt's '~QGeoMercatorCoordinatePrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QGeoMercatorCoordinatePrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QGeoMercatorCoordinatePrivateD1Ev'

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
    'QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomercatorcoordinateprivate.html
    """
    #  QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate()
    self._noteCreation(QGeoMercatorCoordinatePrivate, lambda: Rituals.call(
        'ritual_ZN29QGeoMercatorCoordinatePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoMercatorCoordinatePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate(const
    QGeoMercatorCoordinatePrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomercatorcoordinateprivate.html

    Parameters
    ----------

    other : QGeoMercatorCoordinatePrivate
      Passed on as a value: Qt reads the C++ QGeoMercatorCoordinatePrivate,
      which stays Python's own.
    """
    #  QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate(const
    #      QGeoMercatorCoordinatePrivate &other)
    self._noteCreation(QGeoMercatorCoordinatePrivate, lambda: Rituals.call(
        'ritual_ZN29QGeoMercatorCoordinatePrivateC1ERKS_',
        self._valueOf(other),
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
