"""
QSSGRenderEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendereffect_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderEffect to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3DUtils import QSSGRenderShaderValue
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QVariant


class QSSGRenderEffect(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderEffect: a plain Python object standing in
  front of one C++ QSSGRenderEffect.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's QSSGRenderEffect
  is built on Qt's QSSGRenderGraphObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderEffect that has a ritual and that Python
  can call so far, 6 names in all: 'markDirty', 'clearDirty', 'isDirty',
  'setFlag', 'testFlag', 'resetCommands'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderEffect::~QSSGRenderEffect()': the destructor: Python
    never removes a C++ QSSGRenderEffect.
  - Qt's 'void QSSGRenderEffect::finalizeShaders(const QSSGRenderLayer
    &layer, QSSGRenderContextInterface *renderContext)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGRenderEffect is created at the first use, not by
    'QSSGRenderEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderEffect.
  - Each name of Qt's QSSGRenderEffect that has no cute function yet,
    'finalizeShaders', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderEffect, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flags(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderEffect::Flags' of Qt, with the 7 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Dirty = Kee[int](1)
    UsesDepthTexture = Kee[int](2)
    UsesProjectionMatrix = Kee[int](4)
    UsesInverseProjectionMatrix = Kee[int](8)
    UsesViewMatrix = Kee[int](16)
    UsesNormalTexture = Kee[int](32)
    UsesMotionVectorTexture = Kee[int](64)

  #  The classes Qt writes inside QSSGRenderEffect, each a class in here as
  #  in C++.

  class Property(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderEffect::Property: a plain Python object
    standing in front of one C++ QSSGRenderEffect::Property.

    C++ hands a QSSGRenderEffect::Property around as a copy, so every C++
    QSSGRenderEffect::Property behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGRenderEffect::Property yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderEffect::Property::~Property()': the destructor: Python
      removes its C++ QSSGRenderEffect::Property by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderEffect::Property is created at the first use, not by
      'QSSGRenderEffect::Property(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderEffect::Property back gives a copy the
      ritual made for Python, in a new cute QSSGRenderEffect::Property.
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
    __qt_class__ = 'QSSGRenderEffect::Property'

    #  Qt's '~QSSGRenderEffect::Property()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderEffect::Property behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderEffect8PropertyD1Ev'

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
      'QSSGRenderEffect::Property::Property()', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendereffect-property.html#Property
      """
      #  QSSGRenderEffect::Property::Property()
      self._noteCreation(QSSGRenderEffect.Property, lambda: Rituals.call(
          'ritual_ZN16QSSGRenderEffect8PropertyC1Ev',
      ))

    @overload(QByteArray, QByteArray, QVariant, QSSGRenderShaderValue.Type)
    @overload(
        QByteArray, QByteArray, QVariant, QSSGRenderShaderValue.Type, int,
    )
    def __init__(
        self,
        name: QByteArray,
        typeName: QByteArray,
        value: QVariant,
        shaderDataType: QSSGRenderShaderValue.Type,
        pid: int = -1,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderEffect::Property::Property(const QByteArray &name, const
      QByteArray &typeName, const QVariant &value,
      QSSGRenderShaderValue::Type shaderDataType, int pid)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendereffect-property.html#Property

      Parameters
      ----------

      name : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      typeName : QByteArray
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
      #  QSSGRenderEffect::Property::Property(const QByteArray &name, const
      #      QByteArray &typeName, const QVariant &value,
      #      QSSGRenderShaderValue::Type shaderDataType, int pid)
      self._noteCreation(QSSGRenderEffect.Property, lambda: Rituals.call(
          'ritual_ZN16QSSGRenderEffect8PropertyC1ERK10QByteArrayS3_RK8QVari'
          'antN21QSSGRenderShaderValue4TypeEi',
          self._valueOf(name), self._valueOf(typeName), self._valueOf(value),
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

  class ShaderPrepPassData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderEffect::ShaderPrepPassData: a plain
    Python object standing in front of one C++
    QSSGRenderEffect::ShaderPrepPassData.

    C++ hands a QSSGRenderEffect::ShaderPrepPassData around as a copy, so
    every C++ QSSGRenderEffect::ShaderPrepPassData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderEffect::ShaderPrepPassData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderEffect::ShaderPrepPassData::~ShaderPrepPassData()': the
      destructor: Python removes its C++ QSSGRenderEffect::ShaderPrepPassData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderEffect::ShaderPrepPassData is created at the first
      use, not by 'QSSGRenderEffect::ShaderPrepPassData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderEffect::ShaderPrepPassData back gives a
      copy the ritual made for Python, in a new cute
      QSSGRenderEffect::ShaderPrepPassData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderEffect::ShaderPrepPassData'

    #  Qt's '~QSSGRenderEffect::ShaderPrepPassData()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QSSGRenderEffect::ShaderPrepPassData behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderEffect18ShaderPrepPassDataD1Ev'

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

  class TextureProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderEffect::TextureProperty: a plain Python
    object standing in front of one C++ QSSGRenderEffect::TextureProperty.

    C++ hands a QSSGRenderEffect::TextureProperty around as a copy, so every
    C++ QSSGRenderEffect::TextureProperty behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderEffect::TextureProperty yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderEffect::TextureProperty::~TextureProperty()': the
      destructor: Python removes its C++ QSSGRenderEffect::TextureProperty by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderEffect::TextureProperty is created at the first use,
      not by 'QSSGRenderEffect::TextureProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderEffect::TextureProperty back gives a copy
      the ritual made for Python, in a new cute
      QSSGRenderEffect::TextureProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderEffect::TextureProperty'

    #  Qt's '~QSSGRenderEffect::TextureProperty()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderEffect::TextureProperty
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderEffect15TexturePropertyD1Ev'

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
  __qt_class__ = 'QSSGRenderEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderEffect::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendereffect.html#isDirty
    """
    #  bool QSSGRenderEffect::isDirty() const
    return self.uglySide.call('ritual_ZNK16QSSGRenderEffect7isDirtyEv')

  @overload(Flags)
  def testFlag(self, flag: Flags) -> bool:
    """
    Calls Qt's 'bool QSSGRenderEffect::testFlag(QSSGRenderEffect::Flags flag)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendereffect.html#testFlag

    Parameters
    ----------

    flag : Flags
      Passed on as its number.
    """
    #  bool QSSGRenderEffect::testFlag(QSSGRenderEffect::Flags flag) const
    return self.uglySide.call(
        'ritual_ZNK16QSSGRenderEffect8testFlagENS_5FlagsE', flag.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  @overload(Flags, bool)
  def setFlag(self, flag: Flags, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QSSGRenderEffect::setFlag(QSSGRenderEffect::Flags flag,
    bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendereffect.html#setFlag

    Parameters
    ----------

    flag : Flags
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSSGRenderEffect::setFlag(QSSGRenderEffect::Flags flag, bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN16QSSGRenderEffect7setFlagENS_5FlagsEb',
        flag.value, enabled,
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
    Notes what was given, for Qt's 'QSSGRenderEffect::QSSGRenderEffect()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendereffect.html#QSSGRenderEffect
    """
    #  QSSGRenderEffect::QSSGRenderEffect()
    self._noteCreation(QSSGRenderEffect, lambda: Rituals.call(
        'ritual_ZN16QSSGRenderEffectC1Ev',
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
    Calls Qt's 'void QSSGRenderEffect::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendereffect.html#markDirty
    """
    #  void QSSGRenderEffect::markDirty()
    self.uglySide.call('ritual_ZN16QSSGRenderEffect9markDirtyEv')

  def clearDirty(self) -> None:
    """
    Calls Qt's 'void QSSGRenderEffect::clearDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendereffect.html#clearDirty
    """
    #  void QSSGRenderEffect::clearDirty()
    self.uglySide.call('ritual_ZN16QSSGRenderEffect10clearDirtyEv')

  def resetCommands(self) -> None:
    """
    Calls Qt's 'void QSSGRenderEffect::resetCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendereffect.html#resetCommands
    """
    #  void QSSGRenderEffect::resetCommands()
    self.uglySide.call('ritual_ZN16QSSGRenderEffect13resetCommandsEv')

  @staticmethod
  def finalizeShaders(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderEffect::finalizeShaders(const QSSGRenderLayer
    &layer, QSSGRenderContextInterface *renderContext)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderEffect.finalizeShaders' has no cute function yet. Qt's "
        "'void QSSGRenderEffect::finalizeShaders(const QSSGRenderLayer "
        "&layer, QSSGRenderContextInterface *renderContext)': takes a type "
        "Python has no way to hand over yet.")
