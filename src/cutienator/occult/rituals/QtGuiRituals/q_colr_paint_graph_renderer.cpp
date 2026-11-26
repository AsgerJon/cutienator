//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolrpaintgraphrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolrpaintgraphrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qcolrpaintgraphrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qfontengine.cpp, line 36, as _Z8lcColrv1v
inline const QLoggingCategory &lcColrv1()
{
    static const QLoggingCategory category("qt.text.font.colrv1");
    return category;
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 9, as _ZN23QColrPaintGraphRendererD1Ev
inline QColrPaintGraphRenderer::~QColrPaintGraphRenderer()
{
    Q_ASSERT(m_oldPaths.isEmpty());
    Q_ASSERT(m_oldTransforms.isEmpty());

    delete m_painter;
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 17, as _ZN23QColrPaintGraphRenderer4saveEv
inline void QColrPaintGraphRenderer::save()
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[enter scope]";

    m_oldPaths.append(m_currentPath);
    m_oldTransforms.append(m_currentTransform);

    if (m_painter != nullptr)
        m_painter->save();
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 30, as _ZN23QColrPaintGraphRenderer7restoreEv
inline void QColrPaintGraphRenderer::restore()
{
    m_currentPath = m_oldPaths.takeLast();
    m_currentTransform = m_oldTransforms.takeLast();

    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[exit scope]";

    if (m_painter != nullptr)
        m_painter->restore();
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 64, as _ZN23QColrPaintGraphRenderer10appendPathERK12QPainterPath
inline void QColrPaintGraphRenderer::appendPath(const QPainterPath &path)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[append path: " << path.controlPointRect()
        << "]";

    QPainterPath transformedPath(m_currentTransform.map(path));
    m_currentPath = m_currentPath.united(transformedPath);
    if (!isRendering())
        m_boundingRect = m_boundingRect.united(transformedPath.boundingRect());
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 77, as _ZN23QColrPaintGraphRenderer7setPathERK12QPainterPath
inline void QColrPaintGraphRenderer::setPath(const QPainterPath &path)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[set path]";

    m_currentPath.clear();
    appendPath(path);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 55, as _ZN23QColrPaintGraphRenderer16prependTransformERK10QTransform
inline void QColrPaintGraphRenderer::prependTransform(const QTransform &transform)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[prepend transform: " << transform
        << "]";
    m_currentTransform = transform * m_currentTransform;
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 87, as _ZN23QColrPaintGraphRenderer13setSolidColorE6QColor
inline void QColrPaintGraphRenderer::setSolidColor(QColor color)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[solid " << color
        << "]";

    if (m_painter != nullptr)
        m_painter->setBrush(color);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 192, as _ZN23QColrPaintGraphRenderer17setRadialGradientE7QPointFdS0_dN9QGradient6SpreadERK5QListISt4pairId6QColorEE
inline void QColrPaintGraphRenderer::setRadialGradient(QPointF c0, qreal r0,
                                                QPointF c1, qreal r1,
                                                QGradient::Spread spread,
                                                const QGradientStops &gradientStops)
{
    if (m_painter != nullptr) {
        qCDebug(lcColrv1).noquote().nospace()
            << QByteArray().fill(' ', m_oldPaths.size() * 2)
            << "[radial gradient " << c0
            << ", rad=" << r0
            << ", " << c1
            << ", rad=" << r1
            << ", spread: " << spread
            << ", stop count: " << gradientStops.size()
            << "]";

        QPointF c0e(c0 + QPointF(r0, 0.0));
        QPointF c1e(c1 + QPointF(r1, 0.0));

        c0 = m_currentTransform.map(c0);
        c0e = m_currentTransform.map(c0e);
        c1 = m_currentTransform.map(c1);
        c1e = m_currentTransform.map(c1e);

        const QVector2D d0(c0e - c0);
        const QVector2D d1(c1e - c1);

        QRadialGradient gradient(c1, d1.length(), c0, d0.length());
        gradient.setCoordinateMode(QGradient::LogicalMode);
        gradient.setSpread(spread);
        gradient.setStops(gradientStops);
        m_painter->setBrush(gradient);
    }
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 98, as _ZN23QColrPaintGraphRenderer17setLinearGradientE7QPointFS0_S0_N9QGradient6SpreadERK5QListISt4pairId6QColorEE
inline void QColrPaintGraphRenderer::setLinearGradient(QPointF p0, QPointF p1, QPointF p2,
                                                QGradient::Spread spread,
                                                const QGradientStops &gradientStops)
{
    if (m_painter != nullptr) {
        qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[linear gradient " << p0 << ", " << p1 << ", " << p2
        << ", spread: " << spread
        << ", stop count: " << gradientStops.size()
        << "]";

        // Calculate new start and end point for single vector gradient preferred by Qt
        // Find vector perpendicular to p0p2 and project p0p1 onto this to find p3 (final
        // stop)
        // https://learn.microsoft.com/en-us/typography/opentype/spec/colr#linear-gradients
        QVector2D p0p2(p2 - p0);
        if (qFuzzyIsNull(p0p2.lengthSquared())) {
            qCWarning(lcColrv1) << "Malformed linear gradient in COLRv1 graph. Points:"
                                << p0
                                << p1
                                << p2;
            return;
        }

        // v is perpendicular to p0p2
        QVector2D v(p0p2.y(), -p0p2.x());

        // u is the vector from p0 to p1
        QVector2D u(p1 - p0);
        if (qFuzzyIsNull(u.lengthSquared())) {
            qCWarning(lcColrv1) << "Malformed linear gradient in COLRv1 graph. Points:"
                                << p0
                                << p1
                                << p2;
            return;
        }

        // We find the projected point p3
        QPointF p3((QVector2D(p0) + v * QVector2D::dotProduct(u, v) / v.lengthSquared()).toPointF());

        p0 = m_currentTransform.map(p0);
        p3 = m_currentTransform.map(p1);

        QLinearGradient linearGradient(p0, p3);
        linearGradient.setSpread(spread);
        linearGradient.setStops(gradientStops);
        linearGradient.setCoordinateMode(QGradient::LogicalMode);

        m_painter->setBrush(linearGradient);
    }
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 151, as _ZN23QColrPaintGraphRenderer18setConicalGradientE7QPointFddN9QGradient6SpreadERK5QListISt4pairId6QColorEE
inline void QColrPaintGraphRenderer::setConicalGradient(QPointF center,
                                                 qreal startAngle, qreal endAngle,
                                                 QGradient::Spread spread,
                                                 const QGradientStops &gradientStops)
{
    if (m_painter != nullptr) {
        qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
            << "[conical gradient " << center
            << ", startAngle=" << startAngle
            << ", endAngle=" << endAngle
            << ", spread: " << spread
            << ", stop count: " << gradientStops.size()
            << "]";

        QConicalGradient conicalGradient(center, startAngle);
        conicalGradient.setSpread(spread);

        // Adapt stops to actual span since Qt always assumes end angle of 360
        // Note: This does not give accurate results for the colors outside the angle span.
        // To do this correctly, we would have to insert stops at 0°, 360° and if the spread
        // is reflect/repeat, also throughout the uncovered area to get the correct
        // rendering. It might however be easier to support this in QConicalGradient itself.
        // For now, this is left only semi-supported, as sweep gradients are currently rare.
        const qreal multiplier = qFuzzyCompare(endAngle, startAngle)
                                     ? 1.0
                                     : (endAngle - startAngle) / 360.0;

        QGradientStops adaptedStops;
        adaptedStops.reserve(gradientStops.size());

        for (const QGradientStop &gradientStop : gradientStops)
            adaptedStops.append({gradientStop.first * multiplier, gradientStop.second});

        conicalGradient.setStops(adaptedStops);
        conicalGradient.setCoordinateMode(QGradient::LogicalMode);

        m_painter->setBrush(conicalGradient);
    }
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 261, as _ZN23QColrPaintGraphRenderer18setCompositionModeEN8QPainter15CompositionModeE
inline void QColrPaintGraphRenderer::setCompositionMode(QPainter::CompositionMode mode)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[set composition mode: " << mode << "]";

    if (m_painter != nullptr)
        m_painter->setCompositionMode(mode);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 227, as _ZN23QColrPaintGraphRenderer15drawCurrentPathEv
inline void QColrPaintGraphRenderer::drawCurrentPath()
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
            << "[draw path " << m_currentPath.controlPointRect() << m_currentTransform
        << "]";

    if (m_painter != nullptr)
        m_painter->drawPath(m_currentPath);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 248, as _ZN23QColrPaintGraphRenderer9drawImageERK6QImage
inline void QColrPaintGraphRenderer::drawImage(const QImage &image)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[draw image: " << image.size() << "]";

    if (m_painter != nullptr) {
        m_painter->setWorldMatrixEnabled(false);
        m_painter->drawImage(QPoint(0, 0), image);
        m_painter->setWorldMatrixEnabled(true);
    }
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 43, as _ZN23QColrPaintGraphRenderer7setClipE5QRect
inline void QColrPaintGraphRenderer::setClip(QRect rect)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[set clip: " << rect
        << "]";
    if (!isRendering())
        m_boundingRect = m_boundingRect.united(rect);
    if (m_painter != nullptr)
        m_painter->setClipRect(rect);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 238, as _ZN23QColrPaintGraphRenderer25beginCalculateBoundingBoxEv
inline void QColrPaintGraphRenderer::beginCalculateBoundingBox()
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[begin calculate bounding box]";

    Q_ASSERT(m_painter == nullptr);
    m_boundingRect = QRect{};
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 271, as _ZN23QColrPaintGraphRenderer11beginRenderEdRK10QTransform
inline void QColrPaintGraphRenderer::beginRender(qreal pixelSizeScale, const QTransform &transform)
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[begin render scale: " << pixelSizeScale
        << ", transform: " << transform
        << "]";

    if (m_boundingRect.isEmpty())
        return;

    QRect alignedRect(m_boundingRect.toAlignedRect());

    m_image = QImage(alignedRect.size(), QImage::Format_ARGB32_Premultiplied);
    m_image.fill(Qt::transparent);

    Q_ASSERT(m_painter == nullptr);
    m_painter = new QPainter;
    m_painter->begin(&m_image);
    m_painter->setRenderHint(QPainter::Antialiasing);
    m_painter->setPen(Qt::NoPen);
    m_painter->setBrush(Qt::NoBrush);

    m_painter->translate(-alignedRect.topLeft());

    // Scale from normalized coordinates
    m_painter->scale(pixelSizeScale, pixelSizeScale);
    m_painter->setWorldTransform(transform, true);
}

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 301, as _ZN23QColrPaintGraphRenderer9endRenderEv
inline QImage QColrPaintGraphRenderer::endRender()
{
    qCDebug(lcColrv1).noquote().nospace()
        << QByteArray().fill(' ', m_oldPaths.size() * 2)
        << "[end image size: " << m_image.size()
        << "]";

    Q_ASSERT(m_painter != nullptr);
    m_painter->end();
    delete m_painter;
    m_painter = nullptr;

    return m_image;
}
//  -----------------------------------------------------------------------

//  QColrPaintGraphRenderer::~QColrPaintGraphRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRendererD1Ev(QColrPaintGraphRenderer *self) {
  delete self;
}

//  void QColrPaintGraphRenderer::setBoundingRect(QRectF boundingRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer15setBoundingRectE6QRectF(
    QColrPaintGraphRenderer *self,
    const QRectF *boundingRect) {
  self->setBoundingRect(*boundingRect);
}

//  QRectF QColrPaintGraphRenderer::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QColrPaintGraphRenderer12boundingRectEv(
    const QColrPaintGraphRenderer *self) {
  return new QRectF(self->boundingRect());
}

//  QTransform QColrPaintGraphRenderer::currentTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK23QColrPaintGraphRenderer16currentTransformEv(
    const QColrPaintGraphRenderer *self) {
  return new QTransform(self->currentTransform());
}

//  QPainterPath QColrPaintGraphRenderer::currentPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QColrPaintGraphRenderer11currentPathEv(
    const QColrPaintGraphRenderer *self) {
  return new QPainterPath(self->currentPath());
}

//  void QColrPaintGraphRenderer::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer4saveEv(
    QColrPaintGraphRenderer *self) {
  self->save();
}

//  void QColrPaintGraphRenderer::restore()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer7restoreEv(
    QColrPaintGraphRenderer *self) {
  self->restore();
}

//  void QColrPaintGraphRenderer::appendPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer10appendPathERK12QPainterPath(
    QColrPaintGraphRenderer *self,
    const QPainterPath *path) {
  self->appendPath(*path);
}

//  void QColrPaintGraphRenderer::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer7setPathERK12QPainterPath(
    QColrPaintGraphRenderer *self,
    const QPainterPath *path) {
  self->setPath(*path);
}

//  void QColrPaintGraphRenderer::prependTransform(const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer16prependTransformERK10QTransform(
    QColrPaintGraphRenderer *self,
    const QTransform *transform) {
  self->prependTransform(*transform);
}

//  void QColrPaintGraphRenderer::setSolidColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer13setSolidColorE6QColor(
    QColrPaintGraphRenderer *self,
    const QColor *color) {
  self->setSolidColor(*color);
}

