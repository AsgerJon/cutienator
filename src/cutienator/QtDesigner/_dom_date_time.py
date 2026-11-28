"""
DomDateTime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomDateTime to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomDateTime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomDateTime: a plain Python object standing in front
  of one C++ DomDateTime.

  What exists
  -----------

  Every function of Qt's DomDateTime that has a ritual and that Python can
  call so far, 24 names in all: 'elementHour', 'setElementHour',
  'hasElementHour', 'clearElementHour', 'elementMinute', 'setElementMinute',
  'hasElementMinute', 'clearElementMinute', 'elementSecond',
  'setElementSecond', 'hasElementSecond', 'clearElementSecond',
  'elementYear', 'setElementYear', 'hasElementYear', 'clearElementYear',
  'elementMonth', 'setElementMonth', 'hasElementMonth', 'clearElementMonth',
  'elementDay', 'setElementDay', 'hasElementDay', 'clearElementDay'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomDateTime::~DomDateTime()': the destructor: Python never removes
    a C++ DomDateTime.
  - Qt's 'void DomDateTime::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomDateTime::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomDateTime is created at the first use, not by
    'DomDateTime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomDateTime.
  - Each name of Qt's DomDateTime that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'DomDateTime'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementHour(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementHour() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementHour
    """
    #  int DomDateTime::elementHour() const
    return self.uglySide.call('ritual_ZNK11DomDateTime11elementHourEv')

  def hasElementHour(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementHour() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementHour
    """
    #  bool DomDateTime::hasElementHour() const
    return self.uglySide.call('ritual_ZNK11DomDateTime14hasElementHourEv')

  def elementMinute(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementMinute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementMinute
    """
    #  int DomDateTime::elementMinute() const
    return self.uglySide.call('ritual_ZNK11DomDateTime13elementMinuteEv')

  def hasElementMinute(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementMinute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementMinute
    """
    #  bool DomDateTime::hasElementMinute() const
    return self.uglySide.call('ritual_ZNK11DomDateTime16hasElementMinuteEv')

  def elementSecond(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementSecond() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementSecond
    """
    #  int DomDateTime::elementSecond() const
    return self.uglySide.call('ritual_ZNK11DomDateTime13elementSecondEv')

  def hasElementSecond(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementSecond() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementSecond
    """
    #  bool DomDateTime::hasElementSecond() const
    return self.uglySide.call('ritual_ZNK11DomDateTime16hasElementSecondEv')

  def elementYear(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementYear
    """
    #  int DomDateTime::elementYear() const
    return self.uglySide.call('ritual_ZNK11DomDateTime11elementYearEv')

  def hasElementYear(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementYear
    """
    #  bool DomDateTime::hasElementYear() const
    return self.uglySide.call('ritual_ZNK11DomDateTime14hasElementYearEv')

  def elementMonth(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementMonth
    """
    #  int DomDateTime::elementMonth() const
    return self.uglySide.call('ritual_ZNK11DomDateTime12elementMonthEv')

  def hasElementMonth(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementMonth
    """
    #  bool DomDateTime::hasElementMonth() const
    return self.uglySide.call('ritual_ZNK11DomDateTime15hasElementMonthEv')

  def elementDay(self) -> int:
    """
    Calls Qt's 'int DomDateTime::elementDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#elementDay
    """
    #  int DomDateTime::elementDay() const
    return self.uglySide.call('ritual_ZNK11DomDateTime10elementDayEv')

  def hasElementDay(self) -> bool:
    """
    Calls Qt's 'bool DomDateTime::hasElementDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#hasElementDay
    """
    #  bool DomDateTime::hasElementDay() const
    return self.uglySide.call('ritual_ZNK11DomDateTime13hasElementDayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementHour(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementHour(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementHour

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementHour(int a)
    self.uglySide.call('ritual_ZN11DomDateTime14setElementHourEi', a)

  @overload(int)
  def setElementMinute(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementMinute(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementMinute

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementMinute(int a)
    self.uglySide.call('ritual_ZN11DomDateTime16setElementMinuteEi', a)

  @overload(int)
  def setElementSecond(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementSecond(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementSecond

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementSecond(int a)
    self.uglySide.call('ritual_ZN11DomDateTime16setElementSecondEi', a)

  @overload(int)
  def setElementYear(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementYear(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementYear

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementYear(int a)
    self.uglySide.call('ritual_ZN11DomDateTime14setElementYearEi', a)

  @overload(int)
  def setElementMonth(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementMonth(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementMonth

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementMonth(int a)
    self.uglySide.call('ritual_ZN11DomDateTime15setElementMonthEi', a)

  @overload(int)
  def setElementDay(self, a: int) -> None:
    """
    Calls Qt's 'void DomDateTime::setElementDay(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#setElementDay

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDateTime::setElementDay(int a)
    self.uglySide.call('ritual_ZN11DomDateTime13setElementDayEi', a)

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
    Notes what was given, for Qt's 'DomDateTime::DomDateTime()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#DomDateTime
    """
    #  DomDateTime::DomDateTime()
    self._noteCreation(DomDateTime, lambda: Rituals.call(
        'ritual_ZN11DomDateTimeC1Ev',
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
    Calls Qt's 'void DomDateTime::clearElementHour()'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#clearElementHour
    """
    #  void DomDateTime::clearElementHour()
    self.uglySide.call('ritual_ZN11DomDateTime16clearElementHourEv')

  def clearElementMinute(self) -> None:
    """
    Calls Qt's 'void DomDateTime::clearElementMinute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domdatetime.html#clearElementMinute
    """
    #  void DomDateTime::clearElementMinute()
    self.uglySide.call('ritual_ZN11DomDateTime18clearElementMinuteEv')

  def clearElementSecond(self) -> None:
    """
    Calls Qt's 'void DomDateTime::clearElementSecond()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domdatetime.html#clearElementSecond
    """
    #  void DomDateTime::clearElementSecond()
    self.uglySide.call('ritual_ZN11DomDateTime18clearElementSecondEv')

  def clearElementYear(self) -> None:
    """
    Calls Qt's 'void DomDateTime::clearElementYear()'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#clearElementYear
    """
    #  void DomDateTime::clearElementYear()
    self.uglySide.call('ritual_ZN11DomDateTime16clearElementYearEv')

  def clearElementMonth(self) -> None:
    """
    Calls Qt's 'void DomDateTime::clearElementMonth()'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#clearElementMonth
    """
    #  void DomDateTime::clearElementMonth()
    self.uglySide.call('ritual_ZN11DomDateTime17clearElementMonthEv')

  def clearElementDay(self) -> None:
    """
    Calls Qt's 'void DomDateTime::clearElementDay()'.

    Qt's own words: https://doc.qt.io/qt-6/domdatetime.html#clearElementDay
    """
    #  void DomDateTime::clearElementDay()
    self.uglySide.call('ritual_ZN11DomDateTime15clearElementDayEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomDateTime::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomDateTime.read' has no cute function yet. Qt's 'void "
        "DomDateTime::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomDateTime::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomDateTime.write' has no cute function yet. Qt's 'void "
        "DomDateTime::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
