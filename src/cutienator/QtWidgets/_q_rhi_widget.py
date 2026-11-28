"""
QRhiWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qrhiwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QImage, QPaintEvent, QResizeEvent, QRhi
  from ..QtGui import QRhiCommandBuffer, QRhiRenderBuffer, QRhiRenderTarget
  from ..QtGui import QRhiTexture
  from . import QRhiWidgetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiWidget(QWidget):
  """
  The cute side of Qt's QRhiWidget: a plain Python object standing in front
  of one C++ QRhiWidget.

  It is built on the cute 'QWidget', as Qt's QRhiWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiWidget that has a ritual and that Python can
  call so far, 36 names in all: 'metaObject', 'tr', 'd_func', 'api',
  'setApi', 'isDebugLayerEnabled', 'setDebugLayerEnabled', 'sampleCount',
  'setSampleCount', 'colorBufferFormat', 'setColorBufferFormat',
  'fixedColorBufferSize', 'setFixedColorBufferSize',
  'isMirrorVerticallyEnabled', 'setMirrorVertically', 'grabFramebuffer',
  'isAutoRenderTargetEnabled', 'setAutoRenderTarget', 'initialize', 'render',
  'releaseResources', 'rhi', 'colorTexture', 'msaaColorBuffer',
  'resolveTexture', 'depthStencilBuffer', 'renderTarget', 'resizeEvent',
  'paintEvent', 'event', 'frameSubmitted', 'renderFailed',
  'sampleCountChanged', 'colorBufferFormatChanged',
  'fixedColorBufferSizeChanged', 'mirrorVerticallyChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRhiWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QRhiWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QRhiWidgetPrivate *QRhiWidget::d_func() const': takes in
    Python what 'QRhiWidgetPrivate *QRhiWidget::d_func()' takes.
  - Qt's 'QRhiWidget::~QRhiWidget()': the destructor: Python never removes a
    C++ QRhiWidget.
  - Qt's 'QRhiWidget::QRhiWidget(QRhiWidgetPrivate &dd, QWidget *parent,
    Qt::WindowFlags f)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 45 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRhiWidget is created at the first use, not by 'QRhiWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiWidget.
  - Qt tells when it has removed the C++ QRhiWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QRhiWidget, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Api(CuteNum, scoped=True):
    """
    The enum 'QRhiWidget::Api' of Qt, with the 6 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Null = Kee[int](0)
    OpenGL = Kee[int](1)
    Metal = Kee[int](2)
    Vulkan = Kee[int](3)
    Direct3D11 = Kee[int](4)
    Direct3D12 = Kee[int](5)

  class TextureFormat(CuteNum, scoped=True):
    """
    The enum 'QRhiWidget::TextureFormat' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    RGBA8 = Kee[int](0)
    RGBA16F = Kee[int](1)
    RGBA32F = Kee[int](2)
    RGB10A2 = Kee[int](3)

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
    Calls Qt's 'QString QRhiWidget::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#tr

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
    #  QString QRhiWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QRhiWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiWidget'

  #  A C++ QRhiWidget Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiWidget'

  #  The functions Qt calls itself that QRhiWidget is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'render': (
          ('_ZN10QRhiWidget6renderEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'releaseResources': (
          ('_ZN10QRhiWidget16releaseResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QRhiWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRhiWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def api(self) -> Api:
    """
    Calls Qt's 'Api QRhiWidget::api() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#api

    Returns
    -------

    Api
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Api(number)' gives.
    """
    #  Api QRhiWidget::api() const
    return QRhiWidget.Api(self.uglySide.call('ritual_ZNK10QRhiWidget3apiEv'))

  def isDebugLayerEnabled(self) -> bool:
    """
    Calls Qt's 'bool QRhiWidget::isDebugLayerEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#isDebugLayerEnabled
    """
    #  bool QRhiWidget::isDebugLayerEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10QRhiWidget19isDebugLayerEnabledEv',
    )

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiWidget::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#sampleCount
    """
    #  int QRhiWidget::sampleCount() const
    return self.uglySide.call('ritual_ZNK10QRhiWidget11sampleCountEv')

  def colorBufferFormat(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat QRhiWidget::colorBufferFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#colorBufferFormat

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat QRhiWidget::colorBufferFormat() const
    return QRhiWidget.TextureFormat(self.uglySide.call(
        'ritual_ZNK10QRhiWidget17colorBufferFormatEv',
    ))

  def fixedColorBufferSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiWidget::fixedColorBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#fixedColorBufferSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiWidget::fixedColorBufferSize() const
    address = self.uglySide.call(
        'ritual_ZNK10QRhiWidget20fixedColorBufferSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isMirrorVerticallyEnabled(self) -> bool:
    """
    Calls Qt's 'bool QRhiWidget::isMirrorVerticallyEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#isMirrorVerticallyEnabled
    """
    #  bool QRhiWidget::isMirrorVerticallyEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10QRhiWidget25isMirrorVerticallyEnabledEv',
    )

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QRhiWidget::grabFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRhiWidget::grabFramebuffer() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget15grabFramebufferEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def isAutoRenderTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool QRhiWidget::isAutoRenderTargetEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#isAutoRenderTargetEnabled
    """
    #  bool QRhiWidget::isAutoRenderTargetEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10QRhiWidget25isAutoRenderTargetEnabledEv',
    )

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QRhiWidget::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QRhiWidget::rhi() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def colorTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiWidget::colorTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#colorTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiWidget::colorTexture() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget12colorTextureEv')
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def msaaColorBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QRhiWidget::msaaColorBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#msaaColorBuffer

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiWidget::msaaColorBuffer() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget15msaaColorBufferEv')
    from ..QtGui import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def resolveTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiWidget::resolveTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#resolveTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiWidget::resolveTexture() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget14resolveTextureEv')
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def depthStencilBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QRhiWidget::depthStencilBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#depthStencilBuffer

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiWidget::depthStencilBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK10QRhiWidget18depthStencilBufferEv',
    )
    from ..QtGui import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def renderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QRhiWidget::renderTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#renderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QRhiWidget::renderTarget() const
    address = self.uglySide.call('ritual_ZNK10QRhiWidget12renderTargetEv')
    from ..QtGui import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Api)
  def setApi(self, api: Api) -> None:
    """
    Calls Qt's 'void QRhiWidget::setApi(Api api)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#setApi

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  void QRhiWidget::setApi(Api api)
    self.uglySide.call('ritual_ZN10QRhiWidget6setApiENS_3ApiE', api.value)

  @overload(bool)
  def setDebugLayerEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QRhiWidget::setDebugLayerEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setDebugLayerEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QRhiWidget::setDebugLayerEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget20setDebugLayerEnabledEb', enable,
    )

  @overload(int)
  def setSampleCount(self, samples: int) -> None:
    """
    Calls Qt's 'void QRhiWidget::setSampleCount(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#setSampleCount

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QRhiWidget::setSampleCount(int samples)
    self.uglySide.call('ritual_ZN10QRhiWidget14setSampleCountEi', samples)

  @overload(TextureFormat)
  def setColorBufferFormat(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void QRhiWidget::setColorBufferFormat(TextureFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setColorBufferFormat

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void QRhiWidget::setColorBufferFormat(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget20setColorBufferFormatENS_13TextureFormatE',
        format.value,
    )

  @overload(QSize)
  def setFixedColorBufferSize(self, pixelSize: QSize) -> None:
    """
    Calls Qt's 'void QRhiWidget::setFixedColorBufferSize(QSize pixelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setFixedColorBufferSize

    Parameters
    ----------

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiWidget::setFixedColorBufferSize(QSize pixelSize)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget23setFixedColorBufferSizeE5QSize',
        self._valueOf(pixelSize),
    )

  @overload(int, int)
  def setFixedColorBufferSize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QRhiWidget::setFixedColorBufferSize(int w, int h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setFixedColorBufferSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QRhiWidget::setFixedColorBufferSize(int w, int h)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget23setFixedColorBufferSizeEii', w, h,
    )

  @overload(bool)
  def setMirrorVertically(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QRhiWidget::setMirrorVertically(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setMirrorVertically

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QRhiWidget::setMirrorVertically(bool enabled)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget19setMirrorVerticallyEb', enabled,
    )

  @overload(bool)
  def setAutoRenderTarget(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QRhiWidget::setAutoRenderTarget(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#setAutoRenderTarget

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QRhiWidget::setAutoRenderTarget(bool enabled)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget19setAutoRenderTargetEb', enabled,
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
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QRhiWidget::QRhiWidget(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#QRhiWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QRhiWidget::QRhiWidget(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QRhiWidget, lambda: Rituals.call(
        'ritual_ZN10QRhiWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  def d_func(self) -> Optional[QRhiWidgetPrivate]:
    """
    Calls Qt's 'QRhiWidgetPrivate *QRhiWidget::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#d_func

    Returns
    -------

    Optional[QRhiWidgetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiWidgetPrivate *QRhiWidget::d_func()
    address = self.uglySide.call('ritual_ZN10QRhiWidget6d_funcEv')
    from . import QRhiWidgetPrivate
    return QRhiWidgetPrivate._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def initialize(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiWidget::initialize(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#initialize

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiWidget::initialize(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def render(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiWidget::render(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#render

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiWidget::render(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN10QRhiWidget6renderEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget6renderEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QRhiWidget::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#releaseResources
    """
    #  void QRhiWidget::releaseResources()
    ritual = 'ritual_ZN10QRhiWidget16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QRhiWidget::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiWidget::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN10QRhiWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QRhiWidget::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiWidget::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN10QRhiWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QRhiWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiWidget::event(QEvent *e)
    ritual = 'ritual_ZN10QRhiWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def frameSubmitted(self) -> None:
    """
    Calls Qt's 'void QRhiWidget::frameSubmitted()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#frameSubmitted
    """
    #  void QRhiWidget::frameSubmitted()
    self.uglySide.call('ritual_ZN10QRhiWidget14frameSubmittedEv')

  def renderFailed(self) -> None:
    """
    Calls Qt's 'void QRhiWidget::renderFailed()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#renderFailed
    """
    #  void QRhiWidget::renderFailed()
    self.uglySide.call('ritual_ZN10QRhiWidget12renderFailedEv')

  @overload(int)
  def sampleCountChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void QRhiWidget::sampleCountChanged(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#sampleCountChanged

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QRhiWidget::sampleCountChanged(int samples)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget18sampleCountChangedEi', samples,
    )

  @overload(TextureFormat)
  def colorBufferFormatChanged(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void QRhiWidget::colorBufferFormatChanged(TextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#colorBufferFormatChanged

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void QRhiWidget::colorBufferFormatChanged(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget24colorBufferFormatChangedENS_13TextureFormat'
        'E',
        format.value,
    )

  @overload(QSize)
  def fixedColorBufferSizeChanged(self, pixelSize: QSize) -> None:
    """
    Calls Qt's 'void QRhiWidget::fixedColorBufferSizeChanged(const QSize
    &pixelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#fixedColorBufferSizeChanged

    Parameters
    ----------

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiWidget::fixedColorBufferSizeChanged(const QSize &pixelSize)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget27fixedColorBufferSizeChangedERK5QSize',
        self._valueOf(pixelSize),
    )

  @overload(bool)
  def mirrorVerticallyChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QRhiWidget::mirrorVerticallyChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidget.html#mirrorVerticallyChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QRhiWidget::mirrorVerticallyChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN10QRhiWidget23mirrorVerticallyChangedEb', enabled,
    )
