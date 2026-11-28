"""
QV4::HeapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::HeapItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class HeapItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::HeapItem: a plain Python object standing in
  front of one C++ QV4::HeapItem.

  C++ hands a QV4::HeapItem around as a copy, so every C++ QV4::HeapItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::HeapItem that has a ritual and that Python can
  call so far, 4 names in all: 'isBlack', 'isInUse', 'setAllocatedSlots',
  'size'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Heap::Base *QV4::HeapItem::operator QV4::Heap::Base *()': an
    operator Python has no name for.
  - Qt's 'Chunk *QV4::HeapItem::chunk() const': gives 'QV4::Chunk', which has
    no cute class yet.
  - Qt's 'QV4::HeapItem::~HeapItem()': the destructor: Python removes its C++
    QV4::HeapItem by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QV4::HeapItem is created at the first use, not by
    'QV4::HeapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::HeapItem back gives a copy the ritual made for
    Python, in a new cute QV4::HeapItem.
  - Each name of Qt's QV4::HeapItem that has no cute function yet, 'as_',
    'chunk', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::HeapItem'

  #  Qt's '~QV4::HeapItem()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::HeapItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV48HeapItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isBlack(self) -> bool:
    """
    Calls Qt's 'bool QV4::HeapItem::isBlack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heapitem.html#isBlack
    """
    #  bool QV4::HeapItem::isBlack() const
    return self.uglySide.call('ritual_ZNK3QV48HeapItem7isBlackEv')

  def isInUse(self) -> bool:
    """
    Calls Qt's 'bool QV4::HeapItem::isInUse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heapitem.html#isInUse
    """
    #  bool QV4::HeapItem::isInUse() const
    return self.uglySide.call('ritual_ZNK3QV48HeapItem7isInUseEv')

  def size(self) -> int:
    """
    Calls Qt's 'size_t QV4::HeapItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heapitem.html#size
    """
    #  size_t QV4::HeapItem::size() const
    return self.uglySide.call('ritual_ZNK3QV48HeapItem4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAllocatedSlots(self, nSlots: int) -> None:
    """
    Calls Qt's 'void QV4::HeapItem::setAllocatedSlots(size_t nSlots)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heapitem.html#setAllocatedSlots

    Parameters
    ----------

    nSlots : int
      Passed on as it is.
    """
    #  void QV4::HeapItem::setAllocatedSlots(size_t nSlots)
    self.uglySide.call('ritual_ZN3QV48HeapItem17setAllocatedSlotsEm', nSlots)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def as_(*__, **_) -> Never:
    """
    Qt's 'QV4::HeapItem::as': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.HeapItem.as_' has no cute function yet. Qt's "
        "'QV4::HeapItem::as': a template: a pattern and no single function.")

  @staticmethod
  def chunk(*__, **_) -> Never:
    """
    Qt's 'Chunk *QV4::HeapItem::chunk() const': gives 'QV4::Chunk', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.HeapItem.chunk' has no cute function yet. Qt's 'Chunk "
        "*QV4::HeapItem::chunk() const': gives 'QV4::Chunk', which has no "
        "cute class yet.")
