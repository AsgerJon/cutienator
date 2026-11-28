"""
QV4::Heap::PromiseReaction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::PromiseReaction to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class PromiseReaction(QV4.Heap.Object, QV4.Heap.PromiseReactionData):
  """
  The cute side of Qt's QV4::Heap::PromiseReaction: a plain Python object
  standing in front of one C++ QV4::Heap::PromiseReaction.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::PromiseReaction is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::PromiseReactionData' as well, as Qt's
  QV4::Heap::PromiseReaction is built on Qt's QV4::Heap::PromiseReactionData
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::PromiseReaction that has a ritual and
  that Python can call so far, 2 names in all: 'markObjects',
  'triggerWithValue'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Heap::PromiseReaction is created at the first use, not by
    'QV4::Heap::PromiseReaction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::PromiseReaction.
  - Each name of Qt's QV4::Heap::PromiseReaction that has no cute function
    yet, 'createFulfillReaction', 'createRejectReaction', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::PromiseReaction, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'QV4::Heap::PromiseReaction::Type' of Qt, with the 3 names Qt
    gives in it.
    """

    Function = Kee[int](0)
    Identity = Kee[int](1)
    Thrower = Kee[int](2)

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
    Calls Qt's 'void QV4::Heap::PromiseReaction::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promisereaction.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::PromiseReaction::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap15PromiseReaction11markObjectsEPNS0_4BaseEPNS_9M'
        'arkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::PromiseReaction'

  #  Qt's QV4::Heap::PromiseReaction is built on more than one class. The
  #  part of a C++ QV4::Heap::PromiseReaction that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::PromiseReactionData':
          'ritual_cast_QV4_Heap_PromiseReaction_QV4_Heap_PromiseReactionData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Value'])
  @overload(NoneType, NoneType)
  def triggerWithValue(
      self,
      e: Optional[QV4.ExecutionEngine],
      value: Optional[QV4.Value],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::PromiseReaction::triggerWithValue(ExecutionEngine *e, const
    Value *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-promisereaction.html#triggerWithValue

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::PromiseReaction::triggerWithValue(ExecutionEngine *e,
    #      const Value *value)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15PromiseReaction16triggerWithValueEPNS_15Execut'
        'ionEngineEPKNS_5ValueE',
        self._addressOf(e), self._addressOf(value),
    )

  @staticmethod
  def createFulfillReaction(*__, **_) -> Never:
    """
    Qt's 'Heap::PromiseReaction
    *QV4::Heap::PromiseReaction::createFulfillReaction(ExecutionEngine *e,
    const QV4::PromiseCapability *capability, const QV4::FunctionObject
    *onFulfilled)': leans on 'QV4::PromiseReaction::static_vtbl', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.PromiseReaction.createFulfillReaction' has no cute "
        "function yet. Qt's 'Heap::PromiseReaction "
        "*QV4::Heap::PromiseReaction::createFulfillReaction(ExecutionEngine "
        "*e, const QV4::PromiseCapability *capability, const "
        "QV4::FunctionObject *onFulfilled)': leans on "
        "'QV4::PromiseReaction::static_vtbl', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def createRejectReaction(*__, **_) -> Never:
    """
    Qt's 'Heap::PromiseReaction
    *QV4::Heap::PromiseReaction::createRejectReaction(ExecutionEngine *e,
    const QV4::PromiseCapability *capability, const QV4::FunctionObject
    *onRejected)': leans on 'QV4::PromiseReaction::static_vtbl', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.PromiseReaction.createRejectReaction' has no cute "
        "function yet. Qt's 'Heap::PromiseReaction "
        "*QV4::Heap::PromiseReaction::createRejectReaction(ExecutionEngine "
        "*e, const QV4::PromiseCapability *capability, const "
        "QV4::FunctionObject *onRejected)': leans on "
        "'QV4::PromiseReaction::static_vtbl', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
