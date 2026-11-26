//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltype_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Ptr QQmlType::SingletonInstanceInfo::create()
extern "C" Q_DECL_EXPORT
QQmlType::SingletonInstanceInfo::Ptr *ritual_ZN8QQmlType21SingletonInstanceInfo6createEv() {
  return new QQmlType::SingletonInstanceInfo::Ptr(
      QQmlType::SingletonInstanceInfo::create());
}

//  QQmlType::SingletonInstanceInfo::SingletonInstanceInfo()
extern "C" Q_DECL_EXPORT
QQmlType::SingletonInstanceInfo *ritual_ZN8QQmlType21SingletonInstanceInfoC1Ev() {
  return new QQmlType::SingletonInstanceInfo();
}

//  a QQmlType::SingletonInstanceInfo::Ptr a ritual of
//      QQmlType::SingletonInstanceInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlType_SingletonInstanceInfo__QQmlType_SingletonInstanceInfo_Ptr(
    QQmlType::SingletonInstanceInfo::Ptr *self) {
  delete self;
}
