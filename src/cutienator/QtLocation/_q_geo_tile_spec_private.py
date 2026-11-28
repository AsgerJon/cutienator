"""
QGeoTileSpecPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotilespec_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTileSpecPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData


class QGeoTileSpecPrivate(QSharedData):
  """
  The cute side of Qt's QGeoTileSpecPrivate: a plain Python object standing
  in front of one C++ QGeoTileSpecPrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoTileSpecPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoTileSpecPrivate around as a copy, so every C++
  QGeoTileSpecPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoTileSpecPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'hash', '__eq__', '__lt__'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoTileSpecPrivate::~QGeoTileSpecPrivate()': the destructor:
    Python removes its C++ QGeoTileSpecPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QGeoTileSpecPrivate is created at the first use, not by
    'QGeoTileSpecPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoTileSpecPrivate back gives a copy the ritual made
    for Python, in a new cute QGeoTileSpecPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTileSpecPrivate'

  #  Qt's '~QGeoTileSpecPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoTileSpecPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QGeoTileSpecPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoTileSpecPrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespecprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoTileSpecPrivate::hash(size_t seed) const
    return self.uglySide.call('ritual_ZNK19QGeoTileSpecPrivate4hashEm', seed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoTileSpecPrivate) -> bool:
    """
    Calls Qt's 'bool QGeoTileSpecPrivate::operator==(const
    QGeoTileSpecPrivate &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilespecprivate.html#operator==

    Parameters
    ----------

    rhs : QGeoTileSpecPrivate
      Passed on as a value: Qt reads the C++ QGeoTileSpecPrivate, which stays
      Python's own.
    """
    #  bool QGeoTileSpecPrivate::operator==(const QGeoTileSpecPrivate &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QGeoTileSpecPrivateeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QGeoTileSpecPrivate) -> bool:
    """
    Calls Qt's 'bool QGeoTileSpecPrivate::operator<(const QGeoTileSpecPrivate
    &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespecprivate.html#operator<

    Parameters
    ----------

    rhs : QGeoTileSpecPrivate
      Passed on as a value: Qt reads the C++ QGeoTileSpecPrivate, which stays
      Python's own.
    """
    #  bool QGeoTileSpecPrivate::operator<(const QGeoTileSpecPrivate &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QGeoTileSpecPrivateltERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  @overload(str, int, int, int)
  @overload(str, int, int, int, int)
  @overload(str, int, int, int, int, int)
  def __init__(
      self,
      plugin: str = '',
      mapId: int = 0,
      zoom: int = -1,
      x: int = -1,
      y: int = -1,
      version: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTileSpecPrivate::QGeoTileSpecPrivate(const QString &plugin, int
    mapId, int zoom, int x, int y, int version)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilespecprivate.html#QGeoTileSpecPrivate

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    mapId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    zoom : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    x : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    y : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    version : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QGeoTileSpecPrivate::QGeoTileSpecPrivate(const QString &plugin, int
    #      mapId, int zoom, int x, int y, int version)
    self._noteCreation(QGeoTileSpecPrivate, lambda: Rituals.call(
        'ritual_ZN19QGeoTileSpecPrivateC1ERK7QStringiiiii',
        plugin, mapId, zoom, x, y, version,
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
