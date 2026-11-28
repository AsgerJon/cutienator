"""
QSGTextureMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtexturematerial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSGOpaqueTextureMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterialShader, QSGMaterialType


class QSGTextureMaterial(QSGOpaqueTextureMaterial):
  """
  The cute side of Qt's QSGTextureMaterial: a plain Python object standing in
  front of one C++ QSGTextureMaterial.

  It is built on the cute 'QSGOpaqueTextureMaterial', as Qt's
  QSGTextureMaterial is built on Qt's QSGOpaqueTextureMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTextureMaterial that has a ritual and that Python
  can call so far, 2 names in all: 'type', 'createShader'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What to expect
  --------------

  - The C++ QSGTextureMaterial is created at the first use, not by
    'QSGTextureMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTextureMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTextureMaterial'

  #  A C++ QSGTextureMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTextureMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGTextureMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexturematerial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGTextureMaterial::type() const
    ritual = 'ritual_ZNK18QSGTextureMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGTextureMaterial4typeEv'
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
    *QSGTextureMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexturematerial.html#createShader

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
    #      *QSGTextureMaterial::createShader(QSGRendererInterface::RenderMode
    #      renderMode) const
    ritual = (
        'ritual_ZNK18QSGTextureMaterial12createShaderEN20QSGRendererInterfa'
        'ce10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGTextureMaterial12createShaderEN20QSGRendererI'
          'nterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

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
