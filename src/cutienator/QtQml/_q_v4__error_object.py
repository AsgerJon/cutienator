"""
QV4::ErrorObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ErrorObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class ErrorObject(QV4.Object):
  """
  The cute side of Qt's QV4::ErrorObject: a plain Python object standing in
  front of one C++ QV4::ErrorObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::ErrorObject is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ErrorObject that has a ritual and that Python
  can call so far, 9 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'defaultPrototype', 'virtualDestroy',
  'asSyntaxError', 'className', 'method_get_stack'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 3 forbidden; 3 a template; 1 not a gap;
  1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::ErrorObject is created at the first use, not by
    'QV4::ErrorObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ErrorObject.
  - Each name of Qt's QV4::ErrorObject that has no cute function yet,
    'create', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::ErrorObject::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-errorobject.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::ErrorObject::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV411ErrorObject20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::ErrorObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-errorobject.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::ErrorObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV411ErrorObject16defaultPrototypeEPNS_15ExecutionEngine'
        'E',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::ErrorObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-errorobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ErrorObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV411ErrorObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(QV4.Heap.ErrorObject.ErrorType)
  def className(t: QV4.Heap.ErrorObject.ErrorType) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QV4::ErrorObject::className(Heap::ErrorObject::ErrorType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorobject.html#className

    Parameters
    ----------

    t : QV4.Heap.ErrorObject.ErrorType
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::ErrorObject::className(Heap::ErrorObject::ErrorType
    #      t)
    chars = Rituals.call(
        'ritual_ZN3QV411ErrorObject9classNameENS_4Heap11ErrorObject9ErrorTy'
        'peE',
        t.value,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_get_stack(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ErrorObject::method_get_stack(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-errorobject.html#method_get_stack

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
    #  ReturnedValue QV4::ErrorObject::method_get_stack(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV411ErrorObject16method_get_stackEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ErrorObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ErrorObject]:
    """
    Calls Qt's 'QV4::Heap::ErrorObject *QV4::ErrorObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ErrorObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ErrorObject *QV4::ErrorObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV411ErrorObject11d_uncheckedEv',
    )
    return QV4.Heap.ErrorObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ErrorObject]:
    """
    Calls Qt's 'QV4::Heap::ErrorObject *QV4::ErrorObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ErrorObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ErrorObject *QV4::ErrorObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV411ErrorObject1dEv')
    return QV4.Heap.ErrorObject._cuteAt(address)

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
    Calls Qt's 'void QV4::ErrorObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorobject.html#__dataTest
    """
    #  void QV4::ErrorObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV411ErrorObject10__dataTestEv')

  def asSyntaxError(self) -> Optional[QV4.SyntaxErrorObject]:
    """
    Calls Qt's 'SyntaxErrorObject *QV4::ErrorObject::asSyntaxError()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-errorobject.html#asSyntaxError

    Returns
    -------

    Optional[QV4.SyntaxErrorObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SyntaxErrorObject *QV4::ErrorObject::asSyntaxError()
    address = self.uglySide.call(
        'ritual_ZN3QV411ErrorObject13asSyntaxErrorEv',
    )
    return QV4.SyntaxErrorObject._cuteAt(address)

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QV4::ErrorObject::create': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.ErrorObject.create' has no cute function yet. Qt's "
        "'QV4::ErrorObject::create': a template: a pattern and no single "
        "function.")
