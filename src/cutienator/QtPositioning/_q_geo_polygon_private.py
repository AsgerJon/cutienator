"""
QGeoPolygonPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPolygonPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoPathPrivateBase, QGeoShapePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPolygonPrivate(QGeoPathPrivateBase):
  """
  The cute side of Qt's QGeoPolygonPrivate: a plain Python object standing in
  front of one C++ QGeoPolygonPrivate.

  It is built on the cute 'QGeoPathPrivateBase', as Qt's QGeoPolygonPrivate
  is built on Qt's QGeoPathPrivateBase, and has everything that class has.

  C++ hands a QGeoPolygonPrivate around as a copy, so every C++
  QGeoPolygonPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPolygonPrivate that has a ritual and that Python
  can call so far, 12 names in all: 'clone', 'isValid', 'contains',
  'translate', 'hash', 'markDirty', 'holesCount', 'polygonContains',
  'holePath', 'addHole', 'removeHole', 'ensureClipperPathUpdated'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPolygonPrivate::~QGeoPolygonPrivate()': the destructor: Python
    removes its C++ QGeoPolygonPrivate by it, and has no other use for it.
  - Qt's 'bool QGeoPolygonPrivate::operator==(const QGeoShapePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoPolygonPrivate is created at the first use, not by
    'QGeoPolygonPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPolygonPrivate back gives a copy the ritual made
    for Python, in a new cute QGeoPolygonPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPolygonPrivate'

  #  A C++ QGeoPolygonPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoPolygonPrivate'

  #  Qt's '~QGeoPolygonPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoPolygonPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGeoPolygonPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoPolygonPrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoPolygonPrivate::clone() const
    ritual = 'ritual_ZNK18QGeoPolygonPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGeoPolygonPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QGeoShapePrivate._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoPolygonPrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#isValid
    """
    #  bool QGeoPolygonPrivate::isValid() const
    ritual = 'ritual_ZNK18QGeoPolygonPrivate7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGeoPolygonPrivate7isValidEv'
    return self.uglySide.call(ritual)

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPolygonPrivate::contains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPolygonPrivate::contains(const QGeoCoordinate &coordinate)
    #      const
    ritual = 'ritual_ZNK18QGeoPolygonPrivate8containsERK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QGeoPolygonPrivate8containsERK14QGeoCoordinate')
    return self.uglySide.call(ritual, self._valueOf(coordinate))

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoPolygonPrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoPolygonPrivate::hash(size_t seed) const
    ritual = 'ritual_ZNK18QGeoPolygonPrivate4hashEm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGeoPolygonPrivate4hashEm'
    return self.uglySide.call(ritual, seed)

  def holesCount(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoPolygonPrivate::holesCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#holesCount
    """
    #  qsizetype QGeoPolygonPrivate::holesCount() const
    return self.uglySide.call('ritual_ZNK18QGeoPolygonPrivate10holesCountEv')

  @overload(QGeoCoordinate)
  def polygonContains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPolygonPrivate::polygonContains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivate.html#polygonContains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPolygonPrivate::polygonContains(const QGeoCoordinate
    #      &coordinate) const
    return self.uglySide.call(
        'ritual_ZNK18QGeoPolygonPrivate15polygonContainsERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(int)
  def holePath(self, index: int) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'const QList<QGeoCoordinate>
    QGeoPolygonPrivate::holePath(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#holePath

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QGeoCoordinate> QGeoPolygonPrivate::holePath(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK18QGeoPolygonPrivate8holePathEx', index,
    )
    from . import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

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
    'QGeoPolygonPrivate::QGeoPolygonPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivate.html#QGeoPolygonPrivate
    """
    #  QGeoPolygonPrivate::QGeoPolygonPrivate()
    self._noteCreation(QGeoPolygonPrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoPolygonPrivateC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, path: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPolygonPrivate::QGeoPolygonPrivate(const QList<QGeoCoordinate>
    &path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivate.html#QGeoPolygonPrivate

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoPolygonPrivate::QGeoPolygonPrivate(const QList<QGeoCoordinate>
    #      &path)
    self._noteCreation(QGeoPolygonPrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoPolygonPrivateC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPolygonPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPolygonPrivate::QGeoPolygonPrivate(const QGeoPolygonPrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivate.html#QGeoPolygonPrivate

    Parameters
    ----------

    other : QGeoPolygonPrivate
      Passed on as a value: Qt reads the C++ QGeoPolygonPrivate, which stays
      Python's own.
    """
    #  QGeoPolygonPrivate::QGeoPolygonPrivate(const QGeoPolygonPrivate
    #      &other)
    self._noteCreation(QGeoPolygonPrivate, lambda: Rituals.call(
        'ritual_ZN18QGeoPolygonPrivateC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QGeoPolygonPrivate::translate(double degreesLatitude,
    double degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPolygonPrivate::translate(double degreesLatitude, double
    #      degreesLongitude)
    ritual = 'ritual_ZN18QGeoPolygonPrivate9translateEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QGeoPolygonPrivate9translateEdd'
    self.uglySide.call(ritual, degreesLatitude, degreesLongitude)

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivate::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#markDirty
    """
    #  void QGeoPolygonPrivate::markDirty()
    ritual = 'ritual_ZN18QGeoPolygonPrivate9markDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QGeoPolygonPrivate9markDirtyEv'
    self.uglySide.call(ritual)

  @overload(QList[QGeoCoordinate])
  def addHole(self, holePath: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivate::addHole(const QList<QGeoCoordinate>
    &holePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#addHole

    Parameters
    ----------

    holePath : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPolygonPrivate::addHole(const QList<QGeoCoordinate>
    #      &holePath)
    self.uglySide.call(
        'ritual_ZN18QGeoPolygonPrivate7addHoleERK5QListI14QGeoCoordinateE',
        self._valueOf(holePath),
    )

  @overload(int)
  def removeHole(self, index: int) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivate::removeHole(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygonprivate.html#removeHole

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGeoPolygonPrivate::removeHole(qsizetype index)
    self.uglySide.call('ritual_ZN18QGeoPolygonPrivate10removeHoleEx', index)

  def ensureClipperPathUpdated(self) -> None:
    """
    Calls Qt's 'void QGeoPolygonPrivate::ensureClipperPathUpdated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygonprivate.html#ensureClipperPathUpdated
    """
    #  void QGeoPolygonPrivate::ensureClipperPathUpdated() const
    self.uglySide.call(
        'ritual_ZNK18QGeoPolygonPrivate24ensureClipperPathUpdatedEv',
    )
