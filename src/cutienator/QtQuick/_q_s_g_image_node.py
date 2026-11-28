"""
QSGImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgimagenode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QSGGeometryNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGImageNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGImageNode: a plain Python object standing in front
  of one C++ QSGImageNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGImageNode is built on
  Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGImageNode that has a ritual and that Python can
  call so far, 17 names in all: 'setRect', 'rect', 'setSourceRect',
  'sourceRect', 'setTexture', 'texture', 'setFiltering', 'filtering',
  'setMipmapFiltering', 'mipmapFiltering', 'setAnisotropyLevel',
  'anisotropyLevel', 'setTextureCoordinatesTransform',
  'textureCoordinatesTransform', 'setOwnsTexture', 'ownsTexture',
  'rebuildGeometry'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGImageNode::~QSGImageNode()': the destructor: Python never
    removes a C++ QSGImageNode.

  What to expect
  --------------

  - The C++ QSGImageNode is created at the first use, not by
    'QSGImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGImageNode.
  """

  #  The enums Qt writes inside QSGImageNode, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class TextureCoordinatesTransformFlag(CuteFlags):
    """
    The flags enum 'QSGImageNode::TextureCoordinatesTransformFlag' of Qt,
    with the 3 names Qt gives in it. Qt names the type of its combinations
    'QSGImageNode::TextureCoordinatesTransformMode'.
    """

    NoTransform = 0x0
    MirrorHorizontally = 0x1
    MirrorVertically = 0x2

  TextureCoordinatesTransformMode = TextureCoordinatesTransformFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QSGGeometry, QSGTexture, QRectF, QRectF,
      TextureCoordinatesTransformMode,
  )
  @overload(
      QSGGeometry, NoneType, QRectF, QRectF, TextureCoordinatesTransformMode,
  )
  @overload(
      NoneType, QSGTexture, QRectF, QRectF, TextureCoordinatesTransformMode,
  )
  @overload(
      NoneType, NoneType, QRectF, QRectF, TextureCoordinatesTransformMode,
  )
  def rebuildGeometry(
      g: Optional[QSGGeometry],
      texture: Optional[QSGTexture],
      rect: QRectF,
      sourceRect: QRectF,
      texCoordMode: TextureCoordinatesTransformMode,
  ) -> None:
    """
    Calls Qt's 'void QSGImageNode::rebuildGeometry(QSGGeometry *g, QSGTexture
    *texture, const QRectF &rect, QRectF sourceRect,
    TextureCoordinatesTransformMode texCoordMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#rebuildGeometry

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    texCoordMode : TextureCoordinatesTransformMode
      Passed on as its number.
    """
    #  void QSGImageNode::rebuildGeometry(QSGGeometry *g, QSGTexture
    #      *texture, const QRectF &rect, QRectF sourceRect,
    #      TextureCoordinatesTransformMode texCoordMode)
    Rituals.call(
        'ritual_ZN12QSGImageNode15rebuildGeometryEP11QSGGeometryP10QSGTextu'
        'reRK6QRectFS4_6QFlagsINS_31TextureCoordinatesTransformFlagEE',
        CuteMixin._addressOf(g), CuteMixin._addressOf(texture),
        CuteMixin._valueOf(rect), CuteMixin._valueOf(sourceRect),
        texCoordMode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGImageNode'

  #  A C++ QSGImageNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGImageNode'

  #  The functions Qt calls itself that QSGImageNode is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setRect': (
          ('_ZN12QSGImageNode7setRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'rect': (
          ('_ZNK12QSGImageNode4rectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'setSourceRect': (
          ('_ZN12QSGImageNode13setSourceRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'sourceRect': (
          ('_ZNK12QSGImageNode10sourceRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'setTexture': (
          ('_ZN12QSGImageNode10setTextureEP10QSGTexture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
           )),
      ),
      'texture': (
          ('_ZNK12QSGImageNode7textureEv',
           ('address', 'address', 'QtQuick:QSGTexture'),
           ()),
      ),
      'setFiltering': (
          ('_ZN12QSGImageNode12setFilteringEN10QSGTexture9FilteringE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'filtering': (
          ('_ZNK12QSGImageNode9filteringEv',
           ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           ()),
      ),
      'setMipmapFiltering': (
          ('_ZN12QSGImageNode18setMipmapFilteringEN10QSGTexture9FilteringE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'mipmapFiltering': (
          ('_ZNK12QSGImageNode15mipmapFilteringEv',
           ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           ()),
      ),
      'setAnisotropyLevel': (
          ('_ZN12QSGImageNode18setAnisotropyLevelEN10QSGTexture15Anisotropy'
           'LevelE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.AnisotropyLevel'),
           )),
      ),
      'anisotropyLevel': (
          ('_ZNK12QSGImageNode15anisotropyLevelEv',
           ('int', 'enum', 'QtQuick:QSGTexture.AnisotropyLevel'),
           ()),
      ),
      'setTextureCoordinatesTransform': (
          ('_ZN12QSGImageNode30setTextureCoordinatesTransformE6QFlagsINS_31'
           'TextureCoordinatesTransformFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtQuick:QSGImageNode.TextureCoordinatesTransformFlag'),
           )),
      ),
      'textureCoordinatesTransform': (
          ('_ZNK12QSGImageNode27textureCoordinatesTransformEv',
           ('int', 'flags',
            'QtQuick:QSGImageNode.TextureCoordinatesTransformFlag'),
           ()),
      ),
      'setOwnsTexture': (
          ('_ZN12QSGImageNode14setOwnsTextureEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'ownsTexture': (
          ('_ZNK12QSGImageNode11ownsTextureEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGImageNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGImageNode::rect() const
    address = self.uglySide.call('ritual_ZNK12QSGImageNode4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGImageNode::sourceRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGImageNode::sourceRect() const
    address = self.uglySide.call('ritual_ZNK12QSGImageNode10sourceRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGImageNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGImageNode::texture() const
    address = self.uglySide.call('ritual_ZNK12QSGImageNode7textureEv')
    return QSGTexture._cuteAt(address)

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGImageNode::filtering() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGImageNode::filtering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK12QSGImageNode9filteringEv',
    ))

  def mipmapFiltering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGImageNode::mipmapFiltering() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#mipmapFiltering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGImageNode::mipmapFiltering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK12QSGImageNode15mipmapFilteringEv',
    ))

  def anisotropyLevel(self) -> QSGTexture.AnisotropyLevel:
    """
    Calls Qt's 'QSGTexture::AnisotropyLevel QSGImageNode::anisotropyLevel()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#anisotropyLevel

    Returns
    -------

    QSGTexture.AnisotropyLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.AnisotropyLevel(number)' gives.
    """
    #  QSGTexture::AnisotropyLevel QSGImageNode::anisotropyLevel() const
    return QSGTexture.AnisotropyLevel(self.uglySide.call(
        'ritual_ZNK12QSGImageNode15anisotropyLevelEv',
    ))

  def textureCoordinatesTransform(self) -> TextureCoordinatesTransformMode:
    """
    Calls Qt's 'TextureCoordinatesTransformMode
    QSGImageNode::textureCoordinatesTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgimagenode.html#textureCoordinatesTransform

    Returns
    -------

    TextureCoordinatesTransformMode
      The value standing for the combination Qt gave back.
    """
    #  TextureCoordinatesTransformMode
    #      QSGImageNode::textureCoordinatesTransform() const
    return QSGImageNode.TextureCoordinatesTransformMode(self.uglySide.call(
        'ritual_ZNK12QSGImageNode27textureCoordinatesTransformEv',
    ))

  def ownsTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGImageNode::ownsTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#ownsTexture
    """
    #  bool QSGImageNode::ownsTexture() const
    return self.uglySide.call('ritual_ZNK12QSGImageNode11ownsTextureEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGImageNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGImageNode::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode7setRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGImageNode::setRect(qreal x, qreal y, qreal w, qreal
    h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QSGImageNode::setRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN12QSGImageNode7setRectEdddd', x, y, w, h)

  @overload(QRectF)
  def setSourceRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QSGImageNode::setSourceRect(const QRectF &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setSourceRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGImageNode::setSourceRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode13setSourceRectERK6QRectF', self._valueOf(r),
    )

  @overload(float, float, float, float)
  def setSourceRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGImageNode::setSourceRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setSourceRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QSGImageNode::setSourceRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode13setSourceRectEdddd', x, y, w, h,
    )

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGImageNode::setTexture(QSGTexture *texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGImageNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGImageNode::setFiltering(QSGTexture::Filtering filtering)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode12setFilteringEN10QSGTexture9FilteringE',
        filtering.value,
    )

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGImageNode::setMipmapFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgimagenode.html#setMipmapFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGImageNode::setMipmapFiltering(QSGTexture::Filtering filtering)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode18setMipmapFilteringEN10QSGTexture9Filterin'
        'gE',
        filtering.value,
    )

  @overload(QSGTexture.AnisotropyLevel)
  def setAnisotropyLevel(self, level: QSGTexture.AnisotropyLevel) -> None:
    """
    Calls Qt's 'void
    QSGImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgimagenode.html#setAnisotropyLevel

    Parameters
    ----------

    level : QSGTexture.AnisotropyLevel
      Passed on as its number.
    """
    #  void QSGImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
    #      level)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode18setAnisotropyLevelEN10QSGTexture15Anisotr'
        'opyLevelE',
        level.value,
    )

  @overload(TextureCoordinatesTransformMode)
  def setTextureCoordinatesTransform(
      self,
      mode: TextureCoordinatesTransformMode,
  ) -> None:
    """
    Calls Qt's 'void QSGImageNode::setTextureCoordinatesTransform(
    TextureCoordinatesTransformMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgimagenode.html#setTextureCoordinatesTransform

    Parameters
    ----------

    mode : TextureCoordinatesTransformMode
      Passed on as its number.
    """
    #  void QSGImageNode::setTextureCoordinatesTransform(
    #      TextureCoordinatesTransformMode mode)
    self.uglySide.call(
        'ritual_ZN12QSGImageNode30setTextureCoordinatesTransformE6QFlagsINS'
        '_31TextureCoordinatesTransformFlagEE',
        mode.value,
    )

  @overload(bool)
  def setOwnsTexture(self, owns: bool) -> None:
    """
    Calls Qt's 'void QSGImageNode::setOwnsTexture(bool owns)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgimagenode.html#setOwnsTexture

    Parameters
    ----------

    owns : bool
      Passed on as it is.
    """
    #  void QSGImageNode::setOwnsTexture(bool owns)
    self.uglySide.call('ritual_ZN12QSGImageNode14setOwnsTextureEb', owns)

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
