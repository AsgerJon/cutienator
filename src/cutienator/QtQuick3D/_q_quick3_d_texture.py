"""
QQuick3DTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DTexture to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItemChangeListener
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QUrl
  from ..QtQuick import QQuickGeometryChange, QQuickItem, QQuickWindow
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject, QSSGRenderImage
  from . import QQuick3DRenderExtension, QQuick3DTextureData
  from . import QQuick3DTextureInternalChange
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DRenderExtension = WAIT['QQuick3DRenderExtension']
  QQuick3DTextureData = WAIT['QQuick3DTextureData']
  QQuick3DTextureInternalChange = WAIT['QQuick3DTextureInternalChange']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DTexture(QQuick3DObject, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuick3DTexture: a plain Python object standing in
  front of one C++ QQuick3DTexture.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DTexture is built
  on Qt's QQuick3DObject, and has everything that class has. It is built on
  the cute 'QQuickItemChangeListener' as well, as Qt's QQuick3DTexture is
  built on Qt's QQuickItemChangeListener too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuick3DTexture that has a ritual and that Python
  can call so far, 81 names in all: 'metaObject', 'tr', 'source',
  'sourceItem', 'scaleU', 'scaleV', 'mappingMode', 'horizontalTiling',
  'verticalTiling', 'depthTiling', 'rotationUV', 'positionU', 'positionV',
  'pivotU', 'pivotV', 'flipU', 'flipV', 'indexUV', 'magFilter', 'minFilter',
  'mipFilter', 'textureData', 'generateMipmaps', 'autoOrientation',
  'getRenderImage', 'textureProvider', 'setTextureProvider', 'hasSourceData',
  'setSource', 'setSourceItem', 'setScaleU', 'setScaleV', 'setMappingMode',
  'setHorizontalTiling', 'setVerticalTiling', 'setDepthTiling',
  'setRotationUV', 'setPositionU', 'setPositionV', 'setPivotU', 'setPivotV',
  'setFlipU', 'setFlipV', 'setIndexUV', 'setMagFilter', 'setMinFilter',
  'setMipFilter', 'setTextureData', 'setGenerateMipmaps',
  'setAutoOrientation', 'sourceChanged', 'sourceItemChanged',
  'scaleUChanged', 'scaleVChanged', 'mappingModeChanged',
  'horizontalTilingChanged', 'verticalTilingChanged', 'depthTilingChanged',
  'rotationUVChanged', 'positionUChanged', 'positionVChanged',
  'pivotUChanged', 'pivotVChanged', 'flipUChanged', 'flipVChanged',
  'indexUVChanged', 'magFilterChanged', 'minFilterChanged',
  'mipFilterChanged', 'textureDataChanged', 'generateMipmapsChanged',
  'autoOrientationChanged', 'textureProviderChanged',
  'textureInternalChange', 'updateSpatialNode', 'markAllDirty', 'itemChange',
  'itemGeometryChanged', 'sourceItemDestroyed', 'sourceItemWindowChanged',
  'trySetSourceParent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DTexture::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DTexture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DTexture::~QQuick3DTexture()': the destructor: Python never
    removes a C++ QQuick3DTexture.
  - Qt's 'QQuick3DTexture::QQuick3DTexture(QQuick3DObjectPrivate &dd,
    QQuick3DObject *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuick3DTexture::markDirty(DirtyFlag type, bool
    requestSecondaryUpdate)': names the enum 'QQuick3DTexture::DirtyFlag',
    whose class cannot be named here.
  - Qt's 'bool QQuick3DTexture::effectiveFlipV(const QSSGRenderImage
    &imageNode) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 90 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DTexture is created at the first use, not by
    'QQuick3DTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DTexture.
  - Qt tells when it has removed the C++ QQuick3DTexture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DTexture that has no cute function yet,
    'effectiveFlipV', 'markDirty', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DTexture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Filter(CuteNum):
    """
    The enum 'QQuick3DTexture::Filter' of Qt, with the 3 names Qt gives in
    it.
    """

    NULL = Kee[int](0)
    Nearest = Kee[int](1)
    Linear = Kee[int](2)

  class MappingMode(CuteNum):
    """
    The enum 'QQuick3DTexture::MappingMode' of Qt, with the 3 names Qt gives
    in it.
    """

    UV = Kee[int](0)
    Environment = Kee[int](1)
    LightProbe = Kee[int](2)

  class TilingMode(CuteNum):
    """
    The enum 'QQuick3DTexture::TilingMode' of Qt, with the 3 names Qt gives
    in it.
    """

    ClampToEdge = Kee[int](1)
    MirroredRepeat = Kee[int](2)
    Repeat = Kee[int](3)

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
    Calls Qt's 'QString QQuick3DTexture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#tr

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
    #  QString QQuick3DTexture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuick3DTexture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DTexture'

  #  Qt's QQuick3DTexture is built on more than one class. The part of a C++
  #  QQuick3DTexture that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuick3DTexture_QQuickItemChangeListener',
  }

  #  A C++ QQuick3DTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DTexture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DTexture::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuick3DTexture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DTexture::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DTexture::source() const
    address = self.uglySide.call('ritual_ZNK15QQuick3DTexture6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuick3DTexture::sourceItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#sourceItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuick3DTexture::sourceItem() const
    address = self.uglySide.call('ritual_ZNK15QQuick3DTexture10sourceItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def scaleU(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::scaleU() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#scaleU
    """
    #  float QQuick3DTexture::scaleU() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture6scaleUEv')

  def scaleV(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::scaleV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#scaleV
    """
    #  float QQuick3DTexture::scaleV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture6scaleVEv')

  def mappingMode(self) -> MappingMode:
    """
    Calls Qt's 'MappingMode QQuick3DTexture::mappingMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#mappingMode

    Returns
    -------

    MappingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MappingMode(number)'
      gives.
    """
    #  MappingMode QQuick3DTexture::mappingMode() const
    return QQuick3DTexture.MappingMode(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture11mappingModeEv',
    ))

  def horizontalTiling(self) -> TilingMode:
    """
    Calls Qt's 'TilingMode QQuick3DTexture::horizontalTiling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#horizontalTiling

    Returns
    -------

    TilingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TilingMode(number)'
      gives.
    """
    #  TilingMode QQuick3DTexture::horizontalTiling() const
    return QQuick3DTexture.TilingMode(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture16horizontalTilingEv',
    ))

  def verticalTiling(self) -> TilingMode:
    """
    Calls Qt's 'TilingMode QQuick3DTexture::verticalTiling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#verticalTiling

    Returns
    -------

    TilingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TilingMode(number)'
      gives.
    """
    #  TilingMode QQuick3DTexture::verticalTiling() const
    return QQuick3DTexture.TilingMode(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture14verticalTilingEv',
    ))

  def depthTiling(self) -> TilingMode:
    """
    Calls Qt's 'TilingMode QQuick3DTexture::depthTiling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#depthTiling

    Returns
    -------

    TilingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TilingMode(number)'
      gives.
    """
    #  TilingMode QQuick3DTexture::depthTiling() const
    return QQuick3DTexture.TilingMode(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture11depthTilingEv',
    ))

  def rotationUV(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::rotationUV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#rotationUV
    """
    #  float QQuick3DTexture::rotationUV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture10rotationUVEv')

  def positionU(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::positionU() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#positionU
    """
    #  float QQuick3DTexture::positionU() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture9positionUEv')

  def positionV(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::positionV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#positionV
    """
    #  float QQuick3DTexture::positionV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture9positionVEv')

  def pivotU(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::pivotU() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#pivotU
    """
    #  float QQuick3DTexture::pivotU() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture6pivotUEv')

  def pivotV(self) -> float:
    """
    Calls Qt's 'float QQuick3DTexture::pivotV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#pivotV
    """
    #  float QQuick3DTexture::pivotV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture6pivotVEv')

  def flipU(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTexture::flipU() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#flipU
    """
    #  bool QQuick3DTexture::flipU() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture5flipUEv')

  def flipV(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTexture::flipV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#flipV
    """
    #  bool QQuick3DTexture::flipV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture5flipVEv')

  def indexUV(self) -> int:
    """
    Calls Qt's 'int QQuick3DTexture::indexUV() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#indexUV
    """
    #  int QQuick3DTexture::indexUV() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture7indexUVEv')

  def magFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QQuick3DTexture::magFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#magFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QQuick3DTexture::magFilter() const
    return QQuick3DTexture.Filter(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture9magFilterEv',
    ))

  def minFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QQuick3DTexture::minFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#minFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QQuick3DTexture::minFilter() const
    return QQuick3DTexture.Filter(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture9minFilterEv',
    ))

  def mipFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QQuick3DTexture::mipFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#mipFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QQuick3DTexture::mipFilter() const
    return QQuick3DTexture.Filter(self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture9mipFilterEv',
    ))

  def textureData(self) -> Optional[QQuick3DTextureData]:
    """
    Calls Qt's 'QQuick3DTextureData *QQuick3DTexture::textureData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#textureData

    Returns
    -------

    Optional[QQuick3DTextureData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTextureData *QQuick3DTexture::textureData() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture11textureDataEv',
    )
    from . import QQuick3DTextureData
    return QQuick3DTextureData._cuteAt(address)

  def generateMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTexture::generateMipmaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#generateMipmaps
    """
    #  bool QQuick3DTexture::generateMipmaps() const
    return self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture15generateMipmapsEv',
    )

  def autoOrientation(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTexture::autoOrientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#autoOrientation
    """
    #  bool QQuick3DTexture::autoOrientation() const
    return self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture15autoOrientationEv',
    )

  def textureProvider(self) -> Optional[QQuick3DRenderExtension]:
    """
    Calls Qt's 'QQuick3DRenderExtension *QQuick3DTexture::textureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#textureProvider

    Returns
    -------

    Optional[QQuick3DRenderExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderExtension *QQuick3DTexture::textureProvider() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuick3DTexture15textureProviderEv',
    )
    from . import QQuick3DRenderExtension
    return QQuick3DRenderExtension._cuteAt(address)

  def hasSourceData(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTexture::hasSourceData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#hasSourceData
    """
    #  bool QQuick3DTexture::hasSourceData() const
    return self.uglySide.call('ritual_ZNK15QQuick3DTexture13hasSourceDataEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DRenderExtension)
  @overload(NoneType)
  def setTextureProvider(
      self,
      newRenderTexture: Optional[QQuick3DRenderExtension],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::setTextureProvider(QQuick3DRenderExtension
    *newRenderTexture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setTextureProvider

    Parameters
    ----------

    newRenderTexture : Optional[QQuick3DRenderExtension]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DTexture::setTextureProvider(QQuick3DRenderExtension
    #      *newRenderTexture)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture18setTextureProviderEP23QQuick3DRenderEx'
        'tension',
        self._addressOf(newRenderTexture),
    )

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DTexture::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setSourceItem(self, sourceItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setSourceItem(QQuickItem *sourceItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setSourceItem

    Parameters
    ----------

    sourceItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DTexture::setSourceItem(QQuickItem *sourceItem)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture13setSourceItemEP10QQuickItem',
        self._addressOf(sourceItem),
    )

  @overload(float)
  def setScaleU(self, scaleU: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setScaleU(float scaleU)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setScaleU

    Parameters
    ----------

    scaleU : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setScaleU(float scaleU)
    self.uglySide.call('ritual_ZN15QQuick3DTexture9setScaleUEf', scaleU)

  @overload(float)
  def setScaleV(self, scaleV: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setScaleV(float scaleV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setScaleV

    Parameters
    ----------

    scaleV : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setScaleV(float scaleV)
    self.uglySide.call('ritual_ZN15QQuick3DTexture9setScaleVEf', scaleV)

  @overload(MappingMode)
  def setMappingMode(self, mappingMode: MappingMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::setMappingMode(QQuick3DTexture::MappingMode
    mappingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setMappingMode

    Parameters
    ----------

    mappingMode : MappingMode
      Passed on as its number.
    """
    #  void QQuick3DTexture::setMappingMode(QQuick3DTexture::MappingMode
    #      mappingMode)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture14setMappingModeENS_11MappingModeE',
        mappingMode.value,
    )

  @overload(TilingMode)
  def setHorizontalTiling(self, tilingModeHorizontal: TilingMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::setHorizontalTiling(QQuick3DTexture::TilingMode
    tilingModeHorizontal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setHorizontalTiling

    Parameters
    ----------

    tilingModeHorizontal : TilingMode
      Passed on as its number.
    """
    #  void QQuick3DTexture::setHorizontalTiling(QQuick3DTexture::TilingMode
    #      tilingModeHorizontal)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture19setHorizontalTilingENS_10TilingModeE',
        tilingModeHorizontal.value,
    )

  @overload(TilingMode)
  def setVerticalTiling(self, tilingModeVertical: TilingMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::setVerticalTiling(QQuick3DTexture::TilingMode
    tilingModeVertical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setVerticalTiling

    Parameters
    ----------

    tilingModeVertical : TilingMode
      Passed on as its number.
    """
    #  void QQuick3DTexture::setVerticalTiling(QQuick3DTexture::TilingMode
    #      tilingModeVertical)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture17setVerticalTilingENS_10TilingModeE',
        tilingModeVertical.value,
    )

  @overload(TilingMode)
  def setDepthTiling(self, tilingModeDepth: TilingMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::setDepthTiling(QQuick3DTexture::TilingMode
    tilingModeDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setDepthTiling

    Parameters
    ----------

    tilingModeDepth : TilingMode
      Passed on as its number.
    """
    #  void QQuick3DTexture::setDepthTiling(QQuick3DTexture::TilingMode
    #      tilingModeDepth)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture14setDepthTilingENS_10TilingModeE',
        tilingModeDepth.value,
    )

  @overload(float)
  def setRotationUV(self, rotationUV: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setRotationUV(float rotationUV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setRotationUV

    Parameters
    ----------

    rotationUV : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setRotationUV(float rotationUV)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture13setRotationUVEf', rotationUV,
    )

  @overload(float)
  def setPositionU(self, positionU: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setPositionU(float positionU)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setPositionU

    Parameters
    ----------

    positionU : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setPositionU(float positionU)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture12setPositionUEf', positionU,
    )

  @overload(float)
  def setPositionV(self, positionV: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setPositionV(float positionV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setPositionV

    Parameters
    ----------

    positionV : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setPositionV(float positionV)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture12setPositionVEf', positionV,
    )

  @overload(float)
  def setPivotU(self, pivotU: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setPivotU(float pivotU)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setPivotU

    Parameters
    ----------

    pivotU : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setPivotU(float pivotU)
    self.uglySide.call('ritual_ZN15QQuick3DTexture9setPivotUEf', pivotU)

  @overload(float)
  def setPivotV(self, pivotV: float) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setPivotV(float pivotV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setPivotV

    Parameters
    ----------

    pivotV : float
      Passed on as it is.
    """
    #  void QQuick3DTexture::setPivotV(float pivotV)
    self.uglySide.call('ritual_ZN15QQuick3DTexture9setPivotVEf', pivotV)

  @overload(bool)
  def setFlipU(self, flipU: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setFlipU(bool flipU)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setFlipU

    Parameters
    ----------

    flipU : bool
      Passed on as it is.
    """
    #  void QQuick3DTexture::setFlipU(bool flipU)
    self.uglySide.call('ritual_ZN15QQuick3DTexture8setFlipUEb', flipU)

  @overload(bool)
  def setFlipV(self, flipV: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setFlipV(bool flipV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setFlipV

    Parameters
    ----------

    flipV : bool
      Passed on as it is.
    """
    #  void QQuick3DTexture::setFlipV(bool flipV)
    self.uglySide.call('ritual_ZN15QQuick3DTexture8setFlipVEb', flipV)

  @overload(int)
  def setIndexUV(self, indexUV: int) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setIndexUV(int indexUV)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setIndexUV

    Parameters
    ----------

    indexUV : int
      Passed on as it is.
    """
    #  void QQuick3DTexture::setIndexUV(int indexUV)
    self.uglySide.call('ritual_ZN15QQuick3DTexture10setIndexUVEi', indexUV)

  @overload(Filter)
  def setMagFilter(self, magFilter: Filter) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setMagFilter(QQuick3DTexture::Filter
    magFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setMagFilter

    Parameters
    ----------

    magFilter : Filter
      Passed on as its number.
    """
    #  void QQuick3DTexture::setMagFilter(QQuick3DTexture::Filter magFilter)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture12setMagFilterENS_6FilterE',
        magFilter.value,
    )

  @overload(Filter)
  def setMinFilter(self, minFilter: Filter) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setMinFilter(QQuick3DTexture::Filter
    minFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setMinFilter

    Parameters
    ----------

    minFilter : Filter
      Passed on as its number.
    """
    #  void QQuick3DTexture::setMinFilter(QQuick3DTexture::Filter minFilter)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture12setMinFilterENS_6FilterE',
        minFilter.value,
    )

  @overload(Filter)
  def setMipFilter(self, mipFilter: Filter) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setMipFilter(QQuick3DTexture::Filter
    mipFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#setMipFilter

    Parameters
    ----------

    mipFilter : Filter
      Passed on as its number.
    """
    #  void QQuick3DTexture::setMipFilter(QQuick3DTexture::Filter mipFilter)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture12setMipFilterENS_6FilterE',
        mipFilter.value,
    )

  @overload(QQuick3DTextureData)
  @overload(NoneType)
  def setTextureData(
      self,
      textureData: Optional[QQuick3DTextureData],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setTextureData(QQuick3DTextureData
    *textureData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setTextureData

    Parameters
    ----------

    textureData : Optional[QQuick3DTextureData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DTexture::setTextureData(QQuick3DTextureData *textureData)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture14setTextureDataEP19QQuick3DTextureData',
        self._addressOf(textureData),
    )

  @overload(bool)
  def setGenerateMipmaps(self, generateMipmaps: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setGenerateMipmaps(bool
    generateMipmaps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setGenerateMipmaps

    Parameters
    ----------

    generateMipmaps : bool
      Passed on as it is.
    """
    #  void QQuick3DTexture::setGenerateMipmaps(bool generateMipmaps)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture18setGenerateMipmapsEb', generateMipmaps,
    )

  @overload(bool)
  def setAutoOrientation(self, autoOrientation: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::setAutoOrientation(bool
    autoOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#setAutoOrientation

    Parameters
    ----------

    autoOrientation : bool
      Passed on as it is.
    """
    #  void QQuick3DTexture::setAutoOrientation(bool autoOrientation)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture18setAutoOrientationEb', autoOrientation,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DTexture::QQuick3DTexture(QQuick3DObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#QQuick3DTexture

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DTexture::QQuick3DTexture(QQuick3DObject *parent)
    self._noteCreation(QQuick3DTexture, lambda: Rituals.call(
        'ritual_ZN15QQuick3DTextureC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def getRenderImage(self) -> Optional[QSSGRenderImage]:
    """
    Calls Qt's 'QSSGRenderImage *QQuick3DTexture::getRenderImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#getRenderImage

    Returns
    -------

    Optional[QSSGRenderImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderImage *QQuick3DTexture::getRenderImage()
    address = self.uglySide.call(
        'ritual_ZN15QQuick3DTexture14getRenderImageEv',
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderImage
    return QSSGRenderImage._cuteAt(address)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#sourceChanged
    """
    #  void QQuick3DTexture::sourceChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture13sourceChangedEv')

  def sourceItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::sourceItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#sourceItemChanged
    """
    #  void QQuick3DTexture::sourceItemChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture17sourceItemChangedEv')

  def scaleUChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::scaleUChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#scaleUChanged
    """
    #  void QQuick3DTexture::scaleUChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture13scaleUChangedEv')

  def scaleVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::scaleVChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#scaleVChanged
    """
    #  void QQuick3DTexture::scaleVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture13scaleVChangedEv')

  def mappingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::mappingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#mappingModeChanged
    """
    #  void QQuick3DTexture::mappingModeChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture18mappingModeChangedEv')

  def horizontalTilingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::horizontalTilingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#horizontalTilingChanged
    """
    #  void QQuick3DTexture::horizontalTilingChanged()
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture23horizontalTilingChangedEv',
    )

  def verticalTilingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::verticalTilingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#verticalTilingChanged
    """
    #  void QQuick3DTexture::verticalTilingChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture21verticalTilingChangedEv')

  def depthTilingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::depthTilingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#depthTilingChanged
    """
    #  void QQuick3DTexture::depthTilingChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture18depthTilingChangedEv')

  def rotationUVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::rotationUVChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#rotationUVChanged
    """
    #  void QQuick3DTexture::rotationUVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture17rotationUVChangedEv')

  def positionUChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::positionUChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#positionUChanged
    """
    #  void QQuick3DTexture::positionUChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture16positionUChangedEv')

  def positionVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::positionVChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#positionVChanged
    """
    #  void QQuick3DTexture::positionVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture16positionVChangedEv')

  def pivotUChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::pivotUChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#pivotUChanged
    """
    #  void QQuick3DTexture::pivotUChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture13pivotUChangedEv')

  def pivotVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::pivotVChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#pivotVChanged
    """
    #  void QQuick3DTexture::pivotVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture13pivotVChangedEv')

  def flipUChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::flipUChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#flipUChanged
    """
    #  void QQuick3DTexture::flipUChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture12flipUChangedEv')

  def flipVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::flipVChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#flipVChanged
    """
    #  void QQuick3DTexture::flipVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture12flipVChangedEv')

  def indexUVChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::indexUVChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#indexUVChanged
    """
    #  void QQuick3DTexture::indexUVChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture14indexUVChangedEv')

  def magFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::magFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#magFilterChanged
    """
    #  void QQuick3DTexture::magFilterChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture16magFilterChangedEv')

  def minFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::minFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#minFilterChanged
    """
    #  void QQuick3DTexture::minFilterChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture16minFilterChangedEv')

  def mipFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::mipFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#mipFilterChanged
    """
    #  void QQuick3DTexture::mipFilterChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture16mipFilterChangedEv')

  def textureDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::textureDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#textureDataChanged
    """
    #  void QQuick3DTexture::textureDataChanged()
    self.uglySide.call('ritual_ZN15QQuick3DTexture18textureDataChangedEv')

  def generateMipmapsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::generateMipmapsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#generateMipmapsChanged
    """
    #  void QQuick3DTexture::generateMipmapsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture22generateMipmapsChangedEv',
    )

  def autoOrientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::autoOrientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#autoOrientationChanged
    """
    #  void QQuick3DTexture::autoOrientationChanged()
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture22autoOrientationChangedEv',
    )

  def textureProviderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::textureProviderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#textureProviderChanged
    """
    #  void QQuick3DTexture::textureProviderChanged()
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture22textureProviderChangedEv',
    )

  @overload(QQuick3DTextureInternalChange)
  def textureInternalChange(self, a0: QQuick3DTextureInternalChange) -> None:
    """
    Calls Qt's 'void
    QQuick3DTexture::textureInternalChange(QQuick3DTextureInternalChange a0,
    QPrivateSignal a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#textureInternalChange

    Parameters
    ----------

    a0 : QQuick3DTextureInternalChange
      Passed on as a value: Qt reads the C++ QQuick3DTextureInternalChange,
      which stays Python's own.
    """
    #  void QQuick3DTexture::textureInternalChange(
    #      QQuick3DTextureInternalChange a0, QPrivateSignal a1)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture21textureInternalChangeE29QQuick3DTextur'
        'eInternalChangeNS_14QPrivateSignalE',
        self._valueOf(a0),
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DTexture::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DTexture::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN15QQuick3DTexture17updateSpatialNodeEP21QSSGRenderGraphOb'
        'ject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuick3DTexture17updateSpatialNodeEP21QSSGRenderG'
          'raphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#markAllDirty
    """
    #  void QQuick3DTexture::markAllDirty()
    ritual = 'ritual_ZN15QQuick3DTexture12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuick3DTexture12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      change: QQuick3DObject.ItemChange,
      value: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexture.html#itemChange

    Parameters
    ----------

    change : QQuick3DObject.ItemChange
      Passed on as its number.

    value : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DTexture::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuick3DTexture10itemChangeEN14QQuick3DObject10ItemChan'
        'geERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuick3DTexture10itemChangeEN14QQuick3DObject10It'
          'emChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      geometry: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuick3DTexture::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &geometry)
    ritual = (
        'ritual_ZN15QQuick3DTexture19itemGeometryChangedEP10QQuickItem20QQu'
        'ickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuick3DTexture19itemGeometryChangedEP10QQuickIte'
          'm20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change),
        self._valueOf(geometry),
    )

  @overload(QObject)
  @overload(NoneType)
  def sourceItemDestroyed(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::sourceItemDestroyed(QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#sourceItemDestroyed

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DTexture::sourceItemDestroyed(QObject *item)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture19sourceItemDestroyedEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def sourceItemWindowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::sourceItemWindowChanged(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#sourceItemWindowChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DTexture::sourceItemWindowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN15QQuick3DTexture23sourceItemWindowChangedEP12QQuickWindo'
        'w',
        self._addressOf(window),
    )

  def trySetSourceParent(self) -> None:
    """
    Calls Qt's 'void QQuick3DTexture::trySetSourceParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexture.html#trySetSourceParent
    """
    #  void QQuick3DTexture::trySetSourceParent()
    self.uglySide.call('ritual_ZN15QQuick3DTexture18trySetSourceParentEv')

  @staticmethod
  def effectiveFlipV(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DTexture::effectiveFlipV(const QSSGRenderImage
    &imageNode) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DTexture.effectiveFlipV' has no cute function yet. Qt's "
        "'bool QQuick3DTexture::effectiveFlipV(const QSSGRenderImage "
        "&imageNode) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DTexture::markDirty(DirtyFlag type, bool
    requestSecondaryUpdate)': names the enum 'QQuick3DTexture::DirtyFlag',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DTexture.markDirty' has no cute function yet. Qt's 'void "
        "QQuick3DTexture::markDirty(DirtyFlag type, bool "
        "requestSecondaryUpdate)': names the enum "
        "'QQuick3DTexture::DirtyFlag', whose class cannot be named here.")
