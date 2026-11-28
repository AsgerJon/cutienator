"""
QDragMoveEvent binding of the Qt C++
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
from ..QtCore import Qt, QEvent
from . import QDropEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMimeData, QPoint, QPointF, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDragMoveEvent(QDropEvent):
  """
  The cute side of Qt's QDragMoveEvent: a plain Python object standing in
  front of one C++ QDragMoveEvent.

  It is built on the cute 'QDropEvent', as Qt's QDragMoveEvent is built on
  Qt's QDropEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDragMoveEvent that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'answerRect', 'accept', 'ignore'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDragMoveEvent::QDragMoveEvent(const QDragMoveEvent &a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDragMoveEvent &QDragMoveEvent::operator=(const QDragMoveEvent
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDragMoveEvent::~QDragMoveEvent()': the destructor: Python never
    removes a C++ QDragMoveEvent.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QDragMoveEvent is created at the first use, not by
    'QDragMoveEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDragMoveEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDragMoveEvent'

  #  A C++ QDragMoveEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDragMoveEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QDragMoveEvent]:
    """
    Calls Qt's 'QDragMoveEvent *QDragMoveEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#clone

    Returns
    -------

    Optional[QDragMoveEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDragMoveEvent *QDragMoveEvent::clone() const
    ritual = 'ritual_ZNK14QDragMoveEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QDragMoveEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QDragMoveEvent._cuteAt(address)

  def answerRect(self) -> QRect:
    """
    Calls Qt's 'QRect QDragMoveEvent::answerRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#answerRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDragMoveEvent::answerRect() const
    address = self.uglySide.call('ritual_ZNK14QDragMoveEvent10answerRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
  @overload(
      QPoint, Qt.DropActions, QMimeData, Qt.MouseButtons,
      Qt.KeyboardModifiers, QEvent.Type,
  )
  @overload(
      QPoint, Qt.DropActions, NoneType, Qt.MouseButtons,
      Qt.KeyboardModifiers, QEvent.Type,
  )
  def __init__(
      self,
      pos: QPoint,
      actions: Qt.DropActions,
      data: Optional[QMimeData],
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      type: QEvent.Type = QEvent.Type.DragMove,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDragMoveEvent::QDragMoveEvent(const
    QPoint &pos, Qt::DropActions actions, const QMimeData *data,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, Type type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#QDragMoveEvent

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

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.DragMove.
    """
    #  QDragMoveEvent::QDragMoveEvent(const QPoint &pos, Qt::DropActions
    #      actions, const QMimeData *data, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers, Type type)
    self._noteCreation(QDragMoveEvent, lambda: Rituals.call(
        'ritual_ZN14QDragMoveEventC1ERK6QPoint6QFlagsIN2Qt10DropActionEEPK9'
        'QMimeDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEEN6QEve'
        'nt4TypeE',
        self._valueOf(pos), actions.value, self._addressOf(data),
        buttons.value, modifiers.value, type.value,
    ))

  @overload(
      QPointF, Qt.DropActions, QMimeData, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QPointF, Qt.DropActions, NoneType, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QPointF, Qt.DropActions, QMimeData, Qt.MouseButtons,
      Qt.KeyboardModifiers, QEvent.Type,
  )
  @overload(
      QPointF, Qt.DropActions, NoneType, Qt.MouseButtons,
      Qt.KeyboardModifiers, QEvent.Type,
  )
  def __init__(
      self,
      pos: QPointF,
      actions: Qt.DropActions,
      data: Optional[QMimeData],
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      type: QEvent.Type = QEvent.Type.DragMove,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDragMoveEvent::QDragMoveEvent(QPointF
    pos, Qt::DropActions actions, const QMimeData *data, Qt::MouseButtons
    buttons, Qt::KeyboardModifiers modifiers, Type type)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#QDragMoveEvent

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

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.DragMove.
    """
    #  QDragMoveEvent::QDragMoveEvent(QPointF pos, Qt::DropActions actions,
    #      const QMimeData *data, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers, Type type)
    self._noteCreation(QDragMoveEvent, lambda: Rituals.call(
        'ritual_ZN14QDragMoveEventC1E7QPointF6QFlagsIN2Qt10DropActionEEPK9Q'
        'MimeDataS1_INS2_11MouseButtonEES1_INS2_16KeyboardModifierEEN6QEven'
        't4TypeE',
        self._valueOf(pos, 'QPointF'), actions.value, self._addressOf(data),
        buttons.value, modifiers.value, type.value,
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

  @overload()
  def accept(self) -> None:
    """
    Calls Qt's 'void QDragMoveEvent::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#accept
    """
    #  void QDragMoveEvent::accept()
    self.uglySide.call('ritual_ZN14QDragMoveEvent6acceptEv')

  @overload(QRect)
  def accept(self, r: QRect) -> None:
    """
    Calls Qt's 'void QDragMoveEvent::accept(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#accept

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QDragMoveEvent::accept(const QRect &r)
    self.uglySide.call(
        'ritual_ZN14QDragMoveEvent6acceptERK5QRect', self._valueOf(r),
    )

  @overload()
  def ignore(self) -> None:
    """
    Calls Qt's 'void QDragMoveEvent::ignore()'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#ignore
    """
    #  void QDragMoveEvent::ignore()
    self.uglySide.call('ritual_ZN14QDragMoveEvent6ignoreEv')

  @overload(QRect)
  def ignore(self, r: QRect) -> None:
    """
    Calls Qt's 'void QDragMoveEvent::ignore(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qdragmoveevent.html#ignore

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QDragMoveEvent::ignore(const QRect &r)
    self.uglySide.call(
        'ritual_ZN14QDragMoveEvent6ignoreERK5QRect', self._valueOf(r),
    )
