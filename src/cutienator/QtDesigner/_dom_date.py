"""
DomDate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomDate to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomDate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomDate: a plain Python object standing in front of
  one C++ DomDate.

  What exists
  -----------

  Every function of Qt's DomDate that has a ritual and that Python can call
  so far, 12 names in all: 'elementYear', 'setElementYear', 'hasElementYear',
  'clearElementYear', 'elementMonth', 'setElementMonth', 'hasElementMonth',
  'clearElementMonth', 'elementDay', 'setElementDay', 'hasElementDay',
  'clearElementDay'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomDate::~DomDate()': the destructor: Python never removes a C++
    DomDate.
  - Qt's 'void DomDate::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomDate::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomDate is created at the first use, not by 'DomDate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomDate.
  - Each name of Qt's DomDate that has no cute function yet, 'read', 'write',
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
  __qt_class__ = 'DomDate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementYear(self) -> int:
    """
    Calls Qt's 'int DomDate::elementYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#elementYear
    """
    #  int DomDate::elementYear() const
    return self.uglySide.call('ritual_ZNK7DomDate11elementYearEv')

  def hasElementYear(self) -> bool:
    """
    Calls Qt's 'bool DomDate::hasElementYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#hasElementYear
    """
    #  bool DomDate::hasElementYear() const
    return self.uglySide.call('ritual_ZNK7DomDate14hasElementYearEv')

  def elementMonth(self) -> int:
    """
    Calls Qt's 'int DomDate::elementMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#elementMonth
    """
    #  int DomDate::elementMonth() const
    return self.uglySide.call('ritual_ZNK7DomDate12elementMonthEv')

  def hasElementMonth(self) -> bool:
    """
    Calls Qt's 'bool DomDate::hasElementMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#hasElementMonth
    """
    #  bool DomDate::hasElementMonth() const
    return self.uglySide.call('ritual_ZNK7DomDate15hasElementMonthEv')

  def elementDay(self) -> int:
    """
    Calls Qt's 'int DomDate::elementDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#elementDay
    """
    #  int DomDate::elementDay() const
    return self.uglySide.call('ritual_ZNK7DomDate10elementDayEv')

  def hasElementDay(self) -> bool:
    """
    Calls Qt's 'bool DomDate::hasElementDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#hasElementDay
    """
    #  bool DomDate::hasElementDay() const
    return self.uglySide.call('ritual_ZNK7DomDate13hasElementDayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementYear(self, a: int) -> None:
    """
    Calls Qt's 'void DomDate::setElementYear(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#setElementYear

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDate::setElementYear(int a)
    self.uglySide.call('ritual_ZN7DomDate14setElementYearEi', a)

  @overload(int)
  def setElementMonth(self, a: int) -> None:
    """
    Calls Qt's 'void DomDate::setElementMonth(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#setElementMonth

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDate::setElementMonth(int a)
    self.uglySide.call('ritual_ZN7DomDate15setElementMonthEi', a)

  @overload(int)
  def setElementDay(self, a: int) -> None:
    """
    Calls Qt's 'void DomDate::setElementDay(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#setElementDay

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomDate::setElementDay(int a)
    self.uglySide.call('ritual_ZN7DomDate13setElementDayEi', a)

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
    Notes what was given, for Qt's 'DomDate::DomDate()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#DomDate
    """
    #  DomDate::DomDate()
    self._noteCreation(DomDate, lambda: Rituals.call(
        'ritual_ZN7DomDateC1Ev',
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

  def clearElementYear(self) -> None:
    """
    Calls Qt's 'void DomDate::clearElementYear()'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#clearElementYear
    """
    #  void DomDate::clearElementYear()
    self.uglySide.call('ritual_ZN7DomDate16clearElementYearEv')

  def clearElementMonth(self) -> None:
    """
    Calls Qt's 'void DomDate::clearElementMonth()'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#clearElementMonth
    """
    #  void DomDate::clearElementMonth()
    self.uglySide.call('ritual_ZN7DomDate17clearElementMonthEv')

  def clearElementDay(self) -> None:
    """
    Calls Qt's 'void DomDate::clearElementDay()'.

    Qt's own words: https://doc.qt.io/qt-6/domdate.html#clearElementDay
    """
    #  void DomDate::clearElementDay()
    self.uglySide.call('ritual_ZN7DomDate15clearElementDayEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomDate::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomDate.read' has no cute function yet. Qt's 'void "
        "DomDate::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomDate::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomDate.write' has no cute function yet. Qt's 'void "
        "DomDate::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
