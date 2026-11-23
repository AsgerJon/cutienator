"""
QCollator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QChar, QCollatorSortKey, QLocale
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCollator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCollator: a plain Python object standing in front of
  one C++ QCollator.

  C++ hands a QCollator around as a copy, so every C++ QCollator behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCollator that has a ritual and that Python can call
  so far, 16 names in all: 'setLocale', 'locale', 'caseSensitivity',
  'setCaseSensitivity', 'setNumericMode', 'numericMode',
  'setIgnorePunctuation', 'ignorePunctuation', 'compare', '__call__',
  'sortKey', 'defaultCompare', 'defaultSortKey', '__eq__', '__ne__',
  'detach'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCollator::~QCollator()': the destructor: Python removes its C++
    QCollator by it, and has no other use for it.
  - Qt's 'int QCollator::compare(QStringView s1, QStringView s2) const':
    takes in Python what 'int QCollator::compare(const QString &s1, const
    QString &s2) const' takes.
  - Qt's 'bool QCollator::operator()(QStringView s1, QStringView s2) const':
    takes in Python what 'bool QCollator::operator()(const QString &s1, const
    QString &s2) const' takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QCollator is created at the first use, not by 'QCollator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCollator back gives a copy the ritual made for
    Python, in a new cute QCollator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str)
  def defaultCompare(s1: str, s2: str) -> int:
    """
    Calls Qt's 'int QCollator::defaultCompare(QStringView s1, QStringView
    s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#defaultCompare

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QCollator::defaultCompare(QStringView s1, QStringView s2)
    return Rituals.call(
        'ritual_ZN9QCollator14defaultCompareE11QStringViewS0_', s1, s2,
    )

  @staticmethod
  @overload(str)
  def defaultSortKey(key: str) -> QCollatorSortKey:
    """
    Calls Qt's 'QCollatorSortKey QCollator::defaultSortKey(QStringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#defaultSortKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCollatorSortKey
      A new cute QCollatorSortKey around the copy Qt gave back. Python owns
      it.
    """
    #  QCollatorSortKey QCollator::defaultSortKey(QStringView key)
    address = Rituals.call(
        'ritual_ZN9QCollator14defaultSortKeyE11QStringView', key,
    )
    from . import QCollatorSortKey
    return QCollatorSortKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCollator'

  #  Qt's '~QCollator()'. Naming it makes this a value class: Python owns
  #  every C++ QCollator behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QCollatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QCollator::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QCollator::locale() const
    address = self.uglySide.call('ritual_ZNK9QCollator6localeEv')
    from . import QLocale
    return QLocale._cuteOwning(address)

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QCollator::caseSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QCollator::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK9QCollator15caseSensitivityEv',
    ))

  def numericMode(self) -> bool:
    """
    Calls Qt's 'bool QCollator::numericMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#numericMode
    """
    #  bool QCollator::numericMode() const
    return self.uglySide.call('ritual_ZNK9QCollator11numericModeEv')

  def ignorePunctuation(self) -> bool:
    """
    Calls Qt's 'bool QCollator::ignorePunctuation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#ignorePunctuation
    """
    #  bool QCollator::ignorePunctuation() const
    return self.uglySide.call('ritual_ZNK9QCollator17ignorePunctuationEv')

  @overload(str, str)
  def compare(self, s1: str, s2: str) -> int:
    """
    Calls Qt's 'int QCollator::compare(const QString &s1, const QString &s2)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#compare

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QCollator::compare(const QString &s1, const QString &s2) const
    return self.uglySide.call(
        'ritual_ZNK9QCollator7compareERK7QStringS2_', s1, s2,
    )

  @overload(QChar, int, QChar, int)
  @overload(QChar, int, NoneType, int)
  @overload(NoneType, int, QChar, int)
  @overload(NoneType, int, NoneType, int)
  def compare(
      self,
      s1: Optional[QChar],
      len1: int,
      s2: Optional[QChar],
      len2: int,
  ) -> int:
    """
    Calls Qt's 'int QCollator::compare(const QChar *s1, qsizetype len1, const
    QChar *s2, qsizetype len2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#compare

    Parameters
    ----------

    s1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len1 : int
      Passed on as it is.

    s2 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len2 : int
      Passed on as it is.
    """
    #  int QCollator::compare(const QChar *s1, qsizetype len1, const QChar
    #      *s2, qsizetype len2) const
    return self.uglySide.call(
        'ritual_ZNK9QCollator7compareEPK5QCharxS2_x',
        self._addressOf(s1), len1, self._addressOf(s2), len2,
    )

  @overload(str)
  def sortKey(self, string: str) -> QCollatorSortKey:
    """
    Calls Qt's 'QCollatorSortKey QCollator::sortKey(const QString &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#sortKey

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCollatorSortKey
      A new cute QCollatorSortKey around the copy Qt gave back. Python owns
      it.
    """
    #  QCollatorSortKey QCollator::sortKey(const QString &string) const
    address = self.uglySide.call(
        'ritual_ZNK9QCollator7sortKeyERK7QString', string,
    )
    from . import QCollatorSortKey
    return QCollatorSortKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QCollator::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QCollator::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN9QCollator9setLocaleERK7QLocale', self._valueOf(locale),
    )

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void QCollator::setCaseSensitivity(Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#setCaseSensitivity

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QCollator::setCaseSensitivity(Qt::CaseSensitivity cs)
    self.uglySide.call(
        'ritual_ZN9QCollator18setCaseSensitivityEN2Qt15CaseSensitivityE',
        cs.value,
    )

  @overload(bool)
  def setNumericMode(self, on: bool) -> None:
    """
    Calls Qt's 'void QCollator::setNumericMode(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#setNumericMode

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QCollator::setNumericMode(bool on)
    self.uglySide.call('ritual_ZN9QCollator14setNumericModeEb', on)

  @overload(bool)
  def setIgnorePunctuation(self, on: bool) -> None:
    """
    Calls Qt's 'void QCollator::setIgnorePunctuation(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollator.html#setIgnorePunctuation

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QCollator::setIgnorePunctuation(bool on)
    self.uglySide.call('ritual_ZN9QCollator20setIgnorePunctuationEb', on)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def __call__(self, s1: str, s2: str) -> bool:
    """
    Calls Qt's 'bool QCollator::operator()(const QString &s1, const QString
    &s2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#operator()

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCollator::operator()(const QString &s1, const QString &s2) const
    return self.uglySide.call('ritual_ZNK9QCollatorclERK7QStringS2_', s1, s2)

  @overload(THIS)
  def __eq__(self, rhs: QCollator) -> bool:
    """
    Calls Qt's 'bool operator==(const QCollator &lhs, const QCollator &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#operator==

    Parameters
    ----------

    rhs : QCollator
      Passed on as a value: Qt reads the C++ QCollator, which stays Python's
      own.
    """
    #  bool operator==(const QCollator &lhs, const QCollator &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QCollatorS1_',
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
  def __ne__(self, rhs: QCollator) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCollator &lhs, const QCollator &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#operator!=

    Parameters
    ----------

    rhs : QCollator
      Passed on as a value: Qt reads the C++ QCollator, which stays Python's
      own.
    """
    #  bool operator!=(const QCollator &lhs, const QCollator &rhs)
    return Rituals.call(
        'ritual_ZneRK9QCollatorS1_',
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
    Notes what was given, for Qt's 'QCollator::QCollator()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#QCollator
    """
    #  QCollator::QCollator()
    self._noteCreation(QCollator, lambda: Rituals.call(
        'ritual_ZN9QCollatorC1Ev',
    ))

  @overload(QLocale)
  def __init__(self, locale: QLocale) -> None:
    """
    Notes what was given, for Qt's 'QCollator::QCollator(const QLocale
    &locale)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#QCollator

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  QCollator::QCollator(const QLocale &locale)
    self._noteCreation(QCollator, lambda: Rituals.call(
        'ritual_ZN9QCollatorC1ERK7QLocale', self._valueOf(locale),
    ))

  @overload(THIS)
  def __init__(self, a0: QCollator) -> None:
    """
    Notes what was given, for Qt's 'QCollator::QCollator(const QCollator
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#QCollator

    Parameters
    ----------

    a0 : QCollator
      Passed on as a value: Qt reads the C++ QCollator, which stays Python's
      own.
    """
    #  QCollator::QCollator(const QCollator &a0)
    self._noteCreation(QCollator, lambda: Rituals.call(
        'ritual_ZN9QCollatorC1ERKS_', self._valueOf(a0),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QCollator::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qcollator.html#detach
    """
    #  void QCollator::detach()
    self.uglySide.call('ritual_ZN9QCollator6detachEv')
