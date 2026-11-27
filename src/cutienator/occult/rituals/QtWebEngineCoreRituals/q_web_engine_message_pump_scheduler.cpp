//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebenginemessagepumpscheduler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginemessagepumpscheduler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <functional>

//  Only a class built on QWebEngineMessagePumpScheduler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWebEngineMessagePumpScheduler : QWebEngineMessagePumpScheduler {
  using QWebEngineMessagePumpScheduler::timerEvent;
};

//  const QMetaObject *QWebEngineMessagePumpScheduler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QWebEngineMessagePumpScheduler10metaObjectEv(
    const QWebEngineMessagePumpScheduler *self) {
  return self->metaObject();
}

//  void *QWebEngineMessagePumpScheduler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QWebEngineMessagePumpScheduler11qt_metacastEPKc(
    QWebEngineMessagePumpScheduler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineMessagePumpScheduler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QWebEngineMessagePumpScheduler11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineMessagePumpScheduler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineMessagePumpScheduler::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QWebEngineMessagePumpScheduler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineMessagePumpScheduler::tr(s, c, n));
}

//  QWebEngineMessagePumpScheduler::QWebEngineMessagePumpScheduler(std::funct
//      ion<void ()> callback)
extern "C" Q_DECL_EXPORT
QWebEngineMessagePumpScheduler *ritual_ZN30QWebEngineMessagePumpSchedulerC1ESt8functionIFvvEE(
    const std::function<void ()> *callback) {
  return new QWebEngineMessagePumpScheduler(*callback);
}

//  void QWebEngineMessagePumpScheduler::scheduleImmediateWork()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWebEngineMessagePumpScheduler21scheduleImmediateWorkEv(
    QWebEngineMessagePumpScheduler *self) {
  self->scheduleImmediateWork();
}

//  void QWebEngineMessagePumpScheduler::scheduleDelayedWork(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWebEngineMessagePumpScheduler19scheduleDelayedWorkEi(
    QWebEngineMessagePumpScheduler *self,
    int delay) {
  self->scheduleDelayedWork(delay);
}

//  void QWebEngineMessagePumpScheduler::timerEvent(QTimerEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWebEngineMessagePumpScheduler10timerEventEP11QTimerEvent(
    QWebEngineMessagePumpScheduler *self,
    QTimerEvent *ev) {
  self->timerEvent(ev);
}

//  void QWebEngineMessagePumpScheduler::timerEvent(QTimerEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QWebEngineMessagePumpScheduler10timerEventEP11QTimerEvent(
    QWebEngineMessagePumpScheduler *self,
    QTimerEvent *ev) {
  static_cast<OwnQWebEngineMessagePumpScheduler *>(self)->OwnQWebEngineMessagePumpScheduler::timerEvent(
      ev);
}
