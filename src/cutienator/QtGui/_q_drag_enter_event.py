"""
QDragEnterEvent binding of the Qt C++
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
from ..QtCore import Qt
from . import QDragMoveEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMimeData, QPoint, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDragEnterEvent(QDragMoveEvent):
  """
  The cute side of Qt's QDragEnterEvent: a plain Python object standing in
  front of one C++ QDragEnterEvent.

  It is built on the cute 'QDragMoveEvent', as Qt's QDragEnterEvent is built
  on Qt's QDragMoveEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDragEnterEvent that has a ritual and that Python
  can call so far, 1 name in all: 'clone'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDragEnterEvent::~QDragEnterEvent()': the destructor: Python never
    removes a C++ QDragEnterEvent.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QDragEnterEvent is created at the first use, not by
    'QDragEnterEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDragEnterEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDragEnterEvent'

  #  A C++ QDragEnterEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDragEnterEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QDragEnterEvent]:
    """
    Calls Qt's 'QDragEnterEvent *QDragEnterEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdragenterevent.html#clone

    Returns
    -------

    Optional[QDragEnterEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDragEnterEvent *QDragEnterEvent::clone() const
    ritual = 'ritual_ZNK15QDragEnterEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDragEnterEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QDragEnterEvent._cuteAt(address)

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

  @overload(
      QPoint, Qt.DropActions, QMimeData, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QPoint, Qt.DropActions, NoneType, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def __init__(
      self,
      pos: QPoint,
      actions: Qt.DropActions,
      data: Optional[QMimeData],
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDragEnterEvent::QDragEnterEvent(const
    QPoint &pos, Qt::DropActions actions, const QMimeData *data,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdragenterevent.html#QDragEnterEvent

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    actions : Qt.DropActions
      Passed on as its number.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  QDragEnterEvent::QDragEnterEvent(const QPoint &pos, Qt::DropActions
    #      actions, const QMimeData *data, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers)
    self._noteCreation(QDragEnterEvent, lambda: Rituals.call(
        'ritual_ZN15QDragEnterEventC1ERK6QPoint6QFlagsIN2Qt10DropActionEEPK'
        '9QMimeDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEE',
        self._valueOf(pos), actions.value, self._addressOf(data),
        buttons.value, modifiers.value,
    ))

  @overload(
      QPointF, Qt.DropActions, QMimeData, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QPointF, Qt.DropActions, NoneType, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def __init__(
      self,
      pos: QPointF,
      actions: Qt.DropActions,
      data: Optional[QMimeData],
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDragEnterEvent::QDragEnterEvent(QPointF
    pos, Qt::DropActions actions, const QMimeData *data, Qt::MouseButtons
    buttons, Qt::KeyboardModifiers modifiers)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdragenterevent.html#QDragEnterEvent

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    actions : Qt.DropActions
      Passed on as its number.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  QDragEnterEvent::QDragEnterEvent(QPointF pos, Qt::DropActions actions,
    #      const QMimeData *data, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers)
    self._noteCreation(QDragEnterEvent, lambda: Rituals.call(
        'ritual_ZN15QDragEnterEventC1E7QPointF6QFlagsIN2Qt10DropActionEEPK9'
        'QMimeDataS1_INS2_11MouseButtonEES1_INS2_16KeyboardModifierEE',
        self._valueOf(pos), actions.value, self._addressOf(data),
        buttons.value, modifiers.value,
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
