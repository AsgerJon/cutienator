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
#include <QtCore/qlocale.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QtTemporalPattern::SupportType QDateTimePattern::dateTimeSupport() const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::SupportType ritual_ZNK16QDateTimePattern15dateTimeSupportEv(
    const QDateTimePattern *self) {
  return self->dateTimeSupport();
}

//  bool QDateTimePattern::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDateTimePattern7isValidEv(const QDateTimePattern *self) {
  return self->isValid();
}

//  void QDateTimePattern::setLocale(const QLocale &loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePattern9setLocaleERK7QLocale(
    QDateTimePattern *self,
    const QLocale *loc) {
  self->setLocale(*loc);
}

//  const QLocale &QDateTimePattern::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16QDateTimePattern6localeEv(
    const QDateTimePattern *self) {
  return new QLocale(self->locale());
}

//  void QDateTimePattern::setBaseYear(int centuryStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePattern11setBaseYearEi(
    QDateTimePattern *self,
    int centuryStart) {
  self->setBaseYear(centuryStart);
}

//  void QDateTimePattern::clearBaseYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePattern13clearBaseYearEv(QDateTimePattern *self) {
  self->clearBaseYear();
}

//  void QDateTimePattern::setCalendar(QCalendar cal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePattern11setCalendarE9QCalendar(
    QDateTimePattern *self,
    const QCalendar *cal) {
  self->setCalendar(*cal);
}

//  QCalendar QDateTimePattern::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK16QDateTimePattern8calendarEv(
    const QDateTimePattern *self) {
  return new QCalendar(self->calendar());
}

//  QString QDateTimePattern::serialize(const QDateTime &datetime) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDateTimePattern9serializeERK9QDateTime(
    const QDateTimePattern *self,
    const QDateTime *datetime) {
  return new QString(self->serialize(*datetime));
}

//  QDateTimePattern QDateTimePattern::fromQtFormat(QStringView format)
extern "C" Q_DECL_EXPORT
QDateTimePattern *ritual_ZN16QDateTimePattern12fromQtFormatE11QStringView(
    const QString *format) {
  return new QDateTimePattern(
      QDateTimePattern::fromQtFormat(
          QStringView(*format)));
}

//  QDateTimePattern QDateTimePattern::forLocale(const QLocale &locale,
//      QLocale::FormatType format)
extern "C" Q_DECL_EXPORT
QDateTimePattern *ritual_ZN16QDateTimePattern9forLocaleERK7QLocaleNS0_10FormatTypeE(
    const QLocale *locale,
    QLocale::FormatType format) {
  return new QDateTimePattern(QDateTimePattern::forLocale(*locale, format));
}

//  QDateTimePattern::~QDateTimePattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePatternD1Ev(QDateTimePattern *self) {
  delete self;
}

#endif  // QT_CONFIG(datestring)
#endif  // QT_CONFIG(datestring)
