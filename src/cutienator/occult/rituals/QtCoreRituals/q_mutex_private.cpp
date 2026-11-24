//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmutex_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmutex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QMutexPrivate::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMutexPrivate3refEv(QMutexPrivate *self) {
  return self->ref();
}

#endif  // QT_CONFIG(thread)
