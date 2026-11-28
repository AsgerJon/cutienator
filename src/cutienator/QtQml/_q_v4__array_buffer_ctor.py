"""
QV4::ArrayBufferCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ArrayBufferCtor to be private: it declares the class in a
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


class ArrayBufferCtor(QV4.SharedArrayBufferCtor):
  """
  The cute side of Qt's QV4::ArrayBufferCtor: a plain Python object standing
  in front of one C++ QV4::ArrayBufferCtor.

  It is built on the cute 'QV4::SharedArrayBufferCtor', as Qt's
  QV4::ArrayBufferCtor is built on Qt's QV4::SharedArrayBufferCtor, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ArrayBufferCtor that has a ritual and that
  Python can call so far, 4 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCallAsConstructor'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has no ritual
  ------------------

  6 of the 10 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::ArrayBufferCtor is created at the first use, not by
    'QV4::ArrayBufferCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ArrayBufferCtor.
  - Each name of Qt's QV4::ArrayBufferCtor that has no cute function yet,
    'method_isView', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, int, QV4.Value)
  @overload(QV4.FunctionObject, QV4.Value, int, NoneType)
  @overload(QV4.FunctionObject, NoneType, int, QV4.Value)
  @overload(QV4.FunctionObject, NoneType, int, NoneType)
  @overload(NoneType, QV4.Value, int, QV4.Value)
  @overload(NoneType, QV4.Value, int, NoneType)
  @overload(NoneType, NoneType, int, QV4.Value)
  @overload(NoneType, NoneType, int, NoneType)
  def virtualCallAsConstructor(
      f: Optional[QV4.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
      a3: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::ArrayBufferCtor::virtualCallAsConstructor(const FunctionObject *f,
    const Value *argv, int argc, const Value *a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybufferctor.html#virtualCallAsConstructor

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    a3 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ArrayBufferCtor::virtualCallAsConstructor(const
    #      FunctionObject *f, const Value *argv, int argc, const Value *a3)
    return Rituals.call(
        'ritual_ZN3QV415ArrayBufferCtor24virtualCallAsConstructorEPKNS_14Fu'
        'nctionObjectEPKNS_5ValueEiS6_',
        CuteMixin._addressOf(f), CuteMixin._addressOf(argv), argc,
        CuteMixin._addressOf(a3),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ArrayBufferCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ArrayBufferCtor]:
    """
    Calls Qt's 'QV4::Heap::ArrayBufferCtor
    *QV4::ArrayBufferCtor::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybufferctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ArrayBufferCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayBufferCtor *QV4::ArrayBufferCtor::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ArrayBufferCtor11d_uncheckedEv',
    )
    return QV4.Heap.ArrayBufferCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ArrayBufferCtor]:
    """
    Calls Qt's 'QV4::Heap::ArrayBufferCtor *QV4::ArrayBufferCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybufferctor.html#d

    Returns
    -------

    Optional[QV4.Heap.ArrayBufferCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayBufferCtor *QV4::ArrayBufferCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV415ArrayBufferCtor1dEv')
    return QV4.Heap.ArrayBufferCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::ArrayBufferCtor::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybufferctor.html#__dataTest
    """
    #  void QV4::ArrayBufferCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV415ArrayBufferCtor10__dataTestEv')

  @staticmethod
  def method_isView(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ArrayBufferCtor::method_isView(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::DataView::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ArrayBufferCtor.method_isView' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ArrayBufferCtor::method_isView(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::DataView::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
