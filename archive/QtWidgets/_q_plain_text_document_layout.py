"""
QPlainTextDocumentLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAbstractTextDocumentLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from ..QtGui import QPainter, QTextBlock, QTextDocument, QTextFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFrame = WAIT['QTextFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlainTextDocumentLayout(QAbstractTextDocumentLayout):
  """
  The cute side of Qt's QPlainTextDocumentLayout: a plain Python object
  standing in front of one C++ QPlainTextDocumentLayout.

  It is built on the cute 'QAbstractTextDocumentLayout', as Qt's
  QPlainTextDocumentLayout is built on Qt's QAbstractTextDocumentLayout, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlainTextDocumentLayout that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'draw',
  'hitTest', 'pageCount', 'documentSize', 'frameBoundingRect',
  'blockBoundingRect', 'ensureBlockLayout', 'setCursorWidth', 'cursorWidth',
  'requestUpdate', 'documentChanged', 'setTextWidth', 'textWidth',
  'layoutBlock', 'blockWidth'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlainTextDocumentLayout::~QPlainTextDocumentLayout()': the
    destructor: Python never removes a C++ QPlainTextDocumentLayout.

  What has no ritual
  ------------------

  7 of the 26 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QPlainTextDocumentLayout is created at the first use, not by
    'QPlainTextDocumentLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlainTextDocumentLayout.
  - Qt tells when it has removed the C++ QPlainTextDocumentLayout. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPlainTextDocumentLayout::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlainTextDocumentLayout::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QPlainTextDocumentLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlainTextDocumentLayout'

  #  A C++ QPlainTextDocumentLayout Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlainTextDocumentLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlainTextDocumentLayout::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlainTextDocumentLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QPlainTextDocumentLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(self, a0: QPointF, a1: Qt.HitTestAccuracy) -> int:
    """
    Calls Qt's 'int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
    Qt::HitTestAccuracy a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#hitTest

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a1 : Qt.HitTestAccuracy
      Passed on as its number.
    """
    #  int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
    #      Qt::HitTestAccuracy a1) const
    ritual = (
        'ritual_ZNK24QPlainTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTe'
        'stAccuracyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPlainTextDocumentLayout7hitTestERK7QPointFN2Qt1'
          '5HitTestAccuracyE')
    return self.uglySide.call(ritual, self._valueOf(a0), a1.value)

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QPlainTextDocumentLayout::pageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#pageCount
    """
    #  int QPlainTextDocumentLayout::pageCount() const
    ritual = 'ritual_ZNK24QPlainTextDocumentLayout9pageCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QPlainTextDocumentLayout9pageCountEv'
    return self.uglySide.call(ritual)

  def documentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPlainTextDocumentLayout::documentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#documentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPlainTextDocumentLayout::documentSize() const
    ritual = 'ritual_ZNK24QPlainTextDocumentLayout12documentSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QPlainTextDocumentLayout12documentSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(QTextFrame)
  @overload(NoneType)
  def frameBoundingRect(self, a0: Optional[QTextFrame]) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame
    *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#frameBoundingRect

    Parameters
    ----------

    a0 : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame *a0)
    #      const
    ritual = (
        'ritual_ZNK24QPlainTextDocumentLayout17frameBoundingRectEP10QTextFr'
        'ame')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPlainTextDocumentLayout17frameBoundingRectEP10Q'
          'TextFrame')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextDocumentLayout::blockBoundingRect(const
    QTextBlock &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#blockBoundingRect

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextDocumentLayout::blockBoundingRect(const QTextBlock
    #      &block) const
    ritual = (
        'ritual_ZNK24QPlainTextDocumentLayout17blockBoundingRectERK10QTextB'
        'lock')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPlainTextDocumentLayout17blockBoundingRectERK10'
          'QTextBlock')
    address = self.uglySide.call(ritual, self._valueOf(block))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QPlainTextDocumentLayout::cursorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#cursorWidth
    """
    #  int QPlainTextDocumentLayout::cursorWidth() const
    return self.uglySide.call(
        'ritual_ZNK24QPlainTextDocumentLayout11cursorWidthEv',
    )

  def textWidth(self) -> float:
    """
    Calls Qt's 'qreal QPlainTextDocumentLayout::textWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#textWidth
    """
    #  qreal QPlainTextDocumentLayout::textWidth() const
    return self.uglySide.call(
        'ritual_ZNK24QPlainTextDocumentLayout9textWidthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCursorWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::setCursorWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#setCursorWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QPlainTextDocumentLayout::setCursorWidth(int width)
    self.uglySide.call(
        'ritual_ZN24QPlainTextDocumentLayout14setCursorWidthEi', width,
    )

  @overload(float)
  def setTextWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::setTextWidth(qreal newWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#setTextWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void QPlainTextDocumentLayout::setTextWidth(qreal newWidth)
    self.uglySide.call(
        'ritual_ZN24QPlainTextDocumentLayout12setTextWidthEd', newWidth,
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

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, document: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QPlainTextDocumentLayout::QPlainTextDocumentLayout(QTextDocument
    *document)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlainTextDocumentLayout::QPlainTextDocumentLayout(QTextDocument
    #      *document)
    self._noteCreation(QPlainTextDocumentLayout, lambda: Rituals.call(
        'ritual_ZN24QPlainTextDocumentLayoutC1EP13QTextDocument',
        self._addressOf(document),
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

  @overload(QPainter, QAbstractTextDocumentLayout.PaintContext)
  @overload(NoneType, QAbstractTextDocumentLayout.PaintContext)
  def draw(
      self,
      a0: Optional[QPainter],
      a1: QAbstractTextDocumentLayout.PaintContext,
  ) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::draw(QPainter *a0, const
    PaintContext &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#draw

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QAbstractTextDocumentLayout.PaintContext
      Passed on as a value: Qt reads the C++
      QAbstractTextDocumentLayout::PaintContext, which stays Python's own.
    """
    #  void QPlainTextDocumentLayout::draw(QPainter *a0, const PaintContext
    #      &a1)
    ritual = (
        'ritual_ZN24QPlainTextDocumentLayout4drawEP8QPainterRKN27QAbstractT'
        'extDocumentLayout12PaintContextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QPlainTextDocumentLayout4drawEP8QPainterRKN27QAbs'
          'tractTextDocumentLayout12PaintContextE')
    self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  @overload(QTextBlock)
  def ensureBlockLayout(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::ensureBlockLayout(const
    QTextBlock &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#ensureBlockLayout

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QPlainTextDocumentLayout::ensureBlockLayout(const QTextBlock
    #      &block) const
    self.uglySide.call(
        'ritual_ZNK24QPlainTextDocumentLayout17ensureBlockLayoutERK10QTextB'
        'lock',
        self._valueOf(block),
    )

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#requestUpdate
    """
    #  void QPlainTextDocumentLayout::requestUpdate()
    self.uglySide.call(
        'ritual_ZN24QPlainTextDocumentLayout13requestUpdateEv',
    )

  @overload(int, int, int)
  def documentChanged(self, from_: int, a1: int, charsAdded: int) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::documentChanged(int from, int
    a1, int charsAdded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#documentChanged

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    charsAdded : int
      Passed on as it is.
    """
    #  void QPlainTextDocumentLayout::documentChanged(int from, int a1, int
    #      charsAdded)
    ritual = 'ritual_ZN24QPlainTextDocumentLayout15documentChangedEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QPlainTextDocumentLayout15documentChangedEiii'
    self.uglySide.call(ritual, from_, a1, charsAdded)

  @overload(QTextBlock)
  def layoutBlock(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QPlainTextDocumentLayout::layoutBlock(const QTextBlock
    &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#layoutBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QPlainTextDocumentLayout::layoutBlock(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN24QPlainTextDocumentLayout11layoutBlockERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(QTextBlock)
  def blockWidth(self, block: QTextBlock) -> float:
    """
    Calls Qt's 'qreal QPlainTextDocumentLayout::blockWidth(const QTextBlock
    &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextdocumentlayout.html#blockWidth

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  qreal QPlainTextDocumentLayout::blockWidth(const QTextBlock &block)
    return self.uglySide.call(
        'ritual_ZN24QPlainTextDocumentLayout10blockWidthERK10QTextBlock',
        self._valueOf(block),
    )
