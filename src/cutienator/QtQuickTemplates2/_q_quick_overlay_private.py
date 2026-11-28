"""
QQuickOverlayPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickOverlayPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPointF, QRectF
  from ..QtGui import QHoverEvent, QMouseEvent, QPointerEvent, QTouchEvent
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickOverlay, QQuickPopup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickOverlay = WAIT['QQuickOverlay']
  QQuickPopup = WAIT['QQuickPopup']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickOverlayPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickOverlayPrivate: a plain Python object standing
  in front of one C++ QQuickOverlayPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickOverlayPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has. Qt's
  QQuickOverlayPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickOverlayPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickOverlayPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'get',
  'eatEventIfBlockedByModal', 'startDrag', 'handlePress', 'handleMove',
  'handleMouseEvent', 'handleHoverEvent', 'handleTouchEvent', 'addPopup',
  'removePopup', 'setMouseGrabberPopup', 'stackingOrderPopups',
  'stackingOrderDrawers', 'itemGeometryChanged', 'itemRotationChanged',
  'updateGeometry'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickOverlay *QQuickOverlayPrivate::q_func() const': takes
    in Python what 'QQuickOverlay *QQuickOverlayPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickOverlayPrivate is created at the first use, not by
    'QQuickOverlayPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickOverlayPrivate.
  - Each name of Qt's QQuickOverlayPrivate that has no cute function yet,
    'handleRelease', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickOverlay)
  @overload(NoneType)
  def get(
      overlay: Optional[QQuickOverlay],
  ) -> Optional[QQuickOverlayPrivate]:
    """
    Calls Qt's 'QQuickOverlayPrivate *QQuickOverlayPrivate::get(QQuickOverlay
    *overlay)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayprivate.html#get

    Parameters
    ----------

    overlay : Optional[QQuickOverlay]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickOverlayPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlayPrivate *QQuickOverlayPrivate::get(QQuickOverlay
    #      *overlay)
    address = Rituals.call(
        'ritual_ZN20QQuickOverlayPrivate3getEP13QQuickOverlay',
        CuteMixin._addressOf(overlay),
    )
    return QQuickOverlayPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickOverlayPrivate'

  #  A C++ QQuickOverlayPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickOverlayPrivate'

  #  The functions Qt calls itself that QQuickOverlayPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem20Q'
           'QuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemRotationChanged': (
          ('_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stackingOrderPopups(self) -> QList[QQuickPopup]:
    """
    Calls Qt's 'QList<QQuickPopup *>
    QQuickOverlayPrivate::stackingOrderPopups() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#stackingOrderPopups

    Returns
    -------

    QList[QQuickPopup]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderPopups() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickOverlayPrivate19stackingOrderPopupsEv',
    )
    from . import QQuickPopup
    return QList[QQuickPopup]._cuteOwning(address)

  def stackingOrderDrawers(self) -> QList[QQuickPopup]:
    """
    Calls Qt's 'QList<QQuickPopup *>
    QQuickOverlayPrivate::stackingOrderDrawers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#stackingOrderDrawers

    Returns
    -------

    QList[QQuickPopup]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderDrawers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickOverlayPrivate20stackingOrderDrawersEv',
    )
    from . import QQuickPopup
    return QList[QQuickPopup]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPopup)
  @overload(NoneType)
  def setMouseGrabberPopup(self, popup: Optional[QQuickPopup]) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::setMouseGrabberPopup(QQuickPopup
    *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#setMouseGrabberPopup

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayPrivate::setMouseGrabberPopup(QQuickPopup *popup)
    self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate20setMouseGrabberPopupEP11QQuickPop'
        'up',
        self._addressOf(popup),
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

  def q_func(self) -> Optional[QQuickOverlay]:
    """
    Calls Qt's 'QQuickOverlay *QQuickOverlayPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayprivate.html#q_func

    Returns
    -------

    Optional[QQuickOverlay]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlay *QQuickOverlayPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickOverlayPrivate6q_funcEv')
    from . import QQuickOverlay
    return QQuickOverlay._cuteAt(address)

  @overload(QPointerEvent)
  @overload(NoneType)
  def eatEventIfBlockedByModal(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickOverlayPrivate::eatEventIfBlockedByModal(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#eatEventIfBlockedByModal

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickOverlayPrivate::eatEventIfBlockedByModal(QPointerEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate24eatEventIfBlockedByModalEP13QPoin'
        'terEvent',
        self._addressOf(event),
    )

  @overload(QEvent, QPointF)
  @overload(NoneType, QPointF)
  def startDrag(self, event: Optional[QEvent], pos: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::startDrag(QEvent *event, const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#startDrag

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickOverlayPrivate::startDrag(QEvent *event, const QPointF
    #      &pos)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate9startDragEP6QEventRK7QPointF',
        self._addressOf(event), self._valueOf(pos, 'QPointF'),
    )

  @overload(QQuickItem, QEvent, QQuickPopup)
  @overload(QQuickItem, QEvent, NoneType)
  @overload(QQuickItem, NoneType, QQuickPopup)
  @overload(QQuickItem, NoneType, NoneType)
  @overload(NoneType, QEvent, QQuickPopup)
  @overload(NoneType, QEvent, NoneType)
  @overload(NoneType, NoneType, QQuickPopup)
  @overload(NoneType, NoneType, NoneType)
  def handlePress(
      self,
      source: Optional[QQuickItem],
      event: Optional[QEvent],
      target: Optional[QQuickPopup],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::handlePress(QQuickItem *source,
    QEvent *event, QQuickPopup *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#handlePress

    Parameters
    ----------

    source : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickOverlayPrivate::handlePress(QQuickItem *source, QEvent
    #      *event, QQuickPopup *target)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate11handlePressEP10QQuickItemP6QEvent'
        'P11QQuickPopup',
        self._addressOf(source), self._addressOf(event),
        self._addressOf(target),
    )

  @overload(QQuickItem, QEvent, QQuickPopup)
  @overload(QQuickItem, QEvent, NoneType)
  @overload(QQuickItem, NoneType, QQuickPopup)
  @overload(QQuickItem, NoneType, NoneType)
  @overload(NoneType, QEvent, QQuickPopup)
  @overload(NoneType, QEvent, NoneType)
  @overload(NoneType, NoneType, QQuickPopup)
  @overload(NoneType, NoneType, NoneType)
  def handleMove(
      self,
      source: Optional[QQuickItem],
      event: Optional[QEvent],
      target: Optional[QQuickPopup],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::handleMove(QQuickItem *source,
    QEvent *event, QQuickPopup *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#handleMove

    Parameters
    ----------

    source : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickOverlayPrivate::handleMove(QQuickItem *source, QEvent
    #      *event, QQuickPopup *target)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate10handleMoveEP10QQuickItemP6QEventP'
        '11QQuickPopup',
        self._addressOf(source), self._addressOf(event),
        self._addressOf(target),
    )

  @overload(QQuickItem, QMouseEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  @overload(QQuickItem, QMouseEvent, QQuickPopup)
  @overload(QQuickItem, QMouseEvent, NoneType)
  @overload(QQuickItem, NoneType, QQuickPopup)
  @overload(QQuickItem, NoneType, NoneType)
  @overload(NoneType, QMouseEvent, QQuickPopup)
  @overload(NoneType, QMouseEvent, NoneType)
  @overload(NoneType, NoneType, QQuickPopup)
  @overload(NoneType, NoneType, NoneType)
  def handleMouseEvent(
      self,
      source: Optional[QQuickItem],
      event: Optional[QMouseEvent],
      target: Optional[QQuickPopup] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::handleMouseEvent(QQuickItem
    *source, QMouseEvent *event, QQuickPopup *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#handleMouseEvent

    Parameters
    ----------

    source : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQuickOverlayPrivate::handleMouseEvent(QQuickItem *source,
    #      QMouseEvent *event, QQuickPopup *target)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate16handleMouseEventEP10QQuickItemP11'
        'QMouseEventP11QQuickPopup',
        self._addressOf(source), self._addressOf(event),
        self._addressOf(target),
    )

  @overload(QQuickItem, QHoverEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QHoverEvent)
  @overload(NoneType, NoneType)
  @overload(QQuickItem, QHoverEvent, QQuickPopup)
  @overload(QQuickItem, QHoverEvent, NoneType)
  @overload(QQuickItem, NoneType, QQuickPopup)
  @overload(QQuickItem, NoneType, NoneType)
  @overload(NoneType, QHoverEvent, QQuickPopup)
  @overload(NoneType, QHoverEvent, NoneType)
  @overload(NoneType, NoneType, QQuickPopup)
  @overload(NoneType, NoneType, NoneType)
  def handleHoverEvent(
      self,
      source: Optional[QQuickItem],
      event: Optional[QHoverEvent],
      target: Optional[QQuickPopup] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::handleHoverEvent(QQuickItem
    *source, QHoverEvent *event, QQuickPopup *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#handleHoverEvent

    Parameters
    ----------

    source : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQuickOverlayPrivate::handleHoverEvent(QQuickItem *source,
    #      QHoverEvent *event, QQuickPopup *target)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate16handleHoverEventEP10QQuickItemP11'
        'QHoverEventP11QQuickPopup',
        self._addressOf(source), self._addressOf(event),
        self._addressOf(target),
    )

  @overload(QQuickItem, QTouchEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  @overload(QQuickItem, QTouchEvent, QQuickPopup)
  @overload(QQuickItem, QTouchEvent, NoneType)
  @overload(QQuickItem, NoneType, QQuickPopup)
  @overload(QQuickItem, NoneType, NoneType)
  @overload(NoneType, QTouchEvent, QQuickPopup)
  @overload(NoneType, QTouchEvent, NoneType)
  @overload(NoneType, NoneType, QQuickPopup)
  @overload(NoneType, NoneType, NoneType)
  def handleTouchEvent(
      self,
      source: Optional[QQuickItem],
      event: Optional[QTouchEvent],
      target: Optional[QQuickPopup] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlayPrivate::handleTouchEvent(QQuickItem
    *source, QTouchEvent *event, QQuickPopup *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#handleTouchEvent

    Parameters
    ----------

    source : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQuickOverlayPrivate::handleTouchEvent(QQuickItem *source,
    #      QTouchEvent *event, QQuickPopup *target)
    return self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate16handleTouchEventEP10QQuickItemP11'
        'QTouchEventP11QQuickPopup',
        self._addressOf(source), self._addressOf(event),
        self._addressOf(target),
    )

  @overload(QQuickPopup)
  @overload(NoneType)
  def addPopup(self, popup: Optional[QQuickPopup]) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::addPopup(QQuickPopup *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayprivate.html#addPopup

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayPrivate::addPopup(QQuickPopup *popup)
    self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate8addPopupEP11QQuickPopup',
        self._addressOf(popup),
    )

  @overload(QQuickPopup)
  @overload(NoneType)
  def removePopup(self, popup: Optional[QQuickPopup]) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::removePopup(QQuickPopup *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#removePopup

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayPrivate::removePopup(QQuickPopup *popup)
    self.uglySide.call(
        'ritual_ZN20QQuickOverlayPrivate11removePopupEP11QQuickPopup',
        self._addressOf(popup),
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem'
        '20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQui'
          'ckItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemRotationChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::itemRotationChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#itemRotationChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayPrivate::itemRotationChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQui'
          'ckItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayPrivate::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayprivate.html#updateGeometry
    """
    #  void QQuickOverlayPrivate::updateGeometry()
    self.uglySide.call('ritual_ZN20QQuickOverlayPrivate14updateGeometryEv')

  @staticmethod
  def handleRelease(*__, **_) -> Never:
    """
    Qt's 'bool QQuickOverlayPrivate::handleRelease(QQuickItem *source, QEvent
    *event, QQuickPopup *target)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'closedItselfViaCloseMultiple'.
    """
    raise NotImplementedError(
        "'QQuickOverlayPrivate.handleRelease' has no cute function yet. "
        "Qt's 'bool QQuickOverlayPrivate::handleRelease(QQuickItem *source, "
        "QEvent *event, QQuickPopup *target)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'closedItselfViaCloseMultiple'.")
