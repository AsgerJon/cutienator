//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimeline.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtimeline.h>
#include <QtCore/qstring.h>
#include <QtCore/qeasingcurve.h>

//  const QMetaObject *QTimeLine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTimeLine10metaObjectEv(
    const QTimeLine *self) {
  return self->metaObject();
}

//  QString QTimeLine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTimeLine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTimeLine::tr(s, c, n));
}

//  QTimeLine::QTimeLine(int duration, QObject *parent)
extern "C" Q_DECL_EXPORT
QTimeLine *ritual_ZN9QTimeLineC1EiP7QObject(int duration, QObject *parent) {
  return new QTimeLine(duration, parent);
}

//  QTimeLine::~QTimeLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLineD1Ev(QTimeLine *self) {
  delete self;
}

//  State QTimeLine::state() const
extern "C" Q_DECL_EXPORT
QTimeLine::State ritual_ZNK9QTimeLine5stateEv(const QTimeLine *self) {
  return self->state();
}

//  int QTimeLine::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine9loopCountEv(const QTimeLine *self) {
  return self->loopCount();
}

//  void QTimeLine::setLoopCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine12setLoopCountEi(QTimeLine *self, int count) {
  self->setLoopCount(count);
}

//  Direction QTimeLine::direction() const
extern "C" Q_DECL_EXPORT
QTimeLine::Direction ritual_ZNK9QTimeLine9directionEv(
    const QTimeLine *self) {
  return self->direction();
}

//  void QTimeLine::setDirection(Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine12setDirectionENS_9DirectionE(
    QTimeLine *self,
    QTimeLine::Direction direction) {
  self->setDirection(direction);
}

//  int QTimeLine::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine8durationEv(const QTimeLine *self) {
  return self->duration();
}

//  void QTimeLine::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine11setDurationEi(QTimeLine *self, int duration) {
  self->setDuration(duration);
}

//  int QTimeLine::startFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine10startFrameEv(const QTimeLine *self) {
  return self->startFrame();
}

//  void QTimeLine::setStartFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine13setStartFrameEi(QTimeLine *self, int frame) {
  self->setStartFrame(frame);
}

//  int QTimeLine::endFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine8endFrameEv(const QTimeLine *self) {
  return self->endFrame();
}

//  void QTimeLine::setEndFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine11setEndFrameEi(QTimeLine *self, int frame) {
  self->setEndFrame(frame);
}

//  void QTimeLine::setFrameRange(int startFrame, int endFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine13setFrameRangeEii(
    QTimeLine *self,
    int startFrame,
    int endFrame) {
  self->setFrameRange(startFrame, endFrame);
}

//  int QTimeLine::updateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine14updateIntervalEv(const QTimeLine *self) {
  return self->updateInterval();
}

//  void QTimeLine::setUpdateInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine17setUpdateIntervalEi(
    QTimeLine *self,
    int interval) {
  self->setUpdateInterval(interval);
}

//  QEasingCurve QTimeLine::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK9QTimeLine11easingCurveEv(const QTimeLine *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QTimeLine::setEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine14setEasingCurveERK12QEasingCurve(
    QTimeLine *self,
    const QEasingCurve *curve) {
  self->setEasingCurve(*curve);
}

//  int QTimeLine::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine11currentTimeEv(const QTimeLine *self) {
  return self->currentTime();
}

//  int QTimeLine::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine12currentFrameEv(const QTimeLine *self) {
  return self->currentFrame();
}

//  qreal QTimeLine::currentValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTimeLine12currentValueEv(const QTimeLine *self) {
  return self->currentValue();
}

//  int QTimeLine::frameForTime(int msec) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine12frameForTimeEi(const QTimeLine *self, int msec) {
  return self->frameForTime(msec);
}

//  qreal QTimeLine::valueForTime(int msec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTimeLine12valueForTimeEi(const QTimeLine *self, int msec) {
  return self->valueForTime(msec);
}

//  void QTimeLine::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine5startEv(QTimeLine *self) {
  self->start();
}

//  void QTimeLine::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine6resumeEv(QTimeLine *self) {
  self->resume();
}

//  void QTimeLine::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine4stopEv(QTimeLine *self) {
  self->stop();
}

//  void QTimeLine::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine9setPausedEb(QTimeLine *self, bool paused) {
  self->setPaused(paused);
}

//  void QTimeLine::setCurrentTime(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine14setCurrentTimeEi(QTimeLine *self, int msec) {
  self->setCurrentTime(msec);
}

//  void QTimeLine::toggleDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine15toggleDirectionEv(QTimeLine *self) {
  self->toggleDirection();
}
