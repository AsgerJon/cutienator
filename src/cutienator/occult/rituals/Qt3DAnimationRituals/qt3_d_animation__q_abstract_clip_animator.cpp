//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qabstractclipanimator.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qabstractclipanimator.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QAbstractClipAnimator that Python can take functions over in. Every Qt3DAnimation::QAbstractClipAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAbstractClipAnimatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAbstractClipAnimatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAbstractClipAnimatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAbstractClipAnimatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAbstractClipAnimatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAbstractClipAnimatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAbstractClipAnimatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QAbstractClipAnimator : public Qt3DAnimation::QAbstractClipAnimator {
public:
  using Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall0 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall1 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall2 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall3 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall4 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall5 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractClipAnimatorCall6 call = reinterpret_cast<CuteQt3DAnimation_QAbstractClipAnimatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QAbstractClipAnimator::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator10metaObjectEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAbstractClipAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation21QAbstractClipAnimator11qt_metacastEPKc(
    Qt3DAnimation::QAbstractClipAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAbstractClipAnimator::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation21QAbstractClipAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAbstractClipAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAbstractClipAnimator::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation21QAbstractClipAnimator2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAbstractClipAnimator::tr(s, c, n));
}

//  Qt3DAnimation::QAbstractClipAnimator::~QAbstractClipAnimator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimatorD1Ev(
    Qt3DAnimation::QAbstractClipAnimator *self) {
  delete self;
}

//  bool Qt3DAnimation::QAbstractClipAnimator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator9isRunningEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->isRunning();
}

//  Qt3DAnimation::QChannelMapper
//      *Qt3DAnimation::QAbstractClipAnimator::channelMapper() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapper *ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator13channelMapperEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->channelMapper();
}

//  int Qt3DAnimation::QAbstractClipAnimator::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator9loopCountEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->loopCount();
}

//  Qt3DAnimation::QClock *Qt3DAnimation::QAbstractClipAnimator::clock()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClock *ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator5clockEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->clock();
}

//  float Qt3DAnimation::QAbstractClipAnimator::normalizedTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator14normalizedTimeEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->normalizedTime();
}

//  void Qt3DAnimation::QAbstractClipAnimator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator10setRunningEb(
    Qt3DAnimation::QAbstractClipAnimator *self,
    bool running) {
  self->setRunning(running);
}

//  void Qt3DAnimation::QAbstractClipAnimator::setChannelMapper(Qt3DAnimation
//      ::QChannelMapper *channelMapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator16setChannelMapperEPNS_14QChannelMapperE(
    Qt3DAnimation::QAbstractClipAnimator *self,
    Qt3DAnimation::QChannelMapper *channelMapper) {
  self->setChannelMapper(channelMapper);
}

//  void Qt3DAnimation::QAbstractClipAnimator::setLoopCount(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator12setLoopCountEi(
    Qt3DAnimation::QAbstractClipAnimator *self,
    int loops) {
  self->setLoopCount(loops);
}

//  void Qt3DAnimation::QAbstractClipAnimator::setClock(Qt3DAnimation::QClock
//      *clock)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator8setClockEPNS_6QClockE(
    Qt3DAnimation::QAbstractClipAnimator *self,
    Qt3DAnimation::QClock *clock) {
  self->setClock(clock);
}

//  void Qt3DAnimation::QAbstractClipAnimator::setNormalizedTime(float
//      timeFraction)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator17setNormalizedTimeEf(
    Qt3DAnimation::QAbstractClipAnimator *self,
    float timeFraction) {
  self->setNormalizedTime(timeFraction);
}

//  void Qt3DAnimation::QAbstractClipAnimator::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator5startEv(
    Qt3DAnimation::QAbstractClipAnimator *self) {
  self->start();
}

//  void Qt3DAnimation::QAbstractClipAnimator::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator4stopEv(
    Qt3DAnimation::QAbstractClipAnimator *self) {
  self->stop();
}

//  void Qt3DAnimation::QAbstractClipAnimator::runningChanged(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator14runningChangedEb(
    Qt3DAnimation::QAbstractClipAnimator *self,
    bool running) {
  self->runningChanged(running);
}

//  void Qt3DAnimation::QAbstractClipAnimator::channelMapperChanged(Qt3DAnima
//      tion::QChannelMapper *channelMapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator20channelMapperChangedEPNS_14QChannelMapperE(
    Qt3DAnimation::QAbstractClipAnimator *self,
    Qt3DAnimation::QChannelMapper *channelMapper) {
  self->channelMapperChanged(channelMapper);
}

//  void Qt3DAnimation::QAbstractClipAnimator::loopCountChanged(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator16loopCountChangedEi(
    Qt3DAnimation::QAbstractClipAnimator *self,
    int loops) {
  self->loopCountChanged(loops);
}

//  void
//      Qt3DAnimation::QAbstractClipAnimator::clockChanged(Qt3DAnimation::QCl
//      ock *clock)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator12clockChangedEPNS_6QClockE(
    Qt3DAnimation::QAbstractClipAnimator *self,
    Qt3DAnimation::QClock *clock) {
  self->clockChanged(clock);
}

//  void Qt3DAnimation::QAbstractClipAnimator::normalizedTimeChanged(float
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QAbstractClipAnimator21normalizedTimeChangedEf(
    Qt3DAnimation::QAbstractClipAnimator *self,
    float index) {
  self->normalizedTimeChanged(index);
}

//  Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator(Qt3DCore::QNo
//      de *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipAnimator *ritual_ZN13Qt3DAnimation21QAbstractClipAnimatorC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QAbstractClipAnimator(parent);
}

//  Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator(QAbstractClip
//      AnimatorPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipAnimator *ritual_ZN13Qt3DAnimation21QAbstractClipAnimatorC1ERNS_28QAbstractClipAnimatorPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QAbstractClipAnimatorPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QAbstractClipAnimator(*dd, parent);
}

//  QAbstractClipAnimatorPrivate
//      *Qt3DAnimation::QAbstractClipAnimator::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipAnimatorPrivate *ritual_ZN13Qt3DAnimation21QAbstractClipAnimator6d_funcEv(
    Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->d_func();
}

//  const QAbstractClipAnimatorPrivate
//      *Qt3DAnimation::QAbstractClipAnimator::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAbstractClipAnimatorPrivate *ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator6d_funcEv(
    const Qt3DAnimation::QAbstractClipAnimator *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QAbstractClipAnimator, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAbstractClipAnimator(
    Qt3DAnimation::QAbstractClipAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAbstractClipAnimator *>(self)->take(key, call);
}
