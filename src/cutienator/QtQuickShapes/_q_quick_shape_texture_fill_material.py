"""
QQuickShapeTextureFillMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeTextureFillMaterial to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickShapeGenericStrokeFillNode
  from ..QtQuick import QSGMaterial, QSGMaterialShader, QSGMaterialType
  from ..QtQuick import QSGPlainTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickShapeGenericStrokeFillNode = WAIT['QQuickShapeGenericStrokeFillNode']
  QSGMaterial = WAIT['QSGMaterial']
  QSGPlainTexture = WAIT['QSGPlainTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeTextureFillMaterial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapeTextureFillMaterial: a plain Python object
  standing in front of one C++ QQuickShapeTextureFillMaterial.

  What exists
  -----------

  Every function of Qt's QQuickShapeTextureFillMaterial that has a ritual and
  that Python can call so far, 6 names in all: 'type', 'compare',
  'createShader', 'node', 'dummyTexture', 'setDummyTexture'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickShapeTextureFillMaterial::~QQuickShapeTextureFillMaterial()':
    the destructor: Python never removes a C++
    QQuickShapeTextureFillMaterial.

  What to expect
  --------------

  - The C++ QQuickShapeTextureFillMaterial is created at the first use, not
    by 'QQuickShapeTextureFillMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeTextureFillMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeTextureFillMaterial'

  #  A C++ QQuickShapeTextureFillMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeTextureFillMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QQuickShapeTextureFillMaterial::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
    ritual = 'ritual_ZNK30QQuickShapeTextureFillMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QQuickShapeTextureFillMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QQuickShapeTextureFillMaterial::compare(const QSGMaterial
    *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other)
    #      const
    ritual = (
        'ritual_ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMaterial')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMa'
          'terial')
    return self.uglySide.call(ritual, self._addressOf(other))

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QQuickShapeTextureFillMaterial::createShader(QSGRendererInterface::
    RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html#createShader

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
    #  QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    ritual = (
        'ritual_ZNK30QQuickShapeTextureFillMaterial12createShaderEN20QSGRen'
        'dererInterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickShapeTextureFillMaterial12createShaderEN20'
          'QSGRendererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from ..QtQuick import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  def node(self) -> Optional[QQuickShapeGenericStrokeFillNode]:
    """
    Calls Qt's 'QQuickShapeGenericStrokeFillNode
    *QQuickShapeTextureFillMaterial::node() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html#node

    Returns
    -------

    Optional[QQuickShapeGenericStrokeFillNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGenericStrokeFillNode
    #      *QQuickShapeTextureFillMaterial::node() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickShapeTextureFillMaterial4nodeEv',
    )
    from . import QQuickShapeGenericStrokeFillNode
    return QQuickShapeGenericStrokeFillNode._cuteAt(address)

  def dummyTexture(self) -> Optional[QSGPlainTexture]:
    """
    Calls Qt's 'QSGPlainTexture
    *QQuickShapeTextureFillMaterial::dummyTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html#dummyTexture

    Returns
    -------

    Optional[QSGPlainTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGPlainTexture *QQuickShapeTextureFillMaterial::dummyTexture() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickShapeTextureFillMaterial12dummyTextureEv',
    )
    from ..QtQuick import QSGPlainTexture
    return QSGPlainTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGPlainTexture)
  @overload(NoneType)
  def setDummyTexture(self, texture: Optional[QSGPlainTexture]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeTextureFillMaterial::setDummyTexture(QSGPlainTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html

    Parameters
    ----------

    texture : Optional[QSGPlainTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeTextureFillMaterial::setDummyTexture(QSGPlainTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN30QQuickShapeTextureFillMaterial15setDummyTextureEP15QSGP'
        'lainTexture',
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

  @overload(QQuickShapeGenericStrokeFillNode)
  @overload(NoneType)
  def __init__(
      self,
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickShapeTextureFillMaterial::QQuickShapeTextureFillMaterial(
    QQuickShapeGenericStrokeFillNode *node)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapetexturefillmaterial.html

    Parameters
    ----------

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickShapeTextureFillMaterial::QQuickShapeTextureFillMaterial(
    #      QQuickShapeGenericStrokeFillNode *node)
    self._noteCreation(QQuickShapeTextureFillMaterial, lambda: Rituals.call(
        'ritual_ZN30QQuickShapeTextureFillMaterialC1EP32QQuickShapeGenericS'
        'trokeFillNode',
        self._addressOf(node),
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
