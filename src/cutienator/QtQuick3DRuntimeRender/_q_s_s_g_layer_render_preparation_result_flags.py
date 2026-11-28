"""
QSSGLayerRenderPreparationResultFlags binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLayerRenderPreparationResultFlags to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QSSGLayerRenderPreparationResultFlags(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLayerRenderPreparationResultFlags: a plain Python
  object standing in front of one C++ QSSGLayerRenderPreparationResultFlags.

  C++ hands a QSSGLayerRenderPreparationResultFlags around as a copy, so
  every C++ QSSGLayerRenderPreparationResultFlags behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGLayerRenderPreparationResultFlags that has a
  ritual and that Python can call so far, 24 names in all:
  'wasLayerDataDirty', 'setLayerDataDirty', 'wasDirty', 'setWasDirty',
  'requiresDepthTexture', 'setRequiresDepthTexture',
  'requiresDepthTextureMS', 'setRequiresDepthTextureMS', 'requiresSsaoPass',
  'setRequiresSsaoPass', 'requiresShadowMapPass', 'setRequiresShadowMapPass',
  'requiresScreenTexture', 'setRequiresScreenTexture',
  'requiresMipmapsForScreenTexture', 'setRequiresMipmapsForScreenTexture',
  'hasCustomBlendMode', 'setHasCustomBlendMode', 'requiresNormalTexture',
  'setRequiresNormalTexture', 'requiresMotionVectorPass',
  'setRequiresMotionVectorPass', 'requiresSkyMaterialPass',
  'setRequiresSkyMaterialPass'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLayerRenderPreparationResultFlags::
    ~QSSGLayerRenderPreparationResultFlags()': the destructor: Python removes
    its C++ QSSGLayerRenderPreparationResultFlags by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGLayerRenderPreparationResultFlags is created at the first
    use, not by 'QSSGLayerRenderPreparationResultFlags(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGLayerRenderPreparationResultFlags back gives a
    copy the ritual made for Python, in a new cute
    QSSGLayerRenderPreparationResultFlags.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGLayerRenderPreparationResultFlags'

  #  Qt's '~QSSGLayerRenderPreparationResultFlags()'. Naming it makes this a
  #  value class: Python owns every C++ QSSGLayerRenderPreparationResultFlags
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN37QSSGLayerRenderPreparationResultFlagsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def wasLayerDataDirty(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::wasLayerDataDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::wasLayerDataDirty() const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags17wasLayerDataDir'
        'tyEv',
    )

  def wasDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGLayerRenderPreparationResultFlags::wasDirty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::wasDirty() const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags8wasDirtyEv',
    )

  def requiresDepthTexture(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresDepthTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresDepthTexture()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags20requiresDepthTe'
        'xtureEv',
    )

  def requiresDepthTextureMS(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresDepthTextureMS() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresDepthTextureMS()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags22requiresDepthTe'
        'xtureMSEv',
    )

  def requiresSsaoPass(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresSsaoPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresSsaoPass() const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags16requiresSsaoPas'
        'sEv',
    )

  def requiresShadowMapPass(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresShadowMapPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresShadowMapPass()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags21requiresShadowM'
        'apPassEv',
    )

  def requiresScreenTexture(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresScreenTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresScreenTexture()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags21requiresScreenT'
        'extureEv',
    )

  def requiresMipmapsForScreenTexture(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresMipmapsForScreenTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::
    #      requiresMipmapsForScreenTexture() const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags31requiresMipmaps'
        'ForScreenTextureEv',
    )

  def hasCustomBlendMode(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::hasCustomBlendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::hasCustomBlendMode() const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags18hasCustomBlendM'
        'odeEv',
    )

  def requiresNormalTexture(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresNormalTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresNormalTexture()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags21requiresNormalT'
        'extureEv',
    )

  def requiresMotionVectorPass(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresMotionVectorPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresMotionVectorPass()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags24requiresMotionV'
        'ectorPassEv',
    )

  def requiresSkyMaterialPass(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGLayerRenderPreparationResultFlags::requiresSkyMaterialPass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html
    """
    #  bool QSSGLayerRenderPreparationResultFlags::requiresSkyMaterialPass()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QSSGLayerRenderPreparationResultFlags23requiresSkyMate'
        'rialPassEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setLayerDataDirty(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setLayerDataDirty(bool inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setLayerDataDirty(bool
    #      inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags17setLayerDataDirt'
        'yEb',
        inValue,
    )

  @overload(bool)
  def setWasDirty(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderPreparationResultFlags::setWasDirty(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setWasDirty(bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags11setWasDirtyEb',
        inValue,
    )

  @overload(bool)
  def setRequiresDepthTexture(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresDepthTexture(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresDepthTexture(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags23setRequiresDepth'
        'TextureEb',
        inValue,
    )

  @overload(bool)
  def setRequiresDepthTextureMS(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresDepthTextureMS(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresDepthTextureMS(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags25setRequiresDepth'
        'TextureMSEb',
        inValue,
    )

  @overload(bool)
  def setRequiresSsaoPass(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresSsaoPass(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresSsaoPass(bool
    #      inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags19setRequiresSsaoP'
        'assEb',
        inValue,
    )

  @overload(bool)
  def setRequiresShadowMapPass(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresShadowMapPass(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresShadowMapPass(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags24setRequiresShado'
        'wMapPassEb',
        inValue,
    )

  @overload(bool)
  def setRequiresScreenTexture(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresScreenTexture(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresScreenTexture(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags24setRequiresScree'
        'nTextureEb',
        inValue,
    )

  @overload(bool)
  def setRequiresMipmapsForScreenTexture(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderPreparationResultFlags::
    setRequiresMipmapsForScreenTexture(bool inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::
    #      setRequiresMipmapsForScreenTexture(bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags34setRequiresMipma'
        'psForScreenTextureEb',
        inValue,
    )

  @overload(bool)
  def setHasCustomBlendMode(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setHasCustomBlendMode(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setHasCustomBlendMode(bool
    #      inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags21setHasCustomBlen'
        'dModeEb',
        inValue,
    )

  @overload(bool)
  def setRequiresNormalTexture(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresNormalTexture(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::setRequiresNormalTexture(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags24setRequiresNorma'
        'lTextureEb',
        inValue,
    )

  @overload(bool)
  def setRequiresMotionVectorPass(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresMotionVectorPass(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderPreparationResultFlags::
    #      setRequiresMotionVectorPass(bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags27setRequiresMotio'
        'nVectorPassEb',
        inValue,
    )

  @overload(bool)
  def setRequiresSkyMaterialPass(self, inValue: bool) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderPreparationResultFlags::setRequiresSkyMaterialPass(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresultflags.html

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void
    #      QSSGLayerRenderPreparationResultFlags::setRequiresSkyMaterialPass(
    #      bool inValue)
    self.uglySide.call(
        'ritual_ZN37QSSGLayerRenderPreparationResultFlags26setRequiresSkyMa'
        'terialPassEb',
        inValue,
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
