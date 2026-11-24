//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcoreapplication_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcoreapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QCoreApplicationPrivate that Python can take functions over in. Every QCoreApplicationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationPrivateCall0)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationPrivateCall1)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreApplicationPrivateCall2)(const void *, QEvent *, QObject *, QPostEventList *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreApplicationPrivateCall3)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreApplicationPrivateCall4)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoreApplicationPrivate : public QCoreApplicationPrivate {
public:
  using QCoreApplicationPrivate::QCoreApplicationPrivate;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate21createEventDispatcherEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjectP14QPostEventList")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate4quitEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QCoreApplicationPrivate::createEventDispatcher()
  void createEventDispatcher() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoreApplicationPrivateCall0 call = reinterpret_cast<CuteQCoreApplicationPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QCoreApplicationPrivate::createEventDispatcher();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QCoreApplicationPrivate::eventDispatcherReady()
  void eventDispatcherReady() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoreApplicationPrivateCall1 call = reinterpret_cast<CuteQCoreApplicationPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QCoreApplicationPrivate::eventDispatcherReady();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QCoreApplicationPrivate::compressEvent(QEvent *event, QObject
  //      *receiver, QPostEventList *postedEvents)
  bool compressEvent(
      QEvent *event,
      QObject *receiver,
      QPostEventList *postedEvents) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoreApplicationPrivateCall2 call = reinterpret_cast<CuteQCoreApplicationPrivateCall2>(taken[2]);
      bool given = call(this, event, receiver, postedEvents, &handled);
      if (handled) return given;
    }
    return QCoreApplicationPrivate::compressEvent(event, receiver, postedEvents);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QCoreApplicationPrivate::canQuitAutomatically()
  bool canQuitAutomatically() override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoreApplicationPrivateCall3 call = reinterpret_cast<CuteQCoreApplicationPrivateCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreApplicationPrivate::canQuitAutomatically();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QCoreApplicationPrivate::quit()
  void quit() override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoreApplicationPrivateCall4 call = reinterpret_cast<CuteQCoreApplicationPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QCoreApplicationPrivate::quit();
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QCoreApplication *QCoreApplicationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoreApplication *ritual_ZN23QCoreApplicationPrivate6q_funcEv(
    QCoreApplicationPrivate *self) {
  return self->q_func();
}

//  const QCoreApplication *QCoreApplicationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoreApplication *ritual_ZNK23QCoreApplicationPrivate6q_funcEv(
    const QCoreApplicationPrivate *self) {
  return self->q_func();
}

//  QCoreApplicationPrivate::QCoreApplicationPrivate(int &aargc, char
//      **aargv)
extern "C" Q_DECL_EXPORT
QCoreApplicationPrivate *ritual_ZN23QCoreApplicationPrivateC1ERiPPc(
    int *aargc,
    char **aargv) {
  return new CuteQCoreApplicationPrivate(*aargc, aargv);
}

//  QCoreApplicationPrivate::~QCoreApplicationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivateD1Ev(QCoreApplicationPrivate *self) {
  delete self;
}

//  void QCoreApplicationPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate4initEv(
    QCoreApplicationPrivate *self) {
  self->init();
}

//  QString QCoreApplicationPrivate::appName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QCoreApplicationPrivate7appNameEv(
    const QCoreApplicationPrivate *self) {
  return new QString(self->appName());
}

//  QString QCoreApplicationPrivate::appVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QCoreApplicationPrivate10appVersionEv(
    const QCoreApplicationPrivate *self) {
  return new QString(self->appVersion());
}

//  void QCoreApplicationPrivate::initLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate10initLocaleEv() {
  QCoreApplicationPrivate::initLocale();
}