//  void QColrPaintGraphRenderer::setRadialGradient(QPointF c0, qreal r0,
//      QPointF c1, qreal r1, QGradient::Spread spread, const QGradientStops
//      &gradientStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer17setRadialGradientE7QPointFdS0_dN9QGradient6SpreadERK5QListISt4pairId6QColorEE(
    QColrPaintGraphRenderer *self,
    const QPointF *c0,
    qreal r0,
    const QPointF *c1,
    qreal r1,
    QGradient::Spread spread,
    const QGradientStops *gradientStops) {
  self->setRadialGradient(*c0, r0, *c1, r1, spread, *gradientStops);
}

//  void QColrPaintGraphRenderer::setLinearGradient(QPointF p0, QPointF p1,
//      QPointF p2, QGradient::Spread spread, const QGradientStops
//      &gradientStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer17setLinearGradientE7QPointFS0_S0_N9QGradient6SpreadERK5QListISt4pairId6QColorEE(
    QColrPaintGraphRenderer *self,
    const QPointF *p0,
    const QPointF *p1,
    const QPointF *p2,
    QGradient::Spread spread,
    const QGradientStops *gradientStops) {
  self->setLinearGradient(*p0, *p1, *p2, spread, *gradientStops);
}

//  void QColrPaintGraphRenderer::setConicalGradient(QPointF center, qreal
//      startAngle, qreal endAngle, QGradient::Spread spread, const
//      QGradientStops &gradientStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer18setConicalGradientE7QPointFddN9QGradient6SpreadERK5QListISt4pairId6QColorEE(
    QColrPaintGraphRenderer *self,
    const QPointF *center,
    qreal startAngle,
    qreal endAngle,
    QGradient::Spread spread,
    const QGradientStops *gradientStops) {
  self->setConicalGradient(
      *center,
      startAngle,
      endAngle,
      spread,
      *gradientStops);
}

