"""
QQuickShapeConicalGradientMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeConicalGradientMaterial to be private: it declares the
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickShapeGenericStrokeFillNode = WAIT['QQuickShapeGenericStrokeFillNode']
  QSGMaterial = WAIT['QSGMaterial']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeConicalGradientMaterial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapeConicalGradientMaterial: a plain Python
  object standing in front of one C++ QQuickShapeConicalGradientMaterial.

  What exists
  -----------

  Every function of Qt's QQuickShapeConicalGradientMaterial that has a ritual
  and that Python can call so far, 4 names in all: 'type', 'compare',
  'createShader', 'node'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QQuickShapeConicalGradientMaterial is created at the first use,
    not by 'QQuickShapeConicalGradientMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeConicalGradientMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeConicalGradientMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QQuickShapeConicalGradientMaterial::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradientmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QQuickShapeConicalGradientMaterial::type() const
    ritual = 'ritual_ZNK34QQuickShapeConicalGradientMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK34QQuickShapeConicalGradientMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QQuickShapeConicalGradientMaterial::compare(const
    QSGMaterial *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradientmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickShapeConicalGradientMaterial::compare(const QSGMaterial
    #      *other) const
    ritual = (
        'ritual_ZNK34QQuickShapeConicalGradientMaterial7compareEPK11QSGMate'
        'rial')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QQuickShapeConicalGradientMaterial7compareEPK11Q'
          'SGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QQuickShapeConicalGradientMaterial::createShader(QSGRendererInterface::
    RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradientmaterial.html

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
    #  QSGMaterialShader *QQuickShapeConicalGradientMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    ritual = (
        'ritual_ZNK34QQuickShapeConicalGradientMaterial12createShaderEN20QS'
        'GRendererInterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QQuickShapeConicalGradientMaterial12createShader'
          'EN20QSGRendererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from ..QtQuick import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  def node(self) -> Optional[QQuickShapeGenericStrokeFillNode]:
    """
    Calls Qt's 'QQuickShapeGenericStrokeFillNode
    *QQuickShapeConicalGradientMaterial::node() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradientmaterial.html#node

    Returns
    -------

    Optional[QQuickShapeGenericStrokeFillNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGenericStrokeFillNode
    #      *QQuickShapeConicalGradientMaterial::node() const
    address = self.uglySide.call(
        'ritual_ZNK34QQuickShapeConicalGradientMaterial4nodeEv',
    )
    from . import QQuickShapeGenericStrokeFillNode
    return QQuickShapeGenericStrokeFillNode._cuteAt(address)

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

  @overload(QQuickShapeGenericStrokeFillNode)
  @overload(NoneType)
  def __init__(
      self,
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickShapeConicalGradientMaterial::QQuickShapeConicalGradientMaterial(
    QQuickShapeGenericStrokeFillNode *node)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradientmaterial.html

    Parameters
    ----------

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickShapeConicalGradientMaterial::
    #      QQuickShapeConicalGradientMaterial(
    #      QQuickShapeGenericStrokeFillNode *node)
    self._noteCreation(
        QQuickShapeConicalGradientMaterial, lambda: Rituals.call(
            'ritual_ZN34QQuickShapeConicalGradientMaterialC1EP32QQuickShape'
            'GenericStrokeFillNode',
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
