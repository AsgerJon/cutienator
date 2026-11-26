//  Written by dev_tooling.RitualGenerator from the records of QtQuickTimelin
//  eBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendtreenode_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickTimelineBlendTrees/QtQuickTimelineBlendTrees>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendtreenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QBlendTreeNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QBlendTreeNode10metaObjectEv(
    const QBlendTreeNode *self) {
  return self->metaObject();
}

//  void *QBlendTreeNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QBlendTreeNode11qt_metacastEPKc(
    QBlendTreeNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBlendTreeNode::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QBlendTreeNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QBlendTreeNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBlendTreeNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBlendTreeNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBlendTreeNode::tr(s, c, n));
}

//  void QBlendTreeNode::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBlendTreeNode24qt_qmlMarker_uncreatableEv(
    QBlendTreeNode *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QBlendTreeNode::QBlendTreeNode(QObject *parent)
extern "C" Q_DECL_EXPORT
QBlendTreeNode *ritual_ZN14QBlendTreeNodeC1EP7QObject(QObject *parent) {
  return new QBlendTreeNode(parent);
}

//  const QHash<QQmlProperty, QVariant> &QBlendTreeNode::frameData()
extern "C" Q_DECL_EXPORT
const QHash<QQmlProperty, QVariant> *ritual_ZN14QBlendTreeNode9frameDataEv(
    QBlendTreeNode *self) {
  return &(self->frameData());
}

//  bool QBlendTreeNode::outputEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBlendTreeNode13outputEnabledEv(
    const QBlendTreeNode *self) {
  return self->outputEnabled();
}

//  void QBlendTreeNode::setOutputEnabled(bool isOutputEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBlendTreeNode16setOutputEnabledEb(
    QBlendTreeNode *self,
    bool isOutputEnabled) {
  self->setOutputEnabled(isOutputEnabled);
}

//  void QBlendTreeNode::frameDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBlendTreeNode16frameDataChangedEv(QBlendTreeNode *self) {
  self->frameDataChanged();
}

//  void QBlendTreeNode::outputEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBlendTreeNode20outputEnabledChangedEv(
    QBlendTreeNode *self) {
  self->outputEnabledChanged();
}

//  void QBlendTreeNode::handleFrameDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBlendTreeNode22handleFrameDataChangedEv(
    QBlendTreeNode *self) {
  self->handleFrameDataChanged();
}
