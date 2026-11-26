//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtCore/QSpan>
#include <QtGui/QPaintEngine>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <memory>
#include <QtCore/qdebug.h>
#include <QtCore/qmath.h>
#include <QtCore/qmutex.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintdevice.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qpainter.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpicture.h>
#include <QtGui/qpixmapcache.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qthread.h>
#include <QtCore/qvarlengtharray.h>
#include <QtGui/qstatictext.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qpaintengine_p.h>
#include <QtGui/private/qemulationpaintengine_p.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/private/qpaintengine_raster_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtGui/private/qglyphrun_p.h>
#include <QtGui/private/qhexstring_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtCore/private/qtclasshelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/painting/qpainter.cpp, line 54, as local:qpainter.cpp:QGradient_StretchToDevice
#define QGradient_StretchToDevice 0x10000000

//  from src/gui/painting/qpainter.cpp, line 55, as local:qpainter.cpp:QPaintEngine_OpaqueBackground
#define QPaintEngine_OpaqueBackground 0x40000000

//  from src/gui/painting/qpainter.cpp, line 83, as local:qpainter.cpp:coordinateMode
static inline QGradient::CoordinateMode coordinateMode(const QBrush &brush)
{
    switch (brush.style()) {
    case Qt::LinearGradientPattern:
    case Qt::RadialGradientPattern:
    case Qt::ConicalGradientPattern:
        return brush.gradient()->coordinateMode();
    default:
        ;
    }
    return QGradient::LogicalMode;
}

//  from src/gui/painting/qpainter.cpp, line 157, as local:qpainter.cpp:needsEmulation
static bool needsEmulation(const QBrush &brush)
{
    bool res = false;

    const QGradient *bg = brush.gradient();
    if (bg) {
        res = (bg->coordinateMode() > QGradient::LogicalMode);
    } else if (brush.style() == Qt::TexturePattern) {
        if (qHasPixmapTexture(brush))
            res = !qFuzzyCompare(brush.texture().devicePixelRatio(), qreal(1.0));
        else
            res = !qFuzzyCompare(brush.textureImage().devicePixelRatio(), qreal(1.0));
    }

    return res;
}

//  from src/gui/painting/qpainter.cpp, line 494, as local:qpainter.cpp:stretchGradientToUserSpace
static inline QBrush stretchGradientToUserSpace(const QBrush &brush, const QRectF &boundingRect)
{
    Q_ASSERT(brush.style() >= Qt::LinearGradientPattern
             && brush.style() <= Qt::ConicalGradientPattern);

    QTransform gradientToUser(boundingRect.width(), 0, 0, boundingRect.height(),
                              boundingRect.x(), boundingRect.y());

    QGradient g = *brush.gradient();
    g.setCoordinateMode(QGradient::LogicalMode);

    QBrush b(g);
    if (brush.gradient()->coordinateMode() == QGradient::ObjectMode)
        b.setTransform(b.transform() * gradientToUser);
    else
        b.setTransform(gradientToUser * b.transform());
    return b;
}

//  from src/gui/painting/qpainter.cpp, line 6023, as local:qpainter.cpp:generateWavyPixmap
static QPixmap generateWavyPixmap(qreal maxRadius, const QPen &pen)
{
    const qreal radiusBase = qMax(qreal(1), maxRadius);

    QString key = "WaveUnderline-"_L1
                  % pen.color().name()
                  % HexString<qreal>(radiusBase)
                  % HexString<qreal>(pen.widthF());

    QPixmap pixmap;
    if (QPixmapCache::find(key, &pixmap))
        return pixmap;

    const qreal halfPeriod = qMax(qreal(2), qreal(radiusBase * 1.61803399)); // the golden ratio
    const int width = qCeil(100 / (2 * halfPeriod)) * (2 * halfPeriod);
    const qreal radius = qFloor(radiusBase * 2) / 2.;

    QPainterPath path;

    qreal xs = 0;
    qreal ys = radius;

    while (xs < width) {
        xs += halfPeriod;
        ys = -ys;
        path.quadTo(xs - halfPeriod / 2, ys, xs, 0);
    }

    pixmap = QPixmap(width, radius * 2);
    pixmap.fill(Qt::transparent);
    {
        QPen wavePen = pen;
        wavePen.setCapStyle(Qt::SquareCap);

        // This is to protect against making the line too fat, as happens on OS X
        // due to it having a rather thick width for the regular underline.
        const qreal maxPenWidth = .8 * radius;
        if (wavePen.widthF() > maxPenWidth)
            wavePen.setWidthF(maxPenWidth);

        QPainter imgPainter(&pixmap);
        imgPainter.setPen(wavePen);
        imgPainter.setRenderHint(QPainter::Antialiasing);
        imgPainter.translate(0, radius);
        imgPainter.drawPath(path);
    }

    QPixmapCache::insert(key, pixmap);

    return pixmap;
}

