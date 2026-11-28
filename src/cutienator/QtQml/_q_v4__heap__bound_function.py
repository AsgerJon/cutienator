"""
QV4::Heap::BoundFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::BoundFunction to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoundFunction(QV4.Heap.JavaScriptFunctionObject, QV4.Heap.BoundFunctionData):
  """
  The cute side of Qt's QV4::Heap::BoundFunction: a plain Python object
  standing in front of one C++ QV4::Heap::BoundFunction.

  It is built on the cute 'QV4::Heap::JavaScriptFunctionObject', as Qt's
  QV4::Heap::BoundFunction is built on Qt's
  QV4::Heap::JavaScriptFunctionObject, and has everything that class has. It
  is built on the cute 'QV4::Heap::BoundFunctionData' as well, as Qt's
  QV4::Heap::BoundFunction is built on Qt's QV4::Heap::BoundFunctionData too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::BoundFunction that has a ritual and that
  Python can call so far, 2 names in all: 'markObjects', 'init'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What to expect
  --------------

  - The C++ QV4::Heap::BoundFunction is created at the first use, not by
    'QV4::Heap::BoundFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::BoundFunction.
  """

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
    Calls Qt's 'void QV4::Heap::BoundFunction::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-boundfunction.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::BoundFunction::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap13BoundFunction11markObjectsEPNS0_4BaseEPNS_9Mar'
        'kStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::BoundFunction'

  #  Qt's QV4::Heap::BoundFunction is built on more than one class. The part
  #  of a C++ QV4::Heap::BoundFunction that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::BoundFunctionData':
          'ritual_cast_QV4_Heap_BoundFunction_QV4_Heap_BoundFunctionData',
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

  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.MemberData'],
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.MemberData'])
  @overload(NoneType, WAIT['QV4.Value'], NoneType)
  def init(
      self,
      target: Optional[QV4.FunctionObject],
      boundThis: QV4.Value,
      boundArgs: Optional[QV4.MemberData],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::BoundFunction::init(QV4::FunctionObject
    *target, const Value &boundThis, QV4::MemberData *boundArgs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-boundfunction.html#init

    Parameters
    ----------

    target : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    boundThis : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    boundArgs : Optional[QV4.MemberData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::BoundFunction::init(QV4::FunctionObject *target, const
    #      Value &boundThis, QV4::MemberData *boundArgs)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13BoundFunction4initEPNS_14FunctionObjectERKNS_5'
        'ValueEPNS_10MemberDataE',
        self._addressOf(target), self._valueOf(boundThis),
        self._addressOf(boundArgs),
    )
