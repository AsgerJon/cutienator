"""
QTextLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from . import QFont, QPaintDevice, QPainter, QRawFont, QTextBlock
  from . import QTextLine, QTextOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPaintDevice = WAIT['QPaintDevice']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRawFont = WAIT['QRawFont']
  QTextBlock = WAIT['QTextBlock']
  QTextOption = WAIT['QTextOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextLayout: a plain Python object standing in front
  of one C++ QTextLayout.

  What exists
  -----------

  Every function of Qt's QTextLayout that has a ritual and that Python can
  call so far, 34 names in all: 'setFont', 'font', 'setRawFont', 'setText',
  'text', 'setTextOption', 'textOption', 'setPreeditArea',
  'preeditAreaPosition', 'preeditAreaText', 'clearFormats',
  'setCacheEnabled', 'cacheEnabled', 'setCursorMoveStyle', 'cursorMoveStyle',
  'beginLayout', 'endLayout', 'clearLayout', 'createLine', 'lineCount',
  'lineAt', 'lineForTextPosition', 'isValidCursorPosition',
  'nextCursorPosition', 'previousCursorPosition', 'leftCursorPosition',
  'rightCursorPosition', 'drawCursor', 'position', 'setPosition',
  'boundingRect', 'minimumWidth', 'maximumWidth', 'setFlags'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextLayout::~QTextLayout()': the destructor: Python never removes
    a C++ QTextLayout.

  What has no ritual
  ------------------

  9 of the 49 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 private.

  What to expect
  --------------

  - The C++ QTextLayout is created at the first use, not by
    'QTextLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextLayout.
  """

  #  The enums Qt writes inside QTextLayout, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CursorMode(CuteNum):
    """
    The enum 'QTextLayout::CursorMode' of Qt, with the 2 names Qt gives in
    it.
    """

    SkipCharacters = Kee[int](0)
    SkipWords = Kee[int](1)

  class GlyphRunRetrievalFlag(CuteFlags, number='unsigned short'):
    """
    The flags enum 'QTextLayout::GlyphRunRetrievalFlag' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QTextLayout::GlyphRunRetrievalFlags'.
    """

    RetrieveGlyphIndexes = 0x1
    RetrieveGlyphPositions = 0x2
    RetrieveStringIndexes = 0x4
    RetrieveString = 0x8
    DefaultRetrievalFlags = 0x3
    RetrieveAll = 0xffff

  GlyphRunRetrievalFlags = GlyphRunRetrievalFlag

  #  The classes Qt writes inside QTextLayout, each a class in here as in
  #  C++.

  class FormatRange(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextLayout::FormatRange: a plain Python object
    standing in front of one C++ QTextLayout::FormatRange.

    C++ hands a QTextLayout::FormatRange around as a copy, so every C++
    QTextLayout::FormatRange behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QTextLayout::FormatRange yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextLayout::FormatRange::~FormatRange()': the destructor: Python
      removes its C++ QTextLayout::FormatRange by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QTextLayout::FormatRange is created at the first use, not by
      'QTextLayout::FormatRange(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextLayout::FormatRange back gives a copy the
      ritual made for Python, in a new cute QTextLayout::FormatRange.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextLayout::FormatRange'

    #  Qt's '~QTextLayout::FormatRange()'. Naming it makes this a value
    #  class: Python owns every C++ QTextLayout::FormatRange behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QTextLayout11FormatRangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QTextLayout::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextLayout::font() const
    address = self.uglySide.call('ritual_ZNK11QTextLayout4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QTextLayout::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextLayout::text() const
    return self.uglySide.call('ritual_ZNK11QTextLayout4textEv')

  def textOption(self) -> QTextOption:
    """
    Calls Qt's 'const QTextOption &QTextLayout::textOption() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#textOption

    Returns
    -------

    QTextOption
      A new cute QTextOption around the copy Qt gave back. Python owns it.
    """
    #  const QTextOption &QTextLayout::textOption() const
    address = self.uglySide.call('ritual_ZNK11QTextLayout10textOptionEv')
    from . import QTextOption
    return QTextOption._cuteOwning(address)

  def preeditAreaPosition(self) -> int:
    """
    Calls Qt's 'int QTextLayout::preeditAreaPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#preeditAreaPosition
    """
    #  int QTextLayout::preeditAreaPosition() const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout19preeditAreaPositionEv',
    )

  def preeditAreaText(self) -> str:
    """
    Calls Qt's 'QString QTextLayout::preeditAreaText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#preeditAreaText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextLayout::preeditAreaText() const
    return self.uglySide.call('ritual_ZNK11QTextLayout15preeditAreaTextEv')

  def cacheEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTextLayout::cacheEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#cacheEnabled
    """
    #  bool QTextLayout::cacheEnabled() const
    return self.uglySide.call('ritual_ZNK11QTextLayout12cacheEnabledEv')

  def cursorMoveStyle(self) -> Qt.CursorMoveStyle:
    """
    Calls Qt's 'Qt::CursorMoveStyle QTextLayout::cursorMoveStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#cursorMoveStyle

    Returns
    -------

    Qt.CursorMoveStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CursorMoveStyle(number)' gives.
    """
    #  Qt::CursorMoveStyle QTextLayout::cursorMoveStyle() const
    return Qt.CursorMoveStyle(self.uglySide.call(
        'ritual_ZNK11QTextLayout15cursorMoveStyleEv',
    ))

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QTextLayout::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#lineCount
    """
    #  int QTextLayout::lineCount() const
    return self.uglySide.call('ritual_ZNK11QTextLayout9lineCountEv')

  @overload(int)
  def lineAt(self, i: int) -> QTextLine:
    """
    Calls Qt's 'QTextLine QTextLayout::lineAt(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#lineAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QTextLine
      A new cute QTextLine around the copy Qt gave back. Python owns it.
    """
    #  QTextLine QTextLayout::lineAt(int i) const
    address = self.uglySide.call('ritual_ZNK11QTextLayout6lineAtEi', i)
    from . import QTextLine
    return QTextLine._cuteOwning(address)

  @overload(int)
  def lineForTextPosition(self, pos: int) -> QTextLine:
    """
    Calls Qt's 'QTextLine QTextLayout::lineForTextPosition(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#lineForTextPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextLine
      A new cute QTextLine around the copy Qt gave back. Python owns it.
    """
    #  QTextLine QTextLayout::lineForTextPosition(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextLayout19lineForTextPositionEi', pos,
    )
    from . import QTextLine
    return QTextLine._cuteOwning(address)

  @overload(int)
  def isValidCursorPosition(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QTextLayout::isValidCursorPosition(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#isValidCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QTextLayout::isValidCursorPosition(int pos) const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout21isValidCursorPositionEi', pos,
    )

  @overload(int)
  @overload(int, CursorMode)
  def nextCursorPosition(
      self,
      oldPos: int,
      mode: CursorMode = CursorMode.SkipCharacters,
  ) -> int:
    """
    Calls Qt's 'int QTextLayout::nextCursorPosition(int oldPos, CursorMode
    mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#nextCursorPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.

    mode : CursorMode
      Passed on as its number. May be left out, as in Qt: it is then
      CursorMode.SkipCharacters.
    """
    #  int QTextLayout::nextCursorPosition(int oldPos, CursorMode mode) const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout18nextCursorPositionEiNS_10CursorModeE',
        oldPos, mode.value,
    )

  @overload(int)
  @overload(int, CursorMode)
  def previousCursorPosition(
      self,
      oldPos: int,
      mode: CursorMode = CursorMode.SkipCharacters,
  ) -> int:
    """
    Calls Qt's 'int QTextLayout::previousCursorPosition(int oldPos,
    CursorMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#previousCursorPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.

    mode : CursorMode
      Passed on as its number. May be left out, as in Qt: it is then
      CursorMode.SkipCharacters.
    """
    #  int QTextLayout::previousCursorPosition(int oldPos, CursorMode mode)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout22previousCursorPositionEiNS_10CursorModeE',
        oldPos, mode.value,
    )

  @overload(int)
  def leftCursorPosition(self, oldPos: int) -> int:
    """
    Calls Qt's 'int QTextLayout::leftCursorPosition(int oldPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#leftCursorPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.
    """
    #  int QTextLayout::leftCursorPosition(int oldPos) const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout18leftCursorPositionEi', oldPos,
    )

  @overload(int)
  def rightCursorPosition(self, oldPos: int) -> int:
    """
    Calls Qt's 'int QTextLayout::rightCursorPosition(int oldPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#rightCursorPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.
    """
    #  int QTextLayout::rightCursorPosition(int oldPos) const
    return self.uglySide.call(
        'ritual_ZNK11QTextLayout19rightCursorPositionEi', oldPos,
    )

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QTextLayout::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTextLayout::position() const
    address = self.uglySide.call('ritual_ZNK11QTextLayout8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QTextLayout::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextLayout::boundingRect() const
    address = self.uglySide.call('ritual_ZNK11QTextLayout12boundingRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def minimumWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextLayout::minimumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#minimumWidth
    """
    #  qreal QTextLayout::minimumWidth() const
    return self.uglySide.call('ritual_ZNK11QTextLayout12minimumWidthEv')

  def maximumWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextLayout::maximumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#maximumWidth
    """
    #  qreal QTextLayout::maximumWidth() const
    return self.uglySide.call('ritual_ZNK11QTextLayout12maximumWidthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QTextLayout::setFont(const QFont &f)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTextLayout::setFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN11QTextLayout7setFontERK5QFont', self._valueOf(f),
    )

  @overload(QRawFont)
  def setRawFont(self, rawFont: QRawFont) -> None:
    """
    Calls Qt's 'void QTextLayout::setRawFont(const QRawFont &rawFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setRawFont

    Parameters
    ----------

    rawFont : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  void QTextLayout::setRawFont(const QRawFont &rawFont)
    self.uglySide.call(
        'ritual_ZN11QTextLayout10setRawFontERK8QRawFont',
        self._valueOf(rawFont),
    )

  @overload(str)
  def setText(self, string: str) -> None:
    """
    Calls Qt's 'void QTextLayout::setText(const QString &string)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setText

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextLayout::setText(const QString &string)
    self.uglySide.call('ritual_ZN11QTextLayout7setTextERK7QString', string)

  @overload(QTextOption)
  def setTextOption(self, option: QTextOption) -> None:
    """
    Calls Qt's 'void QTextLayout::setTextOption(const QTextOption &option)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setTextOption

    Parameters
    ----------

    option : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  void QTextLayout::setTextOption(const QTextOption &option)
    self.uglySide.call(
        'ritual_ZN11QTextLayout13setTextOptionERK11QTextOption',
        self._valueOf(option),
    )

  @overload(int, str)
  def setPreeditArea(self, position: int, text: str) -> None:
    """
    Calls Qt's 'void QTextLayout::setPreeditArea(int position, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setPreeditArea

    Parameters
    ----------

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextLayout::setPreeditArea(int position, const QString &text)
    self.uglySide.call(
        'ritual_ZN11QTextLayout14setPreeditAreaEiRK7QString', position, text,
    )

  @overload(bool)
  def setCacheEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTextLayout::setCacheEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setCacheEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTextLayout::setCacheEnabled(bool enable)
    self.uglySide.call('ritual_ZN11QTextLayout15setCacheEnabledEb', enable)

  @overload(Qt.CursorMoveStyle)
  def setCursorMoveStyle(self, style: Qt.CursorMoveStyle) -> None:
    """
    Calls Qt's 'void QTextLayout::setCursorMoveStyle(Qt::CursorMoveStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlayout.html#setCursorMoveStyle

    Parameters
    ----------

    style : Qt.CursorMoveStyle
      Passed on as its number.
    """
    #  void QTextLayout::setCursorMoveStyle(Qt::CursorMoveStyle style)
    self.uglySide.call(
        'ritual_ZN11QTextLayout18setCursorMoveStyleEN2Qt15CursorMoveStyleE',
        style.value,
    )

  @overload(QPointF)
  def setPosition(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QTextLayout::setPosition(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setPosition

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QTextLayout::setPosition(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN11QTextLayout11setPositionERK7QPointF', self._valueOf(p),
    )

  @overload(int)
  def setFlags(self, flags: int) -> None:
    """
    Calls Qt's 'void QTextLayout::setFlags(int flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#setFlags

    Parameters
    ----------

    flags : int
      Passed on as it is.
    """
    #  void QTextLayout::setFlags(int flags)
    self.uglySide.call('ritual_ZN11QTextLayout8setFlagsEi', flags)

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
    Notes what was given, for Qt's 'QTextLayout::QTextLayout()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#QTextLayout
    """
    #  QTextLayout::QTextLayout()
    self._noteCreation(QTextLayout, lambda: Rituals.call(
        'ritual_ZN11QTextLayoutC1Ev',
    ))

  @overload(str)
  def __init__(self, text: str) -> None:
    """
    Notes what was given, for Qt's 'QTextLayout::QTextLayout(const QString
    &text)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#QTextLayout

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QTextLayout::QTextLayout(const QString &text)
    self._noteCreation(QTextLayout, lambda: Rituals.call(
        'ritual_ZN11QTextLayoutC1ERK7QString', text,
    ))

  @overload(str, QFont)
  @overload(str, QFont, QPaintDevice)
  @overload(str, QFont, NoneType)
  def __init__(
      self,
      text: str,
      font: QFont,
      paintdevice: Optional[QPaintDevice] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextLayout::QTextLayout(const QString
    &text, const QFont &font, const QPaintDevice *paintdevice)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#QTextLayout

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    paintdevice : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextLayout::QTextLayout(const QString &text, const QFont &font, const
    #      QPaintDevice *paintdevice)
    self._noteCreation(QTextLayout, lambda: Rituals.call(
        'ritual_ZN11QTextLayoutC1ERK7QStringRK5QFontPK12QPaintDevice',
        text, self._valueOf(font), self._addressOf(paintdevice),
    ))

  @overload(QTextBlock)
  def __init__(self, b: QTextBlock) -> None:
    """
    Notes what was given, for Qt's 'QTextLayout::QTextLayout(const QTextBlock
    &b)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#QTextLayout

    Parameters
    ----------

    b : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  QTextLayout::QTextLayout(const QTextBlock &b)
    self._noteCreation(QTextLayout, lambda: Rituals.call(
        'ritual_ZN11QTextLayoutC1ERK10QTextBlock', self._valueOf(b),
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

  def clearFormats(self) -> None:
    """
    Calls Qt's 'void QTextLayout::clearFormats()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#clearFormats
    """
    #  void QTextLayout::clearFormats()
    self.uglySide.call('ritual_ZN11QTextLayout12clearFormatsEv')

  def beginLayout(self) -> None:
    """
    Calls Qt's 'void QTextLayout::beginLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#beginLayout
    """
    #  void QTextLayout::beginLayout()
    self.uglySide.call('ritual_ZN11QTextLayout11beginLayoutEv')

  def endLayout(self) -> None:
    """
    Calls Qt's 'void QTextLayout::endLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#endLayout
    """
    #  void QTextLayout::endLayout()
    self.uglySide.call('ritual_ZN11QTextLayout9endLayoutEv')

  def clearLayout(self) -> None:
    """
    Calls Qt's 'void QTextLayout::clearLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#clearLayout
    """
    #  void QTextLayout::clearLayout()
    self.uglySide.call('ritual_ZN11QTextLayout11clearLayoutEv')

  def createLine(self) -> QTextLine:
    """
    Calls Qt's 'QTextLine QTextLayout::createLine()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#createLine

    Returns
    -------

    QTextLine
      A new cute QTextLine around the copy Qt gave back. Python owns it.
    """
    #  QTextLine QTextLayout::createLine()
    address = self.uglySide.call('ritual_ZN11QTextLayout10createLineEv')
    from . import QTextLine
    return QTextLine._cuteOwning(address)

  @overload(QPainter, QPointF, int)
  @overload(NoneType, QPointF, int)
  def drawCursor(
      self,
      p: Optional[QPainter],
      pos: QPointF,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void QTextLayout::drawCursor(QPainter *p, const QPointF &pos,
    int cursorPosition) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#drawCursor

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QTextLayout::drawCursor(QPainter *p, const QPointF &pos, int
    #      cursorPosition) const
    self.uglySide.call(
        'ritual_ZNK11QTextLayout10drawCursorEP8QPainterRK7QPointFi',
        self._addressOf(p), self._valueOf(pos), cursorPosition,
    )

  @overload(QPainter, QPointF, int, int)
  @overload(NoneType, QPointF, int, int)
  def drawCursor(
      self,
      p: Optional[QPainter],
      pos: QPointF,
      cursorPosition: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QTextLayout::drawCursor(QPainter *p, const QPointF &pos,
    int cursorPosition, int width) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlayout.html#drawCursor

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cursorPosition : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QTextLayout::drawCursor(QPainter *p, const QPointF &pos, int
    #      cursorPosition, int width) const
    self.uglySide.call(
        'ritual_ZNK11QTextLayout10drawCursorEP8QPainterRK7QPointFii',
        self._addressOf(p), self._valueOf(pos), cursorPosition, width,
    )
