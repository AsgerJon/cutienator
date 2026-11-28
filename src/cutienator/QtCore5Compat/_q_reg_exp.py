"""
QRegExp binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qregexp.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import Qt, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRegExp(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRegExp: a plain Python object standing in front of
  one C++ QRegExp.

  C++ hands a QRegExp around as a copy, so every C++ QRegExp behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRegExp that has a ritual and that Python can call
  so far, 28 names in all: '__eq__', '__ne__', 'isEmpty', 'isValid',
  'pattern', 'setPattern', 'caseSensitivity', 'setCaseSensitivity',
  'patternSyntax', 'setPatternSyntax', 'isMinimal', 'setMinimal',
  'exactMatch', 'indexIn', 'lastIndexIn', 'matchedLength', 'captureCount',
  'capturedTexts', 'cap', 'pos', 'errorString', 'replaceIn', 'removeIn',
  'containedIn', 'countIn', 'splitString', 'filterList', 'escape'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRegExp::~QRegExp()': the destructor: Python removes its C++
    QRegExp by it, and has no other use for it.
  - Qt's 'QRegExp &QRegExp::operator=(const QRegExp &rx)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QRegExp &QRegExp::operator=(QRegExp &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'void QRegExp::swap(QRegExp &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QVariant QRegExp::operator QVariant() const': an operator Python
    has no name for.
  - Qt's 'QStringList QRegExp::capturedTexts()': takes in Python what
    'QStringList QRegExp::capturedTexts() const' takes.
  - Qt's 'QString QRegExp::cap(int nth)': takes in Python what 'QString
    QRegExp::cap(int nth) const' takes.
  - Qt's 'int QRegExp::pos(int nth)': takes in Python what 'int
    QRegExp::pos(int nth) const' takes.
  - Qt's 'QString QRegExp::errorString()': takes in Python what 'QString
    QRegExp::errorString() const' takes.

  What to expect
  --------------

  - The C++ QRegExp is created at the first use, not by 'QRegExp(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRegExp back gives a copy the ritual made for Python,
    in a new cute QRegExp.
  - Each name of Qt's QRegExp that has no cute function yet, 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRegExp, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class CaretMode(CuteNum):
    """
    The enum 'QRegExp::CaretMode' of Qt, with the 3 names Qt gives in it.
    """

    CaretAtZero = Kee[int](0)
    CaretAtOffset = Kee[int](1)
    CaretWontMatch = Kee[int](2)

  class PatternSyntax(CuteNum):
    """
    The enum 'QRegExp::PatternSyntax' of Qt, with the 6 names Qt gives in it.
    """

    RegExp = Kee[int](0)
    Wildcard = Kee[int](1)
    FixedString = Kee[int](2)
    RegExp2 = Kee[int](3)
    WildcardUnix = Kee[int](4)
    W3CXmlSchema11 = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def escape(str: str) -> str:
    """
    Calls Qt's 'QString QRegExp::escape(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#escape

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::escape(const QString &str)
    return Rituals.call('ritual_ZN7QRegExp6escapeERK7QString', str)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegExp'

  #  Qt's '~QRegExp()'. Naming it makes this a value class: Python owns every
  #  C++ QRegExp behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QRegExpD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRegExp::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#isEmpty
    """
    #  bool QRegExp::isEmpty() const
    return self.uglySide.call('ritual_ZNK7QRegExp7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRegExp::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#isValid
    """
    #  bool QRegExp::isValid() const
    return self.uglySide.call('ritual_ZNK7QRegExp7isValidEv')

  def pattern(self) -> str:
    """
    Calls Qt's 'QString QRegExp::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#pattern

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::pattern() const
    return self.uglySide.call('ritual_ZNK7QRegExp7patternEv')

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QRegExp::caseSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QRegExp::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK7QRegExp15caseSensitivityEv',
    ))

  def patternSyntax(self) -> PatternSyntax:
    """
    Calls Qt's 'PatternSyntax QRegExp::patternSyntax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#patternSyntax

    Returns
    -------

    PatternSyntax
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PatternSyntax(number)'
      gives.
    """
    #  PatternSyntax QRegExp::patternSyntax() const
    return QRegExp.PatternSyntax(self.uglySide.call(
        'ritual_ZNK7QRegExp13patternSyntaxEv',
    ))

  def isMinimal(self) -> bool:
    """
    Calls Qt's 'bool QRegExp::isMinimal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#isMinimal
    """
    #  bool QRegExp::isMinimal() const
    return self.uglySide.call('ritual_ZNK7QRegExp9isMinimalEv')

  @overload(str)
  def exactMatch(self, str: str) -> bool:
    """
    Calls Qt's 'bool QRegExp::exactMatch(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#exactMatch

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QRegExp::exactMatch(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp10exactMatchERK7QString', str,
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, CaretMode)
  def indexIn(
      self,
      str: str,
      offset: int = 0,
      caretMode: CaretMode = CaretMode.CaretAtZero,
  ) -> int:
    """
    Calls Qt's 'int QRegExp::indexIn(const QString &str, int offset,
    CaretMode caretMode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#indexIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    caretMode : CaretMode
      Passed on as its number. May be left out, as in Qt: it is then
      CaretMode.CaretAtZero.
    """
    #  int QRegExp::indexIn(const QString &str, int offset, CaretMode
    #      caretMode) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp7indexInERK7QStringiNS_9CaretModeE',
        str, offset, caretMode.value,
    )

  @overload(QStringList, int)
  def indexIn(self, list: QStringList, from_: int) -> int:
    """
    Calls Qt's 'int QRegExp::indexIn(const QStringList &list, int from)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#indexIn

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    from_ : int
      Passed on as it is.
    """
    #  int QRegExp::indexIn(const QStringList &list, int from) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp7indexInERK5QListI7QStringEi',
        self._valueOf(list), from_,
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, CaretMode)
  def lastIndexIn(
      self,
      str: str,
      offset: int = -1,
      caretMode: CaretMode = CaretMode.CaretAtZero,
  ) -> int:
    """
    Calls Qt's 'int QRegExp::lastIndexIn(const QString &str, int offset,
    CaretMode caretMode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#lastIndexIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    caretMode : CaretMode
      Passed on as its number. May be left out, as in Qt: it is then
      CaretMode.CaretAtZero.
    """
    #  int QRegExp::lastIndexIn(const QString &str, int offset, CaretMode
    #      caretMode) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp11lastIndexInERK7QStringiNS_9CaretModeE',
        str, offset, caretMode.value,
    )

  @overload(QStringList, int)
  def lastIndexIn(self, list: QStringList, from_: int) -> int:
    """
    Calls Qt's 'int QRegExp::lastIndexIn(const QStringList &list, int from)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#lastIndexIn

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    from_ : int
      Passed on as it is.
    """
    #  int QRegExp::lastIndexIn(const QStringList &list, int from) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp11lastIndexInERK5QListI7QStringEi',
        self._valueOf(list), from_,
    )

  def matchedLength(self) -> int:
    """
    Calls Qt's 'int QRegExp::matchedLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#matchedLength
    """
    #  int QRegExp::matchedLength() const
    return self.uglySide.call('ritual_ZNK7QRegExp13matchedLengthEv')

  def captureCount(self) -> int:
    """
    Calls Qt's 'int QRegExp::captureCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#captureCount
    """
    #  int QRegExp::captureCount() const
    return self.uglySide.call('ritual_ZNK7QRegExp12captureCountEv')

  def capturedTexts(self) -> QStringList:
    """
    Calls Qt's 'QStringList QRegExp::capturedTexts() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#capturedTexts

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRegExp::capturedTexts() const
    address = self.uglySide.call('ritual_ZNK7QRegExp13capturedTextsEv')
    return QStringList._cuteOwning(address)

  @overload()
  @overload(int)
  def cap(self, nth: int = 0) -> str:
    """
    Calls Qt's 'QString QRegExp::cap(int nth) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#cap

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::cap(int nth) const
    return self.uglySide.call('ritual_ZNK7QRegExp3capEi', nth)

  @overload()
  @overload(int)
  def pos(self, nth: int = 0) -> int:
    """
    Calls Qt's 'int QRegExp::pos(int nth) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#pos

    Parameters
    ----------

    nth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QRegExp::pos(int nth) const
    return self.uglySide.call('ritual_ZNK7QRegExp3posEi', nth)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QRegExp::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::errorString() const
    return self.uglySide.call('ritual_ZNK7QRegExp11errorStringEv')

  @overload(str, str)
  def replaceIn(self, str: str, after: str) -> str:
    """
    Calls Qt's 'QString QRegExp::replaceIn(const QString &str, const QString
    &after) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#replaceIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    after : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::replaceIn(const QString &str, const QString &after)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp9replaceInERK7QStringS2_', str, after,
    )

  @overload(QStringList, str)
  def replaceIn(self, stringList: QStringList, after: str) -> QStringList:
    """
    Calls Qt's 'QStringList QRegExp::replaceIn(const QStringList &stringList,
    const QString &after) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#replaceIn

    Parameters
    ----------

    stringList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    after : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRegExp::replaceIn(const QStringList &stringList, const
    #      QString &after) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegExp9replaceInERK5QListI7QStringERKS1_',
        self._valueOf(stringList), after,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def removeIn(self, str: str) -> str:
    """
    Calls Qt's 'QString QRegExp::removeIn(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#removeIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRegExp::removeIn(const QString &str) const
    return self.uglySide.call('ritual_ZNK7QRegExp8removeInERK7QString', str)

  @overload(str)
  def containedIn(self, str: str) -> bool:
    """
    Calls Qt's 'bool QRegExp::containedIn(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#containedIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QRegExp::containedIn(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK7QRegExp11containedInERK7QString', str,
    )

  @overload(str)
  def countIn(self, str: str) -> int:
    """
    Calls Qt's 'int QRegExp::countIn(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#countIn

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QRegExp::countIn(const QString &str) const
    return self.uglySide.call('ritual_ZNK7QRegExp7countInERK7QString', str)

  @overload(str)
  @overload(str, Qt.SplitBehavior)
  def splitString(
      self,
      str: str,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QRegExp::splitString(const QString &str,
    Qt::SplitBehavior behavior) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#splitString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRegExp::splitString(const QString &str, Qt::SplitBehavior
    #      behavior) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegExp11splitStringERK7QString6QFlagsIN2Qt18SplitBehav'
        'iorFlagsEE',
        str, behavior.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QStringList)
  def filterList(self, stringList: QStringList) -> QStringList:
    """
    Calls Qt's 'QStringList QRegExp::filterList(const QStringList
    &stringList) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#filterList

    Parameters
    ----------

    stringList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRegExp::filterList(const QStringList &stringList) const
    address = self.uglySide.call(
        'ritual_ZNK7QRegExp10filterListERK5QListI7QStringE',
        self._valueOf(stringList),
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPattern(self, pattern: str) -> None:
    """
    Calls Qt's 'void QRegExp::setPattern(const QString &pattern)'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#setPattern

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRegExp::setPattern(const QString &pattern)
    self.uglySide.call('ritual_ZN7QRegExp10setPatternERK7QString', pattern)

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void QRegExp::setCaseSensitivity(Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#setCaseSensitivity

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QRegExp::setCaseSensitivity(Qt::CaseSensitivity cs)
    self.uglySide.call(
        'ritual_ZN7QRegExp18setCaseSensitivityEN2Qt15CaseSensitivityE',
        cs.value,
    )

  @overload(PatternSyntax)
  def setPatternSyntax(self, syntax: PatternSyntax) -> None:
    """
    Calls Qt's 'void QRegExp::setPatternSyntax(PatternSyntax syntax)'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#setPatternSyntax

    Parameters
    ----------

    syntax : PatternSyntax
      Passed on as its number.
    """
    #  void QRegExp::setPatternSyntax(PatternSyntax syntax)
    self.uglySide.call(
        'ritual_ZN7QRegExp16setPatternSyntaxENS_13PatternSyntaxE',
        syntax.value,
    )

  @overload(bool)
  def setMinimal(self, minimal: bool) -> None:
    """
    Calls Qt's 'void QRegExp::setMinimal(bool minimal)'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#setMinimal

    Parameters
    ----------

    minimal : bool
      Passed on as it is.
    """
    #  void QRegExp::setMinimal(bool minimal)
    self.uglySide.call('ritual_ZN7QRegExp10setMinimalEb', minimal)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rx: QRegExp) -> bool:
    """
    Calls Qt's 'bool QRegExp::operator==(const QRegExp &rx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#operator==

    Parameters
    ----------

    rx : QRegExp
      Passed on as a value: Qt reads the C++ QRegExp, which stays Python's
      own.
    """
    #  bool QRegExp::operator==(const QRegExp &rx) const
    return self.uglySide.call('ritual_ZNK7QRegExpeqERKS_', self._valueOf(rx))

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rx: QRegExp) -> bool:
    """
    Calls Qt's 'bool QRegExp::operator!=(const QRegExp &rx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#operator!=

    Parameters
    ----------

    rx : QRegExp
      Passed on as a value: Qt reads the C++ QRegExp, which stays Python's
      own.
    """
    #  bool QRegExp::operator!=(const QRegExp &rx) const
    return self.uglySide.call('ritual_ZNK7QRegExpneERKS_', self._valueOf(rx))

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
    Notes what was given, for Qt's 'QRegExp::QRegExp()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#QRegExp
    """
    #  QRegExp::QRegExp()
    self._noteCreation(QRegExp, lambda: Rituals.call(
        'ritual_ZN7QRegExpC1Ev',
    ))

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  @overload(str, Qt.CaseSensitivity, PatternSyntax)
  def __init__(
      self,
      pattern: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
      syntax: PatternSyntax = PatternSyntax.RegExp,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRegExp::QRegExp(const QString &pattern,
    Qt::CaseSensitivity cs, PatternSyntax syntax)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#QRegExp

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.

    syntax : PatternSyntax
      Passed on as its number. May be left out, as in Qt: it is then
      PatternSyntax.RegExp.
    """
    #  QRegExp::QRegExp(const QString &pattern, Qt::CaseSensitivity cs,
    #      PatternSyntax syntax)
    self._noteCreation(QRegExp, lambda: Rituals.call(
        'ritual_ZN7QRegExpC1ERK7QStringN2Qt15CaseSensitivityENS_13PatternSy'
        'ntaxE',
        pattern, cs.value, syntax.value,
    ))

  @overload(THIS)
  def __init__(self, rx: QRegExp) -> None:
    """
    Notes what was given, for Qt's 'QRegExp::QRegExp(const QRegExp &rx)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qregexp.html#QRegExp

    Parameters
    ----------

    rx : QRegExp
      Passed on as a value: Qt reads the C++ QRegExp, which stays Python's
      own.
    """
    #  QRegExp::QRegExp(const QRegExp &rx)
    self._noteCreation(QRegExp, lambda: Rituals.call(
        'ritual_ZN7QRegExpC1ERKS_', self._valueOf(rx),
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
    Qt's 'void QRegExp::swap(QRegExp &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QRegExp.swap' has no cute function yet. Qt's 'void "
        "QRegExp::swap(QRegExp &other)': takes a type Python has no way to "
        "hand over yet.")
