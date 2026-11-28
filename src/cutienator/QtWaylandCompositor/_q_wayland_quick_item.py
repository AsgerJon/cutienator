"""
QWaylandQuickItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquickitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWaylandSurface
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject, QPoint, QPointF, QVariant
  from ..QtGui import QHoverEvent, QInputMethodEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QTouchEvent, QWheelEvent
  from . import QWaylandCompositor, QWaylandDrag, QWaylandOutput
  from . import QWaylandQuickItemPrivate, QWaylandSeat, QWaylandView
  from ..QtQuick import QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHoverEvent = WAIT['QHoverEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSGNode = WAIT['QSGNode']
  QTouchEvent = WAIT['QTouchEvent']
  QVariant = WAIT['QVariant']
  QWaylandDrag = WAIT['QWaylandDrag']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandQuickItem: a plain Python object standing in
  front of one C++ QWaylandQuickItem.

  What exists
  -----------

  Every function of Qt's QWaylandQuickItem that has a ritual and that Python
  can call so far, 79 names in all: 'metaObject', 'tr', 'd_func',
  'compositor', 'view', 'surface', 'setSurface', 'origin',
  'isTextureProvider', 'textureProvider', 'isPaintEnabled',
  'touchEventsEnabled', 'setTouchEventsEnabled', 'inputEventsEnabled',
  'setInputEventsEnabled', 'focusOnClick', 'setFocusOnClick',
  'inputRegionContains', 'mapToSurface', 'mapFromSurface',
  'inputMethodQuery', 'subsurfaceHandler', 'setSubsurfaceHandler', 'output',
  'setOutput', 'isBufferLocked', 'setBufferLocked',
  'allowDiscardFrontBuffer', 'setAllowDiscardFrontBuffer', 'setPrimary',
  'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'wheelEvent',
  'keyPressEvent', 'keyReleaseEvent', 'touchEvent', 'touchUngrabEvent',
  'inputMethodEvent', 'surfaceChangedEvent', 'takeFocus', 'setPaintEnabled',
  'raise_', 'lower', 'sendMouseMoveEvent', 'surfaceMappedChanged',
  'handleSurfaceChanged', 'handleBufferLockedChanged', 'parentChanged',
  'updateSize', 'updateBuffer', 'updateWindow', 'updateOutput', 'beforeSync',
  'handleSubsurfaceAdded', 'handleSubsurfacePosition', 'handlePlaceAbove',
  'handlePlaceBelow', 'handleDragStarted', 'updateInputMethod',
  'updateFocus', 'surfaceChanged', 'compositorChanged',
  'paintEnabledChanged', 'touchEventsEnabledChanged', 'originChanged',
  'surfaceDestroyed', 'inputEventsEnabledChanged', 'focusOnClickChanged',
  'mouseMove', 'mouseRelease', 'subsurfaceHandlerChanged', 'outputChanged',
  'bufferLockedChanged', 'allowDiscardFrontBufferChanged', 'updatePaintNode'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandQuickItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandQuickItemPrivate *QWaylandQuickItem::d_func() const':
    takes in Python what 'QWaylandQuickItemPrivate
    *QWaylandQuickItem::d_func()' takes.
  - Qt's 'QWaylandQuickItem::~QWaylandQuickItem()': the destructor: Python
    never removes a C++ QWaylandQuickItem.
  - Qt's 'QWaylandQuickItem::QWaylandQuickItem(QWaylandQuickItemPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 88 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickItem is created at the first use, not by
    'QWaylandQuickItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickItem.
  - Qt tells when it has removed the C++ QWaylandQuickItem. Every call on the
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
    Calls Qt's 'QString QWaylandQuickItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#tr

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
    #  QString QWaylandQuickItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QWaylandQuickItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickItem'

  #  A C++ QWaylandQuickItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickItem'

  #  The functions Qt calls itself that QWaylandQuickItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'surfaceChangedEvent': (
          ('_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylandSurfaceS'
           '1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSurface'),
               ('address', 'address', 'QtWaylandCompositor:QWaylandSurface'),
           )),
      ),
      'takeFocus': (
          ('_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSeat'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandQuickItem::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandQuickItem::compositor() const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem10compositorEv',
    )
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def view(self) -> Optional[QWaylandView]:
    """
    Calls Qt's 'QWaylandView *QWaylandQuickItem::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#view

    Returns
    -------

    Optional[QWaylandView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandView *QWaylandQuickItem::view() const
    address = self.uglySide.call('ritual_ZNK17QWaylandQuickItem4viewEv')
    from . import QWaylandView
    return QWaylandView._cuteAt(address)

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandQuickItem::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandQuickItem::surface() const
    address = self.uglySide.call('ritual_ZNK17QWaylandQuickItem7surfaceEv')
    return QWaylandSurface._cuteAt(address)

  def origin(self) -> QWaylandSurface.Origin:
    """
    Calls Qt's 'QWaylandSurface::Origin QWaylandQuickItem::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#origin

    Returns
    -------

    QWaylandSurface.Origin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWaylandSurface.Origin(number)' gives.
    """
    #  QWaylandSurface::Origin QWaylandQuickItem::origin() const
    return QWaylandSurface.Origin(self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem6originEv',
    ))

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#isTextureProvider
    """
    #  bool QWaylandQuickItem::isTextureProvider() const
    ritual = 'ritual_ZNK17QWaylandQuickItem17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QWaylandQuickItem17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QWaylandQuickItem::textureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QWaylandQuickItem::textureProvider() const
    ritual = 'ritual_ZNK17QWaylandQuickItem15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QWaylandQuickItem15textureProviderEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def isPaintEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::isPaintEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#isPaintEnabled
    """
    #  bool QWaylandQuickItem::isPaintEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem14isPaintEnabledEv',
    )

  def touchEventsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::touchEventsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#touchEventsEnabled
    """
    #  bool QWaylandQuickItem::touchEventsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem18touchEventsEnabledEv',
    )

  def inputEventsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::inputEventsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputEventsEnabled
    """
    #  bool QWaylandQuickItem::inputEventsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem18inputEventsEnabledEv',
    )

  def focusOnClick(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::focusOnClick() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#focusOnClick
    """
    #  bool QWaylandQuickItem::focusOnClick() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem12focusOnClickEv',
    )

  @overload(QPointF)
  def inputRegionContains(self, localPosition: QPointF) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::inputRegionContains(const QPointF
    &localPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputRegionContains

    Parameters
    ----------

    localPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QWaylandQuickItem::inputRegionContains(const QPointF
    #      &localPosition) const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem19inputRegionContainsERK7QPointF',
        self._valueOf(localPosition, 'QPointF'),
    )

  @overload(QPointF)
  def mapToSurface(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWaylandQuickItem::mapToSurface(const QPointF &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mapToSurface

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWaylandQuickItem::mapToSurface(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem12mapToSurfaceERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def mapFromSurface(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWaylandQuickItem::mapFromSurface(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mapFromSurface

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWaylandQuickItem::mapFromSurface(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem14mapFromSurfaceERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    ritual = (
        'ritual_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputM'
          'ethodQueryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery query, QVariant
    argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery
    #      query, QVariant argument) const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def subsurfaceHandler(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWaylandQuickItem::subsurfaceHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#subsurfaceHandler

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWaylandQuickItem::subsurfaceHandler() const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem17subsurfaceHandlerEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def output(self) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandQuickItem::output() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#output

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandQuickItem::output() const
    address = self.uglySide.call('ritual_ZNK17QWaylandQuickItem6outputEv')
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def isBufferLocked(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::isBufferLocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#isBufferLocked
    """
    #  bool QWaylandQuickItem::isBufferLocked() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem14isBufferLockedEv',
    )

  def allowDiscardFrontBuffer(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItem::allowDiscardFrontBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#allowDiscardFrontBuffer
    """
    #  bool QWaylandQuickItem::allowDiscardFrontBuffer() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandQuickItem23allowDiscardFrontBufferEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandSurface)
  @overload(NoneType)
  def setSurface(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setSurface(QWaylandSurface
    *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#setSurface

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::setSurface(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem10setSurfaceEP15QWaylandSurface',
        self._addressOf(surface),
    )

  @overload(bool)
  def setTouchEventsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setTouchEventsEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setTouchEventsEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setTouchEventsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem21setTouchEventsEnabledEb', enabled,
    )

  @overload(bool)
  def setInputEventsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setInputEventsEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setInputEventsEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setInputEventsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem21setInputEventsEnabledEb', enabled,
    )

  @overload(bool)
  def setFocusOnClick(self, focus: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setFocusOnClick(bool focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setFocusOnClick

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setFocusOnClick(bool focus)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem15setFocusOnClickEb', focus,
    )

  @overload(QObject)
  @overload(NoneType)
  def setSubsurfaceHandler(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setSubsurfaceHandler(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setSubsurfaceHandler

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::setSubsurfaceHandler(QObject *a0)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem20setSubsurfaceHandlerEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setOutput(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setOutput(QWaylandOutput *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#setOutput

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::setOutput(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem9setOutputEP14QWaylandOutput',
        self._addressOf(output),
    )

  @overload(bool)
  def setBufferLocked(self, locked: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setBufferLocked(bool locked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setBufferLocked

    Parameters
    ----------

    locked : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setBufferLocked(bool locked)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem15setBufferLockedEb', locked,
    )

  @overload(bool)
  def setAllowDiscardFrontBuffer(self, discard: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setAllowDiscardFrontBuffer(bool
    discard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setAllowDiscardFrontBuffer

    Parameters
    ----------

    discard : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setAllowDiscardFrontBuffer(bool discard)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem26setAllowDiscardFrontBufferEb',
        discard,
    )

  def setPrimary(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setPrimary()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#setPrimary
    """
    #  void QWaylandQuickItem::setPrimary()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem10setPrimaryEv')

  @overload(bool)
  def setPaintEnabled(self, paintEnabled: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::setPaintEnabled(bool paintEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#setPaintEnabled

    Parameters
    ----------

    paintEnabled : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::setPaintEnabled(bool paintEnabled)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem15setPaintEnabledEb', paintEnabled,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickItem::QWaylandQuickItem(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#QWaylandQuickItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandQuickItem::QWaylandQuickItem(QQuickItem *parent)
    self._noteCreation(QWaylandQuickItem, lambda: Rituals.call(
        'ritual_ZN17QWaylandQuickItemC1EP10QQuickItem',
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

  def d_func(self) -> Optional[QWaylandQuickItemPrivate]:
    """
    Calls Qt's 'QWaylandQuickItemPrivate *QWaylandQuickItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#d_func

    Returns
    -------

    Optional[QWaylandQuickItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickItemPrivate *QWaylandQuickItem::d_func()
    address = self.uglySide.call('ritual_ZN17QWaylandQuickItem6d_funcEv')
    from . import QWaylandQuickItemPrivate
    return QWaylandQuickItemPrivate._cuteAt(address)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem17mouseReleaseEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QWaylandQuickItem10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QWaylandQuickItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN17QWaylandQuickItem10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QWaylandQuickItem10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::touchUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#touchUngrabEvent
    """
    #  void QWaylandQuickItem::touchUngrabEvent()
    ritual = 'ritual_ZN17QWaylandQuickItem16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QWaylandQuickItem16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::inputMethodEvent(QInputMethodEvent *event)
    ritual = (
        'ritual_ZN17QWaylandQuickItem16inputMethodEventEP17QInputMethodEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem16inputMethodEventEP17QInputMeth'
          'odEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWaylandSurface, QWaylandSurface)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QWaylandSurface)
  @overload(NoneType, NoneType)
  def surfaceChangedEvent(
      self,
      newSurface: Optional[QWaylandSurface],
      oldSurface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::surfaceChangedEvent(QWaylandSurface
    *newSurface, QWaylandSurface *oldSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#surfaceChangedEvent

    Parameters
    ----------

    newSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::surfaceChangedEvent(QWaylandSurface
    #      *newSurface, QWaylandSurface *oldSurface)
    ritual = (
        'ritual_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylandSurfa'
        'ceS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylan'
          'dSurfaceS1_')
    self.uglySide.call(
        ritual, self._addressOf(newSurface), self._addressOf(oldSurface),
    )

  @overload()
  @overload(QWaylandSeat)
  @overload(NoneType)
  def takeFocus(self, device: Optional[QWaylandSeat] = None) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::takeFocus(QWaylandSeat *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#takeFocus

    Parameters
    ----------

    device : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWaylandQuickItem::takeFocus(QWaylandSeat *device)
    ritual = 'ritual_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat'
    self.uglySide.call(ritual, self._addressOf(device))

  def raise_(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::raise()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#raise
    """
    #  void QWaylandQuickItem::raise()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem5raiseEv')

  def lower(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::lower()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#lower
    """
    #  void QWaylandQuickItem::lower()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem5lowerEv')

  @overload(QPointF)
  @overload(QPointF, QWaylandSeat)
  @overload(QPointF, NoneType)
  def sendMouseMoveEvent(
      self,
      position: QPointF,
      seat: Optional[QWaylandSeat] = None,
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::sendMouseMoveEvent(const QPointF
    &position, QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#sendMouseMoveEvent

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWaylandQuickItem::sendMouseMoveEvent(const QPointF &position,
    #      QWaylandSeat *seat)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem18sendMouseMoveEventERK7QPointFP12QWay'
        'landSeat',
        self._valueOf(position, 'QPointF'), self._addressOf(seat),
    )

  def surfaceMappedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::surfaceMappedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#surfaceMappedChanged
    """
    #  void QWaylandQuickItem::surfaceMappedChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem20surfaceMappedChangedEv',
    )

  def handleSurfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handleSurfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handleSurfaceChanged
    """
    #  void QWaylandQuickItem::handleSurfaceChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem20handleSurfaceChangedEv',
    )

  def handleBufferLockedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handleBufferLockedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handleBufferLockedChanged
    """
    #  void QWaylandQuickItem::handleBufferLockedChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem25handleBufferLockedChangedEv',
    )

  @overload(QWaylandSurface, QWaylandSurface)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QWaylandSurface)
  @overload(NoneType, NoneType)
  def parentChanged(
      self,
      newParent: Optional[QWaylandSurface],
      oldParent: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::parentChanged(QWaylandSurface
    *newParent, QWaylandSurface *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#parentChanged

    Parameters
    ----------

    newParent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::parentChanged(QWaylandSurface *newParent,
    #      QWaylandSurface *oldParent)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem13parentChangedEP15QWaylandSurfaceS1_',
        self._addressOf(newParent), self._addressOf(oldParent),
    )

  def updateSize(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::updateSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#updateSize
    """
    #  void QWaylandQuickItem::updateSize()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem10updateSizeEv')

  @overload(bool)
  def updateBuffer(self, hasBuffer: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::updateBuffer(bool hasBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#updateBuffer

    Parameters
    ----------

    hasBuffer : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItem::updateBuffer(bool hasBuffer)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem12updateBufferEb', hasBuffer,
    )

  def updateWindow(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::updateWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#updateWindow
    """
    #  void QWaylandQuickItem::updateWindow()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem12updateWindowEv')

  def updateOutput(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::updateOutput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#updateOutput
    """
    #  void QWaylandQuickItem::updateOutput()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem12updateOutputEv')

  def beforeSync(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::beforeSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#beforeSync
    """
    #  void QWaylandQuickItem::beforeSync()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem10beforeSyncEv')

  @overload(QWaylandSurface)
  @overload(NoneType)
  def handleSubsurfaceAdded(
      self,
      childSurface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handleSubsurfaceAdded(QWaylandSurface
    *childSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handleSubsurfaceAdded

    Parameters
    ----------

    childSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::handleSubsurfaceAdded(QWaylandSurface
    #      *childSurface)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem21handleSubsurfaceAddedEP15QWaylandSur'
        'face',
        self._addressOf(childSurface),
    )

  @overload(QPoint)
  def handleSubsurfacePosition(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handleSubsurfacePosition(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handleSubsurfacePosition

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandQuickItem::handleSubsurfacePosition(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem24handleSubsurfacePositionERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def handlePlaceAbove(
      self,
      referenceSurface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handlePlaceAbove(QWaylandSurface
    *referenceSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handlePlaceAbove

    Parameters
    ----------

    referenceSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::handlePlaceAbove(QWaylandSurface
    #      *referenceSurface)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem16handlePlaceAboveEP15QWaylandSurface',
        self._addressOf(referenceSurface),
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def handlePlaceBelow(
      self,
      referenceSurface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handlePlaceBelow(QWaylandSurface
    *referenceSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handlePlaceBelow

    Parameters
    ----------

    referenceSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::handlePlaceBelow(QWaylandSurface
    #      *referenceSurface)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem16handlePlaceBelowEP15QWaylandSurface',
        self._addressOf(referenceSurface),
    )

  @overload(QWaylandDrag)
  @overload(NoneType)
  def handleDragStarted(self, drag: Optional[QWaylandDrag]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::handleDragStarted(QWaylandDrag
    *drag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#handleDragStarted

    Parameters
    ----------

    drag : Optional[QWaylandDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItem::handleDragStarted(QWaylandDrag *drag)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem17handleDragStartedEP12QWaylandDrag',
        self._addressOf(drag),
    )

  @overload(Qt.InputMethodQueries)
  def updateInputMethod(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickItem::updateInputMethod(Qt::InputMethodQueries queries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#updateInputMethod

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QWaylandQuickItem::updateInputMethod(Qt::InputMethodQueries
    #      queries)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem17updateInputMethodE6QFlagsIN2Qt16Inpu'
        'tMethodQueryEE',
        queries.value,
    )

  def updateFocus(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::updateFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#updateFocus
    """
    #  void QWaylandQuickItem::updateFocus()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem11updateFocusEv')

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::surfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#surfaceChanged
    """
    #  void QWaylandQuickItem::surfaceChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem14surfaceChangedEv')

  def compositorChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::compositorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#compositorChanged
    """
    #  void QWaylandQuickItem::compositorChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem17compositorChangedEv')

  def paintEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::paintEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#paintEnabledChanged
    """
    #  void QWaylandQuickItem::paintEnabledChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem19paintEnabledChangedEv')

  def touchEventsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::touchEventsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#touchEventsEnabledChanged
    """
    #  void QWaylandQuickItem::touchEventsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem25touchEventsEnabledChangedEv',
    )

  def originChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::originChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#originChanged
    """
    #  void QWaylandQuickItem::originChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem13originChangedEv')

  def surfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::surfaceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#surfaceDestroyed
    """
    #  void QWaylandQuickItem::surfaceDestroyed()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem16surfaceDestroyedEv')

  def inputEventsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::inputEventsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#inputEventsEnabledChanged
    """
    #  void QWaylandQuickItem::inputEventsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem25inputEventsEnabledChangedEv',
    )

  def focusOnClickChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::focusOnClickChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#focusOnClickChanged
    """
    #  void QWaylandQuickItem::focusOnClickChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem19focusOnClickChangedEv')

  @overload(QPointF)
  def mouseMove(self, windowPosition: QPointF) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::mouseMove(const QPointF
    &windowPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitem.html#mouseMove

    Parameters
    ----------

    windowPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWaylandQuickItem::mouseMove(const QPointF &windowPosition)
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem9mouseMoveERK7QPointF',
        self._valueOf(windowPosition, 'QPointF'),
    )

  def mouseRelease(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::mouseRelease()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#mouseRelease
    """
    #  void QWaylandQuickItem::mouseRelease()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem12mouseReleaseEv')

  def subsurfaceHandlerChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::subsurfaceHandlerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#subsurfaceHandlerChanged
    """
    #  void QWaylandQuickItem::subsurfaceHandlerChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem24subsurfaceHandlerChangedEv',
    )

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::outputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#outputChanged
    """
    #  void QWaylandQuickItem::outputChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem13outputChangedEv')

  def bufferLockedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::bufferLockedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#bufferLockedChanged
    """
    #  void QWaylandQuickItem::bufferLockedChanged()
    self.uglySide.call('ritual_ZN17QWaylandQuickItem19bufferLockedChangedEv')

  def allowDiscardFrontBufferChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItem::allowDiscardFrontBufferChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html
    """
    #  void QWaylandQuickItem::allowDiscardFrontBufferChanged()
    self.uglySide.call(
        'ritual_ZN17QWaylandQuickItem30allowDiscardFrontBufferChangedEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QWaylandQuickItem::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitem.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QWaylandQuickItem::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN17QWaylandQuickItem15updatePaintNodeEP7QSGNodePN10QQuickI'
        'tem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QWaylandQuickItem15updatePaintNodeEP7QSGNodePN10Q'
          'QuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
