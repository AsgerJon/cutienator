//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthreadpool.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qthreadpool.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QThreadPool that Python can take functions over in. Every QThreadPool
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQThreadPoolCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQThreadPoolCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadPoolCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadPoolCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadPoolCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadPoolCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadPoolCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQThreadPool : public QThreadPool {
public:
  using QThreadPool::QThreadPool;
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
      CuteQThreadPoolCall0 call = reinterpret_cast<CuteQThreadPoolCall0>(taken[0]);
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
      CuteQThreadPoolCall1 call = reinterpret_cast<CuteQThreadPoolCall1>(taken[1]);
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
      CuteQThreadPoolCall2 call = reinterpret_cast<CuteQThreadPoolCall2>(taken[2]);
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
      CuteQThreadPoolCall3 call = reinterpret_cast<CuteQThreadPoolCall3>(taken[3]);
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
      CuteQThreadPoolCall4 call = reinterpret_cast<CuteQThreadPoolCall4>(taken[4]);
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
      CuteQThreadPoolCall5 call = reinterpret_cast<CuteQThreadPoolCall5>(taken[5]);
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
      CuteQThreadPoolCall6 call = reinterpret_cast<CuteQThreadPoolCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QThreadPool::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QThreadPool10metaObjectEv(
    const QThreadPool *self) {
  return self->metaObject();
}

//  QString QThreadPool::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QThreadPool2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QThreadPool::tr(s, c, n));
}

//  QThreadPoolPrivate *QThreadPool::d_func()
extern "C" Q_DECL_EXPORT
QThreadPoolPrivate *ritual_ZN11QThreadPool6d_funcEv(QThreadPool *self) {
  return self->d_func();
}

//  const QThreadPoolPrivate *QThreadPool::d_func() const
extern "C" Q_DECL_EXPORT
const QThreadPoolPrivate *ritual_ZNK11QThreadPool6d_funcEv(
    const QThreadPool *self) {
  return self->d_func();
}

//  QThreadPool::QThreadPool(QObject *parent)
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN11QThreadPoolC1EP7QObject(QObject *parent) {
  return new CuteQThreadPool(parent);
}

//  QThreadPool::~QThreadPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPoolD1Ev(QThreadPool *self) {
  delete self;
}

//  QThreadPool *QThreadPool::globalInstance()
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN11QThreadPool14globalInstanceEv() {
  return QThreadPool::globalInstance();
}

//  void QThreadPool::start(QRunnable *runnable, int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool5startEP9QRunnablei(
    QThreadPool *self,
    QRunnable *runnable,
    int priority) {
  self->start(runnable, priority);
}

//  bool QThreadPool::tryStart(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool8tryStartEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  return self->tryStart(runnable);
}

//  void QThreadPool::startOnReservedThread(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool21startOnReservedThreadEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  self->startOnReservedThread(runnable);
}

//  int QThreadPool::expiryTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool13expiryTimeoutEv(const QThreadPool *self) {
  return self->expiryTimeout();
}

//  void QThreadPool::setExpiryTimeout(int expiryTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool16setExpiryTimeoutEi(
    QThreadPool *self,
    int expiryTimeout) {
  self->setExpiryTimeout(expiryTimeout);
}

//  int QThreadPool::maxThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool14maxThreadCountEv(const QThreadPool *self) {
  return self->maxThreadCount();
}

//  void QThreadPool::setMaxThreadCount(int maxThreadCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool17setMaxThreadCountEi(
    QThreadPool *self,
    int maxThreadCount) {
  self->setMaxThreadCount(maxThreadCount);
}

//  int QThreadPool::activeThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool17activeThreadCountEv(const QThreadPool *self) {
  return self->activeThreadCount();
}

//  void QThreadPool::setStackSize(uint stackSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool12setStackSizeEj(
    QThreadPool *self,
    uint stackSize) {
  self->setStackSize(stackSize);
}

//  uint QThreadPool::stackSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11QThreadPool9stackSizeEv(const QThreadPool *self) {
  return self->stackSize();
}

//  void QThreadPool::setThreadPriority(QThread::Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool17setThreadPriorityEN7QThread8PriorityE(
    QThreadPool *self,
    QThread::Priority priority) {
  self->setThreadPriority(priority);
}

//  QThread::Priority QThreadPool::threadPriority() const
extern "C" Q_DECL_EXPORT
QThread::Priority ritual_ZNK11QThreadPool14threadPriorityEv(
    const QThreadPool *self) {
  return self->threadPriority();
}

//  void QThreadPool::reserveThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool13reserveThreadEv(QThreadPool *self) {
  self->reserveThread();
}

//  void QThreadPool::releaseThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool13releaseThreadEv(QThreadPool *self) {
  self->releaseThread();
}

//  void QThreadPool::setServiceLevel(QThread::QualityOfService serviceLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool15setServiceLevelEN7QThread16QualityOfServiceE(
    QThreadPool *self,
    QThread::QualityOfService serviceLevel) {
  self->setServiceLevel(serviceLevel);
}

//  QThread::QualityOfService QThreadPool::serviceLevel() const
extern "C" Q_DECL_EXPORT
QThread::QualityOfService ritual_ZNK11QThreadPool12serviceLevelEv(
    const QThreadPool *self) {
  return self->serviceLevel();
}

//  bool QThreadPool::waitForDone(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool11waitForDoneEi(QThreadPool *self, int msecs) {
  return self->waitForDone(msecs);
}

//  bool QThreadPool::waitForDone(QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool11waitForDoneE14QDeadlineTimer(
    QThreadPool *self,
    const QDeadlineTimer *deadline) {
  return self->waitForDone(*deadline);
}

//  void QThreadPool::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool5clearEv(QThreadPool *self) {
  self->clear();
}

//  bool QThreadPool::contains(const QThread *thread) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QThreadPool8containsEPK7QThread(
    const QThreadPool *self,
    const QThread *thread) {
  return self->contains(thread);
}

//  bool QThreadPool::tryTake(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool7tryTakeEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  return self->tryTake(runnable);
}

//  a Python function taken by a CuteQThreadPool, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QThreadPool(
    QThreadPool *self,
    const char *key,
    void *call) {
  return static_cast<CuteQThreadPool *>(self)->take(key, call);
}
