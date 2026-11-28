"""
QTimePattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTimePattern to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtTemporalPattern, QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTime = WAIT['QTime']


class QTimePattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTimePattern: a plain Python object standing in front
  of one C++ QTimePattern.

  C++ hands a QTimePattern around as a copy, so every C++ QTimePattern behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTimePattern that has a ritual and that Python can
  call so far, 7 names in all: 'timeSupport', 'isValid', 'setLocale',
  'locale', 'serialize', 'fromQtFormat', 'forLocale'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimePattern::QTimePattern(const QList<Field> &fs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTemporalPattern::ParseResult<QTime>
    QTimePattern::parse(QStringView text, QTime defaults) const': gives a
    type Python has no way to take yet.
  - Qt's 'QTimePattern::~QTimePattern()': the destructor: Python removes its
    C++ QTimePattern by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTimePattern is created at the first use, not by
    'QTimePattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTimePattern back gives a copy the ritual made for
    Python, in a new cute QTimePattern.
  - Each name of Qt's QTimePattern that has no cute function yet, '__init__',
    'parse', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromQtFormat(format: str) -> QTimePattern:
    """
    Calls Qt's 'QTimePattern QTimePattern::fromQtFormat(QStringView format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#fromQtFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTimePattern
      A new cute QTimePattern around the copy Qt gave back. Python owns it.
    """
    #  QTimePattern QTimePattern::fromQtFormat(QStringView format)
    address = Rituals.call(
        'ritual_ZN12QTimePattern12fromQtFormatE11QStringView', format,
    )
    return QTimePattern._cuteOwning(address)

  @staticmethod
  @overload(QLocale)
  @overload(QLocale, QLocale.FormatType)
  def forLocale(
      locale: QLocale,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> QTimePattern:
    """
    Calls Qt's 'QTimePattern QTimePattern::forLocale(const QLocale &locale,
    QLocale::FormatType format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#forLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    QTimePattern
      A new cute QTimePattern around the copy Qt gave back. Python owns it.
    """
    #  QTimePattern QTimePattern::forLocale(const QLocale &locale,
    #      QLocale::FormatType format)
    address = Rituals.call(
        'ritual_ZN12QTimePattern9forLocaleERK7QLocaleNS0_10FormatTypeE',
        CuteMixin._valueOf(locale), format.value,
    )
    return QTimePattern._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimePattern'

  #  Qt's '~QTimePattern()'. Naming it makes this a value class: Python owns
  #  every C++ QTimePattern behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QTimePatternD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def timeSupport(self) -> QtTemporalPattern.SupportType:
    """
    Calls Qt's 'QtTemporalPattern::SupportType QTimePattern::timeSupport()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#timeSupport

    Returns
    -------

    QtTemporalPattern.SupportType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtTemporalPattern.SupportType(number)' gives.
    """
    #  QtTemporalPattern::SupportType QTimePattern::timeSupport() const
    return QtTemporalPattern.SupportType(self.uglySide.call(
        'ritual_ZNK12QTimePattern11timeSupportEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTimePattern::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#isValid
    """
    #  bool QTimePattern::isValid() const
    return self.uglySide.call('ritual_ZNK12QTimePattern7isValidEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'const QLocale &QTimePattern::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  const QLocale &QTimePattern::locale() const
    address = self.uglySide.call('ritual_ZNK12QTimePattern6localeEv')
    return QLocale._cuteOwning(address)

  @overload(QTime)
  def serialize(self, time: QTime) -> str:
    """
    Calls Qt's 'QString QTimePattern::serialize(const QTime &time) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#serialize

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimePattern::serialize(const QTime &time) const
    return self.uglySide.call(
        'ritual_ZNK12QTimePattern9serializeERK5QTime', self._valueOf(time),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, loc: QLocale) -> None:
    """
    Calls Qt's 'void QTimePattern::setLocale(const QLocale &loc)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimepattern.html#setLocale

    Parameters
    ----------

    loc : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QTimePattern::setLocale(const QLocale &loc)
    self.uglySide.call(
        'ritual_ZN12QTimePattern9setLocaleERK7QLocale', self._valueOf(loc),
    )

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
    Qt's 'QTimePattern::QTimePattern(const QList<Field> &fs)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTimePattern.__init__' has no cute function yet. Qt's "
        "'QTimePattern::QTimePattern(const QList<Field> &fs)': takes a type "
        "Python has no way to hand over yet.")

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
  def parse(*__, **_) -> Never:
    """
    Qt's 'QtTemporalPattern::ParseResult<QTime>
    QTimePattern::parse(QStringView text, QTime defaults) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimePattern.parse' has no cute function yet. Qt's "
        "'QtTemporalPattern::ParseResult<QTime> "
        "QTimePattern::parse(QStringView text, QTime defaults) const': "
        "gives a type Python has no way to take yet.")
