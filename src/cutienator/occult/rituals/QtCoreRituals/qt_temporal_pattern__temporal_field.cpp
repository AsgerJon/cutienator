//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datestring)
#if QT_CONFIG(datestring)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  DateTimePart QtTemporalPattern::TemporalField::part() const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::DateTimePart ritual_ZNK17QtTemporalPattern13TemporalField4partEv(
    const QtTemporalPattern::TemporalField *self) {
  return self->part();
}

//  bool operator==(const TemporalField &lhs, const TemporalField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtTemporalPatterneqERKNS_13TemporalFieldES2_(
    const QtTemporalPattern::TemporalField *lhs,
    const QtTemporalPattern::TemporalField *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const TemporalField &lhs, const TemporalField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtTemporalPatternneERKNS_13TemporalFieldES2_(
    const QtTemporalPattern::TemporalField *lhs,
    const QtTemporalPattern::TemporalField *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QtTemporalPattern::TemporalField::~TemporalField()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtTemporalPattern13TemporalFieldD1Ev(
    QtTemporalPattern::TemporalField *self) {
  delete self;
}

#endif  // QT_CONFIG(datestring)
#endif  // QT_CONFIG(datestring)
