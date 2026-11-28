"""
QV4::CompiledData::Location binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Location to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class Location(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Location: a plain Python object
  standing in front of one C++ QV4::CompiledData::Location.

  C++ hands a QV4::CompiledData::Location around as a copy, so every C++
  QV4::CompiledData::Location behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Location that has a ritual and
  that Python can call so far, 6 names in all: '__lt__', '__eq__', '__ne__',
  'set', 'line', 'column'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Location::~Location()': the destructor: Python
    removes its C++ QV4::CompiledData::Location by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Location is created at the first use, not by
    'QV4::CompiledData::Location(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Location back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Location.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Location'

  #  Qt's '~QV4::CompiledData::Location()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::Location behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData8LocationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def line(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Location::line() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#line
    """
    #  quint32 QV4::CompiledData::Location::line() const
    return self.uglySide.call('ritual_ZNK3QV412CompiledData8Location4lineEv')

  def column(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Location::column() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#column
    """
    #  quint32 QV4::CompiledData::Location::column() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Location6columnEv',
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

  @overload(THIS)
  def __lt__(self, other: Location) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Location::operator<(const Location
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#operator<

    Parameters
    ----------

    other : Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  bool QV4::CompiledData::Location::operator<(const Location &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8LocationltERKS1_',
        self._valueOf(other),
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
  def __eq__(self, rhs: Location) -> bool:
    """
    Calls Qt's 'bool operator==(const Location &lhs, const Location &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#operator==

    Parameters
    ----------

    rhs : Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  bool operator==(const Location &lhs, const Location &rhs)
    return Rituals.call(
        'ritual_ZN3QV412CompiledDataeqERKNS0_8LocationES3_',
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
  def __ne__(self, rhs: Location) -> bool:
    """
    Calls Qt's 'bool operator!=(const Location &lhs, const Location &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#operator!=

    Parameters
    ----------

    rhs : Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  bool operator!=(const Location &lhs, const Location &rhs)
    return Rituals.call(
        'ritual_ZN3QV412CompiledDataneERKNS0_8LocationES3_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::CompiledData::Location::Location()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#Location
    """
    #  QV4::CompiledData::Location::Location()
    self._noteCreation(Location, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData8LocationC1Ev',
    ))

  @overload(int, int)
  def __init__(self, l: int, c: int) -> None:
    """
    Notes what was given, for Qt's
    'QV4::CompiledData::Location::Location(quint32 l, quint32 c)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-location.html#Location

    Parameters
    ----------

    l : int
      Passed on as it is.

    c : int
      Passed on as it is.
    """
    #  QV4::CompiledData::Location::Location(quint32 l, quint32 c)
    self._noteCreation(Location, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData8LocationC1Ejj', l, c,
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

  @overload(int, int)
  def set(self, line: int, column: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Location::set(quint32 line, quint32
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-location.html#set

    Parameters
    ----------

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Location::set(quint32 line, quint32 column)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Location3setEjj', line, column,
    )