//  bool QCoreApplicationPrivate::checkInstance(const char *method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate13checkInstanceEPKc(
    const char *method) {
  return QCoreApplicationPrivate::checkInstance(method);
}

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::sendThroughApplicationEventFilters(QObject
//      *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate34sendThroughApplicationEventFiltersEP7QObjectP6QEvent(
    QCoreApplicationPrivate *self,
    QObject *a0,
    QEvent *a1) {
  return self->sendThroughApplicationEventFilters(a0, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject *a0,
//      QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate29sendThroughObjectEventFiltersEP7QObjectP6QEvent(
    QObject *a0,
    QEvent *a1) {
  return QCoreApplicationPrivate::sendThroughObjectEventFilters(a0, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::notify_helper(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate13notify_helperEP7QObjectP6QEvent(
    QObject *a0,
    QEvent *a1) {
  return QCoreApplicationPrivate::notify_helper(a0, a1);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::setEventSpontaneous(QEvent *e, bool
//      spontaneous)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate19setEventSpontaneousEP6QEventb(
    QEvent *e,
    bool spontaneous) {
  QCoreApplicationPrivate::setEventSpontaneous(e, spontaneous);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate21createEventDispatcherEv(
    QCoreApplicationPrivate *self) {
  self->createEventDispatcher();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::eventDispatcherReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv(
    QCoreApplicationPrivate *self) {
  self->eventDispatcherReady();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::compressEvent(QEvent *event, QObject
//      *receiver, QPostEventList *postedEvents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjectP14QPostEventList(
    QCoreApplicationPrivate *self,
    QEvent *event,
    QObject *receiver,
    QPostEventList *postedEvents) {
  return self->compressEvent(event, receiver, postedEvents);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::removePostedEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate17removePostedEventEP6QEvent(
    QEvent *a0) {
  QCoreApplicationPrivate::removePostedEvent(a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate3refEv(
    QCoreApplicationPrivate *self) {
  self->ref();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::deref()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate5derefEv(
    QCoreApplicationPrivate *self) {
  self->deref();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::canQuitAutomatically()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv(
    QCoreApplicationPrivate *self) {
  return self->canQuitAutomatically();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::quitAutomatically()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate17quitAutomaticallyEv(
    QCoreApplicationPrivate *self) {
  self->quitAutomatically();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate4quitEv(
    QCoreApplicationPrivate *self) {
  self->quit();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QThread *QCoreApplicationPrivate::mainThread()
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN23QCoreApplicationPrivate10mainThreadEv() {
  return QCoreApplicationPrivate::mainThread();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::sendPostedEvents(QObject *receiver, int
//      event_type, QThreadData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate16sendPostedEventsEP7QObjectiP11QThreadData(
    QObject *receiver,
    int event_type,
    QThreadData *data) {
  QCoreApplicationPrivate::sendPostedEvents(receiver, event_type, data);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::checkReceiverThread(QObject *receiver)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate19checkReceiverThreadEP7QObject(
    QObject *receiver) {
  QCoreApplicationPrivate::checkReceiverThread(receiver);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::cleanupThreadData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate17cleanupThreadDataEv(
    QCoreApplicationPrivate *self) {
  self->cleanupThreadData();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::execCleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate11execCleanupEv(
    QCoreApplicationPrivate *self) {
  self->execCleanup();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_TRANSLATION)
//  bool QCoreApplicationPrivate::isTranslatorInstalled(QTranslator
//      *translator)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate21isTranslatorInstalledEP11QTranslator(
    QTranslator *translator) {
  return QCoreApplicationPrivate::isTranslatorInstalled(translator);
}
#endif  // !defined(QT_NO_TRANSLATION)

//  bool QCoreApplicationPrivate::testAttribute(uint flag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QCoreApplicationPrivate13testAttributeEj(uint flag) {
  return QCoreApplicationPrivate::testAttribute(flag);
}

//  void QCoreApplicationPrivate::processCommandLineArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCoreApplicationPrivate27processCommandLineArgumentsEv(
    QCoreApplicationPrivate *self) {
  self->processCommandLineArguments();
}

//  a Python function taken by a CuteQCoreApplicationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoreApplicationPrivate(
    QCoreApplicationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoreApplicationPrivate *>(self)->take(key, call);
}

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QCoreApplicationPrivate21createEventDispatcherEv(
    QCoreApplicationPrivate *self) {
  self->QCoreApplicationPrivate::createEventDispatcher();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::eventDispatcherReady()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv(
    QCoreApplicationPrivate *self) {
  self->QCoreApplicationPrivate::eventDispatcherReady();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::compressEvent(QEvent *event, QObject
//      *receiver, QPostEventList *postedEvents)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjectP14QPostEventList(
    QCoreApplicationPrivate *self,
    QEvent *event,
    QObject *receiver,
    QPostEventList *postedEvents) {
  return self->QCoreApplicationPrivate::compressEvent(
      event,
      receiver,
      postedEvents);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  bool QCoreApplicationPrivate::canQuitAutomatically()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv(
    QCoreApplicationPrivate *self) {
  return self->QCoreApplicationPrivate::canQuitAutomatically();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QCoreApplicationPrivate::quit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QCoreApplicationPrivate4quitEv(
    QCoreApplicationPrivate *self) {
  self->QCoreApplicationPrivate::quit();
}
#endif  // !defined(QT_NO_QOBJECT)
