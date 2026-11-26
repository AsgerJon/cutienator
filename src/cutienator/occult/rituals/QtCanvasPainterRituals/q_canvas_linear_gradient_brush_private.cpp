//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasgradient.h>
#include <QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/qcanvaslineargradient.h>
#include <QtCanvasPainter/qcanvasradialgradient.h>
#include <QtCanvasPainter/qcanvasconicalgradient.h>
#include <QtCanvasPainter/qcanvasboxgradient.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCanvasPainter/qcanvaspainter.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <limits>
#include <QtGui/private/qtguiglobal_p.h> // for qpixellayout_p.h's QT_CONFIG(raster_fp) check
#include <QtGui/private/qpixellayout_p.h>
#include <QtCanvasPainter/qcanvaslineargradient.h>
#include <QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 66, as local:qcanvasgradient.cpp:QCPAINTER_GRADIENT_SIZE
#define QCPAINTER_GRADIENT_SIZE 256

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaslineargradient.cpp, line 48, as local:qcanvaslineargradient.cpp:DECONST
#define DECONST(d) const_cast<QCanvasLinearGradientBrushPrivate *>(d)

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 549, as _ZN27QCanvasGradientBrushPrivateC2EN12QCanvasBrush9BrushTypeE
inline QCanvasGradientBrushPrivate::QCanvasGradientBrushPrivate(QCanvasBrush::BrushType type)
    : QCanvasBrushPrivate(type)
    , imageId(0)
    , imageY(0.5)
    , dirty(DirtyFlag::All)
    , textureId(0)
{
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 376, as _ZNK27QCanvasGradientBrushPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasGradientBrushPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasGradientBrushPrivate &>(other);

    if (!qCanvasGradientDataEquals(type, data, pd.data))
        return false;

    return gradientStops == pd.gradientStops
           && imageId == pd.imageId
           && imageY == pd.imageY;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaslineargradient.cpp, line 155, as _ZNK33QCanvasLinearGradientBrushPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasLinearGradientBrushPrivate::createPaint(QCanvasPainter *painter) const
{
    auto *d = this;
    if (d->dirty) {
        if (d->gradientStops.size() == 0) {
            QColor icol = { 0, 0, 0, 0 };
            QColor ocol = { 0, 0, 0, 0 };
            // Note: Without stops, custom image might be used.
            createLinearGradient(icol, ocol, d->imageId);
        } else if (d->gradientStops.size() == 1) {
            QColor c = d->gradientStops.first().color;
            createLinearGradient(c, c, 0);
        } else if (d->gradientStops.size() == 2) {
            QColor ic = d->gradientStops.first().color;
            QColor oc = d->gradientStops.last().color;
            createLinearGradient(ic, oc, 0);
        } else {
            DECONST(d)->updateGradientTexture(painter);
            QColor col = { 255, 255, 255, 255 };
            createLinearGradient(col, col, d->textureId);
        }
        DECONST(d)->dirty = {};
    }
    if (d->paint.imageId > 0) {
        auto *painterPriv = QCanvasPainterPrivate::get(painter);
        painterPriv->markTextureIdUsed(d->paint.imageId);
    }
    return d->paint;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaslineargradient.cpp, line 185, as _ZNK33QCanvasLinearGradientBrushPrivate20createLinearGradientE6QColorS0_i
inline void QCanvasLinearGradientBrushPrivate::createLinearGradient(QColor iColor, QColor oColor,
                                            int imageId) const
{
    auto *d = this;

    const auto dd = d->data.linear;
    QCPaint &p = DECONST(d)->paint;
    p.brushType = BrushLinearGradient;

    qreal dx = dd.ex - dd.sx;
    qreal dy = dd.ey - dd.sy;
    qreal dist = std::sqrt(dx*dx + dy*dy);
    constexpr qreal small = 0.0001;
    if (dist > small) {
        dx /= dist;
        dy /= dist;
    } else {
        dx = 0;
        dy = 1;
    }
    p.transform.setMatrix(dy, -dx, 0,
                          dx, dy, 0,
                          dd.sx, dd.sy, 1);
    p.feather = float(qMax(small, dist));

    // Note: extent and radius not used.

    if (imageId != 0) {
        // Multistop gradient
        p.imageId = imageId;
        p.innerColor.a = float(d->imageY);
    } else {
        // 2 stops gradient
        p.innerColor = { iColor.redF(), iColor.greenF(), iColor.blueF(), iColor.alphaF() };
        p.outerColor = { oColor.redF(), oColor.greenF(), oColor.blueF(), oColor.alphaF() };
        p.imageId = 0;
    }
}
//  -----------------------------------------------------------------------

//  A QCanvasLinearGradientBrushPrivate that Python can take functions over in. Every QCanvasLinearGradientBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QCPaint * (*CuteQCanvasLinearGradientBrushPrivateCall0)(const void *, QCanvasPainter *, int *);
typedef void * (*CuteQCanvasLinearGradientBrushPrivateCall1)(const void *, int *);
class CuteQCanvasLinearGradientBrushPrivate : public QCanvasLinearGradientBrushPrivate {
public:
  using QCanvasLinearGradientBrushPrivate::QCanvasLinearGradientBrushPrivate;
  CuteQCanvasLinearGradientBrushPrivate(const QCanvasLinearGradientBrushPrivate & other) : QCanvasLinearGradientBrushPrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QCanvasBrushPrivate5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QCPaint QCanvasLinearGradientBrushPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasLinearGradientBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasLinearGradientBrushPrivateCall0>(taken[0]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasLinearGradientBrushPrivate::createPaint(painter);
  }

  //  QCanvasBrushPrivate *QCanvasLinearGradientBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasLinearGradientBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasLinearGradientBrushPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasLinearGradientBrushPrivate::clone();
  }
};

//  QCPaint QCanvasLinearGradientBrushPrivate::createPaint(QCanvasPainter
//      *painter) const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK33QCanvasLinearGradientBrushPrivate11createPaintEP14QCanvasPainter(
    const QCanvasLinearGradientBrushPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  void QCanvasLinearGradientBrushPrivate::createLinearGradient(QColor
//      iColor, QColor oColor, int imageId) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK33QCanvasLinearGradientBrushPrivate20createLinearGradientE6QColorS0_i(
    const QCanvasLinearGradientBrushPrivate *self,
    const QColor *iColor,
    const QColor *oColor,
    int imageId) {
  self->createLinearGradient(*iColor, *oColor, imageId);
}

//  QCanvasBrushPrivate *QCanvasLinearGradientBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN33QCanvasLinearGradientBrushPrivate5cloneEv(
    QCanvasLinearGradientBrushPrivate *self) {
  return self->clone();
}

//  QCanvasLinearGradientBrushPrivate::~QCanvasLinearGradientBrushPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QCanvasLinearGradientBrushPrivateD1Ev(
    QCanvasLinearGradientBrushPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasLinearGradientBrushPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasLinearGradientBrushPrivate(
    QCanvasLinearGradientBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasLinearGradientBrushPrivate *>(self)->take(key, call);
}
