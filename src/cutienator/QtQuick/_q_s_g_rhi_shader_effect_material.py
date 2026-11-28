"""
QSGRhiShaderEffectMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiShaderEffectMaterial to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSGMaterialShader, QSGMaterialType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiShaderEffectMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGRhiShaderEffectMaterial: a plain Python object
  standing in front of one C++ QSGRhiShaderEffectMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGRhiShaderEffectMaterial
  is built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiShaderEffectMaterial that has a ritual and
  that Python can call so far, 5 names in all: 'compare', 'type',
  'createShader', 'updateTextureProviders', 'usesSubRectUniform'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QSGRhiShaderEffectMaterial.

  What to expect
  --------------

  - The C++ QSGRhiShaderEffectMaterial is created at the first use, not by
    'QSGRhiShaderEffectMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiShaderEffectMaterial.
  - Each name of Qt's QSGRhiShaderEffectMaterial that has no cute function
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
  __qt_class__ = 'QSGRhiShaderEffectMaterial'

  #  A C++ QSGRhiShaderEffectMaterial Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiShaderEffectMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGRhiShaderEffectMaterial::compare(const QSGMaterial
    *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGRhiShaderEffectMaterial::compare(const QSGMaterial *other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QSGRhiShaderEffectMaterial7compareEPK11QSGMaterial',
        self._addressOf(other),
    )

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGRhiShaderEffectMaterial::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGRhiShaderEffectMaterial::type() const
    ritual = 'ritual_ZNK26QSGRhiShaderEffectMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QSGRhiShaderEffectMaterial4typeEv'
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
    *QSGRhiShaderEffectMaterial::createShader(QSGRendererInterface::
    RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectmaterial.html#createShader

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
    #      *QSGRhiShaderEffectMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK26QSGRhiShaderEffectMaterial12createShaderEN20QSGRendere'
        'rInterface10RenderModeE',
        renderMode.value,
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(int)
  def usesSubRectUniform(self, binding: int) -> bool:
    """
    Calls Qt's 'bool QSGRhiShaderEffectMaterial::usesSubRectUniform(int
    binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectmaterial.html#usesSubRectUniform

    Parameters
    ----------

    binding : int
      Passed on as it is.
    """
    #  bool QSGRhiShaderEffectMaterial::usesSubRectUniform(int binding) const
    return self.uglySide.call(
        'ritual_ZNK26QSGRhiShaderEffectMaterial18usesSubRectUniformEi',
        binding,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGRhiShaderEffectMaterial::QSGRhiShaderEffectMaterial(
    QSGRhiShaderEffectNode *node)': leans on
    'QSGRhiShaderEffectMaterial::~QSGRhiShaderEffectMaterial()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiShaderEffectMaterial.__init__' has no cute function yet. "
        "Qt's "
        "'QSGRhiShaderEffectMaterial::QSGRhiShaderEffectMaterial(QSGRhiShade"
        "rEffectNode *node)': leans on "
        "'QSGRhiShaderEffectMaterial::~QSGRhiShaderEffectMaterial()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(bool)
  def updateTextureProviders(self, layoutChange: bool) -> None:
    """
    Calls Qt's 'void QSGRhiShaderEffectMaterial::updateTextureProviders(bool
    layoutChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectmaterial.html

    Parameters
    ----------

    layoutChange : bool
      Passed on as it is.
    """
    #  void QSGRhiShaderEffectMaterial::updateTextureProviders(bool
    #      layoutChange)
    self.uglySide.call(
        'ritual_ZN26QSGRhiShaderEffectMaterial22updateTextureProvidersEb',
        layoutChange,
    )
