"""
QQuickOverlay binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickOverlay to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QMouseEvent, QTouchEvent, QWheelEvent
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickWindow
  from . import QQuickOverlayAttached, QQuickOverlayPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickOverlay(QQuickItem):
  """
  The cute side of Qt's QQuickOverlay: a plain Python object standing in
  front of one C++ QQuickOverlay.

  It is built on the cute 'QQuickItem', as Qt's QQuickOverlay is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickOverlay that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'modal', 'setModal',
  'modeless', 'setModeless', 'overlay', 'qmlAttachedProperties',
  'modalChanged', 'modelessChanged', 'pressed', 'released', 'itemChange',
  'geometryChange', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'touchEvent', 'wheelEvent', 'dragEnterEvent', 'dragMoveEvent',
  'dragLeaveEvent', 'dropEvent', 'handleWheelAndDnDEvents',
  'childMouseEventFilter', 'eventFilter', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickOverlay::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickOverlay::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickOverlay::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'void QQuickOverlay::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickOverlay::~QQuickOverlay()': the destructor: Python never
    removes a C++ QQuickOverlay.
  - Qt's 'const QQuickOverlayPrivate *QQuickOverlay::d_func() const': takes
    in Python what 'QQuickOverlayPrivate *QQuickOverlay::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickOverlay is created at the first use, not by
    'QQuickOverlay(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickOverlay.
  - Qt tells when it has removed the C++ QQuickOverlay. Every call on the
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
    Calls Qt's 'QString QQuickOverlay::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#tr

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
    #  QString QQuickOverlay::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickOverlay2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuickWindow)
  @overload(NoneType)
  @overload(QQuickWindow, QQuickItem)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def overlay(
      window: Optional[QQuickWindow],
      parent: Optional[QQuickItem] = None,
  ) -> Optional[QQuickOverlay]:
    """
    Calls Qt's 'QQuickOverlay *QQuickOverlay::overlay(QQuickWindow *window,
    QQuickItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#overlay

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQuickOverlay]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlay *QQuickOverlay::overlay(QQuickWindow *window, QQuickItem
    #      *parent)
    address = Rituals.call(
        'ritual_ZN13QQuickOverlay7overlayEP12QQuickWindowP10QQuickItem',
        CuteMixin._addressOf(window), CuteMixin._addressOf(parent),
    )
    return QQuickOverlay._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickOverlayAttached]:
    """
    Calls Qt's 'QQuickOverlayAttached
    *QQuickOverlay::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlay.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickOverlayAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlayAttached *QQuickOverlay::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN13QQuickOverlay21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickOverlayAttached
    return QQuickOverlayAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickOverlay'

  #  A C++ QQuickOverlay Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickOverlay'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickOverlay::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickOverlay::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickOverlay10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def modal(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickOverlay::modal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#modal

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickOverlay::modal() const
    address = self.uglySide.call('ritual_ZNK13QQuickOverlay5modalEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def modeless(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickOverlay::modeless() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#modeless

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickOverlay::modeless() const
    address = self.uglySide.call('ritual_ZNK13QQuickOverlay8modelessEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setModal(self, modal: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::setModal(QQmlComponent *modal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#setModal

    Parameters
    ----------

    modal : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::setModal(QQmlComponent *modal)
    self.uglySide.call(
        'ritual_ZN13QQuickOverlay8setModalEP13QQmlComponent',
        self._addressOf(modal),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setModeless(self, modeless: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::setModeless(QQmlComponent *modeless)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#setModeless

    Parameters
    ----------

    modeless : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::setModeless(QQmlComponent *modeless)
    self.uglySide.call(
        'ritual_ZN13QQuickOverlay11setModelessEP13QQmlComponent',
        self._addressOf(modeless),
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
    Notes what was given, for Qt's 'QQuickOverlay::QQuickOverlay(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#QQuickOverlay

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickOverlay::QQuickOverlay(QQuickItem *parent)
    self._noteCreation(QQuickOverlay, lambda: Rituals.call(
        'ritual_ZN13QQuickOverlayC1EP10QQuickItem', self._addressOf(parent),
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

  def modalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickOverlay::modalChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#modalChanged
    """
    #  void QQuickOverlay::modalChanged()
    self.uglySide.call('ritual_ZN13QQuickOverlay12modalChangedEv')

  def modelessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickOverlay::modelessChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#modelessChanged
    """
    #  void QQuickOverlay::modelessChanged()
    self.uglySide.call('ritual_ZN13QQuickOverlay15modelessChangedEv')

  def pressed(self) -> None:
    """
    Calls Qt's 'void QQuickOverlay::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#pressed
    """
    #  void QQuickOverlay::pressed()
    self.uglySide.call('ritual_ZN13QQuickOverlay7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QQuickOverlay::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#released
    """
    #  void QQuickOverlay::released()
    self.uglySide.call('ritual_ZN13QQuickOverlay8releasedEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickOverlay::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickOverlay::itemChange(ItemChange change, const ItemChangeData
    #      &data)
    ritual = (
        'ritual_ZN13QQuickOverlay10itemChangeEN10QQuickItem10ItemChangeERKN'
        'S0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay10itemChangeEN10QQuickItem10ItemChan'
          'geERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickOverlay::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickOverlay::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN13QQuickOverlay14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlay.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def handleWheelAndDnDEvents(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QQuickOverlay::handleWheelAndDnDEvents(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlay.html#handleWheelAndDnDEvents

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlay::handleWheelAndDnDEvents(QEvent *event)
    self.uglySide.call(
        'ritual_ZN13QQuickOverlay23handleWheelAndDnDEventsEP6QEvent',
        self._addressOf(event),
    )

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlay::childMouseEventFilter(QQuickItem *item,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlay.html#childMouseEventFilter

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickOverlay::childMouseEventFilter(QQuickItem *item, QEvent
    #      *event)
    ritual = (
        'ritual_ZN13QQuickOverlay21childMouseEventFilterEP10QQuickItemP6QEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickOverlay21childMouseEventFilterEP10QQuickIte'
          'mP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickOverlay::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickOverlay::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN13QQuickOverlay11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickOverlay11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  def d_func(self) -> Optional[QQuickOverlayPrivate]:
    """
    Calls Qt's 'QQuickOverlayPrivate *QQuickOverlay::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlay.html#d_func

    Returns
    -------

    Optional[QQuickOverlayPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlayPrivate *QQuickOverlay::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickOverlay6d_funcEv')
    from . import QQuickOverlayPrivate
    return QQuickOverlayPrivate._cuteAt(address)
