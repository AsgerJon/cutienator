"""
QLatin1Char binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLatin1Char(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLatin1Char: a plain Python object standing in front
  of one C++ QLatin1Char.

  C++ hands a QLatin1Char around as a copy, so every C++ QLatin1Char behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLatin1Char that has a ritual and that Python can
  call so far, 7 names in all: 'unicode', '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLatin1Char::QLatin1Char(char c)': takes a single letter as C has
    it.
  - Qt's 'char QLatin1Char::toLatin1() const': gives a single letter as C has
    it.
  - Qt's 'bool operator==(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator!=(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<=(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>=(const QLatin1Char &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator==(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator!=(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<=(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>=(const char &lhs, const QLatin1Char &rhs)': takes a
    single letter as C has it.
  - Qt's 'char16_t QLatin1Char::operator char16_t() const': an operator
    Python has no name for.
  - Qt's 'QLatin1Char::~QLatin1Char()': the destructor: Python removes its
    C++ QLatin1Char by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLatin1Char is created at the first use, not by
    'QLatin1Char(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLatin1Char back gives a copy the ritual made for
    Python, in a new cute QLatin1Char.
  - Each name of Qt's QLatin1Char that has no cute function yet, '__init__',
    'toLatin1', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLatin1Char'

  #  Qt's '~QLatin1Char()'. Naming it makes this a value class: Python owns
  #  every C++ QLatin1Char behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLatin1CharD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def unicode(self) -> int:
    """
    Calls Qt's 'char16_t QLatin1Char::unicode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#unicode
    """
    #  char16_t QLatin1Char::unicode() const
    return self.uglySide.call('ritual_ZNK11QLatin1Char7unicodeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator==

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator==(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator!=

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator!=(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZneRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator<

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator<(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZltRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator>

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator>(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZgtRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator<=

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator<=(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZleRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QLatin1Char) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1Char &lhs, const QLatin1Char
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1char.html#operator>=

    Parameters
    ----------

    rhs : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.
    """
    #  bool operator>=(const QLatin1Char &lhs, const QLatin1Char &rhs)
    return Rituals.call(
        'ritual_ZgeRK11QLatin1CharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QLatin1Char::QLatin1Char(char c)': takes a single letter as C has
    it.
    """
    raise NotImplementedError(
        "'QLatin1Char.__init__' has no cute function yet. Qt's "
        "'QLatin1Char::QLatin1Char(char c)': takes a single letter as C has "
        "it.")

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

  @staticmethod
  def toLatin1(*__, **_) -> Never:
    """
    Qt's 'char QLatin1Char::toLatin1() const': gives a single letter as C has
    it.
    """
    raise NotImplementedError(
        "'QLatin1Char.toLatin1' has no cute function yet. Qt's 'char "
        "QLatin1Char::toLatin1() const': gives a single letter as C has it.")