//  from src/gui/painting/qpainter.cpp, line 6075, as local:qpainter.cpp:drawTextItemDecoration
static void drawTextItemDecoration(QPainter *painter, const QPointF &pos, const QFontEngine *fe, QTextEngine *textEngine,
                                   QTextCharFormat::UnderlineStyle underlineStyle,
                                   QTextItem::RenderFlags flags, qreal width,
                                   const QTextCharFormat &charFormat)
{
    if (underlineStyle == QTextCharFormat::NoUnderline
        && !(flags & (QTextItem::StrikeOut | QTextItem::Overline)))
        return;

    const QPen oldPen = painter->pen();
    const QBrush oldBrush = painter->brush();
    painter->setBrush(Qt::NoBrush);
    QPen pen = oldPen;
    pen.setStyle(Qt::SolidLine);
    pen.setWidthF(fe->lineThickness().toReal());
    pen.setCapStyle(Qt::FlatCap);

    QLineF line(qFloor(pos.x()), pos.y(), qFloor(pos.x() + width), pos.y());

    const qreal underlineOffset = fe->underlinePosition().toReal();

    if (underlineStyle == QTextCharFormat::SpellCheckUnderline) {
        QPlatformTheme *theme = QGuiApplicationPrivate::platformTheme();
        if (theme)
            underlineStyle = QTextCharFormat::UnderlineStyle(theme->themeHint(QPlatformTheme::SpellCheckUnderlineStyle).toInt());
        if (underlineStyle == QTextCharFormat::SpellCheckUnderline) // still not resolved
            underlineStyle = QTextCharFormat::WaveUnderline;
    }

    if (underlineStyle == QTextCharFormat::WaveUnderline) {
        painter->save();
        painter->translate(0, pos.y() + 1);
        qreal maxHeight = fe->descent().toReal() - qreal(1);

        QColor uc = charFormat.underlineColor();
        if (uc.isValid())
            pen.setColor(uc);

        // Adapt wave to underlineOffset or pen width, whatever is larger, to make it work on all platforms
        const QPixmap wave = generateWavyPixmap(qMin(qMax(underlineOffset, pen.widthF()), maxHeight / qreal(2.)), pen);
        const int descent = qFloor(maxHeight);

        painter->setBrushOrigin(painter->brushOrigin().x(), 0);
        painter->fillRect(pos.x(), 0, qCeil(width), qMin(wave.height(), descent), wave);
        painter->restore();
    } else if (underlineStyle != QTextCharFormat::NoUnderline) {
        const bool isAntialiasing = painter->renderHints().testFlag(QPainter::Antialiasing);
        if (!isAntialiasing)
            pen.setWidthF(qMax(fe->lineThickness().round(), QFixed(1)).toReal());
        const qreal lineThicknessOffset = pen.widthF() / 2.0;

        // Deliberately ceil the offset to avoid the underline coming too close to
        // the text above it, but limit it to stay within descent.
        qreal adjustedUnderlineOffset = std::ceil(underlineOffset) + lineThicknessOffset;
        if (underlineOffset <= fe->descent().toReal())
            adjustedUnderlineOffset = qMin(adjustedUnderlineOffset, fe->descent().toReal() - lineThicknessOffset);
        const qreal underlinePos = pos.y() + adjustedUnderlineOffset;
        QColor uc = charFormat.underlineColor();
        if (uc.isValid())
            pen.setColor(uc);

        pen.setStyle((Qt::PenStyle)(underlineStyle));
        painter->setPen(pen);
        QLineF underline(line.x1(), underlinePos, line.x2(), underlinePos);
        if (textEngine)
            textEngine->addUnderline(painter, underline);
        else
            painter->drawLine(underline);

        if (!isAntialiasing)
            pen.setWidthF(fe->lineThickness().toReal());
    }

    pen.setStyle(Qt::SolidLine);
    pen.setColor(oldPen.color());

    if (flags & QTextItem::StrikeOut) {
        QLineF strikeOutLine = line;
        strikeOutLine.translate(0., - fe->ascent().toReal() / 3.);
        QColor uc = charFormat.underlineColor();
        if (uc.isValid())
            pen.setColor(uc);
        painter->setPen(pen);
        if (textEngine)
            textEngine->addStrikeOut(painter, strikeOutLine);
        else
            painter->drawLine(strikeOutLine);
    }

    if (flags & QTextItem::Overline) {
        QLineF overline = line;
        overline.translate(0., - fe->ascent().toReal());
        QColor uc = charFormat.underlineColor();
        if (uc.isValid())
            pen.setColor(uc);
        painter->setPen(pen);
        if (textEngine)
            textEngine->addOverline(painter, overline);
        else
            painter->drawLine(overline);
    }

    painter->setPen(oldPen);
    painter->setBrush(oldBrush);
}

