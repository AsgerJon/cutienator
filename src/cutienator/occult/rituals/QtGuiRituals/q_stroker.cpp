//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qline.h>
#include <cstring>

//  Only a class built on QStroker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStroker : QStroker {
  using QStroker::processCurrentSubpath;
};

//  A QStroker that Python can take functions over in. Every QStroker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStrokerCall0)(const void *, int *);
typedef void (*CuteQStrokerCall1)(const void *, void *, int *);
typedef void (*CuteQStrokerCall2)(const void *, int *);
class CuteQStroker : public QStroker {
public:
  using QStroker::QStroker;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QStrokerOps21processCurrentSubpathEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps5beginEPv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps3endEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QStroker::processCurrentSubpath()
  void processCurrentSubpath() override {
    if (taken[0]) {
      int handled = 0;
      CuteQStrokerCall0 call = reinterpret_cast<CuteQStrokerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QStroker::processCurrentSubpath();
  }

  //  void QStrokerOps::begin(void *customData)
  void begin(void *customData) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStrokerCall1 call = reinterpret_cast<CuteQStrokerCall1>(taken[1]);
      call(this, customData, &handled);
      if (handled) return;
    }
    QStrokerOps::begin(customData);
  }

  //  void QStrokerOps::end()
  void end() override {
    if (taken[2]) {
      int handled = 0;
      CuteQStrokerCall2 call = reinterpret_cast<CuteQStrokerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QStrokerOps::end();
  }
};

//  QStroker::QStroker()
extern "C" Q_DECL_EXPORT
QStroker *ritual_ZN8QStrokerC1Ev() {
  return new CuteQStroker();
}

//  QStroker::~QStroker()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStrokerD1Ev(QStroker *self) {
  delete self;
}

//  void QStroker::setStrokeWidth(qfixed width)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker14setStrokeWidthEd(QStroker *self, qfixed width) {
  self->setStrokeWidth(width);
}

//  qfixed QStroker::strokeWidth() const
extern "C" Q_DECL_EXPORT
qfixed ritual_ZNK8QStroker11strokeWidthEv(const QStroker *self) {
  return self->strokeWidth();
}

//  void QStroker::setCapStyle(Qt::PenCapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker11setCapStyleEN2Qt11PenCapStyleE(
    QStroker *self,
    Qt::PenCapStyle capStyle) {
  self->setCapStyle(capStyle);
}

//  Qt::PenCapStyle QStroker::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK8QStroker8capStyleEv(const QStroker *self) {
  return self->capStyle();
}

//  LineJoinMode QStroker::capStyleMode() const
extern "C" Q_DECL_EXPORT
QStroker::LineJoinMode ritual_ZNK8QStroker12capStyleModeEv(
    const QStroker *self) {
  return self->capStyleMode();
}

//  void QStroker::setJoinStyle(Qt::PenJoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker12setJoinStyleEN2Qt12PenJoinStyleE(
    QStroker *self,
    Qt::PenJoinStyle style) {
  self->setJoinStyle(style);
}

//  Qt::PenJoinStyle QStroker::joinStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZNK8QStroker9joinStyleEv(const QStroker *self) {
  return self->joinStyle();
}

//  LineJoinMode QStroker::joinStyleMode() const
extern "C" Q_DECL_EXPORT
QStroker::LineJoinMode ritual_ZNK8QStroker13joinStyleModeEv(
    const QStroker *self) {
  return self->joinStyleMode();
}

//  void QStroker::setMiterLimit(qfixed length)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker13setMiterLimitEd(QStroker *self, qfixed length) {
  self->setMiterLimit(length);
}

//  qfixed QStroker::miterLimit() const
extern "C" Q_DECL_EXPORT
qfixed ritual_ZNK8QStroker10miterLimitEv(const QStroker *self) {
  return self->miterLimit();
}

//  void QStroker::setForceOpen(bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker12setForceOpenEb(QStroker *self, bool state) {
  self->setForceOpen(state);
}

//  bool QStroker::forceOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QStroker9forceOpenEv(const QStroker *self) {
  return self->forceOpen();
}

//  void QStroker::joinPoints(qfixed x, qfixed y, const QLineF &nextLine,
//      LineJoinMode join)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker10joinPointsEddRK6QLineFNS_12LineJoinModeE(
    QStroker *self,
    qfixed x,
    qfixed y,
    const QLineF *nextLine,
    QStroker::LineJoinMode join) {
  self->joinPoints(x, y, *nextLine, join);
}

//  void QStroker::emitMoveTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker10emitMoveToEdd(QStroker *self, qfixed x, qfixed y) {
  self->emitMoveTo(x, y);
}

//  void QStroker::emitLineTo(qfixed x, qfixed y)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker10emitLineToEdd(QStroker *self, qfixed x, qfixed y) {
  self->emitLineTo(x, y);
}

//  void QStroker::emitCubicTo(qfixed c1x, qfixed c1y, qfixed c2x, qfixed
//      c2y, qfixed ex, qfixed ey)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker11emitCubicToEdddddd(
    QStroker *self,
    qfixed c1x,
    qfixed c1y,
    qfixed c2x,
    qfixed c2y,
    qfixed ex,
    qfixed ey) {
  self->emitCubicTo(c1x, c1y, c2x, c2y, ex, ey);
}

//  Qt::PenCapStyle QStroker::capForJoinMode(LineJoinMode mode)
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZN8QStroker14capForJoinModeENS_12LineJoinModeE(
    QStroker::LineJoinMode mode) {
  return QStroker::capForJoinMode(mode);
}

//  LineJoinMode QStroker::joinModeForCap(Qt::PenCapStyle a0)
extern "C" Q_DECL_EXPORT
QStroker::LineJoinMode ritual_ZN8QStroker14joinModeForCapEN2Qt11PenCapStyleE(
    Qt::PenCapStyle a0) {
  return QStroker::joinModeForCap(a0);
}

//  Qt::PenJoinStyle QStroker::joinForJoinMode(LineJoinMode mode)
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZN8QStroker15joinForJoinModeENS_12LineJoinModeE(
    QStroker::LineJoinMode mode) {
  return QStroker::joinForJoinMode(mode);
}

//  LineJoinMode QStroker::joinModeForJoin(Qt::PenJoinStyle joinStyle)
extern "C" Q_DECL_EXPORT
QStroker::LineJoinMode ritual_ZN8QStroker15joinModeForJoinEN2Qt12PenJoinStyleE(
    Qt::PenJoinStyle joinStyle) {
  return QStroker::joinModeForJoin(joinStyle);
}

//  void QStroker::processCurrentSubpath()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QStroker21processCurrentSubpathEv(QStroker *self) {
  self->processCurrentSubpath();
}

//  a Python function taken by a CuteQStroker, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStroker(QStroker *self, const char *key, void *call) {
  return static_cast<CuteQStroker *>(self)->take(key, call);
}

//  void QStroker::processCurrentSubpath()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QStroker21processCurrentSubpathEv(QStroker *self) {
  static_cast<OwnQStroker *>(self)->OwnQStroker::processCurrentSubpath();
}
