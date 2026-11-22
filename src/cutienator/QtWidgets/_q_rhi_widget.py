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
  from ..QtGui import QImage, QPaintEvent, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
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
  call so far, 19 names in all: 'metaObject', 'tr', 'api', 'setApi',
  'isDebugLayerEnabled', 'setDebugLayerEnabled', 'sampleCount',
  'setSampleCount', 'colorBufferFormat', 'setColorBufferFormat',
  'fixedColorBufferSize', 'setFixedColorBufferSize',
  'isMirrorVerticallyEnabled', 'setMirrorVertically', 'grabFramebuffer',
  'releaseResources', 'resizeEvent', 'paintEvent', 'event'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiWidget::~QRhiWidget()': the destructor: Python never removes a
    C++ QRhiWidget.

  What has no ritual
  ------------------

  23 of the 45 functions Qt declares: 11 protected; 6 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 1 a template.

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

  #  The functions Qt calls itself that QRhiWidget is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'initialize': (
          'void QRhiWidget::initialize(QRhiCommandBuffer *)',
      ),
      'render': (
          'void QRhiWidget::render(QRhiCommandBuffer *)',
      ),
  }

  #  The functions Qt calls itself that QRhiWidget is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
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

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QRhiWidget::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidget.html#releaseResources
    """
    #  void QRhiWidget::releaseResources()
    self.uglySide.call('ritual_own_ZN10QRhiWidget16releaseResourcesEv')

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
    self.uglySide.call(
        'ritual_own_ZN10QRhiWidget11resizeEventEP12QResizeEvent',
        self._addressOf(e),
    )

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
    self.uglySide.call(
        'ritual_own_ZN10QRhiWidget10paintEventEP11QPaintEvent',
        self._addressOf(e),
    )

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
    return self.uglySide.call(
        'ritual_own_ZN10QRhiWidget5eventEP6QEvent', self._addressOf(e),
    )
