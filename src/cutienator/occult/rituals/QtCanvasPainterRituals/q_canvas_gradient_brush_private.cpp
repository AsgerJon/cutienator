//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 4. Kept as it is when the generator runs again.
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

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 66, as local:qcanvasgradient.cpp:QCPAINTER_GRADIENT_SIZE
#define QCPAINTER_GRADIENT_SIZE 256

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 559, as local:qcanvasgradient.cpp:toInt64
static constexpr qint64 toInt64(quint64 value) noexcept
{
    constexpr qint64 QINT64_MAX = std::numeric_limits<qint64>::max();
    if (value <= quint64(QINT64_MAX))
        return qint64(value);
    else
        return -qint64(~value) - 1;
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

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgradient.cpp, line 570, as _ZNK27QCanvasGradientBrushPrivate19generateGradientKeyEv
inline qint64 QCanvasGradientBrushPrivate::generateGradientKey() const
{
    quint64 id = 0;
    for (const auto &v : std::as_const(gradientStops)) {
        id += qHash(int(v.position * QCPAINTER_GRADIENT_SIZE))
              ^ qHash(v.color.rgba());
    }
    return toInt64(id);
}
//  -----------------------------------------------------------------------

//  A QCanvasGradientBrushPrivate that Python can take functions over in. Every QCanvasGradientBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasGradientBrushPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasGradientBrushPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasGradientBrushPrivate : public QCanvasGradientBrushPrivate {
public:
  using QCanvasGradientBrushPrivate::QCanvasGradientBrushPrivate;
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

  //  QCanvasBrushPrivate *QCanvasBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasGradientBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasGradientBrushPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return {};
  }

  //  QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter *painter)
  //      const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasGradientBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasGradientBrushPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  bool QCanvasGradientBrushPrivate::equals(const QCanvasBrushPrivate
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QCanvasGradientBrushPrivate6equalsERK19QCanvasBrushPrivate(
    const QCanvasGradientBrushPrivate *self,
    const QCanvasBrushPrivate *other) {
  return self->equals(*other);
}

//  qint64 QCanvasGradientBrushPrivate::generateGradientKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK27QCanvasGradientBrushPrivate19generateGradientKeyEv(
    const QCanvasGradientBrushPrivate *self) {
  return self->generateGradientKey();
}

//  const QCanvasGradientBrushPrivate *QCanvasGradientBrushPrivate::get(const
//      QCanvasGradient &gradient)
extern "C" Q_DECL_EXPORT
const QCanvasGradientBrushPrivate *ritual_ZN27QCanvasGradientBrushPrivate3getERK15QCanvasGradient(
    const QCanvasGradient *gradient) {
  return QCanvasGradientBrushPrivate::get(*gradient);
}

//  QCanvasGradientBrushPrivate
//      *QCanvasGradientBrushPrivate::get(QCanvasGradient &gradient)
extern "C" Q_DECL_EXPORT
QCanvasGradientBrushPrivate *ritual_ZN27QCanvasGradientBrushPrivate3getER15QCanvasGradient(
    QCanvasGradient *gradient) {
  return QCanvasGradientBrushPrivate::get(*gradient);
}

//  a Python function taken by a CuteQCanvasGradientBrushPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasGradientBrushPrivate(
    QCanvasGradientBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasGradientBrushPrivate *>(self)->take(key, call);
}

//  QCanvasLinearGradient
//      QCanvasGradientBrushPrivate::create<QCanvasLinearGradient>(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient * ritual_ZN27QCanvasGradientBrushPrivate6createI21QCanvasLinearGradientEET_RK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasLinearGradient(QCanvasGradientBrushPrivate::create<QCanvasLinearGradient>(*brush));
}

//  QCanvasRadialGradient
//      QCanvasGradientBrushPrivate::create<QCanvasRadialGradient>(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient * ritual_ZN27QCanvasGradientBrushPrivate6createI21QCanvasRadialGradientEET_RK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasRadialGradient(QCanvasGradientBrushPrivate::create<QCanvasRadialGradient>(*brush));
}

//  QCanvasConicalGradient
//      QCanvasGradientBrushPrivate::create<QCanvasConicalGradient>(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient * ritual_ZN27QCanvasGradientBrushPrivate6createI22QCanvasConicalGradientEET_RK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasConicalGradient(QCanvasGradientBrushPrivate::create<QCanvasConicalGradient>(*brush));
}

//  QCanvasBoxGradient
//      QCanvasGradientBrushPrivate::create<QCanvasBoxGradient>(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient * ritual_ZN27QCanvasGradientBrushPrivate6createI18QCanvasBoxGradientEET_RK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasBoxGradient(QCanvasGradientBrushPrivate::create<QCanvasBoxGradient>(*brush));
}
