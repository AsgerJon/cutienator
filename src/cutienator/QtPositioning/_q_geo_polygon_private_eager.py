"""
QGeoPolygonPrivateEager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPolygonPrivateEager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoPolygonPrivate, QGeoShapePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPolygonPrivateEager(QGeoPolygonPrivate):
  """
  The cute side of Qt's QGeoPolygonPrivateEager: a plain Python object
  standing in front of one C++ QGeoPolygonPrivateEager.

  It is built on the cute 'QGeoPolygonPrivate', as Qt's
  QGeoPolygonPrivateEager is built on Qt's QGeoPolygonPrivate, and has
  everything that class has.

  C++ hands a QGeoPolygonPrivateEager around as a copy, so every C++
  QGeoPolygonPrivateEager behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPolygonPrivateEager that has a ritual and that
  Python can call so far, 5 names in all: 'clone', 'translate', 'markDirty',
  'addCoordinate', 'updateBoundingBox'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPolygonPrivateEager::~QGeoPolygonPrivateEager()': the
    destructor: Python removes its C++ QGeoPolygonPrivateEager by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QGeoPolygonPrivateEager is created at the first use, not by
    'QGeoPolygonPrivateEager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPolygonPrivateEager back gives a copy the ritual
    made for Python, in a new cute QGeoPolygonPrivateEager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPolygonPrivateEager'

  #  Qt's '~QGeoPolygonPrivateEager()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoPolygonPrivateEager behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QGeoPolygonPrivateEagerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoPolygonPrivateEager::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivateeager.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoPolygonPrivateEager::clone() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoPolygonPrivateEager5cloneEv',
    )
    return QGeoShapePrivate._cuteAt(address)

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
    'QGeoPolygonPrivateEager::QGeoPolygonPrivateEager()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html
    """
    #  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager()
    self._noteCreation(QGeoPolygonPrivateEager, lambda: Rituals.call(
        'ritual_ZN23QGeoPolygonPrivateEagerC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, path: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
    QList<QGeoCoordinate> &path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
    #      QList<QGeoCoordinate> &path)
    self._noteCreation(QGeoPolygonPrivateEager, lambda: Rituals.call(
        'ritual_ZN23QGeoPolygonPrivateEagerC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPolygonPrivateEager) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
    QGeoPolygonPrivateEager &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html

    Parameters
    ----------

    other : QGeoPolygonPrivateEager
      Passed on as a value: Qt reads the C++ QGeoPolygonPrivateEager, which
      stays Python's own.
    """
    #  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
    #      QGeoPolygonPrivateEager &other)
    self._noteCreation(QGeoPolygonPrivateEager, lambda: Rituals.call(
        'ritual_ZN23QGeoPolygonPrivateEagerC1ERKS_', self._valueOf(other),
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

  @overload(float, float)
  def translate(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivateEager::translate(double
    degreesLatitude, double degreesLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPolygonPrivateEager::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN23QGeoPolygonPrivateEager9translateEdd',
        degreesLatitude, degreesLongitude,
    )

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivateEager::markDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html#markDirty
    """
    #  void QGeoPolygonPrivateEager::markDirty()
    self.uglySide.call('ritual_ZN23QGeoPolygonPrivateEager9markDirtyEv')

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivateEager::addCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPolygonPrivateEager::addCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN23QGeoPolygonPrivateEager13addCoordinateERK14QGeoCoordina'
        'te',
        self._valueOf(coordinate),
    )

  def updateBoundingBox(self) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivateEager::updateBoundingBox()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivateeager.html#updateBoundingBox
    """
    #  void QGeoPolygonPrivateEager::updateBoundingBox()
    self.uglySide.call(
        'ritual_ZN23QGeoPolygonPrivateEager17updateBoundingBoxEv',
    )
