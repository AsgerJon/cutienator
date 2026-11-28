"""
QGeoSatelliteInfoSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeosatelliteinfosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoSatelliteInfoSourcePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoSatelliteInfoSourcePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGeoSatelliteInfoSourcePrivate: a plain Python object
  standing in front of one C++ QGeoSatelliteInfoSourcePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGeoSatelliteInfoSourcePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoSatelliteInfoSourcePrivate that has a ritual and
  that Python can call so far, 1 name in all: '_qt_property_interval_offset'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoSatelliteInfoSourcePrivate::~QGeoSatelliteInfoSourcePrivate()':
    the destructor: Python never removes a C++
    QGeoSatelliteInfoSourcePrivate.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on
  'QGeoPositionInfoSourcePrivate.

  What to expect
  --------------

  - The C++ QGeoSatelliteInfoSourcePrivate is created at the first use, not
    by 'QGeoSatelliteInfoSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoSatelliteInfoSourcePrivate.
  - Each name of Qt's QGeoSatelliteInfoSourcePrivate that has no cute
    function yet, 'createSourceReal', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_interval_offset() -> int:
    """
    Calls Qt's 'size_t
    QGeoSatelliteInfoSourcePrivate::_qt_property_interval_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosourceprivate.html
    """
    #  size_t QGeoSatelliteInfoSourcePrivate::_qt_property_interval_offset()
    return Rituals.call(
        'ritual_ZN30QGeoSatelliteInfoSourcePrivate28_qt_property_interval_o'
        'ffsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoSatelliteInfoSourcePrivate'

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
  def createSourceReal(*__, **_) -> Never:
    """
    Qt's 'QGeoSatelliteInfoSource
    *QGeoSatelliteInfoSourcePrivate::createSourceReal(const QCborMap &meta,
    const QVariantMap &parameters, QObject *parent)': leans on
    'QGeoPositionInfoSourcePrivate::loadFactory(QCborMap const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGeoSatelliteInfoSourcePrivate.createSourceReal' has no cute "
        "function yet. Qt's 'QGeoSatelliteInfoSource "
        "*QGeoSatelliteInfoSourcePrivate::createSourceReal(const QCborMap "
        "&meta, const QVariantMap &parameters, QObject *parent)': leans on "
        "'QGeoPositionInfoSourcePrivate::loadFactory(QCborMap const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
