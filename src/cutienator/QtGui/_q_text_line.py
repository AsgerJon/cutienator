"""
QTextLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QTextLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from . import QGlyphRun, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextLine: a plain Python object standing in front of
  one C++ QTextLine.

  C++ hands a QTextLine around as a copy, so every C++ QTextLine behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextLine that has a ritual and that Python can call
  so far, 25 names in all: 'isValid', 'rect', 'x', 'y', 'width', 'ascent',
  'descent', 'height', 'leading', 'setLeadingIncluded', 'leadingIncluded',
  'naturalTextWidth', 'horizontalAdvance', 'naturalTextRect', 'cursorToX',
  'xToCursor', 'setLineWidth', 'setNumColumns', 'setPosition', 'position',
  'textStart', 'textLength', 'lineNumber', 'draw', 'glyphRuns'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qreal QTextLine::cursorToX(int *cursorPos, Edge edge) const': takes
    a number to change where it is.
  - Qt's 'QTextLine::~QTextLine()': the destructor: Python removes its C++
    QTextLine by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 3 private.

  What to expect
  --------------

  - The C++ QTextLine is created at the first use, not by 'QTextLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextLine back gives a copy the ritual made for
    Python, in a new cute QTextLine.
  """

  #  The enums Qt writes inside QTextLine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CursorPosition(CuteNum):
    """
    The enum 'QTextLine::CursorPosition' of Qt, with the 2 names Qt gives in
    it.
    """

    CursorBetweenCharacters = Kee[int](0)
    CursorOnCharacter = Kee[int](1)

  class Edge(CuteNum):
    """The enum 'QTextLine::Edge' of Qt, with the 2 names Qt gives in it."""

    Leading = Kee[int](0)
    Trailing = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextLine'

  #  Qt's '~QTextLine()'. Naming it makes this a value class: Python owns
  #  every C++ QTextLine behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QTextLineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextLine::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#isValid
    """
    #  bool QTextLine::isValid() const
    return self.uglySide.call('ritual_ZNK9QTextLine7isValidEv')

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QTextLine::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextLine::rect() const
    address = self.uglySide.call('ritual_ZNK9QTextLine4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#x
    """
    #  qreal QTextLine::x() const
    return self.uglySide.call('ritual_ZNK9QTextLine1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#y
    """
    #  qreal QTextLine::y() const
    return self.uglySide.call('ritual_ZNK9QTextLine1yEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#width
    """
    #  qreal QTextLine::width() const
    return self.uglySide.call('ritual_ZNK9QTextLine5widthEv')

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#ascent
    """
    #  qreal QTextLine::ascent() const
    return self.uglySide.call('ritual_ZNK9QTextLine6ascentEv')

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#descent
    """
    #  qreal QTextLine::descent() const
    return self.uglySide.call('ritual_ZNK9QTextLine7descentEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#height
    """
    #  qreal QTextLine::height() const
    return self.uglySide.call('ritual_ZNK9QTextLine6heightEv')

  def leading(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#leading
    """
    #  qreal QTextLine::leading() const
    return self.uglySide.call('ritual_ZNK9QTextLine7leadingEv')

  def leadingIncluded(self) -> bool:
    """
    Calls Qt's 'bool QTextLine::leadingIncluded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#leadingIncluded
    """
    #  bool QTextLine::leadingIncluded() const
    return self.uglySide.call('ritual_ZNK9QTextLine15leadingIncludedEv')

  def naturalTextWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::naturalTextWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#naturalTextWidth
    """
    #  qreal QTextLine::naturalTextWidth() const
    return self.uglySide.call('ritual_ZNK9QTextLine16naturalTextWidthEv')

  def horizontalAdvance(self) -> float:
    """
    Calls Qt's 'qreal QTextLine::horizontalAdvance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#horizontalAdvance
    """
    #  qreal QTextLine::horizontalAdvance() const
    return self.uglySide.call('ritual_ZNK9QTextLine17horizontalAdvanceEv')

  def naturalTextRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QTextLine::naturalTextRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#naturalTextRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextLine::naturalTextRect() const
    address = self.uglySide.call('ritual_ZNK9QTextLine15naturalTextRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(int)
  @overload(int, Edge)
  def cursorToX(self, cursorPos: int, edge: Edge = Edge.Leading) -> float:
    """
    Calls Qt's 'qreal QTextLine::cursorToX(int cursorPos, Edge edge) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#cursorToX

    Parameters
    ----------

    cursorPos : int
      Passed on as it is.

    edge : Edge
      Passed on as its number. May be left out, as in Qt: it is then
      Edge.Leading.
    """
    #  qreal QTextLine::cursorToX(int cursorPos, Edge edge) const
    return self.uglySide.call(
        'ritual_ZNK9QTextLine9cursorToXEiNS_4EdgeE', cursorPos, edge.value,
    )

  @overload(float)
  @overload(float, CursorPosition)
  def xToCursor(
      self,
      x: float,
      a1: CursorPosition = CursorPosition.CursorBetweenCharacters,
  ) -> int:
    """
    Calls Qt's 'int QTextLine::xToCursor(qreal x, CursorPosition a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#xToCursor

    Parameters
    ----------

    x : float
      Passed on as it is.

    a1 : CursorPosition
      Passed on as its number. May be left out, as in Qt: it is then
      CursorPosition.CursorBetweenCharacters.
    """
    #  int QTextLine::xToCursor(qreal x, CursorPosition a1) const
    return self.uglySide.call(
        'ritual_ZNK9QTextLine9xToCursorEdNS_14CursorPositionE', x, a1.value,
    )

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QTextLine::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTextLine::position() const
    address = self.uglySide.call('ritual_ZNK9QTextLine8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def textStart(self) -> int:
    """
    Calls Qt's 'int QTextLine::textStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#textStart
    """
    #  int QTextLine::textStart() const
    return self.uglySide.call('ritual_ZNK9QTextLine9textStartEv')

  def textLength(self) -> int:
    """
    Calls Qt's 'int QTextLine::textLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#textLength
    """
    #  int QTextLine::textLength() const
    return self.uglySide.call('ritual_ZNK9QTextLine10textLengthEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QTextLine::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#lineNumber
    """
    #  int QTextLine::lineNumber() const
    return self.uglySide.call('ritual_ZNK9QTextLine10lineNumberEv')

  @overload(int, int, QTextLayout.GlyphRunRetrievalFlags)
  def glyphRuns(
      self,
      from_: int,
      length: int,
      flags: QTextLayout.GlyphRunRetrievalFlags,
  ) -> QList[QGlyphRun]:
    """
    Calls Qt's 'QList<QGlyphRun> QTextLine::glyphRuns(int from, int length,
    QTextLayout::GlyphRunRetrievalFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#glyphRuns

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    length : int
      Passed on as it is.

    flags : QTextLayout.GlyphRunRetrievalFlags
      Passed on as its number.

    Returns
    -------

    QList[QGlyphRun]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGlyphRun> QTextLine::glyphRuns(int from, int length,
    #      QTextLayout::GlyphRunRetrievalFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK9QTextLine9glyphRunsEii6QFlagsIN11QTextLayout21GlyphRunR'
        'etrievalFlagEE',
        from_, length, flags.value,
    )
    from . import QGlyphRun
    return QList[QGlyphRun]._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, int)
  def glyphRuns(self, from_: int = -1, length: int = -1) -> QList[QGlyphRun]:
    """
    Calls Qt's 'QList<QGlyphRun> QTextLine::glyphRuns(int from, int length)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#glyphRuns

    Parameters
    ----------

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QList[QGlyphRun]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGlyphRun> QTextLine::glyphRuns(int from, int length) const
    address = self.uglySide.call(
        'ritual_ZNK9QTextLine9glyphRunsEii', from_, length,
    )
    from . import QGlyphRun
    return QList[QGlyphRun]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setLeadingIncluded(self, included: bool) -> None:
    """
    Calls Qt's 'void QTextLine::setLeadingIncluded(bool included)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#setLeadingIncluded

    Parameters
    ----------

    included : bool
      Passed on as it is.
    """
    #  void QTextLine::setLeadingIncluded(bool included)
    self.uglySide.call('ritual_ZN9QTextLine18setLeadingIncludedEb', included)

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QTextLine::setLineWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextLine::setLineWidth(qreal width)
    self.uglySide.call('ritual_ZN9QTextLine12setLineWidthEd', width)

  @overload(int)
  def setNumColumns(self, columns: int) -> None:
    """
    Calls Qt's 'void QTextLine::setNumColumns(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#setNumColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTextLine::setNumColumns(int columns)
    self.uglySide.call('ritual_ZN9QTextLine13setNumColumnsEi', columns)

  @overload(int, float)
  def setNumColumns(self, columns: int, alignmentWidth: float) -> None:
    """
    Calls Qt's 'void QTextLine::setNumColumns(int columns, qreal
    alignmentWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#setNumColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.

    alignmentWidth : float
      Passed on as it is.
    """
    #  void QTextLine::setNumColumns(int columns, qreal alignmentWidth)
    self.uglySide.call(
        'ritual_ZN9QTextLine13setNumColumnsEid', columns, alignmentWidth,
    )

  @overload(QPointF)
  def setPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QTextLine::setPosition(const QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#setPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QTextLine::setPosition(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN9QTextLine11setPositionERK7QPointF', self._valueOf(pos),
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
    Notes what was given, for Qt's 'QTextLine::QTextLine()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#QTextLine
    """
    #  QTextLine::QTextLine()
    self._noteCreation(QTextLine, lambda: Rituals.call(
        'ritual_ZN9QTextLineC1Ev',
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

  @overload(QPainter, QPointF)
  @overload(NoneType, QPointF)
  def draw(self, painter: Optional[QPainter], position: QPointF) -> None:
    """
    Calls Qt's 'void QTextLine::draw(QPainter *painter, const QPointF
    &position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextline.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QTextLine::draw(QPainter *painter, const QPointF &position) const
    self.uglySide.call(
        'ritual_ZNK9QTextLine4drawEP8QPainterRK7QPointF',
        self._addressOf(painter), self._valueOf(position),
    )
