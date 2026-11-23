"""
QSinglePointEvent binding of the Qt C++
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
from . import QPointerEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QPointF
  from . import QEventPoint, QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QObject = WAIT['QObject']
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSinglePointEvent(QPointerEvent):
  """
  The cute side of Qt's QSinglePointEvent: a plain Python object standing in
  front of one C++ QSinglePointEvent.

  It is built on the cute 'QPointerEvent', as Qt's QSinglePointEvent is built
  on Qt's QPointerEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSinglePointEvent that has a ritual and that Python
  can call so far, 11 names in all: 'clone', 'button', 'buttons', 'position',
  'scenePosition', 'globalPosition', 'isBeginEvent', 'isUpdateEvent',
  'isEndEvent', 'exclusivePointGrabber', 'setExclusivePointGrabber'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSinglePointEvent::~QSinglePointEvent()': the destructor: Python
    never removes a C++ QSinglePointEvent.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 2 declared and nowhere to be found; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSinglePointEvent is created at the first use, not by
    'QSinglePointEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSinglePointEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSinglePointEvent'

  #  A C++ QSinglePointEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSinglePointEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QSinglePointEvent]:
    """
    Calls Qt's 'QSinglePointEvent *QSinglePointEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#clone

    Returns
    -------

    Optional[QSinglePointEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSinglePointEvent *QSinglePointEvent::clone() const
    ritual = 'ritual_ZNK17QSinglePointEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSinglePointEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QSinglePointEvent._cuteAt(address)

  def button(self) -> Qt.MouseButton:
    """
    Calls Qt's 'Qt::MouseButton QSinglePointEvent::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#button

    Returns
    -------

    Qt.MouseButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.MouseButton(number)'
      gives.
    """
    #  Qt::MouseButton QSinglePointEvent::button() const
    return Qt.MouseButton(self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent6buttonEv',
    ))

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QSinglePointEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QSinglePointEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent7buttonsEv',
    ))

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::position() const
    address = self.uglySide.call('ritual_ZNK17QSinglePointEvent8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::scenePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#scenePosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::scenePosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent13scenePositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::globalPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#globalPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::globalPosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent14globalPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def isBeginEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isBeginEvent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#isBeginEvent
    """
    #  bool QSinglePointEvent::isBeginEvent() const
    ritual = 'ritual_ZNK17QSinglePointEvent12isBeginEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSinglePointEvent12isBeginEventEv'
    return self.uglySide.call(ritual)

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isUpdateEvent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#isUpdateEvent
    """
    #  bool QSinglePointEvent::isUpdateEvent() const
    ritual = 'ritual_ZNK17QSinglePointEvent13isUpdateEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSinglePointEvent13isUpdateEventEv'
    return self.uglySide.call(ritual)

  def isEndEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isEndEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#isEndEvent
    """
    #  bool QSinglePointEvent::isEndEvent() const
    ritual = 'ritual_ZNK17QSinglePointEvent10isEndEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSinglePointEvent10isEndEventEv'
    return self.uglySide.call(ritual)

  def exclusivePointGrabber(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QSinglePointEvent::exclusivePointGrabber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#exclusivePointGrabber

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QSinglePointEvent::exclusivePointGrabber() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent21exclusivePointGrabberEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setExclusivePointGrabber(
      self,
      exclusiveGrabber: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QSinglePointEvent::setExclusivePointGrabber(QObject
    *exclusiveGrabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#setExclusivePointGrabber

    Parameters
    ----------

    exclusiveGrabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSinglePointEvent::setExclusivePointGrabber(QObject
    #      *exclusiveGrabber)
    self.uglySide.call(
        'ritual_ZN17QSinglePointEvent24setExclusivePointGrabberEP7QObject',
        self._addressOf(exclusiveGrabber),
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
      QEvent.Type, QPointingDevice, QEventPoint, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, Qt.MouseEventSource,
  )
  @overload(
      QEvent.Type, NoneType, QEventPoint, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers, Qt.MouseEventSource,
  )
  def __init__(
      self,
      type: QEvent.Type,
      dev: Optional[QPointingDevice],
      point: QEventPoint,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      source: Qt.MouseEventSource,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSinglePointEvent::QSinglePointEvent(Type
    type, const QPointingDevice *dev, const QEventPoint &point,
    Qt::MouseButton button, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    modifiers, Qt::MouseEventSource source)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#QSinglePointEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    source : Qt.MouseEventSource
      Passed on as its number.
    """
    #  QSinglePointEvent::QSinglePointEvent(Type type, const QPointingDevice
    #      *dev, const QEventPoint &point, Qt::MouseButton button,
    #      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    #      Qt::MouseEventSource source)
    self._noteCreation(QSinglePointEvent, lambda: Rituals.call(
        'ritual_ZN17QSinglePointEventC1EN6QEvent4TypeEPK15QPointingDeviceRK'
        '11QEventPointN2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16KeyboardModif'
        'ierEENS8_16MouseEventSourceE',
        type.value, self._addressOf(dev), self._valueOf(point), button.value,
        buttons.value, modifiers.value, source.value,
    ))

  @overload(
      QEvent.Type, QPointingDevice, QPointF, QPointF, QPointF,
      Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
  )
  @overload(
      QEvent.Type, NoneType, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers,
  )
  @overload(
      QEvent.Type, QPointingDevice, QPointF, QPointF, QPointF,
      Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers,
      Qt.MouseEventSource,
  )
  @overload(
      QEvent.Type, NoneType, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, Qt.MouseEventSource,
  )
  def __init__(
      self,
      type: QEvent.Type,
      dev: Optional[QPointingDevice],
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      source: Qt.MouseEventSource = (
          Qt.MouseEventSource.MouseEventNotSynthesized),
  ) -> None:
    """
    Notes what was given, for Qt's 'QSinglePointEvent::QSinglePointEvent(Type
    type, const QPointingDevice *dev, const QPointF &localPos, const QPointF
    &scenePos, const QPointF &globalPos, Qt::MouseButton button,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    Qt::MouseEventSource source)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#QSinglePointEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    source : Qt.MouseEventSource
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventSource.MouseEventNotSynthesized.
    """
    #  QSinglePointEvent::QSinglePointEvent(Type type, const QPointingDevice
    #      *dev, const QPointF &localPos, const QPointF &scenePos, const
    #      QPointF &globalPos, Qt::MouseButton button, Qt::MouseButtons
    #      buttons, Qt::KeyboardModifiers modifiers, Qt::MouseEventSource
    #      source)
    self._noteCreation(QSinglePointEvent, lambda: Rituals.call(
        'ritual_ZN17QSinglePointEventC1EN6QEvent4TypeEPK15QPointingDeviceRK'
        '7QPointFS7_S7_N2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16KeyboardModi'
        'fierEENS8_16MouseEventSourceE',
        type.value, self._addressOf(dev), self._valueOf(localPos),
        self._valueOf(scenePos), self._valueOf(globalPos), button.value,
        buttons.value, modifiers.value, source.value,
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
