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

//  bool operator==(const Key &lhs, const Key &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN14QDBusSlotCache3KeyES2_(
    const QDBusSlotCache::Key *lhs,
    const QDBusSlotCache::Key *rhs) {
  return operator==(*lhs, *rhs);
}

//  QDBusSlotCache::Key::~Key()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSlotCache3KeyD1Ev(QDBusSlotCache::Key *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
