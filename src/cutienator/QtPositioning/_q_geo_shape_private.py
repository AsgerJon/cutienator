"""
QGeoShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeoshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoShapePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QGeoShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCoordinate, QGeoRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoShapePrivate(QSharedData):
  """
  The cute side of Qt's QGeoShapePrivate: a plain Python object standing in
  front of one C++ QGeoShapePrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoShapePrivate is built on
  Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoShapePrivate that has a ritual and that Python
  can call so far, 7 names in all: 'isValid', 'isEmpty', 'contains',
  'center', 'boundingGeoRectangle', 'clone', 'hash'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoShapePrivate::~QGeoShapePrivate()': the destructor: Python
    never removes a C++ QGeoShapePrivate.
  - Qt's 'bool QGeoShapePrivate::operator==(const QGeoShapePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoShapePrivate is created at the first use, not by
    'QGeoShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoShapePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoShapePrivate'

  #  A C++ QGeoShapePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoShapePrivate'

  #  The functions Qt calls itself that QGeoShapePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK16QGeoShapePrivate7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isEmpty': (
          ('_ZNK16QGeoShapePrivate7isEmptyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'contains': (
          ('_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'center': (
          ('_ZNK16QGeoShapePrivate6centerEv',
           ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           ()),
      ),
      'boundingGeoRectangle': (
          ('_ZNK16QGeoShapePrivate20boundingGeoRectangleEv',
           ('address', 'value', 'QtPositioning:QGeoRectangle'),
           ()),
      ),
      'clone': (
          ('_ZNK16QGeoShapePrivate5cloneEv',
           ('address', 'address', 'QtPositioning:QGeoShapePrivate'),
           ()),
      ),
      'hash': (
          ('_ZNK16QGeoShapePrivate4hashEm',
           ('size_t', 'number', ''),
           (
               ('size_t', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoShapePrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#isValid
    """
    #  bool QGeoShapePrivate::isValid() const
    return self.uglySide.call('ritual_ZNK16QGeoShapePrivate7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoShapePrivate::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#isEmpty
    """
    #  bool QGeoShapePrivate::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QGeoShapePrivate7isEmptyEv')

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoShapePrivate::contains(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoShapePrivate::contains(const QGeoCoordinate &coordinate)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoShapePrivate::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoShapePrivate::center() const
    address = self.uglySide.call('ritual_ZNK16QGeoShapePrivate6centerEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingGeoRectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoShapePrivate::boundingGeoRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoshapeprivate.html#boundingGeoRectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoShapePrivate::boundingGeoRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoShapePrivate20boundingGeoRectangleEv',
    )
    from . import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoShapePrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoShapePrivate::clone() const
    address = self.uglySide.call('ritual_ZNK16QGeoShapePrivate5cloneEv')
    return QGeoShapePrivate._cuteAt(address)

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoShapePrivate::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshapeprivate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoShapePrivate::hash(size_t seed) const
    return self.uglySide.call('ritual_ZNK16QGeoShapePrivate4hashEm', seed)

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

  @overload(QGeoShape.ShapeType)
  def __init__(self, type: QGeoShape.ShapeType) -> None:
    """
    Notes what was given, for Qt's
    'QGeoShapePrivate::QGeoShapePrivate(QGeoShape::ShapeType type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoshapeprivate.html#QGeoShapePrivate

    Parameters
    ----------

    type : QGeoShape.ShapeType
      Passed on as its number.
    """
    #  QGeoShapePrivate::QGeoShapePrivate(QGeoShape::ShapeType type)
    self._noteCreation(QGeoShapePrivate, lambda: Rituals.call(
        'ritual_ZN16QGeoShapePrivateC1EN9QGeoShape9ShapeTypeE', type.value,
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
