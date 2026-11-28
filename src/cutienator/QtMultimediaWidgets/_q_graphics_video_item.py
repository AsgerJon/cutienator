"""
QGraphicsVideoItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaWidgets/qgraphicsvideoitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsItem, QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF, QTimerEvent
  from ..QtCore import QVariant
  from ..QtGui import QPainter
  from ..QtMultimedia import QVideoSink
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsVideoItem(QGraphicsObject):
  """
  The cute side of Qt's QGraphicsVideoItem: a plain Python object standing in
  front of one C++ QGraphicsVideoItem.

  It is built on the cute 'QGraphicsObject', as Qt's QGraphicsVideoItem is
  built on Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsVideoItem that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'videoSink',
  'aspectRatioMode', 'setAspectRatioMode', 'offset', 'setOffset', 'size',
  'setSize', 'nativeSize', 'boundingRect', 'paint', 'type',
  'nativeSizeChanged', 'timerEvent', 'itemChange'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsVideoItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGraphicsVideoItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsVideoItem::~QGraphicsVideoItem()': the destructor: Python
    never removes a C++ QGraphicsVideoItem.
  - Qt's 'QGraphicsVideoItemPrivate *QGraphicsVideoItem::d_func()': gives
    'QGraphicsVideoItemPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsVideoItemPrivate *QGraphicsVideoItem::d_func()
    const': gives 'QGraphicsVideoItemPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGraphicsVideoItem is created at the first use, not by
    'QGraphicsVideoItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsVideoItem.
  - Qt tells when it has removed the C++ QGraphicsVideoItem. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGraphicsVideoItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#tr

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
    #  QString QGraphicsVideoItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QGraphicsVideoItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsVideoItem'

  #  A C++ QGraphicsVideoItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsVideoItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsVideoItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsVideoItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QGraphicsVideoItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QGraphicsVideoItem::videoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QGraphicsVideoItem::videoSink() const
    address = self.uglySide.call(
        'ritual_ZNK18QGraphicsVideoItem9videoSinkEv',
    )
    from ..QtMultimedia import QVideoSink
    return QVideoSink._cuteAt(address)

  def aspectRatioMode(self) -> Qt.AspectRatioMode:
    """
    Calls Qt's 'Qt::AspectRatioMode QGraphicsVideoItem::aspectRatioMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsvideoitem.html#aspectRatioMode

    Returns
    -------

    Qt.AspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.AspectRatioMode(number)' gives.
    """
    #  Qt::AspectRatioMode QGraphicsVideoItem::aspectRatioMode() const
    return Qt.AspectRatioMode(self.uglySide.call(
        'ritual_ZNK18QGraphicsVideoItem15aspectRatioModeEv',
    ))

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsVideoItem::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsVideoItem::offset() const
    address = self.uglySide.call('ritual_ZNK18QGraphicsVideoItem6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsVideoItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsVideoItem::size() const
    address = self.uglySide.call('ritual_ZNK18QGraphicsVideoItem4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def nativeSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsVideoItem::nativeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#nativeSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsVideoItem::nativeSize() const
    address = self.uglySide.call(
        'ritual_ZNK18QGraphicsVideoItem10nativeSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsVideoItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsvideoitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsVideoItem::boundingRect() const
    ritual = 'ritual_ZNK18QGraphicsVideoItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGraphicsVideoItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsVideoItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#type
    """
    #  int QGraphicsVideoItem::type() const
    ritual = 'ritual_ZNK18QGraphicsVideoItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGraphicsVideoItem4typeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.AspectRatioMode)
  def setAspectRatioMode(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void
    QGraphicsVideoItem::setAspectRatioMode(Qt::AspectRatioMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsvideoitem.html#setAspectRatioMode

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QGraphicsVideoItem::setAspectRatioMode(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN18QGraphicsVideoItem18setAspectRatioModeEN2Qt15AspectRati'
        'oModeE',
        mode.value,
    )

  @overload(QPointF)
  def setOffset(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsVideoItem::setOffset(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#setOffset

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsVideoItem::setOffset(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN18QGraphicsVideoItem9setOffsetERK7QPointF',
        self._valueOf(offset, 'QPointF'),
    )

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsVideoItem::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsVideoItem::setSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN18QGraphicsVideoItem7setSizeERK6QSizeF',
        self._valueOf(size),
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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsVideoItem::QGraphicsVideoItem(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsvideoitem.html#QGraphicsVideoItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsVideoItem::QGraphicsVideoItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsVideoItem, lambda: Rituals.call(
        'ritual_ZN18QGraphicsVideoItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsVideoItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsVideoItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN18QGraphicsVideoItem5paintEP8QPainterPK24QStyleOptionGrap'
        'hicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QGraphicsVideoItem5paintEP8QPainterPK24QStyleOpti'
          'onGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QSizeF)
  def nativeSizeChanged(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsVideoItem::nativeSizeChanged(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsvideoitem.html#nativeSizeChanged

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsVideoItem::nativeSizeChanged(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN18QGraphicsVideoItem17nativeSizeChangedERK6QSizeF',
        self._valueOf(size),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsVideoItem::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsVideoItem::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN18QGraphicsVideoItem10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QGraphicsVideoItem10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsItem.GraphicsItemChange, QVariant)
  def itemChange(
      self,
      change: QGraphicsItem.GraphicsItemChange,
      value: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsVideoItem::itemChange(GraphicsItemChange
    change, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsvideoitem.html#itemChange

    Parameters
    ----------

    change : QGraphicsItem.GraphicsItemChange
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsVideoItem::itemChange(GraphicsItemChange change,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN18QGraphicsVideoItem10itemChangeEN13QGraphicsItem18Graphi'
        'csItemChangeERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QGraphicsVideoItem10itemChangeEN13QGraphicsItem18'
          'GraphicsItemChangeERK8QVariant')
    address = self.uglySide.call(ritual, change.value, self._valueOf(value))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
