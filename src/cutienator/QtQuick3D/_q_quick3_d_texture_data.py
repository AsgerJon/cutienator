"""
QQuick3DTextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/qquick3dtexturedata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QSize
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DTextureDataPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DTextureData(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DTextureData: a plain Python object standing
  in front of one C++ QQuick3DTextureData.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DTextureData is
  built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DTextureData that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'd_func',
  'textureData', 'setTextureData', 'size', 'setSize', 'depth', 'setDepth',
  'format', 'setFormat', 'hasTransparency', 'setHasTransparency',
  'textureDataNodeDirty', 'updateSpatialNode', 'markAllDirty'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DTextureData::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DTextureData::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DTextureDataPrivate *QQuick3DTextureData::d_func()
    const': takes in Python what 'QQuick3DTextureDataPrivate
    *QQuick3DTextureData::d_func()' takes.
  - Qt's 'void QQuick3DTextureData::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQuick3DTextureData::~QQuick3DTextureData()': the destructor:
    Python never removes a C++ QQuick3DTextureData.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DTextureData is created at the first use, not by
    'QQuick3DTextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DTextureData.
  - Qt tells when it has removed the C++ QQuick3DTextureData. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DTextureData, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Format(CuteNum):
    """
    The enum 'QQuick3DTextureData::Format' of Qt, with the 37 names Qt gives
    in it.
    """

    NULL = Kee[int](0)
    RGBA8 = Kee[int](1)
    RGBA16F = Kee[int](2)
    RGBA32F = Kee[int](3)
    RGBE8 = Kee[int](4)
    R8 = Kee[int](5)
    R16 = Kee[int](6)
    R16F = Kee[int](7)
    R32F = Kee[int](8)
    BC1 = Kee[int](9)
    BC2 = Kee[int](10)
    BC3 = Kee[int](11)
    BC4 = Kee[int](12)
    BC5 = Kee[int](13)
    BC6H = Kee[int](14)
    BC7 = Kee[int](15)
    DXT1_RGBA = Kee[int](16)
    DXT1_RGB = Kee[int](17)
    DXT3_RGBA = Kee[int](18)
    DXT5_RGBA = Kee[int](19)
    ETC2_RGB8 = Kee[int](20)
    ETC2_RGB8A1 = Kee[int](21)
    ETC2_RGBA8 = Kee[int](22)
    ASTC_4x4 = Kee[int](23)
    ASTC_5x4 = Kee[int](24)
    ASTC_5x5 = Kee[int](25)
    ASTC_6x5 = Kee[int](26)
    ASTC_6x6 = Kee[int](27)
    ASTC_8x5 = Kee[int](28)
    ASTC_8x6 = Kee[int](29)
    ASTC_8x8 = Kee[int](30)
    ASTC_10x5 = Kee[int](31)
    ASTC_10x6 = Kee[int](32)
    ASTC_10x8 = Kee[int](33)
    ASTC_10x10 = Kee[int](34)
    ASTC_12x10 = Kee[int](35)
    ASTC_12x12 = Kee[int](36)

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
    Calls Qt's 'QString QQuick3DTextureData::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#tr

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
    #  QString QQuick3DTextureData::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DTextureData2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DTextureData'

  #  A C++ QQuick3DTextureData Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DTextureData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DTextureData::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DTextureData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DTextureData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureData(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray QQuick3DTextureData::textureData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#textureData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray QQuick3DTextureData::textureData() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DTextureData11textureDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QQuick3DTextureData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuick3DTextureData::size() const
    address = self.uglySide.call('ritual_ZNK19QQuick3DTextureData4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QQuick3DTextureData::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#depth
    """
    #  int QQuick3DTextureData::depth() const
    return self.uglySide.call('ritual_ZNK19QQuick3DTextureData5depthEv')

  def format(self) -> Format:
    """
    Calls Qt's 'Format QQuick3DTextureData::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QQuick3DTextureData::format() const
    return QQuick3DTextureData.Format(self.uglySide.call(
        'ritual_ZNK19QQuick3DTextureData6formatEv',
    ))

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTextureData::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#hasTransparency
    """
    #  bool QQuick3DTextureData::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DTextureData15hasTransparencyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setTextureData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::setTextureData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#setTextureData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DTextureData::setTextureData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN19QQuick3DTextureData14setTextureDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuick3DTextureData::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN19QQuick3DTextureData7setSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::setDepth(int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QQuick3DTextureData::setDepth(int depth)
    self.uglySide.call('ritual_ZN19QQuick3DTextureData8setDepthEi', depth)

  @overload(Format)
  def setFormat(self, format: Format) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::setFormat(Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#setFormat

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void QQuick3DTextureData::setFormat(Format format)
    self.uglySide.call(
        'ritual_ZN19QQuick3DTextureData9setFormatENS_6FormatE', format.value,
    )

  @overload(bool)
  def setHasTransparency(self, hasTransparency: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::setHasTransparency(bool
    hasTransparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#setHasTransparency

    Parameters
    ----------

    hasTransparency : bool
      Passed on as it is.
    """
    #  void QQuick3DTextureData::setHasTransparency(bool hasTransparency)
    self.uglySide.call(
        'ritual_ZN19QQuick3DTextureData18setHasTransparencyEb',
        hasTransparency,
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

  @overload()
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DTextureData::QQuick3DTextureData(QQuick3DObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#QQuick3DTextureData

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DTextureData::QQuick3DTextureData(QQuick3DObject *parent)
    self._noteCreation(QQuick3DTextureData, lambda: Rituals.call(
        'ritual_ZN19QQuick3DTextureDataC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def d_func(self) -> Optional[QQuick3DTextureDataPrivate]:
    """
    Calls Qt's 'QQuick3DTextureDataPrivate *QQuick3DTextureData::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dtexturedata.html#d_func

    Returns
    -------

    Optional[QQuick3DTextureDataPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTextureDataPrivate *QQuick3DTextureData::d_func()
    address = self.uglySide.call('ritual_ZN19QQuick3DTextureData6d_funcEv')
    from . import QQuick3DTextureDataPrivate
    return QQuick3DTextureDataPrivate._cuteAt(address)

  def textureDataNodeDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::textureDataNodeDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#textureDataNodeDirty
    """
    #  void QQuick3DTextureData::textureDataNodeDirty()
    self.uglySide.call(
        'ritual_ZN19QQuick3DTextureData20textureDataNodeDirtyEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN19QQuick3DTextureData17updateSpatialNodeEP21QSSGRenderGra'
        'phObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuick3DTextureData17updateSpatialNodeEP21QSSGRen'
          'derGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureData::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedata.html#markAllDirty
    """
    #  void QQuick3DTextureData::markAllDirty()
    ritual = 'ritual_ZN19QQuick3DTextureData12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuick3DTextureData12markAllDirtyEv'
    self.uglySide.call(ritual)
