"""
QV4::ObjectOwnPropertyKeyIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::ObjectOwnPropertyKeyIterator to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ObjectOwnPropertyKeyIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ObjectOwnPropertyKeyIterator: a plain Python
  object standing in front of one C++ QV4::ObjectOwnPropertyKeyIterator.

  C++ hands a QV4::ObjectOwnPropertyKeyIterator around as a copy, so every
  C++ QV4::ObjectOwnPropertyKeyIterator behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QV4::ObjectOwnPropertyKeyIterator that has a ritual
  and that Python can call so far, 1 name in all: 'next'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QV4::ObjectOwnPropertyKeyIterator::~ObjectOwnPropertyKeyIterator()': the
    destructor: Python removes its C++ QV4::ObjectOwnPropertyKeyIterator by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::ObjectOwnPropertyKeyIterator is created at the first use,
    not by 'QV4::ObjectOwnPropertyKeyIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ObjectOwnPropertyKeyIterator back gives a copy
    the ritual made for Python, in a new cute
    QV4::ObjectOwnPropertyKeyIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ObjectOwnPropertyKeyIterator'

  #  A C++ QV4::ObjectOwnPropertyKeyIterator Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QV4_ObjectOwnPropertyKeyIterator'

  #  Qt's '~QV4::ObjectOwnPropertyKeyIterator()'. Naming it makes this a
  #  value class: Python owns every C++ QV4::ObjectOwnPropertyKeyIterator
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV428ObjectOwnPropertyKeyIteratorD1Ev'

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

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  @overload(WAIT['QV4.Object'], WAIT['QV4.Property'])
  @overload(WAIT['QV4.Object'], NoneType)
  @overload(NoneType, WAIT['QV4.Property'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QV4.Object'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(WAIT['QV4.Object'], WAIT['QV4.Property'], NoneType)
  @overload(WAIT['QV4.Object'], NoneType, WAIT['QV4.PropertyAttributes'])
  @overload(WAIT['QV4.Object'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, WAIT['QV4.Property'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, NoneType, NoneType)
  def next(
      self,
      o: Optional[QV4.Object],
      pd: Optional[QV4.Property] = None,
      attrs: Optional[QV4.PropertyAttributes] = None,
  ) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::ObjectOwnPropertyKeyIterator::next(const
    Object *o, Property *pd, PropertyAttributes *attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-objectownpropertykeyiterator.html#next

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pd : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::ObjectOwnPropertyKeyIterator::next(const Object *o,
    #      Property *pd, PropertyAttributes *attrs)
    ritual = (
        'ritual_ZN3QV428ObjectOwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_'
        '8PropertyEPNS_18PropertyAttributesE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV428ObjectOwnPropertyKeyIterator4nextEPKNS_6Objec'
          'tEPNS_8PropertyEPNS_18PropertyAttributesE')
    address = self.uglySide.call(
        ritual,
        self._addressOf(o), self._addressOf(pd), self._addressOf(attrs),
    )
    return QV4.PropertyKey._cuteOwning(address)
