//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QDBusConnectionPrivate::ArgMatchRules::operator==(const
//      ArgMatchRules &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusConnectionPrivate13ArgMatchRuleseqERKS0_(
    const QDBusConnectionPrivate::ArgMatchRules *self,
    const QDBusConnectionPrivate::ArgMatchRules *other) {
  return self->operator==(*other);
}

//  QDBusConnectionPrivate::ArgMatchRules::~ArgMatchRules()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate13ArgMatchRulesD1Ev(
    QDBusConnectionPrivate::ArgMatchRules *self) {
  delete self;
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
