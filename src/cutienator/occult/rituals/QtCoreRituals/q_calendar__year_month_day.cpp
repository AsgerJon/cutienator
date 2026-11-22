//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcalendar.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcalendar.h>

//  QCalendar::YearMonthDay::YearMonthDay()
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZN9QCalendar12YearMonthDayC1Ev() {
  return new QCalendar::YearMonthDay();
}

//  QCalendar::YearMonthDay::YearMonthDay(int y, int m, int d)
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZN9QCalendar12YearMonthDayC1Eiii(
    int y,
    int m,
    int d) {
  return new QCalendar::YearMonthDay(y, m, d);
}

//  bool QCalendar::YearMonthDay::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar12YearMonthDay7isValidEv(
    const QCalendar::YearMonthDay *self) {
  return self->isValid();
}

//  QCalendar::YearMonthDay::~YearMonthDay()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCalendar12YearMonthDayD1Ev(QCalendar::YearMonthDay *self) {
  delete self;
}
