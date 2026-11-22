"""
QScrollPrepareEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']


class QScrollPrepareEvent(QEvent):
  """
  The cute side of Qt's QScrollPrepareEvent: a plain Python object standing
  in front of one C++ QScrollPrepareEvent.

  It is built on the cute 'QEvent', as Qt's QScrollPrepareEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollPrepareEvent that has a ritual and that
  Python can call so far, 8 names in all: 'clone', 'startPos',
  'viewportSize', 'contentPosRange', 'contentPos', 'setViewportSize',
  'setContentPosRange', 'setContentPos'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScrollPrepareEvent::~QScrollPrepareEvent()': the destructor:
    Python never removes a C++ QScrollPrepareEvent.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QScrollPrepareEvent is created at the first use, not by
    'QScrollPrepareEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollPrepareEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollPrepareEvent'

  #  A C++ QScrollPrepareEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollPrepareEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QScrollPrepareEvent]:
    """
    Calls Qt's 'QScrollPrepareEvent *QScrollPrepareEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollprepareevent.html#clone

    Returns
    -------

    Optional[QScrollPrepareEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollPrepareEvent *QScrollPrepareEvent::clone() const
    ritual = 'ritual_ZNK19QScrollPrepareEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QScrollPrepareEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QScrollPrepareEvent._cuteAt(address)

  def startPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScrollPrepareEvent::startPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollprepareevent.html#startPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScrollPrepareEvent::startPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QScrollPrepareEvent8startPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def viewportSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QScrollPrepareEvent::viewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#viewportSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QScrollPrepareEvent::viewportSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QScrollPrepareEvent12viewportSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def contentPosRange(self) -> QRectF:
    """
    Calls Qt's 'QRectF QScrollPrepareEvent::contentPosRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#contentPosRange

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QScrollPrepareEvent::contentPosRange() const
    address = self.uglySide.call(
        'ritual_ZNK19QScrollPrepareEvent15contentPosRangeEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def contentPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScrollPrepareEvent::contentPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#contentPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScrollPrepareEvent::contentPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QScrollPrepareEvent10contentPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  def setViewportSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QScrollPrepareEvent::setViewportSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#setViewportSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QScrollPrepareEvent::setViewportSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN19QScrollPrepareEvent15setViewportSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(QRectF)
  def setContentPosRange(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QScrollPrepareEvent::setContentPosRange(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#setContentPosRange

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QScrollPrepareEvent::setContentPosRange(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN19QScrollPrepareEvent18setContentPosRangeERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QPointF)
  def setContentPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QScrollPrepareEvent::setContentPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#setContentPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QScrollPrepareEvent::setContentPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN19QScrollPrepareEvent13setContentPosERK7QPointF',
        self._valueOf(pos),
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

  @overload(QPointF)
  def __init__(self, startPos: QPointF) -> None:
    """
    Notes what was given, for Qt's
    'QScrollPrepareEvent::QScrollPrepareEvent(const QPointF &startPos)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollprepareevent.html#QScrollPrepareEvent

    Parameters
    ----------

    startPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QScrollPrepareEvent::QScrollPrepareEvent(const QPointF &startPos)
    self._noteCreation(QScrollPrepareEvent, lambda: Rituals.call(
        'ritual_ZN19QScrollPrepareEventC1ERK7QPointF',
        self._valueOf(startPos),
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
