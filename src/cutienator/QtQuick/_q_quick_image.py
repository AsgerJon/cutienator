"""
QQuickImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickimage_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickImage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickImageBase, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QQuickImagePrivate, QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImage(QQuickImageBase):
  """
  The cute side of Qt's QQuickImage: a plain Python object standing in front
  of one C++ QQuickImage.

  It is built on the cute 'QQuickImageBase', as Qt's QQuickImage is built on
  Qt's QQuickImageBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImage that has a ritual and that Python can
  call so far, 29 names in all: 'metaObject', 'tr', 'fillMode',
  'setFillMode', 'paintedWidth', 'paintedHeight', 'boundingRect',
  'horizontalAlignment', 'setHorizontalAlignment', 'verticalAlignment',
  'setVerticalAlignment', 'isTextureProvider', 'textureProvider', 'mipmap',
  'setMipmap', 'emitAutoTransformBaseChanged', 'fillModeChanged',
  'paintedGeometryChanged', 'horizontalAlignmentChanged',
  'verticalAlignmentChanged', 'mipmapChanged', 'autoTransformChanged',
  'invalidateSceneGraph', 'pixmapChange', 'updatePaintedGeometry',
  'releaseResources', 'geometryChange', 'updatePaintNode', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImage::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickImage::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickImage::~QQuickImage()': the destructor: Python never removes
    a C++ QQuickImage.
  - Qt's 'QQuickImage::QQuickImage(QQuickImagePrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickImagePrivate *QQuickImage::d_func() const': takes in
    Python what 'QQuickImagePrivate *QQuickImage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickImage is created at the first use, not by
    'QQuickImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImage.
  - Qt tells when it has removed the C++ QQuickImage. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickImage, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FillMode(CuteNum):
    """
    The enum 'QQuickImage::FillMode' of Qt, with the 7 names Qt gives in it.
    """

    Stretch = Kee[int](0)
    PreserveAspectFit = Kee[int](1)
    PreserveAspectCrop = Kee[int](2)
    Tile = Kee[int](3)
    TileVertically = Kee[int](4)
    TileHorizontally = Kee[int](5)
    Pad = Kee[int](6)

  class HAlignment(CuteNum):
    """
    The enum 'QQuickImage::HAlignment' of Qt, with the 3 names Qt gives in
    it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickImage::VAlignment' of Qt, with the 3 names Qt gives in
    it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickImage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImage'

  #  A C++ QQuickImage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImage::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickImage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fillMode(self) -> FillMode:
    """
    Calls Qt's 'FillMode QQuickImage::fillMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#fillMode

    Returns
    -------

    FillMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FillMode(number)' gives.
    """
    #  FillMode QQuickImage::fillMode() const
    return QQuickImage.FillMode(self.uglySide.call(
        'ritual_ZNK11QQuickImage8fillModeEv',
    ))

  def paintedWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickImage::paintedWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#paintedWidth
    """
    #  qreal QQuickImage::paintedWidth() const
    return self.uglySide.call('ritual_ZNK11QQuickImage12paintedWidthEv')

  def paintedHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickImage::paintedHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#paintedHeight
    """
    #  qreal QQuickImage::paintedHeight() const
    return self.uglySide.call('ritual_ZNK11QQuickImage13paintedHeightEv')

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickImage::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickImage::boundingRect() const
    ritual = 'ritual_ZNK11QQuickImage12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickImage12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def horizontalAlignment(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickImage::horizontalAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#horizontalAlignment

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickImage::horizontalAlignment() const
    return QQuickImage.HAlignment(self.uglySide.call(
        'ritual_ZNK11QQuickImage19horizontalAlignmentEv',
    ))

  def verticalAlignment(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickImage::verticalAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#verticalAlignment

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickImage::verticalAlignment() const
    return QQuickImage.VAlignment(self.uglySide.call(
        'ritual_ZNK11QQuickImage17verticalAlignmentEv',
    ))

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickImage::isTextureProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#isTextureProvider
    """
    #  bool QQuickImage::isTextureProvider() const
    ritual = 'ritual_ZNK11QQuickImage17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickImage17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuickImage::textureProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickImage::textureProvider() const
    ritual = 'ritual_ZNK11QQuickImage15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickImage15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def mipmap(self) -> bool:
    """
    Calls Qt's 'bool QQuickImage::mipmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#mipmap
    """
    #  bool QQuickImage::mipmap() const
    return self.uglySide.call('ritual_ZNK11QQuickImage6mipmapEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FillMode)
  def setFillMode(self, a0: FillMode) -> None:
    """
    Calls Qt's 'void QQuickImage::setFillMode(FillMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#setFillMode

    Parameters
    ----------

    a0 : FillMode
      Passed on as its number.
    """
    #  void QQuickImage::setFillMode(FillMode a0)
    self.uglySide.call(
        'ritual_ZN11QQuickImage11setFillModeENS_8FillModeE', a0.value,
    )

  @overload(HAlignment)
  def setHorizontalAlignment(self, align: HAlignment) -> None:
    """
    Calls Qt's 'void QQuickImage::setHorizontalAlignment(HAlignment align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#setHorizontalAlignment

    Parameters
    ----------

    align : HAlignment
      Passed on as its number.
    """
    #  void QQuickImage::setHorizontalAlignment(HAlignment align)
    self.uglySide.call(
        'ritual_ZN11QQuickImage22setHorizontalAlignmentENS_10HAlignmentE',
        align.value,
    )

  @overload(VAlignment)
  def setVerticalAlignment(self, align: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickImage::setVerticalAlignment(VAlignment align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#setVerticalAlignment

    Parameters
    ----------

    align : VAlignment
      Passed on as its number.
    """
    #  void QQuickImage::setVerticalAlignment(VAlignment align)
    self.uglySide.call(
        'ritual_ZN11QQuickImage20setVerticalAlignmentENS_10VAlignmentE',
        align.value,
    )

  @overload(bool)
  def setMipmap(self, use: bool) -> None:
    """
    Calls Qt's 'void QQuickImage::setMipmap(bool use)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#setMipmap

    Parameters
    ----------

    use : bool
      Passed on as it is.
    """
    #  void QQuickImage::setMipmap(bool use)
    self.uglySide.call('ritual_ZN11QQuickImage9setMipmapEb', use)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickImage::QQuickImage(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#QQuickImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickImage::QQuickImage(QQuickItem *parent)
    self._noteCreation(QQuickImage, lambda: Rituals.call(
        'ritual_ZN11QQuickImageC1EP10QQuickItem', self._addressOf(parent),
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

  def emitAutoTransformBaseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImage::emitAutoTransformBaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#emitAutoTransformBaseChanged
    """
    #  void QQuickImage::emitAutoTransformBaseChanged()
    ritual = 'ritual_ZN11QQuickImage28emitAutoTransformBaseChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickImage28emitAutoTransformBaseChangedEv'
    self.uglySide.call(ritual)

  def fillModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImage::fillModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#fillModeChanged
    """
    #  void QQuickImage::fillModeChanged()
    self.uglySide.call('ritual_ZN11QQuickImage15fillModeChangedEv')

  def paintedGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImage::paintedGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#paintedGeometryChanged
    """
    #  void QQuickImage::paintedGeometryChanged()
    self.uglySide.call('ritual_ZN11QQuickImage22paintedGeometryChangedEv')

  @overload(HAlignment)
  def horizontalAlignmentChanged(self, alignment: HAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickImage::horizontalAlignmentChanged(QQuickImage::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#horizontalAlignmentChanged

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickImage::horizontalAlignmentChanged(QQuickImage::HAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN11QQuickImage26horizontalAlignmentChangedENS_10HAlignment'
        'E',
        alignment.value,
    )

  @overload(VAlignment)
  def verticalAlignmentChanged(self, alignment: VAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickImage::verticalAlignmentChanged(QQuickImage::VAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#verticalAlignmentChanged

    Parameters
    ----------

    alignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickImage::verticalAlignmentChanged(QQuickImage::VAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN11QQuickImage24verticalAlignmentChangedENS_10VAlignmentE',
        alignment.value,
    )

  @overload(bool)
  def mipmapChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickImage::mipmapChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#mipmapChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickImage::mipmapChanged(bool a0)
    self.uglySide.call('ritual_ZN11QQuickImage13mipmapChangedEb', a0)

  def autoTransformChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImage::autoTransformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#autoTransformChanged
    """
    #  void QQuickImage::autoTransformChanged()
    self.uglySide.call('ritual_ZN11QQuickImage20autoTransformChangedEv')

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickImage::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#invalidateSceneGraph
    """
    #  void QQuickImage::invalidateSceneGraph()
    self.uglySide.call('ritual_ZN11QQuickImage20invalidateSceneGraphEv')

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickImage::pixmapChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#pixmapChange
    """
    #  void QQuickImage::pixmapChange()
    ritual = 'ritual_ZN11QQuickImage12pixmapChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickImage12pixmapChangeEv'
    self.uglySide.call(ritual)

  def updatePaintedGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickImage::updatePaintedGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimage.html#updatePaintedGeometry
    """
    #  void QQuickImage::updatePaintedGeometry()
    self.uglySide.call('ritual_ZN11QQuickImage21updatePaintedGeometryEv')

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickImage::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#releaseResources
    """
    #  void QQuickImage::releaseResources()
    ritual = 'ritual_ZN11QQuickImage16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickImage16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickImage::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickImage::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN11QQuickImage14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickImage14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickImage::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickImage::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
    #      *a1)
    ritual = (
        'ritual_ZN11QQuickImage15updatePaintNodeEP7QSGNodePN10QQuickItem19U'
        'pdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickImage15updatePaintNodeEP7QSGNodePN10QQuickI'
          'tem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def d_func(self) -> Optional[QQuickImagePrivate]:
    """
    Calls Qt's 'QQuickImagePrivate *QQuickImage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimage.html#d_func

    Returns
    -------

    Optional[QQuickImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImagePrivate *QQuickImage::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickImage6d_funcEv')
    from . import QQuickImagePrivate
    return QQuickImagePrivate._cuteAt(address)
