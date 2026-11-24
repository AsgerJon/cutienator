//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <cstring>

//  A QStrokerOps that Python can take functions over in. Every QStrokerOps
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStrokerOpsCall0)(const void *, int *);
typedef void (*CuteQStrokerOpsCall1)(const void *, int *);
class CuteQStrokerOps : public QStrokerOps {
public:
  using QStrokerOps::QStrokerOps;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QStrokerOps3endEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps21processCurrentSubpathEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QStrokerOps::end()
  void end() override {
    if (taken[0]) {
      int handled = 0;
      CuteQStrokerOpsCall0 call = reinterpret_cast<CuteQStrokerOpsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QStrokerOps::end();
  }

  //  void QStrokerOps::processCurrentSubpath()
  void processCurrentSubpath() override {
    if (taken[1]) {
      int handled = 0;
      CuteQStrokerOpsCall1 call = reinterpret_cast<CuteQStrokerOpsCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QStrokerOps::~QStrokerOps()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOpsD1Ev(QStrokerOps *self) {
  delete self;
}

//  void QStrokerOps::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps3endEv(QStrokerOps *self) {
  self->end();
}

//  void QStrokerOps::moveTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps6moveToEdd(
    QStrokerOps *self,
    qfixed x,
    qfixed y) {
  self->moveTo(x, y);
}

//  void QStrokerOps::lineTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps6lineToEdd(
    QStrokerOps *self,
    qfixed x,
    qfixed y) {
  self->lineTo(x, y);
}

//  void QStrokerOps::cubicTo(qfixed x1, qfixed y1, qfixed x2, qfixed y2,
//      qfixed ex, qfixed ey)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps7cubicToEdddddd(
    QStrokerOps *self,
    qfixed x1,
    qfixed y1,
    qfixed x2,
    qfixed y2,
    qfixed ex,
    qfixed ey) {
  self->cubicTo(x1, y1, x2, y2, ex, ey);
}

//  QRectF QStrokerOps::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QStrokerOps8clipRectEv(const QStrokerOps *self) {
  return new QRectF(self->clipRect());
}

//  void QStrokerOps::setClipRect(const QRectF &clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps11setClipRectERK6QRectF(
    QStrokerOps *self,
    const QRectF *clip) {
  self->setClipRect(*clip);
}

//  void QStrokerOps::setCurveThresholdFromTransform(const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps30setCurveThresholdFromTransformERK10QTransform(
    QStrokerOps *self,
    const QTransform *transform) {
  self->setCurveThresholdFromTransform(*transform);
}

//  void QStrokerOps::setCurveThreshold(qfixed threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps17setCurveThresholdEd(
    QStrokerOps *self,
    qfixed threshold) {
  self->setCurveThreshold(threshold);
}

//  qfixed QStrokerOps::curveThreshold() const
extern "C" Q_DECL_EXPORT
qfixed ritual_ZNK11QStrokerOps14curveThresholdEv(const QStrokerOps *self) {
  return self->curveThreshold();
}

//  void QStrokerOps::emitMoveTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps10emitMoveToEdd(
    QStrokerOps *self,
    qfixed x,
    qfixed y) {
  self->emitMoveTo(x, y);
}

//  void QStrokerOps::emitLineTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps10emitLineToEdd(
    QStrokerOps *self,
    qfixed x,
    qfixed y) {
  self->emitLineTo(x, y);
}

//  void QStrokerOps::emitCubicTo(qfixed c1x, qfixed c1y, qfixed c2x, qfixed
//      c2y, qfixed ex, qfixed ey)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps11emitCubicToEdddddd(
    QStrokerOps *self,
    qfixed c1x,
    qfixed c1y,
    qfixed c2x,
    qfixed c2y,
    qfixed ex,
    qfixed ey) {
  self->emitCubicTo(c1x, c1y, c2x, c2y, ex, ey);
}

//  void QStrokerOps::processCurrentSubpath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps21processCurrentSubpathEv(QStrokerOps *self) {
  self->processCurrentSubpath();
}

//  a Python function taken by a CuteQStrokerOps, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStrokerOps(
    QStrokerOps *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStrokerOps *>(self)->take(key, call);
}

//  void QStrokerOps::end()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QStrokerOps3endEv(QStrokerOps *self) {
  self->QStrokerOps::end();
}
