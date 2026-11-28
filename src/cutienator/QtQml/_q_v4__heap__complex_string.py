"""
QV4::Heap::ComplexString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Heap::ComplexString to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ComplexString(QV4.Heap.String):
  """
  The cute side of Qt's QV4::Heap::ComplexString: a plain Python object
  standing in front of one C++ QV4::Heap::ComplexString.

  It is built on the cute 'QV4::Heap::String', as Qt's
  QV4::Heap::ComplexString is built on Qt's QV4::Heap::String, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ComplexString that has a ritual and that
  Python can call so far, 1 name in all: 'init'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ComplexString is created at the first use, not by
    'QV4::Heap::ComplexString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ComplexString.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ComplexString'

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

  @overload(QV4.Heap.String, QV4.Heap.String)
  @overload(QV4.Heap.String, NoneType)
  @overload(NoneType, QV4.Heap.String)
  @overload(NoneType, NoneType)
  def init(
      self,
      l: Optional[QV4.Heap.String],
      n: Optional[QV4.Heap.String],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ComplexString::init(String *l, String *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-complexstring.html#init

    Parameters
    ----------

    l : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ComplexString::init(String *l, String *n)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13ComplexString4initEPNS0_6StringES3_',
        self._addressOf(l), self._addressOf(n),
    )

  @overload(QV4.Heap.String, int, int)
  @overload(NoneType, int, int)
  def init(
      self,
      ref: Optional[QV4.Heap.String],
      from_: int,
      len: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ComplexString::init(String *ref, int from,
    int len)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-complexstring.html#init

    Parameters
    ----------

    ref : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    from_ : int
      Passed on as it is.

    len : int
      Passed on as it is.
    """
    #  void QV4::Heap::ComplexString::init(String *ref, int from, int len)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13ComplexString4initEPNS0_6StringEii',
        self._addressOf(ref), from_, len,
    )
