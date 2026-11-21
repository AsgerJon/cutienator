//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcollator.h>

//  QCollatorSortKey::QCollatorSortKey(const QCollatorSortKey &other)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorSortKeyC1ERKS_(
    const QCollatorSortKey *other) {
  return new QCollatorSortKey(*other);
}

//  QCollatorSortKey::~QCollatorSortKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCollatorSortKeyD1Ev(QCollatorSortKey *self) {
  delete self;
}

//  int QCollatorSortKey::compare(const QCollatorSortKey &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCollatorSortKey7compareERKS_(
    const QCollatorSortKey *self,
    const QCollatorSortKey *key) {
  return self->compare(*key);
}
