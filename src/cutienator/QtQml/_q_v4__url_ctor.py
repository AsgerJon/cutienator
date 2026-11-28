"""
QV4::UrlCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::UrlCtor to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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


class UrlCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::UrlCtor: a plain Python object standing in front
  of one C++ QV4::UrlCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::UrlCtor is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::UrlCtor that has a ritual and that Python can
  call so far, 4 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCallAsConstructor'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::UrlCtor is created at the first use, not by
    'QV4::UrlCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::UrlCtor.
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
      a0: Optional[QV4.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
      a3: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::UrlCtor::virtualCallAsConstructor(const
    FunctionObject *a0, const Value *argv, int argc, const Value *a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlctor.html#virtualCallAsConstructor

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::UrlCtor::virtualCallAsConstructor(const
    #      FunctionObject *a0, const Value *argv, int argc, const Value *a3)
    return Rituals.call(
        'ritual_ZN3QV47UrlCtor24virtualCallAsConstructorEPKNS_14FunctionObj'
        'ectEPKNS_5ValueEiS6_',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(argv), argc,
        CuteMixin._addressOf(a3),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::UrlCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.UrlCtor]:
    """
    Calls Qt's 'QV4::Heap::UrlCtor *QV4::UrlCtor::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.UrlCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlCtor *QV4::UrlCtor::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV47UrlCtor11d_uncheckedEv')
    return QV4.Heap.UrlCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.UrlCtor]:
    """
    Calls Qt's 'QV4::Heap::UrlCtor *QV4::UrlCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlctor.html#d

    Returns
    -------

    Optional[QV4.Heap.UrlCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlCtor *QV4::UrlCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV47UrlCtor1dEv')
    return QV4.Heap.UrlCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::UrlCtor::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlctor.html#__dataTest
    """
    #  void QV4::UrlCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV47UrlCtor10__dataTestEv')
