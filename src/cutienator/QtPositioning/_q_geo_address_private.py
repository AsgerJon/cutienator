"""
QGeoAddressPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeoaddress_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoAddressPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData


class QGeoAddressPrivate(QSharedData):
  """
  The cute side of Qt's QGeoAddressPrivate: a plain Python object standing in
  front of one C++ QGeoAddressPrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoAddressPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoAddressPrivate around as a copy, so every C++
  QGeoAddressPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QGeoAddressPrivate yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoAddressPrivate::~QGeoAddressPrivate()': the destructor: Python
    removes its C++ QGeoAddressPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGeoAddressPrivate is created at the first use, not by
    'QGeoAddressPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoAddressPrivate back gives a copy the ritual made
    for Python, in a new cute QGeoAddressPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoAddressPrivate'

  #  Qt's '~QGeoAddressPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoAddressPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGeoAddressPrivateD1Ev'

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
    'QGeoAddressPrivate::QGeoAddressPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoaddressprivate.html#QGeoAddressPrivate
    """
    #  QGeoAddressPrivate::QGeoAddressPrivate()
    self._noteCreation(QGeoAddressPrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoAddressPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoAddressPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoAddressPrivate::QGeoAddressPrivate(const QGeoAddressPrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoaddressprivate.html#QGeoAddressPrivate

    Parameters
    ----------

    other : QGeoAddressPrivate
      Passed on as a value: Qt reads the C++ QGeoAddressPrivate, which stays
      Python's own.
    """
    #  QGeoAddressPrivate::QGeoAddressPrivate(const QGeoAddressPrivate
    #      &other)
    self._noteCreation(QGeoAddressPrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoAddressPrivateC1ERKS_', self._valueOf(other),
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
