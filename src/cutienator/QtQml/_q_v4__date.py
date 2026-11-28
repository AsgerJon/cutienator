"""
QV4::Date binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Date to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDate, QDateTime, QTime, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']


class Date(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Date: a plain Python object standing in front of
  one C++ QV4::Date.

  C++ hands a QV4::Date around as a copy, so every C++ QV4::Date behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Date that has a ritual and that Python can call
  so far, 6 names in all: 'init', 'toQDate', 'toQTime', 'toQDateTime',
  'toVariant', 'encode'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Date &QV4::Date::operator=(double value)': assignment: Python binds
    a name and has no operator for it.
  - Qt's 'double QV4::Date::operator double() const': an operator Python has
    no name for.
  - Qt's 'QV4::Date::~Date()': the destructor: Python removes its C++
    QV4::Date by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 2 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::Date is created at the first use, not by 'QV4::Date(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Date back gives a copy the ritual made for
    Python, in a new cute QV4::Date.
  - Each name of Qt's QV4::Date that has no cute function yet,
    'withReadonlyStoragePointer', 'withWriteonlyStoragePointer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float)
  def encode(value: float) -> int:
    """
    Calls Qt's 'quint64 QV4::Date::encode(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#encode

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  quint64 QV4::Date::encode(double value)
    return Rituals.call('ritual_ZN3QV44Date6encodeEd', value)

  @staticmethod
  @overload(QDateTime)
  def encode(dateTime: QDateTime) -> int:
    """
    Calls Qt's 'quint64 QV4::Date::encode(const QDateTime &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#encode

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  quint64 QV4::Date::encode(const QDateTime &dateTime)
    return Rituals.call(
        'ritual_ZN3QV44Date6encodeERK9QDateTime',
        CuteMixin._valueOf(dateTime),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Date'

  #  Qt's '~QV4::Date()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::Date behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV44DateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toQDate(self) -> QDate:
    """
    Calls Qt's 'QDate QV4::Date::toQDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#toQDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QV4::Date::toQDate() const
    address = self.uglySide.call('ritual_ZNK3QV44Date7toQDateEv')
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def toQTime(self) -> QTime:
    """
    Calls Qt's 'QTime QV4::Date::toQTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#toQTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QV4::Date::toQTime() const
    address = self.uglySide.call('ritual_ZNK3QV44Date7toQTimeEv')
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  def toQDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QV4::Date::toQDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#toQDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QV4::Date::toQDateTime() const
    address = self.uglySide.call('ritual_ZNK3QV44Date11toQDateTimeEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::Date::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::Date::toVariant() const
    address = self.uglySide.call('ritual_ZNK3QV44Date9toVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  @overload()
  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Date::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#init
    """
    #  void QV4::Date::init()
    self.uglySide.call('ritual_ZN3QV44Date4initEv')

  @overload(THIS)
  def init(self, date: Date) -> None:
    """
    Calls Qt's 'void QV4::Date::init(Date date)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#init

    Parameters
    ----------

    date : Date
      Passed on as a value: Qt reads the C++ QV4::Date, which stays Python's
      own.
    """
    #  void QV4::Date::init(Date date)
    self.uglySide.call('ritual_ZN3QV44Date4initES0_', self._valueOf(date))

  @overload(float)
  def init(self, value: float) -> None:
    """
    Calls Qt's 'void QV4::Date::init(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#init

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QV4::Date::init(double value)
    self.uglySide.call('ritual_ZN3QV44Date4initEd', value)

  @overload(QDateTime)
  def init(self, dateTime: QDateTime) -> None:
    """
    Calls Qt's 'void QV4::Date::init(const QDateTime &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#init

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QV4::Date::init(const QDateTime &dateTime)
    self.uglySide.call(
        'ritual_ZN3QV44Date4initERK9QDateTime', self._valueOf(dateTime),
    )

  @overload(QDate)
  def init(self, date: QDate) -> None:
    """
    Calls Qt's 'void QV4::Date::init(QDate date)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-date.html#init

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QV4::Date::init(QDate date)
    self.uglySide.call('ritual_ZN3QV44Date4initE5QDate', self._valueOf(date))

  @staticmethod
  def withReadonlyStoragePointer(*__, **_) -> Never:
    """
    Qt's 'QV4::Date::withReadonlyStoragePointer': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.Date.withReadonlyStoragePointer' has no cute function yet. "
        "Qt's 'QV4::Date::withReadonlyStoragePointer': a template: a "
        "pattern and no single function.")

  @staticmethod
  def withWriteonlyStoragePointer(*__, **_) -> Never:
    """
    Qt's 'QV4::Date::withWriteonlyStoragePointer': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.Date.withWriteonlyStoragePointer' has no cute function yet. "
        "Qt's 'QV4::Date::withWriteonlyStoragePointer': a template: a "
        "pattern and no single function.")
