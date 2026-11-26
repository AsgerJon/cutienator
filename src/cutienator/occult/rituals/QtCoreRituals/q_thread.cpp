//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthread.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qthread.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QThread may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQThread : QThread {
  using QThread::run;
};

//  A QThread that Python can take functions over in. Every QThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQThreadCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQThreadCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQThreadCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQThread : public QThread {
public:
  using QThread::QThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQThreadCall0 call = reinterpret_cast<CuteQThreadCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QThread::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQThreadCall1 call = reinterpret_cast<CuteQThreadCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QThread::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQThreadCall2 call = reinterpret_cast<CuteQThreadCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQThreadCall3 call = reinterpret_cast<CuteQThreadCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQThreadCall4 call = reinterpret_cast<CuteQThreadCall4>(taken[4]);
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
      CuteQThreadCall5 call = reinterpret_cast<CuteQThreadCall5>(taken[5]);
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
      CuteQThreadCall6 call = reinterpret_cast<CuteQThreadCall6>(taken[6]);
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
      CuteQThreadCall7 call = reinterpret_cast<CuteQThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QThread::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QThread10metaObjectEv(const QThread *self) {
  return self->metaObject();
}

//  void *QThread::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QThread11qt_metacastEPKc(QThread *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QThread::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QThread11qt_metacallEN11QMetaObject4CallEiPPv(
    QThread *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QThread::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QThread2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QThread::tr(s, c, n));
}

//  Qt::HANDLE QThread::currentThreadId()
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZN7QThread15currentThreadIdEv() {
  return QThread::currentThreadId();
}

//  QThread *QThread::currentThread()
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThread13currentThreadEv() {
  return QThread::currentThread();
}

//  bool QThread::isMainThread()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread12isMainThreadEv() {
  return QThread::isMainThread();
}

//  int QThread::idealThreadCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QThread16idealThreadCountEv() {
  return QThread::idealThreadCount();
}

//  void QThread::yieldCurrentThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread18yieldCurrentThreadEv() {
  QThread::yieldCurrentThread();
}

//  QThread::QThread(QObject *parent)
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThreadC1EP7QObject(QObject *parent) {
  return new CuteQThread(parent);
}

//  QThread::~QThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThreadD1Ev(QThread *self) {
  delete self;
}

//  void QThread::setPriority(Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread11setPriorityENS_8PriorityE(
    QThread *self,
    QThread::Priority priority) {
  self->setPriority(priority);
}

//  Priority QThread::priority() const
extern "C" Q_DECL_EXPORT
QThread::Priority ritual_ZNK7QThread8priorityEv(const QThread *self) {
  return self->priority();
}

//  bool QThread::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread10isFinishedEv(const QThread *self) {
  return self->isFinished();
}

//  bool QThread::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread9isRunningEv(const QThread *self) {
  return self->isRunning();
}

//  void QThread::requestInterruption()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread19requestInterruptionEv(QThread *self) {
  self->requestInterruption();
}

//  bool QThread::isInterruptionRequested() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread23isInterruptionRequestedEv(const QThread *self) {
  return self->isInterruptionRequested();
}

//  void QThread::setStackSize(uint stackSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread12setStackSizeEj(QThread *self, uint stackSize) {
  self->setStackSize(stackSize);
}

//  uint QThread::stackSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QThread9stackSizeEv(const QThread *self) {
  return self->stackSize();
}

//  QAbstractEventDispatcher *QThread::eventDispatcher() const
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZNK7QThread15eventDispatcherEv(
    const QThread *self) {
  return self->eventDispatcher();
}

//  void QThread::setEventDispatcher(QAbstractEventDispatcher
//      *eventDispatcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread18setEventDispatcherEP24QAbstractEventDispatcher(
    QThread *self,
    QAbstractEventDispatcher *eventDispatcher) {
  self->setEventDispatcher(eventDispatcher);
}

//  bool QThread::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread5eventEP6QEvent(QThread *self, QEvent *event) {
  return self->event(event);
}

