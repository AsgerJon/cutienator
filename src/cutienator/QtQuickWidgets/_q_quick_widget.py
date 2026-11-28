"""
QQuickWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickWidgets/qquickwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from ..QtWidgets import QWidget
from ..QtQuick import QQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QTimerEvent, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QColor, QDragEnterEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QFocusEvent, QHideEvent
  from ..QtGui import QImage, QKeyEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QResizeEvent, QShowEvent, QSurfaceFormat, QWheelEvent
  from ..QtQml import QQmlComponent, QQmlContext, QQmlEngine, QQmlError
  from ..QtQuick import QQuickItem
  from . import QQuickWidgetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHideEvent = WAIT['QHideEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlEngine = WAIT['QQmlEngine']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QTimerEvent = WAIT['QTimerEvent']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWidget(QWidget):
  """
  The cute side of Qt's QQuickWidget: a plain Python object standing in front
  of one C++ QQuickWidget.

  It is built on the cute 'QWidget', as Qt's QQuickWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWidget that has a ritual and that Python can
  call so far, 49 names in all: 'metaObject', 'tr', 'source', 'engine',
  'rootContext', 'rootObject', 'resizeMode', 'setResizeMode', 'status',
  'errors', 'sizeHint', 'initialSize', 'setFormat', 'format',
  'grabFramebuffer', 'setClearColor', 'quickWindow', 'setSource',
  'setContent', 'setInitialProperties', 'loadFromModule', 'statusChanged',
  'sceneGraphError', 'continueExecute', 'createFramebufferObject',
  'destroyFramebufferObject', 'triggerUpdate', 'propagateFocusObjectChanged',
  'resizeEvent', 'timerEvent', 'keyPressEvent', 'keyReleaseEvent',
  'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent',
  'mouseDoubleClickEvent', 'showEvent', 'hideEvent', 'focusInEvent',
  'focusOutEvent', 'wheelEvent', 'dragEnterEvent', 'dragMoveEvent',
  'dragLeaveEvent', 'dropEvent', 'event', 'paintEvent', 'focusNextPrevChild',
  'd_func'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWidget::~QQuickWidget()': the destructor: Python never
    removes a C++ QQuickWidget.
  - Qt's 'const QQuickWidgetPrivate *QQuickWidget::d_func() const': takes in
    Python what 'QQuickWidgetPrivate *QQuickWidget::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 61 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWidget is created at the first use, not by
    'QQuickWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWidget.
  - Qt tells when it has removed the C++ QQuickWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWidget, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ResizeMode(CuteNum):
    """
    The enum 'QQuickWidget::ResizeMode' of Qt, with the 2 names Qt gives in
    it.
    """

    SizeViewToRootObject = Kee[int](0)
    SizeRootObjectToView = Kee[int](1)

  class Status(CuteNum):
    """
    The enum 'QQuickWidget::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuickWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#tr

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
    #  QString QQuickWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWidget'

  #  A C++ QQuickWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWidget::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWidget::source() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQuickWidget::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQuickWidget::engine() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget6engineEv')
    from ..QtQml import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def rootContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQuickWidget::rootContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#rootContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQuickWidget::rootContext() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget11rootContextEv')
    from ..QtQml import QQmlContext
    return QQmlContext._cuteAt(address)

  def rootObject(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWidget::rootObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#rootObject

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWidget::rootObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget10rootObjectEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def resizeMode(self) -> ResizeMode:
    """
    Calls Qt's 'ResizeMode QQuickWidget::resizeMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#resizeMode

    Returns
    -------

    ResizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResizeMode(number)'
      gives.
    """
    #  ResizeMode QQuickWidget::resizeMode() const
    return QQuickWidget.ResizeMode(self.uglySide.call(
        'ritual_ZNK12QQuickWidget10resizeModeEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickWidget::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickWidget::status() const
    return QQuickWidget.Status(self.uglySide.call(
        'ritual_ZNK12QQuickWidget6statusEv',
    ))

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQuickWidget::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQuickWidget::errors() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget6errorsEv')
    from ..QtQml import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickWidget::sizeHint() const
    ritual = 'ritual_ZNK12QQuickWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def initialSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickWidget::initialSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#initialSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickWidget::initialSize() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget11initialSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QQuickWidget::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QQuickWidget::format() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget6formatEv')
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickWidget::grabFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickWidget::grabFramebuffer() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickWidget15grabFramebufferEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def quickWindow(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickWidget::quickWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#quickWindow

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickWidget::quickWindow() const
    address = self.uglySide.call('ritual_ZNK12QQuickWidget11quickWindowEv')
    return QQuickWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ResizeMode)
  def setResizeMode(self, a0: ResizeMode) -> None:
    """
    Calls Qt's 'void QQuickWidget::setResizeMode(ResizeMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#setResizeMode

    Parameters
    ----------

    a0 : ResizeMode
      Passed on as its number.
    """
    #  void QQuickWidget::setResizeMode(ResizeMode a0)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget13setResizeModeENS_10ResizeModeE', a0.value,
    )

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QQuickWidget::setFormat(const QSurfaceFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QQuickWidget::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(QColor)
  def setClearColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickWidget::setClearColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#setClearColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickWidget::setClearColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget13setClearColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickWidget::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickWidget::setSource(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget9setSourceERK4QUrl', self._valueOf(a0),
    )

  @overload(QUrl, QQmlComponent, QObject)
  @overload(QUrl, QQmlComponent, NoneType)
  @overload(QUrl, NoneType, QObject)
  @overload(QUrl, NoneType, NoneType)
  def setContent(
      self,
      url: QUrl,
      component: Optional[QQmlComponent],
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickWidget::setContent(const QUrl &url, QQmlComponent
    *component, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#setContent

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::setContent(const QUrl &url, QQmlComponent
    #      *component, QObject *item)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget10setContentERK4QUrlP13QQmlComponentP7QObje'
        'ct',
        self._valueOf(url), self._addressOf(component), self._addressOf(item,
        'QObject'),
    )

  @overload(QMap[str, QVariant])
  def setInitialProperties(
      self,
      initialProperties: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQuickWidget::setInitialProperties(const QVariantMap
    &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#setInitialProperties

    Parameters
    ----------

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickWidget::setInitialProperties(const QVariantMap
    #      &initialProperties)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget20setInitialPropertiesERK4QMapI7QString8QVa'
        'riantE',
        self._valueOf(initialProperties),
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
    Notes what was given, for Qt's 'QQuickWidget::QQuickWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#QQuickWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWidget::QQuickWidget(QWidget *parent)
    self._noteCreation(QQuickWidget, lambda: Rituals.call(
        'ritual_ZN12QQuickWidgetC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QQmlEngine, QWidget)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      parent: Optional[QWidget],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickWidget::QQuickWidget(QQmlEngine
    *engine, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#QQuickWidget

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWidget::QQuickWidget(QQmlEngine *engine, QWidget *parent)
    self._noteCreation(QQuickWidget, lambda: Rituals.call(
        'ritual_ZN12QQuickWidgetC1EP10QQmlEngineP7QWidget',
        self._addressOf(engine), self._addressOf(parent),
    ))

  @overload(QUrl)
  @overload(QUrl, QWidget)
  @overload(QUrl, NoneType)
  def __init__(self, source: QUrl, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickWidget::QQuickWidget(const QUrl
    &source, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#QQuickWidget

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWidget::QQuickWidget(const QUrl &source, QWidget *parent)
    self._noteCreation(QQuickWidget, lambda: Rituals.call(
        'ritual_ZN12QQuickWidgetC1ERK4QUrlP7QWidget',
        self._valueOf(source), self._addressOf(parent),
    ))

  @overload(str, str)
  @overload(str, str, QWidget)
  @overload(str, str, NoneType)
  def __init__(
      self,
      uri: str,
      typeName: str,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickWidget::QQuickWidget(QAnyStringView
    uri, QAnyStringView typeName, QWidget *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#QQuickWidget

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWidget::QQuickWidget(QAnyStringView uri, QAnyStringView
    #      typeName, QWidget *parent)
    self._noteCreation(QQuickWidget, lambda: Rituals.call(
        'ritual_ZN12QQuickWidgetC1E14QAnyStringViewS0_P7QWidget',
        uri, typeName, self._addressOf(parent),
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

  @overload(str, str)
  def loadFromModule(self, uri: str, typeName: str) -> None:
    """
    Calls Qt's 'void QQuickWidget::loadFromModule(QAnyStringView uri,
    QAnyStringView typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#loadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWidget::loadFromModule(QAnyStringView uri, QAnyStringView
    #      typeName)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget14loadFromModuleE14QAnyStringViewS0_',
        uri, typeName,
    )

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQuickWidget::statusChanged(QQuickWidget::Status a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQuickWidget::statusChanged(QQuickWidget::Status a0)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget13statusChangedENS_6StatusE', a0.value,
    )

  @overload(QQuickWindow.SceneGraphError, str)
  def sceneGraphError(
      self,
      error: QQuickWindow.SceneGraphError,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWidget::sceneGraphError(QQuickWindow::SceneGraphError error, const
    QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#sceneGraphError

    Parameters
    ----------

    error : QQuickWindow.SceneGraphError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWidget::sceneGraphError(QQuickWindow::SceneGraphError
    #      error, const QString &message)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget15sceneGraphErrorEN12QQuickWindow15SceneGra'
        'phErrorERK7QString',
        error.value, message,
    )

  def continueExecute(self) -> None:
    """
    Calls Qt's 'void QQuickWidget::continueExecute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#continueExecute
    """
    #  void QQuickWidget::continueExecute()
    self.uglySide.call('ritual_ZN12QQuickWidget15continueExecuteEv')

  def createFramebufferObject(self) -> None:
    """
    Calls Qt's 'void QQuickWidget::createFramebufferObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#createFramebufferObject
    """
    #  void QQuickWidget::createFramebufferObject()
    self.uglySide.call('ritual_ZN12QQuickWidget23createFramebufferObjectEv')

  def destroyFramebufferObject(self) -> None:
    """
    Calls Qt's 'void QQuickWidget::destroyFramebufferObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#destroyFramebufferObject
    """
    #  void QQuickWidget::destroyFramebufferObject()
    self.uglySide.call('ritual_ZN12QQuickWidget24destroyFramebufferObjectEv')

  def triggerUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickWidget::triggerUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#triggerUpdate
    """
    #  void QQuickWidget::triggerUpdate()
    self.uglySide.call('ritual_ZN12QQuickWidget13triggerUpdateEv')

  @overload(QObject)
  @overload(NoneType)
  def propagateFocusObjectChanged(
      self,
      focusObject: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickWidget::propagateFocusObjectChanged(QObject
    *focusObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#propagateFocusObjectChanged

    Parameters
    ----------

    focusObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::propagateFocusObjectChanged(QObject *focusObject)
    self.uglySide.call(
        'ritual_ZN12QQuickWidget27propagateFocusObjectChangedEP7QObject',
        self._addressOf(focusObject, 'QObject'),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::keyReleaseEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWidget17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::mouseDoubleClickEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#mouseDoubleClickEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::mouseDoubleClickEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWidget21mouseDoubleClickEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::showEvent(QShowEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN12QQuickWidget12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN12QQuickWidget13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::wheelEvent(QWheelEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::wheelEvent(QWheelEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, a0: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::dragEnterEvent(QDragEnterEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#dragEnterEvent

    Parameters
    ----------

    a0 : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::dragEnterEvent(QDragEnterEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWidget14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, a0: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::dragMoveEvent(QDragMoveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#dragMoveEvent

    Parameters
    ----------

    a0 : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::dragMoveEvent(QDragMoveEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::dragLeaveEvent(QDragLeaveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#dragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::dragLeaveEvent(QDragLeaveEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickWidget14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, a0: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::dropEvent(QDropEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#dropEvent

    Parameters
    ----------

    a0 : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::dropEvent(QDropEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickWidget::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWidget::event(QEvent *a0)
    ritual = 'ritual_ZN12QQuickWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QQuickWidget::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWidget::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN12QQuickWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QQuickWidget::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidget.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QQuickWidget::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN12QQuickWidget18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickWidget18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  def d_func(self) -> Optional[QQuickWidgetPrivate]:
    """
    Calls Qt's 'QQuickWidgetPrivate *QQuickWidget::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidget.html#d_func

    Returns
    -------

    Optional[QQuickWidgetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWidgetPrivate *QQuickWidget::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickWidget6d_funcEv')
    from . import QQuickWidgetPrivate
    return QQuickWidgetPrivate._cuteAt(address)
