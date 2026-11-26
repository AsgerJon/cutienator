//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgvertexpipelineimpl_p.h>
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 33, as local:qssgvertexpipelineimpl.cpp:insertProcessorArgsFragmentMain
static inline void insertProcessorArgsFragmentMain(QByteArray &snippet, const char *argKey, const char* (*argListFunc)(),
                                       QSSGShaderMaterialAdapter *materialAdapter = nullptr, bool isSharedInout = false)
{
    const int argKeyLen = int(strlen(argKey));
    const int argKeyPos = snippet.indexOf(argKey);
    if (argKeyPos >= 0) {
        QByteArray flexArgs;
        if (materialAdapter) {
            if (materialAdapter->isClearcoatEnabled()) {
                flexArgs += QByteArrayLiteral(", inout float CLEARCOAT_AMOUNT, inout float CLEARCOAT_FRESNEL_POWER, inout float CLEARCOAT_ROUGHNESS, inout vec3 CLEARCOAT_NORMAL");
                if (materialAdapter->isClearcoatFresnelScaleBiasEnabled())
                    flexArgs += QByteArrayLiteral(", inout float CLEARCOAT_FRESNEL_SCALE, inout float CLEARCOAT_FRESNEL_BIAS");
            }
            if (materialAdapter->isFresnelScaleBiasEnabled())
                flexArgs += QByteArrayLiteral(", inout float FRESNEL_SCALE, inout float FRESNEL_BIAS");
            if (materialAdapter->isTransmissionEnabled())
                flexArgs += QByteArrayLiteral(", inout float TRANSMISSION_FACTOR, inout float THICKNESS_FACTOR, inout vec3 ATTENUATION_COLOR, inout float ATTENUATION_DISTANCE");
            if (materialAdapter->usesSharedVariables()) {
                const char *inoutString = isSharedInout ? ", inout " : ", in ";
                flexArgs += inoutString + QByteArrayLiteral("QT_SHARED_VARS SHARED");
            }
        }
        snippet = snippet.left(argKeyPos) + argListFunc() + flexArgs + snippet.mid(argKeyPos + argKeyLen);
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 59, as local:qssgvertexpipelineimpl.cpp:insertProcessorArgs
static inline void insertProcessorArgs(QByteArray &snippet, const char *argKey, const char* (*argListFunc)(),
                                    QSSGShaderMaterialAdapter *materialAdapter = nullptr, bool isSharedInout = false)
{
    const int argKeyLen = int(strlen(argKey));
    const int argKeyPos = snippet.indexOf(argKey);
    if (argKeyPos >= 0) {
        QByteArray flexArgs;
        if (materialAdapter && materialAdapter->usesSharedVariables()) {
            const char *inoutString = isSharedInout ? ", inout " : ", in ";
            flexArgs += inoutString + QByteArrayLiteral("QT_SHARED_VARS SHARED");
        }
        snippet = snippet.left(argKeyPos) + argListFunc() + flexArgs + snippet.mid(argKeyPos + argKeyLen);
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 74, as local:qssgvertexpipelineimpl.cpp:insertDirectionalLightProcessorArgs
static inline void insertDirectionalLightProcessorArgs(QByteArray &snippet, QSSGShaderMaterialAdapter *materialAdapter)
{
    insertProcessorArgs(snippet, "/*%QT_ARGS_DIRECTIONAL_LIGHT%*/", QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList, materialAdapter, true);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 104, as local:qssgvertexpipelineimpl.cpp:insertFragmentMainArgs
static inline void insertFragmentMainArgs(QByteArray &snippet, QSSGShaderMaterialAdapter *materialAdapter)
{
    insertProcessorArgsFragmentMain(snippet, "/*%QT_ARGS_MAIN%*/", QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList, materialAdapter, true);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 124, as local:qssgvertexpipelineimpl.cpp:customMainCallWithArguments
static inline const char *customMainCallWithArguments(bool usesInstancing)
{
    if (usesInstancing)
        return "    qt_customMain(qt_vertPosition.xyz, qt_vertNormal, qt_vertUV0, qt_vertUV1, qt_vertTangent, qt_vertBinormal, qt_vertJoints, qt_vertWeights, qt_vertColor, qt_instancedModelMatrix, qt_instancedMVPMatrix);";
    else
        return "    qt_customMain(qt_vertPosition.xyz, qt_vertNormal, qt_vertUV0, qt_vertUV1, qt_vertTangent, qt_vertBinormal, qt_vertJoints, qt_vertWeights, qt_vertColor);\n";
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 132, as local:qssgvertexpipelineimpl.cpp:extractSharedVarsTypeDefinition
static inline QByteArray extractSharedVarsTypeDefinition(QByteArray &snippet, QSSGShaderMaterialAdapter *materialAdapter) {
    if (materialAdapter->usesSharedVariables()) {
        // Extract shared variables from the custom shader snippet
        static QRegularExpression re(QString::fromLocal8Bit(R"(struct\s+QT_SHARED_VARS\s*\{[\s\S]*?\};)"), QRegularExpression::DotMatchesEverythingOption);
        QRegularExpressionMatch match = re.match(QString::fromLocal8Bit(snippet));
        if (!match.hasMatch())
            return QByteArray();
        QString typeDefinition = match.captured(0);
        snippet.remove(match.capturedStart(0), match.capturedLength(0));
        return typeDefinition.toLocal8Bit();
    }
    return QByteArray();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 22, as _ZN26QSSGMaterialVertexPipelineC1ER20QSSGProgramGeneratorRK38QSSGShaderDefaultMaterialKeyPropertiesP25QSSGShaderMaterialAdapter
inline QSSGMaterialVertexPipeline::QSSGMaterialVertexPipeline(QSSGProgramGenerator &programGen,
                                                       const QSSGShaderDefaultMaterialKeyProperties &materialProperties,
                                                       QSSGShaderMaterialAdapter *materialAdapter)
    : m_programGenerator(&programGen)
    , defaultMaterialShaderKeyProperties(materialProperties)
    , materialAdapter(materialAdapter)
    , hasCustomShadedMain(false)
    , skipCustomFragmentSnippet(false)
{
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 589, as _ZN26QSSGMaterialVertexPipeline11activeStageEv
inline QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::activeStage()
{
    return vertex();
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 492, as _ZN26QSSGMaterialVertexPipeline21doGenerateWorldNormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE
inline void QSSGMaterialVertexPipeline::doGenerateWorldNormal(const QSSGShaderDefaultMaterialKey &inKey)
{
    QSSGStageGeneratorBase &vertexGenerator(vertex());
    const bool usesInstancing = defaultMaterialShaderKeyProperties.m_usesInstancing.getValue(inKey);
    if (!usesInstancing)
        vertexGenerator.addUniform("qt_normalMatrix", "mat3");
    if (m_hasMorphing)
        vertexGenerator.append("    qt_vertNormal = qt_getTargetNormal(qt_vertNormal);");
    if (m_hasSkinning) {
        vertexGenerator.append("    if (qt_vertWeights != vec4(0.0))");
        vertexGenerator.append("        qt_vertNormal = qt_getSkinNormalMatrix(qt_vertJoints, qt_vertWeights) * qt_vertNormal;");
    }
    // If new model->skin is used,
    // both qt_normalMatrix and qt_modelMatrix are identity.
    if (!usesInstancing) {
        if (m_hasSkinning)
            vertexGenerator.append("    vec3 qt_world_normal = normalize(qt_vertNormal);");
        else
            vertexGenerator.append("    vec3 qt_world_normal = normalize(qt_normalMatrix * qt_vertNormal);");
    } else {
        vertexGenerator.append("    vec3 qt_world_normal = normalize(qt_instancedNormalMatrix * qt_vertNormal);");
    }
    vertexGenerator.append("    qt_varNormal = qt_world_normal;");
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 517, as _ZN26QSSGMaterialVertexPipeline20doGenerateVarTangentERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE
inline void QSSGMaterialVertexPipeline::doGenerateVarTangent(const QSSGShaderDefaultMaterialKey &inKey)
{
    if (m_hasMorphing)
        vertex() << "    qt_vertTangent = qt_getTargetTangent(qt_vertTangent);\n";
    if (m_needsSkinning) {
        vertex() << "    if (qt_vertWeights != vec4(0.0))\n"
                 << "       qt_vertTangent = (skinMat * vec4(qt_vertTangent, 0.0)).xyz;\n";

    }
    const bool usesInstancing = defaultMaterialShaderKeyProperties.m_usesInstancing.getValue(inKey);
    if (!usesInstancing) {
        if (!m_hasSkinning)
            vertex() << "    qt_varTangent = (qt_modelMatrix * vec4(qt_vertTangent, 0.0)).xyz;\n";
        else
            vertex() << "    qt_varTangent = qt_vertTangent;\n";
    } else {
        vertex() << "    qt_varTangent = (qt_instancedModelMatrix * vec4(qt_vertTangent, 0.0)).xyz;\n";
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 537, as _ZN26QSSGMaterialVertexPipeline21doGenerateVarBinormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE
inline void QSSGMaterialVertexPipeline::doGenerateVarBinormal(const QSSGShaderDefaultMaterialKey &inKey)
{
    if (m_hasMorphing)
        vertex() << "    qt_vertBinormal = qt_getTargetBinormal(qt_vertBinormal);\n";
    if (m_needsSkinning) {
        vertex() << "    if (qt_vertWeights != vec4(0.0))\n"
                 << "       qt_vertBinormal = (skinMat * vec4(qt_vertBinormal, 0.0)).xyz;\n";
    }
    const bool usesInstancing = defaultMaterialShaderKeyProperties.m_usesInstancing.getValue(inKey);
    if (!usesInstancing) {
        if (!m_hasSkinning)
            vertex() << "    qt_varBinormal = (qt_modelMatrix * vec4(qt_vertBinormal, 0.0)).xyz;\n";
        else
            vertex() << "    qt_varBinormal = qt_vertBinormal;\n";
    } else {
        vertex() << "    qt_varBinormal = (qt_instancedModelMatrix * vec4(qt_vertBinormal, 0.0)).xyz;\n";
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgvertexpipelineimpl.cpp, line 556, as _ZN26QSSGMaterialVertexPipeline17hasAttributeInKeyEN28QSSGShaderKeyVertexAttribute19VertexAttributeBitsERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE
inline bool QSSGMaterialVertexPipeline::hasAttributeInKey(QSSGShaderKeyVertexAttribute::VertexAttributeBits inAttr,
                                                   const QSSGShaderDefaultMaterialKey &inKey)
{
    return defaultMaterialShaderKeyProperties.m_vertexAttributes.getBitValue(inAttr, inKey);
}
//  -----------------------------------------------------------------------

//  QSSGMaterialVertexPipeline::QSSGMaterialVertexPipeline(QSSGProgramGenerat
//      or &inProgram, const QSSGShaderDefaultMaterialKeyProperties
//      &materialProperties, QSSGShaderMaterialAdapter *materialAdapter)
extern "C" Q_DECL_EXPORT
QSSGMaterialVertexPipeline *ritual_ZN26QSSGMaterialVertexPipelineC1ER20QSSGProgramGeneratorRK38QSSGShaderDefaultMaterialKeyPropertiesP25QSSGShaderMaterialAdapter(
    QSSGProgramGenerator *inProgram,
    const QSSGShaderDefaultMaterialKeyProperties *materialProperties,
    QSSGShaderMaterialAdapter *materialAdapter) {
  return new QSSGMaterialVertexPipeline(
      *inProgram,
      *materialProperties,
      materialAdapter);
}

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

//  QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::vertex()
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN26QSSGMaterialVertexPipeline6vertexEv(
    QSSGMaterialVertexPipeline *self) {
  return &(self->vertex());
}

//  QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::fragment()
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN26QSSGMaterialVertexPipeline8fragmentEv(
    QSSGMaterialVertexPipeline *self) {
  return &(self->fragment());
}

//  void QSSGMaterialVertexPipeline::generateUVCoords(quint32 inUVSet, const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline16generateUVCoordsEjRK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    quint32 inUVSet,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateUVCoords(inUVSet, *inKey);
}

//  void QSSGMaterialVertexPipeline::generateLightmapUVCoords(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline24generateLightmapUVCoordsERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateLightmapUVCoords(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateEnvMapReflection(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline24generateEnvMapReflectionERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateEnvMapReflection(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateViewVector(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline18generateViewVectorERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateViewVector(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateWorldNormal(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline19generateWorldNormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateWorldNormal(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateObjectNormal()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline20generateObjectNormalEv(
    QSSGMaterialVertexPipeline *self) {
  self->generateObjectNormal();
}

//  void QSSGMaterialVertexPipeline::generateWorldPosition(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline21generateWorldPositionERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateWorldPosition(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateDepth()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline13generateDepthEv(
    QSSGMaterialVertexPipeline *self) {
  self->generateDepth();
}

//  void QSSGMaterialVertexPipeline::generateShadowWorldPosition(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline27generateShadowWorldPositionERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateShadowWorldPosition(*inKey);
}

//  void QSSGMaterialVertexPipeline::generateVarTangentAndBinormal(const
//      QSSGShaderDefaultMaterialKey &inKey, bool &genTangent, bool
//      &genBinormal)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline29generateVarTangentAndBinormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EERbS5_(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey,
    bool *genTangent,
    bool *genBinormal) {
  self->generateVarTangentAndBinormal(*inKey, *genTangent, *genBinormal);
}

//  void QSSGMaterialVertexPipeline::generateVertexColor(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline19generateVertexColorERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->generateVertexColor(*inKey);
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

//  QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::operator<<(const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN26QSSGMaterialVertexPipelinelsERK10QByteArray(
    QSSGMaterialVertexPipeline *self,
    const QByteArray *data) {
  return &(self->operator<<(*data));
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

//  QSSGStageGeneratorBase &QSSGMaterialVertexPipeline::activeStage()
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN26QSSGMaterialVertexPipeline11activeStageEv(
    QSSGMaterialVertexPipeline *self) {
  return &(self->activeStage());
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

//  void QSSGMaterialVertexPipeline::doGenerateWorldNormal(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline21doGenerateWorldNormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->doGenerateWorldNormal(*inKey);
}

//  void QSSGMaterialVertexPipeline::doGenerateVarTangent(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline20doGenerateVarTangentERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->doGenerateVarTangent(*inKey);
}

//  void QSSGMaterialVertexPipeline::doGenerateVarBinormal(const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGMaterialVertexPipeline21doGenerateVarBinormalERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    const QSSGShaderDefaultMaterialKey *inKey) {
  self->doGenerateVarBinormal(*inKey);
}

//  bool QSSGMaterialVertexPipeline::hasAttributeInKey(QSSGShaderKeyVertexAtt
//      ribute::VertexAttributeBits inAttr, const
//      QSSGShaderDefaultMaterialKey &inKey)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QSSGMaterialVertexPipeline17hasAttributeInKeyEN28QSSGShaderKeyVertexAttribute19VertexAttributeBitsERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGMaterialVertexPipeline *self,
    QSSGShaderKeyVertexAttribute::VertexAttributeBits inAttr,
    const QSSGShaderDefaultMaterialKey *inKey) {
  return self->hasAttributeInKey(inAttr, *inKey);
}
