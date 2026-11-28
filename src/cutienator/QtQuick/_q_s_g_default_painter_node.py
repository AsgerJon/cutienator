"""
QSGDefaultPainterNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultpainternode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDefaultPainterNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickPaintedItem, QSGPainterNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QColor, QImage
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultPainterNode(QSGPainterNode):
  """
  The cute side of Qt's QSGDefaultPainterNode: a plain Python object standing
  in front of one C++ QSGDefaultPainterNode.

  It is built on the cute 'QSGPainterNode', as Qt's QSGDefaultPainterNode is
  built on Qt's QSGPainterNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultPainterNode that has a ritual and that
  Python can call so far, 28 names in all: 'setPreferredRenderTarget',
  'setSize', 'size', 'setDirty', 'setOpaquePainting', 'opaquePainting',
  'setLinearFiltering', 'linearFiltering', 'setMipmapping', 'mipmapping',
  'setSmoothPainting', 'smoothPainting', 'setFillColor', 'fillColor',
  'setContentsScale', 'contentsScale', 'setFastFBOResizing',
  'fastFBOResizing', 'setTextureSize', 'textureSize', 'toImage', 'update',
  'paint', 'texture', 'updateTexture', 'updateGeometry',
  'updateRenderTarget', 'updateFBOSize'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDefaultPainterNode::~QSGDefaultPainterNode()': the destructor:
    Python never removes a C++ QSGDefaultPainterNode.

  What to expect
  --------------

  - The C++ QSGDefaultPainterNode is created at the first use, not by
    'QSGDefaultPainterNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultPainterNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultPainterNode'

  #  A C++ QSGDefaultPainterNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultPainterNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSGDefaultPainterNode::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGDefaultPainterNode::size() const
    address = self.uglySide.call('ritual_ZNK21QSGDefaultPainterNode4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def opaquePainting(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultPainterNode::opaquePainting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#opaquePainting
    """
    #  bool QSGDefaultPainterNode::opaquePainting() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode14opaquePaintingEv',
    )

  def linearFiltering(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultPainterNode::linearFiltering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#linearFiltering
    """
    #  bool QSGDefaultPainterNode::linearFiltering() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode15linearFilteringEv',
    )

  def mipmapping(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultPainterNode::mipmapping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#mipmapping
    """
    #  bool QSGDefaultPainterNode::mipmapping() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode10mipmappingEv',
    )

  def smoothPainting(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultPainterNode::smoothPainting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#smoothPainting
    """
    #  bool QSGDefaultPainterNode::smoothPainting() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode14smoothPaintingEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGDefaultPainterNode::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGDefaultPainterNode::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def contentsScale(self) -> float:
    """
    Calls Qt's 'qreal QSGDefaultPainterNode::contentsScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#contentsScale
    """
    #  qreal QSGDefaultPainterNode::contentsScale() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode13contentsScaleEv',
    )

  def fastFBOResizing(self) -> bool:
    """
    Calls Qt's 'bool QSGDefaultPainterNode::fastFBOResizing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#fastFBOResizing
    """
    #  bool QSGDefaultPainterNode::fastFBOResizing() const
    return self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode15fastFBOResizingEv',
    )

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGDefaultPainterNode::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGDefaultPainterNode::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGDefaultPainterNode11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGDefaultPainterNode::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGDefaultPainterNode::toImage() const
    ritual = 'ritual_ZNK21QSGDefaultPainterNode7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGDefaultPainterNode7toImageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGDefaultPainterNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDefaultPainterNode::texture() const
    ritual = 'ritual_ZNK21QSGDefaultPainterNode7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGDefaultPainterNode7textureEv'
    address = self.uglySide.call(ritual)
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPaintedItem.RenderTarget)
  def setPreferredRenderTarget(
      self,
      target: QQuickPaintedItem.RenderTarget,
  ) -> None:
    """
    Calls Qt's 'void
    QSGDefaultPainterNode::setPreferredRenderTarget(QQuickPaintedItem::
    RenderTarget target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html

    Parameters
    ----------

    target : QQuickPaintedItem.RenderTarget
      Passed on as its number.
    """
    #  void QSGDefaultPainterNode::setPreferredRenderTarget(
    #      QQuickPaintedItem::RenderTarget target)
    ritual = (
        'ritual_ZN21QSGDefaultPainterNode24setPreferredRenderTargetEN17QQui'
        'ckPaintedItem12RenderTargetE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGDefaultPainterNode24setPreferredRenderTargetEN'
          '17QQuickPaintedItem12RenderTargetE')
    self.uglySide.call(ritual, target.value)

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGDefaultPainterNode::setSize(const QSize &size)
    ritual = 'ritual_ZN21QSGDefaultPainterNode7setSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode7setSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload()
  @overload(QRect)
  def setDirty(self, dirtyRect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setDirty(const QRect
    &dirtyRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setDirty

    Parameters
    ----------

    dirtyRect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QSGDefaultPainterNode::setDirty(const QRect &dirtyRect)
    if dirtyRect is None:
      from ..QtCore import QRect
      dirtyRect = QRect()
    ritual = 'ritual_ZN21QSGDefaultPainterNode8setDirtyERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode8setDirtyERK5QRect'
    self.uglySide.call(ritual, self._valueOf(dirtyRect))

  @overload(bool)
  def setOpaquePainting(self, opaque: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setOpaquePainting(bool opaque)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setOpaquePainting

    Parameters
    ----------

    opaque : bool
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setOpaquePainting(bool opaque)
    ritual = 'ritual_ZN21QSGDefaultPainterNode17setOpaquePaintingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode17setOpaquePaintingEb'
    self.uglySide.call(ritual, opaque)

  @overload(bool)
  def setLinearFiltering(self, linearFiltering: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setLinearFiltering(bool
    linearFiltering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setLinearFiltering

    Parameters
    ----------

    linearFiltering : bool
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setLinearFiltering(bool linearFiltering)
    ritual = 'ritual_ZN21QSGDefaultPainterNode18setLinearFilteringEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode18setLinearFilteringEb'
    self.uglySide.call(ritual, linearFiltering)

  @overload(bool)
  def setMipmapping(self, mipmapping: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setMipmapping(bool mipmapping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setMipmapping

    Parameters
    ----------

    mipmapping : bool
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setMipmapping(bool mipmapping)
    ritual = 'ritual_ZN21QSGDefaultPainterNode13setMipmappingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode13setMipmappingEb'
    self.uglySide.call(ritual, mipmapping)

  @overload(bool)
  def setSmoothPainting(self, s: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setSmoothPainting(bool s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setSmoothPainting

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setSmoothPainting(bool s)
    ritual = 'ritual_ZN21QSGDefaultPainterNode17setSmoothPaintingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode17setSmoothPaintingEb'
    self.uglySide.call(ritual, s)

  @overload(QColor)
  def setFillColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setFillColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setFillColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDefaultPainterNode::setFillColor(const QColor &c)
    ritual = 'ritual_ZN21QSGDefaultPainterNode12setFillColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode12setFillColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(c))

  @overload(float)
  def setContentsScale(self, s: float) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setContentsScale(qreal s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setContentsScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setContentsScale(qreal s)
    ritual = 'ritual_ZN21QSGDefaultPainterNode16setContentsScaleEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode16setContentsScaleEd'
    self.uglySide.call(ritual, s)

  @overload(bool)
  def setFastFBOResizing(self, fastResizing: bool) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setFastFBOResizing(bool
    fastResizing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setFastFBOResizing

    Parameters
    ----------

    fastResizing : bool
      Passed on as it is.
    """
    #  void QSGDefaultPainterNode::setFastFBOResizing(bool fastResizing)
    ritual = 'ritual_ZN21QSGDefaultPainterNode18setFastFBOResizingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode18setFastFBOResizingEb'
    self.uglySide.call(ritual, fastResizing)

  @overload(QSize)
  def setTextureSize(self, textureSize: QSize) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::setTextureSize(const QSize
    &textureSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#setTextureSize

    Parameters
    ----------

    textureSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGDefaultPainterNode::setTextureSize(const QSize &textureSize)
    ritual = 'ritual_ZN21QSGDefaultPainterNode14setTextureSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGDefaultPainterNode14setTextureSizeERK5QSize')
    self.uglySide.call(ritual, self._valueOf(textureSize))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPaintedItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickPaintedItem]) -> None:
    """
    Notes what was given, for Qt's
    'QSGDefaultPainterNode::QSGDefaultPainterNode(QQuickPaintedItem *item)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#QSGDefaultPainterNode

    Parameters
    ----------

    item : Optional[QQuickPaintedItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGDefaultPainterNode::QSGDefaultPainterNode(QQuickPaintedItem *item)
    self._noteCreation(QSGDefaultPainterNode, lambda: Rituals.call(
        'ritual_ZN21QSGDefaultPainterNodeC1EP17QQuickPaintedItem',
        self._addressOf(item),
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

  def update(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#update
    """
    #  void QSGDefaultPainterNode::update()
    ritual = 'ritual_ZN21QSGDefaultPainterNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGDefaultPainterNode6updateEv'
    self.uglySide.call(ritual)

  def paint(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::paint()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultpainternode.html#paint
    """
    #  void QSGDefaultPainterNode::paint()
    self.uglySide.call('ritual_ZN21QSGDefaultPainterNode5paintEv')

  def updateTexture(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::updateTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#updateTexture
    """
    #  void QSGDefaultPainterNode::updateTexture()
    self.uglySide.call('ritual_ZN21QSGDefaultPainterNode13updateTextureEv')

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#updateGeometry
    """
    #  void QSGDefaultPainterNode::updateGeometry()
    self.uglySide.call('ritual_ZN21QSGDefaultPainterNode14updateGeometryEv')

  def updateRenderTarget(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::updateRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#updateRenderTarget
    """
    #  void QSGDefaultPainterNode::updateRenderTarget()
    self.uglySide.call(
        'ritual_ZN21QSGDefaultPainterNode18updateRenderTargetEv',
    )

  def updateFBOSize(self) -> None:
    """
    Calls Qt's 'void QSGDefaultPainterNode::updateFBOSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultpainternode.html#updateFBOSize
    """
    #  void QSGDefaultPainterNode::updateFBOSize()
    self.uglySide.call('ritual_ZN21QSGDefaultPainterNode13updateFBOSizeEv')
