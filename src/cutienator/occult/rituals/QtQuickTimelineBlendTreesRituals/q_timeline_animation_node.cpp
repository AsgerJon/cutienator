//  Written by dev_tooling.RitualGenerator from the records of QtQuickTimelin
//  eBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qtimelineanimationno
//  de_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickTimelineBlendTrees/QtQuickTimelineBlendTrees>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qtimelineanimationnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QTimelineAnimationNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QTimelineAnimationNode10metaObjectEv(
    const QTimelineAnimationNode *self) {
  return self->metaObject();
}

//  QString QTimelineAnimationNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QTimelineAnimationNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTimelineAnimationNode::tr(s, c, n));
}

//  QTimelineAnimationNode::QTimelineAnimationNode(QObject *parent)
extern "C" Q_DECL_EXPORT
QTimelineAnimationNode *ritual_ZN22QTimelineAnimationNodeC1EP7QObject(
    QObject *parent) {
  return new QTimelineAnimationNode(parent);
}

//  QQuickTimelineAnimation *QTimelineAnimationNode::animation() const
extern "C" Q_DECL_EXPORT
QQuickTimelineAnimation *ritual_ZNK22QTimelineAnimationNode9animationEv(
    const QTimelineAnimationNode *self) {
  return self->animation();
}

//  void QTimelineAnimationNode::setAnimation(QQuickTimelineAnimation
//      *newAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTimelineAnimationNode12setAnimationEP23QQuickTimelineAnimation(
    QTimelineAnimationNode *self,
    QQuickTimelineAnimation *newAnimation) {
  self->setAnimation(newAnimation);
}

//  QQuickTimeline *QTimelineAnimationNode::timeline() const
extern "C" Q_DECL_EXPORT
QQuickTimeline *ritual_ZNK22QTimelineAnimationNode8timelineEv(
    const QTimelineAnimationNode *self) {
  return self->timeline();
}

//  void QTimelineAnimationNode::setTimeline(QQuickTimeline *newTimeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTimelineAnimationNode11setTimelineEP14QQuickTimeline(
    QTimelineAnimationNode *self,
    QQuickTimeline *newTimeline) {
  self->setTimeline(newTimeline);
}

//  qreal QTimelineAnimationNode::currentFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QTimelineAnimationNode12currentFrameEv(
    const QTimelineAnimationNode *self) {
  return self->currentFrame();
}

//  void QTimelineAnimationNode::setCurrentFrame(qreal newCurrentFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTimelineAnimationNode15setCurrentFrameEd(
    QTimelineAnimationNode *self,
    qreal newCurrentFrame) {
  self->setCurrentFrame(newCurrentFrame);
}

//  void QTimelineAnimationNode::updateFrameData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTimelineAnimationNode15updateFrameDataEv(
    QTimelineAnimationNode *self) {
  self->updateFrameData();
}

//  void QTimelineAnimationNode::updateAnimationTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTimelineAnimationNode21updateAnimationTargetEv(
    QTimelineAnimationNode *self) {
  self->updateAnimationTarget();
}
