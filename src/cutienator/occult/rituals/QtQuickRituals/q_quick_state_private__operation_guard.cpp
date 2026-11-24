//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void
//      QQuickStatePrivate::OperationGuard::objectDestroyedImpl(QQmlGuardImpl
//      *guard)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate14OperationGuard19objectDestroyedImplEP13QQmlGuardImpl(
    QQmlGuardImpl *guard) {
  QQuickStatePrivate::OperationGuard::objectDestroyedImpl(guard);
}

//  QQuickStatePrivate::OperationGuard::~OperationGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate14OperationGuardD1Ev(
    QQuickStatePrivate::OperationGuard *self) {
  delete self;
}