//  int QThread::loopLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QThread9loopLevelEv(const QThread *self) {
  return self->loopLevel();
}

//  bool QThread::isCurrentThread() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread15isCurrentThreadEv(const QThread *self) {
  return self->isCurrentThread();
}

//  void QThread::setServiceLevel(QualityOfService serviceLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread15setServiceLevelENS_16QualityOfServiceE(
    QThread *self,
    QThread::QualityOfService serviceLevel) {
  self->setServiceLevel(serviceLevel);
}

//  QualityOfService QThread::serviceLevel() const
extern "C" Q_DECL_EXPORT
QThread::QualityOfService ritual_ZNK7QThread12serviceLevelEv(
    const QThread *self) {
  return self->serviceLevel();
}

//  void QThread::start(Priority a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread5startENS_8PriorityE(
    QThread *self,
    QThread::Priority a0) {
  self->start(a0);
}

//  void QThread::terminate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread9terminateEv(QThread *self) {
  self->terminate();
}

//  void QThread::exit(int retcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread4exitEi(QThread *self, int retcode) {
  self->exit(retcode);
}

//  void QThread::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread4quitEv(QThread *self) {
  self->quit();
}

//  bool QThread::wait(QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread4waitE14QDeadlineTimer(
    QThread *self,
    const QDeadlineTimer *deadline) {
  return self->wait(*deadline);
}

//  bool QThread::wait(unsigned long time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread4waitEm(QThread *self, unsigned long time) {
  return self->wait(time);
}

//  void QThread::sleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread5sleepEm(unsigned long a0) {
  QThread::sleep(a0);
}

//  void QThread::msleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread6msleepEm(unsigned long a0) {
  QThread::msleep(a0);
}

//  void QThread::usleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread6usleepEm(unsigned long a0) {
  QThread::usleep(a0);
}

//  void QThread::sleep(std::chrono::nanoseconds nsec)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread5sleepENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEE(
    long long nsec) {
  QThread::sleep(std::chrono::nanoseconds(nsec));
}

//  void QThread::started(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread7startedENS_14QPrivateSignalE(QThread *self) {
  self->started(QThread::QPrivateSignal());
}

//  void QThread::finished(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread8finishedENS_14QPrivateSignalE(QThread *self) {
  self->finished(QThread::QPrivateSignal());
}

//  void QThread::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread3runEv(QThread *self) {
  self->run();
}

//  int QThread::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QThread4execEv(QThread *self) {
  return self->exec();
}

//  void QThread::setTerminationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread21setTerminationEnabledEb(bool enabled) {
  QThread::setTerminationEnabled(enabled);
}

//  QThread::QThread(QThreadPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThreadC1ER14QThreadPrivateP7QObject(
    QThreadPrivate *dd,
    QObject *parent) {
  return new CuteQThread(*dd, parent);
}

//  QThreadPrivate *QThread::d_func()
extern "C" Q_DECL_EXPORT
QThreadPrivate *ritual_ZN7QThread6d_funcEv(QThread *self) {
  return self->d_func();
}

//  const QThreadPrivate *QThread::d_func() const
extern "C" Q_DECL_EXPORT
const QThreadPrivate *ritual_ZNK7QThread6d_funcEv(const QThread *self) {
  return self->d_func();
}

//  QThread *QThread::createThreadImpl(std::future<void> &&future)
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThread16createThreadImplEOSt6futureIvE(
    std::future<void> *future) {
  return QThread::createThreadImpl(std::move(*future));
}

//  Qt::HANDLE QThread::currentThreadIdImpl()
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZN7QThread19currentThreadIdImplEv() {
  return QThread::currentThreadIdImpl();
}

//  a Python function taken by a CuteQThread, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QThread(QThread *self, const char *key, void *call) {
  return static_cast<CuteQThread *>(self)->take(key, call);
}

//  bool QThread::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QThread5eventEP6QEvent(QThread *self, QEvent *event) {
  return self->QThread::event(event);
}

//  void QThread::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QThread3runEv(QThread *self) {
  static_cast<OwnQThread *>(self)->OwnQThread::run();
}
