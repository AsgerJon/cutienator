//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4sparsearray_p.h>
#include <stdlib.h>
#ifdef QT_QMAP_DEBUG
# include <QtCore/qstring.h>
# include <QtCore/qvector.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4sparsearray.cpp, line 15, as _ZNK3QV415SparseArrayNode8nextNodeEv
namespace QV4 {
inline const SparseArrayNode *SparseArrayNode::nextNode() const
{
    const SparseArrayNode *n = this;
    if (n->right) {
        n = n->right;
        while (n->left)
            n = n->left;
    } else {
        const SparseArrayNode *y = n->parent();
        while (y && n == y->right) {
            n = y;
            y = n->parent();
        }
        n = y;
    }
    return n;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sparsearray.cpp, line 33, as _ZNK3QV415SparseArrayNode12previousNodeEv
namespace QV4 {
inline const SparseArrayNode *SparseArrayNode::previousNode() const
{
    const SparseArrayNode *n = this;
    if (n->left) {
        n = n->left;
        while (n->right)
            n = n->right;
    } else {
        const SparseArrayNode *y = n->parent();
        while (y && n == y->left) {
            n = y;
            y = n->parent();
        }
        n = y;
    }
    return n;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sparsearray.cpp, line 51, as _ZNK3QV415SparseArrayNode4copyEPNS_11SparseArrayE
namespace QV4 {
inline SparseArrayNode *SparseArrayNode::copy(SparseArray *d) const
{
    SparseArrayNode *n = d->createNode(size_left, nullptr, false);
    n->value = value;
    n->setColor(color());
    if (left) {
        n->left = left->copy(d);
        n->left->setParent(n);
    } else {
        n->left = nullptr;
    }
    if (right) {
        n->right = right->copy(d);
        n->right->setParent(n);
    } else {
        n->right = nullptr;
    }
    return n;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const SparseArrayNode *QV4::SparseArrayNode::nextNode() const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV415SparseArrayNode8nextNodeEv(
    const QV4::SparseArrayNode *self) {
  return self->nextNode();
}

//  SparseArrayNode *QV4::SparseArrayNode::nextNode()
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV415SparseArrayNode8nextNodeEv(
    QV4::SparseArrayNode *self) {
  return self->nextNode();
}

//  const SparseArrayNode *QV4::SparseArrayNode::previousNode() const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV415SparseArrayNode12previousNodeEv(
    const QV4::SparseArrayNode *self) {
  return self->previousNode();
}

//  SparseArrayNode *QV4::SparseArrayNode::previousNode()
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV415SparseArrayNode12previousNodeEv(
    QV4::SparseArrayNode *self) {
  return self->previousNode();
}

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

//  SparseArrayNode *QV4::SparseArrayNode::copy(SparseArray *d) const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV415SparseArrayNode4copyEPNS_11SparseArrayE(
    const QV4::SparseArrayNode *self,
    QV4::SparseArray *d) {
  return self->copy(d);
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
