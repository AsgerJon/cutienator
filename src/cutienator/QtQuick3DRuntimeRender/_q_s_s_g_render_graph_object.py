"""
QSSGRenderGraphObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QSSGRenderGraphObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderGraphObject: a plain Python object standing
  in front of one C++ QSSGRenderGraphObject.

  What exists
  -----------

  Every function of Qt's QSSGRenderGraphObject that has a ritual and that
  Python can call so far, 10 names in all: 'isNodeType', 'isLight',
  'isCamera', 'isMaterial', 'isTexture', 'isRenderable', 'isResource',
  'isExtension', 'isUserType', 'hasGraphicsResources'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderGraphObject::~QSSGRenderGraphObject()': the destructor:
    Python never removes a C++ QSSGRenderGraphObject.
  - Qt's 'QDebug operator<<(QDebug stream, QSSGRenderGraphObject::Type
    type)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderGraphObject is created at the first use, not by
    'QSSGRenderGraphObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderGraphObject.
  """

  #  The enums Qt writes inside QSSGRenderGraphObject, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BaseType(CuteNum):
    """
    The enum 'QSSGRenderGraphObject::BaseType' of Qt, with the 9 names Qt
    gives in it.
    """

    Node = Kee[int](4096)
    Light = Kee[int](8192)
    Camera = Kee[int](16384)
    Renderable = Kee[int](32768)
    Resource = Kee[int](65536)
    Material = Kee[int](131072)
    Texture = Kee[int](262144)
    Extension = Kee[int](524288)
    User = Kee[int](2147483648)

  class Flags(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderGraphObject::Flags' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    HasGraphicsResources = Kee[int](1)
    InternallyReserved = Kee[int](4294901760)

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderGraphObject::Type' of Qt, with the 38 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unknown = Kee[int](0)
    Node = Kee[int](4096)
    Root = Kee[int](4097)
    Layer = Kee[int](4098)
    Joint = Kee[int](4099)
    Skeleton = Kee[int](4100)
    ImportScene = Kee[int](4101)
    ReflectionProbe = Kee[int](4102)
    SceneRoot = Kee[int](4103)
    DirectionalLight = Kee[int](12288)
    PointLight = Kee[int](12289)
    SpotLight = Kee[int](12290)
    OrthographicCamera = Kee[int](20480)
    PerspectiveCamera = Kee[int](20481)
    CustomFrustumCamera = Kee[int](20482)
    CustomCamera = Kee[int](20483)
    Model = Kee[int](36864)
    Item2D = Kee[int](36865)
    Particles = Kee[int](36866)
    SceneEnvironment = Kee[int](65536)
    Effect = Kee[int](65537)
    Geometry = Kee[int](65538)
    TextureData = Kee[int](65539)
    MorphTarget = Kee[int](65540)
    ModelInstance = Kee[int](65541)
    ModelBlendParticle = Kee[int](65542)
    ResourceLoader = Kee[int](65543)
    RenderPass = Kee[int](65544)
    SkyMaterial = Kee[int](65545)
    DefaultMaterial = Kee[int](196608)
    PrincipledMaterial = Kee[int](196609)
    CustomMaterial = Kee[int](196610)
    SpecularGlossyMaterial = Kee[int](196611)
    Skin = Kee[int](196612)
    Image2D = Kee[int](327680)
    ImageCube = Kee[int](327681)
    RenderExtension = Kee[int](524288)
    TextureProvider = Kee[int](524289)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Type)
  def isNodeType(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isNodeType(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isNodeType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isNodeType(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject10isNodeTypeENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isLight(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isLight(Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendergraphobject.html#isLight

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isLight(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject7isLightENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isCamera(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isCamera(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isCamera

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isCamera(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject8isCameraENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isMaterial(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isMaterial(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isMaterial

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isMaterial(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject10isMaterialENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isTexture(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isTexture(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isTexture

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isTexture(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject9isTextureENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isRenderable(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isRenderable(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isRenderable

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isRenderable(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject12isRenderableENS_4TypeE',
        type.value,
    )

  @staticmethod
  @overload(Type)
  def isResource(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isResource(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isResource

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isResource(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject10isResourceENS_4TypeE', type.value,
    )

  @staticmethod
  @overload(Type)
  def isExtension(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isExtension(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isExtension

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isExtension(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject11isExtensionENS_4TypeE',
        type.value,
    )

  @staticmethod
  @overload(Type)
  def isUserType(type: Type) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::isUserType(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#isUserType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  bool QSSGRenderGraphObject::isUserType(Type type)
    return Rituals.call(
        'ritual_ZN21QSSGRenderGraphObject10isUserTypeENS_4TypeE', type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderGraphObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasGraphicsResources(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderGraphObject::hasGraphicsResources() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#hasGraphicsResources
    """
    #  bool QSSGRenderGraphObject::hasGraphicsResources() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRenderGraphObject20hasGraphicsResourcesEv',
    )

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

  @overload(Type)
  def __init__(self, inType: Type) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderGraphObject::QSSGRenderGraphObject(QSSGRenderGraphObject::Type
    inType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#QSSGRenderGraphObject

    Parameters
    ----------

    inType : Type
      Passed on as its number.
    """
    #  QSSGRenderGraphObject::QSSGRenderGraphObject(
    #      QSSGRenderGraphObject::Type inType)
    self._noteCreation(QSSGRenderGraphObject, lambda: Rituals.call(
        'ritual_ZN21QSSGRenderGraphObjectC1ENS_4TypeE', inType.value,
    ))

  @overload(Type, int)
  def __init__(self, inType: Type, inFlags: int) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderGraphObject::QSSGRenderGraphObject(QSSGRenderGraphObject::Type
    inType, FlagT inFlags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendergraphobject.html#QSSGRenderGraphObject

    Parameters
    ----------

    inType : Type
      Passed on as its number.

    inFlags : int
      Passed on as it is.
    """
    #  QSSGRenderGraphObject::QSSGRenderGraphObject(
    #      QSSGRenderGraphObject::Type inType, FlagT inFlags)
    self._noteCreation(QSSGRenderGraphObject, lambda: Rituals.call(
        'ritual_ZN21QSSGRenderGraphObjectC1ENS_4TypeEj',
        inType.value, inFlags,
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


#  Qt's 'QList<QSSGRenderGraphObject *>': the list of QSSGRenderGraphObject,
#  which 'QList[QSSGRenderGraphObject]' gives. It is made here, so that there
#  is one as soon as there can be a QSSGRenderGraphObject.
QList.createKind(
    QSSGRenderGraphObject, 'address',
    make='ritual_list_make_QSSGRenderGraphObject_ptr',
    add='ritual_list_add_QSSGRenderGraphObject_ptr',
    size='ritual_list_size_QSSGRenderGraphObject_ptr',
    at='ritual_list_at_QSSGRenderGraphObject_ptr',
    drop='ritual_list_drop_QSSGRenderGraphObject_ptr',
)
