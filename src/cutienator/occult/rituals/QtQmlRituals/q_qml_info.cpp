//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlinfo.h>

//  QQmlInfo::QQmlInfo(const QQmlInfo &a0)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfoC1ERKS_(const QQmlInfo *a0) {
  return new QQmlInfo(*a0);
}

//  QQmlInfo::~QQmlInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlInfoD1Ev(QQmlInfo *self) {
  delete self;
}
