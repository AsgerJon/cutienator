//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(QObject *target)
extern "C" Q_DECL_EXPORT
RequiredPropertiesAndTarget *ritual_ZN27RequiredPropertiesAndTargetC1EP7QObject(
    QObject *target) {
  return new RequiredPropertiesAndTarget(target);
}

//  RequiredPropertiesAndTarget::RequiredPropertiesAndTarget(const
//      RequiredPropertiesAndTarget &a0)
extern "C" Q_DECL_EXPORT
RequiredPropertiesAndTarget *ritual_ZN27RequiredPropertiesAndTargetC1ERKS_(
    const RequiredPropertiesAndTarget *a0) {
  return new RequiredPropertiesAndTarget(*a0);
}

//  RequiredPropertiesAndTarget::~RequiredPropertiesAndTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN27RequiredPropertiesAndTargetD1Ev(
    RequiredPropertiesAndTarget *self) {
  delete self;
}
