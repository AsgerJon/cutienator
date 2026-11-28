"""
QGeoCirclePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeocircle_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoCirclePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGeoShapePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCoordinate, QGeoRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoCirclePrivate(QGeoShapePrivate):
  """
  The cute side of Qt's QGeoCirclePrivate: a plain Python object standing in
  front of one C++ QGeoCirclePrivate.

  It is built on the cute 'QGeoShapePrivate', as Qt's QGeoCirclePrivate is
  built on Qt's QGeoShapePrivate, and has everything that class has.

  C++ hands a QGeoCirclePrivate around as a copy, so every C++
  QGeoCirclePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCirclePrivate that has a ritual and that Python
  can call so far, 13 names in all: 'isValid', 'isEmpty', 'contains',
  'center', 'boundingGeoRectangle', 'crossNorthPole', 'crossSouthPole',
  'updateBoundingBox', 'setCenter', 'setRadius', 'extendCircle', 'clone',
  'hash'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCirclePrivate::~QGeoCirclePrivate()': the destructor: Python
    removes its C++ QGeoCirclePrivate by it, and has no other use for it.
  - Qt's 'bool QGeoCirclePrivate::operator==(const QGeoShapePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoCirclePrivate is created at the first use, not by
    'QGeoCirclePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCirclePrivate back gives a copy the ritual made
    for Python, in a new cute QGeoCirclePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCirclePrivate'

  #  A C++ QGeoCirclePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoCirclePrivate'

  #  Qt's '~QGeoCirclePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoCirclePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QGeoCirclePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoCirclePrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#isValid
    """
    #  bool QGeoCirclePrivate::isValid() const
    ritual = 'ritual_ZNK17QGeoCirclePrivate7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate7isValidEv'
    return self.uglySide.call(ritual)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoCirclePrivate::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#isEmpty
    """
    #  bool QGeoCirclePrivate::isEmpty() const
    ritual = 'ritual_ZNK17QGeoCirclePrivate7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate7isEmptyEv'
    return self.uglySide.call(ritual)

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoCirclePrivate::contains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoCirclePrivate::contains(const QGeoCoordinate &coordinate)
    #      const
    ritual = 'ritual_ZNK17QGeoCirclePrivate8containsERK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGeoCirclePrivate8containsERK14QGeoCoordinate')
    return self.uglySide.call(ritual, self._valueOf(coordinate))

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoCirclePrivate::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoCirclePrivate::center() const
    ritual = 'ritual_ZNK17QGeoCirclePrivate6centerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate6centerEv'
    address = self.uglySide.call(ritual)
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingGeoRectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#boundingGeoRectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle() const
    ritual = 'ritual_ZNK17QGeoCirclePrivate20boundingGeoRectangleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate20boundingGeoRectangleEv'
    address = self.uglySide.call(ritual)
    from . import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def crossNorthPole(self) -> bool:
    """
    Calls Qt's 'bool QGeoCirclePrivate::crossNorthPole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#crossNorthPole
    """
    #  bool QGeoCirclePrivate::crossNorthPole() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoCirclePrivate14crossNorthPoleEv',
    )

  def crossSouthPole(self) -> bool:
    """
    Calls Qt's 'bool QGeoCirclePrivate::crossSouthPole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#crossSouthPole
    """
    #  bool QGeoCirclePrivate::crossSouthPole() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoCirclePrivate14crossSouthPoleEv',
    )

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoCirclePrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoCirclePrivate::clone() const
    ritual = 'ritual_ZNK17QGeoCirclePrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QGeoShapePrivate._cuteAt(address)

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoCirclePrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoCirclePrivate::hash(size_t seed) const
    ritual = 'ritual_ZNK17QGeoCirclePrivate4hashEm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoCirclePrivate4hashEm'
    return self.uglySide.call(ritual, seed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setCenter(self, c: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCirclePrivate::setCenter(const QGeoCoordinate &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#setCenter

    Parameters
    ----------

    c : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCirclePrivate::setCenter(const QGeoCoordinate &c)
    self.uglySide.call(
        'ritual_ZN17QGeoCirclePrivate9setCenterERK14QGeoCoordinate',
        self._valueOf(c),
    )

  @overload(float)
  def setRadius(self, r: float) -> None:
    """
    Calls Qt's 'void QGeoCirclePrivate::setRadius(const qreal r)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocircleprivate.html#setRadius

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  void QGeoCirclePrivate::setRadius(const qreal r)
    self.uglySide.call('ritual_ZN17QGeoCirclePrivate9setRadiusEd', r)

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
    Notes what was given, for Qt's 'QGeoCirclePrivate::QGeoCirclePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#QGeoCirclePrivate
    """
    #  QGeoCirclePrivate::QGeoCirclePrivate()
    self._noteCreation(QGeoCirclePrivate, lambda: Rituals.call(
        'ritual_ZN17QGeoCirclePrivateC1Ev',
    ))

  @overload(QGeoCoordinate, float)
  def __init__(self, center: QGeoCoordinate, radius: float) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCirclePrivate::QGeoCirclePrivate(const QGeoCoordinate &center, qreal
    radius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#QGeoCirclePrivate

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    radius : float
      Passed on as it is.
    """
    #  QGeoCirclePrivate::QGeoCirclePrivate(const QGeoCoordinate &center,
    #      qreal radius)
    self._noteCreation(QGeoCirclePrivate, lambda: Rituals.call(
        'ritual_ZN17QGeoCirclePrivateC1ERK14QGeoCoordinated',
        self._valueOf(center), radius,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCirclePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCirclePrivate::QGeoCirclePrivate(const QGeoCirclePrivate &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#QGeoCirclePrivate

    Parameters
    ----------

    other : QGeoCirclePrivate
      Passed on as a value: Qt reads the C++ QGeoCirclePrivate, which stays
      Python's own.
    """
    #  QGeoCirclePrivate::QGeoCirclePrivate(const QGeoCirclePrivate &other)
    self._noteCreation(QGeoCirclePrivate, lambda: Rituals.call(
        'ritual_ZN17QGeoCirclePrivateC1ERKS_', self._valueOf(other),
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

  def updateBoundingBox(self) -> None:
    """
    Calls Qt's 'void QGeoCirclePrivate::updateBoundingBox()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#updateBoundingBox
    """
    #  void QGeoCirclePrivate::updateBoundingBox()
    self.uglySide.call('ritual_ZN17QGeoCirclePrivate17updateBoundingBoxEv')

  @overload(QGeoCoordinate)
  def extendCircle(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCirclePrivate::extendCircle(const QGeoCoordinate
    &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocircleprivate.html#extendCircle

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCirclePrivate::extendCircle(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN17QGeoCirclePrivate12extendCircleERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )
