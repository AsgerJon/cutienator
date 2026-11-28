"""
QSSGRenderShadowMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderShadowMap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiRenderPassDescriptor, QRhiShaderResourceBindings
  from ..QtGui import QRhiTexture, QRhiTextureRenderTarget
  from . import QSSGShadowMapEntry


class QSSGRenderShadowMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderShadowMap: a plain Python object standing
  in front of one C++ QSSGRenderShadowMap.

  What exists
  -----------

  Every function of Qt's QSSGRenderShadowMap that has a ritual and that
  Python can call so far, 8 names in all: 'releaseCachedResources',
  'shadowMapEntry', 'layerRenderTarget', 'layerRenderPassDescriptor',
  'shadowMapAtlasTexture', 'shadowMapBlueNoiseTexture',
  'shadowMapEntryCount', 'shadowClearSrb'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderShadowMap::QSSGRenderShadowMap(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGRenderShadowMap::~QSSGRenderShadowMap()': the destructor:
    Python never removes a C++ QSSGRenderShadowMap.
  - Qt's 'void QSSGRenderShadowMap::addShadowMaps(const QSSGShaderLightList
    &renderableLights)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGShadowMapEntry *QSSGRenderShadowMap::addShadowMap(quint32
    lightIdx, QSize size, QVector<QSSGShadowMapEntry::AtlasEntry>
    atlasEntries, quint32 csmNumSplits, QRhiTexture::Format format, bool
    isPointLight, const QString &renderNodeObjName)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderShadowMap is created at the first use, not by
    'QSSGRenderShadowMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderShadowMap.
  - Each name of Qt's QSSGRenderShadowMap that has no cute function yet,
    '__init__', 'addShadowMap', 'addShadowMaps', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderShadowMap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shadowMapAtlasTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRenderShadowMap::shadowMapAtlasTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#shadowMapAtlasTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRenderShadowMap::shadowMapAtlasTexture() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGRenderShadowMap21shadowMapAtlasTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def shadowMapBlueNoiseTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRenderShadowMap::shadowMapBlueNoiseTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#shadowMapBlueNoiseTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRenderShadowMap::shadowMapBlueNoiseTexture() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGRenderShadowMap25shadowMapBlueNoiseTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def shadowClearSrb(self) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QSSGRenderShadowMap::shadowClearSrb() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#shadowClearSrb

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QSSGRenderShadowMap::shadowClearSrb()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGRenderShadowMap14shadowClearSrbEv',
    )
    from ..QtGui import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

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
    Qt's 'QSSGRenderShadowMap::QSSGRenderShadowMap(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderShadowMap.__init__' has no cute function yet. Qt's "
        "'QSSGRenderShadowMap::QSSGRenderShadowMap(const "
        "QSSGRenderContextInterface &inContext)': takes a type Python has "
        "no way to hand over yet.")

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

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGRenderShadowMap::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#releaseCachedResources
    """
    #  void QSSGRenderShadowMap::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN19QSSGRenderShadowMap22releaseCachedResourcesEv',
    )

  @overload(int)
  def shadowMapEntry(self, lightIdx: int) -> Optional[QSSGShadowMapEntry]:
    """
    Calls Qt's 'QSSGShadowMapEntry *QSSGRenderShadowMap::shadowMapEntry(int
    lightIdx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#shadowMapEntry

    Parameters
    ----------

    lightIdx : int
      Passed on as it is.

    Returns
    -------

    Optional[QSSGShadowMapEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGShadowMapEntry *QSSGRenderShadowMap::shadowMapEntry(int lightIdx)
    address = self.uglySide.call(
        'ritual_ZN19QSSGRenderShadowMap14shadowMapEntryEi', lightIdx,
    )
    from . import QSSGShadowMapEntry
    return QSSGShadowMapEntry._cuteAt(address)

  @overload(int)
  def layerRenderTarget(
      self,
      layerIndex: int,
  ) -> Optional[QRhiTextureRenderTarget]:
    """
    Calls Qt's 'QRhiTextureRenderTarget
    *QSSGRenderShadowMap::layerRenderTarget(int layerIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#layerRenderTarget

    Parameters
    ----------

    layerIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTextureRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTextureRenderTarget *QSSGRenderShadowMap::layerRenderTarget(int
    #      layerIndex)
    address = self.uglySide.call(
        'ritual_ZN19QSSGRenderShadowMap17layerRenderTargetEi', layerIndex,
    )
    from ..QtGui import QRhiTextureRenderTarget
    return QRhiTextureRenderTarget._cuteAt(address)

  @overload(int)
  def layerRenderPassDescriptor(
      self,
      layerIndex: int,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QSSGRenderShadowMap::layerRenderPassDescriptor(int layerIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#layerRenderPassDescriptor

    Parameters
    ----------

    layerIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QSSGRenderShadowMap::layerRenderPassDescriptor(int layerIndex)
    address = self.uglySide.call(
        'ritual_ZN19QSSGRenderShadowMap25layerRenderPassDescriptorEi',
        layerIndex,
    )
    from ..QtGui import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def shadowMapEntryCount(self) -> int:
    """
    Calls Qt's 'qsizetype QSSGRenderShadowMap::shadowMapEntryCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadowmap.html#shadowMapEntryCount
    """
    #  qsizetype QSSGRenderShadowMap::shadowMapEntryCount()
    return self.uglySide.call(
        'ritual_ZN19QSSGRenderShadowMap19shadowMapEntryCountEv',
    )

  @staticmethod
  def addShadowMap(*__, **_) -> Never:
    """
    Qt's 'QSSGShadowMapEntry *QSSGRenderShadowMap::addShadowMap(quint32
    lightIdx, QSize size, QVector<QSSGShadowMapEntry::AtlasEntry>
    atlasEntries, quint32 csmNumSplits, QRhiTexture::Format format, bool
    isPointLight, const QString &renderNodeObjName)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderShadowMap.addShadowMap' has no cute function yet. Qt's "
        "'QSSGShadowMapEntry *QSSGRenderShadowMap::addShadowMap(quint32 "
        "lightIdx, QSize size, QVector<QSSGShadowMapEntry::AtlasEntry> "
        "atlasEntries, quint32 csmNumSplits, QRhiTexture::Format format, "
        "bool isPointLight, const QString &renderNodeObjName)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def addShadowMaps(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderShadowMap::addShadowMaps(const QSSGShaderLightList
    &renderableLights)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderShadowMap.addShadowMaps' has no cute function yet. Qt's "
        "'void QSSGRenderShadowMap::addShadowMaps(const QSSGShaderLightList "
        "&renderableLights)': takes a type Python has no way to hand over "
        "yet.")
