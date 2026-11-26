//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qthreadpooler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qthreadpooler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QFuture>

//  A Qt3DCore::QThreadPooler that Python can take functions over in. Every Qt3DCore::QThreadPooler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QThreadPoolerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QThreadPoolerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QThreadPoolerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QThreadPoolerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QThreadPoolerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QThreadPoolerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QThreadPoolerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QThreadPooler : public Qt3DCore::QThreadPooler {
public:
  using Qt3DCore::QThreadPooler::QThreadPooler;
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
      CuteQt3DCore_QThreadPoolerCall0 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall0>(taken[0]);
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
      CuteQt3DCore_QThreadPoolerCall1 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall1>(taken[1]);
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
      CuteQt3DCore_QThreadPoolerCall2 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall2>(taken[2]);
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
      CuteQt3DCore_QThreadPoolerCall3 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall3>(taken[3]);
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
      CuteQt3DCore_QThreadPoolerCall4 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall4>(taken[4]);
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
      CuteQt3DCore_QThreadPoolerCall5 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall5>(taken[5]);
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
      CuteQt3DCore_QThreadPoolerCall6 call = reinterpret_cast<CuteQt3DCore_QThreadPoolerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QThreadPooler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore13QThreadPooler10metaObjectEv(
    const Qt3DCore::QThreadPooler *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QThreadPooler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore13QThreadPooler11qt_metacastEPKc(
    Qt3DCore::QThreadPooler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QThreadPooler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore13QThreadPooler11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QThreadPooler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QThreadPooler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore13QThreadPooler2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QThreadPooler::tr(s, c, n));
}

//  Qt3DCore::QThreadPooler::QThreadPooler(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QThreadPooler *ritual_ZN8Qt3DCore13QThreadPoolerC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_QThreadPooler(parent);
}

//  Qt3DCore::QThreadPooler::~QThreadPooler()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPoolerD1Ev(Qt3DCore::QThreadPooler *self) {
  delete self;
}

//  QFuture<void>
//      Qt3DCore::QThreadPooler::mapDependables(QList<RunnableInterface *>
//      &taskQueue)
extern "C" Q_DECL_EXPORT
QFuture<void> *ritual_ZN8Qt3DCore13QThreadPooler14mapDependablesER5QListIPNS_17RunnableInterfaceEE(
    Qt3DCore::QThreadPooler *self,
    QList<Qt3DCore::RunnableInterface *> *taskQueue) {
  return new QFuture<void>(self->mapDependables(*taskQueue));
}

//  int Qt3DCore::QThreadPooler::waitForAllJobs()
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore13QThreadPooler14waitForAllJobsEv(
    Qt3DCore::QThreadPooler *self) {
  return self->waitForAllJobs();
}

//  void Qt3DCore::QThreadPooler::taskFinished(RunnableInterface *task)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler12taskFinishedEPNS_17RunnableInterfaceE(
    Qt3DCore::QThreadPooler *self,
    Qt3DCore::RunnableInterface *task) {
  self->taskFinished(task);
}

//  QFuture<void> Qt3DCore::QThreadPooler::future()
extern "C" Q_DECL_EXPORT
QFuture<void> *ritual_ZN8Qt3DCore13QThreadPooler6futureEv(
    Qt3DCore::QThreadPooler *self) {
  return new QFuture<void>(self->future());
}

//  void Qt3DCore::QThreadPooler::enqueueTasks(const QList<RunnableInterface
//      *> &tasks)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler12enqueueTasksERK5QListIPNS_17RunnableInterfaceEE(
    Qt3DCore::QThreadPooler *self,
    const QList<Qt3DCore::RunnableInterface *> *tasks) {
  self->enqueueTasks(*tasks);
}

//  void Qt3DCore::QThreadPooler::skipTask(RunnableInterface *task)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler8skipTaskEPNS_17RunnableInterfaceE(
    Qt3DCore::QThreadPooler *self,
    Qt3DCore::RunnableInterface *task) {
  self->skipTask(task);
}

//  void Qt3DCore::QThreadPooler::enqueueDepencies(RunnableInterface *task)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler16enqueueDepenciesEPNS_17RunnableInterfaceE(
    Qt3DCore::QThreadPooler *self,
    Qt3DCore::RunnableInterface *task) {
  self->enqueueDepencies(task);
}

//  void Qt3DCore::QThreadPooler::acquire(int add)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler7acquireEi(
    Qt3DCore::QThreadPooler *self,
    int add) {
  self->acquire(add);
}

//  void Qt3DCore::QThreadPooler::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QThreadPooler7releaseEv(
    Qt3DCore::QThreadPooler *self) {
  self->release();
}

//  int Qt3DCore::QThreadPooler::currentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QThreadPooler12currentCountEv(
    const Qt3DCore::QThreadPooler *self) {
  return self->currentCount();
}

//  a Python function taken by a CuteQt3DCore_QThreadPooler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QThreadPooler(
    Qt3DCore::QThreadPooler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QThreadPooler *>(self)->take(key, call);
}

//  a QFuture<void> a ritual of Qt3DCore::QThreadPooler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QThreadPooler__QFuture_void(QFuture<void> *self) {
  delete self;
}
