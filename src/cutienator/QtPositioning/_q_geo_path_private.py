"""
QGeoPathPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPathPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

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


class QGeoPathPrivate(QGeoPathPrivateBase):
  """
  The cute side of Qt's QGeoPathPrivate: a plain Python object standing in
  front of one C++ QGeoPathPrivate.

  It is built on the cute 'QGeoPathPrivateBase', as Qt's QGeoPathPrivate is
  built on Qt's QGeoPathPrivateBase, and has everything that class has.

  C++ hands a QGeoPathPrivate around as a copy, so every C++ QGeoPathPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPathPrivate that has a ritual and that Python
  can call so far, 6 names in all: 'clone', 'contains', 'hash',
  'lineContains', 'width', 'setWidth'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPathPrivate::~QGeoPathPrivate()': the destructor: Python
    removes its C++ QGeoPathPrivate by it, and has no other use for it.
  - Qt's 'bool QGeoPathPrivate::operator==(const QGeoShapePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoPathPrivate is created at the first use, not by
    'QGeoPathPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPathPrivate back gives a copy the ritual made for
    Python, in a new cute QGeoPathPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPathPrivate'

  #  A C++ QGeoPathPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoPathPrivate'

  #  Qt's '~QGeoPathPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoPathPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QGeoPathPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoPathPrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoPathPrivate::clone() const
    ritual = 'ritual_ZNK15QGeoPathPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGeoPathPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QGeoShapePrivate._cuteAt(address)

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPathPrivate::contains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPathPrivate::contains(const QGeoCoordinate &coordinate) const
    ritual = 'ritual_ZNK15QGeoPathPrivate8containsERK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGeoPathPrivate8containsERK14QGeoCoordinate'
    return self.uglySide.call(ritual, self._valueOf(coordinate))

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoPathPrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoPathPrivate::hash(size_t seed) const
    ritual = 'ritual_ZNK15QGeoPathPrivate4hashEm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGeoPathPrivate4hashEm'
    return self.uglySide.call(ritual, seed)

  @overload(QGeoCoordinate)
  def lineContains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPathPrivate::lineContains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#lineContains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPathPrivate::lineContains(const QGeoCoordinate &coordinate)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QGeoPathPrivate12lineContainsERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def width(self) -> float:
    """
    Calls Qt's 'qreal QGeoPathPrivate::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#width
    """
    #  qreal QGeoPathPrivate::width() const
    return self.uglySide.call('ritual_ZNK15QGeoPathPrivate5widthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGeoPathPrivate::setWidth(const qreal &width)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivate.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGeoPathPrivate::setWidth(const qreal &width)
    self.uglySide.call('ritual_ZN15QGeoPathPrivate8setWidthERKd', width)

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
    Notes what was given, for Qt's 'QGeoPathPrivate::QGeoPathPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivate.html#QGeoPathPrivate
    """
    #  QGeoPathPrivate::QGeoPathPrivate()
    self._noteCreation(QGeoPathPrivate, lambda: Rituals.call(
        'ritual_ZN15QGeoPathPrivateC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  @overload(QList[QGeoCoordinate], float)
  def __init__(
      self,
      path: QList[QGeoCoordinate],
      width: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoPathPrivate::QGeoPathPrivate(const
    QList<QGeoCoordinate> &path, const qreal width)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivate.html#QGeoPathPrivate

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    width : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QGeoPathPrivate::QGeoPathPrivate(const QList<QGeoCoordinate> &path,
    #      const qreal width)
    self._noteCreation(QGeoPathPrivate, lambda: Rituals.call(
        'ritual_ZN15QGeoPathPrivateC1ERK5QListI14QGeoCoordinateEd',
        self._valueOf(path), width,
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
