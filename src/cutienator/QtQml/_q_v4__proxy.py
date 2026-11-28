"""
QV4::Proxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Proxy to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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


class Proxy(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::Proxy: a plain Python object standing in front
  of one C++ QV4::Proxy.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::Proxy is built
  on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Proxy that has a ritual and that Python can
  call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCall', 'method_revoke'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has no ritual
  ------------------

  7 of the 12 functions Qt declares: 3 forbidden; 3 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::Proxy is created at the first use, not by 'QV4::Proxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Proxy.
  - Each name of Qt's QV4::Proxy that has no cute function yet,
    'method_revocable', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Proxy::virtualCall(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxy.html#virtualCall

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
    #  ReturnedValue QV4::Proxy::virtualCall(const FunctionObject *a0, const
    #      Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV45Proxy11virtualCallEPKNS_14FunctionObjectEPKNS_5Value'
        'ES6_i',
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
  def method_revoke(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Proxy::method_revoke(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxy.html#method_revoke

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
    #  ReturnedValue QV4::Proxy::method_revoke(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV45Proxy13method_revokeEPKNS_14FunctionObjectEPKNS_5Val'
        'ueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Proxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Proxy]:
    """
    Calls Qt's 'QV4::Heap::Proxy *QV4::Proxy::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxy.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Proxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Proxy *QV4::Proxy::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV45Proxy11d_uncheckedEv')
    return QV4.Heap.Proxy._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Proxy]:
    """
    Calls Qt's 'QV4::Heap::Proxy *QV4::Proxy::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxy.html#d

    Returns
    -------

    Optional[QV4.Heap.Proxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Proxy *QV4::Proxy::d() const
    address = self.uglySide.call('ritual_ZNK3QV45Proxy1dEv')
    return QV4.Heap.Proxy._cuteAt(address)

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
    Calls Qt's 'void QV4::Proxy::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxy.html#__dataTest
    """
    #  void QV4::Proxy::__dataTest()
    self.uglySide.call('ritual_ZN3QV45Proxy10__dataTestEv')

  @staticmethod
  def method_revocable(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Proxy::method_revocable(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)': leans on
    'QV4::ProxyObject::static_vtbl', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Proxy.method_revocable' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Proxy::method_revocable(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::ProxyObject::static_vtbl', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
