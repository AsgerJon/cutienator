"""
QIndexMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QIndexMapper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QIndexMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIndexMapper: a plain Python object standing in front
  of one C++ QIndexMapper.

  C++ hands a QIndexMapper around as a copy, so every C++ QIndexMapper behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIndexMapper that has a ritual and that Python can
  call so far, 11 names in all: 'count', '__getitem__', 'indexOf', 'isValid',
  'isEmpty', 'append', 'first', 'last', 'from_', 'to', 'cost'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIndexMapper::QIndexMapper(const QList<int> &vec)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QIndexMapper::~QIndexMapper()': the destructor: Python removes its
    C++ QIndexMapper by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QIndexMapper is created at the first use, not by
    'QIndexMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIndexMapper back gives a copy the ritual made for
    Python, in a new cute QIndexMapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIndexMapper'

  #  Qt's '~QIndexMapper()'. Naming it makes this a value class: Python owns
  #  every C++ QIndexMapper behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QIndexMapperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#count
    """
    #  int QIndexMapper::count() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper5countEv')

  @overload(int)
  def indexOf(self, x: int) -> int:
    """
    Calls Qt's 'int QIndexMapper::indexOf(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#indexOf

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QIndexMapper::indexOf(int x) const
    return self.uglySide.call('ritual_ZNK12QIndexMapper7indexOfEi', x)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QIndexMapper::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#isValid
    """
    #  bool QIndexMapper::isValid() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QIndexMapper::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#isEmpty
    """
    #  bool QIndexMapper::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper7isEmptyEv')

  def first(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#first
    """
    #  int QIndexMapper::first() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper5firstEv')

  def last(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#last
    """
    #  int QIndexMapper::last() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper4lastEv')

  def from_(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#from
    """
    #  int QIndexMapper::from() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper4fromEv')

  def to(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#to
    """
    #  int QIndexMapper::to() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper2toEv')

  def cost(self) -> int:
    """
    Calls Qt's 'int QIndexMapper::cost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#cost
    """
    #  int QIndexMapper::cost() const
    return self.uglySide.call('ritual_ZNK12QIndexMapper4costEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, index: int) -> int:
    """
    Calls Qt's 'int QIndexMapper::operator[](int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#operator[]

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QIndexMapper::operator[](int index) const
    return self.uglySide.call('ritual_ZNK12QIndexMapperixEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QIndexMapper::QIndexMapper()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#QIndexMapper
    """
    #  QIndexMapper::QIndexMapper()
    self._noteCreation(QIndexMapper, lambda: Rituals.call(
        'ritual_ZN12QIndexMapperC1Ev',
    ))

  @overload(int, int)
  def __init__(self, f: int, t: int) -> None:
    """
    Notes what was given, for Qt's 'QIndexMapper::QIndexMapper(int f, int
    t)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#QIndexMapper

    Parameters
    ----------

    f : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  QIndexMapper::QIndexMapper(int f, int t)
    self._noteCreation(QIndexMapper, lambda: Rituals.call(
        'ritual_ZN12QIndexMapperC1Eii', f, t,
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

  @overload(int)
  def append(self, x: int) -> None:
    """
    Calls Qt's 'void QIndexMapper::append(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qindexmapper.html#append

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QIndexMapper::append(int x)
    self.uglySide.call('ritual_ZN12QIndexMapper6appendEi', x)
