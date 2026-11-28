"""
QSGOpaqueTextureMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtexturematerial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSGMaterial, QSGRendererInterface, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterialShader, QSGMaterialType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGOpaqueTextureMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGOpaqueTextureMaterial: a plain Python object
  standing in front of one C++ QSGOpaqueTextureMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGOpaqueTextureMaterial is
  built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGOpaqueTextureMaterial that has a ritual and that
  Python can call so far, 15 names in all: 'type', 'createShader', 'compare',
  'setTexture', 'texture', 'setMipmapFiltering', 'mipmapFiltering',
  'setFiltering', 'filtering', 'setHorizontalWrapMode', 'horizontalWrapMode',
  'setVerticalWrapMode', 'verticalWrapMode', 'setAnisotropyLevel',
  'anisotropyLevel'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGOpaqueTextureMaterial is created at the first use, not by
    'QSGOpaqueTextureMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGOpaqueTextureMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGOpaqueTextureMaterial'

  #  A C++ QSGOpaqueTextureMaterial Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGOpaqueTextureMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGOpaqueTextureMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGOpaqueTextureMaterial::type() const
    ritual = 'ritual_ZNK24QSGOpaqueTextureMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGOpaqueTextureMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGOpaqueTextureMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader
    #      *QSGOpaqueTextureMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    ritual = (
        'ritual_ZNK24QSGOpaqueTextureMaterial12createShaderEN20QSGRendererI'
        'nterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QSGOpaqueTextureMaterial12createShaderEN20QSGRen'
          'dererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGOpaqueTextureMaterial::compare(const QSGMaterial
    *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK24QSGOpaqueTextureMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QSGOpaqueTextureMaterial7compareEPK11QSGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGOpaqueTextureMaterial::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGOpaqueTextureMaterial::texture() const
    address = self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial7textureEv',
    )
    return QSGTexture._cuteAt(address)

  def mipmapFiltering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering
    QSGOpaqueTextureMaterial::mipmapFiltering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#mipmapFiltering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGOpaqueTextureMaterial::mipmapFiltering()
    #      const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial15mipmapFilteringEv',
    ))

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGOpaqueTextureMaterial::filtering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGOpaqueTextureMaterial::filtering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial9filteringEv',
    ))

  def horizontalWrapMode(self) -> QSGTexture.WrapMode:
    """
    Calls Qt's 'QSGTexture::WrapMode
    QSGOpaqueTextureMaterial::horizontalWrapMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#horizontalWrapMode

    Returns
    -------

    QSGTexture.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.WrapMode(number)' gives.
    """
    #  QSGTexture::WrapMode QSGOpaqueTextureMaterial::horizontalWrapMode()
    #      const
    return QSGTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial18horizontalWrapModeEv',
    ))

  def verticalWrapMode(self) -> QSGTexture.WrapMode:
    """
    Calls Qt's 'QSGTexture::WrapMode
    QSGOpaqueTextureMaterial::verticalWrapMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#verticalWrapMode

    Returns
    -------

    QSGTexture.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.WrapMode(number)' gives.
    """
    #  QSGTexture::WrapMode QSGOpaqueTextureMaterial::verticalWrapMode()
    #      const
    return QSGTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial16verticalWrapModeEv',
    ))

  def anisotropyLevel(self) -> QSGTexture.AnisotropyLevel:
    """
    Calls Qt's 'QSGTexture::AnisotropyLevel
    QSGOpaqueTextureMaterial::anisotropyLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#anisotropyLevel

    Returns
    -------

    QSGTexture.AnisotropyLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.AnisotropyLevel(number)' gives.
    """
    #  QSGTexture::AnisotropyLevel
    #      QSGOpaqueTextureMaterial::anisotropyLevel() const
    return QSGTexture.AnisotropyLevel(self.uglySide.call(
        'ritual_ZNK24QSGOpaqueTextureMaterial15anisotropyLevelEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGOpaqueTextureMaterial::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGOpaqueTextureMaterial::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filteringType: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGOpaqueTextureMaterial::setMipmapFiltering(QSGTexture::Filtering
    filteringType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#setMipmapFiltering

    Parameters
    ----------

    filteringType : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void
    #      QSGOpaqueTextureMaterial::setMipmapFiltering(QSGTexture::Filtering
    #      filteringType)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial18setMipmapFilteringEN10QSGText'
        'ure9FilteringE',
        filteringType.value,
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filteringType: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGOpaqueTextureMaterial::setFiltering(QSGTexture::Filtering
    filteringType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#setFiltering

    Parameters
    ----------

    filteringType : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGOpaqueTextureMaterial::setFiltering(QSGTexture::Filtering
    #      filteringType)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial12setFilteringEN10QSGTexture9Fi'
        'lteringE',
        filteringType.value,
    )

  @overload(QSGTexture.WrapMode)
  def setHorizontalWrapMode(self, mode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGOpaqueTextureMaterial::setHorizontalWrapMode(QSGTexture::WrapMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html

    Parameters
    ----------

    mode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGOpaqueTextureMaterial::setHorizontalWrapMode(QSGTexture::
    #      WrapMode mode)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial21setHorizontalWrapModeEN10QSGT'
        'exture8WrapModeE',
        mode.value,
    )

  @overload(QSGTexture.WrapMode)
  def setVerticalWrapMode(self, mode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGOpaqueTextureMaterial::setVerticalWrapMode(QSGTexture::WrapMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#setVerticalWrapMode

    Parameters
    ----------

    mode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void
    #      QSGOpaqueTextureMaterial::setVerticalWrapMode(QSGTexture::WrapMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial19setVerticalWrapModeEN10QSGTex'
        'ture8WrapModeE',
        mode.value,
    )

  @overload(QSGTexture.AnisotropyLevel)
  def setAnisotropyLevel(self, level: QSGTexture.AnisotropyLevel) -> None:
    """
    Calls Qt's 'void
    QSGOpaqueTextureMaterial::setAnisotropyLevel(QSGTexture::AnisotropyLevel
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html#setAnisotropyLevel

    Parameters
    ----------

    level : QSGTexture.AnisotropyLevel
      Passed on as its number.
    """
    #  void QSGOpaqueTextureMaterial::setAnisotropyLevel(QSGTexture::
    #      AnisotropyLevel level)
    self.uglySide.call(
        'ritual_ZN24QSGOpaqueTextureMaterial18setAnisotropyLevelEN10QSGText'
        'ure15AnisotropyLevelE',
        level.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGOpaqueTextureMaterial::QSGOpaqueTextureMaterial()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopaquetexturematerial.html
    """
    #  QSGOpaqueTextureMaterial::QSGOpaqueTextureMaterial()
    self._noteCreation(QSGOpaqueTextureMaterial, lambda: Rituals.call(
        'ritual_ZN24QSGOpaqueTextureMaterialC1Ev',
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
