//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasboxshadow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasboxshadow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCanvasPainter/private/qcanvasboxshadow_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCore/QVariant>
#include <QtGui/QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 14, as local:qcanvasboxshadow.cpp:QCPAINTER_BOX_SHADOW_MULTIPLIER
static constexpr qreal QCPAINTER_BOX_SHADOW_MULTIPLIER = 1.0;

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 570, as _ZN23QCanvasBoxShadowPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
{
    return new QCanvasBoxShadowPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 489, as _ZNK23QCanvasBoxShadowPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter *painter) const
{
    Q_UNUSED(painter);
    auto *d = this;
    if (d->changed) {
        // TODO: Support non-antialiased shadows?
        const qreal aa = 1.0;

        // Adjust blur to grow equally towards in & out.
        const qreal blurIn = QCPAINTER_BOX_SHADOW_MULTIPLIER * d->blur + 0.5 * aa;
        const qreal blurOut = 2 * QCPAINTER_BOX_SHADOW_MULTIPLIER * d->blur + aa;

        qreal extendX = d->spread - blurIn;
        qreal extendY = d->spread - blurIn;

        // Limit max extends when width & height are < 0.
        // This reduces rendering issues of thin rects with big blur
        // values being to sharp at center (smoothstep is clipped),
        // but causes some extra blurriness to those.
        if (extendX <  -0.5 * d->width) {
            const qreal diff = extendX + 0.5 * d->width;
            extendX -= 0.25 * diff;
        }
        if (extendY <  -0.5 * d->height) {
            const qreal diff = extendY + 0.5 * d->height;
            extendY -= 0.25 * diff;
        }

        const qreal x = d->x - extendX;
        const qreal y = d->y - extendY;
        const qreal width = d->width + 2 * extendX;
        const qreal height = d->height + 2 * extendY;

        QColor color = d->clampedColor();

        // Use adjusted width & height extended with blur & spread.
        // QVector4D is float-based, so the corner radii are truncated here.
        const float commonRadius = float(d->clampedRadius(d->radius, width, height));
        QVector4D radius { commonRadius, commonRadius, commonRadius, commonRadius };

        if (d->topLeftRadius >= 0)
            radius.setX(float(d->clampedRadius(d->topLeftRadius, width, height)));
        if (d->topRightRadius >= 0)
            radius.setY(float(d->clampedRadius(d->topRightRadius, width, height)));
        if (d->bottomLeftRadius >= 0)
            radius.setZ(float(d->clampedRadius(d->bottomLeftRadius, width, height)));
        if (d->bottomRightRadius >= 0)
            radius.setW(float(d->clampedRadius(d->bottomRightRadius, width, height)));

        createBoxShadow(x, y, width, height, radius, blurOut, color);

        const_cast<QCanvasBoxShadowPrivate *>(d)->changed = false;
    }

    return d->paint;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 137, as _ZNK23QCanvasBoxShadowPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasBoxShadowPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasBoxShadowPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || radius != pd.radius
        || blur != pd.blur
        || spread != pd.spread
        || color != pd.color
        || topLeftRadius != pd.topLeftRadius
        || topRightRadius != pd.topRightRadius
        || bottomLeftRadius != pd.bottomLeftRadius
        || bottomRightRadius != pd.bottomRightRadius)
        return false;

    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 546, as _ZNK23QCanvasBoxShadowPrivate15createBoxShadowEddddRK9QVector4Dd6QColor
inline void QCanvasBoxShadowPrivate::createBoxShadow(qreal x, qreal y, qreal width, qreal height,
                                  const QVector4D &radius,
                                  qreal blur, QColor color) const
{
    // QCPaint is the engine-side representation, so the values are
    // truncated to float here.
    QCPaint &p = const_cast<QCanvasBoxShadowPrivate *>(this)->paint;
    p.brushType = BrushBoxShadow;

    p.transform = QTransform::fromTranslate(x + (width * 0.5), y + (height * 0.5));

    p.extent[0] = float(width * 0.5);
    p.extent[1] = float(height * 0.5);

    // Unused, individual corner radius in outerColor
    //p.radius = radius;

    p.feather = float(blur);

    p.innerColor = { color.redF(), color.greenF(), color.blueF(), color.alphaF() };
    p.outerColor = { radius.x(), radius.y(), radius.z(), radius.w() };
    p.imageId = 0;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 575, as _ZNK23QCanvasBoxShadowPrivate13clampedRadiusEddd
inline qreal QCanvasBoxShadowPrivate::clampedRadius(qreal rad, qreal width, qreal height) const
{
    const qreal maxRadius = qMin(width, height) * 0.5;
    qreal spreadRadius = rad + spread;
    if (radius < spread && !qFuzzyIsNull(spread)) {
        // CSS box-shadow has a specific math to calculate radius with spread
        // https://www.w3.org/TR/css-backgrounds-3/#shadow-shape
        // "the spread distance is first multiplied by the proportion 1 + (r-1)^3,
        // where r is the ratio of the border radius to the spread distance".
        const qreal r = (rad / spread) - 1;
        spreadRadius = rad + spread * (1 + r * r * r);
    }
    spreadRadius = qMax(0.0, spreadRadius);
    return qMin(spreadRadius, maxRadius);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 593, as _ZNK23QCanvasBoxShadowPrivate12clampedColorEv
inline QColor QCanvasBoxShadowPrivate::clampedColor() const
{
    QColor c = color;
    const qreal minSize = qMin(width + 2 * spread, height + 2 * spread);
    const qreal blurTreshold = minSize * 0.5 * QCPAINTER_BOX_SHADOW_MULTIPLIER;
    if (blur > blurTreshold) {
        const qreal fade = blurTreshold / blur;
        c.setAlphaF(color.alphaF() * fade);
    }
    return c;
}
//  -----------------------------------------------------------------------

//  A QCanvasBoxShadowPrivate that Python can take functions over in. Every QCanvasBoxShadowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasBoxShadowPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasBoxShadowPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasBoxShadowPrivate : public QCanvasBoxShadowPrivate {
public:
  using QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate;
  CuteQCanvasBoxShadowPrivate(const QCanvasBoxShadowPrivate & other) : QCanvasBoxShadowPrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QCanvasBrushPrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasBoxShadowPrivateCall0 call = reinterpret_cast<CuteQCanvasBoxShadowPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasBoxShadowPrivate::clone();
  }

  //  QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter *painter)
  //      const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasBoxShadowPrivateCall1 call = reinterpret_cast<CuteQCanvasBoxShadowPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasBoxShadowPrivate::createPaint(painter);
  }
};

