"""
QV4::Heap::PromiseObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::PromiseObject to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PromiseObject(QV4.Heap.Object, QV4.Heap.PromiseObjectData):
  """
  The cute side of Qt's QV4::Heap::PromiseObject: a plain Python object
  standing in front of one C++ QV4::Heap::PromiseObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::PromiseObject is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::PromiseObjectData' as well, as Qt's QV4::Heap::PromiseObject is
  built on Qt's QV4::Heap::PromiseObjectData too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::PromiseObject that has a ritual and that
  Python can call so far, 7 names in all: 'markObjects', 'init', 'setState',
  'isSettled', 'isPending', 'isFulfilled', 'isRejected'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Heap::PromiseObject is created at the first use, not by
    'QV4::Heap::PromiseObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::PromiseObject.
  - Each name of Qt's QV4::Heap::PromiseObject that has no cute function yet,
    'triggerFullfillReactions', 'triggerRejectReactions', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::PromiseObject, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class State(CuteNum):
    """
    The enum 'QV4::Heap::PromiseObject::State' of Qt, with the 3 names Qt
    gives in it.
    """

    Pending = Kee[int](0)
    Fulfilled = Kee[int](1)
    Rejected = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::PromiseObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::PromiseObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap13PromiseObject11markObjectsEPNS0_4BaseEPNS_9Mar'
        'kStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::PromiseObject'

  #  Qt's QV4::Heap::PromiseObject is built on more than one class. The part
  #  of a C++ QV4::Heap::PromiseObject that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::PromiseObjectData':
          'ritual_cast_QV4_Heap_PromiseObject_QV4_Heap_PromiseObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSettled(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::PromiseObject::isSettled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#isSettled
    """
    #  bool QV4::Heap::PromiseObject::isSettled() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13PromiseObject9isSettledEv',
    )

  def isPending(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::PromiseObject::isPending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#isPending
    """
    #  bool QV4::Heap::PromiseObject::isPending() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13PromiseObject9isPendingEv',
    )

  def isFulfilled(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::PromiseObject::isFulfilled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#isFulfilled
    """
    #  bool QV4::Heap::PromiseObject::isFulfilled() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13PromiseObject11isFulfilledEv',
    )

  def isRejected(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::PromiseObject::isRejected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#isRejected
    """
    #  bool QV4::Heap::PromiseObject::isRejected() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13PromiseObject10isRejectedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(State)
  def setState(self, a0: State) -> None:
    """
    Calls Qt's 'void QV4::Heap::PromiseObject::setState(State a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#setState

    Parameters
    ----------

    a0 : State
      Passed on as its number.
    """
    #  void QV4::Heap::PromiseObject::setState(State a0)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13PromiseObject8setStateENS1_5StateE', a0.value,
    )

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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def init(self, e: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::Heap::PromiseObject::init(ExecutionEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-promiseobject.html#init

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::PromiseObject::init(ExecutionEngine *e)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13PromiseObject4initEPNS_15ExecutionEngineE',
        self._addressOf(e),
    )

  @staticmethod
  def triggerFullfillReactions(*__, **_) -> Never:
    """
    Qt's 'void
    QV4::Heap::PromiseObject::triggerFullfillReactions(ExecutionEngine *e)':
    leans on 'QV4::PromiseReaction::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.PromiseObject.triggerFullfillReactions' has no cute "
        "function yet. Qt's 'void "
        "QV4::Heap::PromiseObject::triggerFullfillReactions(ExecutionEngine "
        "*e)': leans on 'QV4::PromiseReaction::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def triggerRejectReactions(*__, **_) -> Never:
    """
    Qt's 'void
    QV4::Heap::PromiseObject::triggerRejectReactions(ExecutionEngine *e)':
    leans on 'QV4::PromiseReaction::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.PromiseObject.triggerRejectReactions' has no cute "
        "function yet. Qt's 'void "
        "QV4::Heap::PromiseObject::triggerRejectReactions(ExecutionEngine "
        "*e)': leans on 'QV4::PromiseReaction::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
