//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::SparseArray::~SparseArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411SparseArrayD1Ev(QV4::SparseArray *self) {
  delete self;
}

//  SparseArrayNode *QV4::SparseArray::root() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV411SparseArray4rootEv(
    const QV4::SparseArray *self) {
  return self->root();
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
