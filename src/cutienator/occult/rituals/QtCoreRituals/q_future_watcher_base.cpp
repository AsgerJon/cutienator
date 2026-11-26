//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfuturewatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/qfuturewatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qfutureinterface.h>

//  Only a class built on QFutureWatcherBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFutureWatcherBase : QFutureWatcherBase {
  using QFutureWatcherBase::connectNotify;
  using QFutureWatcherBase::disconnectNotify;
};

//  const QMetaObject *QFutureWatcherBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QFutureWatcherBase10metaObjectEv(
    const QFutureWatcherBase *self) {
  return self->metaObject();
}

//  void *QFutureWatcherBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QFutureWatcherBase11qt_metacastEPKc(
    QFutureWatcherBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QFutureWatcherBase::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QFutureWatcherBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QFutureWatcherBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QFutureWatcherBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFutureWatcherBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFutureWatcherBase::tr(s, c, n));
}

//  QFutureWatcherBasePrivate *QFutureWatcherBase::d_func()
extern "C" Q_DECL_EXPORT
QFutureWatcherBasePrivate *ritual_ZN18QFutureWatcherBase6d_funcEv(
    QFutureWatcherBase *self) {
  return self->d_func();
}

//  const QFutureWatcherBasePrivate *QFutureWatcherBase::d_func() const
extern "C" Q_DECL_EXPORT
const QFutureWatcherBasePrivate *ritual_ZNK18QFutureWatcherBase6d_funcEv(
    const QFutureWatcherBase *self) {
  return self->d_func();
}

//  int QFutureWatcherBase::progressValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase13progressValueEv(
    const QFutureWatcherBase *self) {
  return self->progressValue();
}

//  int QFutureWatcherBase::progressMinimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase15progressMinimumEv(
    const QFutureWatcherBase *self) {
  return self->progressMinimum();
}

//  int QFutureWatcherBase::progressMaximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase15progressMaximumEv(
    const QFutureWatcherBase *self) {
  return self->progressMaximum();
}

//  QString QFutureWatcherBase::progressText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFutureWatcherBase12progressTextEv(
    const QFutureWatcherBase *self) {
  return new QString(self->progressText());
}

//  bool QFutureWatcherBase::isStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase9isStartedEv(
    const QFutureWatcherBase *self) {
  return self->isStarted();
}

//  bool QFutureWatcherBase::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase10isFinishedEv(
    const QFutureWatcherBase *self) {
  return self->isFinished();
}

//  bool QFutureWatcherBase::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase9isRunningEv(
    const QFutureWatcherBase *self) {
  return self->isRunning();
}

//  bool QFutureWatcherBase::isCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase10isCanceledEv(
    const QFutureWatcherBase *self) {
  return self->isCanceled();
}

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QFutureWatcherBase::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase8isPausedEv(
    const QFutureWatcherBase *self) {
  return self->isPaused();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  bool QFutureWatcherBase::isSuspending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase12isSuspendingEv(
    const QFutureWatcherBase *self) {
  return self->isSuspending();
}

//  bool QFutureWatcherBase::isSuspended() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase11isSuspendedEv(
    const QFutureWatcherBase *self) {
  return self->isSuspended();
}

//  void QFutureWatcherBase::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase15waitForFinishedEv(
    QFutureWatcherBase *self) {
  self->waitForFinished();
}

//  void QFutureWatcherBase::setPendingResultsLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase22setPendingResultsLimitEi(
    QFutureWatcherBase *self,
    int limit) {
  self->setPendingResultsLimit(limit);
}

//  bool QFutureWatcherBase::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFutureWatcherBase5eventEP6QEvent(
    QFutureWatcherBase *self,
    QEvent *event) {
  return self->event(event);
}

//  void QFutureWatcherBase::started()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase7startedEv(QFutureWatcherBase *self) {
  self->started();
}

//  void QFutureWatcherBase::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase8finishedEv(QFutureWatcherBase *self) {
  self->finished();
}

//  void QFutureWatcherBase::canceled()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase8canceledEv(QFutureWatcherBase *self) {
  self->canceled();
}

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureWatcherBase::paused()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase6pausedEv(QFutureWatcherBase *self) {
  self->paused();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  void QFutureWatcherBase::suspending()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase10suspendingEv(QFutureWatcherBase *self) {
  self->suspending();
}

//  void QFutureWatcherBase::suspended()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase9suspendedEv(QFutureWatcherBase *self) {
  self->suspended();
}

