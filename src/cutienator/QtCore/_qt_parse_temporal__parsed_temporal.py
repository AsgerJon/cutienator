"""
QtParseTemporal::ParsedTemporal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtparsetemporal_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QtParseTemporal::ParsedTemporal to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QtParseTimeZone

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCalendar, QDate, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QDate = WAIT['QDate']
  QTime = WAIT['QTime']


class ParsedTemporal(QtParseTimeZone.ParsedZone):
  """
  The cute side of Qt's QtParseTemporal::ParsedTemporal: a plain Python
  object standing in front of one C++ QtParseTemporal::ParsedTemporal.

  It is built on the cute 'QtParseTimeZone::ParsedZone', as Qt's
  QtParseTemporal::ParsedTemporal is built on Qt's
  QtParseTimeZone::ParsedZone, and has everything that class has.

  C++ hands a QtParseTemporal::ParsedTemporal around as a copy, so every C++
  QtParseTemporal::ParsedTemporal behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtParseTemporal::ParsedTemporal that has a ritual
  and that Python can call so far, 2 names in all: 'date', 'time'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtParseTemporal::ParsedTemporal::~ParsedTemporal()': the
    destructor: Python removes its C++ QtParseTemporal::ParsedTemporal by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtParseTemporal::ParsedTemporal is created at the first use, not
    by 'QtParseTemporal::ParsedTemporal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtParseTemporal::ParsedTemporal back gives a copy the
    ritual made for Python, in a new cute QtParseTemporal::ParsedTemporal.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtParseTemporal::ParsedTemporal'

  #  Qt's '~QtParseTemporal::ParsedTemporal()'. Naming it makes this a value
  #  class: Python owns every C++ QtParseTemporal::ParsedTemporal behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN15QtParseTemporal14ParsedTemporalD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCalendar)
  @overload(QCalendar, QDate)
  def date(self, cal: QCalendar, defaults: Optional[QDate] = None) -> QDate:
    """
    Calls Qt's 'QDate QtParseTemporal::ParsedTemporal::date(QCalendar cal,
    QDate defaults) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtparsetemporal-parsedtemporal.html#date

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    defaults : Optional[QDate]
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
      May be left out, as in Qt: a new 'QDate()' is then passed on.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QtParseTemporal::ParsedTemporal::date(QCalendar cal, QDate
    #      defaults) const
    if defaults is None:
      from . import QDate
      defaults = QDate()
    address = self.uglySide.call(
        'ritual_ZNK15QtParseTemporal14ParsedTemporal4dateE9QCalendar5QDate',
        self._valueOf(cal), self._valueOf(defaults),
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload()
  @overload(QTime)
  def time(self, defaults: Optional[QTime] = None) -> QTime:
    """
    Calls Qt's 'QTime QtParseTemporal::ParsedTemporal::time(QTime defaults)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtparsetemporal-parsedtemporal.html#time

    Parameters
    ----------

    defaults : Optional[QTime]
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
      May be left out, as in Qt: a new 'QTime()' is then passed on.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QtParseTemporal::ParsedTemporal::time(QTime defaults) const
    if defaults is None:
      from . import QTime
      defaults = QTime()
    address = self.uglySide.call(
        'ritual_ZNK15QtParseTemporal14ParsedTemporal4timeE5QTime',
        self._valueOf(defaults),
    )
    from . import QTime
    return QTime._cuteOwning(address)

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
