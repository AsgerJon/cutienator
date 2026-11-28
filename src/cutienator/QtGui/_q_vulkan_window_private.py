"""
QVulkanWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qvulkanwindow_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVulkanWindowPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from . import QWindowPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QVulkanWindow


class QVulkanWindowPrivate(QWindowPrivate):
  """
  The cute side of Qt's QVulkanWindowPrivate: a plain Python object standing
  in front of one C++ QVulkanWindowPrivate.

  It is built on the cute 'QWindowPrivate', as Qt's QVulkanWindowPrivate is
  built on Qt's QWindowPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVulkanWindowPrivate that has a ritual and that
  Python can call so far, 15 names in all: 'q_func', 'ensureStarted', 'init',
  'reset', 'createDefaultRenderPass', 'surfacePixelSize',
  'recreateSwapChain', 'createSwapChainResources',
  'destroySwapChainResources', 'releaseSwapChain', 'beginFrame', 'endFrame',
  'addReadback', 'releaseReadbackResources', 'finishBlockingReadback'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QVulkanWindow *QVulkanWindowPrivate::q_func() const': takes
    in Python what 'QVulkanWindow *QVulkanWindowPrivate::q_func()' takes.
  - Qt's 'QVulkanWindowPrivate::~QVulkanWindowPrivate()': the destructor:
    Python never removes a C++ QVulkanWindowPrivate.
  - Qt's 'uint32_t QVulkanWindowPrivate::chooseTransientImageMemType(VkImage
    img, uint32_t startIndex)': names 'struct VkImage_T', which has no cute
    class yet.
  - Qt's 'bool QVulkanWindowPrivate::createTransientImage(VkFormat format,
    VkImageUsageFlags usage, VkImageAspectFlags aspectMask, VkImage *images,
    VkDeviceMemory *mem, VkImageView *views, int count)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QVulkanWindowPrivate::checkDeviceLost(VkResult err)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QVulkanWindowPrivate is created at the first use, not by
    'QVulkanWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVulkanWindowPrivate.
  - Each name of Qt's QVulkanWindowPrivate that has no cute function yet,
    'checkDeviceLost', 'chooseTransientImageMemType', 'createTransientImage',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QVulkanWindowPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QVulkanWindowPrivate::Status' of Qt, with the 5 names Qt gives
    in it.
    """

    StatusUninitialized = Kee[int](0)
    StatusFail = Kee[int](1)
    StatusFailRetry = Kee[int](2)
    StatusDeviceReady = Kee[int](3)
    StatusReady = Kee[int](4)

  #  The classes Qt writes inside QVulkanWindowPrivate, each a class in here
  #  as in C++.

  class FrameResources(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVulkanWindowPrivate::FrameResources: a plain
    Python object standing in front of one C++
    QVulkanWindowPrivate::FrameResources.

    C++ hands a QVulkanWindowPrivate::FrameResources around as a copy, so
    every C++ QVulkanWindowPrivate::FrameResources behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QVulkanWindowPrivate::FrameResources yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVulkanWindowPrivate::FrameResources::~FrameResources()': the
      destructor: Python removes its C++ QVulkanWindowPrivate::FrameResources
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QVulkanWindowPrivate::FrameResources is created at the first
      use, not by 'QVulkanWindowPrivate::FrameResources(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVulkanWindowPrivate::FrameResources back gives a
      copy the ritual made for Python, in a new cute
      QVulkanWindowPrivate::FrameResources.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVulkanWindowPrivate::FrameResources'

    #  Qt's '~QVulkanWindowPrivate::FrameResources()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QVulkanWindowPrivate::FrameResources behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN20QVulkanWindowPrivate14FrameResourcesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class ImageResources(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVulkanWindowPrivate::ImageResources: a plain
    Python object standing in front of one C++
    QVulkanWindowPrivate::ImageResources.

    C++ hands a QVulkanWindowPrivate::ImageResources around as a copy, so
    every C++ QVulkanWindowPrivate::ImageResources behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QVulkanWindowPrivate::ImageResources yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVulkanWindowPrivate::ImageResources::~ImageResources()': the
      destructor: Python removes its C++ QVulkanWindowPrivate::ImageResources
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QVulkanWindowPrivate::ImageResources is created at the first
      use, not by 'QVulkanWindowPrivate::ImageResources(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVulkanWindowPrivate::ImageResources back gives a
      copy the ritual made for Python, in a new cute
      QVulkanWindowPrivate::ImageResources.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVulkanWindowPrivate::ImageResources'

    #  Qt's '~QVulkanWindowPrivate::ImageResources()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QVulkanWindowPrivate::ImageResources behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN20QVulkanWindowPrivate14ImageResourcesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVulkanWindowPrivate'

  #  A C++ QVulkanWindowPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVulkanWindowPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVulkanWindowPrivate::surfacePixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVulkanWindowPrivate::surfacePixelSize() const
    address = self.uglySide.call(
        'ritual_ZNK20QVulkanWindowPrivate16surfacePixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def q_func(self) -> Optional[QVulkanWindow]:
    """
    Calls Qt's 'QVulkanWindow *QVulkanWindowPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindowprivate.html#q_func

    Returns
    -------

    Optional[QVulkanWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVulkanWindow *QVulkanWindowPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QVulkanWindowPrivate6q_funcEv')
    from . import QVulkanWindow
    return QVulkanWindow._cuteAt(address)

  def ensureStarted(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::ensureStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#ensureStarted
    """
    #  void QVulkanWindowPrivate::ensureStarted()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate13ensureStartedEv')

  def init(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindowprivate.html#init
    """
    #  void QVulkanWindowPrivate::init()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate4initEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindowprivate.html#reset
    """
    #  void QVulkanWindowPrivate::reset()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate5resetEv')

  def createDefaultRenderPass(self) -> bool:
    """
    Calls Qt's 'bool QVulkanWindowPrivate::createDefaultRenderPass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#createDefaultRenderPass
    """
    #  bool QVulkanWindowPrivate::createDefaultRenderPass()
    return self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate23createDefaultRenderPassEv',
    )

  def recreateSwapChain(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::recreateSwapChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#recreateSwapChain
    """
    #  void QVulkanWindowPrivate::recreateSwapChain()
    self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate17recreateSwapChainEv',
    )

  def createSwapChainResources(self) -> bool:
    """
    Calls Qt's 'bool QVulkanWindowPrivate::createSwapChainResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#createSwapChainResources
    """
    #  bool QVulkanWindowPrivate::createSwapChainResources()
    return self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate24createSwapChainResourcesEv',
    )

  def destroySwapChainResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::destroySwapChainResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html
    """
    #  void QVulkanWindowPrivate::destroySwapChainResources()
    self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate25destroySwapChainResourcesEv',
    )

  def releaseSwapChain(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::releaseSwapChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#releaseSwapChain
    """
    #  void QVulkanWindowPrivate::releaseSwapChain()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate16releaseSwapChainEv')

  def beginFrame(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::beginFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#beginFrame
    """
    #  void QVulkanWindowPrivate::beginFrame()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate10beginFrameEv')

  def endFrame(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::endFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkanwindowprivate.html#endFrame
    """
    #  void QVulkanWindowPrivate::endFrame()
    self.uglySide.call('ritual_ZN20QVulkanWindowPrivate8endFrameEv')

  def addReadback(self) -> bool:
    """
    Calls Qt's 'bool QVulkanWindowPrivate::addReadback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#addReadback
    """
    #  bool QVulkanWindowPrivate::addReadback()
    return self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate11addReadbackEv',
    )

  def releaseReadbackResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::releaseReadbackResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#releaseReadbackResources
    """
    #  void QVulkanWindowPrivate::releaseReadbackResources()
    self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate24releaseReadbackResourcesEv',
    )

  def finishBlockingReadback(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowPrivate::finishBlockingReadback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowprivate.html#finishBlockingReadback
    """
    #  void QVulkanWindowPrivate::finishBlockingReadback()
    self.uglySide.call(
        'ritual_ZN20QVulkanWindowPrivate22finishBlockingReadbackEv',
    )

  @staticmethod
  def checkDeviceLost(*__, **_) -> Never:
    """
    Qt's 'bool QVulkanWindowPrivate::checkDeviceLost(VkResult err)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanWindowPrivate.checkDeviceLost' has no cute function yet. "
        "Qt's 'bool QVulkanWindowPrivate::checkDeviceLost(VkResult err)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def chooseTransientImageMemType(*__, **_) -> Never:
    """
    Qt's 'uint32_t QVulkanWindowPrivate::chooseTransientImageMemType(VkImage
    img, uint32_t startIndex)': names 'struct VkImage_T', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QVulkanWindowPrivate.chooseTransientImageMemType' has no cute "
        "function yet. Qt's 'uint32_t "
        "QVulkanWindowPrivate::chooseTransientImageMemType(VkImage img, "
        "uint32_t startIndex)': names 'struct VkImage_T', which has no cute "
        "class yet.")

  @staticmethod
  def createTransientImage(*__, **_) -> Never:
    """
    Qt's 'bool QVulkanWindowPrivate::createTransientImage(VkFormat format,
    VkImageUsageFlags usage, VkImageAspectFlags aspectMask, VkImage *images,
    VkDeviceMemory *mem, VkImageView *views, int count)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanWindowPrivate.createTransientImage' has no cute function "
        "yet. Qt's 'bool "
        "QVulkanWindowPrivate::createTransientImage(VkFormat format, "
        "VkImageUsageFlags usage, VkImageAspectFlags aspectMask, VkImage "
        "*images, VkDeviceMemory *mem, VkImageView *views, int count)': "
        "takes a type Python has no way to hand over yet.")
