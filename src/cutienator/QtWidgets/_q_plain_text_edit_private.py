"""
QPlainTextEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPlainTextEditPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QTextCursor
from . import QAbstractScrollAreaPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPoint, QRectF
  from . import QPlainTextEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPoint = WAIT['QPoint']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlainTextEditPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QPlainTextEditPrivate: a plain Python object standing
  in front of one C++ QPlainTextEditPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QPlainTextEditPrivate is built on Qt's QAbstractScrollAreaPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlainTextEditPrivate that has a ritual and that
  Python can call so far, 18 names in all: 'q_func', 'repaintContents',
  'updatePlaceholderVisibility', 'mapToContents',
  'verticalScrollbarActionTriggered', 'ensureViewportLayouted', 'pageUpDown',
  'horizontalOffset', 'verticalOffset', 'sendControlEvent',
  'updateDefaultTextOption', 'setTopLine', 'setTopBlock', 'ensureVisible',
  'ensureCursorVisible', 'updateViewport', 'cursorPositionChanged',
  'placeHolderTextToBeShown'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPlainTextEdit *QPlainTextEditPrivate::q_func() const': takes
    in Python what 'QPlainTextEdit *QPlainTextEditPrivate::q_func()' takes.

  What has no ritual
  ------------------

  5 of the 26 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied; 1
  leans on 'vtable for QPlainTextEditControl', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QPlainTextEditPrivate is created at the first use, not by
    'QPlainTextEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlainTextEditPrivate.
  - Each name of Qt's QPlainTextEditPrivate that has no cute function yet,
    'adjustScrollbars', 'append', 'modificationChanged', 'relayoutDocument',
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
  __qt_class__ = 'QPlainTextEditPrivate'

  #  A C++ QPlainTextEditPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlainTextEditPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def mapToContents(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QPlainTextEditPrivate::mapToContents(const QPoint
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#mapToContents

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPlainTextEditPrivate::mapToContents(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK21QPlainTextEditPrivate13mapToContentsERK6QPoint',
        self._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QPlainTextEditPrivate::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#horizontalOffset
    """
    #  int QPlainTextEditPrivate::horizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK21QPlainTextEditPrivate16horizontalOffsetEv',
    )

  @overload(int, int)
  def verticalOffset(self, topBlock: int, topLine: int) -> float:
    """
    Calls Qt's 'qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int
    topLine) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#verticalOffset

    Parameters
    ----------

    topBlock : int
      Passed on as it is.

    topLine : int
      Passed on as it is.
    """
    #  qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int topLine)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QPlainTextEditPrivate14verticalOffsetEii',
        topBlock, topLine,
    )

  @overload()
  def verticalOffset(self) -> float:
    """
    Calls Qt's 'qreal QPlainTextEditPrivate::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#verticalOffset
    """
    #  qreal QPlainTextEditPrivate::verticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK21QPlainTextEditPrivate14verticalOffsetEv',
    )

  def placeHolderTextToBeShown(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEditPrivate::placeHolderTextToBeShown()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html
    """
    #  bool QPlainTextEditPrivate::placeHolderTextToBeShown() const
    return self.uglySide.call(
        'ritual_ZNK21QPlainTextEditPrivate24placeHolderTextToBeShownEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, int)
  def setTopLine(self, visualTopLine: int, dx: int = 0) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::setTopLine(int visualTopLine, int
    dx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#setTopLine

    Parameters
    ----------

    visualTopLine : int
      Passed on as it is.

    dx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QPlainTextEditPrivate::setTopLine(int visualTopLine, int dx)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate10setTopLineEii', visualTopLine, dx,
    )

  @overload(int, int)
  @overload(int, int, int)
  def setTopBlock(
      self,
      newTopBlock: int,
      newTopLine: int,
      dx: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::setTopBlock(int newTopBlock, int
    newTopLine, int dx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#setTopBlock

    Parameters
    ----------

    newTopBlock : int
      Passed on as it is.

    newTopLine : int
      Passed on as it is.

    dx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QPlainTextEditPrivate::setTopBlock(int newTopBlock, int
    #      newTopLine, int dx)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate11setTopBlockEiii',
        newTopBlock, newTopLine, dx,
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
    'QPlainTextEditPrivate::QPlainTextEditPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#QPlainTextEditPrivate
    """
    #  QPlainTextEditPrivate::QPlainTextEditPrivate()
    self._noteCreation(QPlainTextEditPrivate, lambda: Rituals.call(
        'ritual_ZN21QPlainTextEditPrivateC1Ev',
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

  def q_func(self) -> Optional[QPlainTextEdit]:
    """
    Calls Qt's 'QPlainTextEdit *QPlainTextEditPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintexteditprivate.html#q_func

    Returns
    -------

    Optional[QPlainTextEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlainTextEdit *QPlainTextEditPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QPlainTextEditPrivate6q_funcEv')
    from . import QPlainTextEdit
    return QPlainTextEdit._cuteAt(address)

  @overload(QRectF)
  def repaintContents(self, contentsRect: QRectF) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::repaintContents(const QRectF
    &contentsRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#repaintContents

    Parameters
    ----------

    contentsRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPlainTextEditPrivate::repaintContents(const QRectF
    #      &contentsRect)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate15repaintContentsERK6QRectF',
        self._valueOf(contentsRect),
    )

  def updatePlaceholderVisibility(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::updatePlaceholderVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html
    """
    #  void QPlainTextEditPrivate::updatePlaceholderVisibility()
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate27updatePlaceholderVisibilityEv',
    )

  @overload(int)
  def verticalScrollbarActionTriggered(self, action: int) -> None:
    """
    Calls Qt's 'void
    QPlainTextEditPrivate::verticalScrollbarActionTriggered(int action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QPlainTextEditPrivate::verticalScrollbarActionTriggered(int
    #      action)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate32verticalScrollbarActionTriggered'
        'Ei',
        action,
    )

  def ensureViewportLayouted(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::ensureViewportLayouted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#ensureViewportLayouted
    """
    #  void QPlainTextEditPrivate::ensureViewportLayouted()
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate22ensureViewportLayoutedEv',
    )

  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode)
  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode, bool)
  def pageUpDown(
      self,
      op: QTextCursor.MoveOperation,
      moveMode: QTextCursor.MoveMode,
      moveCursor: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QPlainTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op,
    QTextCursor::MoveMode moveMode, bool moveCursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#pageUpDown

    Parameters
    ----------

    op : QTextCursor.MoveOperation
      Passed on as its number.

    moveMode : QTextCursor.MoveMode
      Passed on as its number.

    moveCursor : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPlainTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op,
    #      QTextCursor::MoveMode moveMode, bool moveCursor)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate10pageUpDownEN11QTextCursor13MoveO'
        'perationENS0_8MoveModeEb',
        op.value, moveMode.value, moveCursor,
    )

  @overload(QEvent)
  @overload(NoneType)
  def sendControlEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::sendControlEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#sendControlEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEditPrivate::sendControlEvent(QEvent *e)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate16sendControlEventEP6QEvent',
        self._addressOf(e),
    )

  def updateDefaultTextOption(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::updateDefaultTextOption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#updateDefaultTextOption
    """
    #  void QPlainTextEditPrivate::updateDefaultTextOption()
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate23updateDefaultTextOptionEv',
    )

  @overload(int, bool)
  @overload(int, bool, bool)
  def ensureVisible(
      self,
      position: int,
      center: bool,
      forceCenter: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::ensureVisible(int position, bool
    center, bool forceCenter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#ensureVisible

    Parameters
    ----------

    position : int
      Passed on as it is.

    center : bool
      Passed on as it is.

    forceCenter : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPlainTextEditPrivate::ensureVisible(int position, bool center,
    #      bool forceCenter)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate13ensureVisibleEibb',
        position, center, forceCenter,
    )

  @overload()
  @overload(bool)
  def ensureCursorVisible(self, center: bool = False) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::ensureCursorVisible(bool
    center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#ensureCursorVisible

    Parameters
    ----------

    center : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPlainTextEditPrivate::ensureCursorVisible(bool center)
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate19ensureCursorVisibleEb', center,
    )

  def updateViewport(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::updateViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#updateViewport
    """
    #  void QPlainTextEditPrivate::updateViewport()
    self.uglySide.call('ritual_ZN21QPlainTextEditPrivate14updateViewportEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditPrivate::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditprivate.html#cursorPositionChanged
    """
    #  void QPlainTextEditPrivate::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN21QPlainTextEditPrivate21cursorPositionChangedEv',
    )

  @staticmethod
  def adjustScrollbars(*__, **_) -> Never:
    """
    Qt's 'void QPlainTextEditPrivate::adjustScrollbars()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type
    'QPlainTextDocumentLayoutPrivate'.
    """
    raise NotImplementedError(
        "'QPlainTextEditPrivate.adjustScrollbars' has no cute function yet. "
        "Qt's 'void QPlainTextEditPrivate::adjustScrollbars()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QPlainTextDocumentLayoutPrivate'.")

  @staticmethod
  def append(*__, **_) -> Never:
    """
    Qt's 'void QPlainTextEditPrivate::append(const QString &text,
    Qt::TextFormat format)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QPlainTextDocumentLayoutPrivate'.
    """
    raise NotImplementedError(
        "'QPlainTextEditPrivate.append' has no cute function yet. Qt's "
        "'void QPlainTextEditPrivate::append(const QString &text, "
        "Qt::TextFormat format)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QPlainTextDocumentLayoutPrivate'.")

  @staticmethod
  def modificationChanged(*__, **_) -> Never:
    """
    Qt's 'void QPlainTextEditPrivate::modificationChanged(bool a0)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QPlainTextEditPrivate.modificationChanged' has no cute function "
        "yet. Qt's 'void QPlainTextEditPrivate::modificationChanged(bool "
        "a0)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def relayoutDocument(*__, **_) -> Never:
    """
    Qt's 'void QPlainTextEditPrivate::relayoutDocument()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type
    'QPlainTextDocumentLayoutPrivate'.
    """
    raise NotImplementedError(
        "'QPlainTextEditPrivate.relayoutDocument' has no cute function yet. "
        "Qt's 'void QPlainTextEditPrivate::relayoutDocument()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QPlainTextDocumentLayoutPrivate'.")
