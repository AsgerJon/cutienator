"""
QLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlabel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLabelPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QFramePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QPoint, QRect, QRectF, QSize
  from . import QLabel, QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLabelPrivate(QFramePrivate):
  """
  The cute side of Qt's QLabelPrivate: a plain Python object standing in
  front of one C++ QLabelPrivate.

  It is built on the cute 'QFramePrivate', as Qt's QLabelPrivate is built on
  Qt's QFramePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLabelPrivate that has a ritual and that Python can
  call so far, 20 names in all: 'q_func', 'init', 'clearContents',
  'updateLabel', 'sizeForWidth', 'movieUpdated', 'movieResized',
  'updateShortcut', 'buddyDeleted', 'needTextControl', 'ensureTextPopulated',
  'ensureTextLayouted', 'ensureTextControl', 'sendControlEvent',
  'linkHovered', 'layoutRect', 'documentRect', 'layoutPoint',
  'textDirection', 'createStandardContextMenu'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLabel *QLabelPrivate::q_func() const': takes in Python what
    'QLabel *QLabelPrivate::q_func()' takes.
  - Qt's 'QLabelPrivate::~QLabelPrivate()': the destructor: Python never
    removes a C++ QLabelPrivate.

  What to expect
  --------------

  - The C++ QLabelPrivate is created at the first use, not by
    'QLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLabelPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLabelPrivate'

  #  A C++ QLabelPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLabelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def sizeForWidth(self, w: int) -> QSize:
    """
    Calls Qt's 'QSize QLabelPrivate::sizeForWidth(int w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#sizeForWidth

    Parameters
    ----------

    w : int
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLabelPrivate::sizeForWidth(int w) const
    address = self.uglySide.call(
        'ritual_ZNK13QLabelPrivate12sizeForWidthEi', w,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def needTextControl(self) -> bool:
    """
    Calls Qt's 'bool QLabelPrivate::needTextControl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#needTextControl
    """
    #  bool QLabelPrivate::needTextControl() const
    return self.uglySide.call('ritual_ZNK13QLabelPrivate15needTextControlEv')

  def layoutRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QLabelPrivate::layoutRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#layoutRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QLabelPrivate::layoutRect() const
    address = self.uglySide.call('ritual_ZNK13QLabelPrivate10layoutRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def documentRect(self) -> QRect:
    """
    Calls Qt's 'QRect QLabelPrivate::documentRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#documentRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QLabelPrivate::documentRect() const
    address = self.uglySide.call('ritual_ZNK13QLabelPrivate12documentRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def layoutPoint(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QLabelPrivate::layoutPoint(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#layoutPoint

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QLabelPrivate::layoutPoint(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK13QLabelPrivate11layoutPointERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QLabelPrivate::textDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QLabelPrivate::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK13QLabelPrivate13textDirectionEv',
    ))

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
    Notes what was given, for Qt's 'QLabelPrivate::QLabelPrivate()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#QLabelPrivate
    """
    #  QLabelPrivate::QLabelPrivate()
    self._noteCreation(QLabelPrivate, lambda: Rituals.call(
        'ritual_ZN13QLabelPrivateC1Ev',
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

  def q_func(self) -> Optional[QLabel]:
    """
    Calls Qt's 'QLabel *QLabelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#q_func

    Returns
    -------

    Optional[QLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLabel *QLabelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN13QLabelPrivate6q_funcEv')
    from . import QLabel
    return QLabel._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#init
    """
    #  void QLabelPrivate::init()
    self.uglySide.call('ritual_ZN13QLabelPrivate4initEv')

  def clearContents(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::clearContents()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#clearContents
    """
    #  void QLabelPrivate::clearContents()
    self.uglySide.call('ritual_ZN13QLabelPrivate13clearContentsEv')

  def updateLabel(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::updateLabel()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#updateLabel
    """
    #  void QLabelPrivate::updateLabel()
    self.uglySide.call('ritual_ZN13QLabelPrivate11updateLabelEv')

  @overload(QRect)
  def movieUpdated(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QLabelPrivate::movieUpdated(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#movieUpdated

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QLabelPrivate::movieUpdated(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN13QLabelPrivate12movieUpdatedERK5QRect',
        self._valueOf(rect),
    )

  @overload(QSize)
  def movieResized(self, size: QSize) -> None:
    """
    Calls Qt's 'void QLabelPrivate::movieResized(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#movieResized

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QLabelPrivate::movieResized(const QSize &size)
    self.uglySide.call(
        'ritual_ZN13QLabelPrivate12movieResizedERK5QSize',
        self._valueOf(size),
    )

  def updateShortcut(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::updateShortcut()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#updateShortcut
    """
    #  void QLabelPrivate::updateShortcut()
    self.uglySide.call('ritual_ZN13QLabelPrivate14updateShortcutEv')

  def buddyDeleted(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::buddyDeleted()'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#buddyDeleted
    """
    #  void QLabelPrivate::buddyDeleted()
    self.uglySide.call('ritual_ZN13QLabelPrivate12buddyDeletedEv')

  def ensureTextPopulated(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::ensureTextPopulated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabelprivate.html#ensureTextPopulated
    """
    #  void QLabelPrivate::ensureTextPopulated() const
    self.uglySide.call('ritual_ZNK13QLabelPrivate19ensureTextPopulatedEv')

  def ensureTextLayouted(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::ensureTextLayouted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabelprivate.html#ensureTextLayouted
    """
    #  void QLabelPrivate::ensureTextLayouted() const
    self.uglySide.call('ritual_ZNK13QLabelPrivate18ensureTextLayoutedEv')

  def ensureTextControl(self) -> None:
    """
    Calls Qt's 'void QLabelPrivate::ensureTextControl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabelprivate.html#ensureTextControl
    """
    #  void QLabelPrivate::ensureTextControl() const
    self.uglySide.call('ritual_ZNK13QLabelPrivate17ensureTextControlEv')

  @overload(QEvent)
  @overload(NoneType)
  def sendControlEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QLabelPrivate::sendControlEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabelprivate.html#sendControlEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLabelPrivate::sendControlEvent(QEvent *e)
    self.uglySide.call(
        'ritual_ZN13QLabelPrivate16sendControlEventEP6QEvent',
        self._addressOf(e),
    )

  @overload(str)
  def linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QLabelPrivate::linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qlabelprivate.html#linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLabelPrivate::linkHovered(const QString &link)
    self.uglySide.call(
        'ritual_ZN13QLabelPrivate11linkHoveredERK7QString', link,
    )

  @overload(QPoint)
  def createStandardContextMenu(self, pos: QPoint) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QLabelPrivate::createStandardContextMenu(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlabelprivate.html#createStandardContextMenu

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QLabelPrivate::createStandardContextMenu(const QPoint &pos)
    address = self.uglySide.call(
        'ritual_ZN13QLabelPrivate25createStandardContextMenuERK6QPoint',
        self._valueOf(pos),
    )
    from . import QMenu
    return QMenu._cuteAt(address)
