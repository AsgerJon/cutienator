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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 903, as _ZN34QQuickShapeLinearGradientRhiShaderC1Ei
inline QQuickShapeLinearGradientRhiShader::QQuickShapeLinearGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 972, as _ZNK33QQuickShapeLinearGradientMaterial4typeEv
inline QSGMaterialType *QQuickShapeLinearGradientMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 978, as _ZNK33QQuickShapeLinearGradientMaterial7compareEPK11QSGMaterial
inline int QQuickShapeLinearGradientMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeLinearGradientMaterial *m = static_cast<const QQuickShapeLinearGradientMaterial *>(other);

    QQuickShapeGenericStrokeFillNode *a = node();
    QQuickShapeGenericStrokeFillNode *b = m->node();
    Q_ASSERT(a && b);
    if (a == b)
        return 0;

    const QSGGradientCache::GradientDesc *ga = &a->m_gradient;
    const QSGGradientCache::GradientDesc *gb = &b->m_gradient;

    if (int d = ga->spread - gb->spread)
        return d;

    if (int d = ga->a.x() - gb->a.x())
        return d;
    if (int d = ga->a.y() - gb->a.y())
        return d;
    if (int d = ga->b.x() - gb->b.x())
        return d;
    if (int d = ga->b.y() - gb->b.y())
        return d;

    if (int d = ga->stops.size() - gb->stops.size())
        return d;

    for (int i = 0; i < ga->stops.size(); ++i) {
        if (int d = ga->stops[i].first - gb->stops[i].first)
            return d;
        if (int d = ga->stops[i].second.rgba() - gb->stops[i].second.rgba())
            return d;
    }

    if (int d = a->m_fillTransform.compareTo(b->m_fillTransform))
        return d;

    return 0;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1020, as _ZNK33QQuickShapeLinearGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeLinearGradientMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeLinearGradientRhiShader(viewCount());
}
//  -----------------------------------------------------------------------

//  QSGMaterialType *QQuickShapeLinearGradientMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK33QQuickShapeLinearGradientMaterial4typeEv(
    const QQuickShapeLinearGradientMaterial *self) {
  return self->type();
}

//  int QQuickShapeLinearGradientMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QQuickShapeLinearGradientMaterial7compareEPK11QSGMaterial(
    const QQuickShapeLinearGradientMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialShader *QQuickShapeLinearGradientMaterial::createShader(QSGRen
//      dererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK33QQuickShapeLinearGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QQuickShapeLinearGradientMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  QQuickShapeGenericStrokeFillNode
//      *QQuickShapeLinearGradientMaterial::node() const
extern "C" Q_DECL_EXPORT
QQuickShapeGenericStrokeFillNode *ritual_ZNK33QQuickShapeLinearGradientMaterial4nodeEv(
    const QQuickShapeLinearGradientMaterial *self) {
  return self->node();
}

//  QSGMaterialType *QQuickShapeLinearGradientMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK33QQuickShapeLinearGradientMaterial4typeEv(
    const QQuickShapeLinearGradientMaterial *self) {
  return self->QQuickShapeLinearGradientMaterial::type();
}

//  int QQuickShapeLinearGradientMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK33QQuickShapeLinearGradientMaterial7compareEPK11QSGMaterial(
    const QQuickShapeLinearGradientMaterial *self,
    const QSGMaterial *other) {
  return self->QQuickShapeLinearGradientMaterial::compare(other);
}
