//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 22, as _ZN18QSGRhiShaderLinker5resetERK7QShaderS2_
inline void QSGRhiShaderLinker::reset(const QShader &vs, const QShader &fs)
{
    Q_ASSERT(vs.isValid() && fs.isValid());
    m_vs = vs;
    m_fs = fs;

    m_error = false;

    //m_constantBufferSize = 0;
    m_constants.clear();
    m_samplers.clear();
    m_samplerNameMap.clear();
    m_subRectBindings.clear();

    m_constants.reserve(8);
    m_samplers.reserve(4);
    m_samplerNameMap.reserve(4);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 41, as _ZN18QSGRhiShaderLinker13feedConstantsERKN19QSGShaderEffectNode10ShaderDataEPK4QSetIiE
inline void QSGRhiShaderLinker::feedConstants(const QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)
{
    Q_ASSERT(shader.shaderInfo.variables.size() == shader.varData.size());
    static bool shaderEffectDebug = qEnvironmentVariableIntValue("QSG_RHI_SHADEREFFECT_DEBUG");
    if (!dirtyIndices) {
        for (int i = 0; i < shader.shaderInfo.variables.size(); ++i) {
            const QSGGuiThreadShaderEffectManager::ShaderInfo::Variable &var(shader.shaderInfo.variables.at(i));
            if (var.type == QSGGuiThreadShaderEffectManager::ShaderInfo::Constant) {
                const QSGShaderEffectNode::VariableData &vd(shader.varData.at(i));
                Constant c;
                c.size = var.size;
                c.specialType = vd.specialType;
                if (c.specialType != QSGShaderEffectNode::VariableData::SubRect) {
                    c.value = vd.value;
                    if (shaderEffectDebug) {
                        if (c.specialType == QSGShaderEffectNode::VariableData::None) {
                            qDebug() << "cbuf prepare" << shader.shaderInfo.name << var.name
                                     << "offset" << var.offset << "value" << c.value;
                        } else {
                            qDebug() << "cbuf prepare" << shader.shaderInfo.name << var.name
                                     << "offset" << var.offset << "special" << c.specialType;
                        }
                    }
                } else {
                    Q_ASSERT(var.name.startsWith(QByteArrayLiteral("qt_SubRect_")));
                    c.value = var.name.mid(11);
                }
                m_constants[var.offset] = c;
            }
        }
    } else {
        for (int idx : *dirtyIndices) {
            const int offset = shader.shaderInfo.variables.at(idx).offset;
            const QVariant value = shader.varData.at(idx).value;
            m_constants[offset].value = value;
            if (shaderEffectDebug) {
                qDebug() << "cbuf update" << shader.shaderInfo.name
                         << "offset" << offset << "value" << value;
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 84, as _ZN18QSGRhiShaderLinker12feedSamplersERKN19QSGShaderEffectNode10ShaderDataEPK4QSetIiE
inline void QSGRhiShaderLinker::feedSamplers(const QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)
{
    if (!dirtyIndices) {
        for (int i = 0; i < shader.shaderInfo.variables.size(); ++i) {
            const QSGGuiThreadShaderEffectManager::ShaderInfo::Variable &var(shader.shaderInfo.variables.at(i));
            const QSGShaderEffectNode::VariableData &vd(shader.varData.at(i));
            if (var.type == QSGGuiThreadShaderEffectManager::ShaderInfo::Sampler) {
                Q_ASSERT(vd.specialType == QSGShaderEffectNode::VariableData::Source);

#ifndef QT_NO_DEBUG
                int existingBindPoint = m_samplerNameMap.value(var.name, -1);
                Q_ASSERT(existingBindPoint < 0 || existingBindPoint == var.bindPoint);
#endif

                m_samplers.insert(var.bindPoint, vd.value);
                m_samplerNameMap.insert(var.name, var.bindPoint);
            }
        }
    } else {
        for (int idx : *dirtyIndices) {
            const QSGGuiThreadShaderEffectManager::ShaderInfo::Variable &var(shader.shaderInfo.variables.at(idx));
            const QSGShaderEffectNode::VariableData &vd(shader.varData.at(idx));

#ifndef QT_NO_DEBUG
            int existingBindPoint = m_samplerNameMap.value(var.name, -1);
            Q_ASSERT(existingBindPoint < 0 || existingBindPoint == var.bindPoint);
#endif

            m_samplers.insert(var.bindPoint, vd.value);
            m_samplerNameMap.insert(var.name, var.bindPoint);
        }
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 118, as _ZN18QSGRhiShaderLinker19linkTextureSubRectsEv
inline void QSGRhiShaderLinker::linkTextureSubRects()
{
    // feedConstants stores <name> in Constant::value for subrect entries. Now
    // that both constants and textures are known, replace the name with the
    // texture binding point.
    for (Constant &c : m_constants) {
        if (c.specialType == QSGShaderEffectNode::VariableData::SubRect) {
            if (c.value.userType() == QMetaType::QByteArray) {
                const QByteArray name = c.value.toByteArray();
                if (!m_samplerNameMap.contains(name))
                    qWarning("ShaderEffect: qt_SubRect_%s refers to unknown source texture", name.constData());
                const int binding = m_samplerNameMap[name];
                c.value = binding;
                m_subRectBindings.insert(binding);
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  void QSGRhiShaderLinker::reset(const QShader &vs, const QShader &fs)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinker5resetERK7QShaderS2_(
    QSGRhiShaderLinker *self,
    const QShader *vs,
    const QShader *fs) {
  self->reset(*vs, *fs);
}

//  void QSGRhiShaderLinker::feedConstants(const
//      QSGShaderEffectNode::ShaderData &shader, const QSet<int>
//      *dirtyIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinker13feedConstantsERKN19QSGShaderEffectNode10ShaderDataEPK4QSetIiE(
    QSGRhiShaderLinker *self,
    const QSGShaderEffectNode::ShaderData *shader,
    const QSet<int> *dirtyIndices) {
  self->feedConstants(*shader, dirtyIndices);
}

//  void QSGRhiShaderLinker::feedSamplers(const
//      QSGShaderEffectNode::ShaderData &shader, const QSet<int>
//      *dirtyIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinker12feedSamplersERKN19QSGShaderEffectNode10ShaderDataEPK4QSetIiE(
    QSGRhiShaderLinker *self,
    const QSGShaderEffectNode::ShaderData *shader,
    const QSet<int> *dirtyIndices) {
  self->feedSamplers(*shader, dirtyIndices);
}

//  void QSGRhiShaderLinker::linkTextureSubRects()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinker19linkTextureSubRectsEv(
    QSGRhiShaderLinker *self) {
  self->linkTextureSubRects();
}

//  QSGRhiShaderLinker::~QSGRhiShaderLinker()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinkerD1Ev(QSGRhiShaderLinker *self) {
  delete self;
}
