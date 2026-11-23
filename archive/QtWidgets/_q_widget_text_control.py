"""
QWidgetTextControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWidgetTextControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAbstractTextDocumentLayout, QClipboard, QInputControl
from ..QtGui import QTextCursor, QTextDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QMimeData, QPointF, QRectF
  from ..QtCore import QRegularExpression, QSizeF, QTimerEvent, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QPagedPaintDevice, QPainter, QPalette, QTextBlock
  from ..QtGui import QTextCharFormat, QTransform
  from . import QMenu, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMimeData = WAIT['QMimeData']
  QPagedPaintDevice = WAIT['QPagedPaintDevice']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QRegularExpression = WAIT['QRegularExpression']
  QTextBlock = WAIT['QTextBlock']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTimerEvent = WAIT['QTimerEvent']
  QTransform = WAIT['QTransform']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetTextControl(QInputControl):
  """
  The cute side of Qt's QWidgetTextControl: a plain Python object standing in
  front of one C++ QWidgetTextControl.

  It is built on the cute 'QInputControl', as Qt's QWidgetTextControl is
  built on Qt's QInputControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetTextControl that has a ritual and that Python
  can call so far, 80 names in all: 'metaObject', 'tr', 'setDocument',
  'document', 'setTextCursor', 'textCursor', 'setTextInteractionFlags',
  'textInteractionFlags', 'mergeCurrentCharFormat', 'setCurrentCharFormat',
  'currentCharFormat', 'find', 'toPlainText', 'toHtml', 'toMarkdown',
  'ensureCursorVisible', 'loadResource', 'createStandardContextMenu',
  'cursorForPosition', 'cursorRect', 'selectionRect', 'anchorAt',
  'anchorPosition', 'anchorAtCursor', 'blockWithMarkerAt', 'overwriteMode',
  'setOverwriteMode', 'cursorWidth', 'setCursorWidth', 'acceptRichText',
  'setAcceptRichText', 'setTextWidth', 'textWidth', 'size',
  'setOpenExternalLinks', 'openExternalLinks',
  'setIgnoreUnusedNavigationEvents', 'ignoreUnusedNavigationEvents',
  'moveCursor', 'canPaste', 'setCursorIsFocusIndicator',
  'cursorIsFocusIndicator', 'setDragEnabled', 'isDragEnabled',
  'isWordSelectionEnabled', 'setWordSelectionEnabled', 'isPreediting',
  'print', 'hitTest', 'blockBoundingRect', 'getPaintContext', 'setPlainText',
  'setMarkdown', 'setHtml', 'cut', 'copy', 'paste', 'undo', 'redo', 'clear',
  'selectAll', 'insertPlainText', 'insertHtml', 'append', 'appendHtml',
  'appendPlainText', 'adjustSize', 'palette', 'setPalette', 'processEvent',
  'drawContents', 'setFocus', 'inputMethodQuery',
  'createMimeDataFromSelection', 'canInsertFromMimeData',
  'insertFromMimeData', 'setFocusToAnchor', 'setFocusToNextOrPreviousAnchor',
  'timerEvent', 'event'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetTextControl::~QWidgetTextControl()': the destructor: Python
    never removes a C++ QWidgetTextControl.

  What has no ritual
  ------------------

  29 of the 117 functions Qt declares: 16 a signal; 7 takes or gives a type
  that cannot be passed yet; 4 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QWidgetTextControl is created at the first use, not by
    'QWidgetTextControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetTextControl.
  - Qt tells when it has removed the C++ QWidgetTextControl. Every call on
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
    Calls Qt's 'QString QWidgetTextControl::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#tr

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
    #  QString QWidgetTextControl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWidgetTextControl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetTextControl'

  #  A C++ QWidgetTextControl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetTextControl'

  #  The functions Qt calls itself that QWidgetTextControl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'ensureCursorVisible': (
          ('_ZN18QWidgetTextControl19ensureCursorVisibleEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'loadResource': (
          ('_ZN18QWidgetTextControl12loadResourceEiRK4QUrl',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'anchorAt': (
          ('_ZNK18QWidgetTextControl8anchorAtERK7QPointF',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'hitTest': (
          ('_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccurac'
           'yE',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('int', 'enum', 'QtCore:Qt.HitTestAccuracy'),
           )),
      ),
      'blockBoundingRect': (
          ('_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
      'processEvent': (
          ('_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransformP7Q'
           'Widget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
               ('address', 'value', 'QtGui:QTransform'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethodQue'
           'ryE8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'createMimeDataFromSelection': (
          ('_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv',
           ('address', 'address', 'QtCore:QMimeData'),
           ()),
      ),
      'canInsertFromMimeData': (
          ('_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
      'insertFromMimeData': (
          ('_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetTextControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetTextControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QWidgetTextControl::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QWidgetTextControl::document() const
    address = self.uglySide.call('ritual_ZNK18QWidgetTextControl8documentEv')
    return QTextDocument._cuteAt(address)

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QWidgetTextControl::textCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QWidgetTextControl::textCursor() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl10textCursorEv',
    )
    return QTextCursor._cuteOwning(address)

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags
    QWidgetTextControl::textInteractionFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QWidgetTextControl::textInteractionFlags()
    #      const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl20textInteractionFlagsEv',
    ))

  def currentCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QWidgetTextControl::currentCharFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#currentCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QWidgetTextControl::currentCharFormat() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl17currentCharFormatEv',
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QWidgetTextControl::toPlainText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControl::toPlainText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl11toPlainTextEv',
    )

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QWidgetTextControl::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControl::toHtml() const
    return self.uglySide.call('ritual_ZNK18QWidgetTextControl6toHtmlEv')

  @overload()
  @overload(QTextDocument.MarkdownFeatures)
  def toMarkdown(
      self,
      features: QTextDocument.MarkdownFeatures = (
          QTextDocument.MarkdownFeatures.MarkdownDialectGitHub),
  ) -> str:
    """
    Calls Qt's 'QString
    QWidgetTextControl::toMarkdown(QTextDocument::MarkdownFeatures features)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#toMarkdown

    Parameters
    ----------

    features : QTextDocument.MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.MarkdownFeatures.MarkdownDialectGitHub.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControl::toMarkdown(QTextDocument::MarkdownFeatures
    #      features) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl10toMarkdownE6QFlagsIN13QTextDocumen'
        't15MarkdownFeatureEE',
        features.value,
    )

  @overload(QPointF)
  def cursorForPosition(self, pos: QPointF) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QWidgetTextControl::cursorForPosition(const
    QPointF &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#cursorForPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QWidgetTextControl::cursorForPosition(const QPointF &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl17cursorForPositionERK7QPointF',
        self._valueOf(pos),
    )
    return QTextCursor._cuteOwning(address)

  @overload(QTextCursor)
  def cursorRect(self, cursor: QTextCursor) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControl::cursorRect(const QTextCursor
    &cursor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#cursorRect

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetTextControl::cursorRect(const QTextCursor &cursor) const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl10cursorRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  def cursorRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControl::cursorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#cursorRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetTextControl::cursorRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl10cursorRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextCursor)
  def selectionRect(self, cursor: QTextCursor) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControl::selectionRect(const QTextCursor
    &cursor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#selectionRect

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetTextControl::selectionRect(const QTextCursor &cursor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl13selectionRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  def selectionRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControl::selectionRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#selectionRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetTextControl::selectionRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl13selectionRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF)
  def anchorAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QWidgetTextControl::anchorAt(const QPointF &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#anchorAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControl::anchorAt(const QPointF &pos) const
    ritual = 'ritual_ZNK18QWidgetTextControl8anchorAtERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QWidgetTextControl8anchorAtERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(pos))

  @overload(str)
  def anchorPosition(self, name: str) -> QPointF:
    """
    Calls Qt's 'QPointF QWidgetTextControl::anchorPosition(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#anchorPosition

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidgetTextControl::anchorPosition(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl14anchorPositionERK7QString', name,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def anchorAtCursor(self) -> str:
    """
    Calls Qt's 'QString QWidgetTextControl::anchorAtCursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#anchorAtCursor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControl::anchorAtCursor() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl14anchorAtCursorEv',
    )

  @overload(QPointF)
  def blockWithMarkerAt(self, pos: QPointF) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QWidgetTextControl::blockWithMarkerAt(const
    QPointF &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#blockWithMarkerAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QWidgetTextControl::blockWithMarkerAt(const QPointF &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl17blockWithMarkerAtERK7QPointF',
        self._valueOf(pos),
    )
    from ..QtGui import QTextBlock
    return QTextBlock._cuteOwning(address)

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::overwriteMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#overwriteMode
    """
    #  bool QWidgetTextControl::overwriteMode() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl13overwriteModeEv',
    )

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QWidgetTextControl::cursorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#cursorWidth
    """
    #  int QWidgetTextControl::cursorWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl11cursorWidthEv',
    )

  def acceptRichText(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::acceptRichText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#acceptRichText
    """
    #  bool QWidgetTextControl::acceptRichText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl14acceptRichTextEv',
    )

  def textWidth(self) -> float:
    """
    Calls Qt's 'qreal QWidgetTextControl::textWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#textWidth
    """
    #  qreal QWidgetTextControl::textWidth() const
    return self.uglySide.call('ritual_ZNK18QWidgetTextControl9textWidthEv')

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QWidgetTextControl::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QWidgetTextControl::size() const
    address = self.uglySide.call('ritual_ZNK18QWidgetTextControl4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def openExternalLinks(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::openExternalLinks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#openExternalLinks
    """
    #  bool QWidgetTextControl::openExternalLinks() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl17openExternalLinksEv',
    )

  def ignoreUnusedNavigationEvents(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::ignoreUnusedNavigationEvents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html
    """
    #  bool QWidgetTextControl::ignoreUnusedNavigationEvents() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl28ignoreUnusedNavigationEventsEv',
    )

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#canPaste
    """
    #  bool QWidgetTextControl::canPaste() const
    return self.uglySide.call('ritual_ZNK18QWidgetTextControl8canPasteEv')

  def cursorIsFocusIndicator(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::cursorIsFocusIndicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#cursorIsFocusIndicator
    """
    #  bool QWidgetTextControl::cursorIsFocusIndicator() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl22cursorIsFocusIndicatorEv',
    )

  def isDragEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::isDragEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#isDragEnabled
    """
    #  bool QWidgetTextControl::isDragEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl13isDragEnabledEv',
    )

  def isWordSelectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::isWordSelectionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#isWordSelectionEnabled
    """
    #  bool QWidgetTextControl::isWordSelectionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl22isWordSelectionEnabledEv',
    )

  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(self, point: QPointF, accuracy: Qt.HitTestAccuracy) -> int:
    """
    Calls Qt's 'int QWidgetTextControl::hitTest(const QPointF &point,
    Qt::HitTestAccuracy accuracy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#hitTest

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    accuracy : Qt.HitTestAccuracy
      Passed on as its number.
    """
    #  int QWidgetTextControl::hitTest(const QPointF &point,
    #      Qt::HitTestAccuracy accuracy) const
    ritual = (
        'ritual_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccu'
        'racyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTe'
          'stAccuracyE')
    return self.uglySide.call(ritual, self._valueOf(point), accuracy.value)

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControl::blockBoundingRect(const QTextBlock
    &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#blockBoundingRect

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
    #  QRectF QWidgetTextControl::blockBoundingRect(const QTextBlock &block)
    #      const
    ritual = (
        'ritual_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextB'
          'lock')
    address = self.uglySide.call(ritual, self._valueOf(block))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def getPaintContext(
      self,
      widget: Optional[QWidget],
  ) -> QAbstractTextDocumentLayout.PaintContext:
    """
    Calls Qt's 'QAbstractTextDocumentLayout::PaintContext
    QWidgetTextControl::getPaintContext(QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#getPaintContext

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QAbstractTextDocumentLayout.PaintContext
      A new cute QAbstractTextDocumentLayout::PaintContext around the copy Qt
      gave back. Python owns it.
    """
    #  QAbstractTextDocumentLayout::PaintContext
    #      QWidgetTextControl::getPaintContext(QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl15getPaintContextEP7QWidget',
        self._addressOf(widget),
    )
    return QAbstractTextDocumentLayout.PaintContext._cuteOwning(address)

  def palette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QWidgetTextControl::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QWidgetTextControl::palette() const
    address = self.uglySide.call('ritual_ZNK18QWidgetTextControl7paletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      property: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QWidgetTextControl::inputMethodQuery(Qt::InputMethodQuery property,
    QVariant argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWidgetTextControl::inputMethodQuery(Qt::InputMethodQuery
    #      property, QVariant argument) const
    ritual = (
        'ritual_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethod'
        'QueryE8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16Input'
          'MethodQueryE8QVariant')
    address = self.uglySide.call(
        ritual, property.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def createMimeDataFromSelection(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QWidgetTextControl::createMimeDataFromSelection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QWidgetTextControl::createMimeDataFromSelection() const
    ritual = 'ritual_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QWidgetTextControl27createMimeDataFromSelectionE'
          'v')
    address = self.uglySide.call(ritual)
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QMimeData)
  @overload(NoneType)
  def canInsertFromMimeData(self, source: Optional[QMimeData]) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::canInsertFromMimeData(const
    QMimeData *source) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#canInsertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetTextControl::canInsertFromMimeData(const QMimeData
    #      *source) const
    ritual = (
        'ritual_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMi'
          'meData')
    return self.uglySide.call(ritual, self._addressOf(source))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setDocument(QTextDocument
    *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setDocument

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControl::setDocument(QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl11setDocumentEP13QTextDocument',
        self._addressOf(document),
    )

  @overload(QTextCursor)
  @overload(QTextCursor, bool)
  def setTextCursor(
      self,
      cursor: QTextCursor,
      selectionClipboard: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setTextCursor(const QTextCursor
    &cursor, bool selectionClipboard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    selectionClipboard : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetTextControl::setTextCursor(const QTextCursor &cursor, bool
    #      selectionClipboard)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl13setTextCursorERK11QTextCursorb',
        self._valueOf(cursor), selectionClipboard,
    )

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControl::setTextInteractionFlags(Qt::TextInteractionFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QWidgetTextControl::setTextInteractionFlags(Qt::
    #      TextInteractionFlags flags)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl23setTextInteractionFlagsE6QFlagsIN2Q'
        't19TextInteractionFlagEE',
        flags.value,
    )

  @overload(QTextCharFormat)
  def setCurrentCharFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setCurrentCharFormat(const
    QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setCurrentCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QWidgetTextControl::setCurrentCharFormat(const QTextCharFormat
    #      &format)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl20setCurrentCharFormatERK15QTextCharF'
        'ormat',
        self._valueOf(format),
    )

  @overload(bool)
  def setOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setOverwriteMode(bool overwrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setOverwriteMode(bool overwrite)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl16setOverwriteModeEb', overwrite,
    )

  @overload(int)
  def setCursorWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setCursorWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setCursorWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QWidgetTextControl::setCursorWidth(int width)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl14setCursorWidthEi', width,
    )

  @overload(bool)
  def setAcceptRichText(self, accept: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setAcceptRichText(bool accept)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setAcceptRichText

    Parameters
    ----------

    accept : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setAcceptRichText(bool accept)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl17setAcceptRichTextEb', accept,
    )

  @overload(float)
  def setTextWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setTextWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setTextWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QWidgetTextControl::setTextWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl12setTextWidthEd', width,
    )

  @overload(bool)
  def setOpenExternalLinks(self, open: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setOpenExternalLinks(bool open)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setOpenExternalLinks

    Parameters
    ----------

    open : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setOpenExternalLinks(bool open)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl20setOpenExternalLinksEb', open,
    )

  @overload(bool)
  def setIgnoreUnusedNavigationEvents(self, ignore: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setIgnoreUnusedNavigationEvents(bool
    ignore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html

    Parameters
    ----------

    ignore : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setIgnoreUnusedNavigationEvents(bool ignore)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl31setIgnoreUnusedNavigationEventsEb',
        ignore,
    )

  @overload(bool)
  def setCursorIsFocusIndicator(self, b: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setCursorIsFocusIndicator(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setCursorIsFocusIndicator

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setCursorIsFocusIndicator(bool b)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl25setCursorIsFocusIndicatorEb', b,
    )

  @overload(bool)
  def setDragEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setDragEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setDragEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setDragEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl14setDragEnabledEb', enabled,
    )

  @overload(bool)
  def setWordSelectionEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setWordSelectionEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setWordSelectionEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWidgetTextControl::setWordSelectionEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl23setWordSelectionEnabledEb', enabled,
    )

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setPlainText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::setPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl12setPlainTextERK7QString', text,
    )

  @overload(str)
  def setMarkdown(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setMarkdown(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setMarkdown

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::setMarkdown(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl11setMarkdownERK7QString', text,
    )

  @overload(str)
  def setHtml(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setHtml(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#setHtml

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::setHtml(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl7setHtmlERK7QString', text,
    )

  @overload(QPalette)
  def setPalette(self, pal: QPalette) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setPalette(const QPalette &pal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#setPalette

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QWidgetTextControl::setPalette(const QPalette &pal)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl10setPaletteERK8QPalette',
        self._valueOf(pal),
    )

  @overload(bool)
  @overload(bool, Qt.FocusReason)
  def setFocus(
      self,
      focus: bool,
      a1: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::setFocus(bool focus, Qt::FocusReason
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.

    a1 : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QWidgetTextControl::setFocus(bool focus, Qt::FocusReason a1)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl8setFocusEbN2Qt11FocusReasonE',
        focus, a1.value,
    )

  @overload(QTextCursor)
  def setFocusToAnchor(self, newCursor: QTextCursor) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::setFocusToAnchor(const QTextCursor
    &newCursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#setFocusToAnchor

    Parameters
    ----------

    newCursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  bool QWidgetTextControl::setFocusToAnchor(const QTextCursor
    #      &newCursor)
    return self.uglySide.call(
        'ritual_ZN18QWidgetTextControl16setFocusToAnchorERK11QTextCursor',
        self._valueOf(newCursor),
    )

  @overload(bool)
  def setFocusToNextOrPreviousAnchor(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::setFocusToNextOrPreviousAnchor(bool
    next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QWidgetTextControl::setFocusToNextOrPreviousAnchor(bool next)
    return self.uglySide.call(
        'ritual_ZN18QWidgetTextControl30setFocusToNextOrPreviousAnchorEb',
        next,
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
  @overload(QTextDocument, QObject)
  @overload(QTextDocument, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      doc: Optional[QTextDocument],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetTextControl::QWidgetTextControl(QTextDocument *doc, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#QWidgetTextControl

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWidgetTextControl::QWidgetTextControl(QTextDocument *doc, QObject
    #      *parent)
    self._noteCreation(QWidgetTextControl, lambda: Rituals.call(
        'ritual_ZN18QWidgetTextControlC1EP13QTextDocumentP7QObject',
        self._addressOf(doc), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetTextControl::QWidgetTextControl(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#QWidgetTextControl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWidgetTextControl::QWidgetTextControl(QObject *parent)
    self._noteCreation(QWidgetTextControl, lambda: Rituals.call(
        'ritual_ZN18QWidgetTextControlC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetTextControl::QWidgetTextControl(const QString &text, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#QWidgetTextControl

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWidgetTextControl::QWidgetTextControl(const QString &text, QObject
    #      *parent)
    self._noteCreation(QWidgetTextControl, lambda: Rituals.call(
        'ritual_ZN18QWidgetTextControlC1ERK7QStringP7QObject',
        text, self._addressOf(parent, 'QObject'),
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

  @overload(QTextCharFormat)
  def mergeCurrentCharFormat(self, modifier: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::mergeCurrentCharFormat(const
    QTextCharFormat &modifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#mergeCurrentCharFormat

    Parameters
    ----------

    modifier : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QWidgetTextControl::mergeCurrentCharFormat(const QTextCharFormat
    #      &modifier)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl22mergeCurrentCharFormatERK15QTextCha'
        'rFormat',
        self._valueOf(modifier),
    )

  @overload(str)
  @overload(str, QTextDocument.FindFlags)
  def find(
      self,
      exp: str,
      options: QTextDocument.FindFlags = QTextDocument.FindFlags(),
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::find(const QString &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#find

    Parameters
    ----------

    exp : str
      Passed on as it is: a QString is made of it for the call.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QWidgetTextControl::find(const QString &exp,
    #      QTextDocument::FindFlags options)
    return self.uglySide.call(
        'ritual_ZN18QWidgetTextControl4findERK7QString6QFlagsIN13QTextDocum'
        'ent8FindFlagEE',
        exp, options.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, QTextDocument.FindFlags)
  def find(
      self,
      exp: QRegularExpression,
      options: QTextDocument.FindFlags = QTextDocument.FindFlags(),
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::find(const QRegularExpression &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#find

    Parameters
    ----------

    exp : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QWidgetTextControl::find(const QRegularExpression &exp,
    #      QTextDocument::FindFlags options)
    return self.uglySide.call(
        'ritual_ZN18QWidgetTextControl4findERK18QRegularExpression6QFlagsIN'
        '13QTextDocument8FindFlagEE',
        self._valueOf(exp), options.value,
    )

  def ensureCursorVisible(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::ensureCursorVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#ensureCursorVisible
    """
    #  void QWidgetTextControl::ensureCursorVisible()
    ritual = 'ritual_ZN18QWidgetTextControl19ensureCursorVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWidgetTextControl19ensureCursorVisibleEv'
    self.uglySide.call(ritual)

  @overload(int, QUrl)
  def loadResource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QWidgetTextControl::loadResource(int type, const
    QUrl &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWidgetTextControl::loadResource(int type, const QUrl &name)
    ritual = 'ritual_ZN18QWidgetTextControl12loadResourceEiRK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWidgetTextControl12loadResourceEiRK4QUrl'
    address = self.uglySide.call(ritual, type, self._valueOf(name))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPointF, QWidget)
  @overload(QPointF, NoneType)
  def createStandardContextMenu(
      self,
      pos: QPointF,
      parent: Optional[QWidget],
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QWidgetTextControl::createStandardContextMenu(const
    QPointF &pos, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#createStandardContextMenu

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QWidgetTextControl::createStandardContextMenu(const QPointF
    #      &pos, QWidget *parent)
    address = self.uglySide.call(
        'ritual_ZN18QWidgetTextControl25createStandardContextMenuERK7QPoint'
        'FP7QWidget',
        self._valueOf(pos), self._addressOf(parent),
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QTextCursor.MoveOperation)
  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode)
  def moveCursor(
      self,
      op: QTextCursor.MoveOperation,
      mode: QTextCursor.MoveMode = QTextCursor.MoveMode.MoveAnchor,
  ) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControl::moveCursor(QTextCursor::MoveOperation op,
    QTextCursor::MoveMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#moveCursor

    Parameters
    ----------

    op : QTextCursor.MoveOperation
      Passed on as its number.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  void QWidgetTextControl::moveCursor(QTextCursor::MoveOperation op,
    #      QTextCursor::MoveMode mode)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl10moveCursorEN11QTextCursor13MoveOper'
        'ationENS0_8MoveModeE',
        op.value, mode.value,
    )

  def isPreediting(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::isPreediting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#isPreediting
    """
    #  bool QWidgetTextControl::isPreediting()
    return self.uglySide.call(
        'ritual_ZN18QWidgetTextControl12isPreeditingEv',
    )

  @overload(QPagedPaintDevice)
  @overload(NoneType)
  def print(self, printer: Optional[QPagedPaintDevice]) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::print(QPagedPaintDevice *printer)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#print

    Parameters
    ----------

    printer : Optional[QPagedPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControl::print(QPagedPaintDevice *printer) const
    self.uglySide.call(
        'ritual_ZNK18QWidgetTextControl5printEP17QPagedPaintDevice',
        self._addressOf(printer, 'QPagedPaintDevice'),
    )

  def cut(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#cut
    """
    #  void QWidgetTextControl::cut()
    self.uglySide.call('ritual_ZN18QWidgetTextControl3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#copy
    """
    #  void QWidgetTextControl::copy()
    self.uglySide.call('ritual_ZN18QWidgetTextControl4copyEv')

  @overload()
  @overload(QClipboard.Mode)
  def paste(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::paste(QClipboard::Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#paste

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QWidgetTextControl::paste(QClipboard::Mode mode)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl5pasteEN10QClipboard4ModeE',
        mode.value,
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#undo
    """
    #  void QWidgetTextControl::undo()
    self.uglySide.call('ritual_ZN18QWidgetTextControl4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#redo
    """
    #  void QWidgetTextControl::redo()
    self.uglySide.call('ritual_ZN18QWidgetTextControl4redoEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#clear
    """
    #  void QWidgetTextControl::clear()
    self.uglySide.call('ritual_ZN18QWidgetTextControl5clearEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#selectAll
    """
    #  void QWidgetTextControl::selectAll()
    self.uglySide.call('ritual_ZN18QWidgetTextControl9selectAllEv')

  @overload(str)
  def insertPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::insertPlainText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#insertPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::insertPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl15insertPlainTextERK7QString', text,
    )

  @overload(str)
  def insertHtml(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::insertHtml(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#insertHtml

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::insertHtml(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl10insertHtmlERK7QString', text,
    )

  @overload(str)
  def append(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::append(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#append

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::append(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl6appendERK7QString', text,
    )

  @overload(str)
  def appendHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::appendHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#appendHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::appendHtml(const QString &html)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl10appendHtmlERK7QString', html,
    )

  @overload(str)
  def appendPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::appendPlainText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#appendPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetTextControl::appendPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl15appendPlainTextERK7QString', text,
    )

  def adjustSize(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::adjustSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#adjustSize
    """
    #  void QWidgetTextControl::adjustSize()
    self.uglySide.call('ritual_ZN18QWidgetTextControl10adjustSizeEv')

  @overload(QEvent, QTransform)
  @overload(NoneType, QTransform)
  @overload(QEvent, QTransform, QWidget)
  @overload(QEvent, QTransform, NoneType)
  @overload(NoneType, QTransform, QWidget)
  @overload(NoneType, QTransform, NoneType)
  def processEvent(
      self,
      e: Optional[QEvent],
      transform: QTransform,
      contextWidget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::processEvent(QEvent *e, const
    QTransform &transform, QWidget *contextWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#processEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    contextWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetTextControl::processEvent(QEvent *e, const QTransform
    #      &transform, QWidget *contextWidget)
    ritual = (
        'ritual_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransform'
        'P7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWidgetTextControl12processEventEP6QEventRK10QTra'
          'nsformP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(e), self._valueOf(transform),
        self._addressOf(contextWidget),
    )

  @overload(QEvent)
  @overload(NoneType)
  @overload(QEvent, QPointF)
  @overload(NoneType, QPointF)
  @overload(QEvent, QPointF, QWidget)
  @overload(QEvent, QPointF, NoneType)
  @overload(NoneType, QPointF, QWidget)
  @overload(NoneType, QPointF, NoneType)
  def processEvent(
      self,
      e: Optional[QEvent],
      coordinateOffset: Optional[QPointF] = None,
      contextWidget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::processEvent(QEvent *e, const
    QPointF &coordinateOffset, QWidget *contextWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#processEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coordinateOffset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    contextWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetTextControl::processEvent(QEvent *e, const QPointF
    #      &coordinateOffset, QWidget *contextWidget)
    if coordinateOffset is None:
      from ..QtCore import QPointF
      coordinateOffset = QPointF()
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl12processEventEP6QEventRK7QPointFP7QW'
        'idget',
        self._addressOf(e), self._valueOf(coordinateOffset),
        self._addressOf(contextWidget),
    )

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  @overload(QPainter, QRectF, QWidget)
  @overload(QPainter, QRectF, NoneType)
  @overload(NoneType, QRectF, QWidget)
  @overload(NoneType, QRectF, NoneType)
  def drawContents(
      self,
      painter: Optional[QPainter],
      rect: Optional[QRectF] = None,
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::drawContents(QPainter *painter,
    const QRectF &rect, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#drawContents

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetTextControl::drawContents(QPainter *painter, const QRectF
    #      &rect, QWidget *widget)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN18QWidgetTextControl12drawContentsEP8QPainterRK6QRectFP7Q'
        'Widget',
        self._addressOf(painter), self._valueOf(rect),
        self._addressOf(widget),
    )

  @overload(QMimeData)
  @overload(NoneType)
  def insertFromMimeData(self, source: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::insertFromMimeData(const QMimeData
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrol.html#insertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControl::insertFromMimeData(const QMimeData *source)
    ritual = 'ritual_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeDa'
          'ta')
    self.uglySide.call(ritual, self._addressOf(source))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QWidgetTextControl::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControl::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN18QWidgetTextControl10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWidgetTextControl10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControl::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgettextcontrol.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetTextControl::event(QEvent *e)
    ritual = 'ritual_ZN18QWidgetTextControl5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWidgetTextControl5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))
