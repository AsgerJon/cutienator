"""
QV4::ObjectIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ObjectIterator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ObjectIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ObjectIterator: a plain Python object standing
  in front of one C++ QV4::ObjectIterator.

  C++ hands a QV4::ObjectIterator around as a copy, so every C++
  QV4::ObjectIterator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::ObjectIterator that has a ritual and that
  Python can call so far, 3 names in all: 'next', 'nextPropertyName',
  'nextPropertyNameAsString'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ObjectIterator::ObjectIterator(Scope &scope, const Object *o,
    uint flags)': takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ObjectIterator::~ObjectIterator()': the destructor: Python
    removes its C++ QV4::ObjectIterator by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::ObjectIterator is created at the first use, not by
    'QV4::ObjectIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ObjectIterator back gives a copy the ritual made
    for Python, in a new cute QV4::ObjectIterator.
  - Each name of Qt's QV4::ObjectIterator that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QV4::ObjectIterator, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flags(CuteNum):
    """
    The enum 'QV4::ObjectIterator::Flags' of Qt, with the 3 names Qt gives in
    it.
    """

    NoFlags = Kee[int](0)
    EnumerableOnly = Kee[int](1)
    WithSymbols = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ObjectIterator'

  #  Qt's '~QV4::ObjectIterator()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::ObjectIterator behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV414ObjectIteratorD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QV4::ObjectIterator::ObjectIterator(Scope &scope, const Object *o,
    uint flags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ObjectIterator.__init__' has no cute function yet. Qt's "
        "'QV4::ObjectIterator::ObjectIterator(Scope &scope, const Object "
        "*o, uint flags)': takes a type Python has no way to hand over yet.")

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

  @overload()
  @overload(WAIT['QV4.Property'])
  @overload(NoneType)
  @overload(WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'])
  @overload(WAIT['QV4.Property'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, NoneType)
  def next(
      self,
      pd: Optional[QV4.Property] = None,
      attributes: Optional[QV4.PropertyAttributes] = None,
  ) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::ObjectIterator::next(Property *pd,
    PropertyAttributes *attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-objectiterator.html#next

    Parameters
    ----------

    pd : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    attributes : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::ObjectIterator::next(Property *pd, PropertyAttributes
    #      *attributes)
    address = self.uglySide.call(
        'ritual_ZN3QV414ObjectIterator4nextEPNS_8PropertyEPNS_18PropertyAtt'
        'ributesE',
        self._addressOf(pd), self._addressOf(attributes),
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def nextPropertyName(self, value: Optional[QV4.Value]) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ObjectIterator::nextPropertyName(Value
    *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-objectiterator.html#nextPropertyName

    Parameters
    ----------

    value : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ObjectIterator::nextPropertyName(Value *value)
    return self.uglySide.call(
        'ritual_ZN3QV414ObjectIterator16nextPropertyNameEPNS_5ValueE',
        self._addressOf(value),
    )

  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def nextPropertyNameAsString(self, value: Optional[QV4.Value]) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::ObjectIterator::nextPropertyNameAsString(Value *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-objectiterator.html#nextPropertyNameAsString

    Parameters
    ----------

    value : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ObjectIterator::nextPropertyNameAsString(Value
    #      *value)
    return self.uglySide.call(
        'ritual_ZN3QV414ObjectIterator24nextPropertyNameAsStringEPNS_5Value'
        'E',
        self._addressOf(value),
    )

  @overload()
  def nextPropertyNameAsString(self) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::ObjectIterator::nextPropertyNameAsString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-objectiterator.html#nextPropertyNameAsString
    """
    #  ReturnedValue QV4::ObjectIterator::nextPropertyNameAsString()
    return self.uglySide.call(
        'ritual_ZN3QV414ObjectIterator24nextPropertyNameAsStringEv',
    )
