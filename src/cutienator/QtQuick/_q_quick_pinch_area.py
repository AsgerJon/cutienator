"""
QQuickPinchArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPinchArea to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QTouchEvent
  from . import QQuickPinch, QQuickPinchAreaPrivate, QQuickPinchEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickPinchEvent = WAIT['QQuickPinchEvent']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPinchArea(QQuickItem):
  """
  The cute side of Qt's QQuickPinchArea: a plain Python object standing in
  front of one C++ QQuickPinchArea.

  It is built on the cute 'QQuickItem', as Qt's QQuickPinchArea is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPinchArea that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'isEnabled',
  'setEnabled', 'pinch', 'enabledChanged', 'pinchStarted', 'pinchUpdated',
  'pinchFinished', 'smartZoom', 'childMouseEventFilter', 'touchEvent',
  'geometryChange', 'itemChange', 'event', 'clearPinch', 'cancelPinch',
  'updatePinch', 'updatePinchTarget', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPinchArea::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPinchArea::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPinchArea::~QQuickPinchArea()': the destructor: Python never
    removes a C++ QQuickPinchArea.
  - Qt's 'const QQuickPinchAreaPrivate *QQuickPinchArea::d_func() const':
    takes in Python what 'QQuickPinchAreaPrivate *QQuickPinchArea::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPinchArea is created at the first use, not by
    'QQuickPinchArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPinchArea.
  - Qt tells when it has removed the C++ QQuickPinchArea. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickPinchArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#tr

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
    #  QString QQuickPinchArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickPinchArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPinchArea'

  #  A C++ QQuickPinchArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPinchArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPinchArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPinchArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickPinchArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickPinchArea::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#isEnabled
    """
    #  bool QQuickPinchArea::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QQuickPinchArea9isEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPinchArea::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN15QQuickPinchArea10setEnabledEb', a0)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPinchArea::QQuickPinchArea(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpincharea.html#QQuickPinchArea

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPinchArea::QQuickPinchArea(QQuickItem *parent)
    self._noteCreation(QQuickPinchArea, lambda: Rituals.call(
        'ritual_ZN15QQuickPinchAreaC1EP10QQuickItem',
        self._addressOf(parent),
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

  def pinch(self) -> Optional[QQuickPinch]:
    """
    Calls Qt's 'QQuickPinch *QQuickPinchArea::pinch()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#pinch

    Returns
    -------

    Optional[QQuickPinch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPinch *QQuickPinchArea::pinch()
    address = self.uglySide.call('ritual_ZN15QQuickPinchArea5pinchEv')
    from . import QQuickPinch
    return QQuickPinch._cuteAt(address)

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpincharea.html#enabledChanged
    """
    #  void QQuickPinchArea::enabledChanged()
    self.uglySide.call('ritual_ZN15QQuickPinchArea14enabledChangedEv')

  @overload(QQuickPinchEvent)
  @overload(NoneType)
  def pinchStarted(self, pinch: Optional[QQuickPinchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::pinchStarted(QQuickPinchEvent *pinch)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#pinchStarted

    Parameters
    ----------

    pinch : Optional[QQuickPinchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::pinchStarted(QQuickPinchEvent *pinch)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea12pinchStartedEP16QQuickPinchEvent',
        self._addressOf(pinch),
    )

  @overload(QQuickPinchEvent)
  @overload(NoneType)
  def pinchUpdated(self, pinch: Optional[QQuickPinchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::pinchUpdated(QQuickPinchEvent *pinch)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#pinchUpdated

    Parameters
    ----------

    pinch : Optional[QQuickPinchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::pinchUpdated(QQuickPinchEvent *pinch)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea12pinchUpdatedEP16QQuickPinchEvent',
        self._addressOf(pinch),
    )

  @overload(QQuickPinchEvent)
  @overload(NoneType)
  def pinchFinished(self, pinch: Optional[QQuickPinchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::pinchFinished(QQuickPinchEvent
    *pinch)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#pinchFinished

    Parameters
    ----------

    pinch : Optional[QQuickPinchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::pinchFinished(QQuickPinchEvent *pinch)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea13pinchFinishedEP16QQuickPinchEvent',
        self._addressOf(pinch),
    )

  @overload(QQuickPinchEvent)
  @overload(NoneType)
  def smartZoom(self, pinch: Optional[QQuickPinchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::smartZoom(QQuickPinchEvent *pinch)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#smartZoom

    Parameters
    ----------

    pinch : Optional[QQuickPinchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::smartZoom(QQuickPinchEvent *pinch)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea9smartZoomEP16QQuickPinchEvent',
        self._addressOf(pinch),
    )

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      i: Optional[QQuickItem],
      e: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPinchArea::childMouseEventFilter(QQuickItem *i,
    QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpincharea.html#childMouseEventFilter

    Parameters
    ----------

    i : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPinchArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
    ritual = (
        'ritual_ZN15QQuickPinchArea21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPinchArea21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(i), self._addressOf(e))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN15QQuickPinchArea10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPinchArea10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpincharea.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPinchArea::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickPinchArea14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPinchArea14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickPinchArea::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickPinchArea10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickPinchArea10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickPinchArea::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPinchArea::event(QEvent *a0)
    ritual = 'ritual_ZN15QQuickPinchArea5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickPinchArea5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTouchEvent)
  @overload(NoneType)
  def clearPinch(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::clearPinch(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#clearPinch

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::clearPinch(QTouchEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea10clearPinchEP11QTouchEvent',
        self._addressOf(event),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def cancelPinch(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::cancelPinch(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#cancelPinch

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchArea::cancelPinch(QTouchEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea11cancelPinchEP11QTouchEvent',
        self._addressOf(event),
    )

  @overload(QTouchEvent, bool)
  @overload(NoneType, bool)
  def updatePinch(
      self,
      event: Optional[QTouchEvent],
      filtering: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::updatePinch(QTouchEvent *event, bool
    filtering)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#updatePinch

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filtering : bool
      Passed on as it is.
    """
    #  void QQuickPinchArea::updatePinch(QTouchEvent *event, bool filtering)
    self.uglySide.call(
        'ritual_ZN15QQuickPinchArea11updatePinchEP11QTouchEventb',
        self._addressOf(event), filtering,
    )

  def updatePinchTarget(self) -> None:
    """
    Calls Qt's 'void QQuickPinchArea::updatePinchTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpincharea.html#updatePinchTarget
    """
    #  void QQuickPinchArea::updatePinchTarget()
    self.uglySide.call('ritual_ZN15QQuickPinchArea17updatePinchTargetEv')

  def d_func(self) -> Optional[QQuickPinchAreaPrivate]:
    """
    Calls Qt's 'QQuickPinchAreaPrivate *QQuickPinchArea::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpincharea.html#d_func

    Returns
    -------

    Optional[QQuickPinchAreaPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPinchAreaPrivate *QQuickPinchArea::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickPinchArea6d_funcEv')
    from . import QQuickPinchAreaPrivate
    return QQuickPinchAreaPrivate._cuteAt(address)
