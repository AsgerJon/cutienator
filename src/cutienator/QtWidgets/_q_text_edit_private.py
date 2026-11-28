"""
QTextEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtextedit_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextEditPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QTextCursor
from . import QAbstractScrollAreaPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPoint, QRectF, QUrl
  from ..QtGui import QPaintEvent, QPainter, QTextBlock
  from . import QTextEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRectF = WAIT['QRectF']
  QTextBlock = WAIT['QTextBlock']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextEditPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QTextEditPrivate: a plain Python object standing in
  front of one C++ QTextEditPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QTextEditPrivate is built on Qt's QAbstractScrollAreaPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTextEditPrivate that has a ritual and that Python
  can call so far, 15 names in all: 'q_func', 'paint', 'repaintContents',
  'mapToContents', 'ensureVisible', 'relayoutDocument',
  'createAutoBulletList', 'pageUpDown', 'horizontalOffset', 'verticalOffset',
  'sendControlEvent', 'cursorPositionChanged',
  'hoveredBlockWithMarkerChanged', 'updateDefaultTextOption', 'resolveUrl'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextEdit *QTextEditPrivate::q_func() const': takes in Python
    what 'QTextEdit *QTextEditPrivate::q_func()' takes.
  - Qt's 'QTextEditPrivate::~QTextEditPrivate()': the destructor: Python
    never removes a C++ QTextEditPrivate.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QTextEditPrivate is created at the first use, not by
    'QTextEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextEditPrivate.
  - Each name of Qt's QTextEditPrivate that has no cute function yet,
    'adjustScrollbars', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextEditPrivate'

  #  A C++ QTextEditPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextEditPrivate'

  #  The functions Qt calls itself that QTextEditPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'resolveUrl': (
          ('_ZNK16QTextEditPrivate10resolveUrlERK4QUrl',
           ('address', 'value', 'QtCore:QUrl'),
           (
               ('address', 'value', 'QtCore:QUrl'),
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

  @overload(QPoint)
  def mapToContents(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QTextEditPrivate::mapToContents(const QPoint &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#mapToContents

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
    #  QPoint QTextEditPrivate::mapToContents(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK16QTextEditPrivate13mapToContentsERK6QPoint',
        self._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QTextEditPrivate::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#horizontalOffset
    """
    #  int QTextEditPrivate::horizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QTextEditPrivate16horizontalOffsetEv',
    )

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QTextEditPrivate::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#verticalOffset
    """
    #  int QTextEditPrivate::verticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QTextEditPrivate14verticalOffsetEv',
    )

  @overload(QUrl)
  def resolveUrl(self, url: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QTextEditPrivate::resolveUrl(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexteditprivate.html#resolveUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QTextEditPrivate::resolveUrl(const QUrl &url) const
    ritual = 'ritual_ZNK16QTextEditPrivate10resolveUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QTextEditPrivate10resolveUrlERK4QUrl'
    address = self.uglySide.call(ritual, self._valueOf(url))
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QTextEditPrivate::QTextEditPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#QTextEditPrivate
    """
    #  QTextEditPrivate::QTextEditPrivate()
    self._noteCreation(QTextEditPrivate, lambda: Rituals.call(
        'ritual_ZN16QTextEditPrivateC1Ev',
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

  def q_func(self) -> Optional[QTextEdit]:
    """
    Calls Qt's 'QTextEdit *QTextEditPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexteditprivate.html#q_func

    Returns
    -------

    Optional[QTextEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextEdit *QTextEditPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QTextEditPrivate6q_funcEv')
    from . import QTextEdit
    return QTextEdit._cuteAt(address)

  @overload(QPainter, QPaintEvent)
  @overload(QPainter, NoneType)
  @overload(NoneType, QPaintEvent)
  @overload(NoneType, NoneType)
  def paint(self, p: Optional[QPainter], e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::paint(QPainter *p, QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexteditprivate.html#paint

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEditPrivate::paint(QPainter *p, QPaintEvent *e)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate5paintEP8QPainterP11QPaintEvent',
        self._addressOf(p), self._addressOf(e),
    )

  @overload(QRectF)
  def repaintContents(self, contentsRect: QRectF) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::repaintContents(const QRectF
    &contentsRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#repaintContents

    Parameters
    ----------

    contentsRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QTextEditPrivate::repaintContents(const QRectF &contentsRect)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate15repaintContentsERK6QRectF',
        self._valueOf(contentsRect),
    )

  @overload(QRectF)
  def ensureVisible(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::ensureVisible(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#ensureVisible

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QTextEditPrivate::ensureVisible(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate13ensureVisibleERK6QRectF',
        self._valueOf(rect),
    )

  def relayoutDocument(self) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::relayoutDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#relayoutDocument
    """
    #  void QTextEditPrivate::relayoutDocument()
    self.uglySide.call('ritual_ZN16QTextEditPrivate16relayoutDocumentEv')

  def createAutoBulletList(self) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::createAutoBulletList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#createAutoBulletList
    """
    #  void QTextEditPrivate::createAutoBulletList()
    self.uglySide.call('ritual_ZN16QTextEditPrivate20createAutoBulletListEv')

  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode)
  def pageUpDown(
      self,
      op: QTextCursor.MoveOperation,
      moveMode: QTextCursor.MoveMode,
  ) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::pageUpDown(QTextCursor::MoveOperation
    op, QTextCursor::MoveMode moveMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexteditprivate.html#pageUpDown

    Parameters
    ----------

    op : QTextCursor.MoveOperation
      Passed on as its number.

    moveMode : QTextCursor.MoveMode
      Passed on as its number.
    """
    #  void QTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op,
    #      QTextCursor::MoveMode moveMode)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate10pageUpDownEN11QTextCursor13MoveOperat'
        'ionENS0_8MoveModeE',
        op.value, moveMode.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def sendControlEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::sendControlEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#sendControlEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEditPrivate::sendControlEvent(QEvent *e)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate16sendControlEventEP6QEvent',
        self._addressOf(e),
    )

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#cursorPositionChanged
    """
    #  void QTextEditPrivate::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate21cursorPositionChangedEv',
    )

  @overload(QTextBlock)
  def hoveredBlockWithMarkerChanged(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::hoveredBlockWithMarkerChanged(const
    QTextBlock &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextEditPrivate::hoveredBlockWithMarkerChanged(const QTextBlock
    #      &block)
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate29hoveredBlockWithMarkerChangedERK10QTe'
        'xtBlock',
        self._valueOf(block),
    )

  def updateDefaultTextOption(self) -> None:
    """
    Calls Qt's 'void QTextEditPrivate::updateDefaultTextOption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditprivate.html#updateDefaultTextOption
    """
    #  void QTextEditPrivate::updateDefaultTextOption()
    self.uglySide.call(
        'ritual_ZN16QTextEditPrivate23updateDefaultTextOptionEv',
    )

  @staticmethod
  def adjustScrollbars(*__, **_) -> Never:
    """
    Qt's 'void QTextEditPrivate::adjustScrollbars()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'documentSize'.
    """
    raise NotImplementedError(
        "'QTextEditPrivate.adjustScrollbars' has no cute function yet. Qt's "
        "'void QTextEditPrivate::adjustScrollbars()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'documentSize'.")
