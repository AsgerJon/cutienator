"""
QGraphicsProxyWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsproxywidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGraphicsItem, QGraphicsWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QSizeF, QVariant
  from ..QtGui import QFocusEvent, QHideEvent, QInputMethodEvent, QKeyEvent
  from ..QtGui import QPainter, QShowEvent
  from . import QGraphicsSceneContextMenuEvent, QGraphicsSceneDragDropEvent
  from . import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from . import QGraphicsSceneResizeEvent, QGraphicsSceneWheelEvent
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QGraphicsSceneContextMenuEvent = WAIT['QGraphicsSceneContextMenuEvent']
  QGraphicsSceneDragDropEvent = WAIT['QGraphicsSceneDragDropEvent']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QGraphicsSceneResizeEvent = WAIT['QGraphicsSceneResizeEvent']
  QGraphicsSceneWheelEvent = WAIT['QGraphicsSceneWheelEvent']
  QHideEvent = WAIT['QHideEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QShowEvent = WAIT['QShowEvent']
  QSizeF = WAIT['QSizeF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsProxyWidget(QGraphicsWidget):
  """
  The cute side of Qt's QGraphicsProxyWidget: a plain Python object standing
  in front of one C++ QGraphicsProxyWidget.

  It is built on the cute 'QGraphicsWidget', as Qt's QGraphicsProxyWidget is
  built on Qt's QGraphicsWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsProxyWidget that has a ritual and that
  Python can call so far, 38 names in all: 'metaObject', 'tr', 'setWidget',
  'widget', 'subWidgetRect', 'setGeometry', 'paint', 'type',
  'createProxyForChildWidget', 'itemChange', 'event', 'eventFilter',
  'showEvent', 'hideEvent', 'contextMenuEvent', 'dragEnterEvent',
  'dragLeaveEvent', 'dragMoveEvent', 'dropEvent', 'hoverEnterEvent',
  'hoverLeaveEvent', 'hoverMoveEvent', 'grabMouseEvent', 'ungrabMouseEvent',
  'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent',
  'focusInEvent', 'focusOutEvent', 'focusNextPrevChild', 'inputMethodQuery',
  'inputMethodEvent', 'sizeHint', 'resizeEvent'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsProxyWidget::~QGraphicsProxyWidget()': the destructor:
    Python never removes a C++ QGraphicsProxyWidget.

  What has no ritual
  ------------------

  9 of the 49 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QGraphicsProxyWidget is created at the first use, not by
    'QGraphicsProxyWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsProxyWidget.
  - Qt tells when it has removed the C++ QGraphicsProxyWidget. Every call on
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
    Calls Qt's 'QString QGraphicsProxyWidget::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#tr

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
    #  QString QGraphicsProxyWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QGraphicsProxyWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsProxyWidget'

  #  A C++ QGraphicsProxyWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsProxyWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsProxyWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsProxyWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsProxyWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QGraphicsProxyWidget::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QGraphicsProxyWidget::widget() const
    address = self.uglySide.call('ritual_ZNK20QGraphicsProxyWidget6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def subWidgetRect(self, widget: Optional[QWidget]) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsProxyWidget::subWidgetRect(const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#subWidgetRect

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsProxyWidget::subWidgetRect(const QWidget *widget)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsProxyWidget13subWidgetRectEPK7QWidget',
        self._addressOf(widget),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsProxyWidget::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#type
    """
    #  int QGraphicsProxyWidget::type() const
    ritual = 'ritual_ZNK20QGraphicsProxyWidget4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGraphicsProxyWidget4typeEv'
    return self.uglySide.call(ritual)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery query)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    address = self.uglySide.call(
        'ritual_own_ZNK20QGraphicsProxyWidget16inputMethodQueryEN2Qt16Input'
        'MethodQueryE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    address = self.uglySide.call(
        'ritual_own_ZNK20QGraphicsProxyWidget8sizeHintEN2Qt8SizeHintERK6QSi'
        'zeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::setWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN20QGraphicsProxyWidget9setWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

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
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsProxyWidget::QGraphicsProxyWidget(QGraphicsItem *parent,
    Qt::WindowFlags wFlags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#QGraphicsProxyWidget

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QGraphicsProxyWidget::QGraphicsProxyWidget(QGraphicsItem *parent,
    #      Qt::WindowFlags wFlags)
    self._noteCreation(QGraphicsProxyWidget, lambda: Rituals.call(
        'ritual_ZN20QGraphicsProxyWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10Wi'
        'ndowTypeEE',
        self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
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
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#paint

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
      object.
    """
    #  void QGraphicsProxyWidget::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOp'
          'tionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def createProxyForChildWidget(
      self,
      child: Optional[QWidget],
  ) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget
    *QGraphicsProxyWidget::createProxyForChildWidget(QWidget *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html

    Parameters
    ----------

    child : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget
    #      *QGraphicsProxyWidget::createProxyForChildWidget(QWidget *child)
    address = self.uglySide.call(
        'ritual_ZN20QGraphicsProxyWidget25createProxyForChildWidgetEP7QWidg'
        'et',
        self._addressOf(child),
    )
    return QGraphicsProxyWidget._cuteAt(address)

  @overload(QGraphicsItem.GraphicsItemChange, QVariant)
  def itemChange(
      self,
      change: QGraphicsItem.GraphicsItemChange,
      value: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsProxyWidget::itemChange(GraphicsItemChange
    change, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#itemChange

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
    #  QVariant QGraphicsProxyWidget::itemChange(GraphicsItemChange change,
    #      const QVariant &value)
    address = self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget10itemChangeEN13QGraphicsItem18'
        'GraphicsItemChangeERK8QVariant',
        change.value, self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsProxyWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsproxywidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsProxyWidget::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget5eventEP6QEvent',
        self._addressOf(event),
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
    Calls Qt's 'bool QGraphicsProxyWidget::eventFilter(QObject *object,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsProxyWidget::eventFilter(QObject *object, QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget11eventFilterEP7QObjectP6QEvent',
        self._addressOf(object), self._addressOf(event),
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::showEvent(QShowEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::showEvent(QShowEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget9showEventEP10QShowEvent',
        self._addressOf(event),
    )

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::hideEvent(QHideEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::hideEvent(QHideEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget9hideEventEP10QHideEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(
      self,
      event: Optional[QGraphicsSceneContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::contextMenuEvent(QGraphicsSceneContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::contextMenuEvent(
    #      QGraphicsSceneContextMenuEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget16contextMenuEventEP30QGraphics'
        'SceneContextMenuEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragEnterEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget14dragEnterEventEP27QGraphicsSc'
        'eneDragDropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragLeaveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget14dragLeaveEventEP27QGraphicsSc'
        'eneDragDropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragMoveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget13dragMoveEventEP27QGraphicsSce'
        'neDragDropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#dropEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget9dropEventEP27QGraphicsSceneDra'
        'gDropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget15hoverEnterEventEP24QGraphicsS'
        'ceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget15hoverLeaveEventEP24QGraphicsS'
        'ceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget14hoverMoveEventEP24QGraphicsSc'
        'eneHoverEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def grabMouseEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#grabMouseEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget14grabMouseEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def ungrabMouseEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#ungrabMouseEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget16ungrabMouseEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget14mouseMoveEventEP24QGraphicsSc'
        'eneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget15mousePressEventEP24QGraphicsS'
        'ceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget17mouseReleaseEventEP24QGraphic'
        'sSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::mouseDoubleClickEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget21mouseDoubleClickEventEP24QGra'
        'phicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QGraphicsSceneWheelEvent]) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#wheelEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget10wheelEventEP24QGraphicsSceneW'
        'heelEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget13keyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget15keyReleaseEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::focusOutEvent(QFocusEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::focusOutEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget13focusOutEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QGraphicsProxyWidget::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QGraphicsProxyWidget::focusNextPrevChild(bool next)
    return self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget18focusNextPrevChildEb', next,
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget16inputMethodEventEP17QInputMet'
        'hodEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QGraphicsSceneResizeEvent]) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent
    #      *event)
    self.uglySide.call(
        'ritual_own_ZN20QGraphicsProxyWidget11resizeEventEP25QGraphicsScene'
        'ResizeEvent',
        self._addressOf(event),
    )
