//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgrhishadereffectnode_p.h"
#include "qsgdefaultrendercontext_p.h"
#include "qsgrhisupport_p.h"
#include <qsgmaterialshader.h>
#include <qsgtextureprovider.h>
#include <private/qsgplaintexture_p.h>
#include <rhi/qshaderdescription.h>
#include <QQmlFile>
#include <QtGui/qquaternion.h>
#include <QFile>
#include <QFileSelector>
#include <QMutexLocker>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 518, as _ZN26QSGRhiShaderEffectMaterialC1EP22QSGRhiShaderEffectNode
inline QSGRhiShaderEffectMaterial::QSGRhiShaderEffectMaterial(QSGRhiShaderEffectNode *node)
    : m_node(node)
{
    setFlag(Blending | RequiresFullMatrix, true); // may be changed in syncMaterial()
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 655, as _ZN22QSGRhiShaderEffectNode30updateNormalizedTextureSubRectEb
inline QRectF QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(bool supportsAtlasTextures)
{
    QRectF srcRect(0, 0, 1, 1);
    bool geometryUsesTextureSubRect = false;
    if (supportsAtlasTextures) {
        QSGTextureProvider *tp = nullptr;
        for (int binding = 0, count = m_material.m_textureProviders.size(); binding != count; ++binding) {
            if (QSGTextureProvider *candidate = m_material.m_textureProviders.at(binding)) {
                if (!tp) {
                    tp = candidate;
                } else { // there can only be one...
                    tp = nullptr;
                    break;
                }
            }
        }
        if (tp && tp->texture()) {
            srcRect = tp->texture()->normalizedTextureSubRect();
            geometryUsesTextureSubRect = true;
        }
    }

    if (m_material.m_geometryUsesTextureSubRect != geometryUsesTextureSubRect) {
        m_material.m_geometryUsesTextureSubRect = geometryUsesTextureSubRect;
        markDirty(QSGNode::DirtyMaterial);
    }

    return srcRect;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 898, as _ZN22QSGRhiShaderEffectNode10preprocessEv
inline void QSGRhiShaderEffectNode::preprocess()
{
    for (QSGTextureProvider *tp : std::as_const(m_material.m_textureProviders)) {
        if (tp) {
            if (QSGDynamicTexture *texture = qobject_cast<QSGDynamicTexture *>(tp->texture()))
                texture->updateTexture();
        }
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 884, as _ZN22QSGRhiShaderEffectNode19handleTextureChangeEv
inline void QSGRhiShaderEffectNode::handleTextureChange()
{
    markDirty(QSGNode::DirtyMaterial);
    emit textureChanged();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 890, as _ZN22QSGRhiShaderEffectNode30handleTextureProviderDestroyedEP7QObject
inline void QSGRhiShaderEffectNode::handleTextureProviderDestroyed(QObject *object)
{
    for (QSGTextureProvider *&tp : m_material.m_textureProviders) {
        if (tp == object)
            tp = nullptr;
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QSGRhiShaderEffectNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QSGRhiShaderEffectNode10metaObjectEv(
    const QSGRhiShaderEffectNode *self) {
  return self->metaObject();
}

//  QRectF QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(bool
//      supportsAtlasTextures)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN22QSGRhiShaderEffectNode30updateNormalizedTextureSubRectEb(
    QSGRhiShaderEffectNode *self,
    bool supportsAtlasTextures) {
  return new QRectF(
      self->updateNormalizedTextureSubRect(
          supportsAtlasTextures));
}

//  void QSGRhiShaderEffectNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGRhiShaderEffectNode10preprocessEv(
    QSGRhiShaderEffectNode *self) {
  self->preprocess();
}

//  void QSGRhiShaderEffectNode::handleTextureChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGRhiShaderEffectNode19handleTextureChangeEv(
    QSGRhiShaderEffectNode *self) {
  self->handleTextureChange();
}

//  void QSGRhiShaderEffectNode::handleTextureProviderDestroyed(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGRhiShaderEffectNode30handleTextureProviderDestroyedEP7QObject(
    QSGRhiShaderEffectNode *self,
    QObject *object) {
  self->handleTextureProviderDestroyed(object);
}

//  QRectF QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(bool
//      supportsAtlasTextures)
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZN22QSGRhiShaderEffectNode30updateNormalizedTextureSubRectEb(
    QSGRhiShaderEffectNode *self,
    bool supportsAtlasTextures) {
  return new QRectF(
      self->QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(
          supportsAtlasTextures));
}

//  void QSGRhiShaderEffectNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGRhiShaderEffectNode10preprocessEv(
    QSGRhiShaderEffectNode *self) {
  self->QSGRhiShaderEffectNode::preprocess();
}
