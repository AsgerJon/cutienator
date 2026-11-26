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
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <optional>
#include <QtCore/QDate>
#include <QtCore/QStringView>

//  QDatePattern::QDatePattern(const QList<Field> &fs)
extern "C" Q_DECL_EXPORT
QDatePattern *ritual_ZN12QDatePatternC1ERK5QListIN17QtTemporalPattern13TemporalFieldEE(
    const QList<QDatePattern::Field> *fs) {
  return new QDatePattern(*fs);
}

//  QDatePattern::QDatePattern(const QList<Field> &fs, int centuryStart)
extern "C" Q_DECL_EXPORT
QDatePattern *ritual_ZN12QDatePatternC1ERK5QListIN17QtTemporalPattern13TemporalFieldEEi(
    const QList<QDatePattern::Field> *fs,
    int centuryStart) {
  return new QDatePattern(*fs, centuryStart);
}

//  QtTemporalPattern::SupportType QDatePattern::dateSupport() const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::SupportType ritual_ZNK12QDatePattern11dateSupportEv(
    const QDatePattern *self) {
  return self->dateSupport();
}

//  bool QDatePattern::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDatePattern7isValidEv(const QDatePattern *self) {
  return self->isValid();
}

//  void QDatePattern::setLocale(const QLocale &loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDatePattern9setLocaleERK7QLocale(
    QDatePattern *self,
    const QLocale *loc) {
  self->setLocale(*loc);
}

//  const QLocale &QDatePattern::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK12QDatePattern6localeEv(const QDatePattern *self) {
  return new QLocale(self->locale());
}

//  void QDatePattern::setBaseYear(int centuryStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDatePattern11setBaseYearEi(
    QDatePattern *self,
    int centuryStart) {
  self->setBaseYear(centuryStart);
}

//  void QDatePattern::clearBaseYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDatePattern13clearBaseYearEv(QDatePattern *self) {
  self->clearBaseYear();
}

//  std::optional<int> QDatePattern::baseYear() const
extern "C" Q_DECL_EXPORT
std::optional<int> *ritual_ZNK12QDatePattern8baseYearEv(
    const QDatePattern *self) {
  return new std::optional<int>(self->baseYear());
}

//  void QDatePattern::setCalendar(QCalendar cal)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDatePattern11setCalendarE9QCalendar(
    QDatePattern *self,
    const QCalendar *cal) {
  self->setCalendar(*cal);
}

//  QCalendar QDatePattern::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK12QDatePattern8calendarEv(const QDatePattern *self) {
  return new QCalendar(self->calendar());
}

//  QtTemporalPattern::ParseResult<QDate> QDatePattern::parse(QStringView
//      text, QDate defaults) const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::ParseResult<QDate> *ritual_ZNK12QDatePattern5parseE11QStringView5QDate(
    const QDatePattern *self,
    const QString *text,
    const QDate *defaults) {
  return new QtTemporalPattern::ParseResult<QDate>(
      self->parse(
          QStringView(*text),
          *defaults));
}

//  QString QDatePattern::serialize(const QDate &date) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDatePattern9serializeERK5QDate(
    const QDatePattern *self,
    const QDate *date) {
  return new QString(self->serialize(*date));
}

//  QDatePattern QDatePattern::fromQtFormat(QStringView format)
extern "C" Q_DECL_EXPORT
QDatePattern *ritual_ZN12QDatePattern12fromQtFormatE11QStringView(
    const QString *format) {
  return new QDatePattern(QDatePattern::fromQtFormat(QStringView(*format)));
}

//  QDatePattern QDatePattern::forLocale(const QLocale &locale,
//      QLocale::FormatType format)
extern "C" Q_DECL_EXPORT
QDatePattern *ritual_ZN12QDatePattern9forLocaleERK7QLocaleNS0_10FormatTypeE(
    const QLocale *locale,
    QLocale::FormatType format) {
  return new QDatePattern(QDatePattern::forLocale(*locale, format));
}

//  QDatePattern::~QDatePattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDatePatternD1Ev(QDatePattern *self) {
  delete self;
}

//  a std::optional<int> a ritual of QDatePattern gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDatePattern__std_optional_int(std::optional<int> *self) {
  delete self;
}

//  a QtTemporalPattern::ParseResult<QDate> a ritual of QDatePattern gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDatePattern__QtTemporalPattern_ParseResult_QDate(
    QtTemporalPattern::ParseResult<QDate> *self) {
  delete self;
}

#endif  // QT_CONFIG(datestring)
#endif  // QT_CONFIG(datestring)
