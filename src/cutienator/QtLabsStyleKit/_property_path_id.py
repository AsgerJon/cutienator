"""
PropertyPathId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PropertyPathId to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from . import QQSK

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class PropertyPathId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's PropertyPathId: a plain Python object standing in
  front of one C++ PropertyPathId.

  C++ hands a PropertyPathId around as a copy, so every C++ PropertyPathId
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's PropertyPathId that has a ritual and that Python can
  call so far, 3 names in all: 'property', 'pathId', 'storageId'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'PropertyPathId::PropertyPathId(const QQSK::Property property, const
    PropertyPathId_t groupStart, QQSK::PropertyGroup subtype)': takes a type
    Python has no way to hand over yet.
  - Qt's 'PropertyPathId::~PropertyPathId()': the destructor: Python removes
    its C++ PropertyPathId by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ PropertyPathId is created at the first use, not by
    'PropertyPathId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a PropertyPathId back gives a copy the ritual made for
    Python, in a new cute PropertyPathId.
  - Each name of Qt's PropertyPathId that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside PropertyPathId, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteNum, scoped=True):
    """
    The enum 'PropertyPathId::Flag' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    ExcludeSubtype = Kee[int](0)
    IncludeSubtype = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PropertyPathId'

  #  Qt's '~PropertyPathId()'. Naming it makes this a value class: Python
  #  owns every C++ PropertyPathId behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14PropertyPathIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def property(self) -> QQSK.Property:
    """
    Calls Qt's 'QQSK::Property PropertyPathId::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/propertypathid.html#property

    Returns
    -------

    QQSK.Property
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QQSK.Property(number)'
      gives.
    """
    #  QQSK::Property PropertyPathId::property() const
    return QQSK.Property(self.uglySide.call(
        'ritual_ZNK14PropertyPathId8propertyEv',
    ))

  def pathId(self) -> int:
    """
    Calls Qt's 'PropertyPathId_t PropertyPathId::pathId() const'.

    Qt's own words: https://doc.qt.io/qt-6/propertypathid.html#pathId
    """
    #  PropertyPathId_t PropertyPathId::pathId() const
    return self.uglySide.call('ritual_ZNK14PropertyPathId6pathIdEv')

  @overload(QQSK.State)
  def storageId(self, state: QQSK.State) -> int:
    """
    Calls Qt's 'PropertyStorageId PropertyPathId::storageId(QQSK::State
    state) const'.

    Qt's own words: https://doc.qt.io/qt-6/propertypathid.html#storageId

    Parameters
    ----------

    state : QQSK.State
      Passed on as its number.
    """
    #  PropertyStorageId PropertyPathId::storageId(QQSK::State state) const
    return self.uglySide.call(
        'ritual_ZNK14PropertyPathId9storageIdE6QFlagsIN4QQSK9StateFlagEE',
        state.value,
    )

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
    Qt's 'PropertyPathId::PropertyPathId(const QQSK::Property property, const
    PropertyPathId_t groupStart, QQSK::PropertyGroup subtype)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'PropertyPathId.__init__' has no cute function yet. Qt's "
        "'PropertyPathId::PropertyPathId(const QQSK::Property property, "
        "const PropertyPathId_t groupStart, QQSK::PropertyGroup subtype)': "
        "takes a type Python has no way to hand over yet.")

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
