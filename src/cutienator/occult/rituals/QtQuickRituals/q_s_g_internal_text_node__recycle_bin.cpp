//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsginternaltextnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsginternaltextnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGInternalTextNode::RecycleBin::RecycleBin()
extern "C" Q_DECL_EXPORT
QSGInternalTextNode::RecycleBin *ritual_ZN19QSGInternalTextNode10RecycleBinC1Ev() {
  return new QSGInternalTextNode::RecycleBin();
}

//  QSGInternalTextNode::RecycleBin::~RecycleBin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode10RecycleBinD1Ev(
    QSGInternalTextNode::RecycleBin *self) {
  delete self;
}

//  QSGVisitableNode
//      *QSGInternalTextNode::RecycleBin::takeNextReusableNode(NodeType type)
extern "C" Q_DECL_EXPORT
QSGVisitableNode *ritual_ZN19QSGInternalTextNode10RecycleBin20takeNextReusableNodeENS0_8NodeTypeE(
    QSGInternalTextNode::RecycleBin *self,
    QSGInternalTextNode::RecycleBin::NodeType type) {
  return self->takeNextReusableNode(type);
}

//  void QSGInternalTextNode::RecycleBin::stopReusing()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode10RecycleBin11stopReusingEv(
    QSGInternalTextNode::RecycleBin *self) {
  self->stopReusing();
}

//  const UnusedNode
//      *QSGInternalTextNode::RecycleBin::peekNextReusableNode(NodeType type)
extern "C" Q_DECL_EXPORT
const QSGInternalTextNode::RecycleBin::UnusedNode *ritual_ZN19QSGInternalTextNode10RecycleBin20peekNextReusableNodeENS0_8NodeTypeE(
    QSGInternalTextNode::RecycleBin *self,
    QSGInternalTextNode::RecycleBin::NodeType type) {
  return self->peekNextReusableNode(type);
}
