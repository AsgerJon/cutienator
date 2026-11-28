"""
QSGDefaultImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultimagenode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGDefaultImageNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGImageNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultImageNode(QSGImageNode):
  """
  The cute side of Qt's QSGDefaultImageNode: a plain Python object standing
  in front of one C++ QSGDefaultImageNode.

  It is built on the cute 'QSGImageNode', as Qt's QSGDefaultImageNode is
  built on Qt's QSGImageNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultImageNode that has a ritual and that
  Python can call so far, 16 names in all: 'setRect', 'rect',
  'setSourceRect', 'sourceRect', 'setTexture', 'texture', 'setFiltering',
  'filtering', 'setMipmapFiltering', 'mipmapFiltering', 'setAnisotropyLevel',
  'anisotropyLevel', 'setTextureCoordinatesTransform',
  'textureCoordinatesTransform', 'setOwnsTexture', 'ownsTexture'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDefaultImageNode::~QSGDefaultImageNode()': the destructor:
    Python never removes a C++ QSGDefaultImageNode.

  What to expect
  --------------

  - The C++ QSGDefaultImageNode is created at the first use, not by
    'QSGDefaultImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultImageNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultImageNode'

  #  A C++ QSGDefaultImageNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultImageNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGDefaultImageNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultimagenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGDefaultImageNode::rect() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGDefaultImageNode::sourceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGDefaultImageNode::sourceRect() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode10sourceRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode10sourceRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGDefaultImageNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultimagenode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDefaultImageNode::texture() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode7textureEv'
    address = self.uglySide.call(ritual)
    return QSGTexture._cuteAt(address)

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGDefaultImageNode::filtering()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultimagenode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGDefaultImageNode::filtering() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode9filteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode9filteringEv'
    return QSGTexture.Filtering(self.uglySide.call(ritual))

  def mipmapFiltering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGDefaultImageNode::mipmapFiltering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#mipmapFiltering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGDefaultImageNode::mipmapFiltering() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode15mipmapFilteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode15mipmapFilteringEv'
    return QSGTexture.Filtering(self.uglySide.call(ritual))

  def anisotropyLevel(self) -> QSGTexture.AnisotropyLevel:
    """
    Calls Qt's 'QSGTexture::AnisotropyLevel
    QSGDefaultImageNode::anisotropyLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#anisotropyLevel

    Returns
    -------

    QSGTexture.AnisotropyLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.AnisotropyLevel(number)' gives.
    """
    #  QSGTexture::AnisotropyLevel QSGDefaultImageNode::anisotropyLevel()
    #      const
    ritual = 'ritual_ZNK19QSGDefaultImageNode15anisotropyLevelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode15anisotropyLevelEv'
    return QSGTexture.AnisotropyLevel(self.uglySide.call(ritual))

  def textureCoordinatesTransform(
      self,
  ) -> QSGImageNode.TextureCoordinatesTransformMode:
    """
    Calls Qt's 'TextureCoordinatesTransformMode
    QSGDefaultImageNode::textureCoordinatesTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html

    Returns
    -------

    QSGImageNode.TextureCoordinatesTransformMode
      The value standing for the combination Qt gave back.
    """
    #  TextureCoordinatesTransformMode
    #      QSGDefaultImageNode::textureCoordinatesTransform() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode27textureCoordinatesTransformEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QSGDefaultImageNode27textureCoordinatesTransform'
          'Ev')
    return QSGImageNode.TextureCoordinatesTransformMode(self.uglySide.call(
        ritual,
    ))

  def ownsTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultImageNode::ownsTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#ownsTexture
    """
    #  bool QSGDefaultImageNode::ownsTexture() const
    ritual = 'ritual_ZNK19QSGDefaultImageNode11ownsTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultImageNode11ownsTextureEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGDefaultImageNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN19QSGDefaultImageNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultImageNode7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setSourceRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setSourceRect(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setSourceRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGDefaultImageNode::setSourceRect(const QRectF &r)
    ritual = 'ritual_ZN19QSGDefaultImageNode13setSourceRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultImageNode13setSourceRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultImageNode::setTexture(QSGTexture *texture)
    ritual = 'ritual_ZN19QSGDefaultImageNode10setTextureEP10QSGTexture'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultImageNode10setTextureEP10QSGTexture'
    self.uglySide.call(ritual, self._addressOf(texture))

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGDefaultImageNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN19QSGDefaultImageNode12setFilteringEN10QSGTexture9Filteri'
        'ngE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultImageNode12setFilteringEN10QSGTexture9F'
          'ilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGDefaultImageNode::setMipmapFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setMipmapFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGDefaultImageNode::setMipmapFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN19QSGDefaultImageNode18setMipmapFilteringEN10QSGTexture9F'
        'ilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultImageNode18setMipmapFilteringEN10QSGTex'
          'ture9FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.AnisotropyLevel)
  def setAnisotropyLevel(self, level: QSGTexture.AnisotropyLevel) -> None:
    """
    Calls Qt's 'void
    QSGDefaultImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setAnisotropyLevel

    Parameters
    ----------

    level : QSGTexture.AnisotropyLevel
      Passed on as its number.
    """
    #  void QSGDefaultImageNode::setAnisotropyLevel(QSGTexture::
    #      AnisotropyLevel level)
    ritual = (
        'ritual_ZN19QSGDefaultImageNode18setAnisotropyLevelEN10QSGTexture15'
        'AnisotropyLevelE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultImageNode18setAnisotropyLevelEN10QSGTex'
          'ture15AnisotropyLevelE')
    self.uglySide.call(ritual, level.value)

  @overload(QSGImageNode.TextureCoordinatesTransformMode)
  def setTextureCoordinatesTransform(
      self,
      mode: QSGImageNode.TextureCoordinatesTransformMode,
  ) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setTextureCoordinatesTransform(
    TextureCoordinatesTransformMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html

    Parameters
    ----------

    mode : QSGImageNode.TextureCoordinatesTransformMode
      Passed on as its number.
    """
    #  void QSGDefaultImageNode::setTextureCoordinatesTransform(
    #      TextureCoordinatesTransformMode mode)
    ritual = (
        'ritual_ZN19QSGDefaultImageNode30setTextureCoordinatesTransformE6QF'
        'lagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultImageNode30setTextureCoordinatesTransfo'
          'rmE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(bool)
  def setOwnsTexture(self, owns: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultImageNode::setOwnsTexture(bool owns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#setOwnsTexture

    Parameters
    ----------

    owns : bool
      Passed on as it is.
    """
    #  void QSGDefaultImageNode::setOwnsTexture(bool owns)
    ritual = 'ritual_ZN19QSGDefaultImageNode14setOwnsTextureEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultImageNode14setOwnsTextureEb'
    self.uglySide.call(ritual, owns)

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
    'QSGDefaultImageNode::QSGDefaultImageNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultimagenode.html#QSGDefaultImageNode
    """
    #  QSGDefaultImageNode::QSGDefaultImageNode()
    self._noteCreation(QSGDefaultImageNode, lambda: Rituals.call(
        'ritual_ZN19QSGDefaultImageNodeC1Ev',
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
