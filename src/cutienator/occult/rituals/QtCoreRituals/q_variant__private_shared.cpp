//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qvariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVariant::PrivateShared::PrivateShared()
extern "C" Q_DECL_EXPORT
QVariant::PrivateShared *ritual_ZN8QVariant13PrivateSharedC1Ev() {
  return new QVariant::PrivateShared();
}

//  int QVariant::PrivateShared::computeOffset(PrivateShared *ps, size_t
//      align)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QVariant13PrivateShared13computeOffsetEPS0_m(
    QVariant::PrivateShared *ps,
    size_t align) {
  return QVariant::PrivateShared::computeOffset(ps, align);
}

//  PrivateShared *QVariant::PrivateShared::create(size_t size, size_t align)
extern "C" Q_DECL_EXPORT
QVariant::PrivateShared *ritual_ZN8QVariant13PrivateShared6createEmm(
    size_t size,
    size_t align) {
  return QVariant::PrivateShared::create(size, align);
}

//  void QVariant::PrivateShared::free(PrivateShared *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant13PrivateShared4freeEPS0_(
    QVariant::PrivateShared *p) {
  QVariant::PrivateShared::free(p);
}

//  QVariant::PrivateShared::~PrivateShared()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant13PrivateSharedD1Ev(QVariant::PrivateShared *self) {
  delete self;
}
