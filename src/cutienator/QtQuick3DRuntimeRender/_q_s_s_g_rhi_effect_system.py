"""
QSSGRhiEffectSystem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiEffectSystem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QRhiTexture
from ..QtQuick3DUtils import QSSGRenderTextureFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize
  from . import QSSGApplyInstanceValue, QSSGApplyValue, QSSGBindShader
  from . import QSSGRenderEffect, QSSGRhiSamplerDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGApplyInstanceValue = WAIT['QSSGApplyInstanceValue']
  QSSGApplyValue = WAIT['QSSGApplyValue']
  QSSGBindShader = WAIT['QSSGBindShader']
  QSSGRenderEffect = WAIT['QSSGRenderEffect']
  QSSGRhiSamplerDescription = WAIT['QSSGRhiSamplerDescription']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiEffectSystem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiEffectSystem: a plain Python object standing
  in front of one C++ QSSGRhiEffectSystem.

  C++ hands a QSSGRhiEffectSystem around as a copy, so every C++
  QSSGRhiEffectSystem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiEffectSystem that has a ritual and that
  Python can call so far, 9 names in all: 'setup', 'overriddenOutputFormat',
  'releaseResources', 'applyInstanceValueCmd', 'applyValueCmd',
  'bindShaderCmd', 'addCommonEffectUniforms', 'addTextureToShaderPipeline',
  'releaseTextures'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiEffectSystem::QSSGRhiEffectSystem(const
    std::shared_ptr<QSSGRenderContextInterface> &sgContext)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGRhiEffectSystem::~QSSGRhiEffectSystem()': the destructor:
    Python removes its C++ QSSGRhiEffectSystem by it, and has no other use
    for it.
  - Qt's 'QRhiTexture *QSSGRhiEffectSystem::process(const QSSGRenderLayer
    &layer, QRhiTexture *inTexture, QRhiTexture *inDepthTexture, QRhiTexture
    *inNormalTexture, QRhiTexture *inMotionVectorTexture)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRhiEffectSystem::buildShaderForEffect(const QSSGBindShader &inCmd,
    QSSGProgramGenerator &generator, QSSGShaderLibraryManager &shaderLib,
    QSSGShaderCache &shaderCache, bool isYUpInFramebuffer, int viewCount)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::doRenderEffect(const
    QSSGRenderEffect *inEffect, QSSGRhiEffectTexture *inTexture, quint8
    viewCount)': names 'QSSGRhiEffectTexture', which has no cute class yet.
  - Qt's 'void QSSGRhiEffectSystem::allocateBufferCmd(const
    QSSGAllocateBuffer *inCmd, QSSGRhiEffectTexture *inTexture, const
    QSSGRenderEffect *inEffect, quint8 viewCount)': names
    'QSSGRhiEffectTexture', which has no cute class yet.
  - Qt's 'void QSSGRhiEffectSystem::renderCmd(const QSSGRenderEffect
    *inEffect, QSSGRhiEffectTexture *inTexture, QSSGRhiEffectTexture *target,
    quint8 viewCount)': names 'QSSGRhiEffectTexture', which has no cute class
    yet.
  - Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::findTexture(const
    QByteArray &bufferName)': gives 'QSSGRhiEffectTexture', which has no cute
    class yet.
  - Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::getTexture(const
    QByteArray &bufferName, const QSize &size, QRhiTexture::Format format,
    bool isFinalOutput, const QSSGRenderEffect *inEffect, quint8 viewCount)':
    gives 'QSSGRhiEffectTexture', which has no cute class yet.
  - Qt's 'void QSSGRhiEffectSystem::releaseTexture(QSSGRhiEffectTexture
    *texture)': names 'QSSGRhiEffectTexture', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSSGRhiEffectSystem is created at the first use, not by
    'QSSGRhiEffectSystem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiEffectSystem back gives a copy the ritual made
    for Python, in a new cute QSSGRhiEffectSystem.
  - Each name of Qt's QSSGRhiEffectSystem that has no cute function yet,
    '__init__', 'allocateBufferCmd', 'buildShaderForEffect',
    'doRenderEffect', 'findTexture', 'getTexture', 'process',
    'releaseTexture', 'renderCmd', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRenderEffect)
  @overload(NoneType)
  def overriddenOutputFormat(
      inEffect: Optional[QSSGRenderEffect],
  ) -> QSSGRenderTextureFormat.Format:
    """
    Calls Qt's 'QSSGRenderTextureFormat::Format
    QSSGRhiEffectSystem::overriddenOutputFormat(const QSSGRenderEffect
    *inEffect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#overriddenOutputFormat

    Parameters
    ----------

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGRenderTextureFormat.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderTextureFormat.Format(number)' gives.
    """
    #  QSSGRenderTextureFormat::Format
    #      QSSGRhiEffectSystem::overriddenOutputFormat(const QSSGRenderEffect
    #      *inEffect)
    return QSSGRenderTextureFormat.Format(Rituals.call(
        'ritual_ZN19QSSGRhiEffectSystem22overriddenOutputFormatEPK16QSSGRen'
        'derEffect',
        CuteMixin._addressOf(inEffect),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiEffectSystem'

  #  Qt's '~QSSGRhiEffectSystem()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiEffectSystem behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRhiEffectSystemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiEffectSystem::QSSGRhiEffectSystem(const
    std::shared_ptr<QSSGRenderContextInterface> &sgContext)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.__init__' has no cute function yet. Qt's "
        "'QSSGRhiEffectSystem::QSSGRhiEffectSystem(const "
        "std::shared_ptr<QSSGRenderContextInterface> &sgContext)': takes a "
        "type Python has no way to hand over yet.")

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

  @overload(QSize)
  def setup(self, outputSize: QSize) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::setup(QSize outputSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhieffectsystem.html#setup

    Parameters
    ----------

    outputSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSSGRhiEffectSystem::setup(QSize outputSize)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem5setupE5QSize',
        self._valueOf(outputSize),
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#releaseResources
    """
    #  void QSSGRhiEffectSystem::releaseResources()
    self.uglySide.call('ritual_ZN19QSSGRhiEffectSystem16releaseResourcesEv')

  @overload(QSSGApplyInstanceValue, QSSGRenderEffect)
  @overload(QSSGApplyInstanceValue, NoneType)
  @overload(NoneType, QSSGRenderEffect)
  @overload(NoneType, NoneType)
  def applyInstanceValueCmd(
      self,
      inCmd: Optional[QSSGApplyInstanceValue],
      inEffect: Optional[QSSGRenderEffect],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::applyInstanceValueCmd(const
    QSSGApplyInstanceValue *inCmd, const QSSGRenderEffect *inEffect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#applyInstanceValueCmd

    Parameters
    ----------

    inCmd : Optional[QSSGApplyInstanceValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiEffectSystem::applyInstanceValueCmd(const
    #      QSSGApplyInstanceValue *inCmd, const QSSGRenderEffect *inEffect)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem21applyInstanceValueCmdEPK22QSSGAppl'
        'yInstanceValuePK16QSSGRenderEffect',
        self._addressOf(inCmd), self._addressOf(inEffect),
    )

  @overload(QSSGApplyValue, QSSGRenderEffect)
  @overload(QSSGApplyValue, NoneType)
  @overload(NoneType, QSSGRenderEffect)
  @overload(NoneType, NoneType)
  def applyValueCmd(
      self,
      inCmd: Optional[QSSGApplyValue],
      inEffect: Optional[QSSGRenderEffect],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::applyValueCmd(const QSSGApplyValue
    *inCmd, const QSSGRenderEffect *inEffect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#applyValueCmd

    Parameters
    ----------

    inCmd : Optional[QSSGApplyValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiEffectSystem::applyValueCmd(const QSSGApplyValue *inCmd,
    #      const QSSGRenderEffect *inEffect)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem13applyValueCmdEPK14QSSGApplyValuePK'
        '16QSSGRenderEffect',
        self._addressOf(inCmd), self._addressOf(inEffect),
    )

  @overload(QSSGBindShader, QSSGRenderEffect, int)
  @overload(QSSGBindShader, NoneType, int)
  @overload(NoneType, QSSGRenderEffect, int)
  @overload(NoneType, NoneType, int)
  def bindShaderCmd(
      self,
      inCmd: Optional[QSSGBindShader],
      inEffect: Optional[QSSGRenderEffect],
      viewCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::bindShaderCmd(const QSSGBindShader
    *inCmd, const QSSGRenderEffect *inEffect, quint8 viewCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#bindShaderCmd

    Parameters
    ----------

    inCmd : Optional[QSSGBindShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewCount : int
      Passed on as it is.
    """
    #  void QSSGRhiEffectSystem::bindShaderCmd(const QSSGBindShader *inCmd,
    #      const QSSGRenderEffect *inEffect, quint8 viewCount)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem13bindShaderCmdEPK14QSSGBindShaderPK'
        '16QSSGRenderEffecth',
        self._addressOf(inCmd), self._addressOf(inEffect), viewCount,
    )

  @overload(QSSGRenderEffect, QSize, QSize, int)
  @overload(NoneType, QSize, QSize, int)
  def addCommonEffectUniforms(
      self,
      inEffect: Optional[QSSGRenderEffect],
      inputSize: QSize,
      outputSize: QSize,
      viewCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::addCommonEffectUniforms(const
    QSSGRenderEffect *inEffect, const QSize &inputSize, const QSize
    &outputSize, quint8 viewCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#addCommonEffectUniforms

    Parameters
    ----------

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inputSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    outputSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    viewCount : int
      Passed on as it is.
    """
    #  void QSSGRhiEffectSystem::addCommonEffectUniforms(const
    #      QSSGRenderEffect *inEffect, const QSize &inputSize, const QSize
    #      &outputSize, quint8 viewCount)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem23addCommonEffectUniformsEPK16QSSGRe'
        'nderEffectRK5QSizeS5_h',
        self._addressOf(inEffect), self._valueOf(inputSize),
        self._valueOf(outputSize), viewCount,
    )

  @overload(QByteArray, QRhiTexture, QSSGRhiSamplerDescription)
  @overload(QByteArray, NoneType, QSSGRhiSamplerDescription)
  def addTextureToShaderPipeline(
      self,
      name: QByteArray,
      texture: Optional[QRhiTexture],
      samplerDesc: QSSGRhiSamplerDescription,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::addTextureToShaderPipeline(const
    QByteArray &name, QRhiTexture *texture, const QSSGRhiSamplerDescription
    &samplerDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    samplerDesc : QSSGRhiSamplerDescription
      Passed on as a value: Qt reads the C++ QSSGRhiSamplerDescription, which
      stays Python's own.
    """
    #  void QSSGRhiEffectSystem::addTextureToShaderPipeline(const QByteArray
    #      &name, QRhiTexture *texture, const QSSGRhiSamplerDescription
    #      &samplerDesc)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiEffectSystem26addTextureToShaderPipelineERK10QBy'
        'teArrayP11QRhiTextureRK25QSSGRhiSamplerDescription',
        self._valueOf(name), self._addressOf(texture),
        self._valueOf(samplerDesc),
    )

  def releaseTextures(self) -> None:
    """
    Calls Qt's 'void QSSGRhiEffectSystem::releaseTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhieffectsystem.html#releaseTextures
    """
    #  void QSSGRhiEffectSystem::releaseTextures()
    self.uglySide.call('ritual_ZN19QSSGRhiEffectSystem15releaseTexturesEv')

  @staticmethod
  def allocateBufferCmd(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiEffectSystem::allocateBufferCmd(const
    QSSGAllocateBuffer *inCmd, QSSGRhiEffectTexture *inTexture, const
    QSSGRenderEffect *inEffect, quint8 viewCount)': names
    'QSSGRhiEffectTexture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.allocateBufferCmd' has no cute function yet. "
        "Qt's 'void QSSGRhiEffectSystem::allocateBufferCmd(const "
        "QSSGAllocateBuffer *inCmd, QSSGRhiEffectTexture *inTexture, const "
        "QSSGRenderEffect *inEffect, quint8 viewCount)': names "
        "'QSSGRhiEffectTexture', which has no cute class yet.")

  @staticmethod
  def buildShaderForEffect(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRhiEffectSystem::buildShaderForEffect(const QSSGBindShader &inCmd,
    QSSGProgramGenerator &generator, QSSGShaderLibraryManager &shaderLib,
    QSSGShaderCache &shaderCache, bool isYUpInFramebuffer, int viewCount)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.buildShaderForEffect' has no cute function "
        "yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRhiEffectSystem::buildShaderForEffect(const QSSGBindShader "
        "&inCmd, QSSGProgramGenerator &generator, QSSGShaderLibraryManager "
        "&shaderLib, QSSGShaderCache &shaderCache, bool isYUpInFramebuffer, "
        "int viewCount)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def doRenderEffect(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::doRenderEffect(const
    QSSGRenderEffect *inEffect, QSSGRhiEffectTexture *inTexture, quint8
    viewCount)': names 'QSSGRhiEffectTexture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.doRenderEffect' has no cute function yet. "
        "Qt's 'QSSGRhiEffectTexture "
        "*QSSGRhiEffectSystem::doRenderEffect(const QSSGRenderEffect "
        "*inEffect, QSSGRhiEffectTexture *inTexture, quint8 viewCount)': "
        "names 'QSSGRhiEffectTexture', which has no cute class yet.")

  @staticmethod
  def findTexture(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::findTexture(const
    QByteArray &bufferName)': gives 'QSSGRhiEffectTexture', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.findTexture' has no cute function yet. Qt's "
        "'QSSGRhiEffectTexture *QSSGRhiEffectSystem::findTexture(const "
        "QByteArray &bufferName)': gives 'QSSGRhiEffectTexture', which has "
        "no cute class yet.")

  @staticmethod
  def getTexture(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiEffectTexture *QSSGRhiEffectSystem::getTexture(const
    QByteArray &bufferName, const QSize &size, QRhiTexture::Format format,
    bool isFinalOutput, const QSSGRenderEffect *inEffect, quint8 viewCount)':
    gives 'QSSGRhiEffectTexture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.getTexture' has no cute function yet. Qt's "
        "'QSSGRhiEffectTexture *QSSGRhiEffectSystem::getTexture(const "
        "QByteArray &bufferName, const QSize &size, QRhiTexture::Format "
        "format, bool isFinalOutput, const QSSGRenderEffect *inEffect, "
        "quint8 viewCount)': gives 'QSSGRhiEffectTexture', which has no "
        "cute class yet.")

  @staticmethod
  def process(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture *QSSGRhiEffectSystem::process(const QSSGRenderLayer
    &layer, QRhiTexture *inTexture, QRhiTexture *inDepthTexture, QRhiTexture
    *inNormalTexture, QRhiTexture *inMotionVectorTexture)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.process' has no cute function yet. Qt's "
        "'QRhiTexture *QSSGRhiEffectSystem::process(const QSSGRenderLayer "
        "&layer, QRhiTexture *inTexture, QRhiTexture *inDepthTexture, "
        "QRhiTexture *inNormalTexture, QRhiTexture "
        "*inMotionVectorTexture)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def releaseTexture(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiEffectSystem::releaseTexture(QSSGRhiEffectTexture
    *texture)': names 'QSSGRhiEffectTexture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.releaseTexture' has no cute function yet. "
        "Qt's 'void "
        "QSSGRhiEffectSystem::releaseTexture(QSSGRhiEffectTexture "
        "*texture)': names 'QSSGRhiEffectTexture', which has no cute class "
        "yet.")

  @staticmethod
  def renderCmd(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiEffectSystem::renderCmd(const QSSGRenderEffect
    *inEffect, QSSGRhiEffectTexture *inTexture, QSSGRhiEffectTexture *target,
    quint8 viewCount)': names 'QSSGRhiEffectTexture', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QSSGRhiEffectSystem.renderCmd' has no cute function yet. Qt's "
        "'void QSSGRhiEffectSystem::renderCmd(const QSSGRenderEffect "
        "*inEffect, QSSGRhiEffectTexture *inTexture, QSSGRhiEffectTexture "
        "*target, quint8 viewCount)': names 'QSSGRhiEffectTexture', which "
        "has no cute class yet.")
