//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtparsetimezone_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datetimeparser)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtparsetimezone_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDateTime::TransitionResolution
//      QtParseTimeZone::ParsedZone::resolveType() const
extern "C" Q_DECL_EXPORT
QDateTime::TransitionResolution ritual_ZNK15QtParseTimeZone10ParsedZone11resolveTypeEv(
    const QtParseTimeZone::ParsedZone *self) {
  return self->resolveType();
}

//  QtParseTimeZone::ParsedZone::~ParsedZone()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtParseTimeZone10ParsedZoneD1Ev(
    QtParseTimeZone::ParsedZone *self) {
  delete self;
}

#endif  // QT_CONFIG(datetimeparser)
