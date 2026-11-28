"""
QGeoRectanglePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeorectangle_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRectanglePrivate to be private: it declares the class in a
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


class QGeoRectanglePrivate(QGeoShapePrivate):
  """
  The cute side of Qt's QGeoRectanglePrivate: a plain Python object standing
  in front of one C++ QGeoRectanglePrivate.

  It is built on the cute 'QGeoShapePrivate', as Qt's QGeoRectanglePrivate is
  built on Qt's QGeoShapePrivate, and has everything that class has.

  C++ hands a QGeoRectanglePrivate around as a copy, so every C++
  QGeoRectanglePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRectanglePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'isValid', 'isEmpty', 'contains',
  'center', 'boundingGeoRectangle', 'extendRectangle', 'clone', 'hash'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRectanglePrivate::~QGeoRectanglePrivate()': the destructor:
    Python removes its C++ QGeoRectanglePrivate by it, and has no other use
    for it.
  - Qt's 'bool QGeoRectanglePrivate::operator==(const QGeoShapePrivate
    &other) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoRectanglePrivate is created at the first use, not by
    'QGeoRectanglePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRectanglePrivate back gives a copy the ritual
    made for Python, in a new cute QGeoRectanglePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRectanglePrivate'

  #  A C++ QGeoRectanglePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRectanglePrivate'

  #  Qt's '~QGeoRectanglePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoRectanglePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QGeoRectanglePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoRectanglePrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#isValid
    """
    #  bool QGeoRectanglePrivate::isValid() const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate7isValidEv'
    return self.uglySide.call(ritual)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoRectanglePrivate::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#isEmpty
    """
    #  bool QGeoRectanglePrivate::isEmpty() const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate7isEmptyEv'
    return self.uglySide.call(ritual)

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoRectanglePrivate::contains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoRectanglePrivate::contains(const QGeoCoordinate &coordinate)
    #      const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate8containsERK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QGeoRectanglePrivate8containsERK14QGeoCoordinate')
    return self.uglySide.call(ritual, self._valueOf(coordinate))

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectanglePrivate::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectanglePrivate::center() const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate6centerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate6centerEv'
    address = self.uglySide.call(ritual)
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingGeoRectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorectangleprivate.html#boundingGeoRectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle() const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate20boundingGeoRectangleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate20boundingGeoRectangleEv'
    address = self.uglySide.call(ritual)
    from . import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoRectanglePrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoRectanglePrivate::clone() const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QGeoShapePrivate._cuteAt(address)

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoRectanglePrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangleprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoRectanglePrivate::hash(size_t seed) const
    ritual = 'ritual_ZNK20QGeoRectanglePrivate4hashEm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGeoRectanglePrivate4hashEm'
    return self.uglySide.call(ritual, seed)

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
    'QGeoRectanglePrivate::QGeoRectanglePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorectangleprivate.html#QGeoRectanglePrivate
    """
    #  QGeoRectanglePrivate::QGeoRectanglePrivate()
    self._noteCreation(QGeoRectanglePrivate, lambda: Rituals.call(
        'ritual_ZN20QGeoRectanglePrivateC1Ev',
    ))

  @overload(QGeoCoordinate, QGeoCoordinate)
  def __init__(
      self,
      topLeft: QGeoCoordinate,
      bottomRight: QGeoCoordinate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoCoordinate
    &topLeft, const QGeoCoordinate &bottomRight)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorectangleprivate.html#QGeoRectanglePrivate

    Parameters
    ----------

    topLeft : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    bottomRight : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoCoordinate
    #      &topLeft, const QGeoCoordinate &bottomRight)
    self._noteCreation(QGeoRectanglePrivate, lambda: Rituals.call(
        'ritual_ZN20QGeoRectanglePrivateC1ERK14QGeoCoordinateS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoRectanglePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoRectanglePrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorectangleprivate.html#QGeoRectanglePrivate

    Parameters
    ----------

    other : QGeoRectanglePrivate
      Passed on as a value: Qt reads the C++ QGeoRectanglePrivate, which
      stays Python's own.
    """
    #  QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoRectanglePrivate
    #      &other)
    self._noteCreation(QGeoRectanglePrivate, lambda: Rituals.call(
        'ritual_ZN20QGeoRectanglePrivateC1ERKS_', self._valueOf(other),
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

  @overload(QGeoCoordinate)
  def extendRectangle(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectanglePrivate::extendRectangle(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorectangleprivate.html#extendRectangle

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectanglePrivate::extendRectangle(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN20QGeoRectanglePrivate15extendRectangleERK14QGeoCoordinat'
        'e',
        self._valueOf(coordinate),
    )
