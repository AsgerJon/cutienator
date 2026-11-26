//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QStrokerOps that Python can take functions over in. Every QStrokerOps
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStrokerOpsCall0)(const void *, void *, int *);
typedef void (*CuteQStrokerOpsCall1)(const void *, int *);
typedef void (*CuteQStrokerOpsCall2)(const void *, int *);
class CuteQStrokerOps : public QStrokerOps {
public:
  using QStrokerOps::QStrokerOps;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QStrokerOps5beginEPv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps3endEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps21processCurrentSubpathEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QStrokerOps::begin(void *customData)
  void begin(void *customData) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStrokerOpsCall0 call = reinterpret_cast<CuteQStrokerOpsCall0>(taken[0]);
      call(this, customData, &handled);
      if (handled) return;
    }
    QStrokerOps::begin(customData);
  }

  //  void QStrokerOps::end()
  void end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQStrokerOpsCall1 call = reinterpret_cast<CuteQStrokerOpsCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QStrokerOps::end();
  }

  //  void QStrokerOps::processCurrentSubpath()
  void processCurrentSubpath() override {
    if (taken[2]) {
      int handled = 0;
      CuteQStrokerOpsCall2 call = reinterpret_cast<CuteQStrokerOpsCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QStrokerOps::QStrokerOps()
extern "C" Q_DECL_EXPORT
QStrokerOps *ritual_ZN11QStrokerOpsC1Ev() {
  return new CuteQStrokerOps();
}

//  QStrokerOps::~QStrokerOps()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOpsD1Ev(QStrokerOps *self) {
  delete self;
}

//  void QStrokerOps::setMoveToHook(qStrokerMoveToHook moveToHook)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps13setMoveToHookEPFvddPvE(
    QStrokerOps *self,
    void *moveToHook) {
  self->setMoveToHook(reinterpret_cast<qStrokerMoveToHook>(moveToHook));
}

//  void QStrokerOps::setLineToHook(qStrokerLineToHook lineToHook)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps13setLineToHookEPFvddPvE(
    QStrokerOps *self,
    void *lineToHook) {
  self->setLineToHook(reinterpret_cast<qStrokerLineToHook>(lineToHook));
}

//  void QStrokerOps::setCubicToHook(qStrokerCubicToHook cubicToHook)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps14setCubicToHookEPFvddddddPvE(
    QStrokerOps *self,
    void *cubicToHook) {
  self->setCubicToHook(reinterpret_cast<qStrokerCubicToHook>(cubicToHook));
}

//  void QStrokerOps::begin(void *customData)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps5beginEPv(QStrokerOps *self, void *customData) {
  self->begin(customData);
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

//  void QStrokerOps::strokePath(const QPainterPath &path, void *data, const
//      QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps10strokePathERK12QPainterPathPvRK10QTransform(
    QStrokerOps *self,
    const QPainterPath *path,
    void *data,
    const QTransform *matrix) {
  self->strokePath(*path, data, *matrix);
}

//  void QStrokerOps::strokePolygon(const QPointF *points, int pointCount,
//      bool implicit_close, void *data, const QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps13strokePolygonEPK7QPointFibPvRK10QTransform(
    QStrokerOps *self,
    const QPointF *points,
    int pointCount,
    bool implicit_close,
    void *data,
    const QTransform *matrix) {
  self->strokePolygon(points, pointCount, implicit_close, data, *matrix);
}

//  void QStrokerOps::strokeEllipse(const QRectF &ellipse, void *data, const
//      QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps13strokeEllipseERK6QRectFPvRK10QTransform(
    QStrokerOps *self,
    const QRectF *ellipse,
    void *data,
    const QTransform *matrix) {
  self->strokeEllipse(*ellipse, data, *matrix);
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

//  void QStrokerOps::begin(void *customData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QStrokerOps5beginEPv(
    QStrokerOps *self,
    void *customData) {
  self->QStrokerOps::begin(customData);
}

//  void QStrokerOps::end()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QStrokerOps3endEv(QStrokerOps *self) {
  self->QStrokerOps::end();
}
