"""
QV4::CompiledData::Lookup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Lookup to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class Lookup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Lookup: a plain Python object
  standing in front of one C++ QV4::CompiledData::Lookup.

  C++ hands a QV4::CompiledData::Lookup around as a copy, so every C++
  QV4::CompiledData::Lookup behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Lookup that has a ritual and that
  Python can call so far, 3 names in all: 'type', 'nameIndex', 'mode'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Lookup::~Lookup()': the destructor: Python
    removes its C++ QV4::CompiledData::Lookup by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Lookup is created at the first use, not by
    'QV4::CompiledData::Lookup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Lookup back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Lookup.
  """

  #  The enums Qt writes inside QV4::CompiledData::Lookup, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Mode(CuteNum):
    """
    The enum 'QV4::CompiledData::Lookup::Mode' of Qt, with the 2 names Qt
    gives in it.
    """

    Mode_ForStorage = Kee[int](0)
    Mode_ForCall = Kee[int](1)

  class Type(CuteNum):
    """
    The enum 'QV4::CompiledData::Lookup::Type' of Qt, with the 4 names Qt
    gives in it.
    """

    Type_Getter = Kee[int](0)
    Type_Setter = Kee[int](1)
    Type_GlobalGetter = Kee[int](2)
    Type_QmlContextPropertyGetter = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Lookup'

  #  Qt's '~QV4::CompiledData::Lookup()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Lookup behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData6LookupD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Lookup::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-lookup.html#type
    """
    #  quint32 QV4::CompiledData::Lookup::type() const
    return self.uglySide.call('ritual_ZNK3QV412CompiledData6Lookup4typeEv')

  def nameIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Lookup::nameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-lookup.html#nameIndex
    """
    #  quint32 QV4::CompiledData::Lookup::nameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Lookup9nameIndexEv',
    )

  def mode(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Lookup::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-lookup.html#mode
    """
    #  quint32 QV4::CompiledData::Lookup::mode() const
    return self.uglySide.call('ritual_ZNK3QV412CompiledData6Lookup4modeEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::CompiledData::Lookup::Lookup()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-lookup.html#Lookup
    """
    #  QV4::CompiledData::Lookup::Lookup()
    self._noteCreation(Lookup, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData6LookupC1Ev',
    ))

  @overload(Type, Mode, int)
  def __init__(self, type: Type, mode: Mode, nameIndex: int) -> None:
    """
    Notes what was given, for Qt's 'QV4::CompiledData::Lookup::Lookup(Type
    type, Mode mode, quint32 nameIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-lookup.html#Lookup

    Parameters
    ----------

    type : Type
      Passed on as its number.

    mode : Mode
      Passed on as its number.

    nameIndex : int
      Passed on as it is.
    """
    #  QV4::CompiledData::Lookup::Lookup(Type type, Mode mode, quint32
    #      nameIndex)
    self._noteCreation(Lookup, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData6LookupC1ENS1_4TypeENS1_4ModeEj',
        type.value, mode.value, nameIndex,
    ))

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
