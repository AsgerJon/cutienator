//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 253, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectMaterialShader
class QSGRhiShaderEffectMaterialShader : public QSGMaterialShader
{
public:
    QSGRhiShaderEffectMaterialShader(const QSGRhiShaderEffectMaterial *material);

    bool updateUniformData(RenderState &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial) override;
    void updateSampledImage(RenderState &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial, QSGMaterial *oldMaterial) override;
    bool updateGraphicsPipelineState(RenderState &state, GraphicsPipelineState *ps, QSGMaterial *newMaterial, QSGMaterial *oldMaterial) override;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 263, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectMaterialShader::QSGRhiShaderEffectMaterialShader
inline QSGRhiShaderEffectMaterialShader::QSGRhiShaderEffectMaterialShader(const QSGRhiShaderEffectMaterial *material)
{
    setFlag(UpdatesGraphicsPipelineState, true);
    setShader(VertexStage, material->m_vertexShader);
    setShader(FragmentStage, material->m_fragmentShader);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 277, as local:qsgrhishadereffectnode.cpp:fillUniformBlockMember
template<typename T>
static inline void fillUniformBlockMember(char *dst, const T *value, int valueCount, int fieldSizeBytes)
{
    const size_t valueBytes = sizeof(T) * valueCount;
    const size_t fieldBytes = fieldSizeBytes;
    if (valueBytes <= fieldBytes) {
        memcpy(dst, value, valueBytes);
        if (valueBytes < fieldBytes)
            memset(dst + valueBytes, 0, fieldBytes - valueBytes);
    } else {
        memcpy(dst, value, fieldBytes);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 453, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectMaterialShader::updateSampledImage
inline void QSGRhiShaderEffectMaterialShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                          QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_UNUSED(oldMaterial);
    QSGRhiShaderEffectMaterial *mat = static_cast<QSGRhiShaderEffectMaterial *>(newMaterial);

    if (binding >= QSGRhiShaderEffectMaterial::MAX_BINDINGS)
        return;

    QSGTextureProvider *tp = mat->m_textureProviders.at(binding);
    if (tp) {
        if (QSGTexture *t = tp->texture()) {
            t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());

            if (t->isAtlasTexture() && !mat->m_geometryUsesTextureSubRect && !mat->usesSubRectUniform(binding)) {
                // Why the hassle with the batch: while removedFromAtlas() is
                // able to operate with its own resource update batch (which is
                // then committed immediately), that approach is wrong when the
                // atlas enqueued (in the updateRhiTexture() above) not yet
                // committed operations to state.resourceUpdateBatch()... The
                // only safe way then is to use the same batch the atlas'
                // updateRhiTexture() used.
                QSGTexture *newTexture = t->removedFromAtlas(state.resourceUpdateBatch());
                if (newTexture) {
                    t = newTexture;
                    t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
                }
            }
            *texture = t;
            return;
        }
    }

    if (!mat->m_dummyTexture) {
        mat->m_dummyTexture = new QSGPlainTexture;
        mat->m_dummyTexture->setFiltering(QSGTexture::Nearest);
        mat->m_dummyTexture->setHorizontalWrapMode(QSGTexture::Repeat);
        mat->m_dummyTexture->setVerticalWrapMode(QSGTexture::Repeat);
        QImage img(128, 128, QImage::Format_ARGB32_Premultiplied);
        img.fill(0);
        mat->m_dummyTexture->setImage(img);
        mat->m_dummyTexture->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
    }
    *texture = mat->m_dummyTexture;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 499, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectMaterialShader::updateGraphicsPipelineState
inline bool QSGRhiShaderEffectMaterialShader::updateGraphicsPipelineState(RenderState &state, GraphicsPipelineState *ps,
                                                                   QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_UNUSED(state);
    Q_UNUSED(oldMaterial);
    QSGRhiShaderEffectMaterial *mat = static_cast<QSGRhiShaderEffectMaterial *>(newMaterial);

    switch (mat->m_cullMode) {
    case QSGShaderEffectNode::FrontFaceCulling:
        ps->cullMode = GraphicsPipelineState::CullFront;
        return true;
    case QSGShaderEffectNode::BackFaceCulling:
        ps->cullMode = GraphicsPipelineState::CullBack;
        return true;
    default:
        return false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 532, as local:qsgrhishadereffectnode.cpp:hasAtlasTexture
static bool hasAtlasTexture(const QList<QSGTextureProvider *> &textureProviders)
{
    for (QSGTextureProvider *tp : textureProviders) {
        if (tp && tp->texture() && tp->texture()->isAtlasTexture())
            return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 593, as _ZNK26QSGRhiShaderEffectMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QSGRhiShaderEffectMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QSGRhiShaderEffectMaterialShader(this);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 588, as _ZNK26QSGRhiShaderEffectMaterial4typeEv
inline QSGMaterialType *QSGRhiShaderEffectMaterial::type() const
{
    return m_materialType;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 599, as _ZN26QSGRhiShaderEffectMaterial22updateTextureProvidersEb
inline void QSGRhiShaderEffectMaterial::updateTextureProviders(bool layoutChange)
{
    if (layoutChange) {
        for (QSGTextureProvider *tp : std::as_const(m_textureProviders)) {
            if (tp) {
                QObject::disconnect(tp, SIGNAL(textureChanged()), m_node,
                                    SLOT(handleTextureChange()));
                QObject::disconnect(tp, SIGNAL(destroyed(QObject*)), m_node,
                                    SLOT(handleTextureProviderDestroyed(QObject*)));
            }
        }
        m_textureProviders.fill(nullptr, MAX_BINDINGS);
    }

    for (auto it = m_linker.m_samplers.constBegin(), itEnd = m_linker.m_samplers.constEnd(); it != itEnd; ++it) {
        const int binding = it.key();
        QQuickItem *source = qobject_cast<QQuickItem *>(qvariant_cast<QObject *>(it.value()));
        QSGTextureProvider *newProvider = source && source->isTextureProvider() ? source->textureProvider() : nullptr;
        if (binding >= MAX_BINDINGS) {
            qWarning("Sampler at binding %d exceeds the available ShaderEffect binding slots; ignored",
                     binding);
            continue;
        }
        QSGTextureProvider *&activeProvider(m_textureProviders[binding]);
        if (newProvider != activeProvider) {
            if (activeProvider) {
                QObject::disconnect(activeProvider, SIGNAL(textureChanged()), m_node,
                                    SLOT(handleTextureChange()));
                QObject::disconnect(activeProvider, SIGNAL(destroyed(QObject*)), m_node,
                                    SLOT(handleTextureProviderDestroyed(QObject*)));
            }
            if (newProvider) {
                Q_ASSERT_X(newProvider->thread() == QThread::currentThread(),
                           "QSGRhiShaderEffectMaterial::updateTextureProviders",
                           "Texture provider must belong to the rendering thread");
                QObject::connect(newProvider, SIGNAL(textureChanged()), m_node, SLOT(handleTextureChange()));
                QObject::connect(newProvider, SIGNAL(destroyed(QObject*)), m_node,
                                 SLOT(handleTextureProviderDestroyed(QObject*)));
            } else {
                const char *typeName = source ? source->metaObject()->className() : it.value().typeName();
                qWarning("ShaderEffect: Texture t%d is not assigned a valid texture provider (%s).",
                         binding, typeName);
            }
            activeProvider = newProvider;
        }
    }
}
//  -----------------------------------------------------------------------

//  A QSGRhiShaderEffectMaterial that Python can take functions over in. Every QSGRhiShaderEffectMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGRhiShaderEffectMaterialCall0)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQSGRhiShaderEffectMaterialCall1)(const void *, int *);
typedef void * (*CuteQSGRhiShaderEffectMaterialCall2)(const void *, int, int *);
class CuteQSGRhiShaderEffectMaterial : public QSGRhiShaderEffectMaterial {
public:
  using QSGRhiShaderEffectMaterial::QSGRhiShaderEffectMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  int QSGRhiShaderEffectMaterial::compare(const QSGMaterial *other)
  //      const
  int compare(const QSGMaterial *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiShaderEffectMaterialCall0 call = reinterpret_cast<CuteQSGRhiShaderEffectMaterialCall0>(taken[0]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGRhiShaderEffectMaterial::compare(other);
  }

  //  QSGMaterialType *QSGRhiShaderEffectMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiShaderEffectMaterialCall1 call = reinterpret_cast<CuteQSGRhiShaderEffectMaterialCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGRhiShaderEffectMaterial::type();
  }

  //  QSGMaterialShader *QSGRhiShaderEffectMaterial::createShader(QSGRender
  //      erInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiShaderEffectMaterialCall2 call = reinterpret_cast<CuteQSGRhiShaderEffectMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGRhiShaderEffectMaterial::createShader(renderMode);
  }
};

//  int QSGRhiShaderEffectMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QSGRhiShaderEffectMaterial7compareEPK11QSGMaterial(
    const QSGRhiShaderEffectMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialType *QSGRhiShaderEffectMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK26QSGRhiShaderEffectMaterial4typeEv(
    const QSGRhiShaderEffectMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGRhiShaderEffectMaterial::createShader(QSGRendererIn
//      terface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK26QSGRhiShaderEffectMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGRhiShaderEffectMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  void QSGRhiShaderEffectMaterial::updateTextureProviders(bool
//      layoutChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGRhiShaderEffectMaterial22updateTextureProvidersEb(
    QSGRhiShaderEffectMaterial *self,
    bool layoutChange) {
  self->updateTextureProviders(layoutChange);
}

//  bool QSGRhiShaderEffectMaterial::usesSubRectUniform(int binding) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGRhiShaderEffectMaterial18usesSubRectUniformEi(
    const QSGRhiShaderEffectMaterial *self,
    int binding) {
  return self->usesSubRectUniform(binding);
}

//  a Python function taken by a CuteQSGRhiShaderEffectMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiShaderEffectMaterial(
    QSGRhiShaderEffectMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiShaderEffectMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGRhiShaderEffectMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK26QSGRhiShaderEffectMaterial4typeEv(
    const QSGRhiShaderEffectMaterial *self) {
  return self->QSGRhiShaderEffectMaterial::type();
}
