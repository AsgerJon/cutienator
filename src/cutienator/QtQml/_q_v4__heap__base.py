"""
QV4::Heap::Base binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4heap_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Heap::Base to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Base(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Heap::Base: a plain Python object standing in
  front of one C++ QV4::Heap::Base.

  What exists
  -----------

  Every function of Qt's QV4::Heap::Base that has a ritual and that Python
  can call so far, 12 names in all: 'markObjects', 'asReturnedValue', 'mark',
  'isMarked', 'setMarkBit', 'inUse', 'init', 'destroy',
  '_checkIsInitialized', '_checkIsDestroyed', '_setInitialized',
  '_setDestroyed'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QV4::Heap::Base::operator new(size_t a0, Managed *m)': an
    operator Python has no name for.
  - Qt's 'void *QV4::Heap::Base::operator new(size_t a0, Base *m)': an
    operator Python has no name for.
  - Qt's 'void QV4::Heap::Base::operator delete(void *a0, Base *a1)': an
    operator Python has no name for.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QV4::Heap::Base is created at the first use, not by
    'QV4::Heap::Base(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::Base.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, WAIT['QV4.MarkStack'])
  @overload(THIS, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(a0: Optional[Base], a1: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::markObjects(Base *a0, MarkStack *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#markObjects

    Parameters
    ----------

    a0 : Optional[Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::Base::markObjects(Base *a0, MarkStack *a1)
    Rituals.call(
        'ritual_ZN3QV44Heap4Base11markObjectsEPS1_PNS_9MarkStackE',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::Base'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def asReturnedValue(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Heap::Base::asReturnedValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#asReturnedValue
    """
    #  ReturnedValue QV4::Heap::Base::asReturnedValue() const
    return self.uglySide.call('ritual_ZNK3QV44Heap4Base15asReturnedValueEv')

  def isMarked(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Base::isMarked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#isMarked
    """
    #  bool QV4::Heap::Base::isMarked() const
    return self.uglySide.call('ritual_ZNK3QV44Heap4Base8isMarkedEv')

  def inUse(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Base::inUse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#inUse
    """
    #  bool QV4::Heap::Base::inUse() const
    return self.uglySide.call('ritual_ZNK3QV44Heap4Base5inUseEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setMarkBit(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::setMarkBit()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#setMarkBit
    """
    #  void QV4::Heap::Base::setMarkBit()
    self.uglySide.call('ritual_ZN3QV44Heap4Base10setMarkBitEv')

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

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::mark(QV4::MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::Base::mark(QV4::MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV44Heap4Base4markEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#init
    """
    #  void QV4::Heap::Base::init()
    self.uglySide.call('ritual_ZN3QV44Heap4Base4initEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#destroy
    """
    #  void QV4::Heap::Base::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap4Base7destroyEv')

  def _checkIsInitialized(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::_checkIsInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-base.html#_checkIsInitialized
    """
    #  void QV4::Heap::Base::_checkIsInitialized()
    self.uglySide.call('ritual_ZN3QV44Heap4Base19_checkIsInitializedEv')

  def _checkIsDestroyed(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::_checkIsDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-base.html#_checkIsDestroyed
    """
    #  void QV4::Heap::Base::_checkIsDestroyed()
    self.uglySide.call('ritual_ZN3QV44Heap4Base17_checkIsDestroyedEv')

  def _setInitialized(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::_setInitialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#_setInitialized
    """
    #  void QV4::Heap::Base::_setInitialized()
    self.uglySide.call('ritual_ZN3QV44Heap4Base15_setInitializedEv')

  def _setDestroyed(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Base::_setDestroyed()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-base.html#_setDestroyed
    """
    #  void QV4::Heap::Base::_setDestroyed()
    self.uglySide.call('ritual_ZN3QV44Heap4Base13_setDestroyedEv')
