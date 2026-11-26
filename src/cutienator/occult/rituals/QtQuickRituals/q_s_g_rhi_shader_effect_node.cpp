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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 685, as local:qsgrhishadereffectnode.cpp:loadShaderFromFile
static QShader loadShaderFromFile(const QString &filename)
{
    QFile f(filename);
    if (!f.open(QIODevice::ReadOnly)) {
        qWarning() << "Failed to find shader" << filename;
        return QShader();
    }
    return QShader::fromSerialized(f.readAll());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 695, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectDefaultShader
struct QSGRhiShaderEffectDefaultShader
{
    QShader shader;
    quint32 matrixArrayByteSize;
    quint32 opacityOffset;
    qint8 viewCount;
    static QSGRhiShaderEffectDefaultShader create(const QString &filename, int viewCount);
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhishadereffectnode.cpp, line 704, as local:qsgrhishadereffectnode.cpp:QSGRhiShaderEffectDefaultShader::create
inline QSGRhiShaderEffectDefaultShader QSGRhiShaderEffectDefaultShader::create(const QString &filename, int viewCount)
{
    QSGRhiShaderEffectDefaultShader s;
    s.shader = loadShaderFromFile(filename);
    const QList<QShaderDescription::BlockVariable> uboMembers = s.shader.description().uniformBlocks().constFirst().members;
    for (const auto &member: uboMembers) {
        if (member.name == QByteArrayLiteral("qt_Matrix"))
            s.matrixArrayByteSize = member.size;
        else if (member.name == QByteArrayLiteral("qt_Opacity"))
            s.opacityOffset = member.offset;
    }
    s.viewCount = viewCount;
    return s;
}

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
//  -----------------------------------------------------------------------

//  const QMetaObject *QSGRhiShaderEffectNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QSGRhiShaderEffectNode10metaObjectEv(
    const QSGRhiShaderEffectNode *self) {
  return self->metaObject();
}

//  void *QSGRhiShaderEffectNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QSGRhiShaderEffectNode11qt_metacastEPKc(
    QSGRhiShaderEffectNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiShaderEffectNode::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QSGRhiShaderEffectNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiShaderEffectNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QSGRhiShaderEffectNode::syncMaterial(SyncData *syncData)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGRhiShaderEffectNode12syncMaterialEPN19QSGShaderEffectNode8SyncDataE(
    QSGRhiShaderEffectNode *self,
    QSGShaderEffectNode::SyncData *syncData) {
  self->syncMaterial(syncData);
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
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGRhiShaderEffectNode")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleTextureChange()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleTextureChange()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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
