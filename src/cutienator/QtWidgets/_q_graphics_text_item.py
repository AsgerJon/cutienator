"""
QGraphicsTextItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsItem, QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QRectF, QVariant
  from ..QtGui import QColor, QFocusEvent, QFont, QInputMethodEvent
  from ..QtGui import QKeyEvent, QPainter, QPainterPath, QTextCursor
  from ..QtGui import QTextDocument
  from . import QGraphicsSceneContextMenuEvent, QGraphicsSceneDragDropEvent
  from . import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QGraphicsSceneContextMenuEvent = WAIT['QGraphicsSceneContextMenuEvent']
  QGraphicsSceneDragDropEvent = WAIT['QGraphicsSceneDragDropEvent']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QTextCursor = WAIT['QTextCursor']
  QTextDocument = WAIT['QTextDocument']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsTextItem(QGraphicsObject):
  """
  The cute side of Qt's QGraphicsTextItem: a plain Python object standing in
  front of one C++ QGraphicsTextItem.

  It is built on the cute 'QGraphicsObject', as Qt's QGraphicsTextItem is
  built on Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsTextItem that has a ritual and that Python
  can call so far, 50 names in all: 'metaObject', 'tr', 'toHtml', 'setHtml',
  'toPlainText', 'setPlainText', 'font', 'setFont', 'setDefaultTextColor',
  'defaultTextColor', 'boundingRect', 'shape', 'contains', 'paint',
  'isObscuredBy', 'opaqueArea', 'type', 'setTextWidth', 'textWidth',
  'adjustSize', 'setDocument', 'document', 'setTextInteractionFlags',
  'textInteractionFlags', 'setTabChangesFocus', 'tabChangesFocus',
  'setOpenExternalLinks', 'openExternalLinks', 'setTextCursor', 'textCursor',
  'sceneEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'contextMenuEvent', 'keyPressEvent',
  'keyReleaseEvent', 'focusInEvent', 'focusOutEvent', 'dragEnterEvent',
  'dragLeaveEvent', 'dragMoveEvent', 'dropEvent', 'inputMethodEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'inputMethodQuery',
  'extension'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsTextItem::~QGraphicsTextItem()': the destructor: Python
    never removes a C++ QGraphicsTextItem.
  - Qt's 'bool QGraphicsTextItem::supportsExtension(Extension extension)
    const': names the enum 'QGraphicsItem::Extension', whose class cannot be
    named here.
  - Qt's 'void QGraphicsTextItem::setExtension(Extension extension, const
    QVariant &variant)': names the enum 'QGraphicsItem::Extension', whose
    class cannot be named here.

  What has no ritual
  ------------------

  8 of the 63 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QGraphicsTextItem is created at the first use, not by
    'QGraphicsTextItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsTextItem.
  - Qt tells when it has removed the C++ QGraphicsTextItem. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGraphicsTextItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#tr

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
    #  QString QGraphicsTextItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGraphicsTextItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsTextItem'

  #  A C++ QGraphicsTextItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsTextItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsTextItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsTextItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QGraphicsTextItem::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsTextItem::toHtml() const
    return self.uglySide.call('ritual_ZNK17QGraphicsTextItem6toHtmlEv')

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QGraphicsTextItem::toPlainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsTextItem::toPlainText() const
    return self.uglySide.call('ritual_ZNK17QGraphicsTextItem11toPlainTextEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphicsTextItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphicsTextItem::font() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsTextItem4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def defaultTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphicsTextItem::defaultTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#defaultTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphicsTextItem::defaultTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem16defaultTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsTextItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsTextItem::boundingRect() const
    ritual = 'ritual_ZNK17QGraphicsTextItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsTextItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsTextItem::shape() const
    ritual = 'ritual_ZNK17QGraphicsTextItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsTextItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsTextItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK17QGraphicsTextItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK17QGraphicsTextItem12isObscuredByEPK13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGraphicsTextItem12isObscuredByEPK13QGraphicsIte'
          'm')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsTextItem::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsTextItem::opaqueArea() const
    ritual = 'ritual_ZNK17QGraphicsTextItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsTextItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#type
    """
    #  int QGraphicsTextItem::type() const
    ritual = 'ritual_ZNK17QGraphicsTextItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem4typeEv'
    return self.uglySide.call(ritual)

  def textWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsTextItem::textWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#textWidth
    """
    #  qreal QGraphicsTextItem::textWidth() const
    return self.uglySide.call('ritual_ZNK17QGraphicsTextItem9textWidthEv')

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QGraphicsTextItem::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QGraphicsTextItem::document() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsTextItem8documentEv')
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags
    QGraphicsTextItem::textInteractionFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QGraphicsTextItem::textInteractionFlags()
    #      const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem20textInteractionFlagsEv',
    ))

  def tabChangesFocus(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsTextItem::tabChangesFocus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#tabChangesFocus
    """
    #  bool QGraphicsTextItem::tabChangesFocus() const
    return self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem15tabChangesFocusEv',
    )

  def openExternalLinks(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsTextItem::openExternalLinks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#openExternalLinks
    """
    #  bool QGraphicsTextItem::openExternalLinks() const
    return self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem17openExternalLinksEv',
    )

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QGraphicsTextItem::textCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QGraphicsTextItem::textCursor() const
    address = self.uglySide.call(
        'ritual_ZNK17QGraphicsTextItem10textCursorEv',
    )
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    ritual = (
        'ritual_ZNK17QGraphicsTextItem16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGraphicsTextItem16inputMethodQueryEN2Qt16InputM'
          'ethodQueryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsTextItem::extension(const QVariant
    &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#extension

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsTextItem::extension(const QVariant &variant) const
    ritual = 'ritual_ZNK17QGraphicsTextItem9extensionERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsTextItem9extensionERK8QVariant'
    address = self.uglySide.call(ritual, self._valueOf(variant))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#setHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsTextItem::setHtml(const QString &html)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem7setHtmlERK7QString', html,
    )

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setPlainText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsTextItem::setPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem12setPlainTextERK7QString', text,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsTextItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setDefaultTextColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setDefaultTextColor(const QColor
    &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setDefaultTextColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphicsTextItem::setDefaultTextColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem19setDefaultTextColorERK6QColor',
        self._valueOf(c),
    )

  @overload(float)
  def setTextWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setTextWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setTextWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGraphicsTextItem::setTextWidth(qreal width)
    self.uglySide.call('ritual_ZN17QGraphicsTextItem12setTextWidthEd', width)

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setDocument(QTextDocument
    *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#setDocument

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::setDocument(QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem11setDocumentEP13QTextDocument',
        self._addressOf(document),
    )

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::setTextInteractionFlags(Qt::TextInteractionFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QGraphicsTextItem::setTextInteractionFlags(Qt::
    #      TextInteractionFlags flags)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem23setTextInteractionFlagsE6QFlagsIN2Qt'
        '19TextInteractionFlagEE',
        flags.value,
    )

  @overload(bool)
  def setTabChangesFocus(self, b: bool) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setTabChangesFocus(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setTabChangesFocus

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QGraphicsTextItem::setTabChangesFocus(bool b)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem18setTabChangesFocusEb', b,
    )

  @overload(bool)
  def setOpenExternalLinks(self, open: bool) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setOpenExternalLinks(bool open)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setOpenExternalLinks

    Parameters
    ----------

    open : bool
      Passed on as it is.
    """
    #  void QGraphicsTextItem::setOpenExternalLinks(bool open)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem20setOpenExternalLinksEb', open,
    )

  @overload(QTextCursor)
  def setTextCursor(self, cursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::setTextCursor(const QTextCursor
    &cursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#setTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QGraphicsTextItem::setTextCursor(const QTextCursor &cursor)
    self.uglySide.call(
        'ritual_ZN17QGraphicsTextItem13setTextCursorERK11QTextCursor',
        self._valueOf(cursor),
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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsTextItem::QGraphicsTextItem(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#QGraphicsTextItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsTextItem::QGraphicsTextItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsTextItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsTextItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(str)
  @overload(str, QGraphicsItem)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsTextItem::QGraphicsTextItem(const QString &text, QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#QGraphicsTextItem

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsTextItem::QGraphicsTextItem(const QString &text,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsTextItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsTextItemC1ERK7QStringP13QGraphicsItem',
        text, self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN17QGraphicsTextItem5paintEP8QPainterPK24QStyleOptionGraph'
        'icsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem5paintEP8QPainterPK24QStyleOptio'
          'nGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def adjustSize(self) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::adjustSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#adjustSize
    """
    #  void QGraphicsTextItem::adjustSize()
    self.uglySide.call('ritual_ZN17QGraphicsTextItem10adjustSizeEv')

  @overload(QEvent)
  @overload(NoneType)
  def sceneEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsTextItem::sceneEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#sceneEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsTextItem::sceneEvent(QEvent *event)
    ritual = 'ritual_ZN17QGraphicsTextItem10sceneEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGraphicsTextItem10sceneEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem15mousePressEventEP24QGraphicsSceneMou'
        'seEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem15mousePressEventEP24QGraphicsSc'
          'eneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem14mouseMoveEventEP24QGraphicsSceneMous'
        'eEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem14mouseMoveEventEP24QGraphicsSce'
          'neMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem17mouseReleaseEventEP24QGraphicsSceneM'
        'ouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem17mouseReleaseEventEP24QGraphics'
          'SceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem21mouseDoubleClickEventEP24QGraphicsSc'
        'eneMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem21mouseDoubleClickEventEP24QGrap'
          'hicsSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(
      self,
      event: Optional[QGraphicsSceneContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem16contextMenuEventEP30QGraphicsSceneCo'
        'ntextMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem16contextMenuEventEP30QGraphicsS'
          'ceneContextMenuEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QGraphicsTextItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGraphicsTextItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QGraphicsTextItem15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QGraphicsTextItem12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QGraphicsTextItem13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem13focusOutEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragEnterEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem14dragEnterEventEP27QGraphicsSceneDrag'
        'DropEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem14dragEnterEventEP27QGraphicsSce'
          'neDragDropEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragLeaveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem14dragLeaveEventEP27QGraphicsSceneDrag'
        'DropEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem14dragLeaveEventEP27QGraphicsSce'
          'neDragDropEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragMoveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem13dragMoveEventEP27QGraphicsSceneDragD'
        'ropEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem13dragMoveEventEP27QGraphicsScen'
          'eDragDropEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstextitem.html#dropEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem9dropEventEP27QGraphicsSceneDragDropEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem9dropEventEP27QGraphicsSceneDrag'
          'DropEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem16inputMethodEventEP17QInputMethodEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem16inputMethodEventEP17QInputMeth'
          'odEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem15hoverEnterEventEP24QGraphicsSceneHov'
        'erEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem15hoverEnterEventEP24QGraphicsSc'
          'eneHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem14hoverMoveEventEP24QGraphicsSceneHove'
        'rEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem14hoverMoveEventEP24QGraphicsSce'
          'neHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstextitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    #      *event)
    ritual = (
        'ritual_ZN17QGraphicsTextItem15hoverLeaveEventEP24QGraphicsSceneHov'
        'erEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsTextItem15hoverLeaveEventEP24QGraphicsSc'
          'eneHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))
