"""
QSSGProgramGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGProgramGenerator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGProgramGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGProgramGenerator: a plain Python object standing
  in front of one C++ QSSGProgramGenerator.

  What exists
  -----------

  Every function of Qt's QSSGProgramGenerator that has a ritual and that
  Python can call so far, 1 name in all: 'linkStages'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderGeneratorStageFlags
    QSSGProgramGenerator::defaultFlags()': gives the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'void
    QSSGProgramGenerator::beginProgram(QSSGShaderGeneratorStageFlags
    inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', whose class
    cannot be named here.
  - Qt's 'QSSGShaderGeneratorStageFlags
    QSSGProgramGenerator::getEnabledStages() const': gives the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'QSSGStageGeneratorBase
    &QSSGProgramGenerator::internalGetStage(QSSGShaderGeneratorStage
    inStage)': names the enum 'QSSGShaderGeneratorStage', whose class cannot
    be named here.
  - Qt's 'QSSGStageGeneratorBase
    *QSSGProgramGenerator::getStage(QSSGShaderGeneratorStage inStage)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'void QSSGProgramGenerator::registerShaderMetaDataFromSource(
    QSSGShaderResourceMergeContext *mergeContext, const QByteArray &contents,
    QSSGShaderGeneratorStage stage)': names the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGProgramGenerator::compileGeneratedRhiShader(const QByteArray
    &inMaterialInfoString, const QSSGShaderFeatures &inFeatureSet,
    QSSGShaderLibraryManager &shaderLibraryManager, QSSGShaderCache
    &theCache, QSSGRhiShaderPipeline::StageFlags stageFlags, const
    QSSGUserShaderAugmentation &shaderAugmentation, int viewCount, bool
    perTargetCompilation)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGProgramGenerator is created at the first use, not by
    'QSSGProgramGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGProgramGenerator.
  - Each name of Qt's QSSGProgramGenerator that has no cute function yet,
    'beginProgram', 'compileGeneratedRhiShader', 'defaultFlags',
    'getEnabledStages', 'getStage', 'internalGetStage',
    'registerShaderMetaDataFromSource', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGProgramGenerator'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGProgramGenerator::QSSGProgramGenerator()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgprogramgenerator.html#QSSGProgramGenerator
    """
    #  QSSGProgramGenerator::QSSGProgramGenerator()
    self._noteCreation(QSSGProgramGenerator, lambda: Rituals.call(
        'ritual_ZN20QSSGProgramGeneratorC1Ev',
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

  def linkStages(self) -> None:
    """
    Calls Qt's 'void QSSGProgramGenerator::linkStages()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgprogramgenerator.html#linkStages
    """
    #  void QSSGProgramGenerator::linkStages()
    self.uglySide.call('ritual_ZN20QSSGProgramGenerator10linkStagesEv')

  @staticmethod
  def beginProgram(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGProgramGenerator::beginProgram(QSSGShaderGeneratorStageFlags
    inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.beginProgram' has no cute function yet. Qt's "
        "'void "
        "QSSGProgramGenerator::beginProgram(QSSGShaderGeneratorStageFlags "
        "inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', "
        "whose class cannot be named here.")

  @staticmethod
  def compileGeneratedRhiShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGProgramGenerator::compileGeneratedRhiShader(const QByteArray
    &inMaterialInfoString, const QSSGShaderFeatures &inFeatureSet,
    QSSGShaderLibraryManager &shaderLibraryManager, QSSGShaderCache
    &theCache, QSSGRhiShaderPipeline::StageFlags stageFlags, const
    QSSGUserShaderAugmentation &shaderAugmentation, int viewCount, bool
    perTargetCompilation)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.compileGeneratedRhiShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGProgramGenerator::compileGeneratedRhiShader(const QByteArray "
        "&inMaterialInfoString, const QSSGShaderFeatures &inFeatureSet, "
        "QSSGShaderLibraryManager &shaderLibraryManager, QSSGShaderCache "
        "&theCache, QSSGRhiShaderPipeline::StageFlags stageFlags, const "
        "QSSGUserShaderAugmentation &shaderAugmentation, int viewCount, "
        "bool perTargetCompilation)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def defaultFlags(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderGeneratorStageFlags
    QSSGProgramGenerator::defaultFlags()': gives the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.defaultFlags' has no cute function yet. Qt's "
        "'QSSGShaderGeneratorStageFlags "
        "QSSGProgramGenerator::defaultFlags()': gives the enum "
        "'QSSGShaderGeneratorStage', whose class cannot be named here.")

  @staticmethod
  def getEnabledStages(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderGeneratorStageFlags
    QSSGProgramGenerator::getEnabledStages() const': gives the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.getEnabledStages' has no cute function yet. "
        "Qt's 'QSSGShaderGeneratorStageFlags "
        "QSSGProgramGenerator::getEnabledStages() const': gives the enum "
        "'QSSGShaderGeneratorStage', whose class cannot be named here.")

  @staticmethod
  def getStage(*__, **_) -> Never:
    """
    Qt's 'QSSGStageGeneratorBase
    *QSSGProgramGenerator::getStage(QSSGShaderGeneratorStage inStage)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.getStage' has no cute function yet. Qt's "
        "'QSSGStageGeneratorBase "
        "*QSSGProgramGenerator::getStage(QSSGShaderGeneratorStage "
        "inStage)': names the enum 'QSSGShaderGeneratorStage', whose class "
        "cannot be named here.")

  @staticmethod
  def internalGetStage(*__, **_) -> Never:
    """
    Qt's 'QSSGStageGeneratorBase
    &QSSGProgramGenerator::internalGetStage(QSSGShaderGeneratorStage
    inStage)': names the enum 'QSSGShaderGeneratorStage', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.internalGetStage' has no cute function yet. "
        "Qt's 'QSSGStageGeneratorBase "
        "&QSSGProgramGenerator::internalGetStage(QSSGShaderGeneratorStage "
        "inStage)': names the enum 'QSSGShaderGeneratorStage', whose class "
        "cannot be named here.")

  @staticmethod
  def registerShaderMetaDataFromSource(*__, **_) -> Never:
    """
    Qt's 'void QSSGProgramGenerator::registerShaderMetaDataFromSource(
    QSSGShaderResourceMergeContext *mergeContext, const QByteArray &contents,
    QSSGShaderGeneratorStage stage)': names the enum
    'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGProgramGenerator.registerShaderMetaDataFromSource' has no "
        "cute function yet. Qt's 'void "
        "QSSGProgramGenerator::registerShaderMetaDataFromSource(QSSGShaderRe"
        "sourceMergeContext *mergeContext, const QByteArray &contents, "
        "QSSGShaderGeneratorStage stage)': names the enum "
        "'QSSGShaderGeneratorStage', whose class cannot be named here.")
