"""
QSSGRhiShaderPipeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiShaderPipeline to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QRhiShaderStage, QRhiTexture
  from . import QSSGRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRhiShaderStage = WAIT['QRhiShaderStage']
  QRhiTexture = WAIT['QRhiTexture']
  QSSGRhiTexture = WAIT['QSSGRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiShaderPipeline(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiShaderPipeline: a plain Python object standing
  in front of one C++ QSSGRhiShaderPipeline.

  What exists
  -----------

  Every function of Qt's QSSGRhiShaderPipeline that has a ritual and that
  Python can call so far, 37 names in all: 'isNull', 'addStage',
  'cbeginStages', 'cendStages', 'vertexStage', 'fragmentStage', 'ub0Size',
  'ub0LightDataOffset', 'ub0DirectionalLightDataOffset', 'bindingForTexture',
  'bindingForImage', 'setLightsEnabled', 'isLightingEnabled',
  'lightProbeTexture', 'setScreenTexture', 'screenTexture',
  'setDepthTexture', 'depthTexture', 'setNormalTexture', 'normalTexture',
  'setSsaoTexture', 'ssaoTexture', 'setLightmapTexture', 'lightmapTexture',
  'setMotionVectorTexture', 'MotionVectorTexture',
  'setShadowMapAtlasTexture', 'shadowMapAtlasTexture',
  'setShadowMapBlueNoiseTexture', 'shadowMapBlueNoiseTexture',
  'setOITImages', 'resetExtraTextures', 'addExtraTexture',
  'extraTextureCount', 'extraTextureAt', 'instanceBufferLocations',
  'offsetOfUniform'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiShaderPipeline::QSSGRhiShaderPipeline(QSSGRhiContext
    &context)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiContext &QSSGRhiShaderPipeline::context() const': gives a
    type Python has no way to take yet.
  - Qt's 'const QHash<QSSGRhiInputAssemblerState::InputSemantic,
    QShaderDescription::InOutVariable> &QSSGRhiShaderPipeline::vertexInputs()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QSSGRhiShaderPipeline::setUniformValue(char *ubufData, const
    char *name, const QVariant &value, QSSGRenderShaderValue::Type type)':
    names 'char', which has no cute class yet.
  - Qt's 'void QSSGRhiShaderPipeline::setUniform(char *ubufData, const char
    *name, const void *data, size_t size, int *storeIndex, UniformFlags
    flags)': names 'char', which has no cute class yet.
  - Qt's 'void QSSGRhiShaderPipeline::setUniformArray(char *ubufData, const
    char *name, const void *data, size_t itemCount,
    QSSGRenderShaderValue::Type type, int *storeIndex)': names 'char', which
    has no cute class yet.
  - Qt's 'void QSSGRhiShaderPipeline::setShaderResources(char *ubufData,
    QSSGBufferManager &theBufferManager, const QByteArray &inPropertyName,
    const QVariant &propertyValue, QSSGRenderShaderValue::Type
    inPropertyType)': names 'char', which has no cute class yet.
  - Qt's 'void QSSGRhiShaderPipeline::ensureCombinedUniformBuffer(QRhiBuffer
    **ubuf)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRhiShaderPipeline::ensureUniformBuffer(QRhiBuffer
    **ubuf)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRhiShaderPipeline::setLightProbeTexture(QRhiTexture
    *texture, QSSGRenderTextureCoordOp hTile, QSSGRenderTextureCoordOp
    vTile)': names the enum 'QSSGRenderTextureCoordOp', whose class cannot be
    named here.
  - Qt's 'QPair<QSSGRenderTextureCoordOp, QSSGRenderTextureCoordOp>
    QSSGRhiShaderPipeline::lightProbeTiling() const': gives a type Python has
    no way to take yet.
  - Qt's 'QRhiTexture **QSSGRhiShaderPipeline::oitImages()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiTexture &QSSGRhiShaderPipeline::extraTextureAt(int index)':
    gives a type Python has no way to take yet.
  - Qt's 'QSSGShaderLightsUniformData
    &QSSGRhiShaderPipeline::lightsUniformData()': gives a type Python has no
    way to take yet.
  - Qt's 'QSSGShaderDirectionalLightsUniformData
    &QSSGRhiShaderPipeline::directionalLightsUniformData()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 54 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRhiShaderPipeline is created at the first use, not by
    'QSSGRhiShaderPipeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRhiShaderPipeline.
  - Each name of Qt's QSSGRhiShaderPipeline that has no cute function yet,
    '__init__', 'context', 'directionalLightsUniformData',
    'ensureCombinedUniformBuffer', 'ensureUniformBuffer', 'lightProbeTiling',
    'lightsUniformData', 'oitImages', 'setLightProbeTexture',
    'setShaderResources', 'setUniform', 'setUniformArray', 'setUniformValue',
    'vertexInputs', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSSGRhiShaderPipeline, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StageFlag(CuteFlags):
    """
    The flags enum 'QSSGRhiShaderPipeline::StageFlag' of Qt, with the 1 names
    Qt gives in it. Qt names the type of its combinations
    'QSSGRhiShaderPipeline::StageFlags'.
    """

    UsedWithoutIa = 0x1

  StageFlags = StageFlag

  class UniformFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGRhiShaderPipeline::UniformFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QSSGRhiShaderPipeline::UniformFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Mat3 = 0x1

  UniformFlags = UniformFlag

  #  The classes Qt writes inside QSSGRhiShaderPipeline, each a class in here
  #  as in C++.

  class CommonUniformIndices(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiShaderPipeline::CommonUniformIndices: a
    plain Python object standing in front of one C++
    QSSGRhiShaderPipeline::CommonUniformIndices.

    C++ hands a QSSGRhiShaderPipeline::CommonUniformIndices around as a copy,
    so every C++ QSSGRhiShaderPipeline::CommonUniformIndices behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiShaderPipeline::CommonUniformIndices yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGRhiShaderPipeline::CommonUniformIndices::~CommonUniformIndices()':
      the destructor: Python removes its C++
      QSSGRhiShaderPipeline::CommonUniformIndices by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRhiShaderPipeline::CommonUniformIndices is created at the
      first use, not by 'QSSGRhiShaderPipeline::CommonUniformIndices(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiShaderPipeline::CommonUniformIndices back
      gives a copy the ritual made for Python, in a new cute
      QSSGRhiShaderPipeline::CommonUniformIndices.
    """

    #  The classes Qt writes inside
    #  QSSGRhiShaderPipeline::CommonUniformIndices, each a class in here as
    #  in C++.

    class ImageIndices(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices: a plain
      Python object standing in front of one C++
      QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices.

      C++ hands a QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices
      around as a copy, so every C++
      QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices behind a cute
      one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's
      QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices::
        ~ImageIndices()': the destructor: Python removes its C++
        QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices by it, and
        has no other use for it.

      What to expect
      --------------

      - The C++ QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices is
        created at the first use, not by
        'QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices back gives
        a copy the ritual made for Python, in a new cute
        QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices'

      #  Qt's '~QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QSSGRhiShaderPipeline::CommonUniformIndices::ImageIndices behind a
      #  cute one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN21QSSGRhiShaderPipeline20CommonUniformIndices12ImageIndicesD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiShaderPipeline::CommonUniformIndices'

    #  Qt's '~QSSGRhiShaderPipeline::CommonUniformIndices()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGRhiShaderPipeline::CommonUniformIndices behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN21QSSGRhiShaderPipeline20CommonUniformIndicesD1Ev')

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

  class InstanceLocations(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiShaderPipeline::InstanceLocations: a plain
    Python object standing in front of one C++
    QSSGRhiShaderPipeline::InstanceLocations.

    C++ hands a QSSGRhiShaderPipeline::InstanceLocations around as a copy, so
    every C++ QSSGRhiShaderPipeline::InstanceLocations behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiShaderPipeline::InstanceLocations yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiShaderPipeline::InstanceLocations::~InstanceLocations()':
      the destructor: Python removes its C++
      QSSGRhiShaderPipeline::InstanceLocations by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRhiShaderPipeline::InstanceLocations is created at the
      first use, not by 'QSSGRhiShaderPipeline::InstanceLocations(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiShaderPipeline::InstanceLocations back gives
      a copy the ritual made for Python, in a new cute
      QSSGRhiShaderPipeline::InstanceLocations.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiShaderPipeline::InstanceLocations'

    #  Qt's '~QSSGRhiShaderPipeline::InstanceLocations()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGRhiShaderPipeline::InstanceLocations behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN21QSSGRhiShaderPipeline17InstanceLocationsD1Ev')

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
  __qt_class__ = 'QSSGRhiShaderPipeline'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiShaderPipeline::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#isNull
    """
    #  bool QSSGRhiShaderPipeline::isNull() const
    return self.uglySide.call('ritual_ZNK21QSSGRhiShaderPipeline6isNullEv')

  def cbeginStages(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage *QSSGRhiShaderPipeline::cbeginStages()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#cbeginStages

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QSSGRhiShaderPipeline::cbeginStages() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline12cbeginStagesEv',
    )
    from ..QtGui import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def cendStages(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage *QSSGRhiShaderPipeline::cendStages()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#cendStages

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QSSGRhiShaderPipeline::cendStages() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline10cendStagesEv',
    )
    from ..QtGui import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def vertexStage(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage *QSSGRhiShaderPipeline::vertexStage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#vertexStage

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QSSGRhiShaderPipeline::vertexStage() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline11vertexStageEv',
    )
    from ..QtGui import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def fragmentStage(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage *QSSGRhiShaderPipeline::fragmentStage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#fragmentStage

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QSSGRhiShaderPipeline::fragmentStage() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline13fragmentStageEv',
    )
    from ..QtGui import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def ub0Size(self) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::ub0Size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#ub0Size
    """
    #  int QSSGRhiShaderPipeline::ub0Size() const
    return self.uglySide.call('ritual_ZNK21QSSGRhiShaderPipeline7ub0SizeEv')

  def ub0LightDataOffset(self) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::ub0LightDataOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#ub0LightDataOffset
    """
    #  int QSSGRhiShaderPipeline::ub0LightDataOffset() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline18ub0LightDataOffsetEv',
    )

  def ub0DirectionalLightDataOffset(self) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::ub0DirectionalLightDataOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html
    """
    #  int QSSGRhiShaderPipeline::ub0DirectionalLightDataOffset() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline29ub0DirectionalLightDataOffsetEv',
    )

  def isLightingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiShaderPipeline::isLightingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#isLightingEnabled
    """
    #  bool QSSGRhiShaderPipeline::isLightingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline17isLightingEnabledEv',
    )

  def lightProbeTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::lightProbeTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#lightProbeTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::lightProbeTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline17lightProbeTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def screenTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::screenTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#screenTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::screenTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline13screenTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def depthTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::depthTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#depthTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::depthTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline12depthTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def normalTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::normalTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#normalTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::normalTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline13normalTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def ssaoTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::ssaoTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#ssaoTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::ssaoTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline11ssaoTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def lightmapTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::lightmapTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#lightmapTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::lightmapTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline15lightmapTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def MotionVectorTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::MotionVectorTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#MotionVectorTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::MotionVectorTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline19MotionVectorTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def shadowMapAtlasTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiShaderPipeline::shadowMapAtlasTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#shadowMapAtlasTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::shadowMapAtlasTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline21shadowMapAtlasTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def shadowMapBlueNoiseTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QSSGRhiShaderPipeline::shadowMapBlueNoiseTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiShaderPipeline::shadowMapBlueNoiseTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline25shadowMapBlueNoiseTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def extraTextureCount(self) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::extraTextureCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#extraTextureCount
    """
    #  int QSSGRhiShaderPipeline::extraTextureCount() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline17extraTextureCountEv',
    )

  @overload(int)
  def extraTextureAt(self, index: int) -> QSSGRhiTexture:
    """
    Calls Qt's 'const QSSGRhiTexture
    &QSSGRhiShaderPipeline::extraTextureAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#extraTextureAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QSSGRhiTexture
      A new cute QSSGRhiTexture around the copy Qt gave back. Python owns it.
    """
    #  const QSSGRhiTexture &QSSGRhiShaderPipeline::extraTextureAt(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline14extraTextureAtEi', index,
    )
    from . import QSSGRhiTexture
    return QSSGRhiTexture._cuteOwning(address)

  def instanceBufferLocations(self) -> InstanceLocations:
    """
    Calls Qt's 'InstanceLocations
    QSSGRhiShaderPipeline::instanceBufferLocations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#instanceBufferLocations

    Returns
    -------

    InstanceLocations
      A new cute QSSGRhiShaderPipeline::InstanceLocations around the copy Qt
      gave back. Python owns it.
    """
    #  InstanceLocations QSSGRhiShaderPipeline::instanceBufferLocations()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRhiShaderPipeline23instanceBufferLocationsEv',
    )
    return QSSGRhiShaderPipeline.InstanceLocations._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setLightsEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setLightsEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setLightsEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSSGRhiShaderPipeline::setLightsEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline16setLightsEnabledEb', enable,
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setScreenTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setScreenTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setScreenTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setScreenTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline16setScreenTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setDepthTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setDepthTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setDepthTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setDepthTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline15setDepthTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setNormalTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setNormalTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setNormalTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setNormalTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline16setNormalTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setSsaoTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setSsaoTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setSsaoTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setSsaoTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline14setSsaoTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setLightmapTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setLightmapTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setLightmapTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setLightmapTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline18setLightmapTextureEP11QRhiTextur'
        'e',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setMotionVectorTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void
    QSSGRhiShaderPipeline::setMotionVectorTexture(QRhiTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setMotionVectorTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setMotionVectorTexture(QRhiTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline22setMotionVectorTextureEP11QRhiTe'
        'xture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setShadowMapAtlasTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void
    QSSGRhiShaderPipeline::setShadowMapAtlasTexture(QRhiTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setShadowMapAtlasTexture(QRhiTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline24setShadowMapAtlasTextureEP11QRhi'
        'Texture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setShadowMapBlueNoiseTexture(
      self,
      texture: Optional[QRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGRhiShaderPipeline::setShadowMapBlueNoiseTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setShadowMapBlueNoiseTexture(QRhiTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline28setShadowMapBlueNoiseTextureEP11'
        'QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture, QRhiTexture, QRhiTexture)
  @overload(QRhiTexture, QRhiTexture, NoneType)
  @overload(QRhiTexture, NoneType, QRhiTexture)
  @overload(QRhiTexture, NoneType, NoneType)
  @overload(NoneType, QRhiTexture, QRhiTexture)
  @overload(NoneType, QRhiTexture, NoneType)
  @overload(NoneType, NoneType, QRhiTexture)
  @overload(NoneType, NoneType, NoneType)
  def setOITImages(
      self,
      accumulator: Optional[QRhiTexture],
      auxiliary: Optional[QRhiTexture],
      counter: Optional[QRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::setOITImages(QRhiTexture
    *accumulator, QRhiTexture *auxiliary, QRhiTexture *counter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#setOITImages

    Parameters
    ----------

    accumulator : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    auxiliary : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    counter : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderPipeline::setOITImages(QRhiTexture *accumulator,
    #      QRhiTexture *auxiliary, QRhiTexture *counter)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline12setOITImagesEP11QRhiTextureS1_S1'
        '_',
        self._addressOf(accumulator), self._addressOf(auxiliary),
        self._addressOf(counter),
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
    Qt's 'QSSGRhiShaderPipeline::QSSGRhiShaderPipeline(QSSGRhiContext
    &context)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.__init__' has no cute function yet. Qt's "
        "'QSSGRhiShaderPipeline::QSSGRhiShaderPipeline(QSSGRhiContext "
        "&context)': takes a type Python has no way to hand over yet.")

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

  @overload(QRhiShaderStage)
  @overload(QRhiShaderStage, StageFlags)
  def addStage(
      self,
      stage: QRhiShaderStage,
      flags: StageFlags = StageFlags(),
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::addStage(const QRhiShaderStage
    &stage, StageFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#addStage

    Parameters
    ----------

    stage : QRhiShaderStage
      Passed on as a value: Qt reads the C++ QRhiShaderStage, which stays
      Python's own.

    flags : StageFlags
      Passed on as its number. May be left out, as in Qt: it is then
      StageFlags().
    """
    #  void QSSGRhiShaderPipeline::addStage(const QRhiShaderStage &stage,
    #      StageFlags flags)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline8addStageERK15QRhiShaderStage6QFla'
        'gsINS_9StageFlagEE',
        self._valueOf(stage), flags.value,
    )

  @overload(str)
  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def bindingForTexture(self, name: Optional[str], hint: int = -1) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::bindingForTexture(const char
    *name, int hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#bindingForTexture

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    hint : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QSSGRhiShaderPipeline::bindingForTexture(const char *name, int
    #      hint)
    return self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline17bindingForTextureEPKci',
        self._bytesOf(name), hint,
    )

  @overload(str)
  @overload(NoneType)
  def bindingForImage(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::bindingForImage(const char
    *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#bindingForImage

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QSSGRhiShaderPipeline::bindingForImage(const char *name)
    return self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline15bindingForImageEPKc',
        self._bytesOf(name),
    )

  def resetExtraTextures(self) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::resetExtraTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#resetExtraTextures
    """
    #  void QSSGRhiShaderPipeline::resetExtraTextures()
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline18resetExtraTexturesEv',
    )

  @overload(QSSGRhiTexture)
  def addExtraTexture(self, t: QSSGRhiTexture) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderPipeline::addExtraTexture(const
    QSSGRhiTexture &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#addExtraTexture

    Parameters
    ----------

    t : QSSGRhiTexture
      Passed on as a value: Qt reads the C++ QSSGRhiTexture, which stays
      Python's own.
    """
    #  void QSSGRhiShaderPipeline::addExtraTexture(const QSSGRhiTexture &t)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline15addExtraTextureERK14QSSGRhiTextu'
        're',
        self._valueOf(t),
    )

  @overload(QByteArray)
  def offsetOfUniform(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QSSGRhiShaderPipeline::offsetOfUniform(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderpipeline.html#offsetOfUniform

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QSSGRhiShaderPipeline::offsetOfUniform(const QByteArray &name)
    return self.uglySide.call(
        'ritual_ZN21QSSGRhiShaderPipeline15offsetOfUniformERK10QByteArray',
        self._valueOf(name),
    )

  @staticmethod
  def context(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiContext &QSSGRhiShaderPipeline::context() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.context' has no cute function yet. Qt's "
        "'QSSGRhiContext &QSSGRhiShaderPipeline::context() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def directionalLightsUniformData(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderDirectionalLightsUniformData
    &QSSGRhiShaderPipeline::directionalLightsUniformData()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.directionalLightsUniformData' has no cute "
        "function yet. Qt's 'QSSGShaderDirectionalLightsUniformData "
        "&QSSGRhiShaderPipeline::directionalLightsUniformData()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def ensureCombinedUniformBuffer(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::ensureCombinedUniformBuffer(QRhiBuffer
    **ubuf)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.ensureCombinedUniformBuffer' has no cute "
        "function yet. Qt's 'void "
        "QSSGRhiShaderPipeline::ensureCombinedUniformBuffer(QRhiBuffer "
        "**ubuf)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def ensureUniformBuffer(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::ensureUniformBuffer(QRhiBuffer
    **ubuf)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.ensureUniformBuffer' has no cute function "
        "yet. Qt's 'void "
        "QSSGRhiShaderPipeline::ensureUniformBuffer(QRhiBuffer **ubuf)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def lightProbeTiling(*__, **_) -> Never:
    """
    Qt's 'QPair<QSSGRenderTextureCoordOp, QSSGRenderTextureCoordOp>
    QSSGRhiShaderPipeline::lightProbeTiling() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.lightProbeTiling' has no cute function yet. "
        "Qt's 'QPair<QSSGRenderTextureCoordOp, QSSGRenderTextureCoordOp> "
        "QSSGRhiShaderPipeline::lightProbeTiling() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def lightsUniformData(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderLightsUniformData
    &QSSGRhiShaderPipeline::lightsUniformData()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.lightsUniformData' has no cute function "
        "yet. Qt's 'QSSGShaderLightsUniformData "
        "&QSSGRhiShaderPipeline::lightsUniformData()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def oitImages(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture **QSSGRhiShaderPipeline::oitImages()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.oitImages' has no cute function yet. Qt's "
        "'QRhiTexture **QSSGRhiShaderPipeline::oitImages()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setLightProbeTexture(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::setLightProbeTexture(QRhiTexture
    *texture, QSSGRenderTextureCoordOp hTile, QSSGRenderTextureCoordOp
    vTile)': names the enum 'QSSGRenderTextureCoordOp', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.setLightProbeTexture' has no cute function "
        "yet. Qt's 'void "
        "QSSGRhiShaderPipeline::setLightProbeTexture(QRhiTexture *texture, "
        "QSSGRenderTextureCoordOp hTile, QSSGRenderTextureCoordOp vTile)': "
        "names the enum 'QSSGRenderTextureCoordOp', whose class cannot be "
        "named here.")

  @staticmethod
  def setShaderResources(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::setShaderResources(char *ubufData,
    QSSGBufferManager &theBufferManager, const QByteArray &inPropertyName,
    const QVariant &propertyValue, QSSGRenderShaderValue::Type
    inPropertyType)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.setShaderResources' has no cute function "
        "yet. Qt's 'void QSSGRhiShaderPipeline::setShaderResources(char "
        "*ubufData, QSSGBufferManager &theBufferManager, const QByteArray "
        "&inPropertyName, const QVariant &propertyValue, "
        "QSSGRenderShaderValue::Type inPropertyType)': names 'char', which "
        "has no cute class yet.")

  @staticmethod
  def setUniform(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::setUniform(char *ubufData, const char
    *name, const void *data, size_t size, int *storeIndex, UniformFlags
    flags)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.setUniform' has no cute function yet. Qt's "
        "'void QSSGRhiShaderPipeline::setUniform(char *ubufData, const char "
        "*name, const void *data, size_t size, int *storeIndex, "
        "UniformFlags flags)': names 'char', which has no cute class yet.")

  @staticmethod
  def setUniformArray(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::setUniformArray(char *ubufData, const
    char *name, const void *data, size_t itemCount,
    QSSGRenderShaderValue::Type type, int *storeIndex)': names 'char', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.setUniformArray' has no cute function yet. "
        "Qt's 'void QSSGRhiShaderPipeline::setUniformArray(char *ubufData, "
        "const char *name, const void *data, size_t itemCount, "
        "QSSGRenderShaderValue::Type type, int *storeIndex)': names 'char', "
        "which has no cute class yet.")

  @staticmethod
  def setUniformValue(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiShaderPipeline::setUniformValue(char *ubufData, const
    char *name, const QVariant &value, QSSGRenderShaderValue::Type type)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.setUniformValue' has no cute function yet. "
        "Qt's 'void QSSGRhiShaderPipeline::setUniformValue(char *ubufData, "
        "const char *name, const QVariant &value, "
        "QSSGRenderShaderValue::Type type)': names 'char', which has no "
        "cute class yet.")

  @staticmethod
  def vertexInputs(*__, **_) -> Never:
    """
    Qt's 'const QHash<QSSGRhiInputAssemblerState::InputSemantic,
    QShaderDescription::InOutVariable> &QSSGRhiShaderPipeline::vertexInputs()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiShaderPipeline.vertexInputs' has no cute function yet. "
        "Qt's 'const QHash<QSSGRhiInputAssemblerState::InputSemantic, "
        "QShaderDescription::InOutVariable> "
        "&QSSGRhiShaderPipeline::vertexInputs() const': gives a type Python "
        "has no way to take yet.")
