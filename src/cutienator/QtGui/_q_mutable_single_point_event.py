"""
QMutableSinglePointEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qevent_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMutableSinglePointEvent to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QSinglePointEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEventPoint, QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMutableSinglePointEvent(QSinglePointEvent):
  """
  The cute side of Qt's QMutableSinglePointEvent: a plain Python object
  standing in front of one C++ QMutableSinglePointEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's
  QMutableSinglePointEvent is built on Qt's QSinglePointEvent, and has
  everything that class has.

  C++ hands a QMutableSinglePointEvent around as a copy, so every C++
  QMutableSinglePointEvent behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMutableSinglePointEvent that has a ritual and that
  Python can call so far, 3 names in all: 'setSource', 'isDoubleClick',
  'setDoubleClick'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMutableSinglePointEvent::QMutableSinglePointEvent(const
    QSinglePointEvent &other)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QMutableSinglePointEvent::~QMutableSinglePointEvent()': the
    destructor: Python removes its C++ QMutableSinglePointEvent by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QMutableSinglePointEvent is created at the first use, not by
    'QMutableSinglePointEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMutableSinglePointEvent back gives a copy the ritual
    made for Python, in a new cute QMutableSinglePointEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMutableSinglePointEvent'

  #  A C++ QMutableSinglePointEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMutableSinglePointEvent'

  #  Qt's '~QMutableSinglePointEvent()'. Naming it makes this a value class:
  #  Python owns every C++ QMutableSinglePointEvent behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QMutableSinglePointEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.MouseEventSource)
  def setSource(self, s: Qt.MouseEventSource) -> None:
    """
    Calls Qt's 'void QMutableSinglePointEvent::setSource(Qt::MouseEventSource
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html#setSource

    Parameters
    ----------

    s : Qt.MouseEventSource
      Passed on as its number.
    """
    #  void QMutableSinglePointEvent::setSource(Qt::MouseEventSource s)
    self.uglySide.call(
        'ritual_ZN24QMutableSinglePointEvent9setSourceEN2Qt16MouseEventSour'
        'ceE',
        s.value,
    )

  @overload()
  @overload(bool)
  def setDoubleClick(self, d: bool = True) -> None:
    """
    Calls Qt's 'void QMutableSinglePointEvent::setDoubleClick(bool d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html#setDoubleClick

    Parameters
    ----------

    d : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMutableSinglePointEvent::setDoubleClick(bool d)
    self.uglySide.call(
        'ritual_ZN24QMutableSinglePointEvent14setDoubleClickEb', d,
    )

  @staticmethod
  @overload(QSinglePointEvent, bool)
  @overload(NoneType, bool)
  def setDoubleClick(ev: Optional[QSinglePointEvent], d: bool) -> None:
    """
    Calls Qt's 'void
    QMutableSinglePointEvent::setDoubleClick(QSinglePointEvent *ev, bool d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html#setDoubleClick

    Parameters
    ----------

    ev : Optional[QSinglePointEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : bool
      Passed on as it is.
    """
    #  void QMutableSinglePointEvent::setDoubleClick(QSinglePointEvent *ev,
    #      bool d)
    Rituals.call(
        'ritual_ZN24QMutableSinglePointEvent14setDoubleClickEP17QSinglePoin'
        'tEventb',
        CuteMixin._addressOf(ev), d,
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

  @overload(QEvent.Type, QPointingDevice, QEventPoint)
  @overload(QEvent.Type, NoneType, QEventPoint)
  @overload(QEvent.Type, QPointingDevice, QEventPoint, Qt.MouseButton)
  @overload(QEvent.Type, NoneType, QEventPoint, Qt.MouseButton)
  @overload(
      QEvent.Type, QPointingDevice, QEventPoint, Qt.MouseButton,
      Qt.MouseButtons,
  )
  @overload(
      QEvent.Type, NoneType, QEventPoint, Qt.MouseButton, Qt.MouseButtons,
  )
  @overload(
      QEvent.Type, QPointingDevice, QEventPoint, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers,
  )
  @overload(
      QEvent.Type, NoneType, QEventPoint, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
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
      device: Optional[QPointingDevice],
      point: QEventPoint,
      button: Qt.MouseButton = Qt.MouseButton.NoButton,
      buttons: Qt.MouseButtons = Qt.MouseButtons.NoButton,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      source: Qt.MouseEventSource = (
          Qt.MouseEventSource.MouseEventSynthesizedByQt),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMutableSinglePointEvent::QMutableSinglePointEvent(Type type, const
    QPointingDevice *device, const QEventPoint &point, Qt::MouseButton
    button, Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    Qt::MouseEventSource source)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButton.NoButton.

    buttons : Qt.MouseButtons
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButtons.NoButton.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    source : Qt.MouseEventSource
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventSource.MouseEventSynthesizedByQt.
    """
    #  QMutableSinglePointEvent::QMutableSinglePointEvent(Type type, const
    #      QPointingDevice *device, const QEventPoint &point, Qt::MouseButton
    #      button, Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    #      Qt::MouseEventSource source)
    self._noteCreation(QMutableSinglePointEvent, lambda: Rituals.call(
        'ritual_ZN24QMutableSinglePointEventC1EN6QEvent4TypeEPK15QPointingD'
        'eviceRK11QEventPointN2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16Keyboa'
        'rdModifierEENS8_16MouseEventSourceE',
        type.value, self._addressOf(device), self._valueOf(point),
        button.value, buttons.value, modifiers.value, source.value,
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
  def isDoubleClick(self) -> bool:
    """
    Calls Qt's 'bool QMutableSinglePointEvent::isDoubleClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html#isDoubleClick
    """
    #  bool QMutableSinglePointEvent::isDoubleClick()
    return self.uglySide.call(
        'ritual_ZN24QMutableSinglePointEvent13isDoubleClickEv',
    )

  @staticmethod
  @overload(QSinglePointEvent)
  @overload(NoneType)
  def isDoubleClick(ev: Optional[QSinglePointEvent]) -> bool:
    """
    Calls Qt's 'bool QMutableSinglePointEvent::isDoubleClick(const
    QSinglePointEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutablesinglepointevent.html#isDoubleClick

    Parameters
    ----------

    ev : Optional[QSinglePointEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMutableSinglePointEvent::isDoubleClick(const QSinglePointEvent
    #      *ev)
    return Rituals.call(
        'ritual_ZN24QMutableSinglePointEvent13isDoubleClickEPK17QSinglePoin'
        'tEvent',
        CuteMixin._addressOf(ev),
    )
