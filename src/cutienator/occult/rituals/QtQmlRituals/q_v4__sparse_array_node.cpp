//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Color QV4::SparseArrayNode::color() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode::Color ritual_ZNK3QV415SparseArrayNode5colorEv(
    const QV4::SparseArrayNode *self) {
  return self->color();
}

//  void QV4::SparseArrayNode::setColor(Color c)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayNode8setColorENS0_5ColorE(
    QV4::SparseArrayNode *self,
    QV4::SparseArrayNode::Color c) {
  self->setColor(c);
}

//  SparseArrayNode *QV4::SparseArrayNode::parent() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV415SparseArrayNode6parentEv(
    const QV4::SparseArrayNode *self) {
  return self->parent();
}

//  void QV4::SparseArrayNode::setParent(SparseArrayNode *pp)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayNode9setParentEPS0_(
    QV4::SparseArrayNode *self,
    QV4::SparseArrayNode *pp) {
  self->setParent(pp);
}

//  uint QV4::SparseArrayNode::key() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SparseArrayNode3keyEv(
    const QV4::SparseArrayNode *self) {
  return self->key();
}

//  SparseArrayNode *QV4::SparseArrayNode::lowerBound(uint key)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV415SparseArrayNode10lowerBoundEj(
    QV4::SparseArrayNode *self,
    uint key) {
  return self->lowerBound(key);
}

//  SparseArrayNode *QV4::SparseArrayNode::upperBound(uint key)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV415SparseArrayNode10upperBoundEj(
    QV4::SparseArrayNode *self,
    uint key) {
  return self->upperBound(key);
}

//  QV4::SparseArrayNode::~SparseArrayNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayNodeD1Ev(QV4::SparseArrayNode *self) {
  delete self;
}
