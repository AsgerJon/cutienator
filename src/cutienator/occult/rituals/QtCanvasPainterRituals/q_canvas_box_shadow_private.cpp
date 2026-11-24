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
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcanvasboxshadow.h"
#include "qcanvasboxshadow_p.h"
#include "qcanvaspainter_p.h"
#include <QVariant>
#include <QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 570, as _ZN23QCanvasBoxShadowPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
{
    return new QCanvasBoxShadowPrivate(*this);
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
//  -----------------------------------------------------------------------

//  A QCanvasBoxShadowPrivate that Python can take functions over in. Every QCanvasBoxShadowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasBoxShadowPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasBoxShadowPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasBoxShadowPrivate : public QCanvasBoxShadowPrivate {
public:
  using QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate;
  CuteQCanvasBoxShadowPrivate(const QCanvasBoxShadowPrivate &other) : QCanvasBoxShadowPrivate(other) {}
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
