"""
QSGRenderContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRenderContext to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFontEngine, QImage, QRawFont, QRhi, QRhiCommandBuffer
  from . import QQuickGraphicsConfiguration, QQuickTextureFactory
  from . import QQuickWindow, QSGCompressedTextureFactory, QSGContext
  from . import QSGCurveGlyphAtlas, QSGDistanceFieldGlyphCache, QSGRenderer
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontEngine = WAIT['QFontEngine']
  QImage = WAIT['QImage']
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']
  QQuickTextureFactory = WAIT['QQuickTextureFactory']
  QQuickWindow = WAIT['QQuickWindow']
  QRawFont = WAIT['QRawFont']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QSGCompressedTextureFactory = WAIT['QSGCompressedTextureFactory']
  QSGContext = WAIT['QSGContext']
  QSGRenderer = WAIT['QSGRenderer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRenderContext(QObject):
  """
  The cute side of Qt's QSGRenderContext: a plain Python object standing in
  front of one C++ QSGRenderContext.

  It is built on the cute 'QObject', as Qt's QSGRenderContext is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRenderContext that has a ritual and that Python
  can call so far, 27 names in all: 'metaObject', 'tr', 'sceneGraphContext',
  'isValid', 'initialize', 'invalidate', 'prepareSync', 'renderNextFrame',
  'endNextFrame', 'endSync', 'preprocess', 'invalidateGlyphCaches',
  'flushGlyphCaches', 'distanceFieldGlyphCache', 'curveGlyphAtlas',
  'textureForFactory', 'createTexture', 'createRenderer',
  'compressedTextureForFactory', 'maxTextureSize',
  'unregisterFontengineForCleanup', 'registerFontengineForCleanup', 'rhi',
  'initialized', 'invalidated', 'releaseCachedResourcesRequested',
  'textureFactoryDestroyed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRenderContext::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGRenderContext::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRenderContext::~QSGRenderContext()': the destructor: Python
    never removes a C++ QSGRenderContext.
  - Qt's 'void QSGRenderContext::beginNextFrame(QSGRenderer *renderer, const
    QSGRenderTarget &renderTarget, RenderPassCallback mainPassRecordingStart,
    RenderPassCallback mainPassRecordingEnd, void *callbackUserData)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool operator==(const QSGRenderContext::FontKey &f1, const
    QSGRenderContext::FontKey &f2)': an operator between other classes,
    written inside this one.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGRenderContext is created at the first use, not by
    'QSGRenderContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRenderContext.
  - Qt tells when it has removed the C++ QSGRenderContext. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRenderContext that has no cute function yet,
    'beginNextFrame', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSGRenderContext, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CreateTextureFlags(CuteNum):
    """
    The enum 'QSGRenderContext::CreateTextureFlags' of Qt, with the 3 names
    Qt gives in it.
    """

    CreateTexture_Alpha = Kee[int](1)
    CreateTexture_Atlas = Kee[int](2)
    CreateTexture_Mipmap = Kee[int](4)

  #  The classes Qt writes inside QSGRenderContext, each a class in here as
  #  in C++.

  class InitParams(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGRenderContext::InitParams: a plain Python object
    standing in front of one C++ QSGRenderContext::InitParams.

    C++ hands a QSGRenderContext::InitParams around as a copy, so every C++
    QSGRenderContext::InitParams behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSGRenderContext::InitParams yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGRenderContext::InitParams::~InitParams()': the destructor:
      Python removes its C++ QSGRenderContext::InitParams by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGRenderContext::InitParams is created at the first use, not
      by 'QSGRenderContext::InitParams(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGRenderContext::InitParams back gives a copy the
      ritual made for Python, in a new cute QSGRenderContext::InitParams.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGRenderContext::InitParams'

    #  Qt's '~QSGRenderContext::InitParams()'. Naming it makes this a value
    #  class: Python owns every C++ QSGRenderContext::InitParams behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSGRenderContext10InitParamsD1Ev'

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
    Calls Qt's 'QString QSGRenderContext::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#tr

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
    #  QString QSGRenderContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QSGRenderContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRenderContext'

  #  A C++ QSGRenderContext Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRenderContext'

  #  The functions Qt calls itself that QSGRenderContext is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'beginNextFrame': (
          'void QSGRenderContext::beginNextFrame(QSGRenderer *, const '
          'QSGRenderTarget &, RenderPassCallback, RenderPassCallback, void '
          '*)',
      ),
  }

  #  The functions Qt calls itself that QSGRenderContext is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK16QSGRenderContext7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'initialize': (
          ('_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderContext.InitParams'),
           )),
      ),
      'invalidate': (
          ('_ZN16QSGRenderContext10invalidateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'prepareSync': (
          ('_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQu'
           'ickGraphicsConfiguration',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtQuick:QQuickGraphicsConfiguration'),
           )),
      ),
      'renderNextFrame': (
          ('_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderer'),
           )),
      ),
      'endNextFrame': (
          ('_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderer'),
           )),
      ),
      'endSync': (
          ('_ZN16QSGRenderContext7endSyncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'preprocess': (
          ('_ZN16QSGRenderContext10preprocessEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'invalidateGlyphCaches': (
          ('_ZN16QSGRenderContext21invalidateGlyphCachesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'flushGlyphCaches': (
          ('_ZN16QSGRenderContext16flushGlyphCachesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'distanceFieldGlyphCache': (
          ('_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti',
           ('address', 'address', 'QtQuick:QSGDistanceFieldGlyphCache'),
           (
               ('address', 'value', 'QtGui:QRawFont'),
               ('int', 'number', ''),
           )),
      ),
      'curveGlyphAtlas': (
          ('_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont',
           ('address', 'address', 'QtQuick:QSGCurveGlyphAtlas'),
           (
               ('address', 'value', 'QtGui:QRawFont'),
           )),
      ),
      'createTexture': (
          ('_ZNK16QSGRenderContext13createTextureERK6QImagej',
           ('address', 'address', 'QtQuick:QSGTexture'),
           (
               ('address', 'value', 'QtGui:QImage'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'createRenderer': (
          ('_ZN16QSGRenderContext14createRendererEN20QSGRendererInterface10'
           'RenderModeE',
           ('address', 'address', 'QtQuick:QSGRenderer'),
           (
               ('int', 'enum', 'QtQuick:QSGRendererInterface.RenderMode'),
           )),
      ),
      'compressedTextureForFactory': (
          ('_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGComp'
           'ressedTextureFactory',
           ('address', 'address', 'QtQuick:QSGTexture'),
           (
               ('address', 'address', 'QtQuick:QSGCompressedTextureFactory'),
           )),
      ),
      'maxTextureSize': (
          ('_ZNK16QSGRenderContext14maxTextureSizeEv',
           ('int', 'number', ''),
           ()),
      ),
      'rhi': (
          ('_ZNK16QSGRenderContext3rhiEv',
           ('address', 'address', 'QtGui:QRhi'),
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
    Calls Qt's 'const QMetaObject *QSGRenderContext::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRenderContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGRenderContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGRenderContext::sceneGraphContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#sceneGraphContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGRenderContext::sceneGraphContext() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGRenderContext17sceneGraphContextEv',
    )
    from . import QSGContext
    return QSGContext._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSGRenderContext::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#isValid
    """
    #  bool QSGRenderContext::isValid() const
    ritual = 'ritual_ZNK16QSGRenderContext7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGRenderContext7isValidEv'
    return self.uglySide.call(ritual)

  @overload(QImage)
  @overload(QImage, int)
  def createTexture(
      self,
      image: QImage,
      flags: int = 1,
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGRenderContext::createTexture(const QImage
    &image, uint flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#createTexture

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGRenderContext::createTexture(const QImage &image, uint
    #      flags) const
    address = self.uglySide.call(
        'ritual_ZNK16QSGRenderContext13createTextureERK6QImagej',
        self._valueOf(image), flags,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QSGCompressedTextureFactory)
  @overload(NoneType)
  def compressedTextureForFactory(
      self,
      a0: Optional[QSGCompressedTextureFactory],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGRenderContext::compressedTextureForFactory(const
    QSGCompressedTextureFactory *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#compressedTextureForFactory

    Parameters
    ----------

    a0 : Optional[QSGCompressedTextureFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGRenderContext::compressedTextureForFactory(const
    #      QSGCompressedTextureFactory *a0) const
    ritual = (
        'ritual_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGC'
        'ompressedTextureFactory')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QSGRenderContext27compressedTextureForFactoryEPK'
          '27QSGCompressedTextureFactory')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int QSGRenderContext::maxTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#maxTextureSize
    """
    #  int QSGRenderContext::maxTextureSize() const
    return self.uglySide.call(
        'ritual_ZNK16QSGRenderContext14maxTextureSizeEv',
    )

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSGRenderContext::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSGRenderContext::rhi() const
    ritual = 'ritual_ZNK16QSGRenderContext3rhiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGRenderContext3rhiEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

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
    'QSGRenderContext::QSGRenderContext(QSGContext *context)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#QSGRenderContext

    Parameters
    ----------

    context : Optional[QSGContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGRenderContext::QSGRenderContext(QSGContext *context)
    self._noteCreation(QSGRenderContext, lambda: Rituals.call(
        'ritual_ZN16QSGRenderContextC1EP10QSGContext',
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

  @overload(InitParams)
  @overload(NoneType)
  def initialize(self, params: Optional[InitParams]) -> None:
    """
    Calls Qt's 'void QSGRenderContext::initialize(const InitParams *params)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#initialize

    Parameters
    ----------

    params : Optional[InitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::initialize(const InitParams *params)
    ritual = 'ritual_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE')
    self.uglySide.call(ritual, self._addressOf(params))

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#invalidate
    """
    #  void QSGRenderContext::invalidate()
    ritual = 'ritual_ZN16QSGRenderContext10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext10invalidateEv'
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
    Calls Qt's 'void QSGRenderContext::prepareSync(qreal devicePixelRatio,
    QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#prepareSync

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
    #  void QSGRenderContext::prepareSync(qreal devicePixelRatio,
    #      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
    ritual = (
        'ritual_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27'
        'QQuickGraphicsConfiguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBuff'
          'erRK27QQuickGraphicsConfiguration')
    self.uglySide.call(
        ritual, devicePixelRatio, self._addressOf(cb), self._valueOf(config),
    )

  @overload(QSGRenderer)
  @overload(NoneType)
  def renderNextFrame(self, renderer: Optional[QSGRenderer]) -> None:
    """
    Calls Qt's 'void QSGRenderContext::renderNextFrame(QSGRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#renderNextFrame

    Parameters
    ----------

    renderer : Optional[QSGRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::renderNextFrame(QSGRenderer *renderer)
    self.uglySide.call(
        'ritual_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer',
        self._addressOf(renderer),
    )

  @overload(QSGRenderer)
  @overload(NoneType)
  def endNextFrame(self, renderer: Optional[QSGRenderer]) -> None:
    """
    Calls Qt's 'void QSGRenderContext::endNextFrame(QSGRenderer *renderer)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#endNextFrame

    Parameters
    ----------

    renderer : Optional[QSGRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::endNextFrame(QSGRenderer *renderer)
    ritual = 'ritual_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer'
    self.uglySide.call(ritual, self._addressOf(renderer))

  def endSync(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::endSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#endSync
    """
    #  void QSGRenderContext::endSync()
    ritual = 'ritual_ZN16QSGRenderContext7endSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext7endSyncEv'
    self.uglySide.call(ritual)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::preprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#preprocess
    """
    #  void QSGRenderContext::preprocess()
    ritual = 'ritual_ZN16QSGRenderContext10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext10preprocessEv'
    self.uglySide.call(ritual)

  def invalidateGlyphCaches(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::invalidateGlyphCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#invalidateGlyphCaches
    """
    #  void QSGRenderContext::invalidateGlyphCaches()
    ritual = 'ritual_ZN16QSGRenderContext21invalidateGlyphCachesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext21invalidateGlyphCachesEv'
    self.uglySide.call(ritual)

  def flushGlyphCaches(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::flushGlyphCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#flushGlyphCaches
    """
    #  void QSGRenderContext::flushGlyphCaches()
    ritual = 'ritual_ZN16QSGRenderContext16flushGlyphCachesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext16flushGlyphCachesEv'
    self.uglySide.call(ritual)

  @overload(QRawFont, int)
  def distanceFieldGlyphCache(
      self,
      font: QRawFont,
      renderTypeQuality: int,
  ) -> Optional[QSGDistanceFieldGlyphCache]:
    """
    Calls Qt's 'QSGDistanceFieldGlyphCache
    *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font, int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#distanceFieldGlyphCache

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
    #      *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font,
    #      int renderTypeQuality)
    ritual = (
        'ritual_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRaw'
          'Fonti')
    address = self.uglySide.call(
        ritual, self._valueOf(font), renderTypeQuality,
    )
    from . import QSGDistanceFieldGlyphCache
    return QSGDistanceFieldGlyphCache._cuteAt(address)

  @overload(QRawFont)
  def curveGlyphAtlas(self, font: QRawFont) -> Optional[QSGCurveGlyphAtlas]:
    """
    Calls Qt's 'QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const
    QRawFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#curveGlyphAtlas

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
    #  QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const QRawFont
    #      &font)
    ritual = 'ritual_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont'
    address = self.uglySide.call(ritual, self._valueOf(font))
    from . import QSGCurveGlyphAtlas
    return QSGCurveGlyphAtlas._cuteAt(address)

  @overload(QQuickTextureFactory, QQuickWindow)
  @overload(QQuickTextureFactory, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def textureForFactory(
      self,
      factory: Optional[QQuickTextureFactory],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGRenderContext::textureForFactory(QQuickTextureFactory *factory,
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#textureForFactory

    Parameters
    ----------

    factory : Optional[QQuickTextureFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGRenderContext::textureForFactory(QQuickTextureFactory
    #      *factory, QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN16QSGRenderContext17textureForFactoryEP20QQuickTextureFac'
        'toryP12QQuickWindow',
        self._addressOf(factory), self._addressOf(window),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload()
  @overload(QSGRendererInterface.RenderMode)
  def createRenderer(
      self,
      renderMode: QSGRendererInterface.RenderMode = (
          QSGRendererInterface.RenderMode.RenderMode2D),
  ) -> Optional[QSGRenderer]:
    """
    Calls Qt's 'QSGRenderer
    *QSGRenderContext::createRenderer(QSGRendererInterface::RenderMode
    renderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#createRenderer

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
    #      *QSGRenderContext::createRenderer(QSGRendererInterface::RenderMode
    #      renderMode)
    address = self.uglySide.call(
        'ritual_ZN16QSGRenderContext14createRendererEN20QSGRendererInterfac'
        'e10RenderModeE',
        renderMode.value,
    )
    from . import QSGRenderer
    return QSGRenderer._cuteAt(address)

  @overload(QFontEngine)
  @overload(NoneType)
  def unregisterFontengineForCleanup(
      self,
      engine: Optional[QFontEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRenderContext::unregisterFontengineForCleanup(QFontEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html

    Parameters
    ----------

    engine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::unregisterFontengineForCleanup(QFontEngine
    #      *engine)
    self.uglySide.call(
        'ritual_ZN16QSGRenderContext30unregisterFontengineForCleanupEP11QFo'
        'ntEngine',
        self._addressOf(engine),
    )

  @overload(QFontEngine)
  @overload(NoneType)
  def registerFontengineForCleanup(
      self,
      engine: Optional[QFontEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRenderContext::registerFontengineForCleanup(QFontEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#registerFontengineForCleanup

    Parameters
    ----------

    engine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::registerFontengineForCleanup(QFontEngine
    #      *engine)
    self.uglySide.call(
        'ritual_ZN16QSGRenderContext28registerFontengineForCleanupEP11QFont'
        'Engine',
        self._addressOf(engine),
    )

  def initialized(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::initialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#initialized
    """
    #  void QSGRenderContext::initialized()
    self.uglySide.call('ritual_ZN16QSGRenderContext11initializedEv')

  def invalidated(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::invalidated()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrendercontext.html#invalidated
    """
    #  void QSGRenderContext::invalidated()
    self.uglySide.call('ritual_ZN16QSGRenderContext11invalidatedEv')

  def releaseCachedResourcesRequested(self) -> None:
    """
    Calls Qt's 'void QSGRenderContext::releaseCachedResourcesRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html
    """
    #  void QSGRenderContext::releaseCachedResourcesRequested()
    self.uglySide.call(
        'ritual_ZN16QSGRenderContext31releaseCachedResourcesRequestedEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def textureFactoryDestroyed(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QSGRenderContext::textureFactoryDestroyed(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendercontext.html#textureFactoryDestroyed

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderContext::textureFactoryDestroyed(QObject *o)
    self.uglySide.call(
        'ritual_ZN16QSGRenderContext23textureFactoryDestroyedEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  @staticmethod
  def beginNextFrame(*__, **_) -> Never:
    """
    Qt's 'void QSGRenderContext::beginNextFrame(QSGRenderer *renderer, const
    QSGRenderTarget &renderTarget, RenderPassCallback mainPassRecordingStart,
    RenderPassCallback mainPassRecordingEnd, void *callbackUserData)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGRenderContext.beginNextFrame' has no cute function yet. Qt's "
        "'void QSGRenderContext::beginNextFrame(QSGRenderer *renderer, "
        "const QSGRenderTarget &renderTarget, RenderPassCallback "
        "mainPassRecordingStart, RenderPassCallback mainPassRecordingEnd, "
        "void *callbackUserData)': takes a type Python has no way to hand "
        "over yet.")
