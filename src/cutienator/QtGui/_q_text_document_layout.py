"""
QTextDocumentLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocumentlayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextDocumentLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractTextDocumentLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF, QTimerEvent
  from . import QPainter, QTextBlock, QTextDocument, QTextFormat, QTextFrame
  from . import QTextInlineObject, QTextTable, QTextTableCell
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFormat = WAIT['QTextFormat']
  QTextFrame = WAIT['QTextFrame']
  QTextInlineObject = WAIT['QTextInlineObject']
  QTextTable = WAIT['QTextTable']
  QTextTableCell = WAIT['QTextTableCell']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDocumentLayout(QAbstractTextDocumentLayout):
  """
  The cute side of Qt's QTextDocumentLayout: a plain Python object standing
  in front of one C++ QTextDocumentLayout.

  It is built on the cute 'QAbstractTextDocumentLayout', as Qt's
  QTextDocumentLayout is built on Qt's QAbstractTextDocumentLayout, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTextDocumentLayout that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr', 'draw',
  'hitTest', 'pageCount', 'documentSize', 'setCursorWidth', 'cursorWidth',
  'setFixedColumnWidth', 'setViewport', 'frameBoundingRect',
  'blockBoundingRect', 'tableBoundingRect', 'tableCellBoundingRect',
  'layoutStatus', 'dynamicPageCount', 'dynamicDocumentSize',
  'ensureLayouted', 'idealWidth', 'contentHasAlignment', 'documentChanged',
  'resizeInlineObject', 'positionInlineObject', 'drawInlineObject',
  'timerEvent', 'doLayout', 'layoutFinished'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextDocumentLayoutPrivate *QTextDocumentLayout::d_func()': gives
    'QTextDocumentLayoutPrivate', which has no cute class yet.
  - Qt's 'const QTextDocumentLayoutPrivate *QTextDocumentLayout::d_func()
    const': gives 'QTextDocumentLayoutPrivate', which has no cute class yet.
  - Qt's 'void *QTextDocumentLayout::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QTextDocumentLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTextDocumentLayout is created at the first use, not by
    'QTextDocumentLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextDocumentLayout.
  - Qt tells when it has removed the C++ QTextDocumentLayout. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QTextDocumentLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentlayout.html#tr

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
    #  QString QTextDocumentLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QTextDocumentLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDocumentLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextDocumentLayout::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextDocumentLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(self, point: QPointF, accuracy: Qt.HitTestAccuracy) -> int:
    """
    Calls Qt's 'int QTextDocumentLayout::hitTest(const QPointF &point,
    Qt::HitTestAccuracy accuracy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentlayout.html#hitTest

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    accuracy : Qt.HitTestAccuracy
      Passed on as its number.
    """
    #  int QTextDocumentLayout::hitTest(const QPointF &point,
    #      Qt::HitTestAccuracy accuracy) const
    ritual = (
        'ritual_ZNK19QTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAcc'
        'uracyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QTextDocumentLayout7hitTestERK7QPointFN2Qt15HitT'
          'estAccuracyE')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), accuracy.value,
    )

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QTextDocumentLayout::pageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentlayout.html#pageCount
    """
    #  int QTextDocumentLayout::pageCount() const
    ritual = 'ritual_ZNK19QTextDocumentLayout9pageCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QTextDocumentLayout9pageCountEv'
    return self.uglySide.call(ritual)

  def documentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QTextDocumentLayout::documentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#documentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QTextDocumentLayout::documentSize() const
    ritual = 'ritual_ZNK19QTextDocumentLayout12documentSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QTextDocumentLayout12documentSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QTextDocumentLayout::cursorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#cursorWidth
    """
    #  int QTextDocumentLayout::cursorWidth() const
    return self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout11cursorWidthEv',
    )

  @overload(QTextFrame)
  @overload(NoneType)
  def frameBoundingRect(self, frame: Optional[QTextFrame]) -> QRectF:
    """
    Calls Qt's 'QRectF QTextDocumentLayout::frameBoundingRect(QTextFrame
    *frame) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#frameBoundingRect

    Parameters
    ----------

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextDocumentLayout::frameBoundingRect(QTextFrame *frame) const
    ritual = (
        'ritual_ZNK19QTextDocumentLayout17frameBoundingRectEP10QTextFrame')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QTextDocumentLayout17frameBoundingRectEP10QTextF'
          'rame')
    address = self.uglySide.call(ritual, self._addressOf(frame))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QTextDocumentLayout::blockBoundingRect(const
    QTextBlock &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#blockBoundingRect

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
    #  QRectF QTextDocumentLayout::blockBoundingRect(const QTextBlock &block)
    #      const
    ritual = (
        'ritual_ZNK19QTextDocumentLayout17blockBoundingRectERK10QTextBlock')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QTextDocumentLayout17blockBoundingRectERK10QText'
          'Block')
    address = self.uglySide.call(ritual, self._valueOf(block))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextTable)
  @overload(NoneType)
  def tableBoundingRect(self, table: Optional[QTextTable]) -> QRectF:
    """
    Calls Qt's 'QRectF QTextDocumentLayout::tableBoundingRect(QTextTable
    *table) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#tableBoundingRect

    Parameters
    ----------

    table : Optional[QTextTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextDocumentLayout::tableBoundingRect(QTextTable *table) const
    address = self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout17tableBoundingRectEP10QTextTable',
        self._addressOf(table),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextTable, QTextTableCell)
  @overload(NoneType, QTextTableCell)
  def tableCellBoundingRect(
      self,
      table: Optional[QTextTable],
      cell: QTextTableCell,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QTextDocumentLayout::tableCellBoundingRect(QTextTable
    *table, const QTextTableCell &cell) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#tableCellBoundingRect

    Parameters
    ----------

    table : Optional[QTextTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cell : QTextTableCell
      Passed on as a value: Qt reads the C++ QTextTableCell, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextDocumentLayout::tableCellBoundingRect(QTextTable *table,
    #      const QTextTableCell &cell) const
    address = self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout21tableCellBoundingRectEP10QTextTab'
        'leRK14QTextTableCell',
        self._addressOf(table), self._valueOf(cell),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def layoutStatus(self) -> int:
    """
    Calls Qt's 'int QTextDocumentLayout::layoutStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#layoutStatus
    """
    #  int QTextDocumentLayout::layoutStatus() const
    return self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout12layoutStatusEv',
    )

  def dynamicPageCount(self) -> int:
    """
    Calls Qt's 'int QTextDocumentLayout::dynamicPageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#dynamicPageCount
    """
    #  int QTextDocumentLayout::dynamicPageCount() const
    return self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout16dynamicPageCountEv',
    )

  def dynamicDocumentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QTextDocumentLayout::dynamicDocumentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#dynamicDocumentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QTextDocumentLayout::dynamicDocumentSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout19dynamicDocumentSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def idealWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextDocumentLayout::idealWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#idealWidth
    """
    #  qreal QTextDocumentLayout::idealWidth() const
    return self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout10idealWidthEv',
    )

  def contentHasAlignment(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentLayout::contentHasAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#contentHasAlignment
    """
    #  bool QTextDocumentLayout::contentHasAlignment() const
    return self.uglySide.call(
        'ritual_ZNK19QTextDocumentLayout19contentHasAlignmentEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCursorWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::setCursorWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#setCursorWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QTextDocumentLayout::setCursorWidth(int width)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentLayout14setCursorWidthEi', width,
    )

  @overload(int)
  def setFixedColumnWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::setFixedColumnWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#setFixedColumnWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QTextDocumentLayout::setFixedColumnWidth(int width)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentLayout19setFixedColumnWidthEi', width,
    )

  @overload(QRectF)
  def setViewport(self, viewport: QRectF) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::setViewport(const QRectF
    &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#setViewport

    Parameters
    ----------

    viewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QTextDocumentLayout::setViewport(const QRectF &viewport)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentLayout11setViewportERK6QRectF',
        self._valueOf(viewport),
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
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentLayout::QTextDocumentLayout(QTextDocument *doc)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#QTextDocumentLayout

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextDocumentLayout::QTextDocumentLayout(QTextDocument *doc)
    self._noteCreation(QTextDocumentLayout, lambda: Rituals.call(
        'ritual_ZN19QTextDocumentLayoutC1EP13QTextDocument',
        self._addressOf(doc),
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
      painter: Optional[QPainter],
      context: QAbstractTextDocumentLayout.PaintContext,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::draw(QPainter *painter, const
    PaintContext &context)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentlayout.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : QAbstractTextDocumentLayout.PaintContext
      Passed on as a value: Qt reads the C++
      QAbstractTextDocumentLayout::PaintContext, which stays Python's own.
    """
    #  void QTextDocumentLayout::draw(QPainter *painter, const PaintContext
    #      &context)
    ritual = (
        'ritual_ZN19QTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDo'
        'cumentLayout12PaintContextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QTextDocumentLayout4drawEP8QPainterRKN27QAbstract'
          'TextDocumentLayout12PaintContextE')
    self.uglySide.call(
        ritual, self._addressOf(painter), self._valueOf(context),
    )

  @overload(float)
  def ensureLayouted(self, a0: float) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::ensureLayouted(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#ensureLayouted

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QTextDocumentLayout::ensureLayouted(qreal a0)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentLayout14ensureLayoutedEd', a0,
    )

  @overload(int, int, int)
  def documentChanged(self, from_: int, oldLength: int, length: int) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::documentChanged(int from, int
    oldLength, int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#documentChanged

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    oldLength : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QTextDocumentLayout::documentChanged(int from, int oldLength, int
    #      length)
    ritual = 'ritual_ZN19QTextDocumentLayout15documentChangedEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QTextDocumentLayout15documentChangedEiii'
    self.uglySide.call(ritual, from_, oldLength, length)

  @overload(QTextInlineObject, int, QTextFormat)
  def resizeInlineObject(
      self,
      item: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QTextDocumentLayout::resizeInlineObject(QTextInlineObject item, int
    posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#resizeInlineObject

    Parameters
    ----------

    item : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextDocumentLayout::resizeInlineObject(QTextInlineObject item,
    #      int posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN19QTextDocumentLayout18resizeInlineObjectE17QTextInlineOb'
        'jectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QTextDocumentLayout18resizeInlineObjectE17QTextIn'
          'lineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual, self._valueOf(item), posInDocument, self._valueOf(format),
    )

  @overload(QTextInlineObject, int, QTextFormat)
  def positionInlineObject(
      self,
      item: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QTextDocumentLayout::positionInlineObject(QTextInlineObject item, int
    posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#positionInlineObject

    Parameters
    ----------

    item : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextDocumentLayout::positionInlineObject(QTextInlineObject item,
    #      int posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN19QTextDocumentLayout20positionInlineObjectE17QTextInline'
        'ObjectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QTextDocumentLayout20positionInlineObjectE17QText'
          'InlineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual, self._valueOf(item), posInDocument, self._valueOf(format),
    )

  @overload(QPainter, QRectF, QTextInlineObject, int, QTextFormat)
  @overload(NoneType, QRectF, QTextInlineObject, int, QTextFormat)
  def drawInlineObject(
      self,
      p: Optional[QPainter],
      rect: QRectF,
      item: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::drawInlineObject(QPainter *p, const
    QRectF &rect, QTextInlineObject item, int posInDocument, const
    QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#drawInlineObject

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    item : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextDocumentLayout::drawInlineObject(QPainter *p, const QRectF
    #      &rect, QTextInlineObject item, int posInDocument, const
    #      QTextFormat &format)
    ritual = (
        'ritual_ZN19QTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRec'
        'tF17QTextInlineObjectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QTextDocumentLayout16drawInlineObjectEP8QPainterR'
          'K6QRectF17QTextInlineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual,
        self._addressOf(p), self._valueOf(rect), self._valueOf(item),
        posInDocument, self._valueOf(format),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::timerEvent(QTimerEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentLayout::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN19QTextDocumentLayout10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QTextDocumentLayout10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(int, int, int)
  def doLayout(self, from_: int, oldLength: int, length: int) -> QRectF:
    """
    Calls Qt's 'QRectF QTextDocumentLayout::doLayout(int from, int oldLength,
    int length)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentlayout.html#doLayout

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    oldLength : int
      Passed on as it is.

    length : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTextDocumentLayout::doLayout(int from, int oldLength, int
    #      length)
    address = self.uglySide.call(
        'ritual_ZN19QTextDocumentLayout8doLayoutEiii',
        from_, oldLength, length,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def layoutFinished(self) -> None:
    """
    Calls Qt's 'void QTextDocumentLayout::layoutFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentlayout.html#layoutFinished
    """
    #  void QTextDocumentLayout::layoutFinished()
    self.uglySide.call('ritual_ZN19QTextDocumentLayout14layoutFinishedEv')
