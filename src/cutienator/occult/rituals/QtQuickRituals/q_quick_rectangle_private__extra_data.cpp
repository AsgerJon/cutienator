//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25:
//  the header of QQuickRectangle is included before
//  that of QQuickRectanglePrivate, which uses QQuickPen without
//  declaring it; QQuickPen is defined in the former.
//  Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickRectanglePrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickRectanglePrivate::ExtraData *ritual_ZN22QQuickRectanglePrivate9ExtraDataC1Ev() {
  return new QQuickRectanglePrivate::ExtraData();
}
