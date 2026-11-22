//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimeline.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtimeline.h>
#include <QtCore/qstring.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTimeLine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTimeLine : QTimeLine {
  using QTimeLine::timerEvent;
};

//  A QTimeLine that Python can take functions over in. Every QTimeLine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQTimeLineCall0)(const void *, int, int *);
typedef void (*CuteQTimeLineCall1)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQTimeLineCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQTimeLineCall3)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTimeLineCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQTimeLineCall5)(const void *, QEvent *, int *);
typedef void (*CuteQTimeLineCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTimeLineCall7)(const void *, const QMetaMethod *, int *);
class CuteQTimeLine : public QTimeLine {
public:
  using QTimeLine::QTimeLine;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QTimeLine12valueForTimeEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  qreal QTimeLine::valueForTime(int msec) const
  qreal valueForTime(int msec) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTimeLineCall0 call = reinterpret_cast<CuteQTimeLineCall0>(taken[0]);
      qreal given = call(this, msec, &handled);
      if (handled) return given;
    }
    return QTimeLine::valueForTime(msec);
  }

  //  void QTimeLine::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTimeLineCall1 call = reinterpret_cast<CuteQTimeLineCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTimeLine::timerEvent(event);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTimeLineCall2 call = reinterpret_cast<CuteQTimeLineCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTimeLineCall3 call = reinterpret_cast<CuteQTimeLineCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTimeLineCall4 call = reinterpret_cast<CuteQTimeLineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTimeLineCall5 call = reinterpret_cast<CuteQTimeLineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTimeLineCall6 call = reinterpret_cast<CuteQTimeLineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTimeLineCall7 call = reinterpret_cast<CuteQTimeLineCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

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
  return new CuteQTimeLine(duration, parent);
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

//  a Python function taken by a CuteQTimeLine, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTimeLine(QTimeLine *self, const char *key, void *call) {
  return static_cast<CuteQTimeLine *>(self)->take(key, call);
}

//  qreal QTimeLine::valueForTime(int msec) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK9QTimeLine12valueForTimeEi(
    const QTimeLine *self,
    int msec) {
  return self->QTimeLine::valueForTime(msec);
}

//  void QTimeLine::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTimeLine10timerEventEP11QTimerEvent(
    QTimeLine *self,
    QTimerEvent *event) {
  static_cast<OwnQTimeLine *>(self)->OwnQTimeLine::timerEvent(event);
}
