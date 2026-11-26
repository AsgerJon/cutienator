//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlPropertyCache::ConstPtr::ConstPtr(const Ptr &ptr)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN17QQmlPropertyCache8ConstPtrC1ERK14QQmlRefPointerIS_E(
    const QQmlPropertyCache::Ptr *ptr) {
  return new QQmlPropertyCache::ConstPtr(*ptr);
}

//  QQmlPropertyCache::ConstPtr::ConstPtr(Ptr &&ptr)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN17QQmlPropertyCache8ConstPtrC1EO14QQmlRefPointerIS_E(
    QQmlPropertyCache::Ptr *ptr) {
  return new QQmlPropertyCache::ConstPtr(std::move(*ptr));
}

//  ConstPtr &QQmlPropertyCache::ConstPtr::operator=(const Ptr &ptr)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN17QQmlPropertyCache8ConstPtraSERK14QQmlRefPointerIS_E(
    QQmlPropertyCache::ConstPtr *self,
    const QQmlPropertyCache::Ptr *ptr) {
  return &(self->operator=(*ptr));
}

//  ConstPtr &QQmlPropertyCache::ConstPtr::operator=(Ptr &&ptr)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN17QQmlPropertyCache8ConstPtraSEO14QQmlRefPointerIS_E(
    QQmlPropertyCache::ConstPtr *self,
    QQmlPropertyCache::Ptr *ptr) {
  return &(self->operator=(std::move(*ptr)));
}

//  QQmlPropertyCache::ConstPtr::~ConstPtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache8ConstPtrD1Ev(
    QQmlPropertyCache::ConstPtr *self) {
  delete self;
}
