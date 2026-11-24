//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qssgvertexpipelineimpl_p.h"
#include <QtCore/qregularexpression.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershaderlibrarymanager_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 589, as _ZN26QSSGMaterialVertexPipeline11activeStageEv
inline QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::activeStage()
{
    return vertex();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 487, as _ZN26QSSGMaterialVertexPipeline12assignOutputERK10QByteArrayS2_
inline void QSSGMaterialVertexPipeline::assignOutput(const QByteArray &inVarName, const QByteArray &inVarValue)
{
    vertex() << "    " << inVarName << " = " << inVarValue << ";\n";
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 569, as _ZN26QSSGMaterialVertexPipeline21endFragmentGenerationEv
inline void QSSGMaterialVertexPipeline::endFragmentGeneration()
{
    if (!skipCustomFragmentSnippet && materialAdapter->isUnshaded() && materialAdapter->hasCustomShaderSnippet(QSSGShaderCache::ShaderType::Fragment))
        fragment() << "    qt_customMain();\n";

    fragment().append("}");
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 577, as _ZN26QSSGMaterialVertexPipeline25addInterpolationParameterERK10QByteArrayS2_
inline void QSSGMaterialVertexPipeline::addInterpolationParameter(const QByteArray &inName, const QByteArray &inType)
{
    vertex().addOutgoing(inName, inType);
    fragment().addIncoming(inName, inType);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 583, as _ZN26QSSGMaterialVertexPipeline16addFlatParameterERK10QByteArrayS2_
inline void QSSGMaterialVertexPipeline::addFlatParameter(const QByteArray &inName, const QByteArray &inType)
{
    vertex().addFlatOutgoing(inName, inType);
    fragment().addFlatIncoming(inName, inType);
}
//  -----------------------------------------------------------------------

//  QSSGMaterialVertexPipeline::~QSSGMaterialVertexPipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipelineD1Ev(
    QSSGMaterialVertexPipeline *self) {
  delete self;
}

//  bool QSSGMaterialVertexPipeline::setCode(GenerationFlag inCode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QSSGMaterialVertexPipeline7setCodeENS_14GenerationFlagE(
    QSSGMaterialVertexPipeline *self,
    QSSGMaterialVertexPipeline::GenerationFlag inCode) {
  return self->setCode(inCode);
}

//  bool QSSGMaterialVertexPipeline::hasCode(GenerationFlag inCode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QSSGMaterialVertexPipeline7hasCodeENS_14GenerationFlagE(
    QSSGMaterialVertexPipeline *self,
    QSSGMaterialVertexPipeline::GenerationFlag inCode) {
  return self->hasCode(inCode);
}

//  QSSGProgramGenerator *QSSGMaterialVertexPipeline::programGenerator()
//      const
extern "C" Q_DECL_EXPORT
QSSGProgramGenerator *ritual_ZNK26QSSGMaterialVertexPipeline16programGeneratorEv(
    const QSSGMaterialVertexPipeline *self) {
  return self->programGenerator();
}

//  void QSSGMaterialVertexPipeline::generateObjectNormal()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline20generateObjectNormalEv(
    QSSGMaterialVertexPipeline *self) {
  self->generateObjectNormal();
}

//  void QSSGMaterialVertexPipeline::generateDepth()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline13generateDepthEv(
    QSSGMaterialVertexPipeline *self) {
  self->generateDepth();
}

//  void QSSGMaterialVertexPipeline::addIncoming(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline11addIncomingERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addIncoming(*name, *type);
}

//  void QSSGMaterialVertexPipeline::addOutgoing(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline11addOutgoingERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addOutgoing(*name, *type);
}

//  void QSSGMaterialVertexPipeline::addUniform(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline10addUniformERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addUniform(*name, *type);
}

//  void QSSGMaterialVertexPipeline::addUniformArray(const QByteArray &name,
//      const QByteArray &type, quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline15addUniformArrayERK10QByteArrayS2_j(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *type,
    quint32 size) {
  self->addUniformArray(*name, *type, size);
}

//  void QSSGMaterialVertexPipeline::addInclude(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline10addIncludeERK10QByteArray(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name) {
  self->addInclude(*name);
}

//  void QSSGMaterialVertexPipeline::addFunction(const QByteArray
//      &functionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline11addFunctionERK10QByteArray(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *functionName) {
  self->addFunction(*functionName);
}

//  void QSSGMaterialVertexPipeline::addConstantBuffer(const QByteArray
//      &name, const QByteArray &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline17addConstantBufferERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *layout) {
  self->addConstantBuffer(*name, *layout);
}

//  void QSSGMaterialVertexPipeline::addConstantBufferParam(const QByteArray
//      &cbName, const QByteArray &paramName, const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline22addConstantBufferParamERK10QByteArrayS2_S2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *cbName,
    const QByteArray *paramName,
    const QByteArray *type) {
  self->addConstantBufferParam(*cbName, *paramName, *type);
}

//  void QSSGMaterialVertexPipeline::addDefinition(const QByteArray &name,
//      const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline13addDefinitionERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *name,
    const QByteArray *value) {
  self->addDefinition(*name, *value);
}

//  void QSSGMaterialVertexPipeline::append(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline6appendERK10QByteArray(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *data) {
  self->append(*data);
}

//  QSSGShaderGeneratorStage QSSGMaterialVertexPipeline::stage() const
extern "C" Q_DECL_EXPORT
QSSGShaderGeneratorStage ritual_ZNK26QSSGMaterialVertexPipeline5stageEv(
    const QSSGMaterialVertexPipeline *self) {
  return self->stage();
}

//  void QSSGMaterialVertexPipeline::assignOutput(const QByteArray
//      &inVarName, const QByteArray &inVarValueExpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline12assignOutputERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *inVarName,
    const QByteArray *inVarValueExpr) {
  self->assignOutput(*inVarName, *inVarValueExpr);
}

//  void QSSGMaterialVertexPipeline::endFragmentGeneration()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline21endFragmentGenerationEv(
    QSSGMaterialVertexPipeline *self) {
  self->endFragmentGeneration();
}

//  void QSSGMaterialVertexPipeline::addInterpolationParameter(const
//      QByteArray &inParamName, const QByteArray &inParamType)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline25addInterpolationParameterERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *inParamName,
    const QByteArray *inParamType) {
  self->addInterpolationParameter(*inParamName, *inParamType);
}

//  void QSSGMaterialVertexPipeline::addFlatParameter(const QByteArray
//      &inParamName, const QByteArray &inParamType)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline16addFlatParameterERK10QByteArrayS2_(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *inParamName,
    const QByteArray *inParamType) {
  self->addFlatParameter(*inParamName, *inParamType);
}
