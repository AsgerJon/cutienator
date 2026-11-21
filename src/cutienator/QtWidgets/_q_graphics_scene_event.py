"""
QGraphicsSceneEvent binding of the Qt C++
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
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneEvent(QEvent):
  """
  The cute side of Qt's QGraphicsSceneEvent: a plain Python object standing
  in front of one C++ QGraphicsSceneEvent.

  It is built on the cute 'QEvent', as Qt's QGraphicsSceneEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneEvent that has a ritual and that
  Python can call so far, 4 names in all: 'widget', 'setWidget', 'timestamp',
  'setTimestamp'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneEvent::~QGraphicsSceneEvent()': the destructor:
    Python never removes a C++ QGraphicsSceneEvent.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneEvent is created at the first use, not by
    'QGraphicsSceneEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QGraphicsSceneEvent::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneevent.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QGraphicsSceneEvent::widget() const
    address = self.uglySide.call('ritual_ZNK19QGraphicsSceneEvent6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def timestamp(self) -> int:
    """
    Calls Qt's 'quint64 QGraphicsSceneEvent::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneevent.html#timestamp
    """
    #  quint64 QGraphicsSceneEvent::timestamp() const
    return self.uglySide.call('ritual_ZNK19QGraphicsSceneEvent9timestampEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneEvent::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneevent.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneEvent::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QGraphicsSceneEvent9setWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(int)
  def setTimestamp(self, ts: int) -> None:
    """
    Calls Qt's 'void QGraphicsSceneEvent::setTimestamp(quint64 ts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneevent.html#setTimestamp

    Parameters
    ----------

    ts : int
      Passed on as it is.
    """
    #  void QGraphicsSceneEvent::setTimestamp(quint64 ts)
    self.uglySide.call('ritual_ZN19QGraphicsSceneEvent12setTimestampEy', ts)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QEvent.Type)
  def __init__(self, type: QEvent.Type) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSceneEvent::QGraphicsSceneEvent(Type type)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneevent.html#QGraphicsSceneEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.
    """
    #  QGraphicsSceneEvent::QGraphicsSceneEvent(Type type)
    self._noteCreation(QGraphicsSceneEvent, lambda: Rituals.call(
        'ritual_ZN19QGraphicsSceneEventC1EN6QEvent4TypeE', type.value,
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
