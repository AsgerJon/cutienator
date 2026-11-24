//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtipccommon_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory) || QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtipccommon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtipccommon.h>
#include <QtCore/qstring.h>

//  QString QNativeIpcKeyPrivate::legacyKey(const QNativeIpcKey &key)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QNativeIpcKeyPrivate9legacyKeyERK13QNativeIpcKey(
    const QNativeIpcKey *key) {
  return new QString(QNativeIpcKeyPrivate::legacyKey(*key));
}

//  QNativeIpcKeyPrivate::~QNativeIpcKeyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNativeIpcKeyPrivateD1Ev(QNativeIpcKeyPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(sharedmemory) || QT_CONFIG(systemsemaphore)
