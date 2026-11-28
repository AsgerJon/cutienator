"""
QGeoMapTypePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomaptype_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoMapTypePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMap, QSharedData
from . import QGeoMapType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QVariant
  from . import QGeoCameraCapabilities
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QVariant = WAIT['QVariant']


class QGeoMapTypePrivate(QSharedData):
  """
  The cute side of Qt's QGeoMapTypePrivate: a plain Python object standing in
  front of one C++ QGeoMapTypePrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoMapTypePrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoMapTypePrivate around as a copy, so every C++
  QGeoMapTypePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoMapTypePrivate that has a ritual and that Python
  can call so far, 1 name in all: '__eq__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoMapTypePrivate::~QGeoMapTypePrivate()': the destructor: Python
    removes its C++ QGeoMapTypePrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGeoMapTypePrivate is created at the first use, not by
    'QGeoMapTypePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoMapTypePrivate back gives a copy the ritual made
    for Python, in a new cute QGeoMapTypePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMapTypePrivate'

  #  Qt's '~QGeoMapTypePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoMapTypePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGeoMapTypePrivateD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QGeoMapTypePrivate) -> bool:
    """
    Calls Qt's 'bool QGeoMapTypePrivate::operator==(const QGeoMapTypePrivate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptypeprivate.html#operator==

    Parameters
    ----------

    other : QGeoMapTypePrivate
      Passed on as a value: Qt reads the C++ QGeoMapTypePrivate, which stays
      Python's own.
    """
    #  bool QGeoMapTypePrivate::operator==(const QGeoMapTypePrivate &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QGeoMapTypePrivateeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMapTypePrivate::QGeoMapTypePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaptypeprivate.html#QGeoMapTypePrivate
    """
    #  QGeoMapTypePrivate::QGeoMapTypePrivate()
    self._noteCreation(QGeoMapTypePrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoMapTypePrivateC1Ev',
    ))

  @overload(
      QGeoMapType.MapStyle, str, str, bool, bool, int, QByteArray,
      QGeoCameraCapabilities, QMap[str, QVariant],
  )
  def __init__(
      self,
      style: QGeoMapType.MapStyle,
      name: str,
      description: str,
      mobile: bool,
      night: bool,
      mapId: int,
      pluginName: QByteArray,
      cameraCapabilities: QGeoCameraCapabilities,
      metadata: QMap[str, QVariant],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMapTypePrivate::QGeoMapTypePrivate(QGeoMapType::MapStyle style,
    const QString &name, const QString &description, bool mobile, bool night,
    int mapId, const QByteArray &pluginName, const QGeoCameraCapabilities
    &cameraCapabilities, const QVariantMap &metadata)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaptypeprivate.html#QGeoMapTypePrivate

    Parameters
    ----------

    style : QGeoMapType.MapStyle
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    mobile : bool
      Passed on as it is.

    night : bool
      Passed on as it is.

    mapId : int
      Passed on as it is.

    pluginName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    cameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.

    metadata : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QGeoMapTypePrivate::QGeoMapTypePrivate(QGeoMapType::MapStyle style,
    #      const QString &name, const QString &description, bool mobile, bool
    #      night, int mapId, const QByteArray &pluginName, const
    #      QGeoCameraCapabilities &cameraCapabilities, const QVariantMap
    #      &metadata)
    self._noteCreation(QGeoMapTypePrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoMapTypePrivateC1EN11QGeoMapType8MapStyleERK7QString'
        'S4_bbiRK10QByteArrayRK22QGeoCameraCapabilitiesRK4QMapIS2_8QVariant'
        'E',
        style.value, name, description, mobile, night, mapId,
        self._valueOf(pluginName), self._valueOf(cameraCapabilities),
        self._valueOf(metadata),
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
