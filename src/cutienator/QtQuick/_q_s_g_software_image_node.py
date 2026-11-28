"""
QSGSoftwareImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareImageNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGImageNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareImageNode(QSGImageNode):
  """
  The cute side of Qt's QSGSoftwareImageNode: a plain Python object standing
  in front of one C++ QSGSoftwareImageNode.

  It is built on the cute 'QSGImageNode', as Qt's QSGSoftwareImageNode is
  built on Qt's QSGImageNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareImageNode that has a ritual and that
  Python can call so far, 16 names in all: 'setRect', 'rect',
  'setSourceRect', 'sourceRect', 'setTexture', 'texture', 'setFiltering',
  'filtering', 'setMipmapFiltering', 'mipmapFiltering', 'setAnisotropyLevel',
  'anisotropyLevel', 'setTextureCoordinatesTransform',
  'textureCoordinatesTransform', 'setOwnsTexture', 'ownsTexture'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwareImageNode::~QSGSoftwareImageNode()': the destructor:
    Python never removes a C++ QSGSoftwareImageNode.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 leans on 'QSGSoftwareLayer.

  What to expect
  --------------

  - The C++ QSGSoftwareImageNode is created at the first use, not by
    'QSGSoftwareImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareImageNode.
  - Each name of Qt's QSGSoftwareImageNode that has no cute function yet,
    'paint', 'updateCachedMirroredPixmap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareImageNode'

  #  A C++ QSGSoftwareImageNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareImageNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareImageNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareImageNode::rect() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareImageNode::sourceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareImageNode::sourceRect() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode10sourceRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode10sourceRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGSoftwareImageNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGSoftwareImageNode::texture() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode7textureEv'
    address = self.uglySide.call(ritual)
    return QSGTexture._cuteAt(address)

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGSoftwareImageNode::filtering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGSoftwareImageNode::filtering() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode9filteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode9filteringEv'
    return QSGTexture.Filtering(self.uglySide.call(ritual))

  def mipmapFiltering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGSoftwareImageNode::mipmapFiltering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#mipmapFiltering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGSoftwareImageNode::mipmapFiltering() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode15mipmapFilteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode15mipmapFilteringEv'
    return QSGTexture.Filtering(self.uglySide.call(ritual))

  def anisotropyLevel(self) -> QSGTexture.AnisotropyLevel:
    """
    Calls Qt's 'QSGTexture::AnisotropyLevel
    QSGSoftwareImageNode::anisotropyLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#anisotropyLevel

    Returns
    -------

    QSGTexture.AnisotropyLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.AnisotropyLevel(number)' gives.
    """
    #  QSGTexture::AnisotropyLevel QSGSoftwareImageNode::anisotropyLevel()
    #      const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode15anisotropyLevelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode15anisotropyLevelEv'
    return QSGTexture.AnisotropyLevel(self.uglySide.call(ritual))

  def textureCoordinatesTransform(
      self,
  ) -> QSGImageNode.TextureCoordinatesTransformMode:
    """
    Calls Qt's 'TextureCoordinatesTransformMode
    QSGSoftwareImageNode::textureCoordinatesTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html

    Returns
    -------

    QSGImageNode.TextureCoordinatesTransformMode
      The value standing for the combination Qt gave back.
    """
    #  TextureCoordinatesTransformMode
    #      QSGSoftwareImageNode::textureCoordinatesTransform() const
    ritual = (
        'ritual_ZNK20QSGSoftwareImageNode27textureCoordinatesTransformEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QSGSoftwareImageNode27textureCoordinatesTransfor'
          'mEv')
    return QSGImageNode.TextureCoordinatesTransformMode(self.uglySide.call(
        ritual,
    ))

  def ownsTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareImageNode::ownsTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#ownsTexture
    """
    #  bool QSGSoftwareImageNode::ownsTexture() const
    ritual = 'ritual_ZNK20QSGSoftwareImageNode11ownsTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareImageNode11ownsTextureEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareImageNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN20QSGSoftwareImageNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareImageNode7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setSourceRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setSourceRect(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setSourceRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareImageNode::setSourceRect(const QRectF &r)
    ritual = 'ritual_ZN20QSGSoftwareImageNode13setSourceRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareImageNode13setSourceRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
    ritual = 'ritual_ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture')
    self.uglySide.call(ritual, self._addressOf(texture))

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSoftwareImageNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN20QSGSoftwareImageNode12setFilteringEN10QSGTexture9Filter'
        'ingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareImageNode12setFilteringEN10QSGTexture9'
          'FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, a0: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareImageNode::setMipmapFiltering(QSGTexture::Filtering a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setMipmapFiltering

    Parameters
    ----------

    a0 : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSoftwareImageNode::setMipmapFiltering(QSGTexture::Filtering
    #      a0)
    ritual = (
        'ritual_ZN20QSGSoftwareImageNode18setMipmapFilteringEN10QSGTexture9'
        'FilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareImageNode18setMipmapFilteringEN10QSGTe'
          'xture9FilteringE')
    self.uglySide.call(ritual, a0.value)

  @overload(QSGTexture.AnisotropyLevel)
  def setAnisotropyLevel(self, a0: QSGTexture.AnisotropyLevel) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setAnisotropyLevel

    Parameters
    ----------

    a0 : QSGTexture.AnisotropyLevel
      Passed on as its number.
    """
    #  void QSGSoftwareImageNode::setAnisotropyLevel(QSGTexture::
    #      AnisotropyLevel a0)
    ritual = (
        'ritual_ZN20QSGSoftwareImageNode18setAnisotropyLevelEN10QSGTexture1'
        '5AnisotropyLevelE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareImageNode18setAnisotropyLevelEN10QSGTe'
          'xture15AnisotropyLevelE')
    self.uglySide.call(ritual, a0.value)

  @overload(QSGImageNode.TextureCoordinatesTransformMode)
  def setTextureCoordinatesTransform(
      self,
      transformNode: QSGImageNode.TextureCoordinatesTransformMode,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setTextureCoordinatesTransform(
    TextureCoordinatesTransformMode transformNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html

    Parameters
    ----------

    transformNode : QSGImageNode.TextureCoordinatesTransformMode
      Passed on as its number.
    """
    #  void QSGSoftwareImageNode::setTextureCoordinatesTransform(
    #      TextureCoordinatesTransformMode transformNode)
    ritual = (
        'ritual_ZN20QSGSoftwareImageNode30setTextureCoordinatesTransformE6Q'
        'FlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareImageNode30setTextureCoordinatesTransf'
          'ormE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE')
    self.uglySide.call(ritual, transformNode.value)

  @overload(bool)
  def setOwnsTexture(self, owns: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareImageNode::setOwnsTexture(bool owns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#setOwnsTexture

    Parameters
    ----------

    owns : bool
      Passed on as it is.
    """
    #  void QSGSoftwareImageNode::setOwnsTexture(bool owns)
    ritual = 'ritual_ZN20QSGSoftwareImageNode14setOwnsTextureEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareImageNode14setOwnsTextureEb'
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
    'QSGSoftwareImageNode::QSGSoftwareImageNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareimagenode.html#QSGSoftwareImageNode
    """
    #  QSGSoftwareImageNode::QSGSoftwareImageNode()
    self._noteCreation(QSGSoftwareImageNode, lambda: Rituals.call(
        'ritual_ZN20QSGSoftwareImageNodeC1Ev',
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

  @staticmethod
  def paint(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareImageNode::paint(QPainter *painter)': leans on
    'QSGSoftwareLayer::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareImageNode.paint' has no cute function yet. Qt's 'void "
        "QSGSoftwareImageNode::paint(QPainter *painter)': leans on "
        "'QSGSoftwareLayer::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateCachedMirroredPixmap(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareImageNode::updateCachedMirroredPixmap()': leans on
    'QSGSoftwareLayer::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareImageNode.updateCachedMirroredPixmap' has no cute "
        "function yet. Qt's 'void "
        "QSGSoftwareImageNode::updateCachedMirroredPixmap()': leans on "
        "'QSGSoftwareLayer::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
