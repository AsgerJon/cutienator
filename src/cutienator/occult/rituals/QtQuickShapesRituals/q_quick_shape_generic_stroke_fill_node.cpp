//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickshapegenericrenderer_p.h"
#include <QtGui/private/qtriangulator_p.h>
#include <QtGui/private/qtriangulatingstroker_p.h>
#include <rhi/qrhi.h>
#include <QSGVertexColorMaterial>
#include <QSGTextureProvider>
#include <private/qsgplaintexture_p.h>
#include <QtQuick/private/qsggradientcache_p.h>
#if QT_CONFIG(thread)
#include <QThreadPool>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 891, as _ZN33QQuickShapeGenericMaterialFactory17createTextureFillEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createTextureFill(QQuickWindow *window,
                                                                  QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeTextureFillMaterial(node);

    qWarning("Texture fill material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 844, as _ZN33QQuickShapeGenericMaterialFactory17createVertexColorEP12QQuickWindow
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createVertexColor(QQuickWindow *window)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QSGVertexColorMaterial;

    qWarning("Vertex-color material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 855, as _ZN33QQuickShapeGenericMaterialFactory20createLinearGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createLinearGradient(QQuickWindow *window,
                                                                     QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeLinearGradientMaterial(node);

    qWarning("Linear gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 867, as _ZN33QQuickShapeGenericMaterialFactory20createRadialGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createRadialGradient(QQuickWindow *window,
                                                                     QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeRadialGradientMaterial(node);

    qWarning("Radial gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 879, as _ZN33QQuickShapeGenericMaterialFactory21createConicalGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createConicalGradient(QQuickWindow *window,
                                                                      QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeConicalGradientMaterial(node);

    qWarning("Conical gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 85, as _ZN32QQuickShapeGenericStrokeFillNode10preprocessEv
inline void QQuickShapeGenericStrokeFillNode::preprocess()
{
    if (m_fillTextureProvider != nullptr) {
        if (QSGDynamicTexture *texture = qobject_cast<QSGDynamicTexture *>(m_fillTextureProvider->texture()))
            texture->updateTexture();
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 93, as _ZN32QQuickShapeGenericStrokeFillNode20handleTextureChangedEv
inline void QQuickShapeGenericStrokeFillNode::handleTextureChanged()
{
    markDirty(QSGNode::DirtyMaterial);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 98, as _ZN32QQuickShapeGenericStrokeFillNode30handleTextureProviderDestroyedEv
inline void QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed()
{
    m_fillTextureProvider = nullptr;
    markDirty(QSGNode::DirtyMaterial);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickShapeGenericStrokeFillNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickShapeGenericStrokeFillNode10metaObjectEv(
    const QQuickShapeGenericStrokeFillNode *self) {
  return self->metaObject();
}

//  void QQuickShapeGenericStrokeFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->preprocess();
}

//  void QQuickShapeGenericStrokeFillNode::handleTextureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode20handleTextureChangedEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->handleTextureChanged();
}

//  void QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode30handleTextureProviderDestroyedEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->handleTextureProviderDestroyed();
}

//  QQuickShapeGenericStrokeFillNode as the QSGGeometryNode it is built on
extern "C" Q_DECL_EXPORT
QSGGeometryNode *ritual_cast_QQuickShapeGenericStrokeFillNode_QSGGeometryNode(
    QQuickShapeGenericStrokeFillNode *self) {
  return static_cast<QSGGeometryNode *>(self);
}

//  void QQuickShapeGenericStrokeFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->QQuickShapeGenericStrokeFillNode::preprocess();
}
