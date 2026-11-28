"""
qdesigner_internal::ZoomWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::ZoomWidget to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtWidgets import QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QSizeF
  from ..QtGui import QResizeEvent
  from ..QtWidgets import QGraphicsItem, QGraphicsProxyWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGraphicsItem = WAIT['QGraphicsItem']
  QResizeEvent = WAIT['QResizeEvent']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ZoomWidget(qdesigner_internal.ZoomView):
  """
  The cute side of Qt's qdesigner_internal::ZoomWidget: a plain Python object
  standing in front of one C++ qdesigner_internal::ZoomWidget.

  It is built on the cute 'qdesigner_internal::ZoomView', as Qt's
  qdesigner_internal::ZoomWidget is built on Qt's
  qdesigner_internal::ZoomView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ZoomWidget that has a ritual and
  that Python can call so far, 20 names in all: 'metaObject', 'tr',
  'setWidget', 'proxy', 'isWidgetZoomContextMenuEnabled',
  'setWidgetZoomContextMenuEnabled', 'setItemAcceptDrops', 'itemAcceptDrops',
  'minimumSizeHint', 'sizeHint', 'zoomedEventFilter', 'dump', 'resizeEvent',
  'applyZoom', 'doResize', 'createProxyWidget', 'resizeToWidgetSize',
  'viewPortMargin', 'widgetSize', 'widgetDecorationSizeF'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ZoomWidget::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ZoomWidget::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsProxyWidget *qdesigner_internal::ZoomWidget::proxy()':
    takes in Python what 'const QGraphicsProxyWidget
    *qdesigner_internal::ZoomWidget::proxy() const' takes.
  - Qt's 'QSize qdesigner_internal::ZoomWidget::widgetSizeToViewSize(const
    QSize &s, bool *ptrToValid) const': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 31 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ZoomWidget is created at the first use, not
    by 'qdesigner_internal::ZoomWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ZoomWidget.
  - Qt tells when it has removed the C++ qdesigner_internal::ZoomWidget.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ZoomWidget that has no cute
    function yet, 'widgetSizeToViewSize', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::ZoomWidget::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#tr

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
    #  QString qdesigner_internal::ZoomWidget::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ZoomWidget'

  #  The functions Qt calls itself that qdesigner_internal::ZoomWidget is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'doResize': (
          ('_ZN18qdesigner_internal10ZoomWidget8doResizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'createProxyWidget': (
          ('_ZNK18qdesigner_internal10ZoomWidget17createProxyWidgetEP13QGra'
           'phicsItem6QFlagsIN2Qt10WindowTypeEE',
           ('address', 'address', 'QtWidgets:QGraphicsProxyWidget'),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
               ('int', 'flags', 'QtCore:Qt.WindowType'),
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
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::ZoomWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ZoomWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def proxy(self) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'const QGraphicsProxyWidget
    *qdesigner_internal::ZoomWidget::proxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#proxy

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsProxyWidget *qdesigner_internal::ZoomWidget::proxy()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget5proxyEv',
    )
    from ..QtWidgets import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  def isWidgetZoomContextMenuEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ZoomWidget::isWidgetZoomContextMenuEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html
    """
    #  bool qdesigner_internal::ZoomWidget::isWidgetZoomContextMenuEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget30isWidgetZoomContextMen'
        'uEnabledEv',
    )

  def itemAcceptDrops(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ZoomWidget::itemAcceptDrops()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#itemAcceptDrops
    """
    #  bool qdesigner_internal::ZoomWidget::itemAcceptDrops() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget15itemAcceptDropsEv',
    )

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::ZoomWidget::minimumSizeHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::ZoomWidget::minimumSizeHint() const
    ritual = 'ritual_ZNK18qdesigner_internal10ZoomWidget15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal10ZoomWidget15minimumSizeHintE'
          'v')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::ZoomWidget::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::ZoomWidget::sizeHint() const
    ritual = 'ritual_ZNK18qdesigner_internal10ZoomWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal10ZoomWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def createProxyWidget(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget
    *qdesigner_internal::ZoomWidget::createProxyWidget(QGraphicsItem *parent,
    Qt::WindowFlags wFlags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget
    #      *qdesigner_internal::ZoomWidget::createProxyWidget(QGraphicsItem
    #      *parent, Qt::WindowFlags wFlags) const
    ritual = (
        'ritual_ZNK18qdesigner_internal10ZoomWidget17createProxyWidgetEP13Q'
        'GraphicsItem6QFlagsIN2Qt10WindowTypeEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal10ZoomWidget17createProxyWidge'
          'tEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE')
    address = self.uglySide.call(
        ritual, self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
    )
    from ..QtWidgets import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  def viewPortMargin(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::ZoomWidget::viewPortMargin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#viewPortMargin

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::ZoomWidget::viewPortMargin() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget14viewPortMarginEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def widgetSize(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::ZoomWidget::widgetSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#widgetSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::ZoomWidget::widgetSize() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget10widgetSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def widgetDecorationSizeF(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF
    qdesigner_internal::ZoomWidget::widgetDecorationSizeF() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF qdesigner_internal::ZoomWidget::widgetDecorationSizeF() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ZoomWidget21widgetDecorationSizeFE'
        'v',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def setWidget(
      self,
      w: Optional[QWidget],
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::setWidget(QWidget *w,
    Qt::WindowFlags wFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#setWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  void qdesigner_internal::ZoomWidget::setWidget(QWidget *w,
    #      Qt::WindowFlags wFlags)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget9setWidgetEP7QWidget6QFla'
        'gsIN2Qt10WindowTypeEE',
        self._addressOf(w), wFlags.value,
    )

  @overload(bool)
  def setWidgetZoomContextMenuEnabled(self, e: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ZoomWidget::setWidgetZoomContextMenuEnabled(bool e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html

    Parameters
    ----------

    e : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomWidget::setWidgetZoomContextMenuEnabled(
    #      bool e)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget31setWidgetZoomContextMen'
        'uEnabledEb',
        e,
    )

  @overload(bool)
  def setItemAcceptDrops(self, a0: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::setItemAcceptDrops(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomWidget::setItemAcceptDrops(bool a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget18setItemAcceptDropsEb',
        a0,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ZoomWidget::ZoomWidget(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#ZoomWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::ZoomWidget::ZoomWidget(QWidget *parent)
    self._noteCreation(ZoomWidget, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal10ZoomWidgetC1EP7QWidget',
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def zoomedEventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ZoomWidget::zoomedEventFilter(QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ZoomWidget::zoomedEventFilter(QObject
    #      *watched, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget17zoomedEventFilterEP7QOb'
        'jectP6QEvent',
        self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def dump(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::dump() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#dump
    """
    #  void qdesigner_internal::ZoomWidget::dump() const
    self.uglySide.call('ritual_ZNK18qdesigner_internal10ZoomWidget4dumpEv')

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::resizeEvent(QResizeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ZoomWidget::resizeEvent(QResizeEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal10ZoomWidget11resizeEventEP12QResizeE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal10ZoomWidget11resizeEventEP12QR'
          'esizeEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def applyZoom(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::applyZoom()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#applyZoom
    """
    #  void qdesigner_internal::ZoomWidget::applyZoom()
    ritual = 'ritual_ZN18qdesigner_internal10ZoomWidget9applyZoomEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal10ZoomWidget9applyZoomEv'
    self.uglySide.call(ritual)

  @overload(QSize)
  def doResize(self, s: QSize) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::doResize(const QSize
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html#doResize

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void qdesigner_internal::ZoomWidget::doResize(const QSize &s)
    ritual = 'ritual_ZN18qdesigner_internal10ZoomWidget8doResizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal10ZoomWidget8doResizeERK5QSize')
    self.uglySide.call(ritual, self._valueOf(s))

  def resizeToWidgetSize(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomWidget::resizeToWidgetSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomwidget.html
    """
    #  void qdesigner_internal::ZoomWidget::resizeToWidgetSize()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ZoomWidget18resizeToWidgetSizeEv',
    )

  @staticmethod
  def widgetSizeToViewSize(*__, **_) -> Never:
    """
    Qt's 'QSize qdesigner_internal::ZoomWidget::widgetSizeToViewSize(const
    QSize &s, bool *ptrToValid) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ZoomWidget.widgetSizeToViewSize' has no cute "
        "function yet. Qt's 'QSize "
        "qdesigner_internal::ZoomWidget::widgetSizeToViewSize(const QSize "
        "&s, bool *ptrToValid) const': takes a number to change where it is."
    )
