"""
QStringMatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringmatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringMatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringMatcher: a plain Python object standing in
  front of one C++ QStringMatcher.

  C++ hands a QStringMatcher around as a copy, so every C++ QStringMatcher
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringMatcher that has a ritual and that Python can
  call so far, 6 names in all: 'setPattern', 'setCaseSensitivity', 'indexIn',
  'pattern', 'patternView', 'caseSensitivity'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStringMatcher::QStringMatcher(QStringView pattern,
    Qt::CaseSensitivity cs)': takes in Python what
    'QStringMatcher::QStringMatcher(const QString &pattern,
    Qt::CaseSensitivity cs)' takes.
  - Qt's 'QStringMatcher::~QStringMatcher()': the destructor: Python removes
    its C++ QStringMatcher by it, and has no other use for it.
  - Qt's 'qsizetype QStringMatcher::indexIn(QStringView str, qsizetype from)
    const': takes in Python what 'qsizetype QStringMatcher::indexIn(const
    QString &str, qsizetype from) const' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 1 private; 1 takes or gives a type that
  cannot be passed yet.

  What to expect
  --------------

  - The C++ QStringMatcher is created at the first use, not by
    'QStringMatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringMatcher back gives a copy the ritual made for
    Python, in a new cute QStringMatcher.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringMatcher'

  #  Qt's '~QStringMatcher()'. Naming it makes this a value class: Python
  #  owns every C++ QStringMatcher behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QStringMatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  def indexIn(self, str: str, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QStringMatcher::indexIn(const QString &str,
    qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#indexIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QStringMatcher::indexIn(const QString &str, qsizetype from)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QStringMatcher7indexInERK7QStringx', str, from_,
    )

  @overload(QChar, int)
  @overload(NoneType, int)
  @overload(QChar, int, int)
  @overload(NoneType, int, int)
  def indexIn(
      self,
      str: Optional[QChar],
      length: int,
      from_: int = 0,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringMatcher::indexIn(const QChar *str, qsizetype
    length, qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#indexIn

    Parameters
    ----------

    str : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length : int
      Passed on as it is.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QStringMatcher::indexIn(const QChar *str, qsizetype length,
    #      qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK14QStringMatcher7indexInEPK5QCharxx',
        self._addressOf(str), length, from_,
    )

  def pattern(self) -> str:
    """
    Calls Qt's 'QString QStringMatcher::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#pattern

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringMatcher::pattern() const
    return self.uglySide.call('ritual_ZNK14QStringMatcher7patternEv')

  def patternView(self) -> str:
    """
    Calls Qt's 'QStringView QStringMatcher::patternView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#patternView

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringMatcher::patternView() const
    return self.uglySide.call('ritual_ZNK14QStringMatcher11patternViewEv')

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QStringMatcher::caseSensitivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringmatcher.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QStringMatcher::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK14QStringMatcher15caseSensitivityEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPattern(self, pattern: str) -> None:
    """
    Calls Qt's 'void QStringMatcher::setPattern(const QString &pattern)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#setPattern

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStringMatcher::setPattern(const QString &pattern)
    self.uglySide.call(
        'ritual_ZN14QStringMatcher10setPatternERK7QString', pattern,
    )

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void QStringMatcher::setCaseSensitivity(Qt::CaseSensitivity
    cs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringmatcher.html#setCaseSensitivity

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QStringMatcher::setCaseSensitivity(Qt::CaseSensitivity cs)
    self.uglySide.call(
        'ritual_ZN14QStringMatcher18setCaseSensitivityEN2Qt15CaseSensitivit'
        'yE',
        cs.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStringMatcher::QStringMatcher()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#QStringMatcher
    """
    #  QStringMatcher::QStringMatcher()
    self._noteCreation(QStringMatcher, lambda: Rituals.call(
        'ritual_ZN14QStringMatcherC1Ev',
    ))

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def __init__(
      self,
      pattern: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringMatcher::QStringMatcher(const
    QString &pattern, Qt::CaseSensitivity cs)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#QStringMatcher

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  QStringMatcher::QStringMatcher(const QString &pattern,
    #      Qt::CaseSensitivity cs)
    self._noteCreation(QStringMatcher, lambda: Rituals.call(
        'ritual_ZN14QStringMatcherC1ERK7QStringN2Qt15CaseSensitivityE',
        pattern, cs.value,
    ))

  @overload(QChar, int)
  @overload(NoneType, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  @overload(NoneType, int, Qt.CaseSensitivity)
  def __init__(
      self,
      uc: Optional[QChar],
      len: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringMatcher::QStringMatcher(const
    QChar *uc, qsizetype len, Qt::CaseSensitivity cs)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#QStringMatcher

    Parameters
    ----------

    uc : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  QStringMatcher::QStringMatcher(const QChar *uc, qsizetype len,
    #      Qt::CaseSensitivity cs)
    self._noteCreation(QStringMatcher, lambda: Rituals.call(
        'ritual_ZN14QStringMatcherC1EPK5QCharxN2Qt15CaseSensitivityE',
        self._addressOf(uc), len, cs.value,
    ))

  @overload(THIS)
  def __init__(self, other: QStringMatcher) -> None:
    """
    Notes what was given, for Qt's 'QStringMatcher::QStringMatcher(const
    QStringMatcher &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringmatcher.html#QStringMatcher

    Parameters
    ----------

    other : QStringMatcher
      Passed on as a value: Qt reads the C++ QStringMatcher, which stays
      Python's own.
    """
    #  QStringMatcher::QStringMatcher(const QStringMatcher &other)
    self._noteCreation(QStringMatcher, lambda: Rituals.call(
        'ritual_ZN14QStringMatcherC1ERKS_', self._valueOf(other),
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
