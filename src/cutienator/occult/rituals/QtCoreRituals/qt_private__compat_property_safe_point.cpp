//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtPrivate::CompatPropertySafePoint::CompatPropertySafePoint(QBindingStatu
//      s *status, QUntypedPropertyData *property)
extern "C" Q_DECL_EXPORT
QtPrivate::CompatPropertySafePoint *ritual_ZN9QtPrivate23CompatPropertySafePointC1EP14QBindingStatusP20QUntypedPropertyData(
    QBindingStatus *status,
    QUntypedPropertyData *property) {
  return new QtPrivate::CompatPropertySafePoint(status, property);
}

//  QtPrivate::CompatPropertySafePoint::~CompatPropertySafePoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate23CompatPropertySafePointD1Ev(
    QtPrivate::CompatPropertySafePoint *self) {
  delete self;
}
