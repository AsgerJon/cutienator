"""
QV4::ErrorPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ErrorPrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class ErrorPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::ErrorPrototype: a plain Python object standing
  in front of one C++ QV4::ErrorPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::ErrorPrototype is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ErrorPrototype that has a ritual and that
  Python can call so far, 2 names in all: 'init', 'method_toString'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What to expect
  --------------

  - The C++ QV4::ErrorPrototype is created at the first use, not by
    'QV4::ErrorPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ErrorPrototype.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_toString(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ErrorPrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-errorprototype.html#method_toString

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ErrorPrototype::method_toString(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV414ErrorPrototype15method_toStringEPKNS_14FunctionObje'
        'ctEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ErrorPrototype'

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

  @overload(WAIT['QV4.ExecutionEngine'], QV4.Object)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QV4.Object)
  @overload(NoneType, NoneType)
  def init(
      self,
      engine: Optional[QV4.ExecutionEngine],
      ctor: Optional[QV4.Object],
  ) -> None:
    """
    Calls Qt's 'void QV4::ErrorPrototype::init(ExecutionEngine *engine,
    Object *ctor)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorprototype.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctor : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ErrorPrototype::init(ExecutionEngine *engine, Object *ctor)
    self.uglySide.call(
        'ritual_ZN3QV414ErrorPrototype4initEPNS_15ExecutionEngineEPNS_6Obje'
        'ctE',
        self._addressOf(engine), self._addressOf(ctor),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], QV4.Object, QV4.Object,
      QV4.Heap.ErrorObject.ErrorType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], QV4.Object, NoneType,
      QV4.Heap.ErrorObject.ErrorType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, QV4.Object,
      QV4.Heap.ErrorObject.ErrorType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, NoneType,
      QV4.Heap.ErrorObject.ErrorType,
  )
  @overload(NoneType, QV4.Object, QV4.Object, QV4.Heap.ErrorObject.ErrorType)
  @overload(NoneType, QV4.Object, NoneType, QV4.Heap.ErrorObject.ErrorType)
  @overload(NoneType, NoneType, QV4.Object, QV4.Heap.ErrorObject.ErrorType)
  @overload(NoneType, NoneType, NoneType, QV4.Heap.ErrorObject.ErrorType)
  def init(
      engine: Optional[QV4.ExecutionEngine],
      ctor: Optional[QV4.Object],
      obj: Optional[QV4.Object],
      t: QV4.Heap.ErrorObject.ErrorType,
  ) -> None:
    """
    Calls Qt's 'void QV4::ErrorPrototype::init(ExecutionEngine *engine,
    Object *ctor, Object *obj, Heap::ErrorObject::ErrorType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorprototype.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctor : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    t : QV4.Heap.ErrorObject.ErrorType
      Passed on as its number.
    """
    #  void QV4::ErrorPrototype::init(ExecutionEngine *engine, Object *ctor,
    #      Object *obj, Heap::ErrorObject::ErrorType t)
    Rituals.call(
        'ritual_ZN3QV414ErrorPrototype4initEPNS_15ExecutionEngineEPNS_6Obje'
        'ctES4_NS_4Heap11ErrorObject9ErrorTypeE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(ctor),
        CuteMixin._addressOf(obj), t.value,
    )
