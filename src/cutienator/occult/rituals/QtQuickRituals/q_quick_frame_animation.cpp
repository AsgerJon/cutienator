//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickframeanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickframeanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickFrameAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFrameAnimation : QQuickFrameAnimation {
  using QQuickFrameAnimation::classBegin;
  using QQuickFrameAnimation::componentComplete;
};

//  const QMetaObject *QQuickFrameAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickFrameAnimation10metaObjectEv(
    const QQuickFrameAnimation *self) {
  return self->metaObject();
}

//  void *QQuickFrameAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickFrameAnimation11qt_metacastEPKc(
    QQuickFrameAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFrameAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickFrameAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFrameAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFrameAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickFrameAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFrameAnimation::tr(s, c, n));
}

//  QQuickFrameAnimationPrivate *QQuickFrameAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickFrameAnimationPrivate *ritual_ZN20QQuickFrameAnimation6d_funcEv(
    QQuickFrameAnimation *self) {
  return self->d_func();
}

//  const QQuickFrameAnimationPrivate *QQuickFrameAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFrameAnimationPrivate *ritual_ZNK20QQuickFrameAnimation6d_funcEv(
    const QQuickFrameAnimation *self) {
  return self->d_func();
}

//  QQuickFrameAnimation::QQuickFrameAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFrameAnimation *ritual_ZN20QQuickFrameAnimationC1EP7QObject(
    QObject *parent) {
  return new QQuickFrameAnimation(parent);
}

//  bool QQuickFrameAnimation::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickFrameAnimation9isRunningEv(
    const QQuickFrameAnimation *self) {
  return self->isRunning();
}

//  void QQuickFrameAnimation::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation10setRunningEb(
    QQuickFrameAnimation *self,
    bool running) {
  self->setRunning(running);
}

//  bool QQuickFrameAnimation::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickFrameAnimation8isPausedEv(
    const QQuickFrameAnimation *self) {
  return self->isPaused();
}

//  void QQuickFrameAnimation::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation9setPausedEb(
    QQuickFrameAnimation *self,
    bool paused) {
  self->setPaused(paused);
}

//  int QQuickFrameAnimation::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickFrameAnimation12currentFrameEv(
    const QQuickFrameAnimation *self) {
  return self->currentFrame();
}

//  qreal QQuickFrameAnimation::frameTime() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickFrameAnimation9frameTimeEv(
    const QQuickFrameAnimation *self) {
  return self->frameTime();
}

//  qreal QQuickFrameAnimation::smoothFrameTime() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickFrameAnimation15smoothFrameTimeEv(
    const QQuickFrameAnimation *self) {
  return self->smoothFrameTime();
}

//  qreal QQuickFrameAnimation::elapsedTime() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickFrameAnimation11elapsedTimeEv(
    const QQuickFrameAnimation *self) {
  return self->elapsedTime();
}

//  void QQuickFrameAnimation::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation10classBeginEv(
    QQuickFrameAnimation *self) {
  self->classBegin();
}

//  void QQuickFrameAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation17componentCompleteEv(
    QQuickFrameAnimation *self) {
  self->componentComplete();
}

//  void QQuickFrameAnimation::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation5startEv(QQuickFrameAnimation *self) {
  self->start();
}

//  void QQuickFrameAnimation::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation4stopEv(QQuickFrameAnimation *self) {
  self->stop();
}

//  void QQuickFrameAnimation::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation7restartEv(QQuickFrameAnimation *self) {
  self->restart();
}

//  void QQuickFrameAnimation::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation5pauseEv(QQuickFrameAnimation *self) {
  self->pause();
}

//  void QQuickFrameAnimation::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation6resumeEv(QQuickFrameAnimation *self) {
  self->resume();
}

//  void QQuickFrameAnimation::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation5resetEv(QQuickFrameAnimation *self) {
  self->reset();
}

//  void QQuickFrameAnimation::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation9triggeredEv(
    QQuickFrameAnimation *self) {
  self->triggered();
}

//  void QQuickFrameAnimation::runningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation14runningChangedEv(
    QQuickFrameAnimation *self) {
  self->runningChanged();
}

//  void QQuickFrameAnimation::pausedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation13pausedChangedEv(
    QQuickFrameAnimation *self) {
  self->pausedChanged();
}

//  void QQuickFrameAnimation::currentFrameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation19currentFrameChangedEv(
    QQuickFrameAnimation *self) {
  self->currentFrameChanged();
}

//  void QQuickFrameAnimation::frameTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation16frameTimeChangedEv(
    QQuickFrameAnimation *self) {
  self->frameTimeChanged();
}

//  void QQuickFrameAnimation::smoothFrameTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation22smoothFrameTimeChangedEv(
    QQuickFrameAnimation *self) {
  self->smoothFrameTimeChanged();
}

//  void QQuickFrameAnimation::elapsedTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation18elapsedTimeChangedEv(
    QQuickFrameAnimation *self) {
  self->elapsedTimeChanged();
}

//  void QQuickFrameAnimation::setCurrentFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation15setCurrentFrameEi(
    QQuickFrameAnimation *self,
    int frame) {
  self->setCurrentFrame(frame);
}

//  void QQuickFrameAnimation::setElapsedTime(qreal elapsedTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFrameAnimation14setElapsedTimeEd(
    QQuickFrameAnimation *self,
    qreal elapsedTime) {
  self->setElapsedTime(elapsedTime);
}

//  QQuickFrameAnimation as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickFrameAnimation_QQmlParserStatus(
    QQuickFrameAnimation *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQuickFrameAnimation::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFrameAnimation10classBeginEv(
    QQuickFrameAnimation *self) {
  static_cast<OwnQQuickFrameAnimation *>(self)->OwnQQuickFrameAnimation::classBegin();
}

//  void QQuickFrameAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFrameAnimation17componentCompleteEv(
    QQuickFrameAnimation *self) {
  static_cast<OwnQQuickFrameAnimation *>(self)->OwnQQuickFrameAnimation::componentComplete();
}
