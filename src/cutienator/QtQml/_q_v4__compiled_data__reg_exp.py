"""
QV4::CompiledData::RegExp binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::RegExp to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals


class RegExp(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::RegExp: a plain Python object
  standing in front of one C++ QV4::CompiledData::RegExp.

  C++ hands a QV4::CompiledData::RegExp around as a copy, so every C++
  QV4::CompiledData::RegExp behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::RegExp that has a ritual and that
  Python can call so far, 2 names in all: 'flags', 'stringIndex'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::RegExp::~RegExp()': the destructor: Python
    removes its C++ QV4::CompiledData::RegExp by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::RegExp is created at the first use, not by
    'QV4::CompiledData::RegExp(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::RegExp back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::RegExp.
  """

  #  The enums Qt writes inside QV4::CompiledData::RegExp, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QV4::CompiledData::RegExp::Flag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QV4::CompiledData::RegExp::Flags'.
    """

    RegExp_NoFlags = 0x0
    RegExp_Global = 0x1
    RegExp_IgnoreCase = 0x2
    RegExp_Multiline = 0x4
    RegExp_Sticky = 0x8
    RegExp_Unicode = 0x10

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::RegExp'

  #  Qt's '~QV4::CompiledData::RegExp()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::RegExp behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData6RegExpD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::RegExp::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-regexp.html#flags
    """
    #  quint32 QV4::CompiledData::RegExp::flags() const
    return self.uglySide.call('ritual_ZNK3QV412CompiledData6RegExp5flagsEv')

  def stringIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::RegExp::stringIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-regexp.html#stringIndex
    """
    #  quint32 QV4::CompiledData::RegExp::stringIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6RegExp11stringIndexEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::CompiledData::RegExp::RegExp()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-regexp.html#RegExp
    """
    #  QV4::CompiledData::RegExp::RegExp()
    self._noteCreation(RegExp, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData6RegExpC1Ev',
    ))

  @overload(int, int)
  def __init__(self, flags: int, stringIndex: int) -> None:
    """
    Notes what was given, for Qt's 'QV4::CompiledData::RegExp::RegExp(quint32
    flags, quint32 stringIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-regexp.html#RegExp

    Parameters
    ----------

    flags : int
      Passed on as it is.

    stringIndex : int
      Passed on as it is.
    """
    #  QV4::CompiledData::RegExp::RegExp(quint32 flags, quint32 stringIndex)
    self._noteCreation(RegExp, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData6RegExpC1Ejj', flags, stringIndex,
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
