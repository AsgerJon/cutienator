//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qnodevisitor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qnodevisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::QNodeVisitor::QNodeVisitor()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeVisitor *ritual_ZN8Qt3DCore12QNodeVisitorC1Ev() {
  return new Qt3DCore::QNodeVisitor();
}

//  Qt3DCore::QNodeVisitor::~QNodeVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodeVisitorD1Ev(Qt3DCore::QNodeVisitor *self) {
  delete self;
}

//  QNode *Qt3DCore::QNodeVisitor::rootNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore12QNodeVisitor8rootNodeEv(
    const Qt3DCore::QNodeVisitor *self) {
  return self->rootNode();
}

//  QNode *Qt3DCore::QNodeVisitor::currentNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore12QNodeVisitor11currentNodeEv(
    const Qt3DCore::QNodeVisitor *self) {
  return self->currentNode();
}

//  void Qt3DCore::QNodeVisitor::setPath(QNodeVector path)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodeVisitor7setPathE5QListIPNS_5QNodeEE(
    Qt3DCore::QNodeVisitor *self,
    const Qt3DCore::QNodeVector *path) {
  self->setPath(*path);
}

//  QNodeVector Qt3DCore::QNodeVisitor::path() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeVector *ritual_ZNK8Qt3DCore12QNodeVisitor4pathEv(
    const Qt3DCore::QNodeVisitor *self) {
  return new Qt3DCore::QNodeVector(self->path());
}

//  void Qt3DCore::QNodeVisitor::append(QNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodeVisitor6appendEPNS_5QNodeE(
    Qt3DCore::QNodeVisitor *self,
    Qt3DCore::QNode *n) {
  self->append(n);
}

//  void Qt3DCore::QNodeVisitor::pop_back()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodeVisitor8pop_backEv(
    Qt3DCore::QNodeVisitor *self) {
  self->pop_back();
}

//  a Qt3DCore::QNodeVector a ritual of Qt3DCore::QNodeVisitor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QNodeVisitor__Qt3DCore_QNodeVector(
    Qt3DCore::QNodeVector *self) {
  delete self;
}
