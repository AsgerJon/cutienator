"""
QQuickTextControlPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextControlPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from ..QtGui import QTextCursor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtGui import QKeyEvent, QMouseEvent
  from . import QQuickTextControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextControlPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickTextControlPrivate: a plain Python object
  standing in front of one C++ QQuickTextControlPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickTextControlPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextControlPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'setCursorPosition',
  'setClipboardSelection', 'keyReleaseEvent', 'sendMouseEventToInputContext',
  'isPreediting', 'commitPreedit', 'cancelPreedit'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextControl *QQuickTextControlPrivate::q_func() const':
    takes in Python what 'QQuickTextControl
    *QQuickTextControlPrivate::q_func()' takes.

  What has no ritual
  ------------------

  26 of the 37 functions Qt declares: 20 leans on 'QQuickTextControl; 3
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 3 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickTextControlPrivate is created at the first use, not by
    'QQuickTextControlPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextControlPrivate.
  - Each name of Qt's QQuickTextControlPrivate that has no cute function yet,
    '_q_copyLink', '_q_setCursorAfterUndoRedo',
    '_q_updateCurrentCharFormatAndSelection', '_q_updateCursorPosChanged',
    'activateLinkUnderCursor', 'cursorMoveKeyEvent',
    'extendBlockwiseSelection', 'extendWordwiseSelection', 'focusEvent',
    'hoverEvent', 'inputMethodEvent', 'keyPressEvent',
    'mouseDoubleClickEvent', 'mouseMoveEvent', 'mousePressEvent',
    'mouseReleaseEvent', 'paste', 'rectForPosition', 'repaintCursor',
    'repaintOldAndNewSelection', 'repaintSelection', 'selectionChanged',
    'setBlinkingCursorEnabled', 'setContent', 'updateCurrentCharFormat',
    'updateCursorFlashTime', holds a function that raises
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
  __qt_class__ = 'QQuickTextControlPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isPreediting(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextControlPrivate::isPreediting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#isPreediting
    """
    #  bool QQuickTextControlPrivate::isPreediting() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickTextControlPrivate12isPreeditingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setCursorPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTextControlPrivate::setCursorPosition(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#setCursorPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTextControlPrivate::setCursorPosition(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate17setCursorPositionERK7QPointF',
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
    Calls Qt's 'void QQuickTextControlPrivate::setCursorPosition(int pos,
    QTextCursor::MoveMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#setCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  void QQuickTextControlPrivate::setCursorPosition(int pos,
    #      QTextCursor::MoveMode mode)
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate17setCursorPositionEiN11QTextCu'
        'rsor8MoveModeE',
        pos, mode.value,
    )

  def setClipboardSelection(self) -> None:
    """
    Calls Qt's 'void QQuickTextControlPrivate::setClipboardSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html
    """
    #  void QQuickTextControlPrivate::setClipboardSelection()
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate21setClipboardSelectionEv',
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
    'QQuickTextControlPrivate::QQuickTextControlPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html
    """
    #  QQuickTextControlPrivate::QQuickTextControlPrivate()
    self._noteCreation(QQuickTextControlPrivate, lambda: Rituals.call(
        'ritual_ZN24QQuickTextControlPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTextControl]:
    """
    Calls Qt's 'QQuickTextControl *QQuickTextControlPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextControl *QQuickTextControlPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate6q_funcEv',
    )
    from . import QQuickTextControl
    return QQuickTextControl._cuteAt(address)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextControlPrivate::keyReleaseEvent(QKeyEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#keyReleaseEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextControlPrivate::keyReleaseEvent(QKeyEvent *e)
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate15keyReleaseEventEP9QKeyEvent',
        self._addressOf(e),
    )

  @overload(QMouseEvent, QPointF)
  @overload(NoneType, QPointF)
  def sendMouseEventToInputContext(
      self,
      event: Optional[QMouseEvent],
      pos: QPointF,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextControlPrivate::sendMouseEventToInputContext(QMouseEvent
    *event, const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool
    #      QQuickTextControlPrivate::sendMouseEventToInputContext(QMouseEvent
    #      *event, const QPointF &pos)
    return self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate28sendMouseEventToInputContextE'
        'P11QMouseEventRK7QPointF',
        self._addressOf(event), self._valueOf(pos, 'QPointF'),
    )

  def commitPreedit(self) -> None:
    """
    Calls Qt's 'void QQuickTextControlPrivate::commitPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#commitPreedit
    """
    #  void QQuickTextControlPrivate::commitPreedit()
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate13commitPreeditEv',
    )

  def cancelPreedit(self) -> None:
    """
    Calls Qt's 'void QQuickTextControlPrivate::cancelPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextcontrolprivate.html#cancelPreedit
    """
    #  void QQuickTextControlPrivate::cancelPreedit()
    self.uglySide.call(
        'ritual_ZN24QQuickTextControlPrivate13cancelPreeditEv',
    )

  @staticmethod
  def _q_copyLink(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::_q_copyLink()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate._q_copyLink' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::_q_copyLink()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def _q_setCursorAfterUndoRedo(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::_q_setCursorAfterUndoRedo(int
    undoPosition, int charsAdded, int charsRemoved)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate._q_setCursorAfterUndoRedo' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::_q_setCursorAfterUndoRedo(int "
        "undoPosition, int charsAdded, int charsRemoved)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def _q_updateCurrentCharFormatAndSelection(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTextControlPrivate::_q_updateCurrentCharFormatAndSelection()':
    leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate._q_updateCurrentCharFormatAndSelection' "
        "has no cute function yet. Qt's 'void "
        "QQuickTextControlPrivate::_q_updateCurrentCharFormatAndSelection()'"
        ": leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def _q_updateCursorPosChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::_q_updateCursorPosChanged(const
    QTextCursor &someCursor)': leans on
    'QQuickTextControl::cursorPositionChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate._q_updateCursorPosChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::_q_updateCursorPosChanged(const "
        "QTextCursor &someCursor)': leans on "
        "'QQuickTextControl::cursorPositionChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def activateLinkUnderCursor(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::activateLinkUnderCursor(QString
    href)': leans on 'QQuickTextControl::linkActivated(QString const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.activateLinkUnderCursor' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::activateLinkUnderCursor(QString href)': "
        "leans on 'QQuickTextControl::linkActivated(QString const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def cursorMoveKeyEvent(*__, **_) -> Never:
    """
    Qt's 'bool QQuickTextControlPrivate::cursorMoveKeyEvent(QKeyEvent *e)':
    leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.cursorMoveKeyEvent' has no cute function "
        "yet. Qt's 'bool "
        "QQuickTextControlPrivate::cursorMoveKeyEvent(QKeyEvent *e)': leans "
        "on 'QQuickTextControl::copyAvailable(bool)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def extendBlockwiseSelection(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::extendBlockwiseSelection(int
    suggestedNewPosition)': leans on
    'QQuickTextControl::copyAvailable(bool)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.extendBlockwiseSelection' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::extendBlockwiseSelection(int "
        "suggestedNewPosition)': leans on "
        "'QQuickTextControl::copyAvailable(bool)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def extendWordwiseSelection(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::extendWordwiseSelection(int
    suggestedNewPosition, qreal mouseXPosition)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'currentTextLine'.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.extendWordwiseSelection' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::extendWordwiseSelection(int "
        "suggestedNewPosition, qreal mouseXPosition)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'currentTextLine'.")

  @staticmethod
  def focusEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::focusEvent(QFocusEvent *e)': leans
    on 'QQuickTextControl::copyAvailable(bool)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.focusEvent' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::focusEvent(QFocusEvent *e)': "
        "leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def hoverEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::hoverEvent(QHoverEvent *e, const
    QPointF &pos)': leans on 'QQuickTextControl::linkHovered(QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.hoverEvent' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::hoverEvent(QHoverEvent *e, "
        "const QPointF &pos)': leans on "
        "'QQuickTextControl::linkHovered(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def inputMethodEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::inputMethodEvent(QInputMethodEvent
    *a0)': leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.inputMethodEvent' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextControlPrivate::inputMethodEvent(QInputMethodEvent "
        "*a0)': leans on 'QQuickTextControl::copyAvailable(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def keyPressEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::keyPressEvent(QKeyEvent *e)': leans
    on 'QQuickTextControl::copyAvailable(bool)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.keyPressEvent' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::keyPressEvent(QKeyEvent *e)': "
        "leans on 'QQuickTextControl::copyAvailable(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def mouseDoubleClickEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::mouseDoubleClickEvent(QMouseEvent
    *event, const QPointF &pos)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'currentTextLine'.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.mouseDoubleClickEvent' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::mouseDoubleClickEvent(QMouseEvent "
        "*event, const QPointF &pos)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'currentTextLine'.")

  @staticmethod
  def mouseMoveEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::mouseMoveEvent(QMouseEvent *event,
    const QPointF &pos)': leans on 'QQuickTextControl::copyAvailable(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.mouseMoveEvent' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextControlPrivate::mouseMoveEvent(QMouseEvent *event, const "
        "QPointF &pos)': leans on 'QQuickTextControl::copyAvailable(bool)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def mousePressEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::mousePressEvent(QMouseEvent *event,
    const QPointF &pos)': leans on 'QQuickTextControl::copyAvailable(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.mousePressEvent' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextControlPrivate::mousePressEvent(QMouseEvent *event, "
        "const QPointF &pos)': leans on "
        "'QQuickTextControl::copyAvailable(bool)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mouseReleaseEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::mouseReleaseEvent(QMouseEvent
    *event, const QPointF &pos)': leans on
    'QQuickTextControl::copyAvailable(bool)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.mouseReleaseEvent' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextControlPrivate::mouseReleaseEvent(QMouseEvent *event, "
        "const QPointF &pos)': leans on "
        "'QQuickTextControl::copyAvailable(bool)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def paste(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::paste(const QMimeData *source)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.paste' has no cute function yet. Qt's "
        "'void QQuickTextControlPrivate::paste(const QMimeData *source)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def rectForPosition(*__, **_) -> Never:
    """
    Qt's 'QRectF QQuickTextControlPrivate::rectForPosition(int position)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'textCursorWidth'.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.rectForPosition' has no cute function "
        "yet. Qt's 'QRectF QQuickTextControlPrivate::rectForPosition(int "
        "position) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'textCursorWidth'.")

  @staticmethod
  def repaintCursor(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::repaintCursor()': leans on
    'QQuickTextControl::updateCursorRequest()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.repaintCursor' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::repaintCursor()': leans on "
        "'QQuickTextControl::updateCursorRequest()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def repaintOldAndNewSelection(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::repaintOldAndNewSelection(const
    QTextCursor &oldSelection)': leans on
    'QQuickTextControl::updateRequest()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.repaintOldAndNewSelection' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::repaintOldAndNewSelection(const "
        "QTextCursor &oldSelection)': leans on "
        "'QQuickTextControl::updateRequest()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def repaintSelection(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::repaintSelection()': leans on
    'QQuickTextControl::updateRequest()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.repaintSelection' has no cute function "
        "yet. Qt's 'void QQuickTextControlPrivate::repaintSelection()': "
        "leans on 'QQuickTextControl::updateRequest()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def selectionChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::selectionChanged(bool
    forceEmitSelectionChanged)': leans on
    'QQuickTextControl::copyAvailable(bool)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.selectionChanged' has no cute function "
        "yet. Qt's 'void QQuickTextControlPrivate::selectionChanged(bool "
        "forceEmitSelectionChanged)': leans on "
        "'QQuickTextControl::copyAvailable(bool)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setBlinkingCursorEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::setBlinkingCursorEnabled(bool
    enable)': leans on 'QQuickTextControl::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.setBlinkingCursorEnabled' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::setBlinkingCursorEnabled(bool enable)': "
        "leans on 'QQuickTextControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setContent(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::setContent(Qt::TextFormat format,
    const QString &text)': leans on 'QQuickTextControl::textChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.setContent' has no cute function yet. "
        "Qt's 'void QQuickTextControlPrivate::setContent(Qt::TextFormat "
        "format, const QString &text)': leans on "
        "'QQuickTextControl::textChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateCurrentCharFormat(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::updateCurrentCharFormat()': leans on
    'QQuickTextControl::currentCharFormatChanged(QTextCharFormat const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.updateCurrentCharFormat' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::updateCurrentCharFormat()': leans on "
        "'QQuickTextControl::currentCharFormatChanged(QTextCharFormat "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def updateCursorFlashTime(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextControlPrivate::updateCursorFlashTime()': leans on
    'QQuickTextControl::updateCursorRequest()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextControlPrivate.updateCursorFlashTime' has no cute "
        "function yet. Qt's 'void "
        "QQuickTextControlPrivate::updateCursorFlashTime()': leans on "
        "'QQuickTextControl::updateCursorRequest()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