//  from src/gui/painting/qpainter.cpp, line 6181, as local:qpainter.cpp:qt_draw_decoration_for_glyphs
static void qt_draw_decoration_for_glyphs(QPainter *painter,
                                          const QPointF &decorationPosition,
                                          const glyph_t *glyphArray,
                                          const QFixedPoint *positions,
                                          int glyphCount,
                                          QFontEngine *fontEngine,
                                          bool underline,
                                          bool overline,
                                          bool strikeOut)
{
    if (!underline && !overline && !strikeOut)
        return;

    QTextItem::RenderFlags flags;
    if (underline)
        flags |= QTextItem::Underline;
    if (overline)
        flags |= QTextItem::Overline;
    if (strikeOut)
        flags |= QTextItem::StrikeOut;

    bool rtl = positions[glyphCount - 1].x < positions[0].x;
    QFixed baseline = positions[0].y;
    glyph_metrics_t gm = fontEngine->boundingBox(glyphArray[rtl ? 0 : glyphCount - 1]);

    qreal width = rtl
            ? (positions[0].x + gm.xoff - positions[glyphCount - 1].x).toReal()
            : (positions[glyphCount - 1].x + gm.xoff - positions[0].x).toReal();

    drawTextItemDecoration(painter,
                           QPointF(decorationPosition.x(), baseline.toReal()),
                           fontEngine,
                           nullptr, // textEngine
                           underline ? QTextCharFormat::SingleUnderline
                                     : QTextCharFormat::NoUnderline,
                           flags,
                           width,
                           QTextCharFormat());
}

//  from src/gui/painting/qpainter.cpp, line 202, as _ZN15QPainterPrivateC1EP8QPainter
inline QPainterPrivate::QPainterPrivate(QPainter *painter)
    : q_ptr(painter), txinv(0), inDestructor(false)
{
}

//  from src/gui/painting/qpainter.cpp, line 207, as _ZN15QPainterPrivateD1Ev
inline QPainterPrivate::~QPainterPrivate()
    = default;

//  from src/gui/painting/qpainter.cpp, line 475, as _ZN15QPainterPrivate20drawOpaqueBackgroundERK12QPainterPathNS_13DrawOperationE
inline void QPainterPrivate::drawOpaqueBackground(const QPainterPath &path, DrawOperation op)
{
    Q_Q(QPainter);

    q->setBackgroundMode(Qt::TransparentMode);

    if (op & FillDraw && state->brush.style() != Qt::NoBrush) {
        q->fillPath(path, state->bgBrush.color());
        q->fillPath(path, state->brush);
    }

    if (op & StrokeDraw && state->pen.style() != Qt::NoPen) {
        q->strokePath(path, QPen(state->bgBrush.color(), state->pen.width()));
        q->strokePath(path, state->pen);
    }

    q->setBackgroundMode(Qt::OpaqueMode);
}

//  from src/gui/painting/qpainter.cpp, line 628, as _ZN15QPainterPrivate12updateMatrixEv
inline void QPainterPrivate::updateMatrix()
{
    state->matrix = state->WxF ? state->worldMatrix : QTransform();
    if (state->VxF)
        state->matrix *= viewTransform();

    txinv = false;                                // no inverted matrix
    state->matrix *= state->redirectionMatrix;
    if (extended)
        extended->transformChanged();
    else
        state->dirtyFlags |= QPaintEngine::DirtyTransform;

    state->matrix *= hidpiScaleTransform();

//     printf("VxF=%d, WxF=%d\n", state->VxF, state->WxF);
//     qDebug() << " --- using matrix" << state->matrix << redirection_offset;
}

