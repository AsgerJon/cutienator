"""
DomTime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomTime to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomTime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomTime: a plain Python object standing in front of
  one C++ DomTime.

  What exists
  -----------

  Every function of Qt's DomTime that has a ritual and that Python can call
  so far, 12 names in all: 'elementHour', 'setElementHour', 'hasElementHour',
  'clearElementHour', 'elementMinute', 'setElementMinute',
  'hasElementMinute', 'clearElementMinute', 'elementSecond',
  'setElementSecond', 'hasElementSecond', 'clearElementSecond'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomTime::~DomTime()': the destructor: Python never removes a C++
    DomTime.
  - Qt's 'void DomTime::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomTime::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomTime is created at the first use, not by 'DomTime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomTime.
  - Each name of Qt's DomTime that has no cute function yet, 'read', 'write',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomTime'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementHour(self) -> int:
    """
    Calls Qt's 'int DomTime::elementHour() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#elementHour
    """
    #  int DomTime::elementHour() const
    return self.uglySide.call('ritual_ZNK7DomTime11elementHourEv')

  def hasElementHour(self) -> bool:
    """
    Calls Qt's 'bool DomTime::hasElementHour() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#hasElementHour
    """
    #  bool DomTime::hasElementHour() const
    return self.uglySide.call('ritual_ZNK7DomTime14hasElementHourEv')

  def elementMinute(self) -> int:
    """
    Calls Qt's 'int DomTime::elementMinute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#elementMinute
    """
    #  int DomTime::elementMinute() const
    return self.uglySide.call('ritual_ZNK7DomTime13elementMinuteEv')

  def hasElementMinute(self) -> bool:
    """
    Calls Qt's 'bool DomTime::hasElementMinute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#hasElementMinute
    """
    #  bool DomTime::hasElementMinute() const
    return self.uglySide.call('ritual_ZNK7DomTime16hasElementMinuteEv')

  def elementSecond(self) -> int:
    """
    Calls Qt's 'int DomTime::elementSecond() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#elementSecond
    """
    #  int DomTime::elementSecond() const
    return self.uglySide.call('ritual_ZNK7DomTime13elementSecondEv')

  def hasElementSecond(self) -> bool:
    """
    Calls Qt's 'bool DomTime::hasElementSecond() const'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#hasElementSecond
    """
    #  bool DomTime::hasElementSecond() const
    return self.uglySide.call('ritual_ZNK7DomTime16hasElementSecondEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementHour(self, a: int) -> None:
    """
    Calls Qt's 'void DomTime::setElementHour(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#setElementHour

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomTime::setElementHour(int a)
    self.uglySide.call('ritual_ZN7DomTime14setElementHourEi', a)

  @overload(int)
  def setElementMinute(self, a: int) -> None:
    """
    Calls Qt's 'void DomTime::setElementMinute(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#setElementMinute

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomTime::setElementMinute(int a)
    self.uglySide.call('ritual_ZN7DomTime16setElementMinuteEi', a)

  @overload(int)
  def setElementSecond(self, a: int) -> None:
    """
    Calls Qt's 'void DomTime::setElementSecond(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#setElementSecond

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomTime::setElementSecond(int a)
    self.uglySide.call('ritual_ZN7DomTime16setElementSecondEi', a)

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
    Notes what was given, for Qt's 'DomTime::DomTime()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#DomTime
    """
    #  DomTime::DomTime()
    self._noteCreation(DomTime, lambda: Rituals.call(
        'ritual_ZN7DomTimeC1Ev',
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

  def clearElementHour(self) -> None:
    """
    Calls Qt's 'void DomTime::clearElementHour()'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#clearElementHour
    """
    #  void DomTime::clearElementHour()
    self.uglySide.call('ritual_ZN7DomTime16clearElementHourEv')

  def clearElementMinute(self) -> None:
    """
    Calls Qt's 'void DomTime::clearElementMinute()'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#clearElementMinute
    """
    #  void DomTime::clearElementMinute()
    self.uglySide.call('ritual_ZN7DomTime18clearElementMinuteEv')

  def clearElementSecond(self) -> None:
    """
    Calls Qt's 'void DomTime::clearElementSecond()'.

    Qt's own words: https://doc.qt.io/qt-6/domtime.html#clearElementSecond
    """
    #  void DomTime::clearElementSecond()
    self.uglySide.call('ritual_ZN7DomTime18clearElementSecondEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomTime::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomTime.read' has no cute function yet. Qt's 'void "
        "DomTime::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomTime::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomTime.write' has no cute function yet. Qt's 'void "
        "DomTime::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
