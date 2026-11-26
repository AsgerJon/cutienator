//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QDBusSlotCache::swap(QDBusSlotCache &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSlotCache4swapERS_(
    QDBusSlotCache *self,
    QDBusSlotCache *other) {
  self->swap(*other);
}

//  QDBusSlotCache::~QDBusSlotCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSlotCacheD1Ev(QDBusSlotCache *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
