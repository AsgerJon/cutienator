"""
QGeoSatelliteInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeosatelliteinfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoSatelliteInfoPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoSatelliteInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoSatelliteInfo = WAIT['QGeoSatelliteInfo']


class QGeoSatelliteInfoPrivate(QSharedData):
  """
  The cute side of Qt's QGeoSatelliteInfoPrivate: a plain Python object
  standing in front of one C++ QGeoSatelliteInfoPrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoSatelliteInfoPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoSatelliteInfoPrivate around as a copy, so every C++
  QGeoSatelliteInfoPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoSatelliteInfoPrivate that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', 'get'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoSatelliteInfoPrivate::~QGeoSatelliteInfoPrivate()': the
    destructor: Python removes its C++ QGeoSatelliteInfoPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QGeoSatelliteInfoPrivate is created at the first use, not by
    'QGeoSatelliteInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoSatelliteInfoPrivate back gives a copy the ritual
    made for Python, in a new cute QGeoSatelliteInfoPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoSatelliteInfo)
  def get(info: QGeoSatelliteInfo) -> Optional[QGeoSatelliteInfoPrivate]:
    """
    Calls Qt's 'QGeoSatelliteInfoPrivate *QGeoSatelliteInfoPrivate::get(const
    QGeoSatelliteInfo &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfoprivate.html#get

    Parameters
    ----------

    info : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.

    Returns
    -------

    Optional[QGeoSatelliteInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoPrivate *QGeoSatelliteInfoPrivate::get(const
    #      QGeoSatelliteInfo &info)
    address = Rituals.call(
        'ritual_ZN24QGeoSatelliteInfoPrivate3getERK17QGeoSatelliteInfo',
        CuteMixin._valueOf(info),
    )
    return QGeoSatelliteInfoPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoSatelliteInfoPrivate'

  #  Qt's '~QGeoSatelliteInfoPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoSatelliteInfoPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QGeoSatelliteInfoPrivateD1Ev'

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
  def __eq__(self, other: QGeoSatelliteInfoPrivate) -> bool:
    """
    Calls Qt's 'bool QGeoSatelliteInfoPrivate::operator==(const
    QGeoSatelliteInfoPrivate &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfoprivate.html#operator==

    Parameters
    ----------

    other : QGeoSatelliteInfoPrivate
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfoPrivate, which
      stays Python's own.
    """
    #  bool QGeoSatelliteInfoPrivate::operator==(const
    #      QGeoSatelliteInfoPrivate &other) const
    return self.uglySide.call(
        'ritual_ZNK24QGeoSatelliteInfoPrivateeqERKS_', self._valueOf(other),
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
    'QGeoSatelliteInfoPrivate::QGeoSatelliteInfoPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfoprivate.html
    """
    #  QGeoSatelliteInfoPrivate::QGeoSatelliteInfoPrivate()
    self._noteCreation(QGeoSatelliteInfoPrivate, lambda: Rituals.call(
        'ritual_ZN24QGeoSatelliteInfoPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoSatelliteInfoPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoSatelliteInfoPrivate::QGeoSatelliteInfoPrivate(const
    QGeoSatelliteInfoPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfoprivate.html

    Parameters
    ----------

    other : QGeoSatelliteInfoPrivate
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfoPrivate, which
      stays Python's own.
    """
    #  QGeoSatelliteInfoPrivate::QGeoSatelliteInfoPrivate(const
    #      QGeoSatelliteInfoPrivate &other)
    self._noteCreation(QGeoSatelliteInfoPrivate, lambda: Rituals.call(
        'ritual_ZN24QGeoSatelliteInfoPrivateC1ERKS_', self._valueOf(other),
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
