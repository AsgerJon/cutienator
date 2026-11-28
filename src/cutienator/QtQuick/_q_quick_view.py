"""
QQuickView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from ..QtGui import QWindow
from . import QQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize, QTimerEvent, QUrl, QVariant
  from ..QtGui import QKeyEvent, QMouseEvent, QResizeEvent
  from ..QtQml import QQmlComponent, QQmlContext, QQmlEngine, QQmlError
  from . import QQuickItem, QQuickRenderControl, QQuickViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlEngine = WAIT['QQmlEngine']
  QQuickRenderControl = WAIT['QQuickRenderControl']
  QResizeEvent = WAIT['QResizeEvent']
  QTimerEvent = WAIT['QTimerEvent']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickView(QQuickWindow):
  """
  The cute side of Qt's QQuickView: a plain Python object standing in front
  of one C++ QQuickView.

  It is built on the cute 'QQuickWindow', as Qt's QQuickView is built on Qt's
  QQuickWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickView that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'source', 'engine',
  'rootContext', 'rootObject', 'resizeMode', 'setResizeMode', 'status',
  'errors', 'sizeHint', 'initialSize', 'setSource', 'loadFromModule',
  'setInitialProperties', 'setContent', 'statusChanged', 'continueExecute',
  'resizeEvent', 'timerEvent', 'keyPressEvent', 'keyReleaseEvent',
  'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'd_func'. It can
  be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickView::~QQuickView()': the destructor: Python never removes a
    C++ QQuickView.
  - Qt's 'const QQuickViewPrivate *QQuickView::d_func() const': takes in
    Python what 'QQuickViewPrivate *QQuickView::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickView is created at the first use, not by 'QQuickView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickView.
  - Qt tells when it has removed the C++ QQuickView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickView, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ResizeMode(CuteNum):
    """
    The enum 'QQuickView::ResizeMode' of Qt, with the 2 names Qt gives in it.
    """

    SizeViewToRootObject = Kee[int](0)
    SizeRootObjectToView = Kee[int](1)

  class Status(CuteNum):
    """
    The enum 'QQuickView::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString QQuickView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#tr

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
    #  QString QQuickView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickView'

  #  A C++ QQuickView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickView::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickView::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickView::source() const
    address = self.uglySide.call('ritual_ZNK10QQuickView6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQuickView::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQuickView::engine() const
    address = self.uglySide.call('ritual_ZNK10QQuickView6engineEv')
    from ..QtQml import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def rootContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQuickView::rootContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#rootContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQuickView::rootContext() const
    address = self.uglySide.call('ritual_ZNK10QQuickView11rootContextEv')
    from ..QtQml import QQmlContext
    return QQmlContext._cuteAt(address)

  def rootObject(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickView::rootObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#rootObject

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickView::rootObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickView10rootObjectEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def resizeMode(self) -> ResizeMode:
    """
    Calls Qt's 'ResizeMode QQuickView::resizeMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#resizeMode

    Returns
    -------

    ResizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResizeMode(number)'
      gives.
    """
    #  ResizeMode QQuickView::resizeMode() const
    return QQuickView.ResizeMode(self.uglySide.call(
        'ritual_ZNK10QQuickView10resizeModeEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickView::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickView::status() const
    return QQuickView.Status(self.uglySide.call(
        'ritual_ZNK10QQuickView6statusEv',
    ))

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQuickView::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQuickView::errors() const
    address = self.uglySide.call('ritual_ZNK10QQuickView6errorsEv')
    from ..QtQml import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickView::sizeHint() const
    address = self.uglySide.call('ritual_ZNK10QQuickView8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def initialSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickView::initialSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#initialSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickView::initialSize() const
    address = self.uglySide.call('ritual_ZNK10QQuickView11initialSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ResizeMode)
  def setResizeMode(self, a0: ResizeMode) -> None:
    """
    Calls Qt's 'void QQuickView::setResizeMode(ResizeMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#setResizeMode

    Parameters
    ----------

    a0 : ResizeMode
      Passed on as its number.
    """
    #  void QQuickView::setResizeMode(ResizeMode a0)
    self.uglySide.call(
        'ritual_ZN10QQuickView13setResizeModeENS_10ResizeModeE', a0.value,
    )

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickView::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickView::setSource(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN10QQuickView9setSourceERK4QUrl', self._valueOf(a0),
    )

  @overload(QMap[str, QVariant])
  def setInitialProperties(
      self,
      initialProperties: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQuickView::setInitialProperties(const QVariantMap
    &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickview.html#setInitialProperties

    Parameters
    ----------

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickView::setInitialProperties(const QVariantMap
    #      &initialProperties)
    self.uglySide.call(
        'ritual_ZN10QQuickView20setInitialPropertiesERK4QMapI7QString8QVari'
        'antE',
        self._valueOf(initialProperties),
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
    Calls Qt's 'void QQuickView::setContent(const QUrl &url, QQmlComponent
    *component, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#setContent

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
    #  void QQuickView::setContent(const QUrl &url, QQmlComponent *component,
    #      QObject *item)
    self.uglySide.call(
        'ritual_ZN10QQuickView10setContentERK4QUrlP13QQmlComponentP7QObject',
        self._valueOf(url), self._addressOf(component), self._addressOf(item,
        'QObject'),
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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickView::QQuickView(QWindow *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#QQuickView

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickView::QQuickView(QWindow *parent)
    self._noteCreation(QQuickView, lambda: Rituals.call(
        'ritual_ZN10QQuickViewC1EP7QWindow', self._addressOf(parent),
    ))

  @overload(QQmlEngine, QWindow)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      parent: Optional[QWindow],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickView::QQuickView(QQmlEngine
    *engine, QWindow *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#QQuickView

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickView::QQuickView(QQmlEngine *engine, QWindow *parent)
    self._noteCreation(QQuickView, lambda: Rituals.call(
        'ritual_ZN10QQuickViewC1EP10QQmlEngineP7QWindow',
        self._addressOf(engine), self._addressOf(parent),
    ))

  @overload(QUrl)
  @overload(QUrl, QWindow)
  @overload(QUrl, NoneType)
  def __init__(self, source: QUrl, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickView::QQuickView(const QUrl
    &source, QWindow *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#QQuickView

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickView::QQuickView(const QUrl &source, QWindow *parent)
    self._noteCreation(QQuickView, lambda: Rituals.call(
        'ritual_ZN10QQuickViewC1ERK4QUrlP7QWindow',
        self._valueOf(source), self._addressOf(parent),
    ))

  @overload(str, str)
  @overload(str, str, QWindow)
  @overload(str, str, NoneType)
  def __init__(
      self,
      uri: str,
      typeName: str,
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickView::QQuickView(QAnyStringView
    uri, QAnyStringView typeName, QWindow *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#QQuickView

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickView::QQuickView(QAnyStringView uri, QAnyStringView typeName,
    #      QWindow *parent)
    self._noteCreation(QQuickView, lambda: Rituals.call(
        'ritual_ZN10QQuickViewC1E14QAnyStringViewS0_P7QWindow',
        uri, typeName, self._addressOf(parent),
    ))

  @overload(QUrl, QQuickRenderControl)
  def __init__(
      self,
      source: QUrl,
      renderControl: Optional[QQuickRenderControl],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickView::QQuickView(const QUrl
    &source, QQuickRenderControl *renderControl)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#QQuickView

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    renderControl : Optional[QQuickRenderControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickView::QQuickView(const QUrl &source, QQuickRenderControl
    #      *renderControl)
    self._noteCreation(QQuickView, lambda: Rituals.call(
        'ritual_ZN10QQuickViewC1ERK4QUrlP19QQuickRenderControl',
        self._valueOf(source), self._addressOf(renderControl),
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
    Calls Qt's 'void QQuickView::loadFromModule(QAnyStringView uri,
    QAnyStringView typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#loadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickView::loadFromModule(QAnyStringView uri, QAnyStringView
    #      typeName)
    self.uglySide.call(
        'ritual_ZN10QQuickView14loadFromModuleE14QAnyStringViewS0_',
        uri, typeName,
    )

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQuickView::statusChanged(QQuickView::Status a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQuickView::statusChanged(QQuickView::Status a0)
    self.uglySide.call(
        'ritual_ZN10QQuickView13statusChangedENS_6StatusE', a0.value,
    )

  def continueExecute(self) -> None:
    """
    Calls Qt's 'void QQuickView::continueExecute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#continueExecute
    """
    #  void QQuickView::continueExecute()
    self.uglySide.call('ritual_ZN10QQuickView15continueExecuteEv')

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN10QQuickView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN10QQuickView10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN10QQuickView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::keyReleaseEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN10QQuickView15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QQuickView15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QQuickView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickView::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickView::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QQuickView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickView14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def d_func(self) -> Optional[QQuickViewPrivate]:
    """
    Calls Qt's 'QQuickViewPrivate *QQuickView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickview.html#d_func

    Returns
    -------

    Optional[QQuickViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickViewPrivate *QQuickView::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickView6d_funcEv')
    from . import QQuickViewPrivate
    return QQuickViewPrivate._cuteAt(address)
