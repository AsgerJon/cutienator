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
#include <QtCanvasPainter/qcanvasradialgradient.h>
#include <QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 66, as local:qcanvasgradient.cpp:QCPAINTER_GRADIENT_SIZE
#define QCPAINTER_GRADIENT_SIZE 256

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasradialgradient.cpp, line 47, as local:qcanvasradialgradient.cpp:DECONST
#define DECONST(d) const_cast<QCanvasRadialGradientBrushPrivate *>(d)

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

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasradialgradient.cpp, line 289, as _ZNK33QCanvasRadialGradientBrushPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasRadialGradientBrushPrivate::createPaint(QCanvasPainter *painter) const
{
    auto *d = this;
    if (d->dirty) {
        if (d->gradientStops.size() == 0) {
            QColor icol = { 0, 0, 0, 0 };
            QColor ocol = { 0, 0, 0, 0 };
            // Note: Without stops, custom image might be used.
            createRadialGradient(icol, ocol, d->imageId);
        } else if (d->gradientStops.size() == 1) {
            QColor c = d->gradientStops.first().color;
            createRadialGradient(c, c, 0);
        } else if (d->gradientStops.size() == 2) {
            QColor ic = d->gradientStops.first().color;
            QColor oc = d->gradientStops.last().color;
            createRadialGradient(ic, oc, 0);
        } else {
            DECONST(d)->updateGradientTexture(painter);
            QColor col = { 255, 255, 255, 255 };
            createRadialGradient(col, col, d->textureId);
        }
        DECONST(d)->dirty = {};
    }
    if (d->paint.imageId > 0) {
        auto *painterPriv = QCanvasPainterPrivate::get(painter);
        painterPriv->markTextureIdUsed(d->paint.imageId);
    }
    return d->paint;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasradialgradient.cpp, line 319, as _ZNK33QCanvasRadialGradientBrushPrivate20createRadialGradientE6QColorS0_i
inline void QCanvasRadialGradientBrushPrivate::createRadialGradient(QColor iColor, QColor oColor,
                                               int imageId) const
{
    auto *d = this;
    const auto dd = d->data.radial;
    QCPaint &p = DECONST(d)->paint;
    p.transform = QTransform::fromTranslate(dd.ocx, dd.ocy);

    if (!qFuzzyCompare(dd.icx, dd.ocx) || !qFuzzyCompare(dd.icy, dd.ocy)) {
        // Inner and outer points are not the same, so use more complex
        // extended type.
        p.brushType = BrushRadialGradientExtended;
        // extent used for inner center position.
        p.extent[0] = float(dd.icx);
        p.extent[1] = float(dd.icy);
        p.radius = float(dd.iRadius);
        // feather used for outer radius.
        p.feather = float(dd.oRadius);
    } else {
        p.brushType = BrushRadialGradient;
        constexpr qreal small = 0.0001;
        const qreal r = (dd.iRadius + dd.oRadius) * 0.5;
        const qreal f = (dd.oRadius - dd.iRadius);
        p.radius = float(r);
        p.feather = float(qMax(small, f));
    }

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

//  A QCanvasRadialGradientBrushPrivate that Python can take functions over in. Every QCanvasRadialGradientBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QCPaint * (*CuteQCanvasRadialGradientBrushPrivateCall0)(const void *, QCanvasPainter *, int *);
typedef void * (*CuteQCanvasRadialGradientBrushPrivateCall1)(const void *, int *);
class CuteQCanvasRadialGradientBrushPrivate : public QCanvasRadialGradientBrushPrivate {
public:
  using QCanvasRadialGradientBrushPrivate::QCanvasRadialGradientBrushPrivate;
  CuteQCanvasRadialGradientBrushPrivate(const QCanvasRadialGradientBrushPrivate & other) : QCanvasRadialGradientBrushPrivate(other) {}
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

  //  QCPaint QCanvasRadialGradientBrushPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasRadialGradientBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasRadialGradientBrushPrivateCall0>(taken[0]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasRadialGradientBrushPrivate::createPaint(painter);
  }

  //  QCanvasBrushPrivate *QCanvasRadialGradientBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasRadialGradientBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasRadialGradientBrushPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasRadialGradientBrushPrivate::clone();
  }
};

//  QCPaint QCanvasRadialGradientBrushPrivate::createPaint(QCanvasPainter
//      *painter) const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK33QCanvasRadialGradientBrushPrivate11createPaintEP14QCanvasPainter(
    const QCanvasRadialGradientBrushPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  void QCanvasRadialGradientBrushPrivate::createRadialGradient(QColor
//      iColor, QColor oColor, int imageId) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK33QCanvasRadialGradientBrushPrivate20createRadialGradientE6QColorS0_i(
    const QCanvasRadialGradientBrushPrivate *self,
    const QColor *iColor,
    const QColor *oColor,
    int imageId) {
  self->createRadialGradient(*iColor, *oColor, imageId);
}

//  QCanvasBrushPrivate *QCanvasRadialGradientBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN33QCanvasRadialGradientBrushPrivate5cloneEv(
    QCanvasRadialGradientBrushPrivate *self) {
  return self->clone();
}

//  QCanvasRadialGradientBrushPrivate::~QCanvasRadialGradientBrushPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QCanvasRadialGradientBrushPrivateD1Ev(
    QCanvasRadialGradientBrushPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasRadialGradientBrushPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasRadialGradientBrushPrivate(
    QCanvasRadialGradientBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasRadialGradientBrushPrivate *>(self)->take(key, call);
}
