//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdatetime_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetime_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDateTimePrivate::ZoneState::ZoneState(qint64 local)
extern "C" Q_DECL_EXPORT
QDateTimePrivate::ZoneState *ritual_ZN16QDateTimePrivate9ZoneStateC1Ex(
    qint64 local) {
  return new QDateTimePrivate::ZoneState(local);
}

//  QDateTimePrivate::ZoneState::ZoneState(qint64 w, int o, DaylightStatus d,
//      bool v)
extern "C" Q_DECL_EXPORT
QDateTimePrivate::ZoneState *ritual_ZN16QDateTimePrivate9ZoneStateC1ExiNS_14DaylightStatusEb(
    qint64 w,
    int o,
    QDateTimePrivate::DaylightStatus d,
    bool v) {
  return new QDateTimePrivate::ZoneState(w, o, d, v);
}

//  QDateTimePrivate::ZoneState::~ZoneState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePrivate9ZoneStateD1Ev(
    QDateTimePrivate::ZoneState *self) {
  delete self;
}
