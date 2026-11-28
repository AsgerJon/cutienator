"""
QRegularExpressionMatch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QRegularExpression, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRegularExpressionMatch(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRegularExpressionMatch: a plain Python object
  standing in front of one C++ QRegularExpressionMatch.

  C++ hands a QRegularExpressionMatch around as a copy, so every C++
  QRegularExpressionMatch behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRegularExpressionMatch that has a ritual and that
  Python can call so far, 14 names in all: 'regularExpression', 'matchType',
  'matchOptions', 'hasMatch', 'hasPartialMatch', 'isValid',
  'lastCapturedIndex', 'hasCaptured', 'captured', 'capturedView',
  'capturedTexts', 'capturedStart', 'capturedLength', 'capturedEnd'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRegularExpressionMatch::~QRegularExpressionMatch()': the
    destructor: Python removes its C++ QRegularExpressionMatch by it, and has
    no other use for it.
  - Qt's
    'QRegularExpressionMatch::QRegularExpressionMatch(QRegularExpressionMatch
    &&match)': takes a type Python has no way to hand over yet.
  - Qt's 'QRegularExpressionMatch &QRegularExpressionMatch::operator=(const
    QRegularExpressionMatch &match)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QRegularExpressionMatch
    &QRegularExpressionMatch::operator=(QRegularExpressionMatch &&match)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QRegularExpressionMatch::swap(QRegularExpressionMatch
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QRegularExpressionMatch::QRegularExpressionMatch(
    QRegularExpressionMatchPrivate &dd)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QRegularExpressionMatch is created at the first use, not by
    'QRegularExpressionMatch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRegularExpressionMatch back gives a copy the ritual
    made for Python, in a new cute QRegularExpressionMatch.
  - Each name of Qt's QRegularExpressionMatch that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QRegularExpressionMatch'

  #  Qt's '~QRegularExpressionMatch()'. Naming it makes this a value class:
  #  Python owns every C++ QRegularExpressionMatch behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QRegularExpressionMatchD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def regularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QRegularExpressionMatch::regularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#regularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QRegularExpressionMatch::regularExpression() const
    address = self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch17regularExpressionEv',
    )
    return QRegularExpression._cuteOwning(address)

  def matchType(self) -> QRegularExpression.MatchType:
    """
    Calls Qt's 'QRegularExpression::MatchType
    QRegularExpressionMatch::matchType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#matchType

    Returns
    -------

    QRegularExpression.MatchType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRegularExpression.MatchType(number)' gives.
    """
    #  QRegularExpression::MatchType QRegularExpressionMatch::matchType()
    #      const
    return QRegularExpression.MatchType(self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch9matchTypeEv',
    ))

  def matchOptions(self) -> QRegularExpression.MatchOptions:
    """
    Calls Qt's 'QRegularExpression::MatchOptions
    QRegularExpressionMatch::matchOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#matchOptions

    Returns
    -------

    QRegularExpression.MatchOptions
      The value standing for the combination Qt gave back.
    """
    #  QRegularExpression::MatchOptions
    #      QRegularExpressionMatch::matchOptions() const
    return QRegularExpression.MatchOptions(self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch12matchOptionsEv',
    ))

  def hasMatch(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatch::hasMatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#hasMatch
    """
    #  bool QRegularExpressionMatch::hasMatch() const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch8hasMatchEv',
    )

  def hasPartialMatch(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatch::hasPartialMatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#hasPartialMatch
    """
    #  bool QRegularExpressionMatch::hasPartialMatch() const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch15hasPartialMatchEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatch::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#isValid
    """
    #  bool QRegularExpressionMatch::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch7isValidEv',
    )

  def lastCapturedIndex(self) -> int:
    """
    Calls Qt's 'int QRegularExpressionMatch::lastCapturedIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#lastCapturedIndex
    """
    #  int QRegularExpressionMatch::lastCapturedIndex() const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch17lastCapturedIndexEv',
    )

  @overload(str)
  def hasCaptured(self, name: str) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatch::hasCaptured(QAnyStringView
    name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#hasCaptured

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QRegularExpressionMatch::hasCaptured(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch11hasCapturedE14QAnyStringView',
        name,
    )

  @overload(int)
  def hasCaptured(self, nth: int) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatch::hasCaptured(int nth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#hasCaptured

    Parameters
    ----------

    nth : int
      Passed on as it is.
    """
    #  bool QRegularExpressionMatch::hasCaptured(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch11hasCapturedEi', nth,
    )

  @overload()
  @overload(int)
  def captured(self, nth: int = 0) -> str:
    """
    Calls Qt's 'QString QRegularExpressionMatch::captured(int nth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#captured

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpressionMatch::captured(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch8capturedEi', nth,
    )

  @overload(str)
  def captured(self, name: str) -> str:
    """
    Calls Qt's 'QString QRegularExpressionMatch::captured(QAnyStringView
    name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#captured

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegularExpressionMatch::captured(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch8capturedE14QAnyStringView',
        name,
    )

  @overload()
  @overload(int)
  def capturedView(self, nth: int = 0) -> str:
    """
    Calls Qt's 'QStringView QRegularExpressionMatch::capturedView(int nth)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedView

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QRegularExpressionMatch::capturedView(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch12capturedViewEi', nth,
    )

  @overload(str)
  def capturedView(self, name: str) -> str:
    """
    Calls Qt's 'QStringView
    QRegularExpressionMatch::capturedView(QAnyStringView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedView

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QRegularExpressionMatch::capturedView(QAnyStringView name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch12capturedViewE14QAnyStringView',
        name,
    )

  def capturedTexts(self) -> QStringList:
    """
    Calls Qt's 'QStringList QRegularExpressionMatch::capturedTexts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedTexts

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRegularExpressionMatch::capturedTexts() const
    address = self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch13capturedTextsEv',
    )
    return QStringList._cuteOwning(address)

  @overload()
  @overload(int)
  def capturedStart(self, nth: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QRegularExpressionMatch::capturedStart(int nth)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedStart

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QRegularExpressionMatch::capturedStart(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch13capturedStartEi', nth,
    )

  @overload(str)
  def capturedStart(self, name: str) -> int:
    """
    Calls Qt's 'qsizetype
    QRegularExpressionMatch::capturedStart(QAnyStringView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedStart

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QRegularExpressionMatch::capturedStart(QAnyStringView name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch13capturedStartE14QAnyStringVie'
        'w',
        name,
    )

  @overload()
  @overload(int)
  def capturedLength(self, nth: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QRegularExpressionMatch::capturedLength(int nth)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedLength

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QRegularExpressionMatch::capturedLength(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch14capturedLengthEi', nth,
    )

  @overload(str)
  def capturedLength(self, name: str) -> int:
    """
    Calls Qt's 'qsizetype
    QRegularExpressionMatch::capturedLength(QAnyStringView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedLength

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QRegularExpressionMatch::capturedLength(QAnyStringView name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch14capturedLengthE14QAnyStringVi'
        'ew',
        name,
    )

  @overload()
  @overload(int)
  def capturedEnd(self, nth: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QRegularExpressionMatch::capturedEnd(int nth)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedEnd

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QRegularExpressionMatch::capturedEnd(int nth) const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch11capturedEndEi', nth,
    )

  @overload(str)
  def capturedEnd(self, name: str) -> int:
    """
    Calls Qt's 'qsizetype QRegularExpressionMatch::capturedEnd(QAnyStringView
    name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html#capturedEnd

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QRegularExpressionMatch::capturedEnd(QAnyStringView name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QRegularExpressionMatch11capturedEndE14QAnyStringView',
        name,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionMatch::QRegularExpressionMatch()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html
    """
    #  QRegularExpressionMatch::QRegularExpressionMatch()
    self._noteCreation(QRegularExpressionMatch, lambda: Rituals.call(
        'ritual_ZN23QRegularExpressionMatchC1Ev',
    ))

  @overload(THIS)
  def __init__(self, match: QRegularExpressionMatch) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionMatch::QRegularExpressionMatch(const
    QRegularExpressionMatch &match)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatch.html

    Parameters
    ----------

    match : QRegularExpressionMatch
      Passed on as a value: Qt reads the C++ QRegularExpressionMatch, which
      stays Python's own.
    """
    #  QRegularExpressionMatch::QRegularExpressionMatch(const
    #      QRegularExpressionMatch &match)
    self._noteCreation(QRegularExpressionMatch, lambda: Rituals.call(
        'ritual_ZN23QRegularExpressionMatchC1ERKS_', self._valueOf(match),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QRegularExpressionMatch::swap(QRegularExpressionMatch
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRegularExpressionMatch.swap' has no cute function yet. Qt's "
        "'void QRegularExpressionMatch::swap(QRegularExpressionMatch "
        "&other)': takes a type Python has no way to hand over yet.")
