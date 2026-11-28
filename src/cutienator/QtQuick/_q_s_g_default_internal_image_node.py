"""
QSGDefaultInternalImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalimagenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDefaultInternalImageNode to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGBasicInternalImageNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QSGDefaultRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGDefaultRenderContext = WAIT['QSGDefaultRenderContext']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultInternalImageNode(QSGBasicInternalImageNode):
  """
  The cute side of Qt's QSGDefaultInternalImageNode: a plain Python object
  standing in front of one C++ QSGDefaultInternalImageNode.

  It is built on the cute 'QSGBasicInternalImageNode', as Qt's
  QSGDefaultInternalImageNode is built on Qt's QSGBasicInternalImageNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultInternalImageNode that has a ritual and
  that Python can call so far, 9 names in all: 'setMipmapFiltering',
  'setFiltering', 'setHorizontalWrapMode', 'setVerticalWrapMode',
  'updateMaterialAntialiasing', 'setMaterialTexture', 'materialTexture',
  'updateMaterialBlending', 'supportsWrap'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGDefaultInternalImageNode is created at the first use, not by
    'QSGDefaultInternalImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultInternalImageNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultInternalImageNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def materialTexture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGDefaultInternalImageNode::materialTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html#materialTexture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDefaultInternalImageNode::materialTexture() const
    ritual = 'ritual_ZNK27QSGDefaultInternalImageNode15materialTextureEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSGDefaultInternalImageNode15materialTextureEv')
    address = self.uglySide.call(ritual)
    return QSGTexture._cuteAt(address)

  @overload(QSize)
  def supportsWrap(self, size: QSize) -> bool:
    """
    Calls Qt's 'bool QSGDefaultInternalImageNode::supportsWrap(const QSize
    &size) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html#supportsWrap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool QSGDefaultInternalImageNode::supportsWrap(const QSize &size)
    #      const
    ritual = 'ritual_ZNK27QSGDefaultInternalImageNode12supportsWrapERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSGDefaultInternalImageNode12supportsWrapERK5QSi'
          'ze')
    return self.uglySide.call(ritual, self._valueOf(size))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGDefaultInternalImageNode::setMipmapFiltering(QSGTexture::
    #      Filtering filtering)
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode18setMipmapFilteringEN10QSGT'
        'exture9FilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode18setMipmapFilteringEN'
          '10QSGTexture9FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGDefaultInternalImageNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode12setFilteringEN10QSGTexture'
        '9FilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode12setFilteringEN10QSGT'
          'exture9FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.WrapMode)
  def setHorizontalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGDefaultInternalImageNode::setHorizontalWrapMode(QSGTexture::
    #      WrapMode wrapMode)
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode21setHorizontalWrapModeEN10Q'
        'SGTexture8WrapModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode21setHorizontalWrapMod'
          'eEN10QSGTexture8WrapModeE')
    self.uglySide.call(ritual, wrapMode.value)

  @overload(QSGTexture.WrapMode)
  def setVerticalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGDefaultInternalImageNode::setVerticalWrapMode(QSGTexture::
    #      WrapMode wrapMode)
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode19setVerticalWrapModeEN10QSG'
        'Texture8WrapModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode19setVerticalWrapModeE'
          'N10QSGTexture8WrapModeE')
    self.uglySide.call(ritual, wrapMode.value)

  @overload(QSGTexture)
  @overload(NoneType)
  def setMaterialTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::setMaterialTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultInternalImageNode::setMaterialTexture(QSGTexture
    #      *texture)
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode18setMaterialTextureEP10QSGT'
        'exture')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode18setMaterialTextureEP'
          '10QSGTexture')
    self.uglySide.call(ritual, self._addressOf(texture))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGDefaultRenderContext)
  @overload(NoneType)
  def __init__(self, rc: Optional[QSGDefaultRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGDefaultInternalImageNode::QSGDefaultInternalImageNode(
    QSGDefaultRenderContext *rc)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html

    Parameters
    ----------

    rc : Optional[QSGDefaultRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGDefaultInternalImageNode::QSGDefaultInternalImageNode(
    #      QSGDefaultRenderContext *rc)
    self._noteCreation(QSGDefaultInternalImageNode, lambda: Rituals.call(
        'ritual_ZN27QSGDefaultInternalImageNodeC1EP23QSGDefaultRenderContex'
        't',
        self._addressOf(rc),
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

  def updateMaterialAntialiasing(self) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalImageNode::updateMaterialAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html
    """
    #  void QSGDefaultInternalImageNode::updateMaterialAntialiasing()
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode26updateMaterialAntialiasing'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode26updateMaterialAntial'
          'iasingEv')
    self.uglySide.call(ritual)

  def updateMaterialBlending(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultInternalImageNode::updateMaterialBlending()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalimagenode.html
    """
    #  bool QSGDefaultInternalImageNode::updateMaterialBlending()
    ritual = (
        'ritual_ZN27QSGDefaultInternalImageNode22updateMaterialBlendingEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGDefaultInternalImageNode22updateMaterialBlendi'
          'ngEv')
    return self.uglySide.call(ritual)