//  void
//      QColrPaintGraphRenderer::setCompositionMode(QPainter::CompositionMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer18setCompositionModeEN8QPainter15CompositionModeE(
    QColrPaintGraphRenderer *self,
    QPainter::CompositionMode mode) {
  self->setCompositionMode(mode);
}

//  void QColrPaintGraphRenderer::drawCurrentPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer15drawCurrentPathEv(
    QColrPaintGraphRenderer *self) {
  self->drawCurrentPath();
}

//  void QColrPaintGraphRenderer::drawImage(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer9drawImageERK6QImage(
    QColrPaintGraphRenderer *self,
    const QImage *image) {
  self->drawImage(*image);
}

//  void QColrPaintGraphRenderer::setClip(QRect rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer7setClipE5QRect(
    QColrPaintGraphRenderer *self,
    const QRect *rect) {
  self->setClip(*rect);
}

//  void QColrPaintGraphRenderer::beginCalculateBoundingBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer25beginCalculateBoundingBoxEv(
    QColrPaintGraphRenderer *self) {
  self->beginCalculateBoundingBox();
}

//  void QColrPaintGraphRenderer::beginRender(qreal pixelSizeScale, const
//      QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer11beginRenderEdRK10QTransform(
    QColrPaintGraphRenderer *self,
    qreal pixelSizeScale,
    const QTransform *transform) {
  self->beginRender(pixelSizeScale, *transform);
}

//  QImage QColrPaintGraphRenderer::endRender()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN23QColrPaintGraphRenderer9endRenderEv(
    QColrPaintGraphRenderer *self) {
  return new QImage(self->endRender());
}

//  bool QColrPaintGraphRenderer::isRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QColrPaintGraphRenderer11isRenderingEv(
    const QColrPaintGraphRenderer *self) {
  return self->isRendering();
}
