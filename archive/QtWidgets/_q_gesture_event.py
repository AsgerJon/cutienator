"""
QGestureEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from . import QGesture, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGesture = WAIT['QGesture']
  QPointF = WAIT['QPointF']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGestureEvent(QEvent):
  """
  The cute side of Qt's QGestureEvent: a plain Python object standing in
  front of one C++ QGestureEvent.

  It is built on the cute 'QEvent', as Qt's QGestureEvent is built on Qt's
  QEvent, and has everything that class has.

  C++ hands a QGestureEvent around as a copy, so every C++ QGestureEvent
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGestureEvent that has a ritual and that Python can
  call so far, 11 names in all: 'gestures', 'gesture', 'activeGestures',
  'canceledGestures', 'setAccepted', 'accept', 'ignore', 'isAccepted',
  'setWidget', 'widget', 'mapToGraphicsScene'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGestureEvent::~QGestureEvent()': the destructor: Python removes
    its C++ QGestureEvent by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGestureEvent is created at the first use, not by
    'QGestureEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGestureEvent back gives a copy the ritual made for
    Python, in a new cute QGestureEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGestureEvent'

  #  A C++ QGestureEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGestureEvent'

  #  Qt's '~QGestureEvent()'. Naming it makes this a value class: Python owns
  #  every C++ QGestureEvent behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QGestureEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def gestures(self) -> QList[QGesture]:
    """
    Calls Qt's 'QList<QGesture *> QGestureEvent::gestures() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#gestures

    Returns
    -------

    QList[QGesture]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGesture *> QGestureEvent::gestures() const
    address = self.uglySide.call('ritual_ZNK13QGestureEvent8gesturesEv')
    from . import QGesture
    return QList[QGesture]._cuteOwning(address)

  @overload(Qt.GestureType)
  def gesture(self, type: Qt.GestureType) -> Optional[QGesture]:
    """
    Calls Qt's 'QGesture *QGestureEvent::gesture(Qt::GestureType type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#gesture

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.

    Returns
    -------

    Optional[QGesture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGesture *QGestureEvent::gesture(Qt::GestureType type) const
    address = self.uglySide.call(
        'ritual_ZNK13QGestureEvent7gestureEN2Qt11GestureTypeE', type.value,
    )
    from . import QGesture
    return QGesture._cuteAt(address)

  def activeGestures(self) -> QList[QGesture]:
    """
    Calls Qt's 'QList<QGesture *> QGestureEvent::activeGestures() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#activeGestures

    Returns
    -------

    QList[QGesture]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGesture *> QGestureEvent::activeGestures() const
    address = self.uglySide.call(
        'ritual_ZNK13QGestureEvent14activeGesturesEv',
    )
    from . import QGesture
    return QList[QGesture]._cuteOwning(address)

  def canceledGestures(self) -> QList[QGesture]:
    """
    Calls Qt's 'QList<QGesture *> QGestureEvent::canceledGestures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgestureevent.html#canceledGestures

    Returns
    -------

    QList[QGesture]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGesture *> QGestureEvent::canceledGestures() const
    address = self.uglySide.call(
        'ritual_ZNK13QGestureEvent16canceledGesturesEv',
    )
    from . import QGesture
    return QList[QGesture]._cuteOwning(address)

  @overload(QGesture)
  @overload(NoneType)
  def isAccepted(self, a0: Optional[QGesture]) -> bool:
    """
    Calls Qt's 'bool QGestureEvent::isAccepted(QGesture *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#isAccepted

    Parameters
    ----------

    a0 : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGestureEvent::isAccepted(QGesture *a0) const
    return self.uglySide.call(
        'ritual_ZNK13QGestureEvent10isAcceptedEP8QGesture',
        self._addressOf(a0),
    )

  @overload(Qt.GestureType)
  def isAccepted(self, a0: Qt.GestureType) -> bool:
    """
    Calls Qt's 'bool QGestureEvent::isAccepted(Qt::GestureType a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#isAccepted

    Parameters
    ----------

    a0 : Qt.GestureType
      Passed on as its number.
    """
    #  bool QGestureEvent::isAccepted(Qt::GestureType a0) const
    return self.uglySide.call(
        'ritual_ZNK13QGestureEvent10isAcceptedEN2Qt11GestureTypeE', a0.value,
    )

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QGestureEvent::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QGestureEvent::widget() const
    address = self.uglySide.call('ritual_ZNK13QGestureEvent6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QPointF)
  def mapToGraphicsScene(self, gesturePoint: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGestureEvent::mapToGraphicsScene(const QPointF
    &gesturePoint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgestureevent.html#mapToGraphicsScene

    Parameters
    ----------

    gesturePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGestureEvent::mapToGraphicsScene(const QPointF &gesturePoint)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QGestureEvent18mapToGraphicsSceneERK7QPointF',
        self._valueOf(gesturePoint),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGesture, bool)
  @overload(NoneType, bool)
  def setAccepted(self, a0: Optional[QGesture], a1: bool) -> None:
    """
    Calls Qt's 'void QGestureEvent::setAccepted(QGesture *a0, bool a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#setAccepted

    Parameters
    ----------

    a0 : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is.
    """
    #  void QGestureEvent::setAccepted(QGesture *a0, bool a1)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent11setAcceptedEP8QGestureb',
        self._addressOf(a0), a1,
    )

  @overload(Qt.GestureType, bool)
  def setAccepted(self, a0: Qt.GestureType, a1: bool) -> None:
    """
    Calls Qt's 'void QGestureEvent::setAccepted(Qt::GestureType a0, bool
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#setAccepted

    Parameters
    ----------

    a0 : Qt.GestureType
      Passed on as its number.

    a1 : bool
      Passed on as it is.
    """
    #  void QGestureEvent::setAccepted(Qt::GestureType a0, bool a1)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent11setAcceptedEN2Qt11GestureTypeEb',
        a0.value, a1,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGestureEvent::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureEvent::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent9setWidgetEP7QWidget',
        self._addressOf(widget),
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

  @overload(QList[QGesture])
  def __init__(self, gestures: QList[QGesture]) -> None:
    """
    Notes what was given, for Qt's 'QGestureEvent::QGestureEvent(const
    QList<QGesture *> &gestures)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#QGestureEvent

    Parameters
    ----------

    gestures : QList[QGesture]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGestureEvent::QGestureEvent(const QList<QGesture *> &gestures)
    self._noteCreation(QGestureEvent, lambda: Rituals.call(
        'ritual_ZN13QGestureEventC1ERK5QListIP8QGestureE',
        self._valueOf(gestures),
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

  @overload(QGesture)
  @overload(NoneType)
  def accept(self, a0: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QGestureEvent::accept(QGesture *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#accept

    Parameters
    ----------

    a0 : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureEvent::accept(QGesture *a0)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent6acceptEP8QGesture', self._addressOf(a0),
    )

  @overload(Qt.GestureType)
  def accept(self, a0: Qt.GestureType) -> None:
    """
    Calls Qt's 'void QGestureEvent::accept(Qt::GestureType a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#accept

    Parameters
    ----------

    a0 : Qt.GestureType
      Passed on as its number.
    """
    #  void QGestureEvent::accept(Qt::GestureType a0)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent6acceptEN2Qt11GestureTypeE', a0.value,
    )

  @overload(QGesture)
  @overload(NoneType)
  def ignore(self, a0: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QGestureEvent::ignore(QGesture *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#ignore

    Parameters
    ----------

    a0 : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureEvent::ignore(QGesture *a0)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent6ignoreEP8QGesture', self._addressOf(a0),
    )

  @overload(Qt.GestureType)
  def ignore(self, a0: Qt.GestureType) -> None:
    """
    Calls Qt's 'void QGestureEvent::ignore(Qt::GestureType a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgestureevent.html#ignore

    Parameters
    ----------

    a0 : Qt.GestureType
      Passed on as its number.
    """
    #  void QGestureEvent::ignore(Qt::GestureType a0)
    self.uglySide.call(
        'ritual_ZN13QGestureEvent6ignoreEN2Qt11GestureTypeE', a0.value,
    )
