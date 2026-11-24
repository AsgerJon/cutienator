//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qtmm_rtsan_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if !(defined(__has_feature) && __has_feature(realtime_sanitizer))
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmm_rtsan_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtPrivate::ScopedRTSanDisabler::ScopedRTSanDisabler()
extern "C" Q_DECL_EXPORT
QtPrivate::ScopedRTSanDisabler *ritual_ZN9QtPrivate19ScopedRTSanDisablerC1Ev() {
  return new QtPrivate::ScopedRTSanDisabler();
}

//  QtPrivate::ScopedRTSanDisabler::~ScopedRTSanDisabler()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19ScopedRTSanDisablerD1Ev(
    QtPrivate::ScopedRTSanDisabler *self) {
  delete self;
}

#endif  // !(defined(__has_feature) && __has_feature(realtime_sanitizer))
