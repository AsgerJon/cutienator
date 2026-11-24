//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmltimer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQmlMeta/qtqmlmetaexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlMeta/QtQmlMeta>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlMeta/6.12.0/QtQmlMeta/private/qqmltimer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQmlTimer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTimer : QQmlTimer {
  using QQmlTimer::classBegin;
  using QQmlTimer::componentComplete;
  using QQmlTimer::event;
};

//  const QMetaObject *QQmlTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QQmlTimer10metaObjectEv(
    const QQmlTimer *self) {
  return self->metaObject();
}

//  QString QQmlTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QQmlTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTimer::tr(s, c, n));
}

//  QQmlTimer::QQmlTimer(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTimer *ritual_ZN9QQmlTimerC1EP7QObject(QObject *parent) {
  return new QQmlTimer(parent);
}

//  void QQmlTimer::setInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer11setIntervalEi(QQmlTimer *self, int interval) {
  self->setInterval(interval);
}

//  int QQmlTimer::interval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQmlTimer8intervalEv(const QQmlTimer *self) {
  return self->interval();
}

//  bool QQmlTimer::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQmlTimer9isRunningEv(const QQmlTimer *self) {
  return self->isRunning();
}

//  void QQmlTimer::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer10setRunningEb(QQmlTimer *self, bool running) {
  self->setRunning(running);
}

//  bool QQmlTimer::isRepeating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQmlTimer11isRepeatingEv(const QQmlTimer *self) {
  return self->isRepeating();
}

//  void QQmlTimer::setRepeating(bool repeating)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer12setRepeatingEb(QQmlTimer *self, bool repeating) {
  self->setRepeating(repeating);
}

//  bool QQmlTimer::triggeredOnStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQmlTimer16triggeredOnStartEv(const QQmlTimer *self) {
  return self->triggeredOnStart();
}

//  void QQmlTimer::setTriggeredOnStart(bool triggeredOnStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer19setTriggeredOnStartEb(
    QQmlTimer *self,
    bool triggeredOnStart) {
  self->setTriggeredOnStart(triggeredOnStart);
}

//  void QQmlTimer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer10classBeginEv(QQmlTimer *self) {
  self->classBegin();
}

//  void QQmlTimer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer17componentCompleteEv(QQmlTimer *self) {
  self->componentComplete();
}

//  bool QQmlTimer::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QQmlTimer5eventEP6QEvent(QQmlTimer *self, QEvent *a0) {
  return self->event(a0);
}

//  void QQmlTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer5startEv(QQmlTimer *self) {
  self->start();
}

//  void QQmlTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer4stopEv(QQmlTimer *self) {
  self->stop();
}

//  void QQmlTimer::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer7restartEv(QQmlTimer *self) {
  self->restart();
}

//  void QQmlTimer::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer6updateEv(QQmlTimer *self) {
  self->update();
}

//  void QQmlTimer::ticked()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQmlTimer6tickedEv(QQmlTimer *self) {
  self->ticked();
}

//  QQmlTimer as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlTimer_QQmlParserStatus(QQmlTimer *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQmlTimer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QQmlTimer10classBeginEv(QQmlTimer *self) {
  static_cast<OwnQQmlTimer *>(self)->OwnQQmlTimer::classBegin();
}

//  void QQmlTimer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QQmlTimer17componentCompleteEv(QQmlTimer *self) {
  static_cast<OwnQQmlTimer *>(self)->OwnQQmlTimer::componentComplete();
}

//  bool QQmlTimer::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QQmlTimer5eventEP6QEvent(QQmlTimer *self, QEvent *a0) {
  return static_cast<OwnQQmlTimer *>(self)->OwnQQmlTimer::event(a0);
}

#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(qml_animation)
