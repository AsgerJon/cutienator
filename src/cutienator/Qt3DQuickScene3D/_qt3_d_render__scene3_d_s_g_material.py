"""
Qt3DRender::Scene3DSGMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgmaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Scene3DSGMaterial to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QSGMaterial

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene3DSGMaterial(QSGMaterial):
  """
  The cute side of Qt's Qt3DRender::Scene3DSGMaterial: a plain Python object
  standing in front of one C++ Qt3DRender::Scene3DSGMaterial.

  It is built on the cute 'QSGMaterial', as Qt's
  Qt3DRender::Scene3DSGMaterial is built on Qt's QSGMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Scene3DSGMaterial that has a ritual and
  that Python can call so far, 4 names in all: 'setTexture', 'texture',
  'show', 'visible'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 2 leans on 'Qt3DRender; 1 leans on
  'vtable for Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Scene3DSGMaterial is created at the first use, not by
    'Qt3DRender::Scene3DSGMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Scene3DSGMaterial.
  - Each name of Qt's Qt3DRender::Scene3DSGMaterial that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Scene3DSGMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *Qt3DRender::Scene3DSGMaterial::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgmaterial.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *Qt3DRender::Scene3DSGMaterial::texture() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17Scene3DSGMaterial7textureEv',
    )
    from ..QtQuick import QSGTexture
    return QSGTexture._cuteAt(address)

  def visible(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DSGMaterial::visible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgmaterial.html#visible
    """
    #  bool Qt3DRender::Scene3DSGMaterial::visible() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17Scene3DSGMaterial7visibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DSGMaterial::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgmaterial.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DSGMaterial::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17Scene3DSGMaterial10setTextureEP10QSGTexture',
        self._addressOf(texture),
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
    Qt's 'Qt3DRender::Scene3DSGMaterial::Scene3DSGMaterial()': leans on
    'Qt3DRender::Scene3DSGMaterialShader::type', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DSGMaterial.__init__' has no cute function yet. "
        "Qt's 'Qt3DRender::Scene3DSGMaterial::Scene3DSGMaterial()': leans "
        "on 'Qt3DRender::Scene3DSGMaterialShader::type', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def show(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DSGMaterial::show()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgmaterial.html#show
    """
    #  void Qt3DRender::Scene3DSGMaterial::show()
    self.uglySide.call('ritual_ZN10Qt3DRender17Scene3DSGMaterial4showEv')
