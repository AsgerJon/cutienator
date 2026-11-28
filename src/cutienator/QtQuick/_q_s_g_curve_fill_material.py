"""
QSGCurveFillMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGCurveFillMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGCurveFillNode, QSGMaterialShader, QSGMaterialType
  from . import QSGPlainTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGCurveFillNode = WAIT['QSGCurveFillNode']
  QSGPlainTexture = WAIT['QSGPlainTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCurveFillMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGCurveFillMaterial: a plain Python object standing
  in front of one C++ QSGCurveFillMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGCurveFillMaterial is
  built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCurveFillMaterial that has a ritual and that
  Python can call so far, 6 names in all: 'compare', 'node', 'dummyTexture',
  'setDummyTexture', 'type', 'createShader'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGCurveFillMaterial::~QSGCurveFillMaterial()': the destructor:
    Python never removes a C++ QSGCurveFillMaterial.

  What to expect
  --------------

  - The C++ QSGCurveFillMaterial is created at the first use, not by
    'QSGCurveFillMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCurveFillMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCurveFillMaterial'

  #  A C++ QSGCurveFillMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCurveFillMaterial'

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
    Calls Qt's 'int QSGCurveFillMaterial::compare(const QSGMaterial *other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGCurveFillMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK20QSGCurveFillMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCurveFillMaterial7compareEPK11QSGMaterial'
    return self.uglySide.call(ritual, self._addressOf(other))

  def node(self) -> Optional[QSGCurveFillNode]:
    """
    Calls Qt's 'QSGCurveFillNode *QSGCurveFillMaterial::node() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#node

    Returns
    -------

    Optional[QSGCurveFillNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGCurveFillNode *QSGCurveFillMaterial::node() const
    address = self.uglySide.call('ritual_ZNK20QSGCurveFillMaterial4nodeEv')
    from . import QSGCurveFillNode
    return QSGCurveFillNode._cuteAt(address)

  def dummyTexture(self) -> Optional[QSGPlainTexture]:
    """
    Calls Qt's 'QSGPlainTexture *QSGCurveFillMaterial::dummyTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#dummyTexture

    Returns
    -------

    Optional[QSGPlainTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGPlainTexture *QSGCurveFillMaterial::dummyTexture() const
    address = self.uglySide.call(
        'ritual_ZNK20QSGCurveFillMaterial12dummyTextureEv',
    )
    from . import QSGPlainTexture
    return QSGPlainTexture._cuteAt(address)

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGCurveFillMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGCurveFillMaterial::type() const
    ritual = 'ritual_ZNK20QSGCurveFillMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGCurveFillMaterial4typeEv'
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
    *QSGCurveFillMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#createShader

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
    #      *QSGCurveFillMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    ritual = (
        'ritual_ZNK20QSGCurveFillMaterial12createShaderEN20QSGRendererInter'
        'face10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QSGCurveFillMaterial12createShaderEN20QSGRendere'
          'rInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGPlainTexture)
  @overload(NoneType)
  def setDummyTexture(self, dummyTexture: Optional[QSGPlainTexture]) -> None:
    """
    Calls Qt's 'void QSGCurveFillMaterial::setDummyTexture(QSGPlainTexture
    *dummyTexture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#setDummyTexture

    Parameters
    ----------

    dummyTexture : Optional[QSGPlainTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGCurveFillMaterial::setDummyTexture(QSGPlainTexture
    #      *dummyTexture)
    self.uglySide.call(
        'ritual_ZN20QSGCurveFillMaterial15setDummyTextureEP15QSGPlainTextur'
        'e',
        self._addressOf(dummyTexture),
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

  @overload(QSGCurveFillNode)
  @overload(NoneType)
  def __init__(self, node: Optional[QSGCurveFillNode]) -> None:
    """
    Notes what was given, for Qt's
    'QSGCurveFillMaterial::QSGCurveFillMaterial(QSGCurveFillNode *node)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillmaterial.html#QSGCurveFillMaterial

    Parameters
    ----------

    node : Optional[QSGCurveFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGCurveFillMaterial::QSGCurveFillMaterial(QSGCurveFillNode *node)
    self._noteCreation(QSGCurveFillMaterial, lambda: Rituals.call(
        'ritual_ZN20QSGCurveFillMaterialC1EP16QSGCurveFillNode',
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
