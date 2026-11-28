"""
QV4::SharedArrayBufferPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::SharedArrayBufferPrototype to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class SharedArrayBufferPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::SharedArrayBufferPrototype: a plain Python
  object standing in front of one C++ QV4::SharedArrayBufferPrototype.

  It is built on the cute 'QV4::Object', as Qt's
  QV4::SharedArrayBufferPrototype is built on Qt's QV4::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SharedArrayBufferPrototype that has a ritual
  and that Python can call so far, 4 names in all: 'init',
  'method_get_byteLength', 'method_slice', 'slice'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::SharedArrayBufferPrototype is created at the first use, not
    by 'QV4::SharedArrayBufferPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SharedArrayBufferPrototype.
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
  def method_get_byteLength(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::SharedArrayBufferPrototype::method_get_byteLength(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybufferprototype.html

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
    #  ReturnedValue
    #      QV4::SharedArrayBufferPrototype::method_get_byteLength(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV426SharedArrayBufferPrototype21method_get_byteLengthEP'
        'KNS_14FunctionObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_slice(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::SharedArrayBufferPrototype::method_slice(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybufferprototype.html#method_slice

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
    #  ReturnedValue QV4::SharedArrayBufferPrototype::method_slice(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV426SharedArrayBufferPrototype12method_sliceEPKNS_14Fun'
        'ctionObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int, bool)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int, bool)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int, bool)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int, bool)
  @overload(NoneType, QV4.Value, QV4.Value, int, bool)
  @overload(NoneType, QV4.Value, NoneType, int, bool)
  @overload(NoneType, NoneType, QV4.Value, int, bool)
  @overload(NoneType, NoneType, NoneType, int, bool)
  def slice(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
      shared: bool,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SharedArrayBufferPrototype::slice(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int argc,
    bool shared)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybufferprototype.html#slice

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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

    shared : bool
      Passed on as it is.
    """
    #  ReturnedValue QV4::SharedArrayBufferPrototype::slice(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc, bool shared)
    return Rituals.call(
        'ritual_ZN3QV426SharedArrayBufferPrototype5sliceEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_ib',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc, shared,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SharedArrayBufferPrototype'

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
    Calls Qt's 'void QV4::SharedArrayBufferPrototype::init(ExecutionEngine
    *engine, Object *ctor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybufferprototype.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctor : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SharedArrayBufferPrototype::init(ExecutionEngine *engine,
    #      Object *ctor)
    self.uglySide.call(
        'ritual_ZN3QV426SharedArrayBufferPrototype4initEPNS_15ExecutionEngi'
        'neEPNS_6ObjectE',
        self._addressOf(engine), self._addressOf(ctor),
    )
