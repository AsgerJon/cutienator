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

//  QString QQuickFrameAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickFrameAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFrameAnimation::tr(s, c, n));
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
