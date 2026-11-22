"""
QDropEvent binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMimeData, QObject, QPoint, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDropEvent(QEvent):
  """
  The cute side of Qt's QDropEvent: a plain Python object standing in front
  of one C++ QDropEvent.

  It is built on the cute 'QEvent', as Qt's QDropEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDropEvent that has a ritual and that Python can
  call so far, 15 names in all: 'clone', 'pos', 'posF', 'mouseButtons',
  'keyboardModifiers', 'position', 'buttons', 'modifiers', 'possibleActions',
  'proposedAction', 'acceptProposedAction', 'dropAction', 'setDropAction',
  'source', 'mimeData'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDropEvent::~QDropEvent()': the destructor: Python never removes a
    C++ QDropEvent.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QDropEvent is created at the first use, not by 'QDropEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDropEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDropEvent'

  #  A C++ QDropEvent Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDropEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QDropEvent]:
    """
    Calls Qt's 'QDropEvent *QDropEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#clone

    Returns
    -------

    Optional[QDropEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDropEvent *QDropEvent::clone() const
    ritual = 'ritual_ZNK10QDropEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QDropEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QDropEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QDropEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QDropEvent::pos() const
    address = self.uglySide.call('ritual_ZNK10QDropEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def posF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QDropEvent::posF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#posF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDropEvent::posF() const
    address = self.uglySide.call('ritual_ZNK10QDropEvent4posFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def mouseButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QDropEvent::mouseButtons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#mouseButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QDropEvent::mouseButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK10QDropEvent12mouseButtonsEv',
    ))

  def keyboardModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QDropEvent::keyboardModifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#keyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QDropEvent::keyboardModifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK10QDropEvent17keyboardModifiersEv',
    ))

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QDropEvent::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDropEvent::position() const
    address = self.uglySide.call('ritual_ZNK10QDropEvent8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QDropEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QDropEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK10QDropEvent7buttonsEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QDropEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QDropEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK10QDropEvent9modifiersEv',
    ))

  def possibleActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QDropEvent::possibleActions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#possibleActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QDropEvent::possibleActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK10QDropEvent15possibleActionsEv',
    ))

  def proposedAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QDropEvent::proposedAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#proposedAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QDropEvent::proposedAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK10QDropEvent14proposedActionEv',
    ))

  def dropAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QDropEvent::dropAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#dropAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QDropEvent::dropAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK10QDropEvent10dropActionEv',
    ))

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDropEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#source

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDropEvent::source() const
    address = self.uglySide.call('ritual_ZNK10QDropEvent6sourceEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def mimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'const QMimeData *QDropEvent::mimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#mimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMimeData *QDropEvent::mimeData() const
    address = self.uglySide.call('ritual_ZNK10QDropEvent8mimeDataEv')
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.DropAction)
  def setDropAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QDropEvent::setDropAction(Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#setDropAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QDropEvent::setDropAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN10QDropEvent13setDropActionEN2Qt10DropActionE',
        action.value,
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
      type: QEvent.Type = QEvent.Type.Drop,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDropEvent::QDropEvent(const QPointF
    &pos, Qt::DropActions actions, const QMimeData *data, Qt::MouseButtons
    buttons, Qt::KeyboardModifiers modifiers, Type type)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdropevent.html#QDropEvent

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
      QEvent.Type.Drop.
    """
    #  QDropEvent::QDropEvent(const QPointF &pos, Qt::DropActions actions,
    #      const QMimeData *data, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers, Type type)
    self._noteCreation(QDropEvent, lambda: Rituals.call(
        'ritual_ZN10QDropEventC1ERK7QPointF6QFlagsIN2Qt10DropActionEEPK9QMi'
        'meDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEEN6QEvent4'
        'TypeE',
        self._valueOf(pos), actions.value, self._addressOf(data),
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

  def acceptProposedAction(self) -> None:
    """
    Calls Qt's 'void QDropEvent::acceptProposedAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdropevent.html#acceptProposedAction
    """
    #  void QDropEvent::acceptProposedAction()
    self.uglySide.call('ritual_ZN10QDropEvent20acceptProposedActionEv')
