"""
QRegularExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QRegularExpressionMatch, QRegularExpressionMatchIterator


class QRegularExpression(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRegularExpression: a plain Python object standing in
  front of one C++ QRegularExpression.

  C++ hands a QRegularExpression around as a copy, so every C++
  QRegularExpression behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRegularExpression that has a ritual and that Python
  can call so far, 17 names in all: 'patternOptions', 'setPatternOptions',
  'pattern', 'setPattern', 'isValid', 'patternErrorOffset', 'errorString',
  'captureCount', 'match', 'matchView', 'globalMatch', 'globalMatchView',
  'optimize', 'escape', 'wildcardToRegularExpression', 'anchoredPattern',
  'fromWildcard'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRegularExpression::~QRegularExpression()': the destructor: Python
    removes its C++ QRegularExpression by it, and has no other use for it.
  - Qt's 'QRegularExpressionMatch QRegularExpression::match(QStringView
    subjectView, qsizetype offset, MatchType matchType, MatchOptions
    matchOptions) const': takes in Python what 'QRegularExpressionMatch
    QRegularExpression::match(const QString &subject, qsizetype offset,
    MatchType matchType, MatchOptions matchOptions) const' takes.
  - Qt's 'QRegularExpressionMatchIterator
    QRegularExpression::globalMatch(QStringView subjectView, qsizetype
    offset, MatchType matchType, MatchOptions matchOptions) const': takes in
    Python what 'QRegularExpressionMatchIterator
    QRegularExpression::globalMatch(const QString &subject, qsizetype offset,
    MatchType matchType, MatchOptions matchOptions) const' takes.
  - Qt's 'QString QRegularExpression::escape(QStringView str)': takes in
    Python what 'QString QRegularExpression::escape(const QString &str)'
    takes.
  - Qt's 'QString QRegularExpression::wildcardToRegularExpression(QStringView
    str, WildcardConversionOptions options)': takes in Python what 'QString
    QRegularExpression::wildcardToRegularExpression(const QString &str,
    WildcardConversionOptions options)' takes.
  - Qt's 'QString QRegularExpression::anchoredPattern(QStringView
    expression)': takes in Python what 'QString
    QRegularExpression::anchoredPattern(const QString &expression)' takes.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QRegularExpression is created at the first use, not by
    'QRegularExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRegularExpression back gives a copy the ritual made
    for Python, in a new cute QRegularExpression.
  """

  #  The enums Qt writes inside QRegularExpression, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MatchOption(CuteFlags):
    """
    The flags enum 'QRegularExpression::MatchOption' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QRegularExpression::MatchOptions'.
    """

    NoMatchOption = 0x0
    AnchorAtOffsetMatchOption = 0x1
    AnchoredMatchOption = 0x1
    DontCheckSubjectStringMatchOption = 0x2

  MatchOptions = MatchOption

  class MatchType(CuteNum):
    """
    The enum 'QRegularExpression::MatchType' of Qt, with the 4 names Qt gives
    in it.
    """

    NormalMatch = Kee[int](0)
    PartialPreferCompleteMatch = Kee[int](1)
    PartialPreferFirstMatch = Kee[int](2)
    NoMatch = Kee[int](3)

  class PatternOption(CuteFlags):
    """
    The flags enum 'QRegularExpression::PatternOption' of Qt, with the 8
    names Qt gives in it. Qt names the type of its combinations
    'QRegularExpression::PatternOptions'.
    """

    NoPatternOption = 0x0
    CaseInsensitiveOption = 0x1
    DotMatchesEverythingOption = 0x2
    MultilineOption = 0x4
    ExtendedPatternSyntaxOption = 0x8
    InvertedGreedinessOption = 0x10
    DontCaptureOption = 0x20
    UseUnicodePropertiesOption = 0x40

  PatternOptions = PatternOption

  class WildcardConversionOption(CuteFlags):
    """
    The flags enum 'QRegularExpression::WildcardConversionOption' of Qt, with
    the 3 names Qt gives in it. Qt names the type of its combinations
    'QRegularExpression::WildcardConversionOptions'.
    """

    DefaultWildcardConversion = 0x0
    UnanchoredWildcardConversion = 0x1
    NonPathWildcardConversion = 0x2

  WildcardConversionOptions = WildcardConversionOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def escape(str: str) -> str:
    """
    Calls Qt's 'QString QRegularExpression::escape(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#escape

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpression::escape(const QString &str)
    return Rituals.call(
        'ritual_ZN18QRegularExpression6escapeERK7QString', str,
    )

  @staticmethod
  @overload(str)
  @overload(str, WildcardConversionOptions)
  def wildcardToRegularExpression(
      str: str,
      options: WildcardConversionOptions = (
          WildcardConversionOptions.DefaultWildcardConversion),
  ) -> str:
    """
    Calls Qt's 'QString QRegularExpression::wildcardToRegularExpression(const
    QString &str, WildcardConversionOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    options : WildcardConversionOptions
      Passed on as its number. May be left out, as in Qt: it is then
      WildcardConversionOptions.DefaultWildcardConversion.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpression::wildcardToRegularExpression(const QString
    #      &str, WildcardConversionOptions options)
    return Rituals.call(
        'ritual_ZN18QRegularExpression27wildcardToRegularExpressionERK7QStr'
        'ing6QFlagsINS_24WildcardConversionOptionEE',
        str, options.value,
    )

  @staticmethod
  @overload(str)
  def anchoredPattern(expression: str) -> str:
    """
    Calls Qt's 'QString QRegularExpression::anchoredPattern(const QString
    &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#anchoredPattern

    Parameters
    ----------

    expression : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpression::anchoredPattern(const QString &expression)
    return Rituals.call(
        'ritual_ZN18QRegularExpression15anchoredPatternERK7QString',
        expression,
    )

  @staticmethod
  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  @overload(str, Qt.CaseSensitivity, WildcardConversionOptions)
  def fromWildcard(
      pattern: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseInsensitive,
      options: WildcardConversionOptions = (
          WildcardConversionOptions.DefaultWildcardConversion),
  ) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QRegularExpression::fromWildcard(QStringView pattern, Qt::CaseSensitivity
    cs, WildcardConversionOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#fromWildcard

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseInsensitive.

    options : WildcardConversionOptions
      Passed on as its number. May be left out, as in Qt: it is then
      WildcardConversionOptions.DefaultWildcardConversion.

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QRegularExpression::fromWildcard(QStringView
    #      pattern, Qt::CaseSensitivity cs, WildcardConversionOptions
    #      options)
    address = Rituals.call(
        'ritual_ZN18QRegularExpression12fromWildcardE11QStringViewN2Qt15Cas'
        'eSensitivityE6QFlagsINS_24WildcardConversionOptionEE',
        pattern, cs.value, options.value,
    )
    return QRegularExpression._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegularExpression'

  #  Qt's '~QRegularExpression()'. Naming it makes this a value class: Python
  #  owns every C++ QRegularExpression behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QRegularExpressionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def patternOptions(self) -> PatternOptions:
    """
    Calls Qt's 'PatternOptions QRegularExpression::patternOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#patternOptions

    Returns
    -------

    PatternOptions
      The value standing for the combination Qt gave back.
    """
    #  PatternOptions QRegularExpression::patternOptions() const
    return QRegularExpression.PatternOptions(self.uglySide.call(
        'ritual_ZNK18QRegularExpression14patternOptionsEv',
    ))

  def pattern(self) -> str:
    """
    Calls Qt's 'QString QRegularExpression::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#pattern

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpression::pattern() const
    return self.uglySide.call('ritual_ZNK18QRegularExpression7patternEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpression::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#isValid
    """
    #  bool QRegularExpression::isValid() const
    return self.uglySide.call('ritual_ZNK18QRegularExpression7isValidEv')

  def patternErrorOffset(self) -> int:
    """
    Calls Qt's 'qsizetype QRegularExpression::patternErrorOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#patternErrorOffset
    """
    #  qsizetype QRegularExpression::patternErrorOffset() const
    return self.uglySide.call(
        'ritual_ZNK18QRegularExpression18patternErrorOffsetEv',
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QRegularExpression::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpression::errorString() const
    return self.uglySide.call(
        'ritual_ZNK18QRegularExpression11errorStringEv',
    )

  def captureCount(self) -> int:
    """
    Calls Qt's 'int QRegularExpression::captureCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#captureCount
    """
    #  int QRegularExpression::captureCount() const
    return self.uglySide.call(
        'ritual_ZNK18QRegularExpression12captureCountEv',
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, MatchType)
  @overload(str, int, MatchType, MatchOptions)
  def match(
      self,
      subject: str,
      offset: int = 0,
      matchType: MatchType = MatchType.NormalMatch,
      matchOptions: MatchOptions = MatchOptions.NoMatchOption,
  ) -> QRegularExpressionMatch:
    """
    Calls Qt's 'QRegularExpressionMatch QRegularExpression::match(const
    QString &subject, qsizetype offset, MatchType matchType, MatchOptions
    matchOptions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#match

    Parameters
    ----------

    subject : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    matchType : MatchType
      Passed on as its number. May be left out, as in Qt: it is then
      MatchType.NormalMatch.

    matchOptions : MatchOptions
      Passed on as its number. May be left out, as in Qt: it is then
      MatchOptions.NoMatchOption.

    Returns
    -------

    QRegularExpressionMatch
      A new cute QRegularExpressionMatch around the copy Qt gave back. Python
      owns it.
    """
    #  QRegularExpressionMatch QRegularExpression::match(const QString
    #      &subject, qsizetype offset, MatchType matchType, MatchOptions
    #      matchOptions) const
    address = self.uglySide.call(
        'ritual_ZNK18QRegularExpression5matchERK7QStringxNS_9MatchTypeE6QFl'
        'agsINS_11MatchOptionEE',
        subject, offset, matchType.value, matchOptions.value,
    )
    from . import QRegularExpressionMatch
    return QRegularExpressionMatch._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, MatchType)
  @overload(str, int, MatchType, MatchOptions)
  def matchView(
      self,
      subjectView: str,
      offset: int = 0,
      matchType: MatchType = MatchType.NormalMatch,
      matchOptions: MatchOptions = MatchOptions.NoMatchOption,
  ) -> QRegularExpressionMatch:
    """
    Calls Qt's 'QRegularExpressionMatch
    QRegularExpression::matchView(QStringView subjectView, qsizetype offset,
    MatchType matchType, MatchOptions matchOptions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#matchView

    Parameters
    ----------

    subjectView : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    matchType : MatchType
      Passed on as its number. May be left out, as in Qt: it is then
      MatchType.NormalMatch.

    matchOptions : MatchOptions
      Passed on as its number. May be left out, as in Qt: it is then
      MatchOptions.NoMatchOption.

    Returns
    -------

    QRegularExpressionMatch
      A new cute QRegularExpressionMatch around the copy Qt gave back. Python
      owns it.
    """
    #  QRegularExpressionMatch QRegularExpression::matchView(QStringView
    #      subjectView, qsizetype offset, MatchType matchType, MatchOptions
    #      matchOptions) const
    address = self.uglySide.call(
        'ritual_ZNK18QRegularExpression9matchViewE11QStringViewxNS_9MatchTy'
        'peE6QFlagsINS_11MatchOptionEE',
        subjectView, offset, matchType.value, matchOptions.value,
    )
    from . import QRegularExpressionMatch
    return QRegularExpressionMatch._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, MatchType)
  @overload(str, int, MatchType, MatchOptions)
  def globalMatch(
      self,
      subject: str,
      offset: int = 0,
      matchType: MatchType = MatchType.NormalMatch,
      matchOptions: MatchOptions = MatchOptions.NoMatchOption,
  ) -> QRegularExpressionMatchIterator:
    """
    Calls Qt's 'QRegularExpressionMatchIterator
    QRegularExpression::globalMatch(const QString &subject, qsizetype offset,
    MatchType matchType, MatchOptions matchOptions) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#globalMatch

    Parameters
    ----------

    subject : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    matchType : MatchType
      Passed on as its number. May be left out, as in Qt: it is then
      MatchType.NormalMatch.

    matchOptions : MatchOptions
      Passed on as its number. May be left out, as in Qt: it is then
      MatchOptions.NoMatchOption.

    Returns
    -------

    QRegularExpressionMatchIterator
      A new cute QRegularExpressionMatchIterator around the copy Qt gave
      back. Python owns it.
    """
    #  QRegularExpressionMatchIterator QRegularExpression::globalMatch(const
    #      QString &subject, qsizetype offset, MatchType matchType,
    #      MatchOptions matchOptions) const
    address = self.uglySide.call(
        'ritual_ZNK18QRegularExpression11globalMatchERK7QStringxNS_9MatchTy'
        'peE6QFlagsINS_11MatchOptionEE',
        subject, offset, matchType.value, matchOptions.value,
    )
    from . import QRegularExpressionMatchIterator
    return QRegularExpressionMatchIterator._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, MatchType)
  @overload(str, int, MatchType, MatchOptions)
  def globalMatchView(
      self,
      subjectView: str,
      offset: int = 0,
      matchType: MatchType = MatchType.NormalMatch,
      matchOptions: MatchOptions = MatchOptions.NoMatchOption,
  ) -> QRegularExpressionMatchIterator:
    """
    Calls Qt's 'QRegularExpressionMatchIterator
    QRegularExpression::globalMatchView(QStringView subjectView, qsizetype
    offset, MatchType matchType, MatchOptions matchOptions) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#globalMatchView

    Parameters
    ----------

    subjectView : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    matchType : MatchType
      Passed on as its number. May be left out, as in Qt: it is then
      MatchType.NormalMatch.

    matchOptions : MatchOptions
      Passed on as its number. May be left out, as in Qt: it is then
      MatchOptions.NoMatchOption.

    Returns
    -------

    QRegularExpressionMatchIterator
      A new cute QRegularExpressionMatchIterator around the copy Qt gave
      back. Python owns it.
    """
    #  QRegularExpressionMatchIterator
    #      QRegularExpression::globalMatchView(QStringView subjectView,
    #      qsizetype offset, MatchType matchType, MatchOptions matchOptions)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QRegularExpression15globalMatchViewE11QStringViewxNS_9'
        'MatchTypeE6QFlagsINS_11MatchOptionEE',
        subjectView, offset, matchType.value, matchOptions.value,
    )
    from . import QRegularExpressionMatchIterator
    return QRegularExpressionMatchIterator._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PatternOptions)
  def setPatternOptions(self, options: PatternOptions) -> None:
    """
    Calls Qt's 'void QRegularExpression::setPatternOptions(PatternOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#setPatternOptions

    Parameters
    ----------

    options : PatternOptions
      Passed on as its number.
    """
    #  void QRegularExpression::setPatternOptions(PatternOptions options)
    self.uglySide.call(
        'ritual_ZN18QRegularExpression17setPatternOptionsE6QFlagsINS_13Patt'
        'ernOptionEE',
        options.value,
    )

  @overload(str)
  def setPattern(self, pattern: str) -> None:
    """
    Calls Qt's 'void QRegularExpression::setPattern(const QString &pattern)'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#setPattern

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRegularExpression::setPattern(const QString &pattern)
    self.uglySide.call(
        'ritual_ZN18QRegularExpression10setPatternERK7QString', pattern,
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
    Notes what was given, for Qt's
    'QRegularExpression::QRegularExpression()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#QRegularExpression
    """
    #  QRegularExpression::QRegularExpression()
    self._noteCreation(QRegularExpression, lambda: Rituals.call(
        'ritual_ZN18QRegularExpressionC1Ev',
    ))

  @overload(str)
  @overload(str, PatternOptions)
  def __init__(
      self,
      pattern: str,
      options: PatternOptions = PatternOptions.NoPatternOption,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpression::QRegularExpression(const QString &pattern,
    PatternOptions options)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#QRegularExpression

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    options : PatternOptions
      Passed on as its number. May be left out, as in Qt: it is then
      PatternOptions.NoPatternOption.
    """
    #  QRegularExpression::QRegularExpression(const QString &pattern,
    #      PatternOptions options)
    self._noteCreation(QRegularExpression, lambda: Rituals.call(
        'ritual_ZN18QRegularExpressionC1ERK7QString6QFlagsINS_13PatternOpti'
        'onEE',
        pattern, options.value,
    ))

  @overload(THIS)
  def __init__(self, re: QRegularExpression) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpression::QRegularExpression(const QRegularExpression &re)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpression.html#QRegularExpression

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  QRegularExpression::QRegularExpression(const QRegularExpression &re)
    self._noteCreation(QRegularExpression, lambda: Rituals.call(
        'ritual_ZN18QRegularExpressionC1ERKS_', self._valueOf(re),
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

  def optimize(self) -> None:
    """
    Calls Qt's 'void QRegularExpression::optimize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregularexpression.html#optimize
    """
    #  void QRegularExpression::optimize() const
    self.uglySide.call('ritual_ZNK18QRegularExpression8optimizeEv')
