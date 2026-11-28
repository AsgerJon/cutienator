"""
QV4::IntrinsicTypedArrayCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::IntrinsicTypedArrayCtor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class IntrinsicTypedArrayCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::IntrinsicTypedArrayCtor: a plain Python object
  standing in front of one C++ QV4::IntrinsicTypedArrayCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's
  QV4::IntrinsicTypedArrayCtor is built on Qt's QV4::FunctionObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::IntrinsicTypedArrayCtor that has a ritual and
  that Python can call so far, 3 names in all: '__dataTest', 'd_unchecked',
  'd'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has no ritual
  ------------------

  7 of the 10 functions Qt declares: 3 forbidden; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  not a gap; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::IntrinsicTypedArrayCtor is created at the first use, not by
    'QV4::IntrinsicTypedArrayCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::IntrinsicTypedArrayCtor.
  - Each name of Qt's QV4::IntrinsicTypedArrayCtor that has no cute function
    yet, 'method_from', 'method_of', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::IntrinsicTypedArrayCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.IntrinsicTypedArrayCtor]:
    """
    Calls Qt's 'QV4::Heap::IntrinsicTypedArrayCtor
    *QV4::IntrinsicTypedArrayCtor::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-intrinsictypedarrayctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.IntrinsicTypedArrayCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::IntrinsicTypedArrayCtor
    #      *QV4::IntrinsicTypedArrayCtor::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV423IntrinsicTypedArrayCtor11d_uncheckedEv',
    )
    return QV4.Heap.IntrinsicTypedArrayCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.IntrinsicTypedArrayCtor]:
    """
    Calls Qt's 'QV4::Heap::IntrinsicTypedArrayCtor
    *QV4::IntrinsicTypedArrayCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-intrinsictypedarrayctor.html#d

    Returns
    -------

    Optional[QV4.Heap.IntrinsicTypedArrayCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::IntrinsicTypedArrayCtor *QV4::IntrinsicTypedArrayCtor::d()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV423IntrinsicTypedArrayCtor1dEv',
    )
    return QV4.Heap.IntrinsicTypedArrayCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::IntrinsicTypedArrayCtor::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-intrinsictypedarrayctor.html#__dataTest
    """
    #  void QV4::IntrinsicTypedArrayCtor::__dataTest()
    self.uglySide.call(
        'ritual_ZN3QV423IntrinsicTypedArrayCtor10__dataTestEv',
    )

  @staticmethod
  def method_from(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::IntrinsicTypedArrayCtor::method_from(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no member named 'validateTypedArray' in
    the global namespace.
    """
    raise NotImplementedError(
        "'QV4.IntrinsicTypedArrayCtor.method_from' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::IntrinsicTypedArrayCtor::method_from(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no member named 'validateTypedArray' "
        "in the global namespace.")

  @staticmethod
  def method_of(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::IntrinsicTypedArrayCtor::method_of(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no member named 'validateTypedArray' in
    the global namespace.
    """
    raise NotImplementedError(
        "'QV4.IntrinsicTypedArrayCtor.method_of' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::IntrinsicTypedArrayCtor::method_of(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no member named "
        "'validateTypedArray' in the global namespace.")
