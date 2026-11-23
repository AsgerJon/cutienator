"""
QGraphicsSceneDragDropEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QGraphicsSceneEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMimeData, QPoint, QPointF
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneDragDropEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneDragDropEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneDragDropEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneDragDropEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneDragDropEvent that has a ritual and
  that Python can call so far, 21 names in all: 'pos', 'setPos', 'scenePos',
  'setScenePos', 'screenPos', 'setScreenPos', 'buttons', 'setButtons',
  'modifiers', 'setModifiers', 'possibleActions', 'setPossibleActions',
  'proposedAction', 'setProposedAction', 'acceptProposedAction',
  'dropAction', 'setDropAction', 'source', 'setSource', 'mimeData',
  'setMimeData'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneDragDropEvent::~QGraphicsSceneDragDropEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneDragDropEvent.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneDragDropEvent is created at the first use, not by
    'QGraphicsSceneDragDropEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneDragDropEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneDragDropEvent'

  #  A C++ QGraphicsSceneDragDropEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneDragDropEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneDragDropEvent::pos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneDragDropEvent::pos() const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneDragDropEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneDragDropEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneDragDropEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneDragDropEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QGraphicsSceneDragDropEvent::buttons()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QGraphicsSceneDragDropEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent7buttonsEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QGraphicsSceneDragDropEvent::modifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGraphicsSceneDragDropEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent9modifiersEv',
    ))

  def possibleActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions
    QGraphicsSceneDragDropEvent::possibleActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#possibleActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QGraphicsSceneDragDropEvent::possibleActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent15possibleActionsEv',
    ))

  def proposedAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QGraphicsSceneDragDropEvent::proposedAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#proposedAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QGraphicsSceneDragDropEvent::proposedAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent14proposedActionEv',
    ))

  def dropAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QGraphicsSceneDragDropEvent::dropAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#dropAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QGraphicsSceneDragDropEvent::dropAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent10dropActionEv',
    ))

  def source(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QGraphicsSceneDragDropEvent::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#source

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QGraphicsSceneDragDropEvent::source() const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent6sourceEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def mimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'const QMimeData *QGraphicsSceneDragDropEvent::mimeData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#mimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMimeData *QGraphicsSceneDragDropEvent::mimeData() const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsSceneDragDropEvent8mimeDataEv',
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneDragDropEvent::setPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent6setPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneDragDropEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent11setScenePosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneDragDropEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent12setScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.MouseButtons)
  def setButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphicsSceneDragDropEvent::setButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent10setButtonsE6QFlagsIN2Qt11M'
        'ouseButtonEE',
        buttons.value,
    )

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneDragDropEvent::setModifiers(Qt::KeyboardModifiers
    modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QGraphicsSceneDragDropEvent::setModifiers(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent12setModifiersE6QFlagsIN2Qt1'
        '6KeyboardModifierEE',
        modifiers.value,
    )

  @overload(Qt.DropActions)
  def setPossibleActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneDragDropEvent::setPossibleActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QGraphicsSceneDragDropEvent::setPossibleActions(Qt::DropActions
    #      actions)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent18setPossibleActionsE6QFlags'
        'IN2Qt10DropActionEE',
        actions.value,
    )

  @overload(Qt.DropAction)
  def setProposedAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneDragDropEvent::setProposedAction(Qt::DropAction action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setProposedAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QGraphicsSceneDragDropEvent::setProposedAction(Qt::DropAction
    #      action)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent17setProposedActionEN2Qt10Dr'
        'opActionE',
        action.value,
    )

  @overload(Qt.DropAction)
  def setDropAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneDragDropEvent::setDropAction(Qt::DropAction action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setDropAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QGraphicsSceneDragDropEvent::setDropAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent13setDropActionEN2Qt10DropAc'
        'tionE',
        action.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setSource(self, source: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setSource(QWidget
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setSource

    Parameters
    ----------

    source : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneDragDropEvent::setSource(QWidget *source)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent9setSourceEP7QWidget',
        self._addressOf(source),
    )

  @overload(QMimeData)
  @overload(NoneType)
  def setMimeData(self, data: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneDragDropEvent::setMimeData(const QMimeData
    *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html#setMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneDragDropEvent::setMimeData(const QMimeData *data)
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent11setMimeDataEPK9QMimeData',
        self._addressOf(data),
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
  @overload(QEvent.Type)
  def __init__(self, type: QEvent.Type = QEvent.Type.NULL) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSceneDragDropEvent::QGraphicsSceneDragDropEvent(Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneDragDropEvent::QGraphicsSceneDragDropEvent(Type type)
    self._noteCreation(QGraphicsSceneDragDropEvent, lambda: Rituals.call(
        'ritual_ZN27QGraphicsSceneDragDropEventC1EN6QEvent4TypeE',
        type.value,
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
    Calls Qt's 'void QGraphicsSceneDragDropEvent::acceptProposedAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenedragdropevent.html
    """
    #  void QGraphicsSceneDragDropEvent::acceptProposedAction()
    self.uglySide.call(
        'ritual_ZN27QGraphicsSceneDragDropEvent20acceptProposedActionEv',
    )
