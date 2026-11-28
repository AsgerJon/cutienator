"""
QVkSwapChain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkSwapChain to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from . import QRhiSwapChain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QRhiCommandBuffer, QRhiRenderPassDescriptor, QRhiRenderTarget
  from . import QRhiSwapChainHdrInfo


class QVkSwapChain(QRhiSwapChain):
  """
  The cute side of Qt's QVkSwapChain: a plain Python object standing in front
  of one C++ QVkSwapChain.

  It is built on the cute 'QRhiSwapChain', as Qt's QVkSwapChain is built on
  Qt's QRhiSwapChain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVkSwapChain that has a ritual and that Python can
  call so far, 8 names in all: 'destroy', 'currentFrameCommandBuffer',
  'currentFrameRenderTarget', 'surfacePixelSize', 'isFormatSupported',
  'hdrInfo', 'newCompatibleRenderPassDescriptor', 'createOrResize'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkSwapChain::~QVkSwapChain()': the destructor: Python never
    removes a C++ QVkSwapChain.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QVkSwapChain.

  What to expect
  --------------

  - The C++ QVkSwapChain is created at the first use, not by
    'QVkSwapChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkSwapChain.
  - Each name of Qt's QVkSwapChain that has no cute function yet, '__init__',
    'ensureSurface', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QVkSwapChain, each a class in here as in
  #  C++.

  class FrameResources(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVkSwapChain::FrameResources: a plain Python object
    standing in front of one C++ QVkSwapChain::FrameResources.

    C++ hands a QVkSwapChain::FrameResources around as a copy, so every C++
    QVkSwapChain::FrameResources behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QVkSwapChain::FrameResources yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVkSwapChain::FrameResources::~FrameResources()': the destructor:
      Python removes its C++ QVkSwapChain::FrameResources by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QVkSwapChain::FrameResources is created at the first use, not
      by 'QVkSwapChain::FrameResources(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVkSwapChain::FrameResources back gives a copy the
      ritual made for Python, in a new cute QVkSwapChain::FrameResources.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVkSwapChain::FrameResources'

    #  Qt's '~QVkSwapChain::FrameResources()'. Naming it makes this a value
    #  class: Python owns every C++ QVkSwapChain::FrameResources behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QVkSwapChain14FrameResourcesD1Ev'

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
    The cute side of Qt's QVkSwapChain::ImageResources: a plain Python object
    standing in front of one C++ QVkSwapChain::ImageResources.

    C++ hands a QVkSwapChain::ImageResources around as a copy, so every C++
    QVkSwapChain::ImageResources behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QVkSwapChain::ImageResources yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVkSwapChain::ImageResources::~ImageResources()': the destructor:
      Python removes its C++ QVkSwapChain::ImageResources by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QVkSwapChain::ImageResources is created at the first use, not
      by 'QVkSwapChain::ImageResources(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVkSwapChain::ImageResources back gives a copy the
      ritual made for Python, in a new cute QVkSwapChain::ImageResources.
    """

    #  The enums Qt writes inside QVkSwapChain::ImageResources, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class LastUse(CuteNum):
      """
      The enum 'QVkSwapChain::ImageResources::LastUse' of Qt, with the 3
      names Qt gives in it.
      """

      ScImageUseNone = Kee[int](0)
      ScImageUseRender = Kee[int](1)
      ScImageUseTransferSource = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVkSwapChain::ImageResources'

    #  Qt's '~QVkSwapChain::ImageResources()'. Naming it makes this a value
    #  class: Python owns every C++ QVkSwapChain::ImageResources behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QVkSwapChain14ImageResourcesD1Ev'

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
  __qt_class__ = 'QVkSwapChain'

  #  A C++ QVkSwapChain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkSwapChain'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QVkSwapChain::QVkSwapChain(QRhiImplementation *rhi)': leans on
    'QVkSwapChain::createOrResize()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QVkSwapChain.__init__' has no cute function yet. Qt's "
        "'QVkSwapChain::QVkSwapChain(QRhiImplementation *rhi)': leans on "
        "'QVkSwapChain::createOrResize()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QVkSwapChain::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkswapchain.html#destroy
    """
    #  void QVkSwapChain::destroy()
    self.uglySide.call('ritual_ZN12QVkSwapChain7destroyEv')

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QVkSwapChain::currentFrameCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchain.html#currentFrameCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QVkSwapChain::currentFrameCommandBuffer()
    ritual = 'ritual_ZN12QVkSwapChain25currentFrameCommandBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVkSwapChain25currentFrameCommandBufferEv'
    address = self.uglySide.call(ritual)
    from . import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  @overload()
  def currentFrameRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchain.html#currentFrameRenderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()
    ritual = 'ritual_ZN12QVkSwapChain24currentFrameRenderTargetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVkSwapChain24currentFrameRenderTargetEv'
    address = self.uglySide.call(ritual)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  @overload(QRhiSwapChain.StereoTargetBuffer)
  def currentFrameRenderTarget(
      self,
      targetBuffer: QRhiSwapChain.StereoTargetBuffer,
  ) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer
    targetBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchain.html#currentFrameRenderTarget

    Parameters
    ----------

    targetBuffer : QRhiSwapChain.StereoTargetBuffer
      Passed on as its number.

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget
    #      *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer
    #      targetBuffer)
    ritual = (
        'ritual_ZN12QVkSwapChain24currentFrameRenderTargetEN13QRhiSwapChain'
        '18StereoTargetBufferE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QVkSwapChain24currentFrameRenderTargetEN13QRhiSwa'
          'pChain18StereoTargetBufferE')
    address = self.uglySide.call(ritual, targetBuffer.value)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVkSwapChain::surfacePixelSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkswapchain.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVkSwapChain::surfacePixelSize()
    address = self.uglySide.call(
        'ritual_ZN12QVkSwapChain16surfacePixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRhiSwapChain.Format)
  def isFormatSupported(self, f: QRhiSwapChain.Format) -> bool:
    """
    Calls Qt's 'bool QVkSwapChain::isFormatSupported(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchain.html#isFormatSupported

    Parameters
    ----------

    f : QRhiSwapChain.Format
      Passed on as its number.
    """
    #  bool QVkSwapChain::isFormatSupported(Format f)
    ritual = (
        'ritual_ZN12QVkSwapChain17isFormatSupportedEN13QRhiSwapChain6Format'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QVkSwapChain17isFormatSupportedEN13QRhiSwapChain6'
          'FormatE')
    return self.uglySide.call(ritual, f.value)

  def hdrInfo(self) -> QRhiSwapChainHdrInfo:
    """
    Calls Qt's 'QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkswapchain.html#hdrInfo

    Returns
    -------

    QRhiSwapChainHdrInfo
      A new cute QRhiSwapChainHdrInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()
    ritual = 'ritual_ZN12QVkSwapChain7hdrInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVkSwapChain7hdrInfoEv'
    address = self.uglySide.call(ritual)
    from . import QRhiSwapChainHdrInfo
    return QRhiSwapChainHdrInfo._cuteOwning(address)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QVkSwapChain::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchain.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QVkSwapChain::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN12QVkSwapChain33newCompatibleRenderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def createOrResize(self) -> bool:
    """
    Calls Qt's 'bool QVkSwapChain::createOrResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkswapchain.html#createOrResize
    """
    #  bool QVkSwapChain::createOrResize()
    return self.uglySide.call('ritual_ZN12QVkSwapChain14createOrResizeEv')

  @staticmethod
  def ensureSurface(*__, **_) -> Never:
    """
    Qt's 'bool QVkSwapChain::ensureSurface()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'hdrFormatMatchesVkSurfaceFormat'.
    """
    raise NotImplementedError(
        "'QVkSwapChain.ensureSurface' has no cute function yet. Qt's 'bool "
        "QVkSwapChain::ensureSurface()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'hdrFormatMatchesVkSurfaceFormat'.")
