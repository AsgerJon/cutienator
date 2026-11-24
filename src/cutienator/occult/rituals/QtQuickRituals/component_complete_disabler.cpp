//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ComponentCompleteDisabler::ComponentCompleteDisabler()
extern "C" Q_DECL_EXPORT
ComponentCompleteDisabler *ritual_ZN25ComponentCompleteDisablerC1Ev() {
  return new ComponentCompleteDisabler();
}

//  ComponentCompleteDisabler::~ComponentCompleteDisabler()
extern "C" Q_DECL_EXPORT
void ritual_ZN25ComponentCompleteDisablerD1Ev(
    ComponentCompleteDisabler *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
