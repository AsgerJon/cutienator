"""
QV4::BitVector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4util_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::BitVector to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class BitVector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::BitVector: a plain Python object standing in
  front of one C++ QV4::BitVector.

  C++ hands a QV4::BitVector around as a copy, so every C++ QV4::BitVector
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::BitVector that has a ritual and that Python can
  call so far, 9 names in all: 'clear', 'reserve', 'size', 'resize',
  'assign', 'findNext', 'at', 'setBit', 'clearBit'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::BitVector::~BitVector()': the destructor: Python removes its
    C++ QV4::BitVector by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::BitVector is created at the first use, not by
    'QV4::BitVector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::BitVector back gives a copy the ritual made for
    Python, in a new cute QV4::BitVector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::BitVector'

  #  Qt's '~QV4::BitVector()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::BitVector behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV49BitVectorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QV4::BitVector::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#size
    """
    #  int QV4::BitVector::size() const
    return self.uglySide.call('ritual_ZNK3QV49BitVector4sizeEv')

  @overload(int, bool, bool)
  def findNext(self, start: int, value: bool, wrapAround: bool) -> int:
    """
    Calls Qt's 'int QV4::BitVector::findNext(int start, bool value, bool
    wrapAround) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#findNext

    Parameters
    ----------

    start : int
      Passed on as it is.

    value : bool
      Passed on as it is.

    wrapAround : bool
      Passed on as it is.
    """
    #  int QV4::BitVector::findNext(int start, bool value, bool wrapAround)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV49BitVector8findNextEibb', start, value, wrapAround,
    )

  @overload(int)
  def at(self, idx: int) -> bool:
    """
    Calls Qt's 'bool QV4::BitVector::at(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#at

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  bool QV4::BitVector::at(int idx) const
    return self.uglySide.call('ritual_ZNK3QV49BitVector2atEi', idx)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBit(self, idx: int) -> None:
    """
    Calls Qt's 'void QV4::BitVector::setBit(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#setBit

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QV4::BitVector::setBit(int idx)
    self.uglySide.call('ritual_ZN3QV49BitVector6setBitEi', idx)

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
  @overload(int)
  @overload(int, bool)
  def __init__(self, size: int = 0, value: bool = False) -> None:
    """
    Notes what was given, for Qt's 'QV4::BitVector::BitVector(int size, bool
    value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#BitVector

    Parameters
    ----------

    size : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    value : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QV4::BitVector::BitVector(int size, bool value)
    self._noteCreation(BitVector, lambda: Rituals.call(
        'ritual_ZN3QV49BitVectorC1Eib', size, value,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::BitVector::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#clear
    """
    #  void QV4::BitVector::clear()
    self.uglySide.call('ritual_ZN3QV49BitVector5clearEv')

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QV4::BitVector::reserve(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QV4::BitVector::reserve(int size)
    self.uglySide.call('ritual_ZN3QV49BitVector7reserveEi', size)

  @overload(int)
  def resize(self, newSize: int) -> None:
    """
    Calls Qt's 'void QV4::BitVector::resize(int newSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#resize

    Parameters
    ----------

    newSize : int
      Passed on as it is.
    """
    #  void QV4::BitVector::resize(int newSize)
    self.uglySide.call('ritual_ZN3QV49BitVector6resizeEi', newSize)

  @overload(int, bool)
  def resize(self, newSize: int, newValue: bool) -> None:
    """
    Calls Qt's 'void QV4::BitVector::resize(int newSize, bool newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#resize

    Parameters
    ----------

    newSize : int
      Passed on as it is.

    newValue : bool
      Passed on as it is.
    """
    #  void QV4::BitVector::resize(int newSize, bool newValue)
    self.uglySide.call(
        'ritual_ZN3QV49BitVector6resizeEib', newSize, newValue,
    )

  @overload(int, bool)
  def assign(self, newSize: int, value: bool) -> None:
    """
    Calls Qt's 'void QV4::BitVector::assign(int newSize, bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#assign

    Parameters
    ----------

    newSize : int
      Passed on as it is.

    value : bool
      Passed on as it is.
    """
    #  void QV4::BitVector::assign(int newSize, bool value)
    self.uglySide.call('ritual_ZN3QV49BitVector6assignEib', newSize, value)

  @overload(int)
  def clearBit(self, idx: int) -> None:
    """
    Calls Qt's 'void QV4::BitVector::clearBit(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-bitvector.html#clearBit

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QV4::BitVector::clearBit(int idx)
    self.uglySide.call('ritual_ZN3QV49BitVector8clearBitEi', idx)
