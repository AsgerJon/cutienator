//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGDefaultInternalRectangleNode::QSGDefaultInternalRectangleNode()
extern "C" Q_DECL_EXPORT
QSGDefaultInternalRectangleNode *ritual_ZN31QSGDefaultInternalRectangleNodeC1Ev() {
  return new QSGDefaultInternalRectangleNode();
}

//  void QSGDefaultInternalRectangleNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGDefaultInternalRectangleNode26updateMaterialAntialiasingEv(
    QSGDefaultInternalRectangleNode *self) {
  self->updateMaterialAntialiasing();
}

//  void QSGDefaultInternalRectangleNode::updateMaterialBlending(QSGNode::Dir
//      tyState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGDefaultInternalRectangleNode22updateMaterialBlendingEP6QFlagsIN7QSGNode13DirtyStateBitEE(
    QSGDefaultInternalRectangleNode *self,
    QSGNode::DirtyState *state) {
  self->updateMaterialBlending(state);
}

//  void QSGDefaultInternalRectangleNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QSGDefaultInternalRectangleNode26updateMaterialAntialiasingEv(
    QSGDefaultInternalRectangleNode *self) {
  self->QSGDefaultInternalRectangleNode::updateMaterialAntialiasing();
}

//  void QSGDefaultInternalRectangleNode::updateMaterialBlending(QSGNode::Dir
//      tyState *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QSGDefaultInternalRectangleNode22updateMaterialBlendingEP6QFlagsIN7QSGNode13DirtyStateBitEE(
    QSGDefaultInternalRectangleNode *self,
    QSGNode::DirtyState *state) {
  self->QSGDefaultInternalRectangleNode::updateMaterialBlending(state);
}
