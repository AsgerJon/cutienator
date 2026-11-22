//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qeventloop.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>

//  const QMetaObject *QEventLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QEventLoop10metaObjectEv(
    const QEventLoop *self) {
  return self->metaObject();
}

//  QString QEventLoop::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QEventLoop2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventLoop::tr(s, c, n));
}

//  QEventLoop::QEventLoop(QObject *parent)
extern "C" Q_DECL_EXPORT
QEventLoop *ritual_ZN10QEventLoopC1EP7QObject(QObject *parent) {
  return new QEventLoop(parent);
}

//  QEventLoop::~QEventLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoopD1Ev(QEventLoop *self) {
  delete self;
}

//  bool QEventLoop::processEvents(ProcessEventsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEE(
    QEventLoop *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventLoop::processEvents(ProcessEventsFlags flags, int maximumTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEEi(
    QEventLoop *self,
    int flags,
    int maximumTime) {
  self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      maximumTime);
}

//  void QEventLoop::processEvents(ProcessEventsFlags flags, QDeadlineTimer
//      deadline)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEE14QDeadlineTimer(
    QEventLoop *self,
    int flags,
    const QDeadlineTimer *deadline) {
  self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}

//  int QEventLoop::exec(ProcessEventsFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QEventLoop4execE6QFlagsINS_17ProcessEventsFlagEE(
    QEventLoop *self,
    int flags) {
  return self->exec(QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  bool QEventLoop::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QEventLoop9isRunningEv(const QEventLoop *self) {
  return self->isRunning();
}

//  void QEventLoop::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop6wakeUpEv(QEventLoop *self) {
  self->wakeUp();
}

//  bool QEventLoop::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QEventLoop5eventEP6QEvent(QEventLoop *self, QEvent *event) {
  return self->event(event);
}

//  void QEventLoop::exit(int returnCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop4exitEi(QEventLoop *self, int returnCode) {
  self->exit(returnCode);
}

//  void QEventLoop::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop4quitEv(QEventLoop *self) {
  self->quit();
}
