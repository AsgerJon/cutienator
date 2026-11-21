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
from ..QtCore import Qt
from . import QGraphicsItem, QGraphicsWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
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
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'setWidget',
  'widget', 'subWidgetRect', 'setGeometry', 'paint', 'type',
  'createProxyForChildWidget'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsProxyWidget::~QGraphicsProxyWidget()': the destructor:
    Python never removes a C++ QGraphicsProxyWidget.

  What has no ritual
  ------------------

  38 of the 49 functions Qt declares: 30 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

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
    return self.uglySide.call('ritual_ZNK20QGraphicsProxyWidget4typeEv')

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
    self.uglySide.call(
        'ritual_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF',
        self._valueOf(rect),
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
    self.uglySide.call(
        'ritual_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget',
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
