"""
QSGDefaultRenderContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDefaultRenderContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QShader
from . import QSGRenderContext, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage, QRawFont, QRhi, QRhiCommandBuffer
  from ..QtGui import QRhiRenderPassDescriptor, QRhiResourceUpdateBatch
  from ..QtGui import QRhiTexture
  from . import QQuickGraphicsConfiguration, QSGCompressedTextureFactory
  from . import QSGContext, QSGCurveGlyphAtlas, QSGDistanceFieldGlyphCache
  from . import QSGMaterialShader, QSGRenderer, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']
  QRawFont = WAIT['QRawFont']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiTexture = WAIT['QRhiTexture']
  QSGCompressedTextureFactory = WAIT['QSGCompressedTextureFactory']
  QSGContext = WAIT['QSGContext']
  QSGMaterialShader = WAIT['QSGMaterialShader']
  QSGRenderer = WAIT['QSGRenderer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultRenderContext(QSGRenderContext):
  """
  The cute side of Qt's QSGDefaultRenderContext: a plain Python object
  standing in front of one C++ QSGDefaultRenderContext.

  It is built on the cute 'QSGRenderContext', as Qt's QSGDefaultRenderContext
  is built on Qt's QSGRenderContext, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultRenderContext that has a ritual and that
  Python can call so far, 28 names in all: 'metaObject', 'tr', 'rhi',
  'isValid', 'initialize', 'invalidate', 'prepareSync', 'renderNextFrame',
  'endNextFrame', 'preprocess', 'invalidateGlyphCaches', 'flushGlyphCaches',
  'distanceFieldGlyphCache', 'curveGlyphAtlas', 'createTexture',
  'createRenderer', 'compressedTextureForFactory', 'initializeRhiShader',
  'maxTextureSize', 'useDepthBufferFor2D', 'msaaSampleCount',
  'currentFrameCommandBuffer', 'currentFrameRenderPass',
  'currentDevicePixelRatio', 'maybeGlyphCacheResourceUpdates',
  'glyphCacheResourceUpdates', 'deferredReleaseGlyphCacheTexture',
  'resetGlyphCacheResources'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGDefaultRenderContext::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGDefaultRenderContext::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QSGDefaultRenderContext::beginNextFrame(QSGRenderer *renderer,
    const QSGRenderTarget &renderTarget, RenderPassCallback
    mainPassRecordingStart, RenderPassCallback mainPassRecordingEnd, void
    *callbackUserData)': takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<QSGDepthStencilBuffer>
    QSGDefaultRenderContext::getDepthStencilBuffer(const QSize &size, int
    sampleCount)': gives a type Python has no way to take yet.
  - Qt's 'void QSGDefaultRenderContext::addDepthStencilBuffer(const
    QSharedPointer<QSGDepthStencilBuffer> &ds)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGDefaultRenderContext is created at the first use, not by
    'QSGDefaultRenderContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultRenderContext.
  - Qt tells when it has removed the C++ QSGDefaultRenderContext. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGDefaultRenderContext that has no cute function yet,
    'addDepthStencilBuffer', 'getDepthStencilBuffer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGDefaultRenderContext, each a class in
  #  here as in C++.

  class InitParams(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGDefaultRenderContext::InitParams: a plain Python
    object standing in front of one C++ QSGDefaultRenderContext::InitParams.

    C++ hands a QSGDefaultRenderContext::InitParams around as a copy, so
    every C++ QSGDefaultRenderContext::InitParams behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSGDefaultRenderContext::InitParams yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGDefaultRenderContext::InitParams::~InitParams()': the
      destructor: Python removes its C++ QSGDefaultRenderContext::InitParams
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGDefaultRenderContext::InitParams is created at the first
      use, not by 'QSGDefaultRenderContext::InitParams(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGDefaultRenderContext::InitParams back gives a
      copy the ritual made for Python, in a new cute
      QSGDefaultRenderContext::InitParams.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGDefaultRenderContext::InitParams'

    #  Qt's '~QSGDefaultRenderContext::InitParams()'. Naming it makes this a
    #  value class: Python owns every C++ QSGDefaultRenderContext::InitParams
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QSGDefaultRenderContext10InitParamsD1Ev'

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
    Calls Qt's 'QString QSGDefaultRenderContext::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#tr

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
    #  QString QSGDefaultRenderContext::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QSGDefaultRenderContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultRenderContext'

  #  A C++ QSGDefaultRenderContext Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultRenderContext'

  #  The functions Qt calls itself that QSGDefaultRenderContext is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeRhiShader': (
          ('_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17QSGMateria'
           'lShaderN7QShader7VariantE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGMaterialShader'),
               ('int', 'enum', 'QtGui:QShader.Variant'),
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
    Calls Qt's 'const QMetaObject *QSGDefaultRenderContext::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGDefaultRenderContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSGDefaultRenderContext::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSGDefaultRenderContext::rhi() const
    ritual = 'ritual_ZNK23QSGDefaultRenderContext3rhiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGDefaultRenderContext3rhiEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultRenderContext::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#isValid
    """
    #  bool QSGDefaultRenderContext::isValid() const
    ritual = 'ritual_ZNK23QSGDefaultRenderContext7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGDefaultRenderContext7isValidEv'
    return self.uglySide.call(ritual)

  @overload(QImage, int)
  def createTexture(self, image: QImage, flags: int) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGDefaultRenderContext::createTexture(const
    QImage &image, uint flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#createTexture

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : int
      Passed on as it is.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDefaultRenderContext::createTexture(const QImage
    #      &image, uint flags) const
    ritual = 'ritual_ZNK23QSGDefaultRenderContext13createTextureERK6QImagej'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QSGDefaultRenderContext13createTextureERK6QImage'
          'j')
    address = self.uglySide.call(ritual, self._valueOf(image), flags)
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QSGCompressedTextureFactory)
  @overload(NoneType)
  def compressedTextureForFactory(
      self,
      factory: Optional[QSGCompressedTextureFactory],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGDefaultRenderContext::compressedTextureForFactory(const
    QSGCompressedTextureFactory *factory) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Parameters
    ----------

    factory : Optional[QSGCompressedTextureFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDefaultRenderContext::compressedTextureForFactory(const
    #      QSGCompressedTextureFactory *factory) const
    ritual = (
        'ritual_ZNK23QSGDefaultRenderContext27compressedTextureForFactoryEP'
        'K27QSGCompressedTextureFactory')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QSGDefaultRenderContext27compressedTextureForFac'
          'toryEPK27QSGCompressedTextureFactory')
    address = self.uglySide.call(ritual, self._addressOf(factory))
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int QSGDefaultRenderContext::maxTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#maxTextureSize
    """
    #  int QSGDefaultRenderContext::maxTextureSize() const
    ritual = 'ritual_ZNK23QSGDefaultRenderContext14maxTextureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGDefaultRenderContext14maxTextureSizeEv'
    return self.uglySide.call(ritual)

  def useDepthBufferFor2D(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultRenderContext::useDepthBufferFor2D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#useDepthBufferFor2D
    """
    #  bool QSGDefaultRenderContext::useDepthBufferFor2D() const
    return self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext19useDepthBufferFor2DEv',
    )

  def msaaSampleCount(self) -> int:
    """
    Calls Qt's 'int QSGDefaultRenderContext::msaaSampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#msaaSampleCount
    """
    #  int QSGDefaultRenderContext::msaaSampleCount() const
    return self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext15msaaSampleCountEv',
    )

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QSGDefaultRenderContext::currentFrameCommandBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer
    #      *QSGDefaultRenderContext::currentFrameCommandBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext25currentFrameCommandBufferEv',
    )
    from ..QtGui import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  def currentFrameRenderPass(self) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QSGDefaultRenderContext::currentFrameRenderPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QSGDefaultRenderContext::currentFrameRenderPass() const
    address = self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext22currentFrameRenderPassEv',
    )
    from ..QtGui import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def currentDevicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QSGDefaultRenderContext::currentDevicePixelRatio()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html
    """
    #  qreal QSGDefaultRenderContext::currentDevicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK23QSGDefaultRenderContext23currentDevicePixelRatioEv',
    )

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

  @overload(QSGContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGDefaultRenderContext::QSGDefaultRenderContext(QSGContext *context)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Parameters
    ----------

    context : Optional[QSGContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGDefaultRenderContext::QSGDefaultRenderContext(QSGContext *context)
    self._noteCreation(QSGDefaultRenderContext, lambda: Rituals.call(
        'ritual_ZN23QSGDefaultRenderContextC1EP10QSGContext',
        self._addressOf(context),
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

  @overload(QSGRenderContext.InitParams)
  @overload(NoneType)
  def initialize(
      self,
      params: Optional[QSGRenderContext.InitParams],
  ) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::initialize(const
    QSGRenderContext::InitParams *params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#initialize

    Parameters
    ----------

    params : Optional[QSGRenderContext.InitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultRenderContext::initialize(const
    #      QSGRenderContext::InitParams *params)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext10initializeEPKN16QSGRenderConte'
        'xt10InitParamsE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext10initializeEPKN16QSGRende'
          'rContext10InitParamsE')
    self.uglySide.call(ritual, self._addressOf(params))

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#invalidate
    """
    #  void QSGDefaultRenderContext::invalidate()
    ritual = 'ritual_ZN23QSGDefaultRenderContext10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultRenderContext10invalidateEv'
    self.uglySide.call(ritual)

  @overload(float, QRhiCommandBuffer, QQuickGraphicsConfiguration)
  @overload(float, NoneType, QQuickGraphicsConfiguration)
  def prepareSync(
      self,
      devicePixelRatio: float,
      cb: Optional[QRhiCommandBuffer],
      config: QQuickGraphicsConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::prepareSync(qreal
    devicePixelRatio, QRhiCommandBuffer *cb, const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#prepareSync

    Parameters
    ----------

    devicePixelRatio : float
      Passed on as it is.

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  void QSGDefaultRenderContext::prepareSync(qreal devicePixelRatio,
    #      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext11prepareSyncEdP17QRhiCommandBuf'
        'ferRK27QQuickGraphicsConfiguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext11prepareSyncEdP17QRhiComm'
          'andBufferRK27QQuickGraphicsConfiguration')
    self.uglySide.call(
        ritual, devicePixelRatio, self._addressOf(cb), self._valueOf(config),
    )

  @overload(QSGRenderer)
  @overload(NoneType)
  def renderNextFrame(self, renderer: Optional[QSGRenderer]) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::renderNextFrame(QSGRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#renderNextFrame

    Parameters
    ----------

    renderer : Optional[QSGRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultRenderContext::renderNextFrame(QSGRenderer *renderer)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext15renderNextFrameEP11QSGRenderer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext15renderNextFrameEP11QSGRe'
          'nderer')
    self.uglySide.call(ritual, self._addressOf(renderer))

  @overload(QSGRenderer)
  @overload(NoneType)
  def endNextFrame(self, renderer: Optional[QSGRenderer]) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::endNextFrame(QSGRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#endNextFrame

    Parameters
    ----------

    renderer : Optional[QSGRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultRenderContext::endNextFrame(QSGRenderer *renderer)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext12endNextFrameEP11QSGRenderer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext12endNextFrameEP11QSGRende'
          'rer')
    self.uglySide.call(ritual, self._addressOf(renderer))

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#preprocess
    """
    #  void QSGDefaultRenderContext::preprocess()
    ritual = 'ritual_ZN23QSGDefaultRenderContext10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultRenderContext10preprocessEv'
    self.uglySide.call(ritual)

  def invalidateGlyphCaches(self) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::invalidateGlyphCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#invalidateGlyphCaches
    """
    #  void QSGDefaultRenderContext::invalidateGlyphCaches()
    ritual = 'ritual_ZN23QSGDefaultRenderContext21invalidateGlyphCachesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext21invalidateGlyphCachesEv')
    self.uglySide.call(ritual)

  def flushGlyphCaches(self) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::flushGlyphCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#flushGlyphCaches
    """
    #  void QSGDefaultRenderContext::flushGlyphCaches()
    ritual = 'ritual_ZN23QSGDefaultRenderContext16flushGlyphCachesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultRenderContext16flushGlyphCachesEv'
    self.uglySide.call(ritual)

  @overload(QRawFont, int)
  def distanceFieldGlyphCache(
      self,
      font: QRawFont,
      renderTypeQuality: int,
  ) -> Optional[QSGDistanceFieldGlyphCache]:
    """
    Calls Qt's 'QSGDistanceFieldGlyphCache
    *QSGDefaultRenderContext::distanceFieldGlyphCache(const QRawFont &font,
    int renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    renderTypeQuality : int
      Passed on as it is.

    Returns
    -------

    Optional[QSGDistanceFieldGlyphCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGDistanceFieldGlyphCache
    #      *QSGDefaultRenderContext::distanceFieldGlyphCache(const QRawFont
    #      &font, int renderTypeQuality)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext23distanceFieldGlyphCacheERK8QRa'
        'wFonti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext23distanceFieldGlyphCacheE'
          'RK8QRawFonti')
    address = self.uglySide.call(
        ritual, self._valueOf(font), renderTypeQuality,
    )
    from . import QSGDistanceFieldGlyphCache
    return QSGDistanceFieldGlyphCache._cuteAt(address)

  @overload(QRawFont)
  def curveGlyphAtlas(self, font: QRawFont) -> Optional[QSGCurveGlyphAtlas]:
    """
    Calls Qt's 'QSGCurveGlyphAtlas
    *QSGDefaultRenderContext::curveGlyphAtlas(const QRawFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#curveGlyphAtlas

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    Returns
    -------

    Optional[QSGCurveGlyphAtlas]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGCurveGlyphAtlas *QSGDefaultRenderContext::curveGlyphAtlas(const
    #      QRawFont &font)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext15curveGlyphAtlasERK8QRawFont')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext15curveGlyphAtlasERK8QRawF'
          'ont')
    address = self.uglySide.call(ritual, self._valueOf(font))
    from . import QSGCurveGlyphAtlas
    return QSGCurveGlyphAtlas._cuteAt(address)

  @overload()
  @overload(QSGRendererInterface.RenderMode)
  def createRenderer(
      self,
      renderMode: QSGRendererInterface.RenderMode = (
          QSGRendererInterface.RenderMode.RenderMode2D),
  ) -> Optional[QSGRenderer]:
    """
    Calls Qt's 'QSGRenderer
    *QSGDefaultRenderContext::createRenderer(QSGRendererInterface::RenderMode
    renderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#createRenderer

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number. May be left out, as in Qt: it is then
      QSGRendererInterface.RenderMode.RenderMode2D.

    Returns
    -------

    Optional[QSGRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderer
    #      *QSGDefaultRenderContext::createRenderer(QSGRendererInterface::
    #      RenderMode renderMode)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext14createRendererEN20QSGRendererI'
        'nterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext14createRendererEN20QSGRen'
          'dererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGRenderer
    return QSGRenderer._cuteAt(address)

  @overload(QSGMaterialShader, QShader.Variant)
  @overload(NoneType, QShader.Variant)
  def initializeRhiShader(
      self,
      shader: Optional[QSGMaterialShader],
      shaderVariant: QShader.Variant,
  ) -> None:
    """
    Calls Qt's 'void
    QSGDefaultRenderContext::initializeRhiShader(QSGMaterialShader *shader,
    QShader::Variant shaderVariant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html#initializeRhiShader

    Parameters
    ----------

    shader : Optional[QSGMaterialShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    shaderVariant : QShader.Variant
      Passed on as its number.
    """
    #  void QSGDefaultRenderContext::initializeRhiShader(QSGMaterialShader
    #      *shader, QShader::Variant shaderVariant)
    ritual = (
        'ritual_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17QSGMate'
        'rialShaderN7QShader7VariantE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17Q'
          'SGMaterialShaderN7QShader7VariantE')
    self.uglySide.call(ritual, self._addressOf(shader), shaderVariant.value)

  def maybeGlyphCacheResourceUpdates(
      self,
  ) -> Optional[QRhiResourceUpdateBatch]:
    """
    Calls Qt's 'QRhiResourceUpdateBatch
    *QSGDefaultRenderContext::maybeGlyphCacheResourceUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Returns
    -------

    Optional[QRhiResourceUpdateBatch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatch
    #      *QSGDefaultRenderContext::maybeGlyphCacheResourceUpdates()
    address = self.uglySide.call(
        'ritual_ZN23QSGDefaultRenderContext30maybeGlyphCacheResourceUpdates'
        'Ev',
    )
    from ..QtGui import QRhiResourceUpdateBatch
    return QRhiResourceUpdateBatch._cuteAt(address)

  def glyphCacheResourceUpdates(self) -> Optional[QRhiResourceUpdateBatch]:
    """
    Calls Qt's 'QRhiResourceUpdateBatch
    *QSGDefaultRenderContext::glyphCacheResourceUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Returns
    -------

    Optional[QRhiResourceUpdateBatch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatch
    #      *QSGDefaultRenderContext::glyphCacheResourceUpdates()
    address = self.uglySide.call(
        'ritual_ZN23QSGDefaultRenderContext25glyphCacheResourceUpdatesEv',
    )
    from ..QtGui import QRhiResourceUpdateBatch
    return QRhiResourceUpdateBatch._cuteAt(address)

  @overload(QRhiTexture)
  @overload(NoneType)
  def deferredReleaseGlyphCacheTexture(
      self,
      texture: Optional[QRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QSGDefaultRenderContext::deferredReleaseGlyphCacheTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultRenderContext::deferredReleaseGlyphCacheTexture(
    #      QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN23QSGDefaultRenderContext32deferredReleaseGlyphCacheTextu'
        'reEP11QRhiTexture',
        self._addressOf(texture),
    )

  def resetGlyphCacheResources(self) -> None:
    """
    Calls Qt's 'void QSGDefaultRenderContext::resetGlyphCacheResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultrendercontext.html
    """
    #  void QSGDefaultRenderContext::resetGlyphCacheResources()
    self.uglySide.call(
        'ritual_ZN23QSGDefaultRenderContext24resetGlyphCacheResourcesEv',
    )

  @staticmethod
  def addDepthStencilBuffer(*__, **_) -> Never:
    """
    Qt's 'void QSGDefaultRenderContext::addDepthStencilBuffer(const
    QSharedPointer<QSGDepthStencilBuffer> &ds)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDefaultRenderContext.addDepthStencilBuffer' has no cute "
        "function yet. Qt's 'void "
        "QSGDefaultRenderContext::addDepthStencilBuffer(const "
        "QSharedPointer<QSGDepthStencilBuffer> &ds)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def getDepthStencilBuffer(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QSGDepthStencilBuffer>
    QSGDefaultRenderContext::getDepthStencilBuffer(const QSize &size, int
    sampleCount)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGDefaultRenderContext.getDepthStencilBuffer' has no cute "
        "function yet. Qt's 'QSharedPointer<QSGDepthStencilBuffer> "
        "QSGDefaultRenderContext::getDepthStencilBuffer(const QSize &size, "
        "int sampleCount)': gives a type Python has no way to take yet.")
