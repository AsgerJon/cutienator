"""
QSSGRenderCustomMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercustommaterial_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderCustomMaterial to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3DUtils import QSSGRenderShaderValue
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QVariant


class QSSGRenderCustomMaterial(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderCustomMaterial: a plain Python object
  standing in front of one C++ QSSGRenderCustomMaterial.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderCustomMaterial is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderCustomMaterial that has a ritual and that
  Python can call so far, 4 names in all: 'markDirty', 'clearDirty',
  'setAlwaysDirty', 'isDirty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderCustomMaterial::~QSSGRenderCustomMaterial()': the
    destructor: Python never removes a C++ QSSGRenderCustomMaterial.

  What to expect
  --------------

  - The C++ QSSGRenderCustomMaterial is created at the first use, not by
    'QSSGRenderCustomMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderCustomMaterial.
  """

  #  The enums Qt writes inside QSSGRenderCustomMaterial, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class CustomShaderPresenceFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGRenderCustomMaterial::CustomShaderPresenceFlag' of
    Qt, with the 2 names Qt gives in it. Qt names the type of its
    combinations 'QSSGRenderCustomMaterial::CustomShaderPresence'. C++ keeps
    these names inside the enum, so the class that holds the enum does not
    have them.
    """

    Vertex = 0x1
    Fragment = 0x2

  CustomShaderPresence = CustomShaderPresenceFlag

  class Flags(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderCustomMaterial::Flags' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Dirty = Kee[int](1)
    AlwaysDirty = Kee[int](2)

  class RenderFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGRenderCustomMaterial::RenderFlag' of Qt, with the 20
    names Qt gives in it. Qt names the type of its combinations
    'QSSGRenderCustomMaterial::RenderFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Blending = 0x1
    ScreenTexture = 0x2
    DepthTexture = 0x4
    AoTexture = 0x8
    OverridesPosition = 0x10
    ProjectionMatrix = 0x20
    InverseProjectionMatrix = 0x40
    ScreenMipTexture = 0x80
    VarColor = 0x100
    IblOrientation = 0x200
    Lightmap = 0x400
    Skinning = 0x800
    Morphing = 0x1000
    ViewIndex = 0x2000
    Clearcoat = 0x4000
    ClearcoatFresnelScaleBias = 0x8000
    FresnelScaleBias = 0x10000
    Transmission = 0x20000
    NormalTexture = 0x40000
    MotionVectorTexture = 0x80000

  RenderFlags = RenderFlag

  class ShadingMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderCustomMaterial::ShadingMode' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unshaded = Kee[int](0)
    Shaded = Kee[int](1)

  #  The classes Qt writes inside QSSGRenderCustomMaterial, each a class in
  #  here as in C++.

  class Property(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderCustomMaterial::Property: a plain Python
    object standing in front of one C++ QSSGRenderCustomMaterial::Property.

    C++ hands a QSSGRenderCustomMaterial::Property around as a copy, so every
    C++ QSSGRenderCustomMaterial::Property behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderCustomMaterial::Property yet. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderCustomMaterial::Property::~Property()': the destructor:
      Python removes its C++ QSSGRenderCustomMaterial::Property by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderCustomMaterial::Property is created at the first use,
      not by 'QSSGRenderCustomMaterial::Property(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderCustomMaterial::Property back gives a
      copy the ritual made for Python, in a new cute
      QSSGRenderCustomMaterial::Property.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderCustomMaterial::Property'

    #  Qt's '~QSSGRenderCustomMaterial::Property()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderCustomMaterial::Property
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QSSGRenderCustomMaterial8PropertyD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderCustomMaterial::Property::Property()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercustommaterial-property.html#Property
      """
      #  QSSGRenderCustomMaterial::Property::Property()
      self._noteCreation(
          QSSGRenderCustomMaterial.Property, lambda: Rituals.call(
              'ritual_ZN24QSSGRenderCustomMaterial8PropertyC1Ev',
          ))

    @overload(QByteArray, QVariant, QSSGRenderShaderValue.Type)
    @overload(QByteArray, QVariant, QSSGRenderShaderValue.Type, int)
    def __init__(
        self,
        name: QByteArray,
        value: QVariant,
        shaderDataType: QSSGRenderShaderValue.Type,
        pid: int = -1,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderCustomMaterial::Property::Property(const QByteArray &name,
      const QVariant &value, QSSGRenderShaderValue::Type shaderDataType, int
      pid)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercustommaterial-property.html#Property

      Parameters
      ----------

      name : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      value : QVariant
        Passed on as a value: Qt reads the C++ QVariant, which stays Python's
        own.

      shaderDataType : QSSGRenderShaderValue.Type
        Passed on as its number.

      pid : int
        Passed on as it is. May be left out, as in Qt: it is then -1.
      """
      #  QSSGRenderCustomMaterial::Property::Property(const QByteArray &name,
      #      const QVariant &value, QSSGRenderShaderValue::Type
      #      shaderDataType, int pid)
      self._noteCreation(
          QSSGRenderCustomMaterial.Property, lambda: Rituals.call(
              'ritual_ZN24QSSGRenderCustomMaterial8PropertyC1ERK10QByteArra'
              'yRK8QVariantN21QSSGRenderShaderValue4TypeEi',
              self._valueOf(name), self._valueOf(value),
              shaderDataType.value, pid,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TextureProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderCustomMaterial::TextureProperty: a plain
    Python object standing in front of one C++
    QSSGRenderCustomMaterial::TextureProperty.

    C++ hands a QSSGRenderCustomMaterial::TextureProperty around as a copy,
    so every C++ QSSGRenderCustomMaterial::TextureProperty behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderCustomMaterial::TextureProperty yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderCustomMaterial::TextureProperty::~TextureProperty()':
      the destructor: Python removes its C++
      QSSGRenderCustomMaterial::TextureProperty by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderCustomMaterial::TextureProperty is created at the
      first use, not by 'QSSGRenderCustomMaterial::TextureProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderCustomMaterial::TextureProperty back
      gives a copy the ritual made for Python, in a new cute
      QSSGRenderCustomMaterial::TextureProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderCustomMaterial::TextureProperty'

    #  Qt's '~QSSGRenderCustomMaterial::TextureProperty()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGRenderCustomMaterial::TextureProperty behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QSSGRenderCustomMaterial15TexturePropertyD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderCustomMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderCustomMaterial::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercustommaterial.html#isDirty
    """
    #  bool QSSGRenderCustomMaterial::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGRenderCustomMaterial7isDirtyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAlwaysDirty(self, v: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderCustomMaterial::setAlwaysDirty(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercustommaterial.html#setAlwaysDirty

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGRenderCustomMaterial::setAlwaysDirty(bool v)
    self.uglySide.call(
        'ritual_ZN24QSSGRenderCustomMaterial14setAlwaysDirtyEb', v,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderCustomMaterial::QSSGRenderCustomMaterial()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercustommaterial.html
    """
    #  QSSGRenderCustomMaterial::QSSGRenderCustomMaterial()
    self._noteCreation(QSSGRenderCustomMaterial, lambda: Rituals.call(
        'ritual_ZN24QSSGRenderCustomMaterialC1Ev',
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

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QSSGRenderCustomMaterial::markDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercustommaterial.html#markDirty
    """
    #  void QSSGRenderCustomMaterial::markDirty()
    self.uglySide.call('ritual_ZN24QSSGRenderCustomMaterial9markDirtyEv')

  def clearDirty(self) -> None:
    """
    Calls Qt's 'void QSSGRenderCustomMaterial::clearDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercustommaterial.html#clearDirty
    """
    #  void QSSGRenderCustomMaterial::clearDirty()
    self.uglySide.call('ritual_ZN24QSSGRenderCustomMaterial10clearDirtyEv')
