//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  A QCanvasConicalGradientBrushPrivate that Python can take functions over in. Every QCanvasConicalGradientBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QCPaint * (*CuteQCanvasConicalGradientBrushPrivateCall0)(const void *, QCanvasPainter *, int *);
typedef void * (*CuteQCanvasConicalGradientBrushPrivateCall1)(const void *, int *);
class CuteQCanvasConicalGradientBrushPrivate : public QCanvasConicalGradientBrushPrivate {
public:
  using QCanvasConicalGradientBrushPrivate::QCanvasConicalGradientBrushPrivate;
  CuteQCanvasConicalGradientBrushPrivate(const QCanvasConicalGradientBrushPrivate &other) : QCanvasConicalGradientBrushPrivate(other) {}
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

  //  QCPaint
  //      QCanvasConicalGradientBrushPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasConicalGradientBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasConicalGradientBrushPrivateCall0>(taken[0]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasConicalGradientBrushPrivate::createPaint(painter);
  }

  //  QCanvasBrushPrivate *QCanvasConicalGradientBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasConicalGradientBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasConicalGradientBrushPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasConicalGradientBrushPrivate::clone();
  }
};

//  QCanvasBrushPrivate *QCanvasConicalGradientBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN34QCanvasConicalGradientBrushPrivate5cloneEv(
    QCanvasConicalGradientBrushPrivate *self) {
  return self->clone();
}

//  QCanvasConicalGradientBrushPrivate::~QCanvasConicalGradientBrushPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QCanvasConicalGradientBrushPrivateD1Ev(
    QCanvasConicalGradientBrushPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasConicalGradientBrushPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasConicalGradientBrushPrivate(
    QCanvasConicalGradientBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasConicalGradientBrushPrivate *>(self)->take(key, call);
}
