"""
QQuickTextControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from ..QtGui import QClipboard, QInputControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QMimeData, QPointF, QRectF
  from ..QtCore import QTimerEvent, QVariant
  from ..QtGui import QTextBlock, QTextCharFormat, QTextCursor, QTextDocument
  from ..QtGui import QTransform
  from . import QQuickTextControlPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMimeData = WAIT['QMimeData']
  QPointF = WAIT['QPointF']
  QTextBlock = WAIT['QTextBlock']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextCursor = WAIT['QTextCursor']
  QTimerEvent = WAIT['QTimerEvent']
  QTransform = WAIT['QTransform']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextControl(QInputControl):
  """
  The cute side of Qt's QQuickTextControl: a plain Python object standing in
  front of one C++ QQuickTextControl.

  It is built on the cute 'QInputControl', as Qt's QQuickTextControl is built
  on Qt's QInputControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextControl that has a ritual and that Python
  can call so far, 59 names in all: 'metaObject', 'd_func', 'document',
  'textCursor', 'textInteractionFlags', 'toPlainText', 'toHtml',
  'toMarkdown', 'hasImState', 'overwriteMode', 'cursorVisible', 'anchorRect',
  'cursorRect', 'hoveredLink', 'anchorAt', 'blockWithMarkerAt',
  'setAcceptRichText', 'canPaste', 'setWordSelectionEnabled',
  'setTouchDragSelectionEnabled', 'hitTest', 'blockBoundingRect',
  'preeditText', 'setPlainText', 'setMarkdownText', 'setHtml', 'cut', 'copy',
  'paste', 'undo', 'redo', 'clear', 'selectAll', 'textChanged',
  'preeditTextChanged', 'contentsChange', 'undoAvailable', 'redoAvailable',
  'currentCharFormatChanged', 'copyAvailable', 'selectionChanged',
  'cursorPositionChanged', 'overwriteModeChanged', 'updateCursorRequest',
  'updateRequest', 'cursorRectangleChanged', 'linkActivated', 'linkHovered',
  'markerClicked', 'markerHovered', 'processEvent', 'inputMethodQuery',
  'createMimeDataFromSelection', 'canInsertFromMimeData',
  'insertFromMimeData', 'cursorOn', 'isBeingEdited', 'timerEvent', 'event'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextControl::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTextControl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickTextControlPrivate *QQuickTextControl::d_func() const':
    takes in Python what 'QQuickTextControlPrivate
    *QQuickTextControl::d_func()' takes.
  - Qt's 'QQuickTextControl::~QQuickTextControl()': the destructor: Python
    never removes a C++ QQuickTextControl.

  What has no ritual
  ------------------

  17 of the 83 functions Qt declares: 10 leans on 'QQuickTextControl; 3
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextControl is created at the first use, not by
    'QQuickTextControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextControl.
  - Qt tells when it has removed the C++ QQuickTextControl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTextControl that has no cute function yet,
    '__init__', 'moveCursor', 'selectionRect', 'setCursorIsFocusIndicator',
    'setCursorVisible', 'setCursorWidth', 'setDocument', 'setOverwriteMode',
    'setTextCursor', 'setTextInteractionFlags', 'updateCursorRectangle',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextControl'

  #  A C++ QQuickTextControl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextControl'

  #  The functions Qt calls itself that QQuickTextControl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'hitTest': (
          ('_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracy'
           'E',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('int', 'enum', 'QtCore:Qt.HitTestAccuracy'),
           )),
      ),
      'blockBoundingRect': (
          ('_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
      'processEvent': (
          ('_ZN17QQuickTextControl12processEventEP6QEventRK10QTransform',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQuer'
           'yE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'createMimeDataFromSelection': (
          ('_ZNK17QQuickTextControl27createMimeDataFromSelectionEv',
           ('address', 'address', 'QtCore:QMimeData'),
           ()),
      ),
      'canInsertFromMimeData': (
          ('_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
      'insertFromMimeData': (
          ('_ZN17QQuickTextControl18insertFromMimeDataEPK9QMimeData',
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
    Calls Qt's 'const QMetaObject *QQuickTextControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QQuickTextControl::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QQuickTextControl::document() const
    address = self.uglySide.call('ritual_ZNK17QQuickTextControl8documentEv')
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QQuickTextControl::textCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QQuickTextControl::textCursor() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl10textCursorEv',
    )
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags
    QQuickTextControl::textInteractionFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QQuickTextControl::textInteractionFlags()
    #      const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK17QQuickTextControl20textInteractionFlagsEv',
    ))

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::toPlainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextControl::toPlainText() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl11toPlainTextEv')

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextControl::toHtml() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl6toHtmlEv')

  def toMarkdown(self) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::toMarkdown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#toMarkdown

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextControl::toMarkdown() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl10toMarkdownEv')

  def hasImState(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::hasImState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#hasImState
    """
    #  bool QQuickTextControl::hasImState() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl10hasImStateEv')

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::overwriteMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#overwriteMode
    """
    #  bool QQuickTextControl::overwriteMode() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextControl13overwriteModeEv',
    )

  def cursorVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::cursorVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorVisible
    """
    #  bool QQuickTextControl::cursorVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextControl13cursorVisibleEv',
    )

  def anchorRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextControl::anchorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#anchorRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextControl::anchorRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl10anchorRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextCursor)
  def cursorRect(self, cursor: QTextCursor) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextControl::cursorRect(const QTextCursor
    &cursor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorRect

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
    #  QRectF QQuickTextControl::cursorRect(const QTextCursor &cursor) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl10cursorRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  def cursorRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextControl::cursorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextControl::cursorRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl10cursorRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def hoveredLink(self) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::hoveredLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#hoveredLink

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextControl::hoveredLink() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl11hoveredLinkEv')

  @overload(QPointF)
  def anchorAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::anchorAt(const QPointF &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#anchorAt

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
    #  QString QQuickTextControl::anchorAt(const QPointF &pos) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextControl8anchorAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def blockWithMarkerAt(self, pos: QPointF) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QQuickTextControl::blockWithMarkerAt(const QPointF
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#blockWithMarkerAt

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
    #  QTextBlock QQuickTextControl::blockWithMarkerAt(const QPointF &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl17blockWithMarkerAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtGui import QTextBlock
    return QTextBlock._cuteOwning(address)

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#canPaste
    """
    #  bool QQuickTextControl::canPaste() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl8canPasteEv')

  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(self, point: QPointF, accuracy: Qt.HitTestAccuracy) -> int:
    """
    Calls Qt's 'int QQuickTextControl::hitTest(const QPointF &point,
    Qt::HitTestAccuracy accuracy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#hitTest

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    accuracy : Qt.HitTestAccuracy
      Passed on as its number.
    """
    #  int QQuickTextControl::hitTest(const QPointF &point,
    #      Qt::HitTestAccuracy accuracy) const
    ritual = (
        'ritual_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccur'
        'acyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTes'
          'tAccuracyE')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), accuracy.value,
    )

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextControl::blockBoundingRect(const QTextBlock
    &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#blockBoundingRect

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
    #  QRectF QQuickTextControl::blockBoundingRect(const QTextBlock &block)
    #      const
    ritual = (
        'ritual_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBl'
          'ock')
    address = self.uglySide.call(ritual, self._valueOf(block))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def preeditText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextControl::preeditText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#preeditText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextControl::preeditText() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl11preeditTextEv')

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, property: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery property)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery
    #      property) const
    ritual = (
        'ritual_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputM'
          'ethodQueryE')
    address = self.uglySide.call(ritual, property.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery query, const
    QVariant &argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery
    #      query, const QVariant &argument) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryERK8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def createMimeDataFromSelection(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QQuickTextControl::createMimeDataFromSelection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#createMimeDataFromSelection

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QQuickTextControl::createMimeDataFromSelection() const
    ritual = 'ritual_ZNK17QQuickTextControl27createMimeDataFromSelectionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickTextControl27createMimeDataFromSelectionEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QMimeData)
  @overload(NoneType)
  def canInsertFromMimeData(self, source: Optional[QMimeData]) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::canInsertFromMimeData(const QMimeData
    *source) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#canInsertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextControl::canInsertFromMimeData(const QMimeData *source)
    #      const
    ritual = (
        'ritual_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMim'
          'eData')
    return self.uglySide.call(ritual, self._addressOf(source))

  def cursorOn(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::cursorOn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorOn
    """
    #  bool QQuickTextControl::cursorOn() const
    return self.uglySide.call('ritual_ZNK17QQuickTextControl8cursorOnEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAcceptRichText(self, accept: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setAcceptRichText(bool accept)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#setAcceptRichText

    Parameters
    ----------

    accept : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::setAcceptRichText(bool accept)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl17setAcceptRichTextEb', accept,
    )

  @overload(bool)
  def setWordSelectionEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setWordSelectionEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#setWordSelectionEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::setWordSelectionEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl23setWordSelectionEnabledEb', enabled,
    )

  @overload(bool)
  def setTouchDragSelectionEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setTouchDragSelectionEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::setTouchDragSelectionEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl28setTouchDragSelectionEnabledEb',
        enabled,
    )

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setPlainText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextControl::setPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl12setPlainTextERK7QString', text,
    )

  @overload(str)
  def setMarkdownText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setMarkdownText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#setMarkdownText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextControl::setMarkdownText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl15setMarkdownTextERK7QString', text,
    )

  @overload(str)
  def setHtml(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextControl::setHtml(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#setHtml

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextControl::setHtml(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl7setHtmlERK7QString', text,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickTextControl::QQuickTextControl(QTextDocument *doc, QObject
    *parent)': leans on 'QQuickTextControl::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.__init__' has no cute function yet. Qt's "
        "'QQuickTextControl::QQuickTextControl(QTextDocument *doc, QObject "
        "*parent)': leans on "
        "'QQuickTextControl::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def d_func(self) -> Optional[QQuickTextControlPrivate]:
    """
    Calls Qt's 'QQuickTextControlPrivate *QQuickTextControl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#d_func

    Returns
    -------

    Optional[QQuickTextControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextControlPrivate *QQuickTextControl::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickTextControl6d_funcEv')
    from . import QQuickTextControlPrivate
    return QQuickTextControlPrivate._cuteAt(address)

  def cut(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#cut
    """
    #  void QQuickTextControl::cut()
    self.uglySide.call('ritual_ZN17QQuickTextControl3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#copy
    """
    #  void QQuickTextControl::copy()
    self.uglySide.call('ritual_ZN17QQuickTextControl4copyEv')

  @overload()
  @overload(QClipboard.Mode)
  def paste(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QQuickTextControl::paste(QClipboard::Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#paste

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QQuickTextControl::paste(QClipboard::Mode mode)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl5pasteEN10QClipboard4ModeE', mode.value,
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#undo
    """
    #  void QQuickTextControl::undo()
    self.uglySide.call('ritual_ZN17QQuickTextControl4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#redo
    """
    #  void QQuickTextControl::redo()
    self.uglySide.call('ritual_ZN17QQuickTextControl4redoEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#clear
    """
    #  void QQuickTextControl::clear()
    self.uglySide.call('ritual_ZN17QQuickTextControl5clearEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#selectAll
    """
    #  void QQuickTextControl::selectAll()
    self.uglySide.call('ritual_ZN17QQuickTextControl9selectAllEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#textChanged
    """
    #  void QQuickTextControl::textChanged()
    self.uglySide.call('ritual_ZN17QQuickTextControl11textChangedEv')

  def preeditTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::preeditTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#preeditTextChanged
    """
    #  void QQuickTextControl::preeditTextChanged()
    self.uglySide.call('ritual_ZN17QQuickTextControl18preeditTextChangedEv')

  @overload(int, int, int)
  def contentsChange(
      self,
      from_: int,
      charsRemoved: int,
      charsAdded: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextControl::contentsChange(int from, int
    charsRemoved, int charsAdded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#contentsChange

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    charsRemoved : int
      Passed on as it is.

    charsAdded : int
      Passed on as it is.
    """
    #  void QQuickTextControl::contentsChange(int from, int charsRemoved, int
    #      charsAdded)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl14contentsChangeEiii',
        from_, charsRemoved, charsAdded,
    )

  @overload(bool)
  def undoAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::undoAvailable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#undoAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::undoAvailable(bool b)
    self.uglySide.call('ritual_ZN17QQuickTextControl13undoAvailableEb', b)

  @overload(bool)
  def redoAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::redoAvailable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#redoAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::redoAvailable(bool b)
    self.uglySide.call('ritual_ZN17QQuickTextControl13redoAvailableEb', b)

  @overload(QTextCharFormat)
  def currentCharFormatChanged(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QQuickTextControl::currentCharFormatChanged(const
    QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#currentCharFormatChanged

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QQuickTextControl::currentCharFormatChanged(const QTextCharFormat
    #      &format)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl24currentCharFormatChangedERK15QTextCh'
        'arFormat',
        self._valueOf(format),
    )

  @overload(bool)
  def copyAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::copyAvailable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#copyAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::copyAvailable(bool b)
    self.uglySide.call('ritual_ZN17QQuickTextControl13copyAvailableEb', b)

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#selectionChanged
    """
    #  void QQuickTextControl::selectionChanged()
    self.uglySide.call('ritual_ZN17QQuickTextControl16selectionChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorPositionChanged
    """
    #  void QQuickTextControl::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl21cursorPositionChangedEv',
    )

  @overload(bool)
  def overwriteModeChanged(self, overwriteMode: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::overwriteModeChanged(bool
    overwriteMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#overwriteModeChanged

    Parameters
    ----------

    overwriteMode : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::overwriteModeChanged(bool overwriteMode)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl20overwriteModeChangedEb',
        overwriteMode,
    )

  def updateCursorRequest(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::updateCursorRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#updateCursorRequest
    """
    #  void QQuickTextControl::updateCursorRequest()
    self.uglySide.call('ritual_ZN17QQuickTextControl19updateCursorRequestEv')

  def updateRequest(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::updateRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#updateRequest
    """
    #  void QQuickTextControl::updateRequest()
    self.uglySide.call('ritual_ZN17QQuickTextControl13updateRequestEv')

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#cursorRectangleChanged
    """
    #  void QQuickTextControl::cursorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl22cursorRectangleChangedEv',
    )

  @overload(str)
  def linkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickTextControl::linkActivated(const QString &link)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#linkActivated

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextControl::linkActivated(const QString &link)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl13linkActivatedERK7QString', link,
    )

  @overload(str)
  def linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickTextControl::linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextControl::linkHovered(const QString &link)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl11linkHoveredERK7QString', link,
    )

  def markerClicked(self) -> None:
    """
    Calls Qt's 'void QQuickTextControl::markerClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#markerClicked
    """
    #  void QQuickTextControl::markerClicked()
    self.uglySide.call('ritual_ZN17QQuickTextControl13markerClickedEv')

  @overload(bool)
  def markerHovered(self, marker: bool) -> None:
    """
    Calls Qt's 'void QQuickTextControl::markerHovered(bool marker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#markerHovered

    Parameters
    ----------

    marker : bool
      Passed on as it is.
    """
    #  void QQuickTextControl::markerHovered(bool marker)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl13markerHoveredEb', marker,
    )

  @overload(QEvent, QTransform)
  @overload(NoneType, QTransform)
  def processEvent(self, e: Optional[QEvent], transform: QTransform) -> None:
    """
    Calls Qt's 'void QQuickTextControl::processEvent(QEvent *e, const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#processEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QQuickTextControl::processEvent(QEvent *e, const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl12processEventEP6QEventRK10QTransform',
        self._addressOf(e), self._valueOf(transform),
    )

  @overload(QEvent)
  @overload(NoneType)
  @overload(QEvent, QPointF)
  @overload(NoneType, QPointF)
  def processEvent(
      self,
      e: Optional[QEvent],
      coordinateOffset: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextControl::processEvent(QEvent *e, const QPointF
    &coordinateOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#processEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coordinateOffset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QQuickTextControl::processEvent(QEvent *e, const QPointF
    #      &coordinateOffset)
    if coordinateOffset is None:
      from ..QtCore import QPointF
      coordinateOffset = QPointF()
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl12processEventEP6QEventRK7QPointF',
        self._addressOf(e), self._valueOf(coordinateOffset, 'QPointF'),
    )

  @overload(QMimeData)
  @overload(NoneType)
  def insertFromMimeData(self, source: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QQuickTextControl::insertFromMimeData(const QMimeData
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#insertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextControl::insertFromMimeData(const QMimeData *source)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl18insertFromMimeDataEPK9QMimeData',
        self._addressOf(source),
    )

  def isBeingEdited(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::isBeingEdited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrol.html#isBeingEdited
    """
    #  bool QQuickTextControl::isBeingEdited()
    return self.uglySide.call(
        'ritual_ZN17QQuickTextControl13isBeingEditedEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextControl::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextControl::timerEvent(QTimerEvent *e)
    self.uglySide.call(
        'ritual_ZN17QQuickTextControl10timerEventEP11QTimerEvent',
        self._addressOf(e),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickTextControl::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextcontrol.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextControl::event(QEvent *e)
    ritual = 'ritual_ZN17QQuickTextControl5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickTextControl5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def moveCursor(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::moveCursor(QTextCursor::MoveOperation op,
    QTextCursor::MoveMode mode)': leans on
    'QQuickTextControl::cursorPositionChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.moveCursor' has no cute function yet. Qt's "
        "'void QQuickTextControl::moveCursor(QTextCursor::MoveOperation op, "
        "QTextCursor::MoveMode mode)': leans on "
        "'QQuickTextControl::cursorPositionChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def selectionRect(*__, **_) -> Never:
    """
    - Qt's 'QRectF QQuickTextControl::selectionRect(const QTextCursor
      &cursor) const': cannot be called and cannot be called through the
      meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    - Qt's 'QRectF QQuickTextControl::selectionRect() const': cannot be
      called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextControl.selectionRect' has no cute function yet. Qt's "
        "'QRectF QQuickTextControl::selectionRect(const QTextCursor "
        "&cursor) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's 'QRectF QQuickTextControl::selectionRect() "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setCursorIsFocusIndicator(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setCursorIsFocusIndicator(bool b)': leans
    on 'QQuickTextControl::updateCursorRequest()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setCursorIsFocusIndicator' has no cute function "
        "yet. Qt's 'void QQuickTextControl::setCursorIsFocusIndicator(bool "
        "b)': leans on 'QQuickTextControl::updateCursorRequest()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setCursorVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setCursorVisible(bool visible)': leans on
    'QQuickTextControl::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setCursorVisible' has no cute function yet. "
        "Qt's 'void QQuickTextControl::setCursorVisible(bool visible)': "
        "leans on 'QQuickTextControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setCursorWidth(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setCursorWidth(int width)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setCursorWidth' has no cute function yet. Qt's "
        "'void QQuickTextControl::setCursorWidth(int width)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setDocument(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setDocument(QTextDocument *doc)': leans on
    'QQuickTextControl::textChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setDocument' has no cute function yet. Qt's "
        "'void QQuickTextControl::setDocument(QTextDocument *doc)': leans "
        "on 'QQuickTextControl::textChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setOverwriteMode(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setOverwriteMode(bool overwrite)': leans on
    'QQuickTextControl::overwriteModeChanged(bool)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setOverwriteMode' has no cute function yet. "
        "Qt's 'void QQuickTextControl::setOverwriteMode(bool overwrite)': "
        "leans on 'QQuickTextControl::overwriteModeChanged(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setTextCursor(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::setTextCursor(const QTextCursor &cursor)':
    leans on 'QQuickTextControl::cursorPositionChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setTextCursor' has no cute function yet. Qt's "
        "'void QQuickTextControl::setTextCursor(const QTextCursor "
        "&cursor)': leans on 'QQuickTextControl::cursorPositionChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setTextInteractionFlags(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTextControl::setTextInteractionFlags(Qt::TextInteractionFlags
    flags)': leans on 'QQuickTextControl::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.setTextInteractionFlags' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextControl::setTextInteractionFlags(Qt::TextInteractionFlags"
        " flags)': leans on 'QQuickTextControl::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateCursorRectangle(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControl::updateCursorRectangle(bool force)': leans
    on 'QQuickTextControl::cursorRectangleChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControl.updateCursorRectangle' has no cute function "
        "yet. Qt's 'void QQuickTextControl::updateCursorRectangle(bool "
        "force)': leans on 'QQuickTextControl::cursorRectangleChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