//  QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN23QCanvasBoxShadowPrivate5cloneEv(
    QCanvasBoxShadowPrivate *self) {
  return self->clone();
}

//  bool QCanvasBoxShadowPrivate::equals(const QCanvasBrushPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QCanvasBoxShadowPrivate6equalsERK19QCanvasBrushPrivate(
    const QCanvasBoxShadowPrivate *self,
    const QCanvasBrushPrivate *other) {
  return self->equals(*other);
}

//  QCanvasBoxShadowPrivate *QCanvasBoxShadowPrivate::get(QCanvasBoxShadow
//      *brush)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadowPrivate *ritual_ZN23QCanvasBoxShadowPrivate3getEP16QCanvasBoxShadow(
    QCanvasBoxShadow *brush) {
  return QCanvasBoxShadowPrivate::get(brush);
}

//  const QCanvasBoxShadowPrivate *QCanvasBoxShadowPrivate::get(const
//      QCanvasBoxShadow *brush)
extern "C" Q_DECL_EXPORT
const QCanvasBoxShadowPrivate *ritual_ZN23QCanvasBoxShadowPrivate3getEPK16QCanvasBoxShadow(
    const QCanvasBoxShadow *brush) {
  return QCanvasBoxShadowPrivate::get(brush);
}

//  QCanvasBoxShadow QCanvasBoxShadowPrivate::create(QCanvasBoxShadowPrivate
//      *p)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN23QCanvasBoxShadowPrivate6createEPS_(
    QCanvasBoxShadowPrivate *p) {
  return new QCanvasBoxShadow(QCanvasBoxShadowPrivate::create(p));
}

//  QCanvasBoxShadow QCanvasBoxShadowPrivate::getFromCanvasBrush(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN23QCanvasBoxShadowPrivate18getFromCanvasBrushERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasBoxShadow(
      QCanvasBoxShadowPrivate::getFromCanvasBrush(
          *brush));
}

//  QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK23QCanvasBoxShadowPrivate11createPaintEP14QCanvasPainter(
    const QCanvasBoxShadowPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  void QCanvasBoxShadowPrivate::createBoxShadow(qreal x, qreal y, qreal
//      width, qreal height, const QVector4D &radius, qreal blur, QColor
//      color) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QCanvasBoxShadowPrivate15createBoxShadowEddddRK9QVector4Dd6QColor(
    const QCanvasBoxShadowPrivate *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    const QVector4D *radius,
    qreal blur,
    const QColor *color) {
  self->createBoxShadow(x, y, width, height, *radius, blur, *color);
}

//  qreal QCanvasBoxShadowPrivate::clampedRadius(qreal radius, qreal width,
//      qreal height) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QCanvasBoxShadowPrivate13clampedRadiusEddd(
    const QCanvasBoxShadowPrivate *self,
    qreal radius,
    qreal width,
    qreal height) {
  return self->clampedRadius(radius, width, height);
}

//  QColor QCanvasBoxShadowPrivate::clampedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QCanvasBoxShadowPrivate12clampedColorEv(
    const QCanvasBoxShadowPrivate *self) {
  return new QColor(self->clampedColor());
}

//  QCanvasBoxShadowPrivate::~QCanvasBoxShadowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanvasBoxShadowPrivateD1Ev(QCanvasBoxShadowPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasBoxShadowPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasBoxShadowPrivate(
    QCanvasBoxShadowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasBoxShadowPrivate *>(self)->take(key, call);
}

//  QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_own_ZN23QCanvasBoxShadowPrivate5cloneEv(
    QCanvasBoxShadowPrivate *self) {
  return self->QCanvasBoxShadowPrivate::clone();
}

//  QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_own_ZNK23QCanvasBoxShadowPrivate11createPaintEP14QCanvasPainter(
    const QCanvasBoxShadowPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->QCanvasBoxShadowPrivate::createPaint(painter));
}
