"""
QV4::FunctionPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::FunctionPrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FunctionPrototype(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::FunctionPrototype: a plain Python object
  standing in front of one C++ QV4::FunctionPrototype.

  It is built on the cute 'QV4::FunctionObject', as Qt's
  QV4::FunctionPrototype is built on Qt's QV4::FunctionObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::FunctionPrototype that has a ritual and that
  Python can call so far, 7 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCall', 'method_toString', 'method_call', 'method_hasInstance'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 4 leans on 'QV4; 3 forbidden; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::FunctionPrototype is created at the first use, not by
    'QV4::FunctionPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::FunctionPrototype.
  - Each name of Qt's QV4::FunctionPrototype that has no cute function yet,
    'init', 'method_apply', 'method_bind', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def virtualCall(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionPrototype::virtualCall(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#virtualCall

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::FunctionPrototype::virtualCall(const FunctionObject
    #      *f, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV417FunctionPrototype11virtualCallEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
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
    Calls Qt's 'ReturnedValue QV4::FunctionPrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#method_toString

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
    #  ReturnedValue QV4::FunctionPrototype::method_toString(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV417FunctionPrototype15method_toStringEPKNS_14FunctionO'
        'bjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_call(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::FunctionPrototype::method_call(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#method_call

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
    #  ReturnedValue QV4::FunctionPrototype::method_call(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV417FunctionPrototype11method_callEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_hasInstance(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::FunctionPrototype::method_hasInstance(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#method_hasInstance

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
    #  ReturnedValue QV4::FunctionPrototype::method_hasInstance(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV417FunctionPrototype18method_hasInstanceEPKNS_14Functi'
        'onObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::FunctionPrototype'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.FunctionPrototype]:
    """
    Calls Qt's 'QV4::Heap::FunctionPrototype
    *QV4::FunctionPrototype::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.FunctionPrototype]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionPrototype *QV4::FunctionPrototype::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV417FunctionPrototype11d_uncheckedEv',
    )
    return QV4.Heap.FunctionPrototype._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.FunctionPrototype]:
    """
    Calls Qt's 'QV4::Heap::FunctionPrototype *QV4::FunctionPrototype::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionprototype.html#d

    Returns
    -------

    Optional[QV4.Heap.FunctionPrototype]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionPrototype *QV4::FunctionPrototype::d() const
    address = self.uglySide.call('ritual_ZNK3QV417FunctionPrototype1dEv')
    return QV4.Heap.FunctionPrototype._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::FunctionPrototype::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-functionprototype.html#__dataTest
    """
    #  void QV4::FunctionPrototype::__dataTest()
    self.uglySide.call('ritual_ZN3QV417FunctionPrototype10__dataTestEv')

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QV4::FunctionPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::BoundFunction::static_vtbl', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.FunctionPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::FunctionPrototype::init(ExecutionEngine *engine, Object "
        "*ctor)': leans on 'QV4::BoundFunction::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_apply(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::FunctionPrototype::method_apply(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::ArgumentsObject::static_vtbl', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.FunctionPrototype.method_apply' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::FunctionPrototype::method_apply(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::ArgumentsObject::static_vtbl', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def method_bind(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::FunctionPrototype::method_bind(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::BoundFunction::static_vtbl', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.FunctionPrototype.method_bind' has no cute function yet. Qt's "
        "'ReturnedValue QV4::FunctionPrototype::method_bind(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::BoundFunction::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
