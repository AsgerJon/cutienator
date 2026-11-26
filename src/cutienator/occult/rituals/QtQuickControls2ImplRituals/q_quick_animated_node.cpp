//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickanimatednode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickAnimatedNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimatedNode : QQuickAnimatedNode {
  using QQuickAnimatedNode::updateCurrentTime;
};

//  const QMetaObject *QQuickAnimatedNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickAnimatedNode10metaObjectEv(
    const QQuickAnimatedNode *self) {
  return self->metaObject();
}

//  void *QQuickAnimatedNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickAnimatedNode11qt_metacastEPKc(
    QQuickAnimatedNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnimatedNode::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickAnimatedNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnimatedNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAnimatedNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickAnimatedNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimatedNode::tr(s, c, n));
}

//  QQuickAnimatedNode::QQuickAnimatedNode(QQuickItem *target)
extern "C" Q_DECL_EXPORT
QQuickAnimatedNode *ritual_ZN18QQuickAnimatedNodeC1EP10QQuickItem(
    QQuickItem *target) {
  return new QQuickAnimatedNode(target);
}

//  bool QQuickAnimatedNode::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickAnimatedNode9isRunningEv(
    const QQuickAnimatedNode *self) {
  return self->isRunning();
}

//  int QQuickAnimatedNode::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickAnimatedNode11currentTimeEv(
    const QQuickAnimatedNode *self) {
  return self->currentTime();
}

//  void QQuickAnimatedNode::setCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode14setCurrentTimeEi(
    QQuickAnimatedNode *self,
    int time) {
  self->setCurrentTime(time);
}

//  int QQuickAnimatedNode::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickAnimatedNode8durationEv(
    const QQuickAnimatedNode *self) {
  return self->duration();
}

//  void QQuickAnimatedNode::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode11setDurationEi(
    QQuickAnimatedNode *self,
    int duration) {
  self->setDuration(duration);
}

//  int QQuickAnimatedNode::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickAnimatedNode9loopCountEv(
    const QQuickAnimatedNode *self) {
  return self->loopCount();
}

//  void QQuickAnimatedNode::setLoopCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode12setLoopCountEi(
    QQuickAnimatedNode *self,
    int count) {
  self->setLoopCount(count);
}

//  void QQuickAnimatedNode::sync(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode4syncEP10QQuickItem(
    QQuickAnimatedNode *self,
    QQuickItem *target) {
  self->sync(target);
}

//  QQuickWindow *QQuickAnimatedNode::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK18QQuickAnimatedNode6windowEv(
    const QQuickAnimatedNode *self) {
  return self->window();
}

//  void QQuickAnimatedNode::start(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode5startEi(
    QQuickAnimatedNode *self,
    int duration) {
  self->start(duration);
}

//  void QQuickAnimatedNode::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode7restartEv(QQuickAnimatedNode *self) {
  self->restart();
}

//  void QQuickAnimatedNode::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode4stopEv(QQuickAnimatedNode *self) {
  self->stop();
}

//  void QQuickAnimatedNode::started()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode7startedEv(QQuickAnimatedNode *self) {
  self->started();
}

//  void QQuickAnimatedNode::stopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode7stoppedEv(QQuickAnimatedNode *self) {
  self->stopped();
}

//  void QQuickAnimatedNode::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode17updateCurrentTimeEi(
    QQuickAnimatedNode *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QQuickAnimatedNode::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode7advanceEv(QQuickAnimatedNode *self) {
  self->advance();
}

//  void QQuickAnimatedNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickAnimatedNode6updateEv(QQuickAnimatedNode *self) {
  self->update();
}

//  QQuickAnimatedNode as the QSGTransformNode it is built on
extern "C" Q_DECL_EXPORT
QSGTransformNode *ritual_cast_QQuickAnimatedNode_QSGTransformNode(
    QQuickAnimatedNode *self) {
  return static_cast<QSGTransformNode *>(self);
}

//  void QQuickAnimatedNode::sync(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickAnimatedNode4syncEP10QQuickItem(
    QQuickAnimatedNode *self,
    QQuickItem *target) {
  self->QQuickAnimatedNode::sync(target);
}

//  void QQuickAnimatedNode::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickAnimatedNode17updateCurrentTimeEi(
    QQuickAnimatedNode *self,
    int time) {
  static_cast<OwnQQuickAnimatedNode *>(self)->OwnQQuickAnimatedNode::updateCurrentTime(
      time);
}
