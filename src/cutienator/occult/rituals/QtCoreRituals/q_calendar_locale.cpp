//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h>
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLocaleData::DataRange QCalendarLocale::monthName(QLocale::FormatType
//      type) const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK15QCalendarLocale9monthNameEN7QLocale10FormatTypeE(
    const QCalendarLocale *self,
    QLocale::FormatType type) {
  return new QLocaleData::DataRange(self->monthName(type));
}

//  QLocaleData::DataRange
//      QCalendarLocale::standaloneMonthName(QLocale::FormatType type) const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK15QCalendarLocale19standaloneMonthNameEN7QLocale10FormatTypeE(
    const QCalendarLocale *self,
    QLocale::FormatType type) {
  return new QLocaleData::DataRange(self->standaloneMonthName(type));
}

//  QCalendarLocale::~QCalendarLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarLocaleD1Ev(QCalendarLocale *self) {
  delete self;
}
