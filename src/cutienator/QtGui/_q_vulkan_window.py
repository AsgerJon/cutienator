"""
QVulkanWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvulkanwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject, QSize
  from . import QExposeEvent, QImage, QMatrix4x4, QResizeEvent
  from . import QVulkanWindowPrivate, QVulkanWindowRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QImage = WAIT['QImage']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVulkanWindow(QWindow):
  """
  The cute side of Qt's QVulkanWindow: a plain Python object standing in
  front of one C++ QVulkanWindow.

  It is built on the cute 'QWindow', as Qt's QVulkanWindow is built on Qt's
  QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVulkanWindow that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'd_func', 'setFlags',
  'flags', 'setPhysicalDeviceIndex', 'setDeviceExtensions', 'setSampleCount',
  'isValid', 'createRenderer', 'frameReady', 'graphicsQueueFamilyIndex',
  'hostVisibleMemoryIndex', 'deviceLocalMemoryIndex', 'swapChainImageSize',
  'currentFrame', 'concurrentFrameCount', 'swapChainImageCount',
  'currentSwapChainImageIndex', 'supportsGrab', 'grab',
  'clipCorrectionMatrix', 'frameGrabbed', 'exposeEvent', 'resizeEvent',
  'event'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVulkanWindow::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QVulkanWindow::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QVulkanWindowPrivate *QVulkanWindow::d_func() const': takes
    in Python what 'QVulkanWindowPrivate *QVulkanWindow::d_func()' takes.
  - Qt's 'QVulkanWindow::~QVulkanWindow()': the destructor: Python never
    removes a C++ QVulkanWindow.
  - Qt's 'QList<VkPhysicalDeviceProperties>
    QVulkanWindow::availablePhysicalDevices()': gives a type Python has no
    way to take yet.
  - Qt's 'QVulkanInfoVector<QVulkanExtension>
    QVulkanWindow::supportedDeviceExtensions()': gives a type Python has no
    way to take yet.
  - Qt's 'void QVulkanWindow::setEnabledFeaturesModifier(const
    EnabledFeaturesModifier &modifier)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QVulkanWindow::setEnabledFeaturesModifier(EnabledFeatures2Modifier
    modifier)': takes a type Python has no way to hand over yet.
  - Qt's 'void QVulkanWindow::setPreferredColorFormats(const QList<VkFormat>
    &formats)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<int> QVulkanWindow::supportedSampleCounts()': gives a type
    Python has no way to take yet.
  - Qt's 'void QVulkanWindow::setQueueCreateInfoModifier(const
    QueueCreateInfoModifier &modifier)': takes a type Python has no way to
    hand over yet.
  - Qt's 'VkPhysicalDevice QVulkanWindow::physicalDevice() const': gives a
    type Python has no way to take yet.
  - Qt's 'const VkPhysicalDeviceProperties
    *QVulkanWindow::physicalDeviceProperties() const': gives
    'VkPhysicalDeviceProperties', which has no cute class yet.
  - Qt's 'VkDevice QVulkanWindow::device() const': gives a type Python has no
    way to take yet.
  - Qt's 'VkQueue QVulkanWindow::graphicsQueue() const': gives a type Python
    has no way to take yet.
  - Qt's 'VkCommandPool QVulkanWindow::graphicsCommandPool() const': gives a
    type Python has no way to take yet.
  - Qt's 'VkRenderPass QVulkanWindow::defaultRenderPass() const': gives a
    type Python has no way to take yet.
  - Qt's 'VkFormat QVulkanWindow::colorFormat() const': gives a type Python
    has no way to take yet.
  - Qt's 'VkFormat QVulkanWindow::depthStencilFormat() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkCommandBuffer QVulkanWindow::currentCommandBuffer() const': gives
    a type Python has no way to take yet.
  - Qt's 'VkFramebuffer QVulkanWindow::currentFramebuffer() const': gives a
    type Python has no way to take yet.
  - Qt's 'VkImage QVulkanWindow::swapChainImage(int idx) const': gives a type
    Python has no way to take yet.
  - Qt's 'VkImageView QVulkanWindow::swapChainImageView(int idx) const':
    gives a type Python has no way to take yet.
  - Qt's 'VkImage QVulkanWindow::depthStencilImage() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkImageView QVulkanWindow::depthStencilImageView() const': gives a
    type Python has no way to take yet.
  - Qt's 'VkSampleCountFlagBits QVulkanWindow::sampleCountFlagBits() const':
    gives a type Python has no way to take yet.
  - Qt's 'VkImage QVulkanWindow::msaaColorImage(int idx) const': gives a type
    Python has no way to take yet.
  - Qt's 'VkImageView QVulkanWindow::msaaColorImageView(int idx) const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 59 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QVulkanWindow is created at the first use, not by
    'QVulkanWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVulkanWindow.
  - Qt tells when it has removed the C++ QVulkanWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QVulkanWindow that has no cute function yet,
    'availablePhysicalDevices', 'colorFormat', 'currentCommandBuffer',
    'currentFramebuffer', 'defaultRenderPass', 'depthStencilFormat',
    'depthStencilImage', 'depthStencilImageView', 'device',
    'graphicsCommandPool', 'graphicsQueue', 'msaaColorImage',
    'msaaColorImageView', 'physicalDevice', 'physicalDeviceProperties',
    'sampleCountFlagBits', 'setEnabledFeaturesModifier',
    'setPreferredColorFormats', 'setQueueCreateInfoModifier',
    'supportedDeviceExtensions', 'supportedSampleCounts', 'swapChainImage',
    'swapChainImageView', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QVulkanWindow, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QVulkanWindow::Flag' of Qt, with the 1 names Qt gives in
    it. Qt names the type of its combinations 'QVulkanWindow::Flags'.
    """

    PersistentResources = 0x1

  Flags = Flag

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
    Calls Qt's 'QString QVulkanWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#tr

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
    #  QString QVulkanWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QVulkanWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVulkanWindow'

  #  A C++ QVulkanWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVulkanWindow'

  #  The functions Qt calls itself that QVulkanWindow is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createRenderer': (
          ('_ZN13QVulkanWindow14createRendererEv',
           ('address', 'address', 'QtGui:QVulkanWindowRenderer'),
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
    Calls Qt's 'const QMetaObject *QVulkanWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVulkanWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QVulkanWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QVulkanWindow::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QVulkanWindow::flags() const
    return QVulkanWindow.Flags(self.uglySide.call(
        'ritual_ZNK13QVulkanWindow5flagsEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QVulkanWindow::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#isValid
    """
    #  bool QVulkanWindow::isValid() const
    return self.uglySide.call('ritual_ZNK13QVulkanWindow7isValidEv')

  def graphicsQueueFamilyIndex(self) -> int:
    """
    Calls Qt's 'uint32_t QVulkanWindow::graphicsQueueFamilyIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#graphicsQueueFamilyIndex
    """
    #  uint32_t QVulkanWindow::graphicsQueueFamilyIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow24graphicsQueueFamilyIndexEv',
    )

  def hostVisibleMemoryIndex(self) -> int:
    """
    Calls Qt's 'uint32_t QVulkanWindow::hostVisibleMemoryIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#hostVisibleMemoryIndex
    """
    #  uint32_t QVulkanWindow::hostVisibleMemoryIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow22hostVisibleMemoryIndexEv',
    )

  def deviceLocalMemoryIndex(self) -> int:
    """
    Calls Qt's 'uint32_t QVulkanWindow::deviceLocalMemoryIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#deviceLocalMemoryIndex
    """
    #  uint32_t QVulkanWindow::deviceLocalMemoryIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow22deviceLocalMemoryIndexEv',
    )

  def swapChainImageSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVulkanWindow::swapChainImageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#swapChainImageSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVulkanWindow::swapChainImageSize() const
    address = self.uglySide.call(
        'ritual_ZNK13QVulkanWindow18swapChainImageSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QVulkanWindow::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#currentFrame
    """
    #  int QVulkanWindow::currentFrame() const
    return self.uglySide.call('ritual_ZNK13QVulkanWindow12currentFrameEv')

  def concurrentFrameCount(self) -> int:
    """
    Calls Qt's 'int QVulkanWindow::concurrentFrameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#concurrentFrameCount
    """
    #  int QVulkanWindow::concurrentFrameCount() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow20concurrentFrameCountEv',
    )

  def swapChainImageCount(self) -> int:
    """
    Calls Qt's 'int QVulkanWindow::swapChainImageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#swapChainImageCount
    """
    #  int QVulkanWindow::swapChainImageCount() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow19swapChainImageCountEv',
    )

  def currentSwapChainImageIndex(self) -> int:
    """
    Calls Qt's 'int QVulkanWindow::currentSwapChainImageIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#currentSwapChainImageIndex
    """
    #  int QVulkanWindow::currentSwapChainImageIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QVulkanWindow26currentSwapChainImageIndexEv',
    )

  def supportsGrab(self) -> bool:
    """
    Calls Qt's 'bool QVulkanWindow::supportsGrab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#supportsGrab
    """
    #  bool QVulkanWindow::supportsGrab() const
    return self.uglySide.call('ritual_ZNK13QVulkanWindow12supportsGrabEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QVulkanWindow::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QVulkanWindow::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN13QVulkanWindow8setFlagsE6QFlagsINS_4FlagEE', flags.value,
    )

  @overload(int)
  def setPhysicalDeviceIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QVulkanWindow::setPhysicalDeviceIndex(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#setPhysicalDeviceIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QVulkanWindow::setPhysicalDeviceIndex(int idx)
    self.uglySide.call(
        'ritual_ZN13QVulkanWindow22setPhysicalDeviceIndexEi', idx,
    )

  @overload(QList[QByteArray])
  def setDeviceExtensions(self, extensions: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QVulkanWindow::setDeviceExtensions(const QByteArrayList
    &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#setDeviceExtensions

    Parameters
    ----------

    extensions : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVulkanWindow::setDeviceExtensions(const QByteArrayList
    #      &extensions)
    self.uglySide.call(
        'ritual_ZN13QVulkanWindow19setDeviceExtensionsERK5QListI10QByteArra'
        'yE',
        self._valueOf(extensions),
    )

  @overload(int)
  def setSampleCount(self, sampleCount: int) -> None:
    """
    Calls Qt's 'void QVulkanWindow::setSampleCount(int sampleCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#setSampleCount

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.
    """
    #  void QVulkanWindow::setSampleCount(int sampleCount)
    self.uglySide.call(
        'ritual_ZN13QVulkanWindow14setSampleCountEi', sampleCount,
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
    Notes what was given, for Qt's 'QVulkanWindow::QVulkanWindow(QWindow
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#QVulkanWindow

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVulkanWindow::QVulkanWindow(QWindow *parent)
    self._noteCreation(QVulkanWindow, lambda: Rituals.call(
        'ritual_ZN13QVulkanWindowC1EP7QWindow', self._addressOf(parent),
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

  def d_func(self) -> Optional[QVulkanWindowPrivate]:
    """
    Calls Qt's 'QVulkanWindowPrivate *QVulkanWindow::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#d_func

    Returns
    -------

    Optional[QVulkanWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVulkanWindowPrivate *QVulkanWindow::d_func()
    address = self.uglySide.call('ritual_ZN13QVulkanWindow6d_funcEv')
    from . import QVulkanWindowPrivate
    return QVulkanWindowPrivate._cuteAt(address)

  def createRenderer(self) -> Optional[QVulkanWindowRenderer]:
    """
    Calls Qt's 'QVulkanWindowRenderer *QVulkanWindow::createRenderer()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#createRenderer

    Returns
    -------

    Optional[QVulkanWindowRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVulkanWindowRenderer *QVulkanWindow::createRenderer()
    ritual = 'ritual_ZN13QVulkanWindow14createRendererEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QVulkanWindow14createRendererEv'
    address = self.uglySide.call(ritual)
    from . import QVulkanWindowRenderer
    return QVulkanWindowRenderer._cuteAt(address)

  def frameReady(self) -> None:
    """
    Calls Qt's 'void QVulkanWindow::frameReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#frameReady
    """
    #  void QVulkanWindow::frameReady()
    self.uglySide.call('ritual_ZN13QVulkanWindow10frameReadyEv')

  def grab(self) -> QImage:
    """
    Calls Qt's 'QImage QVulkanWindow::grab()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#grab

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QVulkanWindow::grab()
    address = self.uglySide.call('ritual_ZN13QVulkanWindow4grabEv')
    from . import QImage
    return QImage._cuteOwning(address)

  def clipCorrectionMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QVulkanWindow::clipCorrectionMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindow.html#clipCorrectionMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QVulkanWindow::clipCorrectionMatrix()
    address = self.uglySide.call(
        'ritual_ZN13QVulkanWindow20clipCorrectionMatrixEv',
    )
    from . import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QImage)
  def frameGrabbed(self, image: QImage) -> None:
    """
    Calls Qt's 'void QVulkanWindow::frameGrabbed(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#frameGrabbed

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QVulkanWindow::frameGrabbed(const QImage &image)
    self.uglySide.call(
        'ritual_ZN13QVulkanWindow12frameGrabbedERK6QImage',
        self._valueOf(image),
    )

  @overload(QExposeEvent)
  @overload(NoneType)
  def exposeEvent(self, a0: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QVulkanWindow::exposeEvent(QExposeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#exposeEvent

    Parameters
    ----------

    a0 : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVulkanWindow::exposeEvent(QExposeEvent *a0)
    ritual = 'ritual_ZN13QVulkanWindow11exposeEventEP12QExposeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QVulkanWindow11exposeEventEP12QExposeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QVulkanWindow::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVulkanWindow::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN13QVulkanWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QVulkanWindow11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QVulkanWindow::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindow.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVulkanWindow::event(QEvent *a0)
    ritual = 'ritual_ZN13QVulkanWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QVulkanWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def availablePhysicalDevices(*__, **_) -> Never:
    """
    Qt's 'QList<VkPhysicalDeviceProperties>
    QVulkanWindow::availablePhysicalDevices()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.availablePhysicalDevices' has no cute function yet. "
        "Qt's 'QList<VkPhysicalDeviceProperties> "
        "QVulkanWindow::availablePhysicalDevices()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def colorFormat(*__, **_) -> Never:
    """
    Qt's 'VkFormat QVulkanWindow::colorFormat() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.colorFormat' has no cute function yet. Qt's "
        "'VkFormat QVulkanWindow::colorFormat() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def currentCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'VkCommandBuffer QVulkanWindow::currentCommandBuffer() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.currentCommandBuffer' has no cute function yet. "
        "Qt's 'VkCommandBuffer QVulkanWindow::currentCommandBuffer() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def currentFramebuffer(*__, **_) -> Never:
    """
    Qt's 'VkFramebuffer QVulkanWindow::currentFramebuffer() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.currentFramebuffer' has no cute function yet. Qt's "
        "'VkFramebuffer QVulkanWindow::currentFramebuffer() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def defaultRenderPass(*__, **_) -> Never:
    """
    Qt's 'VkRenderPass QVulkanWindow::defaultRenderPass() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.defaultRenderPass' has no cute function yet. Qt's "
        "'VkRenderPass QVulkanWindow::defaultRenderPass() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def depthStencilFormat(*__, **_) -> Never:
    """
    Qt's 'VkFormat QVulkanWindow::depthStencilFormat() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.depthStencilFormat' has no cute function yet. Qt's "
        "'VkFormat QVulkanWindow::depthStencilFormat() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def depthStencilImage(*__, **_) -> Never:
    """
    Qt's 'VkImage QVulkanWindow::depthStencilImage() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.depthStencilImage' has no cute function yet. Qt's "
        "'VkImage QVulkanWindow::depthStencilImage() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def depthStencilImageView(*__, **_) -> Never:
    """
    Qt's 'VkImageView QVulkanWindow::depthStencilImageView() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.depthStencilImageView' has no cute function yet. "
        "Qt's 'VkImageView QVulkanWindow::depthStencilImageView() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def device(*__, **_) -> Never:
    """
    Qt's 'VkDevice QVulkanWindow::device() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.device' has no cute function yet. Qt's 'VkDevice "
        "QVulkanWindow::device() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def graphicsCommandPool(*__, **_) -> Never:
    """
    Qt's 'VkCommandPool QVulkanWindow::graphicsCommandPool() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.graphicsCommandPool' has no cute function yet. Qt's "
        "'VkCommandPool QVulkanWindow::graphicsCommandPool() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def graphicsQueue(*__, **_) -> Never:
    """
    Qt's 'VkQueue QVulkanWindow::graphicsQueue() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.graphicsQueue' has no cute function yet. Qt's "
        "'VkQueue QVulkanWindow::graphicsQueue() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def msaaColorImage(*__, **_) -> Never:
    """
    Qt's 'VkImage QVulkanWindow::msaaColorImage(int idx) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.msaaColorImage' has no cute function yet. Qt's "
        "'VkImage QVulkanWindow::msaaColorImage(int idx) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def msaaColorImageView(*__, **_) -> Never:
    """
    Qt's 'VkImageView QVulkanWindow::msaaColorImageView(int idx) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.msaaColorImageView' has no cute function yet. Qt's "
        "'VkImageView QVulkanWindow::msaaColorImageView(int idx) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def physicalDevice(*__, **_) -> Never:
    """
    Qt's 'VkPhysicalDevice QVulkanWindow::physicalDevice() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.physicalDevice' has no cute function yet. Qt's "
        "'VkPhysicalDevice QVulkanWindow::physicalDevice() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def physicalDeviceProperties(*__, **_) -> Never:
    """
    Qt's 'const VkPhysicalDeviceProperties
    *QVulkanWindow::physicalDeviceProperties() const': gives
    'VkPhysicalDeviceProperties', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.physicalDeviceProperties' has no cute function yet. "
        "Qt's 'const VkPhysicalDeviceProperties "
        "*QVulkanWindow::physicalDeviceProperties() const': gives "
        "'VkPhysicalDeviceProperties', which has no cute class yet.")

  @staticmethod
  def sampleCountFlagBits(*__, **_) -> Never:
    """
    Qt's 'VkSampleCountFlagBits QVulkanWindow::sampleCountFlagBits() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.sampleCountFlagBits' has no cute function yet. Qt's "
        "'VkSampleCountFlagBits QVulkanWindow::sampleCountFlagBits() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setEnabledFeaturesModifier(*__, **_) -> Never:
    """
    - Qt's 'void QVulkanWindow::setEnabledFeaturesModifier(const
      EnabledFeaturesModifier &modifier)': takes a type Python has no way to
      hand over yet.
    - Qt's 'void
      QVulkanWindow::setEnabledFeaturesModifier(EnabledFeatures2Modifier
      modifier)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.setEnabledFeaturesModifier' has no cute function "
        "yet. Qt's 'void QVulkanWindow::setEnabledFeaturesModifier(const "
        "EnabledFeaturesModifier &modifier)': takes a type Python has no "
        "way to hand over yet. Qt's 'void "
        "QVulkanWindow::setEnabledFeaturesModifier(EnabledFeatures2Modifier "
        "modifier)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPreferredColorFormats(*__, **_) -> Never:
    """
    Qt's 'void QVulkanWindow::setPreferredColorFormats(const QList<VkFormat>
    &formats)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.setPreferredColorFormats' has no cute function yet. "
        "Qt's 'void QVulkanWindow::setPreferredColorFormats(const "
        "QList<VkFormat> &formats)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setQueueCreateInfoModifier(*__, **_) -> Never:
    """
    Qt's 'void QVulkanWindow::setQueueCreateInfoModifier(const
    QueueCreateInfoModifier &modifier)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.setQueueCreateInfoModifier' has no cute function "
        "yet. Qt's 'void QVulkanWindow::setQueueCreateInfoModifier(const "
        "QueueCreateInfoModifier &modifier)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def supportedDeviceExtensions(*__, **_) -> Never:
    """
    Qt's 'QVulkanInfoVector<QVulkanExtension>
    QVulkanWindow::supportedDeviceExtensions()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.supportedDeviceExtensions' has no cute function "
        "yet. Qt's 'QVulkanInfoVector<QVulkanExtension> "
        "QVulkanWindow::supportedDeviceExtensions()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def supportedSampleCounts(*__, **_) -> Never:
    """
    Qt's 'QList<int> QVulkanWindow::supportedSampleCounts()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.supportedSampleCounts' has no cute function yet. "
        "Qt's 'QList<int> QVulkanWindow::supportedSampleCounts()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def swapChainImage(*__, **_) -> Never:
    """
    Qt's 'VkImage QVulkanWindow::swapChainImage(int idx) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.swapChainImage' has no cute function yet. Qt's "
        "'VkImage QVulkanWindow::swapChainImage(int idx) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def swapChainImageView(*__, **_) -> Never:
    """
    Qt's 'VkImageView QVulkanWindow::swapChainImageView(int idx) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanWindow.swapChainImageView' has no cute function yet. Qt's "
        "'VkImageView QVulkanWindow::swapChainImageView(int idx) const': "
        "gives a type Python has no way to take yet.")
