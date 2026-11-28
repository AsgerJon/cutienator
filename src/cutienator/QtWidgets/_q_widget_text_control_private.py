"""
QWidgetTextControlPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWidgetTextControlPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QObjectPrivate
from ..QtGui import QTextCursor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMimeData, QObject, QPoint, QPointF, QRectF
  from ..QtGui import QFocusEvent, QInputMethodEvent, QKeyEvent, QTextBlock
  from ..QtGui import QTextDocument
  from . import QWidget, QWidgetTextControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMimeData = WAIT['QMimeData']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetTextControlPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWidgetTextControlPrivate: a plain Python object
  standing in front of one C++ QWidgetTextControlPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWidgetTextControlPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetTextControlPrivate that has a ritual and that
  Python can call so far, 49 names in all: 'q_func',
  'updateCurrentCharFormat', 'indent', 'outdent', 'gotoNextTableCell',
  'gotoPreviousTableCell', 'createAutoBulletList', 'init', 'setContent',
  'startDrag', 'setCursorPosition', 'repaintCursor', 'repaintSelection',
  'repaintOldAndNewSelection', 'selectionChanged',
  '_q_updateCurrentCharFormatAndSelection', 'setClipboardSelection',
  '_q_emitCursorPosChanged', '_q_contentsChanged', 'setCursorVisible',
  'updateCursorBlinking', 'extendBlockwiseSelection', '_q_deleteSelected',
  'cursorRectPlusUnicodeDirectionMarkers', 'rectForPosition',
  'anchorForCursor', 'updateHighlightedAnchor', 'resetHighlightedAnchor',
  'keyPressEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'sendMouseEventToInputContext', 'contextMenuEvent', 'focusEvent',
  'dragEnterEvent', 'dragLeaveEvent', 'dragMoveEvent', 'dropEvent',
  'inputMethodEvent', 'activateLinkUnderCursor', 'showToolTip',
  'isPreediting', 'commitPreedit', 'insertParagraphSeparator', 'append',
  '_q_copyLink', '_q_updateBlock', '_q_documentLayoutChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWidgetTextControl *QWidgetTextControlPrivate::q_func()
    const': takes in Python what 'QWidgetTextControl
    *QWidgetTextControlPrivate::q_func()' takes.

  What has no ritual
  ------------------

  8 of the 60 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied; 3 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QWidgetTextControlPrivate.

  What to expect
  --------------

  - The C++ QWidgetTextControlPrivate is created at the first use, not by
    'QWidgetTextControlPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetTextControlPrivate.
  - Each name of Qt's QWidgetTextControlPrivate that has no cute function
    yet, '_q_setCursorAfterUndoRedo', 'cursorMoveKeyEvent',
    'extendWordwiseSelection', 'mouseDoubleClickEvent', 'paste',
    'selectionRect', 'setBlinkingCursorEnabled', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetTextControlPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextCursor)
  def cursorRectPlusUnicodeDirectionMarkers(
      self,
      cursor: QTextCursor,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QWidgetTextControlPrivate::cursorRectPlusUnicodeDirectionMarkers(const
    QTextCursor &cursor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

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
    #  QRectF
    #      QWidgetTextControlPrivate::cursorRectPlusUnicodeDirectionMarkers(
    #      const QTextCursor &cursor) const
    address = self.uglySide.call(
        'ritual_ZNK25QWidgetTextControlPrivate37cursorRectPlusUnicodeDirect'
        'ionMarkersERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(int)
  def rectForPosition(self, position: int) -> QRectF:
    """
    Calls Qt's 'QRectF QWidgetTextControlPrivate::rectForPosition(int
    position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#rectForPosition

    Parameters
    ----------

    position : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetTextControlPrivate::rectForPosition(int position) const
    address = self.uglySide.call(
        'ritual_ZNK25QWidgetTextControlPrivate15rectForPositionEi', position,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextCursor)
  def anchorForCursor(self, anchor: QTextCursor) -> str:
    """
    Calls Qt's 'QString QWidgetTextControlPrivate::anchorForCursor(const
    QTextCursor &anchor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#anchorForCursor

    Parameters
    ----------

    anchor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetTextControlPrivate::anchorForCursor(const QTextCursor
    #      &anchor) const
    return self.uglySide.call(
        'ritual_ZNK25QWidgetTextControlPrivate15anchorForCursorERK11QTextCu'
        'rsor',
        self._valueOf(anchor),
    )

  def isPreediting(self) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControlPrivate::isPreediting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#isPreediting
    """
    #  bool QWidgetTextControlPrivate::isPreediting() const
    return self.uglySide.call(
        'ritual_ZNK25QWidgetTextControlPrivate12isPreeditingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(Qt.TextFormat)
  @overload(Qt.TextFormat, str)
  @overload(Qt.TextFormat, str, QTextDocument)
  @overload(Qt.TextFormat, str, NoneType)
  def setContent(
      self,
      format: Qt.TextFormat = Qt.TextFormat.RichText,
      text: str = '',
      document: Optional[QTextDocument] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::setContent(Qt::TextFormat
    format, const QString &text, QTextDocument *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#setContent

    Parameters
    ----------

    format : Qt.TextFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TextFormat.RichText.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetTextControlPrivate::setContent(Qt::TextFormat format,
    #      const QString &text, QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate10setContentEN2Qt10TextFormatE'
        'RK7QStringP13QTextDocument',
        format.value, text, self._addressOf(document),
    )

  @overload(QPointF)
  def setCursorPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::setCursorPosition(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#setCursorPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::setCursorPosition(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate17setCursorPositionERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(int)
  @overload(int, QTextCursor.MoveMode)
  def setCursorPosition(
      self,
      pos: int,
      mode: QTextCursor.MoveMode = QTextCursor.MoveMode.MoveAnchor,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::setCursorPosition(int pos,
    QTextCursor::MoveMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#setCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  void QWidgetTextControlPrivate::setCursorPosition(int pos,
    #      QTextCursor::MoveMode mode)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate17setCursorPositionEiN11QTextC'
        'ursor8MoveModeE',
        pos, mode.value,
    )

  def setClipboardSelection(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::setClipboardSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::setClipboardSelection()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate21setClipboardSelectionEv',
    )

  @overload(bool)
  def setCursorVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::setCursorVisible(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#setCursorVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWidgetTextControlPrivate::setCursorVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate16setCursorVisibleEb', visible,
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
    Notes what was given, for Qt's
    'QWidgetTextControlPrivate::QWidgetTextControlPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  QWidgetTextControlPrivate::QWidgetTextControlPrivate()
    self._noteCreation(QWidgetTextControlPrivate, lambda: Rituals.call(
        'ritual_ZN25QWidgetTextControlPrivateC1Ev',
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

  def q_func(self) -> Optional[QWidgetTextControl]:
    """
    Calls Qt's 'QWidgetTextControl *QWidgetTextControlPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#q_func

    Returns
    -------

    Optional[QWidgetTextControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidgetTextControl *QWidgetTextControlPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate6q_funcEv',
    )
    from . import QWidgetTextControl
    return QWidgetTextControl._cuteAt(address)

  def updateCurrentCharFormat(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::updateCurrentCharFormat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::updateCurrentCharFormat()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate23updateCurrentCharFormatEv',
    )

  def indent(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::indent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#indent
    """
    #  void QWidgetTextControlPrivate::indent()
    self.uglySide.call('ritual_ZN25QWidgetTextControlPrivate6indentEv')

  def outdent(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::outdent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#outdent
    """
    #  void QWidgetTextControlPrivate::outdent()
    self.uglySide.call('ritual_ZN25QWidgetTextControlPrivate7outdentEv')

  def gotoNextTableCell(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::gotoNextTableCell()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#gotoNextTableCell
    """
    #  void QWidgetTextControlPrivate::gotoNextTableCell()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate17gotoNextTableCellEv',
    )

  def gotoPreviousTableCell(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::gotoPreviousTableCell()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::gotoPreviousTableCell()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate21gotoPreviousTableCellEv',
    )

  def createAutoBulletList(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::createAutoBulletList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::createAutoBulletList()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate20createAutoBulletListEv',
    )

  @overload()
  @overload(Qt.TextFormat)
  @overload(Qt.TextFormat, str)
  @overload(Qt.TextFormat, str, QTextDocument)
  @overload(Qt.TextFormat, str, NoneType)
  def init(
      self,
      format: Qt.TextFormat = Qt.TextFormat.RichText,
      text: str = '',
      document: Optional[QTextDocument] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::init(Qt::TextFormat format,
    const QString &text, QTextDocument *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#init

    Parameters
    ----------

    format : Qt.TextFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TextFormat.RichText.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetTextControlPrivate::init(Qt::TextFormat format, const
    #      QString &text, QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate4initEN2Qt10TextFormatERK7QStr'
        'ingP13QTextDocument',
        format.value, text, self._addressOf(document),
    )

  def startDrag(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::startDrag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#startDrag
    """
    #  void QWidgetTextControlPrivate::startDrag()
    self.uglySide.call('ritual_ZN25QWidgetTextControlPrivate9startDragEv')

  def repaintCursor(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::repaintCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#repaintCursor
    """
    #  void QWidgetTextControlPrivate::repaintCursor()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate13repaintCursorEv',
    )

  def repaintSelection(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::repaintSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#repaintSelection
    """
    #  void QWidgetTextControlPrivate::repaintSelection()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate16repaintSelectionEv',
    )

  @overload(QTextCursor)
  def repaintOldAndNewSelection(self, oldSelection: QTextCursor) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControlPrivate::repaintOldAndNewSelection(const QTextCursor
    &oldSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    oldSelection : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QWidgetTextControlPrivate::repaintOldAndNewSelection(const
    #      QTextCursor &oldSelection)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate25repaintOldAndNewSelectionERK'
        '11QTextCursor',
        self._valueOf(oldSelection),
    )

  @overload()
  @overload(bool)
  def selectionChanged(
      self,
      forceEmitSelectionChanged: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::selectionChanged(bool
    forceEmitSelectionChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#selectionChanged

    Parameters
    ----------

    forceEmitSelectionChanged : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetTextControlPrivate::selectionChanged(bool
    #      forceEmitSelectionChanged)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate16selectionChangedEb',
        forceEmitSelectionChanged,
    )

  def _q_updateCurrentCharFormatAndSelection(self) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControlPrivate::_q_updateCurrentCharFormatAndSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void
    #      QWidgetTextControlPrivate::_q_updateCurrentCharFormatAndSelection(
    #      )
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate38_q_updateCurrentCharFormatAn'
        'dSelectionEv',
    )

  @overload(QTextCursor)
  def _q_emitCursorPosChanged(self, someCursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_emitCursorPosChanged(const
    QTextCursor &someCursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    someCursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QWidgetTextControlPrivate::_q_emitCursorPosChanged(const
    #      QTextCursor &someCursor)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate23_q_emitCursorPosChangedERK11'
        'QTextCursor',
        self._valueOf(someCursor),
    )

  @overload(int, int, int)
  def _q_contentsChanged(
      self,
      from_: int,
      charsRemoved: int,
      charsAdded: int,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_contentsChanged(int from,
    int charsRemoved, int charsAdded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#_q_contentsChanged

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    charsRemoved : int
      Passed on as it is.

    charsAdded : int
      Passed on as it is.
    """
    #  void QWidgetTextControlPrivate::_q_contentsChanged(int from, int
    #      charsRemoved, int charsAdded)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate18_q_contentsChangedEiii',
        from_, charsRemoved, charsAdded,
    )

  def updateCursorBlinking(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::updateCursorBlinking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::updateCursorBlinking()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate20updateCursorBlinkingEv',
    )

  @overload(int)
  def extendBlockwiseSelection(self, suggestedNewPosition: int) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::extendBlockwiseSelection(int
    suggestedNewPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    suggestedNewPosition : int
      Passed on as it is.
    """
    #  void QWidgetTextControlPrivate::extendBlockwiseSelection(int
    #      suggestedNewPosition)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate24extendBlockwiseSelectionEi',
        suggestedNewPosition,
    )

  def _q_deleteSelected(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_deleteSelected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#_q_deleteSelected
    """
    #  void QWidgetTextControlPrivate::_q_deleteSelected()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate17_q_deleteSelectedEv',
    )

  @overload(QPointF)
  def updateHighlightedAnchor(self, mousePos: QPointF) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControlPrivate::updateHighlightedAnchor(QPointF mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    mousePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::updateHighlightedAnchor(QPointF
    #      mousePos)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate23updateHighlightedAnchorE7QPo'
        'intF',
        self._valueOf(mousePos, 'QPointF'),
    )

  def resetHighlightedAnchor(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::resetHighlightedAnchor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::resetHighlightedAnchor()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate22resetHighlightedAnchorEv',
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::keyPressEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#keyPressEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControlPrivate::keyPressEvent(QKeyEvent *e)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate13keyPressEventEP9QKeyEvent',
        self._addressOf(e),
    )

  @overload(
      QEvent, Qt.MouseButton, QPointF, Qt.KeyboardModifiers, Qt.MouseButtons,
      QPointF,
  )
  @overload(
      NoneType, Qt.MouseButton, QPointF, Qt.KeyboardModifiers,
      Qt.MouseButtons, QPointF,
  )
  def mousePressEvent(
      self,
      e: Optional[QEvent],
      button: Qt.MouseButton,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      buttons: Qt.MouseButtons,
      globalPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::mousePressEvent(QEvent *e,
    Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::mousePressEvent(QEvent *e,
    #      Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    #      modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate15mousePressEventEP6QEventN2Qt'
        '11MouseButtonERK7QPointF6QFlagsINS2_16KeyboardModifierEES7_IS3_ES6'
        '_',
        self._addressOf(e), button.value, self._valueOf(pos, 'QPointF'),
        modifiers.value, buttons.value, self._valueOf(globalPos, 'QPointF'),
    )

  @overload(
      QEvent, Qt.MouseButton, QPointF, Qt.KeyboardModifiers, Qt.MouseButtons,
      QPointF,
  )
  @overload(
      NoneType, Qt.MouseButton, QPointF, Qt.KeyboardModifiers,
      Qt.MouseButtons, QPointF,
  )
  def mouseMoveEvent(
      self,
      e: Optional[QEvent],
      button: Qt.MouseButton,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      buttons: Qt.MouseButtons,
      globalPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::mouseMoveEvent(QEvent *e,
    Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::mouseMoveEvent(QEvent *e,
    #      Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    #      modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate14mouseMoveEventEP6QEventN2Qt1'
        '1MouseButtonERK7QPointF6QFlagsINS2_16KeyboardModifierEES7_IS3_ES6_',
        self._addressOf(e), button.value, self._valueOf(pos, 'QPointF'),
        modifiers.value, buttons.value, self._valueOf(globalPos, 'QPointF'),
    )

  @overload(
      QEvent, Qt.MouseButton, QPointF, Qt.KeyboardModifiers, Qt.MouseButtons,
      QPointF,
  )
  @overload(
      NoneType, Qt.MouseButton, QPointF, Qt.KeyboardModifiers,
      Qt.MouseButtons, QPointF,
  )
  def mouseReleaseEvent(
      self,
      e: Optional[QEvent],
      button: Qt.MouseButton,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      buttons: Qt.MouseButtons,
      globalPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::mouseReleaseEvent(QEvent *e,
    Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::mouseReleaseEvent(QEvent *e,
    #      Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    #      modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate17mouseReleaseEventEP6QEventN2'
        'Qt11MouseButtonERK7QPointF6QFlagsINS2_16KeyboardModifierEES7_IS3_E'
        'S6_',
        self._addressOf(e), button.value, self._valueOf(pos, 'QPointF'),
        modifiers.value, buttons.value, self._valueOf(globalPos, 'QPointF'),
    )

  @overload(
      QEvent, QEvent.Type, Qt.MouseButton, QPointF, Qt.KeyboardModifiers,
      Qt.MouseButtons, QPointF,
  )
  @overload(
      NoneType, QEvent.Type, Qt.MouseButton, QPointF, Qt.KeyboardModifiers,
      Qt.MouseButtons, QPointF,
  )
  def sendMouseEventToInputContext(
      self,
      e: Optional[QEvent],
      eventType: QEvent.Type,
      button: Qt.MouseButton,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      buttons: Qt.MouseButtons,
      globalPos: QPointF,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWidgetTextControlPrivate::sendMouseEventToInputContext(QEvent *e,
    QEvent::Type eventType, Qt::MouseButton button, const QPointF &pos,
    Qt::KeyboardModifiers modifiers, Qt::MouseButtons buttons, const QPointF
    &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    eventType : QEvent.Type
      Passed on as its number.

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QWidgetTextControlPrivate::sendMouseEventToInputContext(QEvent
    #      *e, QEvent::Type eventType, Qt::MouseButton button, const QPointF
    #      &pos, Qt::KeyboardModifiers modifiers, Qt::MouseButtons buttons,
    #      const QPointF &globalPos)
    return self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate28sendMouseEventToInputContext'
        'EP6QEventNS0_4TypeEN2Qt11MouseButtonERK7QPointF6QFlagsINS3_16Keybo'
        'ardModifierEES8_IS4_ES7_',
        self._addressOf(e), eventType.value, button.value, self._valueOf(pos,
        'QPointF'), modifiers.value, buttons.value, self._valueOf(globalPos,
        'QPointF'),
    )

  @overload(QPointF, QPointF, QWidget)
  @overload(QPointF, QPointF, NoneType)
  def contextMenuEvent(
      self,
      screenPos: QPointF,
      docPos: QPointF,
      contextWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::contextMenuEvent(const
    QPointF &screenPos, const QPointF &docPos, QWidget *contextWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#contextMenuEvent

    Parameters
    ----------

    screenPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    docPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    contextWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControlPrivate::contextMenuEvent(const QPointF
    #      &screenPos, const QPointF &docPos, QWidget *contextWidget)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate16contextMenuEventERK7QPointFS'
        '2_P7QWidget',
        self._valueOf(screenPos, 'QPointF'), self._valueOf(docPos,
        'QPointF'), self._addressOf(contextWidget),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusEvent(self, e: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::focusEvent(QFocusEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#focusEvent

    Parameters
    ----------

    e : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControlPrivate::focusEvent(QFocusEvent *e)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate10focusEventEP11QFocusEvent',
        self._addressOf(e),
    )

  @overload(QEvent, QMimeData)
  @overload(QEvent, NoneType)
  @overload(NoneType, QMimeData)
  @overload(NoneType, NoneType)
  def dragEnterEvent(
      self,
      e: Optional[QEvent],
      mimeData: Optional[QMimeData],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControlPrivate::dragEnterEvent(QEvent *e,
    const QMimeData *mimeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#dragEnterEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetTextControlPrivate::dragEnterEvent(QEvent *e, const
    #      QMimeData *mimeData)
    return self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate14dragEnterEventEP6QEventPK9QM'
        'imeData',
        self._addressOf(e), self._addressOf(mimeData),
    )

  def dragLeaveEvent(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::dragLeaveEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#dragLeaveEvent
    """
    #  void QWidgetTextControlPrivate::dragLeaveEvent()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate14dragLeaveEventEv',
    )

  @overload(QEvent, QMimeData, QPointF)
  @overload(QEvent, NoneType, QPointF)
  @overload(NoneType, QMimeData, QPointF)
  @overload(NoneType, NoneType, QPointF)
  def dragMoveEvent(
      self,
      e: Optional[QEvent],
      mimeData: Optional[QMimeData],
      pos: QPointF,
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControlPrivate::dragMoveEvent(QEvent *e,
    const QMimeData *mimeData, const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QWidgetTextControlPrivate::dragMoveEvent(QEvent *e, const
    #      QMimeData *mimeData, const QPointF &pos)
    return self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate13dragMoveEventEP6QEventPK9QMi'
        'meDataRK7QPointF',
        self._addressOf(e), self._addressOf(mimeData), self._valueOf(pos,
        'QPointF'),
    )

  @overload(QMimeData, QPointF, Qt.DropAction, QObject)
  @overload(QMimeData, QPointF, Qt.DropAction, NoneType)
  @overload(NoneType, QPointF, Qt.DropAction, QObject)
  @overload(NoneType, QPointF, Qt.DropAction, NoneType)
  def dropEvent(
      self,
      mimeData: Optional[QMimeData],
      pos: QPointF,
      dropAction: Qt.DropAction,
      source: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetTextControlPrivate::dropEvent(const QMimeData
    *mimeData, const QPointF &pos, Qt::DropAction dropAction, QObject
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#dropEvent

    Parameters
    ----------

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    dropAction : Qt.DropAction
      Passed on as its number.

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetTextControlPrivate::dropEvent(const QMimeData *mimeData,
    #      const QPointF &pos, Qt::DropAction dropAction, QObject *source)
    return self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate9dropEventEPK9QMimeDataRK7QPoi'
        'ntFN2Qt10DropActionEP7QObject',
        self._addressOf(mimeData), self._valueOf(pos, 'QPointF'),
        dropAction.value, self._addressOf(source, 'QObject'),
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void
    QWidgetTextControlPrivate::inputMethodEvent(QInputMethodEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControlPrivate::inputMethodEvent(QInputMethodEvent
    #      *a0)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate16inputMethodEventEP17QInputMe'
        'thodEvent',
        self._addressOf(a0),
    )

  @overload()
  @overload(str)
  def activateLinkUnderCursor(self, href: str = '') -> None:
    """
    Calls Qt's 'void
    QWidgetTextControlPrivate::activateLinkUnderCursor(QString href)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html

    Parameters
    ----------

    href : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QWidgetTextControlPrivate::activateLinkUnderCursor(QString href)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate23activateLinkUnderCursorE7QSt'
        'ring',
        href,
    )

  @overload(QPoint, QPointF, QWidget)
  @overload(QPoint, QPointF, NoneType)
  def showToolTip(
      self,
      globalPos: QPoint,
      pos: QPointF,
      contextWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::showToolTip(const QPoint
    &globalPos, const QPointF &pos, QWidget *contextWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#showToolTip

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    contextWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetTextControlPrivate::showToolTip(const QPoint &globalPos,
    #      const QPointF &pos, QWidget *contextWidget)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate11showToolTipERK6QPointRK7QPoi'
        'ntFP7QWidget',
        self._valueOf(globalPos), self._valueOf(pos, 'QPointF'),
        self._addressOf(contextWidget),
    )

  def commitPreedit(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::commitPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#commitPreedit
    """
    #  void QWidgetTextControlPrivate::commitPreedit()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate13commitPreeditEv',
    )

  def insertParagraphSeparator(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::insertParagraphSeparator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::insertParagraphSeparator()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate24insertParagraphSeparatorEv',
    )

  @overload(str)
  @overload(str, Qt.TextFormat)
  def append(
      self,
      text: str,
      format: Qt.TextFormat = Qt.TextFormat.AutoText,
  ) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::append(const QString &text,
    Qt::TextFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#append

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.TextFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TextFormat.AutoText.
    """
    #  void QWidgetTextControlPrivate::append(const QString &text,
    #      Qt::TextFormat format)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate6appendERK7QStringN2Qt10TextFo'
        'rmatE',
        text, format.value,
    )

  def _q_copyLink(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_copyLink()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#_q_copyLink
    """
    #  void QWidgetTextControlPrivate::_q_copyLink()
    self.uglySide.call('ritual_ZN25QWidgetTextControlPrivate11_q_copyLinkEv')

  @overload(QTextBlock)
  def _q_updateBlock(self, a0: QTextBlock) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_updateBlock(const
    QTextBlock &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html#_q_updateBlock

    Parameters
    ----------

    a0 : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QWidgetTextControlPrivate::_q_updateBlock(const QTextBlock &a0)
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate14_q_updateBlockERK10QTextBloc'
        'k',
        self._valueOf(a0),
    )

  def _q_documentLayoutChanged(self) -> None:
    """
    Calls Qt's 'void QWidgetTextControlPrivate::_q_documentLayoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgettextcontrolprivate.html
    """
    #  void QWidgetTextControlPrivate::_q_documentLayoutChanged()
    self.uglySide.call(
        'ritual_ZN25QWidgetTextControlPrivate24_q_documentLayoutChangedEv',
    )

  @staticmethod
  def _q_setCursorAfterUndoRedo(*__, **_) -> Never:
    """
    Qt's 'void QWidgetTextControlPrivate::_q_setCursorAfterUndoRedo(int
    undoPosition, int charsAdded, int charsRemoved)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate._q_setCursorAfterUndoRedo' has no cute "
        "function yet. Qt's 'void "
        "QWidgetTextControlPrivate::_q_setCursorAfterUndoRedo(int "
        "undoPosition, int charsAdded, int charsRemoved)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def cursorMoveKeyEvent(*__, **_) -> Never:
    """
    Qt's 'bool QWidgetTextControlPrivate::cursorMoveKeyEvent(QKeyEvent *e)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'currentTextLine'.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.cursorMoveKeyEvent' has no cute "
        "function yet. Qt's 'bool "
        "QWidgetTextControlPrivate::cursorMoveKeyEvent(QKeyEvent *e)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'currentTextLine'.")

  @staticmethod
  def extendWordwiseSelection(*__, **_) -> Never:
    """
    Qt's 'void QWidgetTextControlPrivate::extendWordwiseSelection(int
    suggestedNewPosition, qreal mouseXPosition)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'currentTextLine'.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.extendWordwiseSelection' has no cute "
        "function yet. Qt's 'void "
        "QWidgetTextControlPrivate::extendWordwiseSelection(int "
        "suggestedNewPosition, qreal mouseXPosition)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'currentTextLine'.")

  @staticmethod
  def mouseDoubleClickEvent(*__, **_) -> Never:
    """
    Qt's 'void QWidgetTextControlPrivate::mouseDoubleClickEvent(QEvent *e,
    Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
    modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'currentTextLine'.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.mouseDoubleClickEvent' has no cute "
        "function yet. Qt's 'void "
        "QWidgetTextControlPrivate::mouseDoubleClickEvent(QEvent *e, "
        "Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers "
        "modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'currentTextLine'.")

  @staticmethod
  def paste(*__, **_) -> Never:
    """
    Qt's 'void QWidgetTextControlPrivate::paste(const QMimeData *source)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.paste' has no cute function yet. Qt's "
        "'void QWidgetTextControlPrivate::paste(const QMimeData *source)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def selectionRect(*__, **_) -> Never:
    """
    - Qt's 'QRectF QWidgetTextControlPrivate::selectionRect(const QTextCursor
      &cursor) const': cannot be called and cannot be called through the
      meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    - Qt's 'QRectF QWidgetTextControlPrivate::selectionRect() const': leans
      on 'QWidgetTextControlPrivate::selectionRect(QTextCursor const&)
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.selectionRect' has no cute function "
        "yet. Qt's 'QRectF QWidgetTextControlPrivate::selectionRect(const "
        "QTextCursor &cursor) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's 'QRectF "
        "QWidgetTextControlPrivate::selectionRect() const': leans on "
        "'QWidgetTextControlPrivate::selectionRect(QTextCursor const&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setBlinkingCursorEnabled(*__, **_) -> Never:
    """
    Qt's 'void QWidgetTextControlPrivate::setBlinkingCursorEnabled(bool
    enable)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWidgetTextControlPrivate.setBlinkingCursorEnabled' has no cute "
        "function yet. Qt's 'void "
        "QWidgetTextControlPrivate::setBlinkingCursorEnabled(bool enable)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
