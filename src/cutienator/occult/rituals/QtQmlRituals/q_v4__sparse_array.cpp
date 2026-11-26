//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
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
//  -----------------------------------------------------------------------

//  QV4::SparseArray::SparseArray()
extern "C" Q_DECL_EXPORT
QV4::SparseArray *ritual_ZN3QV411SparseArrayC1Ev() {
  return new QV4::SparseArray();
}

//  QV4::SparseArray::~SparseArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArrayD1Ev(QV4::SparseArray *self) {
  delete self;
}

//  QV4::SparseArray::SparseArray(const SparseArray &other)
extern "C" Q_DECL_EXPORT
QV4::SparseArray *ritual_ZN3QV411SparseArrayC1ERKS0_(
    const QV4::SparseArray *other) {
  return new QV4::SparseArray(*other);
}

//  void QV4::SparseArray::rotateLeft(SparseArrayNode *x)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray10rotateLeftEPNS_15SparseArrayNodeE(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *x) {
  self->rotateLeft(x);
}

//  void QV4::SparseArray::rotateRight(SparseArrayNode *x)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray11rotateRightEPNS_15SparseArrayNodeE(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *x) {
  self->rotateRight(x);
}

//  void QV4::SparseArray::rebalance(SparseArrayNode *x)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray9rebalanceEPNS_15SparseArrayNodeE(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *x) {
  self->rebalance(x);
}

//  void QV4::SparseArray::recalcMostLeftNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray18recalcMostLeftNodeEv(
    QV4::SparseArray *self) {
  self->recalcMostLeftNode();
}

//  SparseArrayNode *QV4::SparseArray::root() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray4rootEv(
    const QV4::SparseArray *self) {
  return self->root();
}

//  void QV4::SparseArray::deleteNode(SparseArrayNode *z)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray10deleteNodeEPNS_15SparseArrayNodeE(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *z) {
  self->deleteNode(z);
}

//  SparseArrayNode *QV4::SparseArray::createNode(uint sl, SparseArrayNode
//      *parent, bool left)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray10createNodeEjPNS_15SparseArrayNodeEb(
    QV4::SparseArray *self,
    uint sl,
    QV4::SparseArrayNode *parent,
    bool left) {
  return self->createNode(sl, parent, left);
}

//  void QV4::SparseArray::freeTree(SparseArrayNode *root, int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray8freeTreeEPNS_15SparseArrayNodeEi(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *root,
    int alignment) {
  self->freeTree(root, alignment);
}

//  SparseArrayNode *QV4::SparseArray::findNode(uint akey) const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray8findNodeEj(
    const QV4::SparseArray *self,
    uint akey) {
  return self->findNode(akey);
}

//  uint QV4::SparseArray::nEntries() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV411SparseArray8nEntriesEv(const QV4::SparseArray *self) {
  return self->nEntries();
}

//  uint QV4::SparseArray::pop_front()
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV411SparseArray9pop_frontEv(QV4::SparseArray *self) {
  return self->pop_front();
}

//  void QV4::SparseArray::push_front(uint at)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray10push_frontEj(
    QV4::SparseArray *self,
    uint at) {
  self->push_front(at);
}

//  uint QV4::SparseArray::pop_back(uint len)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV411SparseArray8pop_backEj(
    QV4::SparseArray *self,
    uint len) {
  return self->pop_back(len);
}

//  void QV4::SparseArray::push_back(uint at, uint len)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArray9push_backEjj(
    QV4::SparseArray *self,
    uint at,
    uint len) {
  self->push_back(at, len);
}

//  QList<int> QV4::SparseArray::keys() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK3QV411SparseArray4keysEv(
    const QV4::SparseArray *self) {
  return new QList<int>(self->keys());
}

//  const SparseArrayNode *QV4::SparseArray::end() const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray3endEv(
    const QV4::SparseArray *self) {
  return self->end();
}

//  SparseArrayNode *QV4::SparseArray::end()
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray3endEv(
    QV4::SparseArray *self) {
  return self->end();
}

//  const SparseArrayNode *QV4::SparseArray::begin() const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray5beginEv(
    const QV4::SparseArray *self) {
  return self->begin();
}

//  SparseArrayNode *QV4::SparseArray::begin()
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray5beginEv(
    QV4::SparseArray *self) {
  return self->begin();
}

//  SparseArrayNode *QV4::SparseArray::erase(SparseArrayNode *n)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray5eraseEPNS_15SparseArrayNodeE(
    QV4::SparseArray *self,
    QV4::SparseArrayNode *n) {
  return self->erase(n);
}

//  SparseArrayNode *QV4::SparseArray::lowerBound(uint key)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray10lowerBoundEj(
    QV4::SparseArray *self,
    uint key) {
  return self->lowerBound(key);
}

//  const SparseArrayNode *QV4::SparseArray::lowerBound(uint key) const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray10lowerBoundEj(
    const QV4::SparseArray *self,
    uint key) {
  return self->lowerBound(key);
}

//  SparseArrayNode *QV4::SparseArray::upperBound(uint key)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray10upperBoundEj(
    QV4::SparseArray *self,
    uint key) {
  return self->upperBound(key);
}

//  const SparseArrayNode *QV4::SparseArray::upperBound(uint key) const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray10upperBoundEj(
    const QV4::SparseArray *self,
    uint key) {
  return self->upperBound(key);
}

//  SparseArrayNode *QV4::SparseArray::insert(uint akey)
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZN3QV411SparseArray6insertEj(
    QV4::SparseArray *self,
    uint akey) {
  return self->insert(akey);
}

//  a QList<int> a ritual of QV4::SparseArray gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_SparseArray__QList_int(QList<int> *self) {
  delete self;
}
