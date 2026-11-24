//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgrhishadereffectnode_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgrhisupport_p.h>
#include <QtQuick/qsgmaterialshader.h>
#include <QtQuick/qsgtextureprovider.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtGui/rhi/qshaderdescription.h>
#include <QtQml/QQmlFile>
#include <QtGui/qquaternion.h>
#include <QtCore/QFile>
#include <QtCore/QFileSelector>
#include <QtCore/QMutexLocker>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 908, as _ZNK34QSGRhiGuiThreadShaderEffectManager35hasSeparateSamplerAndTextureObjectsEv
inline bool QSGRhiGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjects() const
{
    return false; // because SPIR-V and QRhi make it look so, regardless of the underlying API
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 913, as _ZNK34QSGRhiGuiThreadShaderEffectManager3logEv
inline QString QSGRhiGuiThreadShaderEffectManager::log() const
{
    return QString();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 918, as _ZNK34QSGRhiGuiThreadShaderEffectManager6statusEv
inline QSGGuiThreadShaderEffectManager::Status QSGRhiGuiThreadShaderEffectManager::status() const
{
    return m_status;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 956, as _ZN34QSGRhiGuiThreadShaderEffectManager7reflectEPN31QSGGuiThreadShaderEffectManager10ShaderInfoE
inline bool QSGRhiGuiThreadShaderEffectManager::reflect(ShaderInfo *result)
{
    switch (result->rhiShader.stage()) {
    case QShader::VertexStage:
        result->type = ShaderInfo::TypeVertex;
        break;
    case QShader::FragmentStage:
        result->type = ShaderInfo::TypeFragment;
        break;
    default:
        result->type = ShaderInfo::TypeOther;
        qWarning("Unsupported shader stage (%d)", result->rhiShader.stage());
        return false;
    }

    const QShaderDescription desc = result->rhiShader.description();

    int ubufBinding = -1;
    const QList<QShaderDescription::UniformBlock> ubufs = desc.uniformBlocks();
    const int ubufCount = ubufs.size();
    for (int i = 0; i < ubufCount; ++i) {
        const QShaderDescription::UniformBlock &ubuf(ubufs[i]);
        if (ubufBinding == -1 && ubuf.binding >= 0) {
            ubufBinding = ubuf.binding;
            for (const QShaderDescription::BlockVariable &member : ubuf.members) {
                // The uniform buffer is sized from ubuf.size, while the members are
                // written at their own offsets, so a member reaching outside the block
                // would have updateUniformData() write past the buffer.
                if (member.offset < 0 || member.size < 0
                    || member.offset > ubuf.size - member.size)
                {
                    qWarning("Uniform block member %s at offset %d with size %d does not fit "
                             "the %d byte block; shader will not be used",
                             member.name.constData(), member.offset, member.size, ubuf.size);
                    return false;
                }
                ShaderInfo::Variable v;
                v.type = ShaderInfo::Constant;
                v.name = member.name;
                v.offset = member.offset;
                v.size = member.size;
                result->variables.append(v);
            }
        } else {
            qWarning("Uniform block %s (binding %d) ignored", ubuf.blockName.constData(),
                     ubuf.binding);
        }
    }

    const QList<QShaderDescription::InOutVariable> combinedImageSamplers = desc.combinedImageSamplers();
    const int samplerCount = combinedImageSamplers.size();
    for (int i = 0; i < samplerCount; ++i) {
        const QShaderDescription::InOutVariable &combinedImageSampler(combinedImageSamplers[i]);
        ShaderInfo::Variable v;
        v.type = ShaderInfo::Sampler;
        v.name = combinedImageSampler.name;
        v.bindPoint = combinedImageSampler.binding;
        result->variables.append(v);
    }

    return true;
}
//  -----------------------------------------------------------------------

//  bool
//      QSGRhiGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjec
//      ts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QSGRhiGuiThreadShaderEffectManager35hasSeparateSamplerAndTextureObjectsEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return self->hasSeparateSamplerAndTextureObjects();
}

//  QString QSGRhiGuiThreadShaderEffectManager::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK34QSGRhiGuiThreadShaderEffectManager3logEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return new QString(self->log());
}

//  Status QSGRhiGuiThreadShaderEffectManager::status() const
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager::Status ritual_ZNK34QSGRhiGuiThreadShaderEffectManager6statusEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return self->status();
}

//  bool QSGRhiGuiThreadShaderEffectManager::reflect(ShaderInfo *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QSGRhiGuiThreadShaderEffectManager7reflectEPN31QSGGuiThreadShaderEffectManager10ShaderInfoE(
    QSGRhiGuiThreadShaderEffectManager *self,
    QSGGuiThreadShaderEffectManager::ShaderInfo *result) {
  return self->reflect(result);
}

//  bool
//      QSGRhiGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjec
//      ts() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager35hasSeparateSamplerAndTextureObjectsEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return self->QSGRhiGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjects();
}

//  QString QSGRhiGuiThreadShaderEffectManager::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager3logEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return new QString(self->QSGRhiGuiThreadShaderEffectManager::log());
}

//  Status QSGRhiGuiThreadShaderEffectManager::status() const
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager::Status ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager6statusEv(
    const QSGRhiGuiThreadShaderEffectManager *self) {
  return self->QSGRhiGuiThreadShaderEffectManager::status();
}
