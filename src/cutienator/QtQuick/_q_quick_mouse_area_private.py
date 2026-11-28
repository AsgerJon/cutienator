"""
QQuickMouseAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmousearea_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickMouseAreaPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtGui import QMouseEvent
  from . import QQuickItem, QQuickMouseArea, QQuickMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickMouseEvent = WAIT['QQuickMouseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMouseAreaPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickMouseAreaPrivate: a plain Python object
  standing in front of one C++ QQuickMouseAreaPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickMouseAreaPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMouseAreaPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'saveEvent', 'propagate',
  'propagateHelper', 'isPressAndHoldConnected', 'isDoubleClickConnected',
  'isClickConnected', 'isWheelConnected'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMouseArea *QQuickMouseAreaPrivate::q_func() const':
    takes in Python what 'QQuickMouseArea *QQuickMouseAreaPrivate::q_func()'
    takes.
  - Qt's 'QQuickMouseAreaPrivate::~QQuickMouseAreaPrivate()': the destructor:
    Python never removes a C++ QQuickMouseAreaPrivate.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickMouseAreaPrivate is created at the first use, not by
    'QQuickMouseAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMouseAreaPrivate.
  """

  #  The enums Qt writes inside QQuickMouseAreaPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class PropagateType(CuteNum):
    """
    The enum 'QQuickMouseAreaPrivate::PropagateType' of Qt, with the 3 names
    Qt gives in it.
    """

    Click = Kee[int](0)
    DoubleClick = Kee[int](1)
    PressAndHold = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMouseAreaPrivate'

  #  A C++ QQuickMouseAreaPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMouseAreaPrivate'

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
    Notes what was given, for Qt's
    'QQuickMouseAreaPrivate::QQuickMouseAreaPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#QQuickMouseAreaPrivate
    """
    #  QQuickMouseAreaPrivate::QQuickMouseAreaPrivate()
    self._noteCreation(QQuickMouseAreaPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickMouseAreaPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickMouseArea]:
    """
    Calls Qt's 'QQuickMouseArea *QQuickMouseAreaPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmouseareaprivate.html#q_func

    Returns
    -------

    Optional[QQuickMouseArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMouseArea *QQuickMouseAreaPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate6q_funcEv',
    )
    from . import QQuickMouseArea
    return QQuickMouseArea._cuteAt(address)

  @overload(QMouseEvent)
  @overload(NoneType)
  def saveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseAreaPrivate::saveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#saveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseAreaPrivate::saveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate9saveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QQuickMouseEvent, PropagateType)
  @overload(NoneType, PropagateType)
  def propagate(
      self,
      event: Optional[QQuickMouseEvent],
      a1: PropagateType,
  ) -> None:
    """
    Calls Qt's 'void QQuickMouseAreaPrivate::propagate(QQuickMouseEvent
    *event, PropagateType a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#propagate

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : PropagateType
      Passed on as its number.
    """
    #  void QQuickMouseAreaPrivate::propagate(QQuickMouseEvent *event,
    #      PropagateType a1)
    self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate9propagateEP16QQuickMouseEventNS_'
        '13PropagateTypeE',
        self._addressOf(event), a1.value,
    )

  @overload(QQuickMouseEvent, QQuickItem, QPointF, PropagateType)
  @overload(QQuickMouseEvent, NoneType, QPointF, PropagateType)
  @overload(NoneType, QQuickItem, QPointF, PropagateType)
  @overload(NoneType, NoneType, QPointF, PropagateType)
  def propagateHelper(
      self,
      a0: Optional[QQuickMouseEvent],
      a1: Optional[QQuickItem],
      a2: QPointF,
      a3: PropagateType,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMouseAreaPrivate::propagateHelper(QQuickMouseEvent
    *a0, QQuickItem *a1, const QPointF &a2, PropagateType a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#propagateHelper

    Parameters
    ----------

    a0 : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a3 : PropagateType
      Passed on as its number.
    """
    #  bool QQuickMouseAreaPrivate::propagateHelper(QQuickMouseEvent *a0,
    #      QQuickItem *a1, const QPointF &a2, PropagateType a3)
    return self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate15propagateHelperEP16QQuickMouseE'
        'ventP10QQuickItemRK7QPointFNS_13PropagateTypeE',
        self._addressOf(a0), self._addressOf(a1), self._valueOf(a2,
        'QPointF'), a3.value,
    )

  def isPressAndHoldConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseAreaPrivate::isPressAndHoldConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html
    """
    #  bool QQuickMouseAreaPrivate::isPressAndHoldConnected()
    return self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate23isPressAndHoldConnectedEv',
    )

  def isDoubleClickConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseAreaPrivate::isDoubleClickConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#isDoubleClickConnected
    """
    #  bool QQuickMouseAreaPrivate::isDoubleClickConnected()
    return self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate22isDoubleClickConnectedEv',
    )

  def isClickConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseAreaPrivate::isClickConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#isClickConnected
    """
    #  bool QQuickMouseAreaPrivate::isClickConnected()
    return self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate16isClickConnectedEv',
    )

  def isWheelConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseAreaPrivate::isWheelConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmouseareaprivate.html#isWheelConnected
    """
    #  bool QQuickMouseAreaPrivate::isWheelConnected()
    return self.uglySide.call(
        'ritual_ZN22QQuickMouseAreaPrivate16isWheelConnectedEv',
    )
