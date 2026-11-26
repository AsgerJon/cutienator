//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainterpath.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainterpath.h>
#include <QtGui/qpen.h>
#include <QtCore/QList>

//  QPainterPathStrokerPrivate *QPainterPathStroker::d_func()
extern "C" Q_DECL_EXPORT
QPainterPathStrokerPrivate *ritual_ZN19QPainterPathStroker6d_funcEv(
    QPainterPathStroker *self) {
  return self->d_func();
}

//  const QPainterPathStrokerPrivate *QPainterPathStroker::d_func() const
extern "C" Q_DECL_EXPORT
const QPainterPathStrokerPrivate *ritual_ZNK19QPainterPathStroker6d_funcEv(
    const QPainterPathStroker *self) {
  return self->d_func();
}

//  QPainterPathStroker::QPainterPathStroker()
extern "C" Q_DECL_EXPORT
QPainterPathStroker *ritual_ZN19QPainterPathStrokerC1Ev() {
  return new QPainterPathStroker();
}

//  QPainterPathStroker::QPainterPathStroker(const QPen &pen)
extern "C" Q_DECL_EXPORT
QPainterPathStroker *ritual_ZN19QPainterPathStrokerC1ERK4QPen(
    const QPen *pen) {
  return new QPainterPathStroker(*pen);
}

//  QPainterPathStroker::~QPainterPathStroker()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStrokerD1Ev(QPainterPathStroker *self) {
  delete self;
}

//  void QPainterPathStroker::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker8setWidthEd(
    QPainterPathStroker *self,
    qreal width) {
  self->setWidth(width);
}

//  qreal QPainterPathStroker::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QPainterPathStroker5widthEv(
    const QPainterPathStroker *self) {
  return self->width();
}

//  void QPainterPathStroker::setCapStyle(Qt::PenCapStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker11setCapStyleEN2Qt11PenCapStyleE(
    QPainterPathStroker *self,
    Qt::PenCapStyle style) {
  self->setCapStyle(style);
}

//  Qt::PenCapStyle QPainterPathStroker::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK19QPainterPathStroker8capStyleEv(
    const QPainterPathStroker *self) {
  return self->capStyle();
}

//  void QPainterPathStroker::setJoinStyle(Qt::PenJoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker12setJoinStyleEN2Qt12PenJoinStyleE(
    QPainterPathStroker *self,
    Qt::PenJoinStyle style) {
  self->setJoinStyle(style);
}

//  Qt::PenJoinStyle QPainterPathStroker::joinStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZNK19QPainterPathStroker9joinStyleEv(
    const QPainterPathStroker *self) {
  return self->joinStyle();
}

//  void QPainterPathStroker::setMiterLimit(qreal length)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker13setMiterLimitEd(
    QPainterPathStroker *self,
    qreal length) {
  self->setMiterLimit(length);
}

//  qreal QPainterPathStroker::miterLimit() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QPainterPathStroker10miterLimitEv(
    const QPainterPathStroker *self) {
  return self->miterLimit();
}

//  void QPainterPathStroker::setCurveThreshold(qreal threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker17setCurveThresholdEd(
    QPainterPathStroker *self,
    qreal threshold) {
  self->setCurveThreshold(threshold);
}

//  qreal QPainterPathStroker::curveThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QPainterPathStroker14curveThresholdEv(
    const QPainterPathStroker *self) {
  return self->curveThreshold();
}

//  void QPainterPathStroker::setDashPattern(Qt::PenStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker14setDashPatternEN2Qt8PenStyleE(
    QPainterPathStroker *self,
    Qt::PenStyle a0) {
  self->setDashPattern(a0);
}

//  void QPainterPathStroker::setDashPattern(const QList<qreal> &dashPattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker14setDashPatternERK5QListIdE(
    QPainterPathStroker *self,
    const QList<qreal> *dashPattern) {
  self->setDashPattern(*dashPattern);
}

//  QList<qreal> QPainterPathStroker::dashPattern() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK19QPainterPathStroker11dashPatternEv(
    const QPainterPathStroker *self) {
  return new QList<qreal>(self->dashPattern());
}

//  void QPainterPathStroker::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathStroker13setDashOffsetEd(
    QPainterPathStroker *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  qreal QPainterPathStroker::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QPainterPathStroker10dashOffsetEv(
    const QPainterPathStroker *self) {
  return self->dashOffset();
}

//  QPainterPath QPainterPathStroker::createStroke(const QPainterPath &path)
//      const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QPainterPathStroker12createStrokeERK12QPainterPath(
    const QPainterPathStroker *self,
    const QPainterPath *path) {
  return new QPainterPath(self->createStroke(*path));
}

//  a QList<qreal> a ritual of QPainterPathStroker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPainterPathStroker__QList_qreal(QList<qreal> *self) {
  delete self;
}