//  from src/gui/painting/qpainter.cpp, line 648, as _ZN15QPainterPrivate15updateInvMatrixEv
inline void QPainterPrivate::updateInvMatrix()
{
    Q_ASSERT(txinv == false);
    txinv = true;                                // creating inverted matrix
    invMatrix = state->matrix.inverted();
}

//  from src/gui/painting/qpainter.cpp, line 210, as _ZNK15QPainterPrivate13viewTransformEv
inline QTransform QPainterPrivate::viewTransform() const
{
    if (state->VxF) {
        qreal scaleW = qreal(state->vw)/qreal(state->ww);
        qreal scaleH = qreal(state->vh)/qreal(state->wh);
        return QTransform(scaleW, 0, 0, scaleH,
                          state->vx - state->wx*scaleW, state->vy - state->wy*scaleH);
    }
    return QTransform();
}

//  from src/gui/painting/qpainter.cpp, line 221, as _ZNK15QPainterPrivate25effectiveDevicePixelRatioEv
inline qreal QPainterPrivate::effectiveDevicePixelRatio() const
{
    // Special cases for devices that does not support PdmDevicePixelRatio go here:
    if (device->devType() == QInternal::Printer)
        return qreal(1);

    return device->devicePixelRatio();
}

//  from src/gui/painting/qpainter.cpp, line 230, as _ZNK15QPainterPrivate19hidpiScaleTransformEv
inline QTransform QPainterPrivate::hidpiScaleTransform() const
{
    const qreal devicePixelRatio = effectiveDevicePixelRatio();
    return QTransform::fromScale(devicePixelRatio, devicePixelRatio);
}

//  from src/gui/painting/qpainter.cpp, line 240, as _ZN15QPainterPrivate20attachPainterPrivateEP8QPainterP12QPaintDevice
inline bool QPainterPrivate::attachPainterPrivate(QPainter *q, QPaintDevice *pdev)
{
    Q_ASSERT(q);
    Q_ASSERT(pdev);

    QPainter *sp = pdev->sharedPainter();
    if (!sp)
        return false;

    // Save the current state of the shared painter and assign
    // the current d_ptr to the shared painter's d_ptr.
    sp->save();
    ++sp->d_ptr->refcount;
    sp->d_ptr->d_ptrs.push_back(std::move(q->d_ptr));
    q->d_ptr.reset(sp->d_ptr.get());

    Q_ASSERT(q->d_ptr->state);

    // Now initialize the painter with correct widget properties.
    q->d_ptr->initFrom(pdev);
    QPoint offset;
    pdev->redirected(&offset);
    offset += q->d_ptr->engine->coordinateOffset();

    // Update system rect.
    q->d_ptr->state->ww = q->d_ptr->state->vw = pdev->width();
    q->d_ptr->state->wh = q->d_ptr->state->vh = pdev->height();

    // Update matrix.
    if (q->d_ptr->state->WxF) {
        q->d_ptr->state->redirectionMatrix = q->d_ptr->state->matrix;
        q->d_ptr->state->redirectionMatrix *= q->d_ptr->hidpiScaleTransform().inverted();
        q->d_ptr->state->redirectionMatrix.translate(-offset.x(), -offset.y());
        q->d_ptr->state->worldMatrix = QTransform();
        q->d_ptr->state->WxF = false;
    } else {
        q->d_ptr->state->redirectionMatrix = QTransform::fromTranslate(-offset.x(), -offset.y());
    }
    q->d_ptr->updateMatrix();

    QPaintEnginePrivate *enginePrivate = q->d_ptr->engine->d_func();
    if (enginePrivate->currentClipDevice == pdev) {
        enginePrivate->systemStateChanged();
        return true;
    }

    // Update system transform and clip.
    enginePrivate->currentClipDevice = pdev;
    enginePrivate->setSystemTransform(q->d_ptr->state->matrix);
    return true;
}

//  from src/gui/painting/qpainter.cpp, line 292, as _ZN15QPainterPrivate20detachPainterPrivateEP8QPainter
inline void QPainterPrivate::detachPainterPrivate(QPainter *q)
{
    Q_ASSERT(refcount > 1);
    Q_ASSERT(q);

    --refcount;
    auto original = std::move(d_ptrs.back());
    d_ptrs.pop_back();
    if (inDestructor) {
        inDestructor = false;
        if (original)
            original->inDestructor = true;
    } else if (!original) {
        original = std::make_unique<QPainterPrivate>(q);
    }

    q->restore();
    Q_UNUSED(q->d_ptr.release());
    q->d_ptr = std::move(original);

    if (emulationEngine) {
        extended = emulationEngine->real_engine;
        emulationEngine = nullptr;
    }
}