//  void QFutureWatcherBase::resumed()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase7resumedEv(QFutureWatcherBase *self) {
  self->resumed();
}

//  void QFutureWatcherBase::resultReadyAt(int resultIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase13resultReadyAtEi(
    QFutureWatcherBase *self,
    int resultIndex) {
  self->resultReadyAt(resultIndex);
}

//  void QFutureWatcherBase::resultsReadyAt(int beginIndex, int endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase14resultsReadyAtEii(
    QFutureWatcherBase *self,
    int beginIndex,
    int endIndex) {
  self->resultsReadyAt(beginIndex, endIndex);
}

//  void QFutureWatcherBase::progressRangeChanged(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase20progressRangeChangedEii(
    QFutureWatcherBase *self,
    int minimum,
    int maximum) {
  self->progressRangeChanged(minimum, maximum);
}

//  void QFutureWatcherBase::progressValueChanged(int progressValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase20progressValueChangedEi(
    QFutureWatcherBase *self,
    int progressValue) {
  self->progressValueChanged(progressValue);
}

//  void QFutureWatcherBase::progressTextChanged(const QString &progressText)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase19progressTextChangedERK7QString(
    QFutureWatcherBase *self,
    const QString *progressText) {
  self->progressTextChanged(*progressText);
}

//  void QFutureWatcherBase::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase6cancelEv(QFutureWatcherBase *self) {
  self->cancel();
}

//  void QFutureWatcherBase::setSuspended(bool suspend)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase12setSuspendedEb(
    QFutureWatcherBase *self,
    bool suspend) {
  self->setSuspended(suspend);
}

//  void QFutureWatcherBase::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase7suspendEv(QFutureWatcherBase *self) {
  self->suspend();
}

//  void QFutureWatcherBase::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase6resumeEv(QFutureWatcherBase *self) {
  self->resume();
}

//  void QFutureWatcherBase::toggleSuspended()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase15toggleSuspendedEv(
    QFutureWatcherBase *self) {
  self->toggleSuspended();
}

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureWatcherBase::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase9setPausedEb(
    QFutureWatcherBase *self,
    bool paused) {
  self->setPaused(paused);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureWatcherBase::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase5pauseEv(QFutureWatcherBase *self) {
  self->pause();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureWatcherBase::togglePaused()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase12togglePausedEv(
    QFutureWatcherBase *self) {
  self->togglePaused();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  void QFutureWatcherBase::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase13connectNotifyERK11QMetaMethod(
    QFutureWatcherBase *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  void QFutureWatcherBase::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase16disconnectNotifyERK11QMetaMethod(
    QFutureWatcherBase *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  void QFutureWatcherBase::connectOutputInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase22connectOutputInterfaceEv(
    QFutureWatcherBase *self) {
  self->connectOutputInterface();
}

//  void QFutureWatcherBase::disconnectOutputInterface(bool
//      pendingAssignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase25disconnectOutputInterfaceEb(
    QFutureWatcherBase *self,
    bool pendingAssignment) {
  self->disconnectOutputInterface(pendingAssignment);
}

//  const QFutureInterfaceBase &QFutureWatcherBase::futureInterface() const
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZNK18QFutureWatcherBase15futureInterfaceEv(
    const QFutureWatcherBase *self) {
  return new QFutureInterfaceBase(self->futureInterface());
}

//  QFutureInterfaceBase &QFutureWatcherBase::futureInterface()
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN18QFutureWatcherBase15futureInterfaceEv(
    QFutureWatcherBase *self) {
  return &(self->futureInterface());
}

//  bool QFutureWatcherBase::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QFutureWatcherBase5eventEP6QEvent(
    QFutureWatcherBase *self,
    QEvent *event) {
  return self->QFutureWatcherBase::event(event);
}

//  void QFutureWatcherBase::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFutureWatcherBase13connectNotifyERK11QMetaMethod(
    QFutureWatcherBase *self,
    const QMetaMethod *signal) {
  static_cast<OwnQFutureWatcherBase *>(self)->OwnQFutureWatcherBase::connectNotify(
      *signal);
}

//  void QFutureWatcherBase::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFutureWatcherBase16disconnectNotifyERK11QMetaMethod(
    QFutureWatcherBase *self,
    const QMetaMethod *signal) {
  static_cast<OwnQFutureWatcherBase *>(self)->OwnQFutureWatcherBase::disconnectNotify(
      *signal);
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
