"""
QQuickDrawer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDrawer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QMouseEvent, QTouchEvent
  from ..QtQuick import QQuickItem
  from . import QQuickDrawerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDrawer(QQuickPopup):
  """
  The cute side of Qt's QQuickDrawer: a plain Python object standing in front
  of one C++ QQuickDrawer.

  It is built on the cute 'QQuickPopup', as Qt's QQuickDrawer is built on
  Qt's QQuickPopup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDrawer that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'edge', 'setEdge',
  'position', 'setPosition', 'dragMargin', 'setDragMargin',
  'resetDragMargin', 'isInteractive', 'setInteractive', 'edgeChanged',
  'positionChanged', 'dragMarginChanged', 'interactiveChanged',
  'childMouseEventFilter', 'mouseMoveEvent', 'overlayEvent', 'touchEvent',
  'geometryChange', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDrawer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDrawer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickDrawerPrivate *QQuickDrawer::d_func() const': takes in
    Python what 'QQuickDrawerPrivate *QQuickDrawer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDrawer is created at the first use, not by
    'QQuickDrawer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDrawer.
  - Qt tells when it has removed the C++ QQuickDrawer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickDrawer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickDrawer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickDrawer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDrawer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDrawer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDrawer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickDrawer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def edge(self) -> Qt.Edge:
    """
    Calls Qt's 'Qt::Edge QQuickDrawer::edge() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#edge

    Returns
    -------

    Qt.Edge
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Edge(number)' gives.
    """
    #  Qt::Edge QQuickDrawer::edge() const
    return Qt.Edge(self.uglySide.call('ritual_ZNK12QQuickDrawer4edgeEv'))

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrawer::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#position
    """
    #  qreal QQuickDrawer::position() const
    return self.uglySide.call('ritual_ZNK12QQuickDrawer8positionEv')

  def dragMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrawer::dragMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#dragMargin
    """
    #  qreal QQuickDrawer::dragMargin() const
    return self.uglySide.call('ritual_ZNK12QQuickDrawer10dragMarginEv')

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrawer::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#isInteractive
    """
    #  bool QQuickDrawer::isInteractive() const
    return self.uglySide.call('ritual_ZNK12QQuickDrawer13isInteractiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Edge)
  def setEdge(self, edge: Qt.Edge) -> None:
    """
    Calls Qt's 'void QQuickDrawer::setEdge(Qt::Edge edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#setEdge

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  void QQuickDrawer::setEdge(Qt::Edge edge)
    self.uglySide.call(
        'ritual_ZN12QQuickDrawer7setEdgeEN2Qt4EdgeE', edge.value,
    )

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickDrawer::setPosition(qreal position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickDrawer::setPosition(qreal position)
    self.uglySide.call('ritual_ZN12QQuickDrawer11setPositionEd', position)

  @overload(float)
  def setDragMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickDrawer::setDragMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#setDragMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickDrawer::setDragMargin(qreal margin)
    self.uglySide.call('ritual_ZN12QQuickDrawer13setDragMarginEd', margin)

  @overload(bool)
  def setInteractive(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QQuickDrawer::setInteractive(bool interactive)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#setInteractive

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QQuickDrawer::setInteractive(bool interactive)
    self.uglySide.call(
        'ritual_ZN12QQuickDrawer14setInteractiveEb', interactive,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickDrawer::QQuickDrawer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#QQuickDrawer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDrawer::QQuickDrawer(QObject *parent)
    self._noteCreation(QQuickDrawer, lambda: Rituals.call(
        'ritual_ZN12QQuickDrawerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def resetDragMargin(self) -> None:
    """
    Calls Qt's 'void QQuickDrawer::resetDragMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#resetDragMargin
    """
    #  void QQuickDrawer::resetDragMargin()
    self.uglySide.call('ritual_ZN12QQuickDrawer15resetDragMarginEv')

  def edgeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrawer::edgeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#edgeChanged
    """
    #  void QQuickDrawer::edgeChanged()
    self.uglySide.call('ritual_ZN12QQuickDrawer11edgeChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrawer::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#positionChanged
    """
    #  void QQuickDrawer::positionChanged()
    self.uglySide.call('ritual_ZN12QQuickDrawer15positionChangedEv')

  def dragMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrawer::dragMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawer.html#dragMarginChanged
    """
    #  void QQuickDrawer::dragMarginChanged()
    self.uglySide.call('ritual_ZN12QQuickDrawer17dragMarginChangedEv')

  def interactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrawer::interactiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawer.html#interactiveChanged
    """
    #  void QQuickDrawer::interactiveChanged()
    self.uglySide.call('ritual_ZN12QQuickDrawer18interactiveChangedEv')

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      child: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawer::childMouseEventFilter(QQuickItem *child,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawer.html#childMouseEventFilter

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDrawer::childMouseEventFilter(QQuickItem *child, QEvent
    #      *event)
    ritual = (
        'ritual_ZN12QQuickDrawer21childMouseEventFilterEP10QQuickItemP6QEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickDrawer21childMouseEventFilterEP10QQuickItem'
          'P6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(child), self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickDrawer::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDrawer::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN12QQuickDrawer14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDrawer14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def overlayEvent(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawer::overlayEvent(QQuickItem *item, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#overlayEvent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDrawer::overlayEvent(QQuickItem *item, QEvent *event)
    ritual = 'ritual_ZN12QQuickDrawer12overlayEventEP10QQuickItemP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickDrawer12overlayEventEP10QQuickItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickDrawer::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDrawer::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN12QQuickDrawer10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDrawer10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickDrawer::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickDrawer::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN12QQuickDrawer14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDrawer14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def d_func(self) -> Optional[QQuickDrawerPrivate]:
    """
    Calls Qt's 'QQuickDrawerPrivate *QQuickDrawer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawer.html#d_func

    Returns
    -------

    Optional[QQuickDrawerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDrawerPrivate *QQuickDrawer::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickDrawer6d_funcEv')
    from . import QQuickDrawerPrivate
    return QQuickDrawerPrivate._cuteAt(address)