//  from src/gui/painting/qpainter.cpp, line 1535, as _ZN15QPainterPrivate8initFromEPK12QPaintDevice
inline void QPainterPrivate::initFrom(const QPaintDevice *device)
{
    if (!engine) {
        qWarning("QPainter::initFrom: Painter not active, aborted");
        return;
    }

    Q_Q(QPainter);
    device->initPainter(q);
}
//  -----------------------------------------------------------------------

//  QPainter *QPainterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN15QPainterPrivate6q_funcEv(QPainterPrivate *self) {
  return self->q_func();
}

//  const QPainter *QPainterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPainter *ritual_ZNK15QPainterPrivate6q_funcEv(
    const QPainterPrivate *self) {
  return self->q_func();
}

//  QPainterPrivate::QPainterPrivate(QPainter *painter)
extern "C" Q_DECL_EXPORT
QPainterPrivate *ritual_ZN15QPainterPrivateC1EP8QPainter(QPainter *painter) {
  return new QPainterPrivate(painter);
}

//  QPainterPrivate::~QPainterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivateD1Ev(QPainterPrivate *self) {
  delete self;
}

//  QPainterDummyState *QPainterPrivate::fakeState() const
extern "C" Q_DECL_EXPORT
QPainterDummyState *ritual_ZNK15QPainterPrivate9fakeStateEv(
    const QPainterPrivate *self) {
  return self->fakeState();
}

//  void QPainterPrivate::drawOpaqueBackground(const QPainterPath &path,
//      DrawOperation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate20drawOpaqueBackgroundERK12QPainterPathNS_13DrawOperationE(
    QPainterPrivate *self,
    const QPainterPath *path,
    QPainterPrivate::DrawOperation operation) {
  self->drawOpaqueBackground(*path, operation);
}

//  void QPainterPrivate::updateMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate12updateMatrixEv(QPainterPrivate *self) {
  self->updateMatrix();
}

//  void QPainterPrivate::updateInvMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate15updateInvMatrixEv(QPainterPrivate *self) {
  self->updateInvMatrix();
}

//  QPainterPrivate *QPainterPrivate::get(QPainter *painter)
extern "C" Q_DECL_EXPORT
QPainterPrivate *ritual_ZN15QPainterPrivate3getEP8QPainter(
    QPainter *painter) {
  return QPainterPrivate::get(painter);
}

//  QTransform QPainterPrivate::viewTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QPainterPrivate13viewTransformEv(
    const QPainterPrivate *self) {
  return new QTransform(self->viewTransform());
}

//  qreal QPainterPrivate::effectiveDevicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPainterPrivate25effectiveDevicePixelRatioEv(
    const QPainterPrivate *self) {
  return self->effectiveDevicePixelRatio();
}

//  QTransform QPainterPrivate::hidpiScaleTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QPainterPrivate19hidpiScaleTransformEv(
    const QPainterPrivate *self) {
  return new QTransform(self->hidpiScaleTransform());
}

//  bool QPainterPrivate::attachPainterPrivate(QPainter *q, QPaintDevice
//      *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPainterPrivate20attachPainterPrivateEP8QPainterP12QPaintDevice(
    QPainter *q,
    QPaintDevice *pdev) {
  return QPainterPrivate::attachPainterPrivate(q, pdev);
}

//  void QPainterPrivate::detachPainterPrivate(QPainter *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate20detachPainterPrivateEP8QPainter(
    QPainterPrivate *self,
    QPainter *q) {
  self->detachPainterPrivate(q);
}

//  void QPainterPrivate::initFrom(const QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate8initFromEPK12QPaintDevice(
    QPainterPrivate *self,
    const QPaintDevice *device) {
  self->initFrom(device);
}

//  void QPainterPrivate::setEngineDirtyFlags(QSpan<const
//      QPaintEngine::DirtyFlags> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate19setEngineDirtyFlagsE5QSpanIK6QFlagsIN12QPaintEngine9DirtyFlagEELm18446744073709551615EE(
    QPainterPrivate *self,
    const QSpan<const QPaintEngine::DirtyFlags> *a0) {
  self->setEngineDirtyFlags(*a0);
}
