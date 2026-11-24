//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetatype_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetatype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QtPrivate::QMetaTypeInterface
//      *QMetaTypeModuleHelper::interfaceForType_dummy(int a0)
extern "C" Q_DECL_EXPORT
const QtPrivate::QMetaTypeInterface *ritual_ZN21QMetaTypeModuleHelper22interfaceForType_dummyEi(
    int a0) {
  return QMetaTypeModuleHelper::interfaceForType_dummy(a0);
}

//  QMetaTypeModuleHelper::~QMetaTypeModuleHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMetaTypeModuleHelperD1Ev(QMetaTypeModuleHelper *self) {
  delete self;
}
