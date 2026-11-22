"""
QGraphicsWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicswidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QGraphicsItem, QGraphicsLayoutItem, QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMarginsF, QMetaObject, QPointF, QRectF
  from ..QtCore import QSizeF, QVariant
  from ..QtGui import QAction, QCloseEvent, QFocusEvent, QFont, QHideEvent
  from ..QtGui import QKeySequence, QPainter, QPainterPath, QPalette
  from ..QtGui import QShowEvent
  from . import QGraphicsLayout, QGraphicsSceneHoverEvent
  from . import QGraphicsSceneMoveEvent, QGraphicsSceneResizeEvent, QStyle
  from . import QStyleOption, QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QCloseEvent = WAIT['QCloseEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QGraphicsLayout = WAIT['QGraphicsLayout']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMoveEvent = WAIT['QGraphicsSceneMoveEvent']
  QGraphicsSceneResizeEvent = WAIT['QGraphicsSceneResizeEvent']
  QHideEvent = WAIT['QHideEvent']
  QKeySequence = WAIT['QKeySequence']
  QMarginsF = WAIT['QMarginsF']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QShowEvent = WAIT['QShowEvent']
  QSizeF = WAIT['QSizeF']
  QStyle = WAIT['QStyle']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
  """
  The cute side of Qt's QGraphicsWidget: a plain Python object standing in
  front of one C++ QGraphicsWidget.

  It is built on the cute 'QGraphicsObject', as Qt's QGraphicsWidget is built
  on Qt's QGraphicsObject, and has everything that class has. It is built on
  the cute 'QGraphicsLayoutItem' as well, as Qt's QGraphicsWidget is built on
  Qt's QGraphicsLayoutItem too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsWidget that has a ritual and that Python
  can call so far, 78 names in all: 'metaObject', 'tr', 'layout',
  'setLayout', 'adjustSize', 'layoutDirection', 'setLayoutDirection',
  'unsetLayoutDirection', 'style', 'setStyle', 'font', 'setFont', 'palette',
  'setPalette', 'autoFillBackground', 'setAutoFillBackground', 'resize',
  'size', 'setGeometry', 'rect', 'setContentsMargins',
  'setWindowFrameMargins', 'unsetWindowFrameMargins', 'windowFrameGeometry',
  'windowFrameRect', 'windowFlags', 'windowType', 'setWindowFlags',
  'isActiveWindow', 'setWindowTitle', 'windowTitle', 'focusPolicy',
  'setFocusPolicy', 'setTabOrder', 'focusWidget', 'grabShortcut',
  'releaseShortcut', 'setShortcutEnabled', 'setShortcutAutoRepeat',
  'addAction', 'addActions', 'insertActions', 'insertAction', 'removeAction',
  'actions', 'setAttribute', 'testAttribute', 'type', 'paint',
  'paintWindowFrame', 'boundingRect', 'shape', 'close', 'initStyleOption',
  'sizeHint', 'updateGeometry', 'itemChange', 'propertyChange', 'sceneEvent',
  'windowFrameEvent', 'windowFrameSectionAt', 'event', 'changeEvent',
  'closeEvent', 'focusInEvent', 'focusNextPrevChild', 'focusOutEvent',
  'hideEvent', 'moveEvent', 'polishEvent', 'resizeEvent', 'showEvent',
  'hoverMoveEvent', 'hoverLeaveEvent', 'grabMouseEvent', 'ungrabMouseEvent',
  'grabKeyboardEvent', 'ungrabKeyboardEvent'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsWidget::~QGraphicsWidget()': the destructor: Python never
    removes a C++ QGraphicsWidget.
  - Qt's 'void QGraphicsWidget::getContentsMargins(qreal *left, qreal *top,
    qreal *right, qreal *bottom) const': takes a number to change where it
    is.
  - Qt's 'void QGraphicsWidget::getWindowFrameMargins(qreal *left, qreal
    *top, qreal *right, qreal *bottom) const': takes a number to change where
    it is.

  What has no ritual
  ------------------

  11 of the 97 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QGraphicsWidget is created at the first use, not by
    'QGraphicsWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsWidget.
  - Qt tells when it has removed the C++ QGraphicsWidget. Every call on the
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
    Calls Qt's 'QString QGraphicsWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#tr

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
    #  QString QGraphicsWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGraphicsWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def setTabOrder(
      first: Optional[QGraphicsWidget],
      second: Optional[QGraphicsWidget],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setTabOrder(QGraphicsWidget *first,
    QGraphicsWidget *second)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setTabOrder

    Parameters
    ----------

    first : Optional[QGraphicsWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    second : Optional[QGraphicsWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::setTabOrder(QGraphicsWidget *first,
    #      QGraphicsWidget *second)
    Rituals.call(
        'ritual_ZN15QGraphicsWidget11setTabOrderEPS_S0_',
        CuteMixin._addressOf(first), CuteMixin._addressOf(second),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsWidget'

  #  Qt's QGraphicsWidget is built on more than one class. The part of a C++
  #  QGraphicsWidget that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGraphicsLayoutItem':
          'ritual_cast_QGraphicsWidget_QGraphicsLayoutItem',
  }

  #  A C++ QGraphicsWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsWidget'

  #  The functions Qt calls itself that QGraphicsWidget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'paintWindowFrame': (
          ('_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOpti'
           'onGraphicsItemP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'address', 'QtWidgets:QStyleOptionGraphicsItem'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'initStyleOption': (
          ('_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOption'),
           )),
      ),
      'propertyChange': (
          ('_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'windowFrameEvent': (
          ('_ZN15QGraphicsWidget16windowFrameEventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'windowFrameSectionAt': (
          ('_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF',
           ('int', 'enum', 'QtCore:Qt.WindowFrameSection'),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'changeEvent': (
          ('_ZN15QGraphicsWidget11changeEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'closeEvent': (
          ('_ZN15QGraphicsWidget10closeEventEP11QCloseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QCloseEvent'),
           )),
      ),
      'focusNextPrevChild': (
          ('_ZN15QGraphicsWidget18focusNextPrevChildEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'hideEvent': (
          ('_ZN15QGraphicsWidget9hideEventEP10QHideEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHideEvent'),
           )),
      ),
      'moveEvent': (
          ('_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneMoveEvent'),
           )),
      ),
      'polishEvent': (
          ('_ZN15QGraphicsWidget11polishEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeEvent': (
          ('_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneResizeEvent'),
           )),
      ),
      'showEvent': (
          ('_ZN15QGraphicsWidget9showEventEP10QShowEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QShowEvent'),
           )),
      ),
      'grabMouseEvent': (
          ('_ZN15QGraphicsWidget14grabMouseEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'ungrabMouseEvent': (
          ('_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'grabKeyboardEvent': (
          ('_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'ungrabKeyboardEvent': (
          ('_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
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
    Calls Qt's 'const QMetaObject *QGraphicsWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def layout(self) -> Optional[QGraphicsLayout]:
    """
    Calls Qt's 'QGraphicsLayout *QGraphicsWidget::layout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#layout

    Returns
    -------

    Optional[QGraphicsLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayout *QGraphicsWidget::layout() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget6layoutEv')
    from . import QGraphicsLayout
    return QGraphicsLayout._cuteAt(address)

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QGraphicsWidget::layoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QGraphicsWidget::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget15layoutDirectionEv',
    ))

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QGraphicsWidget::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QGraphicsWidget::style() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget5styleEv')
    from . import QStyle
    return QStyle._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphicsWidget::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphicsWidget::font() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def palette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QGraphicsWidget::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QGraphicsWidget::palette() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget7paletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def autoFillBackground(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::autoFillBackground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#autoFillBackground
    """
    #  bool QGraphicsWidget::autoFillBackground() const
    return self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget18autoFillBackgroundEv',
    )

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsWidget::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsWidget::size() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsWidget::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsWidget::rect() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def windowFrameGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsWidget::windowFrameGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#windowFrameGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsWidget::windowFrameGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget19windowFrameGeometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def windowFrameRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsWidget::windowFrameRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#windowFrameRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsWidget::windowFrameRect() const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget15windowFrameRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def windowFlags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QGraphicsWidget::windowFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#windowFlags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QGraphicsWidget::windowFlags() const
    return Qt.WindowFlags(self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget11windowFlagsEv',
    ))

  def windowType(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QGraphicsWidget::windowType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#windowType

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QGraphicsWidget::windowType() const
    return Qt.WindowType(self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget10windowTypeEv',
    ))

  def isActiveWindow(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::isActiveWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#isActiveWindow
    """
    #  bool QGraphicsWidget::isActiveWindow() const
    return self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget14isActiveWindowEv',
    )

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QGraphicsWidget::windowTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsWidget::windowTitle() const
    return self.uglySide.call('ritual_ZNK15QGraphicsWidget11windowTitleEv')

  def focusPolicy(self) -> Qt.FocusPolicy:
    """
    Calls Qt's 'Qt::FocusPolicy QGraphicsWidget::focusPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#focusPolicy

    Returns
    -------

    Qt.FocusPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusPolicy(number)'
      gives.
    """
    #  Qt::FocusPolicy QGraphicsWidget::focusPolicy() const
    return Qt.FocusPolicy(self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget11focusPolicyEv',
    ))

  def focusWidget(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsWidget::focusWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#focusWidget

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsWidget::focusWidget() const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget11focusWidgetEv',
    )
    return QGraphicsWidget._cuteAt(address)

  def actions(self) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *> QGraphicsWidget::actions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#actions

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *> QGraphicsWidget::actions() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsWidget7actionsEv')
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  @overload(Qt.WidgetAttribute)
  def testAttribute(self, attribute: Qt.WidgetAttribute) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::testAttribute(Qt::WidgetAttribute
    attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#testAttribute

    Parameters
    ----------

    attribute : Qt.WidgetAttribute
      Passed on as its number.
    """
    #  bool QGraphicsWidget::testAttribute(Qt::WidgetAttribute attribute)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QGraphicsWidget13testAttributeEN2Qt15WidgetAttributeE',
        attribute.value,
    )

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsWidget::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#type
    """
    #  int QGraphicsWidget::type() const
    ritual = 'ritual_ZNK15QGraphicsWidget4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGraphicsWidget4typeEv'
    return self.uglySide.call(ritual)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsWidget::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsWidget::boundingRect() const
    ritual = 'ritual_ZNK15QGraphicsWidget12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGraphicsWidget12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsWidget::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsWidget::shape() const
    ritual = 'ritual_ZNK15QGraphicsWidget5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGraphicsWidget5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsWidget::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#sizeHint

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
    #  QSizeF QGraphicsWidget::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    address = self.uglySide.call(
        'ritual_own_ZNK15QGraphicsWidget8sizeHintEN2Qt8SizeHintERK6QSizeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(QPointF)
  def windowFrameSectionAt(self, pos: QPointF) -> Qt.WindowFrameSection:
    """
    Calls Qt's 'Qt::WindowFrameSection
    QGraphicsWidget::windowFrameSectionAt(const QPointF &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#windowFrameSectionAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    Qt.WindowFrameSection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowFrameSection(number)' gives.
    """
    #  Qt::WindowFrameSection QGraphicsWidget::windowFrameSectionAt(const
    #      QPointF &pos) const
    return Qt.WindowFrameSection(self.uglySide.call(
        'ritual_own_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF',
        self._valueOf(pos),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsLayout)
  @overload(NoneType)
  def setLayout(self, layout: Optional[QGraphicsLayout]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setLayout(QGraphicsLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setLayout

    Parameters
    ----------

    layout : Optional[QGraphicsLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::setLayout(QGraphicsLayout *layout)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget9setLayoutEP15QGraphicsLayout',
        self._addressOf(layout),
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QGraphicsWidget::setLayoutDirection(Qt::LayoutDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget18setLayoutDirectionEN2Qt15LayoutDirecti'
        'onE',
        direction.value,
    )

  @overload(QStyle)
  @overload(NoneType)
  def setStyle(self, style: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setStyle(QStyle *style)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setStyle

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::setStyle(QStyle *style)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget8setStyleEP6QStyle',
        self._addressOf(style),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsWidget::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QPalette)
  def setPalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setPalette(const QPalette &palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsWidget::setPalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget10setPaletteERK8QPalette',
        self._valueOf(palette),
    )

  @overload(bool)
  def setAutoFillBackground(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setAutoFillBackground(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setAutoFillBackground

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsWidget::setAutoFillBackground(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget21setAutoFillBackgroundEb', enabled,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsWidget::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN15QGraphicsWidget11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGraphicsWidget11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(float, float, float, float)
  def setGeometry(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setGeometry(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setGeometry

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsWidget::setGeometry(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget11setGeometryEdddd', x, y, w, h,
    )

  @overload(float, float, float, float)
  def setContentsMargins(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setContentsMargins(qreal left, qreal
    top, qreal right, qreal bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setContentsMargins

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  void QGraphicsWidget::setContentsMargins(qreal left, qreal top, qreal
    #      right, qreal bottom)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget18setContentsMarginsEdddd',
        left, top, right, bottom,
    )

  @overload(QMarginsF)
  def setContentsMargins(self, margins: QMarginsF) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setContentsMargins(QMarginsF margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setContentsMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QGraphicsWidget::setContentsMargins(QMarginsF margins)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget18setContentsMarginsE9QMarginsF',
        self._valueOf(margins),
    )

  @overload(float, float, float, float)
  def setWindowFrameMargins(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setWindowFrameMargins(qreal left, qreal
    top, qreal right, qreal bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setWindowFrameMargins

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  void QGraphicsWidget::setWindowFrameMargins(qreal left, qreal top,
    #      qreal right, qreal bottom)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget21setWindowFrameMarginsEdddd',
        left, top, right, bottom,
    )

  @overload(QMarginsF)
  def setWindowFrameMargins(self, margins: QMarginsF) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setWindowFrameMargins(QMarginsF
    margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setWindowFrameMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QGraphicsWidget::setWindowFrameMargins(QMarginsF margins)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget21setWindowFrameMarginsE9QMarginsF',
        self._valueOf(margins),
    )

  @overload(Qt.WindowFlags)
  def setWindowFlags(self, wFlags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setWindowFlags(Qt::WindowFlags
    wFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setWindowFlags

    Parameters
    ----------

    wFlags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QGraphicsWidget::setWindowFlags(Qt::WindowFlags wFlags)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget14setWindowFlagsE6QFlagsIN2Qt10WindowTyp'
        'eEE',
        wFlags.value,
    )

  @overload(str)
  def setWindowTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setWindowTitle(const QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setWindowTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsWidget::setWindowTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget14setWindowTitleERK7QString', title,
    )

  @overload(Qt.FocusPolicy)
  def setFocusPolicy(self, policy: Qt.FocusPolicy) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setFocusPolicy(Qt::FocusPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setFocusPolicy

    Parameters
    ----------

    policy : Qt.FocusPolicy
      Passed on as its number.
    """
    #  void QGraphicsWidget::setFocusPolicy(Qt::FocusPolicy policy)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget14setFocusPolicyEN2Qt11FocusPolicyE',
        policy.value,
    )

  @overload(int)
  @overload(int, bool)
  def setShortcutEnabled(self, id: int, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setShortcutEnabled(int id, bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setShortcutEnabled

    Parameters
    ----------

    id : int
      Passed on as it is.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsWidget::setShortcutEnabled(int id, bool enabled)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget18setShortcutEnabledEib', id, enabled,
    )

  @overload(int)
  @overload(int, bool)
  def setShortcutAutoRepeat(self, id: int, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setShortcutAutoRepeat(int id, bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#setShortcutAutoRepeat

    Parameters
    ----------

    id : int
      Passed on as it is.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsWidget::setShortcutAutoRepeat(int id, bool enabled)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget21setShortcutAutoRepeatEib', id, enabled,
    )

  @overload(Qt.WidgetAttribute)
  @overload(Qt.WidgetAttribute, bool)
  def setAttribute(
      self,
      attribute: Qt.WidgetAttribute,
      on: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::setAttribute(Qt::WidgetAttribute
    attribute, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#setAttribute

    Parameters
    ----------

    attribute : Qt.WidgetAttribute
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsWidget::setAttribute(Qt::WidgetAttribute attribute, bool
    #      on)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget12setAttributeEN2Qt15WidgetAttributeEb',
        attribute.value, on,
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
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsWidget::QGraphicsWidget(QGraphicsItem *parent, Qt::WindowFlags
    wFlags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#QGraphicsWidget

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QGraphicsWidget::QGraphicsWidget(QGraphicsItem *parent,
    #      Qt::WindowFlags wFlags)
    self._noteCreation(QGraphicsWidget, lambda: Rituals.call(
        'ritual_ZN15QGraphicsWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowT'
        'ypeEE',
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

  def adjustSize(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::adjustSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#adjustSize
    """
    #  void QGraphicsWidget::adjustSize()
    self.uglySide.call('ritual_ZN15QGraphicsWidget10adjustSizeEv')

  def unsetLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::unsetLayoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#unsetLayoutDirection
    """
    #  void QGraphicsWidget::unsetLayoutDirection()
    self.uglySide.call('ritual_ZN15QGraphicsWidget20unsetLayoutDirectionEv')

  @overload(QSizeF)
  def resize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::resize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#resize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsWidget::resize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget6resizeERK6QSizeF', self._valueOf(size),
    )

  @overload(float, float)
  def resize(self, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::resize(qreal w, qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#resize

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsWidget::resize(qreal w, qreal h)
    self.uglySide.call('ritual_ZN15QGraphicsWidget6resizeEdd', w, h)

  def unsetWindowFrameMargins(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::unsetWindowFrameMargins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#unsetWindowFrameMargins
    """
    #  void QGraphicsWidget::unsetWindowFrameMargins()
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget23unsetWindowFrameMarginsEv',
    )

  @overload(QKeySequence)
  @overload(QKeySequence, Qt.ShortcutContext)
  def grabShortcut(
      self,
      sequence: QKeySequence,
      context: Qt.ShortcutContext = Qt.ShortcutContext.WindowShortcut,
  ) -> int:
    """
    Calls Qt's 'int QGraphicsWidget::grabShortcut(const QKeySequence
    &sequence, Qt::ShortcutContext context)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#grabShortcut

    Parameters
    ----------

    sequence : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    context : Qt.ShortcutContext
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ShortcutContext.WindowShortcut.
    """
    #  int QGraphicsWidget::grabShortcut(const QKeySequence &sequence,
    #      Qt::ShortcutContext context)
    return self.uglySide.call(
        'ritual_ZN15QGraphicsWidget12grabShortcutERK12QKeySequenceN2Qt15Sho'
        'rtcutContextE',
        self._valueOf(sequence), context.value,
    )

  @overload(int)
  def releaseShortcut(self, id: int) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::releaseShortcut(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#releaseShortcut

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QGraphicsWidget::releaseShortcut(int id)
    self.uglySide.call('ritual_ZN15QGraphicsWidget15releaseShortcutEi', id)

  @overload(QAction)
  @overload(NoneType)
  def addAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::addAction(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#addAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::addAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget9addActionEP7QAction',
        self._addressOf(action),
    )

  @overload(QList[QAction])
  def addActions(self, actions: QList[QAction]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::addActions(const QList<QAction *>
    &actions)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#addActions

    Parameters
    ----------

    actions : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphicsWidget::addActions(const QList<QAction *> &actions)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget10addActionsERK5QListIP7QActionE',
        self._valueOf(actions),
    )

  @overload(QAction, QList[QAction])
  @overload(NoneType, QList[QAction])
  def insertActions(
      self,
      before: Optional[QAction],
      actions: QList[QAction],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::insertActions(QAction *before, const
    QList<QAction *> &actions)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#insertActions

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    actions : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphicsWidget::insertActions(QAction *before, const
    #      QList<QAction *> &actions)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget13insertActionsEP7QActionRK5QListIS1_E',
        self._addressOf(before), self._valueOf(actions),
    )

  @overload(QAction, QAction)
  @overload(QAction, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def insertAction(
      self,
      before: Optional[QAction],
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::insertAction(QAction *before, QAction
    *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#insertAction

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::insertAction(QAction *before, QAction *action)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget12insertActionEP7QActionS1_',
        self._addressOf(before), self._addressOf(action),
    )

  @overload(QAction)
  @overload(NoneType)
  def removeAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::removeAction(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#removeAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::removeAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN15QGraphicsWidget12removeActionEP7QAction',
        self._addressOf(action),
    )

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
    Calls Qt's 'void QGraphicsWidget::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#paint

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
    #  void QGraphicsWidget::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN15QGraphicsWidget5paintEP8QPainterPK24QStyleOptionGraphic'
        'sItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGraphicsWidget5paintEP8QPainterPK24QStyleOptionG'
          'raphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

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
  def paintWindowFrame(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::paintWindowFrame(QPainter *painter,
    const QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#paintWindowFrame

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
    #  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleO'
        'ptionGraphicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24Q'
          'StyleOptionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def close(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#close
    """
    #  bool QGraphicsWidget::close()
    return self.uglySide.call('ritual_ZN15QGraphicsWidget5closeEv')

  @overload(QStyleOption)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOption]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::initStyleOption(QStyleOption *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
    self.uglySide.call(
        'ritual_own_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption',
        self._addressOf(option),
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#updateGeometry
    """
    #  void QGraphicsWidget::updateGeometry()
    self.uglySide.call('ritual_own_ZN15QGraphicsWidget14updateGeometryEv')

  @overload(QGraphicsItem.GraphicsItemChange, QVariant)
  def itemChange(
      self,
      change: QGraphicsItem.GraphicsItemChange,
      value: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsWidget::itemChange(GraphicsItemChange
    change, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#itemChange

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
    #  QVariant QGraphicsWidget::itemChange(GraphicsItemChange change, const
    #      QVariant &value)
    address = self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget10itemChangeEN13QGraphicsItem18Graph'
        'icsItemChangeERK8QVariant',
        change.value, self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str, QVariant)
  def propertyChange(self, propertyName: str, value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsWidget::propertyChange(const QString
    &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#propertyChange

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
    #      const QVariant &value)
    address = self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVaria'
        'nt',
        propertyName, self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QEvent)
  @overload(NoneType)
  def sceneEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::sceneEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#sceneEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsWidget::sceneEvent(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget10sceneEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def windowFrameEvent(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::windowFrameEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#windowFrameEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget16windowFrameEventEP6QEvent',
        self._addressOf(e),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsWidget::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget5eventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::changeEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget11changeEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, event: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::closeEvent(QCloseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#closeEvent

    Parameters
    ----------

    event : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::closeEvent(QCloseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget10closeEventEP11QCloseEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidget::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QGraphicsWidget::focusNextPrevChild(bool next)
    return self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget18focusNextPrevChildEb', next,
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::focusOutEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget13focusOutEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::hideEvent(QHideEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::hideEvent(QHideEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget9hideEventEP10QHideEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMoveEvent)
  @overload(NoneType)
  def moveEvent(self, event: Optional[QGraphicsSceneMoveEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#moveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEven'
        't',
        self._addressOf(event),
    )

  def polishEvent(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::polishEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#polishEvent
    """
    #  void QGraphicsWidget::polishEvent()
    self.uglySide.call('ritual_own_ZN15QGraphicsWidget11polishEventEv')

  @overload(QGraphicsSceneResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QGraphicsSceneResizeEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResiz'
        'eEvent',
        self._addressOf(event),
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidget.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::showEvent(QShowEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget9showEventEP10QShowEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget14hoverMoveEventEP24QGraphicsSceneHo'
        'verEvent',
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
    QGraphicsWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget15hoverLeaveEventEP24QGraphicsSceneH'
        'overEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def grabMouseEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::grabMouseEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#grabMouseEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::grabMouseEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget14grabMouseEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def ungrabMouseEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::ungrabMouseEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#ungrabMouseEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::ungrabMouseEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def grabKeyboardEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::grabKeyboardEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#grabKeyboardEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def ungrabKeyboardEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidget.html#ungrabKeyboardEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent',
        self._addressOf(event),
    )
