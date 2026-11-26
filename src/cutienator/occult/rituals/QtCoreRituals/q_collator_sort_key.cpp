//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcollator.h>

//  QCollatorSortKey::QCollatorSortKey(const QCollatorSortKey &other)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyC1ERKS_(
    const QCollatorSortKey *other) {
  return new QCollatorSortKey(*other);
}

//  QCollatorSortKey::QCollatorSortKey(QCollatorSortKey &&other)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyC1EOS_(
    QCollatorSortKey *other) {
  return new QCollatorSortKey(std::move(*other));
}

//  QCollatorSortKey::~QCollatorSortKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCollatorSortKeyD1Ev(QCollatorSortKey *self) {
  delete self;
}

//  QCollatorSortKey &QCollatorSortKey::operator=(const QCollatorSortKey
//      &other)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyaSERKS_(
    QCollatorSortKey *self,
    const QCollatorSortKey *other) {
  return &(self->operator=(*other));
}

//  QCollatorSortKey &QCollatorSortKey::operator=(QCollatorSortKey &&other)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyaSEOS_(
    QCollatorSortKey *self,
    QCollatorSortKey *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCollatorSortKey::swap(QCollatorSortKey &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCollatorSortKey4swapERS_(
    QCollatorSortKey *self,
    QCollatorSortKey *other) {
  self->swap(*other);
}

//  int QCollatorSortKey::compare(const QCollatorSortKey &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCollatorSortKey7compareERKS_(
    const QCollatorSortKey *self,
    const QCollatorSortKey *key) {
  return self->compare(*key);
}

//  QCollatorSortKey::QCollatorSortKey(QCollatorSortKeyPrivate *a0)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyC1EP23QCollatorSortKeyPrivate(
    QCollatorSortKeyPrivate *a0) {
  return new QCollatorSortKey(a0);
}

//  bool operator==(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCollatorSortKey &lhs, const QCollatorSortKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK16QCollatorSortKeyS1_(
    const QCollatorSortKey *lhs,
    const QCollatorSortKey *rhs) {
  return operator>=(*lhs, *rhs);
}
