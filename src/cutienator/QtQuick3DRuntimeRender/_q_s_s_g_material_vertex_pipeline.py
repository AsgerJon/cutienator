"""
QSSGMaterialVertexPipeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGMaterialVertexPipeline to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from . import QSSGShaderKeyVertexAttribute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QSSGProgramGenerator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSSGMaterialVertexPipeline(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMaterialVertexPipeline: a plain Python object
  standing in front of one C++ QSSGMaterialVertexPipeline.

  C++ hands a QSSGMaterialVertexPipeline around as a copy, so every C++
  QSSGMaterialVertexPipeline behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGMaterialVertexPipeline that has a ritual and
  that Python can call so far, 19 names in all: 'setCode', 'hasCode',
  'programGenerator', 'generateObjectNormal', 'generateDepth', 'addIncoming',
  'addOutgoing', 'addUniform', 'addUniformArray', 'addInclude',
  'addFunction', 'addConstantBuffer', 'addConstantBufferParam',
  'addDefinition', 'append', 'assignOutput', 'endFragmentGeneration',
  'addInterpolationParameter', 'addFlatParameter'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMaterialVertexPipeline::QSSGMaterialVertexPipeline(
    QSSGProgramGenerator &inProgram, const
    QSSGShaderDefaultMaterialKeyProperties &materialProperties,
    QSSGShaderMaterialAdapter *materialAdapter)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGMaterialVertexPipeline::~QSSGMaterialVertexPipeline()': the
    destructor: Python removes its C++ QSSGMaterialVertexPipeline by it, and
    has no other use for it.
  - Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::vertex()':
    gives a type Python has no way to take yet.
  - Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::fragment()':
    gives a type Python has no way to take yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateUVCoords(quint32 inUVSet,
    const QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateLightmapUVCoords(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateEnvMapReflection(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateViewVector(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateWorldNormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateWorldPosition(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateShadowWorldPosition(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QSSGMaterialVertexPipeline::generateVarTangentAndBinormal(const
    QSSGShaderDefaultMaterialKey &inKey, bool &genTangent, bool
    &genBinormal)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::generateVertexColor(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSSGStageGeneratorBase
    &QSSGMaterialVertexPipeline::operator<<(const QByteArray &data)': gives a
    type Python has no way to take yet.
  - Qt's 'QSSGShaderGeneratorStage QSSGMaterialVertexPipeline::stage()
    const': gives the enum 'QSSGShaderGeneratorStage', whose class cannot be
    named here.
  - Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::activeStage()':
    gives a type Python has no way to take yet.
  - Qt's 'void QSSGMaterialVertexPipeline::doGenerateWorldNormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::doGenerateVarTangent(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGMaterialVertexPipeline::doGenerateVarBinormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QSSGMaterialVertexPipeline::hasAttributeInKey(
    QSSGShaderKeyVertexAttribute::VertexAttributeBits inAttr, const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  3 of the 42 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSSGMaterialVertexPipeline is created at the first use, not by
    'QSSGMaterialVertexPipeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMaterialVertexPipeline back gives a copy the
    ritual made for Python, in a new cute QSSGMaterialVertexPipeline.
  - Each name of Qt's QSSGMaterialVertexPipeline that has no cute function
    yet, '__init__', 'activeStage', 'beginFragmentGeneration',
    'beginVertexGeneration', 'doGenerateVarBinormal', 'doGenerateVarTangent',
    'doGenerateWorldNormal', 'endVertexGeneration', 'fragment',
    'generateEnvMapReflection', 'generateLightmapUVCoords',
    'generateShadowWorldPosition', 'generateUVCoords',
    'generateVarTangentAndBinormal', 'generateVertexColor',
    'generateViewVector', 'generateWorldNormal', 'generateWorldPosition',
    'hasAttributeInKey', 'stage', 'vertex', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGMaterialVertexPipeline, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class GenerationFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGMaterialVertexPipeline::GenerationFlag' of Qt, with
    the 11 names Qt gives in it. Qt names the type of its combinations
    'QSSGMaterialVertexPipeline::GenerationFlags'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    UVCoords = 0x1
    EnvMapReflection = 0x2
    ViewVector = 0x4
    WorldNormal = 0x8
    ObjectNormal = 0x10
    WorldPosition = 0x20
    TangentBinormal = 0x40
    UVCoords1 = 0x80
    VertexColor = 0x100
    PerspDivDepth = 0x200
    PerspDivWorldPos = 0x400

  GenerationFlags = GenerationFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMaterialVertexPipeline'

  #  Qt's '~QSSGMaterialVertexPipeline()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGMaterialVertexPipeline behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QSSGMaterialVertexPipelineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def programGenerator(self) -> Optional[QSSGProgramGenerator]:
    """
    Calls Qt's 'QSSGProgramGenerator
    *QSSGMaterialVertexPipeline::programGenerator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#programGenerator

    Returns
    -------

    Optional[QSSGProgramGenerator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGProgramGenerator *QSSGMaterialVertexPipeline::programGenerator()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QSSGMaterialVertexPipeline16programGeneratorEv',
    )
    from . import QSSGProgramGenerator
    return QSSGProgramGenerator._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(GenerationFlag)
  def setCode(self, inCode: GenerationFlag) -> bool:
    """
    Calls Qt's 'bool QSSGMaterialVertexPipeline::setCode(GenerationFlag
    inCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#setCode

    Parameters
    ----------

    inCode : GenerationFlag
      Passed on as its number.
    """
    #  bool QSSGMaterialVertexPipeline::setCode(GenerationFlag inCode)
    return self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline7setCodeENS_14GenerationFlagE',
        inCode.value,
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
    Qt's 'QSSGMaterialVertexPipeline::QSSGMaterialVertexPipeline(
    QSSGProgramGenerator &inProgram, const
    QSSGShaderDefaultMaterialKeyProperties &materialProperties,
    QSSGShaderMaterialAdapter *materialAdapter)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.__init__' has no cute function yet. "
        "Qt's "
        "'QSSGMaterialVertexPipeline::QSSGMaterialVertexPipeline(QSSGProgram"
        "Generator &inProgram, const QSSGShaderDefaultMaterialKeyProperties "
        "&materialProperties, QSSGShaderMaterialAdapter *materialAdapter)': "
        "takes a type Python has no way to hand over yet.")

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

  @overload(GenerationFlag)
  def hasCode(self, inCode: GenerationFlag) -> bool:
    """
    Calls Qt's 'bool QSSGMaterialVertexPipeline::hasCode(GenerationFlag
    inCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#hasCode

    Parameters
    ----------

    inCode : GenerationFlag
      Passed on as its number.
    """
    #  bool QSSGMaterialVertexPipeline::hasCode(GenerationFlag inCode)
    return self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline7hasCodeENS_14GenerationFlagE',
        inCode.value,
    )

  def generateObjectNormal(self) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::generateObjectNormal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html
    """
    #  void QSSGMaterialVertexPipeline::generateObjectNormal()
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline20generateObjectNormalEv',
    )

  def generateDepth(self) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::generateDepth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#generateDepth
    """
    #  void QSSGMaterialVertexPipeline::generateDepth()
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline13generateDepthEv',
    )

  @overload(QByteArray, QByteArray)
  def addIncoming(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addIncoming(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addIncoming

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addIncoming(const QByteArray &name,
    #      const QByteArray &type)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline11addIncomingERK10QByteArrayS'
        '2_',
        self._valueOf(name), self._valueOf(type),
    )

  @overload(QByteArray, QByteArray)
  def addOutgoing(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addOutgoing(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addOutgoing

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addOutgoing(const QByteArray &name,
    #      const QByteArray &type)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline11addOutgoingERK10QByteArrayS'
        '2_',
        self._valueOf(name), self._valueOf(type),
    )

  @overload(QByteArray, QByteArray)
  def addUniform(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addUniform(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addUniform

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addUniform(const QByteArray &name,
    #      const QByteArray &type)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline10addUniformERK10QByteArrayS2'
        '_',
        self._valueOf(name), self._valueOf(type),
    )

  @overload(QByteArray, QByteArray, int)
  def addUniformArray(
      self,
      name: QByteArray,
      type: QByteArray,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addUniformArray(const
    QByteArray &name, const QByteArray &type, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addUniformArray

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    size : int
      Passed on as it is.
    """
    #  void QSSGMaterialVertexPipeline::addUniformArray(const QByteArray
    #      &name, const QByteArray &type, quint32 size)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline15addUniformArrayERK10QByteAr'
        'rayS2_j',
        self._valueOf(name), self._valueOf(type), size,
    )

  @overload(QByteArray)
  def addInclude(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addInclude(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addInclude

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addInclude(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline10addIncludeERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QByteArray)
  def addFunction(self, functionName: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addFunction(const QByteArray
    &functionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addFunction

    Parameters
    ----------

    functionName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addFunction(const QByteArray
    #      &functionName)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline11addFunctionERK10QByteArray',
        self._valueOf(functionName),
    )

  @overload(QByteArray, QByteArray)
  def addConstantBuffer(self, name: QByteArray, layout: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addConstantBuffer(const
    QByteArray &name, const QByteArray &layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addConstantBuffer

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    layout : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addConstantBuffer(const QByteArray
    #      &name, const QByteArray &layout)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline17addConstantBufferERK10QByte'
        'ArrayS2_',
        self._valueOf(name), self._valueOf(layout),
    )

  @overload(QByteArray, QByteArray, QByteArray)
  def addConstantBufferParam(
      self,
      cbName: QByteArray,
      paramName: QByteArray,
      type: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addConstantBufferParam(const
    QByteArray &cbName, const QByteArray &paramName, const QByteArray
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html

    Parameters
    ----------

    cbName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    paramName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addConstantBufferParam(const
    #      QByteArray &cbName, const QByteArray &paramName, const QByteArray
    #      &type)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline22addConstantBufferParamERK10'
        'QByteArrayS2_S2_',
        self._valueOf(cbName), self._valueOf(paramName), self._valueOf(type),
    )

  @overload(QByteArray)
  @overload(QByteArray, QByteArray)
  def addDefinition(
      self,
      name: QByteArray,
      value: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addDefinition(const
    QByteArray &name, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addDefinition

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QSSGMaterialVertexPipeline::addDefinition(const QByteArray &name,
    #      const QByteArray &value)
    if value is None:
      from ..QtCore import QByteArray
      value = QByteArray()
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline13addDefinitionERK10QByteArra'
        'yS2_',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(QByteArray)
  def append(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::append(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#append

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::append(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline6appendERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray, QByteArray)
  def assignOutput(
      self,
      inVarName: QByteArray,
      inVarValueExpr: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::assignOutput(const
    QByteArray &inVarName, const QByteArray &inVarValueExpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#assignOutput

    Parameters
    ----------

    inVarName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    inVarValueExpr : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::assignOutput(const QByteArray
    #      &inVarName, const QByteArray &inVarValueExpr)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline12assignOutputERK10QByteArray'
        'S2_',
        self._valueOf(inVarName), self._valueOf(inVarValueExpr),
    )

  def endFragmentGeneration(self) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::endFragmentGeneration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html
    """
    #  void QSSGMaterialVertexPipeline::endFragmentGeneration()
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline21endFragmentGenerationEv',
    )

  @overload(QByteArray, QByteArray)
  def addInterpolationParameter(
      self,
      inParamName: QByteArray,
      inParamType: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QSSGMaterialVertexPipeline::addInterpolationParameter(const QByteArray
    &inParamName, const QByteArray &inParamType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html

    Parameters
    ----------

    inParamName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    inParamType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addInterpolationParameter(const
    #      QByteArray &inParamName, const QByteArray &inParamType)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline25addInterpolationParameterER'
        'K10QByteArrayS2_',
        self._valueOf(inParamName), self._valueOf(inParamType),
    )

  @overload(QByteArray, QByteArray)
  def addFlatParameter(
      self,
      inParamName: QByteArray,
      inParamType: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QSSGMaterialVertexPipeline::addFlatParameter(const
    QByteArray &inParamName, const QByteArray &inParamType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialvertexpipeline.html#addFlatParameter

    Parameters
    ----------

    inParamName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    inParamType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGMaterialVertexPipeline::addFlatParameter(const QByteArray
    #      &inParamName, const QByteArray &inParamType)
    self.uglySide.call(
        'ritual_ZN26QSSGMaterialVertexPipeline16addFlatParameterERK10QByteA'
        'rrayS2_',
        self._valueOf(inParamName), self._valueOf(inParamType),
    )

  @staticmethod
  def activeStage(*__, **_) -> Never:
    """
    Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::activeStage()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.activeStage' has no cute function yet. "
        "Qt's 'QSSGStageGeneratorBase "
        "&QSSGMaterialVertexPipeline::activeStage()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def beginFragmentGeneration(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::beginFragmentGeneration(
    QSSGShaderLibraryManager &shaderLibraryManager,
    QSSGRenderLayer::OITMethod oitMethod)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'insertAmbientLightProcessorArgs'; did you mean
    'insertDirectionalLightProcessorArgs'?.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.beginFragmentGeneration' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::beginFragmentGeneration(QSSGShaderLibra"
        "ryManager &shaderLibraryManager, QSSGRenderLayer::OITMethod "
        "oitMethod)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'insertAmbientLightProcessorArgs'; did you mean "
        "'insertDirectionalLightProcessorArgs'?.")

  @staticmethod
  def beginVertexGeneration(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::beginVertexGeneration(const
    QSSGShaderDefaultMaterialKey &inKey, const QSSGShaderFeatures
    &inFeatureSet, QSSGShaderLibraryManager &shaderLibraryManager)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'insertVertexInstancedMainArgs'.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.beginVertexGeneration' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::beginVertexGeneration(const "
        "QSSGShaderDefaultMaterialKey &inKey, const QSSGShaderFeatures "
        "&inFeatureSet, QSSGShaderLibraryManager &shaderLibraryManager)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'insertVertexInstancedMainArgs'.")

  @staticmethod
  def doGenerateVarBinormal(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::doGenerateVarBinormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.doGenerateVarBinormal' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::doGenerateVarBinormal(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def doGenerateVarTangent(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::doGenerateVarTangent(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.doGenerateVarTangent' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::doGenerateVarTangent(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def doGenerateWorldNormal(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::doGenerateWorldNormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.doGenerateWorldNormal' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::doGenerateWorldNormal(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def endVertexGeneration(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::endVertexGeneration()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'customMainCallWithArguments'.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.endVertexGeneration' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::endVertexGeneration()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'customMainCallWithArguments'.")

  @staticmethod
  def fragment(*__, **_) -> Never:
    """
    Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::fragment()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.fragment' has no cute function yet. "
        "Qt's 'QSSGStageGeneratorBase "
        "&QSSGMaterialVertexPipeline::fragment()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def generateEnvMapReflection(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateEnvMapReflection(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateEnvMapReflection' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateEnvMapReflection(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateLightmapUVCoords(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateLightmapUVCoords(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateLightmapUVCoords' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateLightmapUVCoords(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateShadowWorldPosition(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateShadowWorldPosition(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateShadowWorldPosition' has no "
        "cute function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateShadowWorldPosition(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateUVCoords(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateUVCoords(quint32 inUVSet,
    const QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateUVCoords' has no cute function "
        "yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateUVCoords(quint32 inUVSet, "
        "const QSSGShaderDefaultMaterialKey &inKey)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def generateVarTangentAndBinormal(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGMaterialVertexPipeline::generateVarTangentAndBinormal(const
    QSSGShaderDefaultMaterialKey &inKey, bool &genTangent, bool
    &genBinormal)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateVarTangentAndBinormal' has no "
        "cute function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateVarTangentAndBinormal(const "
        "QSSGShaderDefaultMaterialKey &inKey, bool &genTangent, bool "
        "&genBinormal)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def generateVertexColor(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateVertexColor(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateVertexColor' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateVertexColor(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateViewVector(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateViewVector(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateViewVector' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateViewVector(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateWorldNormal(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateWorldNormal(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateWorldNormal' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateWorldNormal(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def generateWorldPosition(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialVertexPipeline::generateWorldPosition(const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.generateWorldPosition' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialVertexPipeline::generateWorldPosition(const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def hasAttributeInKey(*__, **_) -> Never:
    """
    Qt's 'bool QSSGMaterialVertexPipeline::hasAttributeInKey(
    QSSGShaderKeyVertexAttribute::VertexAttributeBits inAttr, const
    QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.hasAttributeInKey' has no cute "
        "function yet. Qt's 'bool "
        "QSSGMaterialVertexPipeline::hasAttributeInKey(QSSGShaderKeyVertexAt"
        "tribute::VertexAttributeBits inAttr, const "
        "QSSGShaderDefaultMaterialKey &inKey)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def stage(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderGeneratorStage QSSGMaterialVertexPipeline::stage()
    const': gives the enum 'QSSGShaderGeneratorStage', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.stage' has no cute function yet. Qt's "
        "'QSSGShaderGeneratorStage QSSGMaterialVertexPipeline::stage() "
        "const': gives the enum 'QSSGShaderGeneratorStage', whose class "
        "cannot be named here.")

  @staticmethod
  def vertex(*__, **_) -> Never:
    """
    Qt's 'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::vertex()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialVertexPipeline.vertex' has no cute function yet. Qt's "
        "'QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::vertex()': "
        "gives a type Python has no way to take yet.")
