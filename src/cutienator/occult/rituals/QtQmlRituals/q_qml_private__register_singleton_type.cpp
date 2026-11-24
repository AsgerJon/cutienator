//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  QQmlPrivate::RegisterSingletonType::~RegisterSingletonType()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate21RegisterSingletonTypeD1Ev(
    QQmlPrivate::RegisterSingletonType *self) {
  delete self;
}
