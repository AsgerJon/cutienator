//  Written by dev_tooling.RitualGenerator from the records of QtQuickEffects
//  /6.12.0/QtQuickEffects/private/qquickrectangularshadow_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuickEffects/qtquickeffectsexports.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#include <QtQuickEffects/QtQuickEffects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtypes.h>
#include <QtQuickEffects/private/qquickrectangularshadow_p_p.h>
#include <QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtCore/qurl.h>
#include <QtGui/qvector4d.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 665, as _ZN30QQuickRectangularShadowPrivateC1Ev
inline QQuickRectangularShadowPrivate::QQuickRectangularShadowPrivate()
{
    Q_Q(QQuickRectangularShadow);
    m_defaultMaterial = new QQuickShaderEffect(q);
    // Initial values to not get warnings of missing properties.
    // Proper values are updated later.
    m_defaultMaterial->setProperty("iResolution", QVector3D());
    m_defaultMaterial->setProperty("rectSize", QPointF());
    m_defaultMaterial->setProperty("color", QColorConstants::Black);
    // Add both radius variants, shader decides which one to use
    m_defaultMaterial->setProperty("radius", 0.0);
    m_defaultMaterial->setProperty("radius4", QVector4D());
    m_defaultMaterial->setProperty("blur", 10.0);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 690, as _ZN30QQuickRectangularShadowPrivate10initializeEv
inline void QQuickRectangularShadowPrivate::initialize()
{
    Q_Q(QQuickRectangularShadow);
    if (m_initialized)
        return;
    if (!q->isComponentComplete())
        return;
    if (!q->window())
        return;
    if (q->width() <= 0 || q->height() <= 0)
        return;

    m_defaultMaterial->setParentItem(q);
    m_defaultMaterial->setZ(-1);
    // Default to antialiased
    setImplicitAntialiasing(true);

    updateDefaultShader();
    QUrl vs = QUrl(QStringLiteral("qrc:/data/shaders/rectangularshadow.vert.qsb"));
    m_defaultMaterial->setVertexShader(vs);

    updateShaderSource();
    m_initialized = true;
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 722, as _ZN30QQuickRectangularShadowPrivate20handleGeometryChangeERK6QRectFS2_
inline void QQuickRectangularShadowPrivate::handleGeometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    Q_UNUSED(newGeometry);
    Q_UNUSED(oldGeometry);
    initialize();
    updateSizeProperties();
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 715, as _ZN30QQuickRectangularShadowPrivate16handleItemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickRectangularShadowPrivate::handleItemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &value)
{
    Q_UNUSED(value);
    if (change == QQuickItem::ItemSceneChange)
        initialize();
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 730, as _ZNK30QQuickRectangularShadowPrivate10getPaddingEv
inline qreal QQuickRectangularShadowPrivate::getPadding() const
{
    return qreal(m_blur * 2 + m_spread * 2);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 735, as _ZN30QQuickRectangularShadowPrivate11updateColorEv
inline void QQuickRectangularShadowPrivate::updateColor()
{
    currentMaterial()->setProperty("color", m_color);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 740, as _ZN30QQuickRectangularShadowPrivate18updateShaderSourceEv
inline void QQuickRectangularShadowPrivate::updateShaderSource()
{
    Q_Q(QQuickRectangularShadow);
    if (!q->isComponentComplete())
        return;

    if (m_material)
        m_defaultMaterial->setVisible(false);

    updateSizeProperties();
    updateColor();
    currentMaterial()->setVisible(true);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 754, as _ZN30QQuickRectangularShadowPrivate20updateSizePropertiesEv
inline void QQuickRectangularShadowPrivate::updateSizeProperties()
{
    Q_Q(QQuickRectangularShadow);

    // Check if we should switch the shader
    updateDefaultShader();

    auto *material = currentMaterial();

    const qreal padding = getPadding();
    const qreal effectWidth = q->width() + padding;
    const qreal effectHeight = q->height() + padding;

    const qreal effectX = (q->width() - effectWidth) * 0.5 + m_offset.x();
    const qreal effectY = (q->height() - effectHeight) * 0.5 + m_offset.y();
    material->setX(effectX);
    material->setY(effectY);
    material->setWidth(effectWidth);
    material->setHeight(effectHeight);

    const qreal aa = q->antialiasing() ? 1.0 : 0.0;
    material->setProperty("iResolution", QVector3D(effectWidth, effectHeight, 1.0));

    // The shrinking ratio when the amount of blur increases
    // so blur extends also towards inner direction.
    const qreal blurReduction = m_blur * 1.8 + aa;
    QPointF rectSize = QPointF((effectWidth * 0.5 - blurReduction),
                               (effectHeight * 0.5 - blurReduction));
    material->setProperty("rectSize", rectSize);
    if (useIndividualRadius()) {
        const QVector4D clampedRad4 = clampedRadius4R();
        material->setProperty("radius4", clampedRad4);
        material->setProperty("radius", -1);
    } else {
        const qreal clampedRad = clampedRadius(m_radius);
        material->setProperty("radius", clampedRad);
    }
    // Extend blur amount to match with how the CSS box-shadow blur behaves.
    // and to fully utilize the item size.
    const qreal shaderBlur = m_blur * 2.1 + aa;
    material->setProperty("blur", shaderBlur);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 797, as _ZN30QQuickRectangularShadowPrivate12updateCachedEv
inline void QQuickRectangularShadowPrivate::updateCached()
{
    QQuickItemPrivate *effectPrivate = QQuickItemPrivate::get(currentMaterial());
    effectPrivate->layer()->setEnabled(m_cached);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 803, as _ZNK30QQuickRectangularShadowPrivate13clampedRadiusEd
inline qreal QQuickRectangularShadowPrivate::clampedRadius(qreal radius) const
{
    Q_Q(const QQuickRectangularShadow);
    qreal maxRadius = qMin(q->width(), q->height()) * 0.5;
    maxRadius += m_spread * 2;
    qreal spreadRadius = radius + m_spread;
    if (radius < m_spread && !qFuzzyIsNull(m_spread)) {
        // CSS box-shadow has a specific math to calculate radius with spread
        // https://www.w3.org/TR/css-backgrounds-3/#shadow-shape
        // "the spread distance is first multiplied by the proportion 1 + (r-1)^3,
        // where r is the ratio of the border radius to the spread distance".
        qreal r = (radius / m_spread) - 1;
        spreadRadius = radius + m_spread * (1 + r * r * r);
    }
    // Reduce the radius when the blur increases
    const qreal blurReduce = m_blur * 0.75;
    maxRadius -= blurReduce;
    const qreal limitedRadius = qMax(0.0, spreadRadius - blurReduce);
    return qMin(limitedRadius, maxRadius);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 824, as _ZNK30QQuickRectangularShadowPrivate15clampedRadius4REv
inline QVector4D QQuickRectangularShadowPrivate::clampedRadius4R() const
{
    Q_Q(const QQuickRectangularShadow);
    // Clamp each corner individually
    qreal tl = clampedRadius(q->topLeftRadius());
    qreal tr = clampedRadius(q->topRightRadius());
    qreal bl = clampedRadius(q->bottomLeftRadius());
    qreal br = clampedRadius(q->bottomRightRadius());
    return QVector4D(tl, tr, bl, br);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 835, as _ZNK30QQuickRectangularShadowPrivate15currentMaterialEv
inline QQuickItem *QQuickRectangularShadowPrivate::currentMaterial() const
{
    if (m_material)
        return m_material;
    else
        return m_defaultMaterial;
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 843, as _ZN30QQuickRectangularShadowPrivate28maybeSetImplicitAntialiasingEv
inline void QQuickRectangularShadowPrivate::maybeSetImplicitAntialiasing()
{
    bool implicitAA = (m_radius > 0);
    if (extra.isAllocated() && !implicitAA) {
        const auto &e = extra.value();
        implicitAA = (e.isTopLeftRadiusSet && e.topLeftRadius > 0)
                || (e.isTopRightRadiusSet && e.topRightRadius > 0)
                || (e.isBottomLeftRadiusSet && e.bottomLeftRadius > 0)
                || (e.isBottomRightRadiusSet && e.bottomRightRadius > 0);
    }
    setImplicitAntialiasing(implicitAA);
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 856, as _ZNK30QQuickRectangularShadowPrivate19useIndividualRadiusEv
inline bool QQuickRectangularShadowPrivate::useIndividualRadius() const
{
    bool individualRadius = false;
    if (extra.isAllocated()) {
        const auto &e = extra.value();
        individualRadius = e.isTopLeftRadiusSet
                || e.isTopRightRadiusSet
                || e.isBottomLeftRadiusSet
                || e.isBottomRightRadiusSet;
    }
    return individualRadius;
}

//  from ../qtdeclarative/src/effects/qquickrectangularshadow.cpp, line 680, as _ZN30QQuickRectangularShadowPrivate19updateDefaultShaderEv
inline void QQuickRectangularShadowPrivate::updateDefaultShader()
{
    QUrl fs;
    if (useIndividualRadius())
        fs = QUrl(QStringLiteral("qrc:/data/shaders/rectangularshadow4r.frag.qsb"));
    else
        fs = QUrl(QStringLiteral("qrc:/data/shaders/rectangularshadow.frag.qsb"));
    m_defaultMaterial->setFragmentShader(fs);
}
//  -----------------------------------------------------------------------

//  QQuickRectangularShadow *QQuickRectangularShadowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickRectangularShadow *ritual_ZN30QQuickRectangularShadowPrivate6q_funcEv(
    QQuickRectangularShadowPrivate *self) {
  return self->q_func();
}

//  const QQuickRectangularShadow *QQuickRectangularShadowPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickRectangularShadow *ritual_ZNK30QQuickRectangularShadowPrivate6q_funcEv(
    const QQuickRectangularShadowPrivate *self) {
  return self->q_func();
}

//  QQuickRectangularShadowPrivate::QQuickRectangularShadowPrivate()
extern "C" Q_DECL_EXPORT
QQuickRectangularShadowPrivate *ritual_ZN30QQuickRectangularShadowPrivateC1Ev() {
  return new QQuickRectangularShadowPrivate();
}

//  void QQuickRectangularShadowPrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate10initializeEv(
    QQuickRectangularShadowPrivate *self) {
  self->initialize();
}

//  void QQuickRectangularShadowPrivate::handleGeometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate20handleGeometryChangeERK6QRectFS2_(
    QQuickRectangularShadowPrivate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->handleGeometryChange(*newGeometry, *oldGeometry);
}

//  void
//      QQuickRectangularShadowPrivate::handleItemChange(QQuickItem::ItemChan
//      ge change, const QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate16handleItemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRectangularShadowPrivate *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->handleItemChange(change, *value);
}

//  qreal QQuickRectangularShadowPrivate::getPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK30QQuickRectangularShadowPrivate10getPaddingEv(
    const QQuickRectangularShadowPrivate *self) {
  return self->getPadding();
}

//  void QQuickRectangularShadowPrivate::updateColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate11updateColorEv(
    QQuickRectangularShadowPrivate *self) {
  self->updateColor();
}

//  void QQuickRectangularShadowPrivate::updateShaderSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate18updateShaderSourceEv(
    QQuickRectangularShadowPrivate *self) {
  self->updateShaderSource();
}

//  void QQuickRectangularShadowPrivate::updateSizeProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate20updateSizePropertiesEv(
    QQuickRectangularShadowPrivate *self) {
  self->updateSizeProperties();
}

//  void QQuickRectangularShadowPrivate::updateCached()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate12updateCachedEv(
    QQuickRectangularShadowPrivate *self) {
  self->updateCached();
}

//  qreal QQuickRectangularShadowPrivate::clampedRadius(qreal radius) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK30QQuickRectangularShadowPrivate13clampedRadiusEd(
    const QQuickRectangularShadowPrivate *self,
    qreal radius) {
  return self->clampedRadius(radius);
}

//  QVector4D QQuickRectangularShadowPrivate::clampedRadius4R() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK30QQuickRectangularShadowPrivate15clampedRadius4REv(
    const QQuickRectangularShadowPrivate *self) {
  return new QVector4D(self->clampedRadius4R());
}

//  QQuickItem *QQuickRectangularShadowPrivate::currentMaterial() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK30QQuickRectangularShadowPrivate15currentMaterialEv(
    const QQuickRectangularShadowPrivate *self) {
  return self->currentMaterial();
}

//  void QQuickRectangularShadowPrivate::maybeSetImplicitAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate28maybeSetImplicitAntialiasingEv(
    QQuickRectangularShadowPrivate *self) {
  self->maybeSetImplicitAntialiasing();
}

//  bool QQuickRectangularShadowPrivate::useIndividualRadius() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickRectangularShadowPrivate19useIndividualRadiusEv(
    const QQuickRectangularShadowPrivate *self) {
  return self->useIndividualRadius();
}

//  void QQuickRectangularShadowPrivate::updateDefaultShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickRectangularShadowPrivate19updateDefaultShaderEv(
    QQuickRectangularShadowPrivate *self) {
  self->updateDefaultShader();
}

#endif  // QT_CONFIG(quick_shadereffect)
