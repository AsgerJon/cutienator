//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimeline.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(easingcurve)
#if QT_CONFIG(easingcurve)
#include <QtCore/qtimeline.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/QTimeLine>
#include <QtCore/QEasingCurve>

//  Only a class built on QTimeLine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTimeLine : QTimeLine {
  using QTimeLine::timerEvent;
};

//  A QTimeLine that Python can take functions over in. Every QTimeLine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(easingcurve)
typedef qreal (*CuteQTimeLineCall0)(const void *, int, int *);
#endif  // QT_CONFIG(easingcurve)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(easingcurve)
typedef void (*CuteQTimeLineCall1)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(easingcurve)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTimeLineCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTimeLineCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimeLineCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimeLineCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimeLineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimeLineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTimeLine : public QTimeLine {
public:
  using QTimeLine::QTimeLine;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(easingcurve)
    if (!std::strcmp(key, "_ZNK9QTimeLine12valueForTimeEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(easingcurve)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(easingcurve)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(easingcurve)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(easingcurve)
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
#endif  // QT_CONFIG(easingcurve)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(easingcurve)
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
#endif  // QT_CONFIG(easingcurve)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTimeLine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTimeLine10metaObjectEv(
    const QTimeLine *self) {
  return self->metaObject();
}

//  void *QTimeLine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QTimeLine11qt_metacastEPKc(QTimeLine *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTimeLine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QTimeLine11qt_metacallEN11QMetaObject4CallEiPPv(
    QTimeLine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QBindable<int> QTimeLine::bindableLoopCount()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN9QTimeLine17bindableLoopCountEv(QTimeLine *self) {
  return new QBindable<int>(self->bindableLoopCount());
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

//  QBindable<Direction> QTimeLine::bindableDirection()
extern "C" Q_DECL_EXPORT
QBindable<QTimeLine::Direction> *ritual_ZN9QTimeLine17bindableDirectionEv(
    QTimeLine *self) {
  return new QBindable<QTimeLine::Direction>(self->bindableDirection());
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

//  QBindable<int> QTimeLine::bindableDuration()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN9QTimeLine16bindableDurationEv(QTimeLine *self) {
  return new QBindable<int>(self->bindableDuration());
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

//  QBindable<int> QTimeLine::bindableUpdateInterval()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN9QTimeLine22bindableUpdateIntervalEv(
    QTimeLine *self) {
  return new QBindable<int>(self->bindableUpdateInterval());
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

//  QBindable<QEasingCurve> QTimeLine::bindableEasingCurve()
extern "C" Q_DECL_EXPORT
QBindable<QEasingCurve> *ritual_ZN9QTimeLine19bindableEasingCurveEv(
    QTimeLine *self) {
  return new QBindable<QEasingCurve>(self->bindableEasingCurve());
}

//  int QTimeLine::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeLine11currentTimeEv(const QTimeLine *self) {
  return self->currentTime();
}

//  QBindable<int> QTimeLine::bindableCurrentTime()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN9QTimeLine19bindableCurrentTimeEv(QTimeLine *self) {
  return new QBindable<int>(self->bindableCurrentTime());
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

//  void QTimeLine::valueChanged(qreal x, QPrivateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine12valueChangedEdNS_14QPrivateSignalE(
    QTimeLine *self,
    qreal x) {
  self->valueChanged(x, QTimeLine::QPrivateSignal());
}

//  void QTimeLine::frameChanged(int a0, QPrivateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine12frameChangedEiNS_14QPrivateSignalE(
    QTimeLine *self,
    int a0) {
  self->frameChanged(a0, QTimeLine::QPrivateSignal());
}

//  void QTimeLine::stateChanged(QTimeLine::State newState, QPrivateSignal
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine12stateChangedENS_5StateENS_14QPrivateSignalE(
    QTimeLine *self,
    QTimeLine::State newState) {
  self->stateChanged(newState, QTimeLine::QPrivateSignal());
}

//  void QTimeLine::finished(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine8finishedENS_14QPrivateSignalE(QTimeLine *self) {
  self->finished(QTimeLine::QPrivateSignal());
}

//  void QTimeLine::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeLine10timerEventEP11QTimerEvent(
    QTimeLine *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QTimeLinePrivate *QTimeLine::d_func()
extern "C" Q_DECL_EXPORT
QTimeLinePrivate *ritual_ZN9QTimeLine6d_funcEv(QTimeLine *self) {
  return self->d_func();
}

//  const QTimeLinePrivate *QTimeLine::d_func() const
extern "C" Q_DECL_EXPORT
const QTimeLinePrivate *ritual_ZNK9QTimeLine6d_funcEv(
    const QTimeLine *self) {
  return self->d_func();
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

//  a QBindable<int> a ritual of QTimeLine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimeLine__QBindable_int(QBindable<int> *self) {
  delete self;
}

//  a QBindable<QTimeLine::Direction> a ritual of QTimeLine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimeLine__QBindable_QTimeLine_Direction(
    QBindable<QTimeLine::Direction> *self) {
  delete self;
}

//  a QBindable<QEasingCurve> a ritual of QTimeLine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimeLine__QBindable_QEasingCurve(
    QBindable<QEasingCurve> *self) {
  delete self;
}

#endif  // QT_CONFIG(easingcurve)
#endif  // QT_CONFIG(easingcurve)
