//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4util_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !defined(BROKEN_STD_VECTOR_BOOL_OR_BROKEN_STD_FIND)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4util_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::BitVector::BitVector(int size, bool value)
extern "C" Q_DECL_EXPORT
QV4::BitVector *ritual_ZN3QV49BitVectorC1Eib(int size, bool value) {
  return new QV4::BitVector(size, value);
}

//  void QV4::BitVector::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector5clearEv(QV4::BitVector *self) {
  self->clear();
}

//  void QV4::BitVector::reserve(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector7reserveEi(QV4::BitVector *self, int size) {
  self->reserve(size);
}

//  int QV4::BitVector::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV49BitVector4sizeEv(const QV4::BitVector *self) {
  return self->size();
}

//  void QV4::BitVector::resize(int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector6resizeEi(QV4::BitVector *self, int newSize) {
  self->resize(newSize);
}

//  void QV4::BitVector::resize(int newSize, bool newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector6resizeEib(
    QV4::BitVector *self,
    int newSize,
    bool newValue) {
  self->resize(newSize, newValue);
}

//  void QV4::BitVector::assign(int newSize, bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector6assignEib(
    QV4::BitVector *self,
    int newSize,
    bool value) {
  self->assign(newSize, value);
}

//  int QV4::BitVector::findNext(int start, bool value, bool wrapAround)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV49BitVector8findNextEibb(
    const QV4::BitVector *self,
    int start,
    bool value,
    bool wrapAround) {
  return self->findNext(start, value, wrapAround);
}

//  bool QV4::BitVector::at(int idx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49BitVector2atEi(const QV4::BitVector *self, int idx) {
  return self->at(idx);
}

//  void QV4::BitVector::setBit(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector6setBitEi(QV4::BitVector *self, int idx) {
  self->setBit(idx);
}

//  void QV4::BitVector::clearBit(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVector8clearBitEi(QV4::BitVector *self, int idx) {
  self->clearBit(idx);
}

//  QV4::BitVector::~BitVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49BitVectorD1Ev(QV4::BitVector *self) {
  delete self;
}

#endif  // !defined(BROKEN_STD_VECTOR_BOOL_OR_BROKEN_STD_FIND)
