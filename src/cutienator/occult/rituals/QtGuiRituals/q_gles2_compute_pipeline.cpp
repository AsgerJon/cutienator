//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 5569, as _ZN9QRhiGles211linkProgramEj
inline bool QRhiGles2::linkProgram(GLuint program)
{
    f->glLinkProgram(program);
    GLint linked = 0;
    f->glGetProgramiv(program, GL_LINK_STATUS, &linked);
    if (!linked) {
        GLint infoLogLength = 0;
        f->glGetProgramiv(program, GL_INFO_LOG_LENGTH, &infoLogLength);
        QByteArray log;
        if (infoLogLength > 1) {
            GLsizei length = 0;
            log.resize(infoLogLength);
            f->glGetProgramInfoLog(program, infoLogLength, &length, log.data());
        }
        qWarning("Failed to link shader program: %s", log.constData());
        return false;
    }
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5496, as _ZN9QRhiGles212shaderSourceERK15QRhiShaderStageP14QShaderVersionSt8optionalIS3_E
inline QByteArray QRhiGles2::shaderSource(const QRhiShaderStage &shaderStage, QShaderVersion *shaderVersion,
                                   std::optional<QShaderVersion> commonVersion)
{
    const QShader bakedShader = shaderStage.shader();
    const QList<QShaderVersion> versionsToTry = commonVersion
            ? QList<QShaderVersion>{ *commonVersion }
            : glslVersionsToTry();

    QByteArray source;
    for (const QShaderVersion &ver : versionsToTry) {
        source = bakedShader.shader({ QShader::GlslShader, ver, shaderStage.shaderVariant() }).shader();
        if (!source.isEmpty()) {
            if (shaderVersion)
                *shaderVersion = ver;
            break;
        }
    }
    if (source.isEmpty()) {
        qWarning() << "No GLSL shader code found (versions tried: " << versionsToTry
                   << ") in baked shader" << bakedShader;
    }
    return source;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5667, as _ZN9QRhiGles214gatherSamplersEjRKN18QShaderDescription13InOutVariableEP15QVarLengthArrayI24QGles2SamplerDescriptionLx4EE
inline void QRhiGles2::gatherSamplers(GLuint program,
                               const QShaderDescription::InOutVariable &v,
                               QGles2SamplerDescriptionVector *dst)
{
    QGles2SamplerDescription sampler;
    sampler.glslLocation = f->glGetUniformLocation(program, v.name.constData());
    if (sampler.glslLocation >= 0) {
        sampler.combinedBinding = v.binding;
        sampler.tbinding = -1;
        sampler.sbinding = -1;
        dst->append(sampler);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5625, as _ZN9QRhiGles214gatherUniformsEjRKN18QShaderDescription12UniformBlockEP17QDuplicateTrackerIiLm32EEP15QVarLengthArrayI24QGles2UniformDescriptionLx8EE
inline void QRhiGles2::gatherUniforms(GLuint program,
                               const QShaderDescription::UniformBlock &ub,
                               ActiveUniformLocationTracker *activeUniformLocations,
                               QGles2UniformDescriptionVector *dst)
{
    QByteArray prefix = ub.structName + '.';
    for (const QShaderDescription::BlockVariable &blockMember : ub.members) {
        if (blockMember.type == QShaderDescription::Struct) {
            QByteArray structPrefix = prefix + blockMember.name;

            const int baseOffset = blockMember.offset;
            if (blockMember.arrayDims.isEmpty()) {
                for (const QShaderDescription::BlockVariable &structMember : blockMember.structMembers)
                    registerUniformIfActive(structMember, structPrefix + ".", ub.binding,
                                            baseOffset, program, activeUniformLocations, dst);
            } else {
                if (blockMember.arrayDims.size() > 1) {
                    qWarning("Array of struct '%s' has more than one dimension. Only the first "
                             "dimension is used.",
                             blockMember.name.constData());
                }
                const int dim = blockMember.arrayDims.first();
                if (dim < 1) {
                    qWarning("Array of struct '%s' has an invalid first dimension (%d). Ignored.",
                             blockMember.name.constData(), dim);
                    continue;
                }
                const int elemSize = blockMember.size / dim;
                int elemOffset = baseOffset;
                for (int di = 0; di < dim; ++di) {
                    const QByteArray arrayPrefix = structPrefix + '[' + QByteArray::number(di) + ']' + '.';
                    for (const QShaderDescription::BlockVariable &structMember : blockMember.structMembers)
                        registerUniformIfActive(structMember, arrayPrefix, ub.binding, elemOffset, program, activeUniformLocations, dst);
                    elemOffset += elemSize;
                }
            }
        } else {
            registerUniformIfActive(blockMember, prefix, ub.binding, 0, program, activeUniformLocations, dst);
        }
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5853, as _ZN9QRhiGles222trySaveToPipelineCacheEjRK10QByteArrayb
inline void QRhiGles2::trySaveToPipelineCache(GLuint program, const QByteArray &cacheKey, bool force)
{
    // This handles our own simulated "pipeline cache". (specific to QRhi, not
    // shared with legacy QOpenGL* stuff)

    if (caps.programBinary && (force || !m_pipelineCache.contains(cacheKey))) {
        GLint blobSize = 0;
        f->glGetProgramiv(program, GL_PROGRAM_BINARY_LENGTH, &blobSize);
        QByteArray blob(blobSize, Qt::Uninitialized);
        GLint outSize = 0;
        GLenum binaryFormat = 0;
        f->glGetProgramBinary(program, blobSize, &outSize, &binaryFormat, blob.data());
        if (blobSize == outSize)
            m_pipelineCache.insert(cacheKey, { binaryFormat, blob });
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5681, as _ZN9QRhiGles223gatherGeneratedSamplersEjRKN7QShader37SeparateToCombinedImageSamplerMappingEP15QVarLengthArrayI24QGles2SamplerDescriptionLx4EE
inline void QRhiGles2::gatherGeneratedSamplers(GLuint program,
                                        const QShader::SeparateToCombinedImageSamplerMapping &mapping,
                                        QGles2SamplerDescriptionVector *dst)
{
    QGles2SamplerDescription sampler;
    sampler.glslLocation = f->glGetUniformLocation(program, mapping.combinedSamplerName.constData());
    if (sampler.glslLocation >= 0) {
        sampler.combinedBinding = -1;
        sampler.tbinding = mapping.textureBinding;
        sampler.sbinding = mapping.samplerBinding;
        dst->append(sampler);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 7094, as _ZN21QGles2ComputePipelineD1Ev
inline QGles2ComputePipeline::~QGles2ComputePipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7099, as _ZN21QGles2ComputePipeline7destroyEv
inline void QGles2ComputePipeline::destroy()
{
    if (!program)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::Pipeline;

    e.pipeline.program = program;

    program = 0;
    uniforms.clear();
    samplers.clear();

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 7120, as _ZN21QGles2ComputePipeline6createEv
inline bool QGles2ComputePipeline::create()
{
    QRHI_RES_RHI(QRhiGles2);

    if (program)
        destroy();

    if (!rhiD->ensureContext())
        return false;

    rhiD->pipelineCreationStart();

    const QShaderDescription csDesc = m_shaderStage.shader().description();
    QShader::SeparateToCombinedImageSamplerMappingList csSamplerMappingList;
    QShaderVersion shaderVersion;
    if (!rhiD->shaderSource(m_shaderStage, &shaderVersion).isEmpty()) {
        csSamplerMappingList = m_shaderStage.shader().separateToCombinedImageSamplerMappingList(
                    { QShader::GlslShader, shaderVersion, m_shaderStage.shaderVariant() });
    }

    program = rhiD->f->glCreateProgram();

    QByteArray cacheKey;
    QRhiGles2::ProgramCacheResult cacheResult = rhiD->tryLoadFromDiskOrPipelineCache(&m_shaderStage, 1, program, {}, &cacheKey);
    if (cacheResult == QRhiGles2::ProgramCacheError)
        return false;

    if (cacheResult == QRhiGles2::ProgramCacheMiss) {
        if (!rhiD->compileShader(program, m_shaderStage, nullptr))
            return false;

        if (!rhiD->linkProgram(program))
            return false;

        if (rhiD->rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave)) {
            // force replacing existing cache entry (if there is one, then
            // something is wrong with it, as there was no hit)
            rhiD->trySaveToPipelineCache(program, cacheKey, true);
        } else {
            // legacy QOpenGLShaderProgram style behavior: the "pipeline cache"
            // was not enabled, so instead store to the Qt 5 disk cache
            rhiD->trySaveToDiskCache(program, cacheKey);
        }
    } else {
        Q_ASSERT(cacheResult == QRhiGles2::ProgramCacheHit);
        if (rhiD->rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave)) {
            // just so that it ends up in the pipeline cache also when the hit was
            // from the disk cache
            rhiD->trySaveToPipelineCache(program, cacheKey);
        }
    }

    QRhiGles2::ActiveUniformLocationTracker activeUniformLocations;
    const auto csUniformBlocks = csDesc.uniformBlocks();
    for (const QShaderDescription::UniformBlock &ub : csUniformBlocks)
        rhiD->gatherUniforms(program, ub, &activeUniformLocations, &uniforms);
    const auto csCombinedImageSamplers = csDesc.combinedImageSamplers();
    for (const QShaderDescription::InOutVariable &v : csCombinedImageSamplers)
        rhiD->gatherSamplers(program, v, &samplers);
    for (const QShader::SeparateToCombinedImageSamplerMapping &mapping : std::as_const(csSamplerMappingList))
        rhiD->gatherGeneratedSamplers(program, mapping, &samplers);

    // storage images and buffers need no special steps here

    memset(uniformState, 0, sizeof(uniformState));

    currentSrb = nullptr;
    currentSrbGeneration = 0;

    rhiD->pipelineCreationEnd();
    generation += 1;
    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QGles2ComputePipeline that Python can take functions over in. Every QGles2ComputePipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2ComputePipelineCall0)(const void *, int *);
typedef bool (*CuteQGles2ComputePipelineCall1)(const void *, int *);
typedef int (*CuteQGles2ComputePipelineCall2)(const void *, int *);
class CuteQGles2ComputePipeline : public QGles2ComputePipeline {
public:
  using QGles2ComputePipeline::QGles2ComputePipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QRhiComputePipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QGles2ComputePipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2ComputePipelineCall0 call = reinterpret_cast<CuteQGles2ComputePipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2ComputePipeline::destroy();
  }

  //  bool QGles2ComputePipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2ComputePipelineCall1 call = reinterpret_cast<CuteQGles2ComputePipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2ComputePipeline::create();
  }

  //  QRhiResource::Type QRhiComputePipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2ComputePipelineCall2 call = reinterpret_cast<CuteQGles2ComputePipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiComputePipeline::resourceType();
  }
};

//  QGles2ComputePipeline::~QGles2ComputePipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGles2ComputePipelineD1Ev(QGles2ComputePipeline *self) {
  delete self;
}

//  void QGles2ComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGles2ComputePipeline7destroyEv(
    QGles2ComputePipeline *self) {
  self->destroy();
}

//  bool QGles2ComputePipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGles2ComputePipeline6createEv(QGles2ComputePipeline *self) {
  return self->create();
}

//  a Python function taken by a CuteQGles2ComputePipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2ComputePipeline(
    QGles2ComputePipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2ComputePipeline *>(self)->take(key, call);
}

//  void QGles2ComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGles2ComputePipeline7destroyEv(
    QGles2ComputePipeline *self) {
  self->QGles2ComputePipeline::destroy();
}

#endif  // QT_CONFIG(opengl)
