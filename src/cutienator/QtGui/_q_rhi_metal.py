"""
QRhiMetal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiMetal to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList
from . import QRhi, QRhiBuffer, QRhiCommandBuffer, QRhiImplementation
from . import QRhiRenderBuffer, QRhiSampler, QRhiTexture
from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize
  from . import QColor, QMatrix4x4, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiNativeHandles, QRhiRenderTarget
  from . import QRhiResourceUpdateBatch, QRhiScissor
  from . import QRhiShaderResourceBindings, QRhiShadingRateMap, QRhiStats
  from . import QRhiSwapChain, QRhiTextureRenderTargetDescription
  from . import QRhiViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QRhiComputePipeline = WAIT['QRhiComputePipeline']
  QRhiDepthStencilClearValue = WAIT['QRhiDepthStencilClearValue']
  QRhiGraphicsPipeline = WAIT['QRhiGraphicsPipeline']
  QRhiNativeHandles = WAIT['QRhiNativeHandles']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiMetal(QRhiImplementation):
  """
  The cute side of Qt's QRhiMetal: a plain Python object standing in front of
  one C++ QRhiMetal.

  It is built on the cute 'QRhiImplementation', as Qt's QRhiMetal is built on
  Qt's QRhiImplementation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiMetal that has a ritual and that Python can call
  so far, 56 names in all: 'create', 'destroy', 'createGraphicsPipeline',
  'createComputePipeline', 'createShaderResourceBindings', 'createBuffer',
  'createRenderBuffer', 'createTexture', 'createSampler',
  'createTextureRenderTarget', 'createShadingRateMap', 'createSwapChain',
  'endFrame', 'endOffscreenFrame', 'finish', 'resourceUpdate', 'beginPass',
  'endPass', 'setGraphicsPipeline', 'setViewport', 'setScissor',
  'setBlendConstants', 'setStencilRef', 'setShadingRate', 'draw',
  'drawIndexed', 'drawIndirect', 'drawIndexedIndirect', 'debugMarkBegin',
  'debugMarkEnd', 'debugMarkMsg', 'beginComputePass', 'endComputePass',
  'setComputePipeline', 'dispatch', 'nativeHandles', 'beginExternal',
  'endExternal', 'lastCompletedGpuTime', 'supportedShadingRates',
  'ubufAlignment', 'isYUpInFramebuffer', 'isYUpInNDC',
  'isClipDepthZeroToOne', 'clipSpaceCorrMatrix', 'isTextureFormatSupported',
  'isFeatureSupported', 'resourceLimit', 'driverInfo', 'statistics',
  'makeThreadLocalNativeContextCurrent', 'setQueueSubmitParams',
  'releaseCachedResources', 'isDeviceLost', 'pipelineCacheData',
  'setPipelineCacheData'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhi::FrameOpResult QRhiMetal::beginFrame(QRhiSwapChain *swapChain,
    QRhi::BeginFrameFlags flags)': names the enum 'QRhi::BeginFrameFlag',
    whose class cannot be named here.
  - Qt's 'QRhi::FrameOpResult
    QRhiMetal::beginOffscreenFrame(QRhiCommandBuffer **cb,
    QRhi::BeginFrameFlags flags)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRhiMetal::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiMetal::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
  - Qt's 'QList<int> QRhiMetal::supportedSampleCounts() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  17 of the 79 functions Qt declares: 17 cannot be called and cannot be
  called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QRhiMetal is created at the first use, not by 'QRhiMetal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiMetal.
  - Each name of Qt's QRhiMetal that has no cute function yet, '__init__',
    'adjustForMultiViewDraw', 'enqueueResourceUpdates',
    'enqueueShaderResourceBindings', 'enqueueSubresUpload',
    'executeBufferHostWritesForCurrentFrame',
    'executeBufferHostWritesForSlot', 'executeDeferredReleases',
    'finalizeDeferredStoreActions', 'finishActiveReadbacks',
    'interruptRenderPass', 'probe', 'setDefaultScissor',
    'subresUploadByteSize', 'tessellatedDraw', 'updateSwapChainProxyData',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QRhiMetal, each a class in here as in C++.

  class TessDrawArgs(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiMetal::TessDrawArgs: a plain Python object
    standing in front of one C++ QRhiMetal::TessDrawArgs.

    C++ hands a QRhiMetal::TessDrawArgs around as a copy, so every C++
    QRhiMetal::TessDrawArgs behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiMetal::TessDrawArgs yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiMetal::TessDrawArgs::~TessDrawArgs()': the destructor: Python
      removes its C++ QRhiMetal::TessDrawArgs by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QRhiMetal::TessDrawArgs is created at the first use, not by
      'QRhiMetal::TessDrawArgs(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiMetal::TessDrawArgs back gives a copy the
      ritual made for Python, in a new cute QRhiMetal::TessDrawArgs.
    """

    #  The classes Qt writes inside QRhiMetal::TessDrawArgs, each a class in
    #  here as in C++.

    class IndexedArgs(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QRhiMetal::TessDrawArgs::IndexedArgs: a plain
      Python object standing in front of one C++
      QRhiMetal::TessDrawArgs::IndexedArgs.

      C++ hands a QRhiMetal::TessDrawArgs::IndexedArgs around as a copy, so
      every C++ QRhiMetal::TessDrawArgs::IndexedArgs behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiMetal::TessDrawArgs::IndexedArgs yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiMetal::TessDrawArgs::IndexedArgs::~IndexedArgs()': the
        destructor: Python removes its C++
        QRhiMetal::TessDrawArgs::IndexedArgs by it, and has no other use for
        it.

      What to expect
      --------------

      - The C++ QRhiMetal::TessDrawArgs::IndexedArgs is created at the first
        use, not by 'QRhiMetal::TessDrawArgs::IndexedArgs(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiMetal::TessDrawArgs::IndexedArgs back gives a
        copy the ritual made for Python, in a new cute
        QRhiMetal::TessDrawArgs::IndexedArgs.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiMetal::TessDrawArgs::IndexedArgs'

      #  Qt's '~QRhiMetal::TessDrawArgs::IndexedArgs()'. Naming it makes this
      #  a value class: Python owns every C++
      #  QRhiMetal::TessDrawArgs::IndexedArgs behind a cute one, and removes
      #  it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN9QRhiMetal12TessDrawArgs11IndexedArgsD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class NonIndexedArgs(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QRhiMetal::TessDrawArgs::NonIndexedArgs: a plain
      Python object standing in front of one C++
      QRhiMetal::TessDrawArgs::NonIndexedArgs.

      C++ hands a QRhiMetal::TessDrawArgs::NonIndexedArgs around as a copy,
      so every C++ QRhiMetal::TessDrawArgs::NonIndexedArgs behind a cute one
      is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiMetal::TessDrawArgs::NonIndexedArgs yet. None
      can be made from Python: one comes out of a function of another class
      that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiMetal::TessDrawArgs::NonIndexedArgs::~NonIndexedArgs()':
        the destructor: Python removes its C++
        QRhiMetal::TessDrawArgs::NonIndexedArgs by it, and has no other use
        for it.

      What to expect
      --------------

      - The C++ QRhiMetal::TessDrawArgs::NonIndexedArgs is created at the
        first use, not by 'QRhiMetal::TessDrawArgs::NonIndexedArgs(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiMetal::TessDrawArgs::NonIndexedArgs back
        gives a copy the ritual made for Python, in a new cute
        QRhiMetal::TessDrawArgs::NonIndexedArgs.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiMetal::TessDrawArgs::NonIndexedArgs'

      #  Qt's '~QRhiMetal::TessDrawArgs::NonIndexedArgs()'. Naming it makes
      #  this a value class: Python owns every C++
      #  QRhiMetal::TessDrawArgs::NonIndexedArgs behind a cute one, and
      #  removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN9QRhiMetal12TessDrawArgs14NonIndexedArgsD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiMetal::TessDrawArgs'

    #  Qt's '~QRhiMetal::TessDrawArgs()'. Naming it makes this a value class:
    #  Python owns every C++ QRhiMetal::TessDrawArgs behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QRhiMetal12TessDrawArgsD1Ev'

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
  __qt_class__ = 'QRhiMetal'

  #  A C++ QRhiMetal Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiMetal'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def supportedShadingRates(self, sampleCount: int) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QRhiMetal::supportedShadingRates(int
    sampleCount) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhiMetal::supportedShadingRates(int sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK9QRhiMetal21supportedShadingRatesEi', sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhiMetal::ubufAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#ubufAlignment
    """
    #  int QRhiMetal::ubufAlignment() const
    return self.uglySide.call('ritual_ZNK9QRhiMetal13ubufAlignmentEv')

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isYUpInFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#isYUpInFramebuffer
    """
    #  bool QRhiMetal::isYUpInFramebuffer() const
    return self.uglySide.call('ritual_ZNK9QRhiMetal18isYUpInFramebufferEv')

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#isYUpInNDC
    """
    #  bool QRhiMetal::isYUpInNDC() const
    return self.uglySide.call('ritual_ZNK9QRhiMetal10isYUpInNDCEv')

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isClipDepthZeroToOne() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#isClipDepthZeroToOne
    """
    #  bool QRhiMetal::isClipDepthZeroToOne() const
    return self.uglySide.call('ritual_ZNK9QRhiMetal20isClipDepthZeroToOneEv')

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhiMetal::clipSpaceCorrMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhiMetal::clipSpaceCorrMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK9QRhiMetal19clipSpaceCorrMatrixEv',
    )
    from . import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QRhiTexture.Format, QRhiTexture.Flags)
  def isTextureFormatSupported(
      self,
      format: QRhiTexture.Format,
      flags: QRhiTexture.Flags,
  ) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isTextureFormatSupported(QRhiTexture::Format
    format, QRhiTexture::Flags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  bool QRhiMetal::isTextureFormatSupported(QRhiTexture::Format format,
    #      QRhiTexture::Flags flags) const
    return self.uglySide.call(
        'ritual_ZNK9QRhiMetal24isTextureFormatSupportedEN11QRhiTexture6Form'
        'atE6QFlagsINS0_4FlagEE',
        format.value, flags.value,
    )

  @overload(QRhi.Feature)
  def isFeatureSupported(self, feature: QRhi.Feature) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isFeatureSupported(QRhi::Feature feature)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#isFeatureSupported

    Parameters
    ----------

    feature : QRhi.Feature
      Passed on as its number.
    """
    #  bool QRhiMetal::isFeatureSupported(QRhi::Feature feature) const
    return self.uglySide.call(
        'ritual_ZNK9QRhiMetal18isFeatureSupportedEN4QRhi7FeatureE',
        feature.value,
    )

  @overload(QRhi.ResourceLimit)
  def resourceLimit(self, limit: QRhi.ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhiMetal::resourceLimit(QRhi::ResourceLimit limit)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#resourceLimit

    Parameters
    ----------

    limit : QRhi.ResourceLimit
      Passed on as its number.
    """
    #  int QRhiMetal::resourceLimit(QRhi::ResourceLimit limit) const
    return self.uglySide.call(
        'ritual_ZNK9QRhiMetal13resourceLimitEN4QRhi13ResourceLimitE',
        limit.value,
    )

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhiMetal::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhiMetal::driverInfo() const
    address = self.uglySide.call('ritual_ZNK9QRhiMetal10driverInfoEv')
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::isDeviceLost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#isDeviceLost
    """
    #  bool QRhiMetal::isDeviceLost() const
    return self.uglySide.call('ritual_ZNK9QRhiMetal12isDeviceLostEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiCommandBuffer, QRhiGraphicsPipeline)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiGraphicsPipeline)
  @overload(NoneType, NoneType)
  def setGraphicsPipeline(
      self,
      cb: Optional[QRhiCommandBuffer],
      ps: Optional[QRhiGraphicsPipeline],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setGraphicsPipeline(QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::setGraphicsPipeline(QRhiCommandBuffer *cb,
    #      QRhiGraphicsPipeline *ps)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal19setGraphicsPipelineEP17QRhiCommandBufferP20QR'
        'hiGraphicsPipeline',
        self._addressOf(cb), self._addressOf(ps),
    )

  @overload(QRhiCommandBuffer, QRhiViewport)
  @overload(NoneType, QRhiViewport)
  def setViewport(
      self,
      cb: Optional[QRhiCommandBuffer],
      viewport: QRhiViewport,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setViewport(QRhiCommandBuffer *cb, const
    QRhiViewport &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setViewport

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiMetal::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
    #      &viewport)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal11setViewportEP17QRhiCommandBufferRK12QRhiViewp'
        'ort',
        self._addressOf(cb), self._valueOf(viewport),
    )

  @overload(QRhiCommandBuffer, QRhiScissor)
  @overload(NoneType, QRhiScissor)
  def setScissor(
      self,
      cb: Optional[QRhiCommandBuffer],
      scissor: QRhiScissor,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setScissor(QRhiCommandBuffer *cb, const
    QRhiScissor &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setScissor

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiMetal::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
    #      &scissor)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal10setScissorEP17QRhiCommandBufferRK11QRhiScisso'
        'r',
        self._addressOf(cb), self._valueOf(scissor),
    )

  @overload(QRhiCommandBuffer, QColor)
  @overload(NoneType, QColor)
  def setBlendConstants(
      self,
      cb: Optional[QRhiCommandBuffer],
      c: QColor,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setBlendConstants(QRhiCommandBuffer *cb,
    const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setBlendConstants

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiMetal::setBlendConstants(QRhiCommandBuffer *cb, const QColor
    #      &c)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal17setBlendConstantsEP17QRhiCommandBufferRK6QCol'
        'or',
        self._addressOf(cb), self._valueOf(c),
    )

  @overload(QRhiCommandBuffer, int)
  @overload(NoneType, int)
  def setStencilRef(
      self,
      cb: Optional[QRhiCommandBuffer],
      refValue: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setStencilRef(QRhiCommandBuffer *cb, quint32
    refValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setStencilRef

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refValue : int
      Passed on as it is.
    """
    #  void QRhiMetal::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal13setStencilRefEP17QRhiCommandBufferj',
        self._addressOf(cb), refValue,
    )

  @overload(QRhiCommandBuffer, QSize)
  @overload(NoneType, QSize)
  def setShadingRate(
      self,
      cb: Optional[QRhiCommandBuffer],
      coarsePixelSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setShadingRate(QRhiCommandBuffer *cb, const
    QSize &coarsePixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setShadingRate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiMetal::setShadingRate(QRhiCommandBuffer *cb, const QSize
    #      &coarsePixelSize)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal14setShadingRateEP17QRhiCommandBufferRK5QSize',
        self._addressOf(cb), self._valueOf(coarsePixelSize),
    )

  @overload(QRhiCommandBuffer, QRhiComputePipeline)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiComputePipeline)
  @overload(NoneType, NoneType)
  def setComputePipeline(
      self,
      cb: Optional[QRhiCommandBuffer],
      ps: Optional[QRhiComputePipeline],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setComputePipeline(QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#setComputePipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::setComputePipeline(QRhiCommandBuffer *cb,
    #      QRhiComputePipeline *ps)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal18setComputePipelineEP17QRhiCommandBufferP19QRh'
        'iComputePipeline',
        self._addressOf(cb), self._addressOf(ps),
    )

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::setQueueSubmitParams(QRhiNativeHandles
    *params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::setQueueSubmitParams(QRhiNativeHandles *params)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal20setQueueSubmitParamsEP17QRhiNativeHandles',
        self._addressOf(params),
    )

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiMetal::setPipelineCacheData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiMetal::setPipelineCacheData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal20setPipelineCacheDataERK10QByteArray',
        self._valueOf(data),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QRhiMetal::QRhiMetal(QRhiMetalInitParams *params,
    QRhiMetalNativeHandles *importDevice)': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.__init__' has no cute function yet. Qt's "
        "'QRhiMetal::QRhiMetal(QRhiMetalInitParams *params, "
        "QRhiMetalNativeHandles *importDevice)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

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

  @overload(QRhi.Flags)
  def create(self, flags: QRhi.Flags) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::create(QRhi::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#create

    Parameters
    ----------

    flags : QRhi.Flags
      Passed on as its number.
    """
    #  bool QRhiMetal::create(QRhi::Flags flags)
    return self.uglySide.call(
        'ritual_ZN9QRhiMetal6createE6QFlagsIN4QRhi4FlagEE', flags.value,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QRhiMetal::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#destroy
    """
    #  void QRhiMetal::destroy()
    self.uglySide.call('ritual_ZN9QRhiMetal7destroyEv')

  def createGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QRhiMetal::createGraphicsPipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#createGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhiMetal::createGraphicsPipeline()
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal22createGraphicsPipelineEv',
    )
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def createComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline *QRhiMetal::createComputePipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#createComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhiMetal::createComputePipeline()
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal21createComputePipelineEv',
    )
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def createShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiMetal::createShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#createShaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QRhiMetal::createShaderResourceBindings()
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal28createShaderResourceBindingsEv',
    )
    from . import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  @overload(QRhiBuffer.Type, QRhiBuffer.UsageFlags, int)
  def createBuffer(
      self,
      type: QRhiBuffer.Type,
      usage: QRhiBuffer.UsageFlags,
      size: int,
  ) -> Optional[QRhiBuffer]:
    """
    Calls Qt's 'QRhiBuffer *QRhiMetal::createBuffer(QRhiBuffer::Type type,
    QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#createBuffer

    Parameters
    ----------

    type : QRhiBuffer.Type
      Passed on as its number.

    usage : QRhiBuffer.UsageFlags
      Passed on as its number.

    size : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiBuffer *QRhiMetal::createBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9'
        'UsageFlagEEj',
        type.value, usage.value, size,
    )
    return QRhiBuffer._cuteAt(address)

  @overload(
      QRhiRenderBuffer.Type, QSize, int, QRhiRenderBuffer.Flags,
      QRhiTexture.Format,
  )
  def createRenderBuffer(
      self,
      type: QRhiRenderBuffer.Type,
      pixelSize: QSize,
      sampleCount: int,
      flags: QRhiRenderBuffer.Flags,
      backingFormatHint: QRhiTexture.Format,
  ) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer
    *QRhiMetal::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize
    &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#createRenderBuffer

    Parameters
    ----------

    type : QRhiRenderBuffer.Type
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is.

    flags : QRhiRenderBuffer.Flags
      Passed on as its number.

    backingFormatHint : QRhiTexture.Format
      Passed on as its number.

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiMetal::createRenderBuffer(QRhiRenderBuffer::Type
    #      type, const QSize &pixelSize, int sampleCount,
    #      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
    #      backingFormatHint)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal18createRenderBufferEN16QRhiRenderBuffer4TypeER'
        'K5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
        type.value, self._valueOf(pixelSize), sampleCount, flags.value,
        backingFormatHint.value,
    )
    return QRhiRenderBuffer._cuteAt(address)

  @overload(QRhiTexture.Format, QSize, int, int, int, QRhiTexture.Flags)
  def createTexture(
      self,
      format: QRhiTexture.Format,
      pixelSize: QSize,
      depth: int,
      arraySize: int,
      sampleCount: int,
      flags: QRhiTexture.Flags,
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiMetal::createTexture(QRhiTexture::Format
    format, const QSize &pixelSize, int depth, int arraySize, int
    sampleCount, QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#createTexture

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    depth : int
      Passed on as it is.

    arraySize : int
      Passed on as it is.

    sampleCount : int
      Passed on as it is.

    flags : QRhiTexture.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiMetal::createTexture(QRhiTexture::Format format,
    #      const QSize &pixelSize, int depth, int arraySize, int sampleCount,
    #      QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal13createTextureEN11QRhiTexture6FormatERK5QSizei'
        'ii6QFlagsINS0_4FlagEE',
        format.value, self._valueOf(pixelSize), depth, arraySize,
        sampleCount, flags.value,
    )
    return QRhiTexture._cuteAt(address)

  @overload(
      QRhiSampler.Filter, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.AddressMode, QRhiSampler.AddressMode,
      QRhiSampler.AddressMode,
  )
  def createSampler(
      self,
      magFilter: QRhiSampler.Filter,
      minFilter: QRhiSampler.Filter,
      mipmapMode: QRhiSampler.Filter,
      u: QRhiSampler.AddressMode,
      v: QRhiSampler.AddressMode,
      w: QRhiSampler.AddressMode,
  ) -> Optional[QRhiSampler]:
    """
    Calls Qt's 'QRhiSampler *QRhiMetal::createSampler(QRhiSampler::Filter
    magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#createSampler

    Parameters
    ----------

    magFilter : QRhiSampler.Filter
      Passed on as its number.

    minFilter : QRhiSampler.Filter
      Passed on as its number.

    mipmapMode : QRhiSampler.Filter
      Passed on as its number.

    u : QRhiSampler.AddressMode
      Passed on as its number.

    v : QRhiSampler.AddressMode
      Passed on as its number.

    w : QRhiSampler.AddressMode
      Passed on as its number.

    Returns
    -------

    Optional[QRhiSampler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSampler *QRhiMetal::createSampler(QRhiSampler::Filter magFilter,
    #      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    #      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    #      QRhiSampler::AddressMode w)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal13createSamplerEN11QRhiSampler6FilterES1_S1_NS0'
        '_11AddressModeES2_S2_',
        magFilter.value, minFilter.value, mipmapMode.value, u.value, v.value,
        w.value,
    )
    return QRhiSampler._cuteAt(address)

  @overload(
      QRhiTextureRenderTargetDescription, QRhiTextureRenderTarget.Flags,
  )
  def createTextureRenderTarget(
      self,
      desc: QRhiTextureRenderTargetDescription,
      flags: QRhiTextureRenderTarget.Flags,
  ) -> Optional[QRhiTextureRenderTarget]:
    """
    Calls Qt's 'QRhiTextureRenderTarget
    *QRhiMetal::createTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#createTextureRenderTarget

    Parameters
    ----------

    desc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    flags : QRhiTextureRenderTarget.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QRhiTextureRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTextureRenderTarget *QRhiMetal::createTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal25createTextureRenderTargetERK34QRhiTextureRend'
        'erTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE',
        self._valueOf(desc), flags.value,
    )
    return QRhiTextureRenderTarget._cuteAt(address)

  def createShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhiMetal::createShadingRateMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#createShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiMetal::createShadingRateMap()
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal20createShadingRateMapEv',
    )
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def createSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiMetal::createSwapChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#createSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiMetal::createSwapChain()
    address = self.uglySide.call('ritual_ZN9QRhiMetal15createSwapChainEv')
    from . import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

  @overload(QRhiSwapChain, QRhi.EndFrameFlags)
  @overload(NoneType, QRhi.EndFrameFlags)
  def endFrame(
      self,
      swapChain: Optional[QRhiSwapChain],
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiMetal::endFrame(QRhiSwapChain
    *swapChain, QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#endFrame

    Parameters
    ----------

    swapChain : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QRhi.EndFrameFlags
      Passed on as its number.

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiMetal::endFrame(QRhiSwapChain *swapChain,
    #      QRhi::EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiMetal8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFr'
        'ameFlagEE',
        self._addressOf(swapChain), flags.value,
    ))

  @overload(QRhi.EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult
    QRhiMetal::endOffscreenFrame(QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#endOffscreenFrame

    Parameters
    ----------

    flags : QRhi.EndFrameFlags
      Passed on as its number.

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiMetal::endOffscreenFrame(QRhi::EndFrameFlags
    #      flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiMetal17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFla'
        'gEE',
        flags.value,
    ))

  def finish(self) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiMetal::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#finish

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiMetal::finish()
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiMetal6finishEv',
    ))

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def resourceUpdate(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::resourceUpdate(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#resourceUpdate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::resourceUpdate(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal14resourceUpdateEP17QRhiCommandBufferP23QRhiRes'
        'ourceUpdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(
      QRhiCommandBuffer, QRhiRenderTarget, QColor,
      QRhiDepthStencilClearValue, QRhiResourceUpdateBatch,
      QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, QRhiRenderTarget, QColor,
      QRhiDepthStencilClearValue, NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, NoneType, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, NoneType, QColor, QRhiDepthStencilClearValue,
      NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, NoneType, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, NoneType, QColor, QRhiDepthStencilClearValue, NoneType,
      QRhiCommandBuffer.BeginPassFlags,
  )
  def beginPass(
      self,
      cb: Optional[QRhiCommandBuffer],
      rt: Optional[QRhiRenderTarget],
      colorClearValue: QColor,
      depthStencilClearValue: QRhiDepthStencilClearValue,
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
      flags: QRhiCommandBuffer.BeginPassFlags,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::beginPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QColor &colorClearValue, const
    QRhiDepthStencilClearValue &depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#beginPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    colorClearValue : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    depthStencilClearValue : QRhiDepthStencilClearValue
      Passed on as a value: Qt reads the C++ QRhiDepthStencilClearValue,
      which stays Python's own.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QRhiCommandBuffer.BeginPassFlags
      Passed on as its number.
    """
    #  void QRhiMetal::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
    #      const QColor &colorClearValue, const QRhiDepthStencilClearValue
    #      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal9beginPassEP17QRhiCommandBufferP16QRhiRenderTar'
        'getRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBat'
        'ch6QFlagsINS0_13BeginPassFlagEE',
        self._addressOf(cb), self._addressOf(rt),
        self._valueOf(colorClearValue),
        self._valueOf(depthStencilClearValue),
        self._addressOf(resourceUpdates), flags.value,
    )

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def endPass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::endPass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#endPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
    #      *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal7endPassEP17QRhiCommandBufferP23QRhiResourceUpd'
        'ateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(QRhiCommandBuffer, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  def draw(
      self,
      cb: Optional[QRhiCommandBuffer],
      vertexCount: int,
      instanceCount: int,
      firstVertex: int,
      firstInstance: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::draw(QRhiCommandBuffer *cb, quint32
    vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#draw

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    vertexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.

    firstVertex : int
      Passed on as it is.

    firstInstance : int
      Passed on as it is.
    """
    #  void QRhiMetal::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
    #      quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal4drawEP17QRhiCommandBufferjjjj',
        self._addressOf(cb), vertexCount, instanceCount, firstVertex,
        firstInstance,
    )

  @overload(QRhiCommandBuffer, int, int, int, int, int)
  @overload(NoneType, int, int, int, int, int)
  def drawIndexed(
      self,
      cb: Optional[QRhiCommandBuffer],
      indexCount: int,
      instanceCount: int,
      firstIndex: int,
      vertexOffset: int,
      firstInstance: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::drawIndexed(QRhiCommandBuffer *cb, quint32
    indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    vertexOffset, quint32 firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#drawIndexed

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.

    firstIndex : int
      Passed on as it is.

    vertexOffset : int
      Passed on as it is.

    firstInstance : int
      Passed on as it is.
    """
    #  void QRhiMetal::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
    #      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
    #      quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal11drawIndexedEP17QRhiCommandBufferjjjij',
        self._addressOf(cb), indexCount, instanceCount, firstIndex,
        vertexOffset, firstInstance,
    )

  @overload(QRhiCommandBuffer, QRhiBuffer, int, int, int)
  @overload(QRhiCommandBuffer, NoneType, int, int, int)
  @overload(NoneType, QRhiBuffer, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def drawIndirect(
      self,
      cb: Optional[QRhiCommandBuffer],
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::drawIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#drawIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBufferOffset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiMetal::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal12drawIndirectEP17QRhiCommandBufferP10QRhiBuffe'
        'rjjj',
        self._addressOf(cb), self._addressOf(indirectBuffer),
        indirectBufferOffset, drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QRhiBuffer, int, int, int)
  @overload(QRhiCommandBuffer, NoneType, int, int, int)
  @overload(NoneType, QRhiBuffer, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def drawIndexedIndirect(
      self,
      cb: Optional[QRhiCommandBuffer],
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::drawIndexedIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#drawIndexedIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBufferOffset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiMetal::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal19drawIndexedIndirectEP17QRhiCommandBufferP10QR'
        'hiBufferjjj',
        self._addressOf(cb), self._addressOf(indirectBuffer),
        indirectBufferOffset, drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkBegin(
      self,
      cb: Optional[QRhiCommandBuffer],
      name: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::debugMarkBegin(QRhiCommandBuffer *cb, const
    QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#debugMarkBegin

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiMetal::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
    #      &name)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal14debugMarkBeginEP17QRhiCommandBufferRK10QByteA'
        'rray',
        self._addressOf(cb), self._valueOf(name),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def debugMarkEnd(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiMetal::debugMarkEnd(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#debugMarkEnd

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::debugMarkEnd(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal12debugMarkEndEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkMsg(
      self,
      cb: Optional[QRhiCommandBuffer],
      msg: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::debugMarkMsg(QRhiCommandBuffer *cb, const
    QByteArray &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#debugMarkMsg

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiMetal::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
    #      &msg)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal12debugMarkMsgEP17QRhiCommandBufferRK10QByteArr'
        'ay',
        self._addressOf(cb), self._valueOf(msg),
    )

  @overload(
      QRhiCommandBuffer, QRhiResourceUpdateBatch,
      QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(QRhiCommandBuffer, NoneType, QRhiCommandBuffer.BeginPassFlags)
  @overload(
      NoneType, QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(NoneType, NoneType, QRhiCommandBuffer.BeginPassFlags)
  def beginComputePass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
      flags: QRhiCommandBuffer.BeginPassFlags,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::beginComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#beginComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QRhiCommandBuffer.BeginPassFlags
      Passed on as its number.
    """
    #  void QRhiMetal::beginComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal16beginComputePassEP17QRhiCommandBufferP23QRhiR'
        'esourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
        self._addressOf(cb), self._addressOf(resourceUpdates), flags.value,
    )

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def endComputePass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::endComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#endComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::endComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal14endComputePassEP17QRhiCommandBufferP23QRhiRes'
        'ourceUpdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(QRhiCommandBuffer, int, int, int)
  @overload(NoneType, int, int, int)
  def dispatch(
      self,
      cb: Optional[QRhiCommandBuffer],
      x: int,
      y: int,
      z: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiMetal::dispatch(QRhiCommandBuffer *cb, int x, int y,
    int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#dispatch

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QRhiMetal::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal8dispatchEP17QRhiCommandBufferiii',
        self._addressOf(cb), x, y, z,
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def nativeHandles(
      self,
      cb: Optional[QRhiCommandBuffer],
  ) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QRhiMetal::nativeHandles(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#nativeHandles

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiMetal::nativeHandles(QRhiCommandBuffer
    #      *cb)
    address = self.uglySide.call(
        'ritual_ZN9QRhiMetal13nativeHandlesEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload()
  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhiMetal::nativeHandles()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiMetal::nativeHandles()
    address = self.uglySide.call('ritual_ZN9QRhiMetal13nativeHandlesEv')
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def beginExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiMetal::beginExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#beginExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::beginExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal13beginExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def endExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiMetal::endExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#endExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiMetal::endExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN9QRhiMetal11endExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def lastCompletedGpuTime(self, cb: Optional[QRhiCommandBuffer]) -> float:
    """
    Calls Qt's 'double QRhiMetal::lastCompletedGpuTime(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#lastCompletedGpuTime

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QRhiMetal::lastCompletedGpuTime(QRhiCommandBuffer *cb)
    return self.uglySide.call(
        'ritual_ZN9QRhiMetal20lastCompletedGpuTimeEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhiMetal::statistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhiMetal::statistics()
    address = self.uglySide.call('ritual_ZN9QRhiMetal10statisticsEv')
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool QRhiMetal::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#makeThreadLocalNativeContextCurrent
    """
    #  bool QRhiMetal::makeThreadLocalNativeContextCurrent()
    return self.uglySide.call(
        'ritual_ZN9QRhiMetal35makeThreadLocalNativeContextCurrentEv',
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhiMetal::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhimetal.html#releaseCachedResources
    """
    #  void QRhiMetal::releaseCachedResources()
    self.uglySide.call('ritual_ZN9QRhiMetal22releaseCachedResourcesEv')

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiMetal::pipelineCacheData()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhimetal.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiMetal::pipelineCacheData()
    address = self.uglySide.call('ritual_ZN9QRhiMetal17pipelineCacheDataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def adjustForMultiViewDraw(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::adjustForMultiViewDraw(quint32 *instanceCount,
    QRhiCommandBuffer *cb)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.adjustForMultiViewDraw' has no cute function yet. Qt's "
        "'void QRhiMetal::adjustForMultiViewDraw(quint32 *instanceCount, "
        "QRhiCommandBuffer *cb)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def enqueueResourceUpdates(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::enqueueResourceUpdates(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.enqueueResourceUpdates' has no cute function yet. Qt's "
        "'void QRhiMetal::enqueueResourceUpdates(QRhiCommandBuffer *cb, "
        "QRhiResourceUpdateBatch *resourceUpdates)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def enqueueShaderResourceBindings(*__, **_) -> Never:
    """
    Qt's 'void
    QRhiMetal::enqueueShaderResourceBindings(QMetalShaderResourceBindings
    *srbD, QMetalCommandBuffer *cbD, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets, bool offsetOnlyChange,
    const QShader::NativeResourceBindingMap **nativeResourceBindingMaps)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.enqueueShaderResourceBindings' has no cute function "
        "yet. Qt's 'void "
        "QRhiMetal::enqueueShaderResourceBindings(QMetalShaderResourceBindin"
        "gs *srbD, QMetalCommandBuffer *cbD, int dynamicOffsetCount, const "
        "QRhiCommandBuffer::DynamicOffset *dynamicOffsets, bool "
        "offsetOnlyChange, const QShader::NativeResourceBindingMap "
        "**nativeResourceBindingMaps)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def enqueueSubresUpload(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::enqueueSubresUpload(QMetalTexture *texD, void *mp,
    void *blitEncPtr, int layer, int level, const
    QRhiTextureSubresourceUploadDescription &subresDesc, qsizetype *curOfs)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.enqueueSubresUpload' has no cute function yet. Qt's "
        "'void QRhiMetal::enqueueSubresUpload(QMetalTexture *texD, void "
        "*mp, void *blitEncPtr, int layer, int level, const "
        "QRhiTextureSubresourceUploadDescription &subresDesc, qsizetype "
        "*curOfs)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def executeBufferHostWritesForCurrentFrame(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::executeBufferHostWritesForCurrentFrame(QMetalBuffer
    *bufD)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.executeBufferHostWritesForCurrentFrame' has no cute "
        "function yet. Qt's 'void "
        "QRhiMetal::executeBufferHostWritesForCurrentFrame(QMetalBuffer "
        "*bufD)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def executeBufferHostWritesForSlot(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::executeBufferHostWritesForSlot(QMetalBuffer *bufD,
    int slot)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.executeBufferHostWritesForSlot' has no cute function "
        "yet. Qt's 'void "
        "QRhiMetal::executeBufferHostWritesForSlot(QMetalBuffer *bufD, int "
        "slot)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def executeDeferredReleases(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::executeDeferredReleases(bool forced)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.executeDeferredReleases' has no cute function yet. Qt's "
        "'void QRhiMetal::executeDeferredReleases(bool forced)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def finalizeDeferredStoreActions(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::finalizeDeferredStoreActions(QMetalCommandBuffer
    *cbD, bool passIsEnding)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.finalizeDeferredStoreActions' has no cute function yet. "
        "Qt's 'void "
        "QRhiMetal::finalizeDeferredStoreActions(QMetalCommandBuffer *cbD, "
        "bool passIsEnding)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def finishActiveReadbacks(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::finishActiveReadbacks(bool forced)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.finishActiveReadbacks' has no cute function yet. Qt's "
        "'void QRhiMetal::finishActiveReadbacks(bool forced)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def interruptRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::interruptRenderPass(QMetalCommandBuffer *cbD)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.interruptRenderPass' has no cute function yet. Qt's "
        "'void QRhiMetal::interruptRenderPass(QMetalCommandBuffer *cbD)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def probe(*__, **_) -> Never:
    """
    Qt's 'bool QRhiMetal::probe(QRhiMetalInitParams *params)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.probe' has no cute function yet. Qt's 'bool "
        "QRhiMetal::probe(QRhiMetalInitParams *params)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def setDefaultScissor(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::setDefaultScissor(QMetalCommandBuffer *cbD)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.setDefaultScissor' has no cute function yet. Qt's 'void "
        "QRhiMetal::setDefaultScissor(QMetalCommandBuffer *cbD)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def subresUploadByteSize(*__, **_) -> Never:
    """
    Qt's 'qsizetype QRhiMetal::subresUploadByteSize(const
    QRhiTextureSubresourceUploadDescription &subresDesc) const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.subresUploadByteSize' has no cute function yet. Qt's "
        "'qsizetype QRhiMetal::subresUploadByteSize(const "
        "QRhiTextureSubresourceUploadDescription &subresDesc) const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def tessellatedDraw(*__, **_) -> Never:
    """
    Qt's 'void QRhiMetal::tessellatedDraw(const TessDrawArgs &args)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.tessellatedDraw' has no cute function yet. Qt's 'void "
        "QRhiMetal::tessellatedDraw(const TessDrawArgs &args)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def updateSwapChainProxyData(*__, **_) -> Never:
    """
    Qt's 'QRhiSwapChainProxyData QRhiMetal::updateSwapChainProxyData(QWindow
    *window)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRhiMetal.updateSwapChainProxyData' has no cute function yet. "
        "Qt's 'QRhiSwapChainProxyData "
        "QRhiMetal::updateSwapChainProxyData(QWindow *window)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
