"""
QChar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_char_category import Category
from ._q_char_combining_class import CombiningClass
from ._q_char_decomposition import Decomposition
from ._q_char_direction import Direction
from ._q_char_joining_type import JoiningType
from ._q_char_script import Script
from ._q_char_special_character import SpecialCharacter
from ._q_char_unicode_version import UnicodeVersion


class QChar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QChar: a plain Python object standing in front of one
  C++ QChar.

  C++ hands a QChar around as a copy, so every C++ QChar behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QChar that has a ritual and that Python can call so
  far, 37 names in all: 'category', 'direction', 'joiningType',
  'combiningClass', 'mirroredChar', 'hasMirrored', 'decomposition',
  'decompositionTag', 'digitValue', 'toLower', 'toUpper', 'toTitleCase',
  'toCaseFolded', 'script', 'unicodeVersion', 'isNull', 'isPrint', 'isSpace',
  'isMark', 'isPunct', 'isSymbol', 'isLetter', 'isNumber',
  'isLetterOrNumber', 'isDigit', 'isLower', 'isUpper', 'isTitleCase',
  'isNonCharacter', 'isHighSurrogate', 'isLowSurrogate', 'isSurrogate',
  'cell', 'row', 'setCell', 'setRow', 'currentUnicodeVersion'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char QChar::toLatin1() const': gives a single letter as C has it.
  - Qt's 'QChar QChar::fromLatin1(char c)': takes a single letter as C has
    it.
  - Qt's 'QChar::~QChar()': the destructor: Python removes its C++ QChar by
    it, and has no other use for it.

  What has no ritual
  ------------------

  50 of the 92 functions Qt declares: 40 takes or gives a type that cannot be
  passed yet; 6 private; 4 a template.

  What to expect
  --------------

  - The C++ QChar is created at the first use, not by 'QChar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QChar back gives a copy the ritual made for Python,
    in a new cute QChar.
  """

  #  The enums Qt writes inside QChar, and the names Qt has for the
  #  combinations of its flags enums.
  Category = Category
  CombiningClass = CombiningClass
  Decomposition = Decomposition
  Direction = Direction
  JoiningType = JoiningType
  Script = Script
  SpecialCharacter = SpecialCharacter
  UnicodeVersion = UnicodeVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def currentUnicodeVersion() -> UnicodeVersion:
    """
    Calls Qt's 'UnicodeVersion QChar::currentUnicodeVersion()'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#currentUnicodeVersion

    Returns
    -------

    UnicodeVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UnicodeVersion(number)'
      gives.
    """
    #  UnicodeVersion QChar::currentUnicodeVersion()
    return UnicodeVersion(Rituals.call(
        'ritual_ZN5QChar21currentUnicodeVersionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChar'

  #  Qt's '~QChar()'. Naming it makes this a value class: Python owns every
  #  C++ QChar behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QCharD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def category(self) -> Category:
    """
    Calls Qt's 'Category QChar::category() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#category

    Returns
    -------

    Category
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Category(number)' gives.
    """
    #  Category QChar::category() const
    return Category(self.uglySide.call('ritual_ZNK5QChar8categoryEv'))

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QChar::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QChar::direction() const
    return Direction(self.uglySide.call('ritual_ZNK5QChar9directionEv'))

  def joiningType(self) -> JoiningType:
    """
    Calls Qt's 'JoiningType QChar::joiningType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#joiningType

    Returns
    -------

    JoiningType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'JoiningType(number)'
      gives.
    """
    #  JoiningType QChar::joiningType() const
    return JoiningType(self.uglySide.call('ritual_ZNK5QChar11joiningTypeEv'))

  def combiningClass(self) -> int:
    """
    Calls Qt's 'unsigned char QChar::combiningClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#combiningClass
    """
    #  unsigned char QChar::combiningClass() const
    return self.uglySide.call('ritual_ZNK5QChar14combiningClassEv')

  def mirroredChar(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::mirroredChar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#mirroredChar

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::mirroredChar() const
    address = self.uglySide.call('ritual_ZNK5QChar12mirroredCharEv')
    return QChar._cuteOwning(address)

  def hasMirrored(self) -> bool:
    """
    Calls Qt's 'bool QChar::hasMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#hasMirrored
    """
    #  bool QChar::hasMirrored() const
    return self.uglySide.call('ritual_ZNK5QChar11hasMirroredEv')

  def decomposition(self) -> str:
    """
    Calls Qt's 'QString QChar::decomposition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#decomposition

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QChar::decomposition() const
    return self.uglySide.call('ritual_ZNK5QChar13decompositionEv')

  def decompositionTag(self) -> Decomposition:
    """
    Calls Qt's 'Decomposition QChar::decompositionTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#decompositionTag

    Returns
    -------

    Decomposition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Decomposition(number)'
      gives.
    """
    #  Decomposition QChar::decompositionTag() const
    return Decomposition(self.uglySide.call(
        'ritual_ZNK5QChar16decompositionTagEv',
    ))

  def digitValue(self) -> int:
    """
    Calls Qt's 'int QChar::digitValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#digitValue
    """
    #  int QChar::digitValue() const
    return self.uglySide.call('ritual_ZNK5QChar10digitValueEv')

  def toLower(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toLower

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toLower() const
    address = self.uglySide.call('ritual_ZNK5QChar7toLowerEv')
    return QChar._cuteOwning(address)

  def toUpper(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toUpper

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toUpper() const
    address = self.uglySide.call('ritual_ZNK5QChar7toUpperEv')
    return QChar._cuteOwning(address)

  def toTitleCase(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toTitleCase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toTitleCase

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toTitleCase() const
    address = self.uglySide.call('ritual_ZNK5QChar11toTitleCaseEv')
    return QChar._cuteOwning(address)

  def toCaseFolded(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toCaseFolded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toCaseFolded

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toCaseFolded() const
    address = self.uglySide.call('ritual_ZNK5QChar12toCaseFoldedEv')
    return QChar._cuteOwning(address)

  def script(self) -> Script:
    """
    Calls Qt's 'Script QChar::script() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#script

    Returns
    -------

    Script
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Script(number)' gives.
    """
    #  Script QChar::script() const
    return Script(self.uglySide.call('ritual_ZNK5QChar6scriptEv'))

  def unicodeVersion(self) -> UnicodeVersion:
    """
    Calls Qt's 'UnicodeVersion QChar::unicodeVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#unicodeVersion

    Returns
    -------

    UnicodeVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UnicodeVersion(number)'
      gives.
    """
    #  UnicodeVersion QChar::unicodeVersion() const
    return UnicodeVersion(self.uglySide.call(
        'ritual_ZNK5QChar14unicodeVersionEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNull
    """
    #  bool QChar::isNull() const
    return self.uglySide.call('ritual_ZNK5QChar6isNullEv')

  def isPrint(self) -> bool:
    """
    Calls Qt's 'bool QChar::isPrint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isPrint
    """
    #  bool QChar::isPrint() const
    return self.uglySide.call('ritual_ZNK5QChar7isPrintEv')

  def isSpace(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSpace
    """
    #  bool QChar::isSpace() const
    return self.uglySide.call('ritual_ZNK5QChar7isSpaceEv')

  def isMark(self) -> bool:
    """
    Calls Qt's 'bool QChar::isMark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isMark
    """
    #  bool QChar::isMark() const
    return self.uglySide.call('ritual_ZNK5QChar6isMarkEv')

  def isPunct(self) -> bool:
    """
    Calls Qt's 'bool QChar::isPunct() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isPunct
    """
    #  bool QChar::isPunct() const
    return self.uglySide.call('ritual_ZNK5QChar7isPunctEv')

  def isSymbol(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSymbol
    """
    #  bool QChar::isSymbol() const
    return self.uglySide.call('ritual_ZNK5QChar8isSymbolEv')

  def isLetter(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLetter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLetter
    """
    #  bool QChar::isLetter() const
    return self.uglySide.call('ritual_ZNK5QChar8isLetterEv')

  def isNumber(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNumber
    """
    #  bool QChar::isNumber() const
    return self.uglySide.call('ritual_ZNK5QChar8isNumberEv')

  def isLetterOrNumber(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLetterOrNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLetterOrNumber
    """
    #  bool QChar::isLetterOrNumber() const
    return self.uglySide.call('ritual_ZNK5QChar16isLetterOrNumberEv')

  def isDigit(self) -> bool:
    """
    Calls Qt's 'bool QChar::isDigit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isDigit
    """
    #  bool QChar::isDigit() const
    return self.uglySide.call('ritual_ZNK5QChar7isDigitEv')

  def isLower(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLower
    """
    #  bool QChar::isLower() const
    return self.uglySide.call('ritual_ZNK5QChar7isLowerEv')

  def isUpper(self) -> bool:
    """
    Calls Qt's 'bool QChar::isUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isUpper
    """
    #  bool QChar::isUpper() const
    return self.uglySide.call('ritual_ZNK5QChar7isUpperEv')

  def isTitleCase(self) -> bool:
    """
    Calls Qt's 'bool QChar::isTitleCase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isTitleCase
    """
    #  bool QChar::isTitleCase() const
    return self.uglySide.call('ritual_ZNK5QChar11isTitleCaseEv')

  def isNonCharacter(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNonCharacter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNonCharacter
    """
    #  bool QChar::isNonCharacter() const
    return self.uglySide.call('ritual_ZNK5QChar14isNonCharacterEv')

  def isHighSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isHighSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isHighSurrogate
    """
    #  bool QChar::isHighSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar15isHighSurrogateEv')

  def isLowSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLowSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLowSurrogate
    """
    #  bool QChar::isLowSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar14isLowSurrogateEv')

  def isSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSurrogate
    """
    #  bool QChar::isSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar11isSurrogateEv')

  def cell(self) -> int:
    """
    Calls Qt's 'uchar QChar::cell() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#cell
    """
    #  uchar QChar::cell() const
    return self.uglySide.call('ritual_ZNK5QChar4cellEv')

  def row(self) -> int:
    """
    Calls Qt's 'uchar QChar::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#row
    """
    #  uchar QChar::row() const
    return self.uglySide.call('ritual_ZNK5QChar3rowEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCell(self, acell: int) -> None:
    """
    Calls Qt's 'void QChar::setCell(uchar acell)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#setCell

    Parameters
    ----------

    acell : int
      Passed on as it is.
    """
    #  void QChar::setCell(uchar acell)
    self.uglySide.call('ritual_ZN5QChar7setCellEh', acell)

  @overload(int)
  def setRow(self, arow: int) -> None:
    """
    Calls Qt's 'void QChar::setRow(uchar arow)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#setRow

    Parameters
    ----------

    arow : int
      Passed on as it is.
    """
    #  void QChar::setRow(uchar arow)
    self.uglySide.call('ritual_ZN5QChar6setRowEh', arow)

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
    Notes what was given, for Qt's 'QChar::QChar()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#QChar
    """
    #  QChar::QChar()
    self._noteCreation(QChar, lambda: Rituals.call('ritual_ZN5QCharC1Ev'))

  @overload(int, int)
  def __init__(self, c: int, r: int) -> None:
    """
    Notes what was given, for Qt's 'QChar::QChar(uchar c, uchar r)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#QChar

    Parameters
    ----------

    c : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  QChar::QChar(uchar c, uchar r)
    self._noteCreation(QChar, lambda: Rituals.call(
        'ritual_ZN5QCharC1Ehh', c, r,
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
