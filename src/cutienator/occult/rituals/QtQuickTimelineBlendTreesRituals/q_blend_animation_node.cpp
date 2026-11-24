//  Written by dev_tooling.RitualGenerator from the records of QtQuickTimelin
//  eBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendanimationnode_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickTimelineBlendTrees/QtQuickTimelineBlendTrees>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendanimationnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QBlendAnimationNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QBlendAnimationNode10metaObjectEv(
    const QBlendAnimationNode *self) {
  return self->metaObject();
}

//  QString QBlendAnimationNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QBlendAnimationNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBlendAnimationNode::tr(s, c, n));
}

//  QBlendAnimationNode::QBlendAnimationNode(QObject *parent)
extern "C" Q_DECL_EXPORT
QBlendAnimationNode *ritual_ZN19QBlendAnimationNodeC1EP7QObject(
    QObject *parent) {
  return new QBlendAnimationNode(parent);
}

//  QBlendTreeNode *QBlendAnimationNode::source1() const
extern "C" Q_DECL_EXPORT
QBlendTreeNode *ritual_ZNK19QBlendAnimationNode7source1Ev(
    const QBlendAnimationNode *self) {
  return self->source1();
}

//  void QBlendAnimationNode::setSource1(QBlendTreeNode *newSource1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlendAnimationNode10setSource1EP14QBlendTreeNode(
    QBlendAnimationNode *self,
    QBlendTreeNode *newSource1) {
  self->setSource1(newSource1);
}

//  QBlendTreeNode *QBlendAnimationNode::source2() const
extern "C" Q_DECL_EXPORT
QBlendTreeNode *ritual_ZNK19QBlendAnimationNode7source2Ev(
    const QBlendAnimationNode *self) {
  return self->source2();
}

//  void QBlendAnimationNode::setSource2(QBlendTreeNode *newSource2)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlendAnimationNode10setSource2EP14QBlendTreeNode(
    QBlendAnimationNode *self,
    QBlendTreeNode *newSource2) {
  self->setSource2(newSource2);
}

//  qreal QBlendAnimationNode::weight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QBlendAnimationNode6weightEv(
    const QBlendAnimationNode *self) {
  return self->weight();
}

//  void QBlendAnimationNode::setWeight(qreal newWeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlendAnimationNode9setWeightEd(
    QBlendAnimationNode *self,
    qreal newWeight) {
  self->setWeight(newWeight);
}

//  void QBlendAnimationNode::handleInputFrameDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlendAnimationNode27handleInputFrameDataChangedEv(
    QBlendAnimationNode *self) {
  self->handleInputFrameDataChanged();
}
