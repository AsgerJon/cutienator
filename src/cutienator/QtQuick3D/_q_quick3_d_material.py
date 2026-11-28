"""
QQuick3DMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DMaterial to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DSceneManager, QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DMaterial(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DMaterial: a plain Python object standing in
  front of one C++ QQuick3DMaterial.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DMaterial is built
  on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DMaterial that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'lightProbe',
  'cullMode', 'depthDrawMode', 'setLightProbe', 'setCullMode',
  'setDepthDrawMode', 'lightProbeChanged', 'cullModeChanged',
  'depthDrawModeChanged', 'updateSpatialNode', 'itemChange',
  'updateSceneManager'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DMaterial::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DMaterial::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DMaterial::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuick3DMaterial::~QQuick3DMaterial()': the destructor: Python
    never removes a C++ QQuick3DMaterial.
  - Qt's 'QQuick3DMaterial::QQuick3DMaterial(QQuick3DObjectPrivate &dd,
    QQuick3DObject *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DMaterial is created at the first use, not by
    'QQuick3DMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DMaterial.
  - Qt tells when it has removed the C++ QQuick3DMaterial. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DMaterial that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DMaterial, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CullMode(CuteNum):
    """
    The enum 'QQuick3DMaterial::CullMode' of Qt, with the 3 names Qt gives in
    it.
    """

    BackFaceCulling = Kee[int](1)
    FrontFaceCulling = Kee[int](2)
    NoCulling = Kee[int](3)

  class DepthDrawMode(CuteNum):
    """
    The enum 'QQuick3DMaterial::DepthDrawMode' of Qt, with the 4 names Qt
    gives in it.
    """

    OpaqueOnlyDepthDraw = Kee[int](0)
    AlwaysDepthDraw = Kee[int](1)
    NeverDepthDraw = Kee[int](2)
    OpaquePrePassDepthDraw = Kee[int](3)

  class TextureChannelMapping(CuteNum):
    """
    The enum 'QQuick3DMaterial::TextureChannelMapping' of Qt, with the 4
    names Qt gives in it.
    """

    R = Kee[int](0)
    G = Kee[int](1)
    B = Kee[int](2)
    A = Kee[int](3)

  class VertexColorMask(CuteFlags):
    """
    The flags enum 'QQuick3DMaterial::VertexColorMask' of Qt, with the 12
    names Qt gives in it. Qt names the type of its combinations
    'QQuick3DMaterial::VertexColorMaskFlags'.
    """

    NoMask = 0x0
    RoughnessMask = 0x1
    NormalStrengthMask = 0x2
    SpecularAmountMask = 0x4
    ClearcoatAmountMask = 0x8
    ClearcoatRoughnessAmountMask = 0x10
    ClearcoatNormalStrengthMask = 0x20
    HeightAmountMask = 0x40
    MetalnessMask = 0x80
    OcclusionAmountMask = 0x100
    ThicknessFactorMask = 0x200
    TransmissionFactorMask = 0x400

  VertexColorMaskFlags = VertexColorMask

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
    Calls Qt's 'QString QQuick3DMaterial::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#tr

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
    #  QString QQuick3DMaterial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DMaterial'

  #  A C++ QQuick3DMaterial Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DMaterial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lightProbe(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DMaterial::lightProbe() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#lightProbe

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DMaterial::lightProbe() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DMaterial10lightProbeEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def cullMode(self) -> CullMode:
    """
    Calls Qt's 'CullMode QQuick3DMaterial::cullMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#cullMode

    Returns
    -------

    CullMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CullMode(number)' gives.
    """
    #  CullMode QQuick3DMaterial::cullMode() const
    return QQuick3DMaterial.CullMode(self.uglySide.call(
        'ritual_ZNK16QQuick3DMaterial8cullModeEv',
    ))

  def depthDrawMode(self) -> DepthDrawMode:
    """
    Calls Qt's 'DepthDrawMode QQuick3DMaterial::depthDrawMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#depthDrawMode

    Returns
    -------

    DepthDrawMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DepthDrawMode(number)'
      gives.
    """
    #  DepthDrawMode QQuick3DMaterial::depthDrawMode() const
    return QQuick3DMaterial.DepthDrawMode(self.uglySide.call(
        'ritual_ZNK16QQuick3DMaterial13depthDrawModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setLightProbe(self, lightProbe: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DMaterial::setLightProbe(QQuick3DTexture
    *lightProbe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#setLightProbe

    Parameters
    ----------

    lightProbe : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DMaterial::setLightProbe(QQuick3DTexture *lightProbe)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial13setLightProbeEP15QQuick3DTexture',
        self._addressOf(lightProbe),
    )

  @overload(CullMode)
  def setCullMode(self, cullMode: CullMode) -> None:
    """
    Calls Qt's 'void QQuick3DMaterial::setCullMode(QQuick3DMaterial::CullMode
    cullMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#setCullMode

    Parameters
    ----------

    cullMode : CullMode
      Passed on as its number.
    """
    #  void QQuick3DMaterial::setCullMode(QQuick3DMaterial::CullMode
    #      cullMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial11setCullModeENS_8CullModeE',
        cullMode.value,
    )

  @overload(DepthDrawMode)
  def setDepthDrawMode(self, depthDrawMode: DepthDrawMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DMaterial::setDepthDrawMode(QQuick3DMaterial::DepthDrawMode
    depthDrawMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#setDepthDrawMode

    Parameters
    ----------

    depthDrawMode : DepthDrawMode
      Passed on as its number.
    """
    #  void
    #      QQuick3DMaterial::setDepthDrawMode(QQuick3DMaterial::DepthDrawMode
    #      depthDrawMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial16setDepthDrawModeENS_13DepthDrawModeE',
        depthDrawMode.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DMaterial::QQuick3DMaterial(QQuick3DObjectPrivate &dd,
    QQuick3DObject *parent)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DMaterial.__init__' has no cute function yet. Qt's "
        "'QQuick3DMaterial::QQuick3DMaterial(QQuick3DObjectPrivate &dd, "
        "QQuick3DObject *parent)': takes a type Python has no way to hand "
        "over yet.")

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

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def lightProbeChanged(self, lightProbe: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DMaterial::lightProbeChanged(QQuick3DTexture
    *lightProbe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#lightProbeChanged

    Parameters
    ----------

    lightProbe : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DMaterial::lightProbeChanged(QQuick3DTexture *lightProbe)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial17lightProbeChangedEP15QQuick3DTexture',
        self._addressOf(lightProbe),
    )

  @overload(CullMode)
  def cullModeChanged(self, cullMode: CullMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DMaterial::cullModeChanged(QQuick3DMaterial::CullMode cullMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#cullModeChanged

    Parameters
    ----------

    cullMode : CullMode
      Passed on as its number.
    """
    #  void QQuick3DMaterial::cullModeChanged(QQuick3DMaterial::CullMode
    #      cullMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial15cullModeChangedENS_8CullModeE',
        cullMode.value,
    )

  @overload(DepthDrawMode)
  def depthDrawModeChanged(self, depthDrawMode: DepthDrawMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DMaterial::depthDrawModeChanged(QQuick3DMaterial::DepthDrawMode
    depthDrawMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#depthDrawModeChanged

    Parameters
    ----------

    depthDrawMode : DepthDrawMode
      Passed on as its number.
    """
    #  void QQuick3DMaterial::depthDrawModeChanged(QQuick3DMaterial::
    #      DepthDrawMode depthDrawMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial20depthDrawModeChangedENS_13DepthDrawMo'
        'deE',
        depthDrawMode.value,
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DMaterial::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#updateSpatialNode

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
    #      *QQuick3DMaterial::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN16QQuick3DMaterial17updateSpatialNodeEP21QSSGRenderGraphO'
        'bject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DMaterial17updateSpatialNodeEP21QSSGRender'
          'GraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DMaterial::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmaterial.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DMaterial::itemChange(ItemChange a0, const ItemChangeData
    #      &a1)
    ritual = (
        'ritual_ZN16QQuick3DMaterial10itemChangeEN14QQuick3DObject10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DMaterial10itemChangeEN14QQuick3DObject10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DMaterial::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmaterial.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DMaterial::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN16QQuick3DMaterial18updateSceneManagerEP20QQuick3DSceneMa'
        'nager',
        self._addressOf(sceneManager),
    )
