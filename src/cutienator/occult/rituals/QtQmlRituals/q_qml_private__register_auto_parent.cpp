//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  QQmlPrivate::RegisterAutoParent::~RegisterAutoParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18RegisterAutoParentD1Ev(
    QQmlPrivate::RegisterAutoParent *self) {
  delete self;
}
