//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qislamiccivilcalendar_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(islamiccivilcalendar)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qislamiccivilcalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlocale.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QIslamicCivilCalendar that Python can take functions over in. Every QIslamicCivilCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(islamiccivilcalendar)
typedef QString * (*CuteQIslamicCivilCalendarCall0)(const void *, int *);
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(islamiccivilcalendar)
typedef bool (*CuteQIslamicCivilCalendarCall1)(const void *, int, int *);
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(islamiccivilcalendar)
typedef const QCalendar::YearMonthDay * (*CuteQIslamicCivilCalendarCall2)(const void *, qint64, int *);
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQIslamicCivilCalendarCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQIslamicCivilCalendarCall4)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQIslamicCivilCalendarCall5)(const void *, int, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQIslamicCivilCalendarCall6)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQIslamicCivilCalendarCall7)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQIslamicCivilCalendarCall8)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef void * (*CuteQIslamicCivilCalendarCall9)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef void * (*CuteQIslamicCivilCalendarCall10)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
typedef int (*CuteQIslamicCivilCalendarCall11)(const void *, int, int *);
typedef bool (*CuteQIslamicCivilCalendarCall12)(const void *, int, int, int, int *);
typedef bool (*CuteQIslamicCivilCalendarCall13)(const void *, int *);
typedef bool (*CuteQIslamicCivilCalendarCall14)(const void *, int *);
typedef int (*CuteQIslamicCivilCalendarCall15)(const void *, int *);
typedef int (*CuteQIslamicCivilCalendarCall16)(const void *, int *);
typedef int (*CuteQIslamicCivilCalendarCall17)(const void *, qint64, int *);
typedef qint64 (*CuteQIslamicCivilCalendarCall18)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQIslamicCivilCalendarCall19)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQIslamicCivilCalendarCall20)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQIslamicCivilCalendarCall21)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQIslamicCivilCalendarCall22)(const void *, const QLocale *, int, int, int *);
class CuteQIslamicCivilCalendar : public QIslamicCivilCalendar {
public:
  using QIslamicCivilCalendar::QIslamicCivilCalendar;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(islamiccivilcalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(islamiccivilcalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(islamiccivilcalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(islamiccivilcalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15localeMonthDataEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9dayOfWeekEx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(islamiccivilcalendar)
  //  QString QIslamicCivilCalendar::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall0 call = reinterpret_cast<CuteQIslamicCivilCalendarCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QIslamicCivilCalendar::name();
  }
#endif  // QT_CONFIG(islamiccivilcalendar)

#if QT_CONFIG(islamiccivilcalendar)
  //  bool QIslamicCivilCalendar::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall1 call = reinterpret_cast<CuteQIslamicCivilCalendarCall1>(taken[1]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return QIslamicCivilCalendar::isLeapYear(year);
  }
#endif  // QT_CONFIG(islamiccivilcalendar)

#if QT_CONFIG(islamiccivilcalendar)
  //  QCalendar::YearMonthDay QIslamicCivilCalendar::julianDayToDate(qint64
  //      jd) const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall2 call = reinterpret_cast<CuteQIslamicCivilCalendarCall2>(taken[2]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return QIslamicCivilCalendar::julianDayToDate(jd);
  }
#endif  // QT_CONFIG(islamiccivilcalendar)

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall3 call = reinterpret_cast<CuteQIslamicCivilCalendarCall3>(taken[3]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::daysInMonth(month, year);
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall4 call = reinterpret_cast<CuteQIslamicCivilCalendarCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::maximumDaysInMonth();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall5 call = reinterpret_cast<CuteQIslamicCivilCalendarCall5>(taken[5]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::daysInYear(year);
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall6 call = reinterpret_cast<CuteQIslamicCivilCalendarCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isLunar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall7 call = reinterpret_cast<CuteQIslamicCivilCalendarCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isLuniSolar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall8 call = reinterpret_cast<CuteQIslamicCivilCalendarCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isSolar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  const QCalendarLocale *QHijriCalendar::localeMonthIndexData() const
  const QCalendarLocale *localeMonthIndexData() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall9 call = reinterpret_cast<CuteQIslamicCivilCalendarCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QHijriCalendar::localeMonthIndexData();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  const char16_t *QHijriCalendar::localeMonthData() const
  const char16_t *localeMonthData() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall10 call = reinterpret_cast<CuteQIslamicCivilCalendarCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const char16_t *>(given);
    }
    return QHijriCalendar::localeMonthData();
  }
#endif  // QT_CONFIG(hijricalendar)

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall11 call = reinterpret_cast<CuteQIslamicCivilCalendarCall11>(taken[11]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall12 call = reinterpret_cast<CuteQIslamicCivilCalendarCall12>(taken[12]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall13 call = reinterpret_cast<CuteQIslamicCivilCalendarCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall14 call = reinterpret_cast<CuteQIslamicCivilCalendarCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall15 call = reinterpret_cast<CuteQIslamicCivilCalendarCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::minimumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall16 call = reinterpret_cast<CuteQIslamicCivilCalendarCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall17 call = reinterpret_cast<CuteQIslamicCivilCalendarCall17>(taken[17]);
      int given = call(this, jd, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::dayOfWeek(jd);
  }

  //  qint64 QCalendarBackend::matchCenturyToWeekday(const
  //      QCalendar::YearMonthDay &parts, int dow) const
  qint64 matchCenturyToWeekday(
      const QCalendar::YearMonthDay &parts,
      int dow) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall18 call = reinterpret_cast<CuteQIslamicCivilCalendarCall18>(taken[18]);
      qint64 given = call(this, &parts, dow, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::matchCenturyToWeekday(parts, dow);
  }

  //  QString QCalendarBackend::monthName(const QLocale &locale, int month,
  //      int year, QLocale::FormatType format) const
  QString monthName(
      const QLocale &locale,
      int month,
      int year,
      QLocale::FormatType format) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall19 call = reinterpret_cast<CuteQIslamicCivilCalendarCall19>(taken[19]);
      QString * given = call(this, &locale, month, year, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCalendarBackend::monthName(locale, month, year, format);
  }

  //  QString QCalendarBackend::standaloneMonthName(const QLocale &locale,
  //      int month, int year, QLocale::FormatType format) const
  QString standaloneMonthName(
      const QLocale &locale,
      int month,
      int year,
      QLocale::FormatType format) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall20 call = reinterpret_cast<CuteQIslamicCivilCalendarCall20>(taken[20]);
      QString * given = call(this, &locale, month, year, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCalendarBackend::standaloneMonthName(locale, month, year, format);
  }

  //  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
  //      QLocale::FormatType format) const
  QString weekDayName(
      const QLocale &locale,
      int day,
      QLocale::FormatType format) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall21 call = reinterpret_cast<CuteQIslamicCivilCalendarCall21>(taken[21]);
      QString * given = call(this, &locale, day, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCalendarBackend::weekDayName(locale, day, format);
  }

  //  QString QCalendarBackend::standaloneWeekDayName(const QLocale
  //      &locale, int day, QLocale::FormatType format) const
  QString standaloneWeekDayName(
      const QLocale &locale,
      int day,
      QLocale::FormatType format) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQIslamicCivilCalendarCall22 call = reinterpret_cast<CuteQIslamicCivilCalendarCall22>(taken[22]);
      QString * given = call(this, &locale, day, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCalendarBackend::standaloneWeekDayName(locale, day, format);
  }
};

//  QString QIslamicCivilCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QIslamicCivilCalendar4nameEv(
    const QIslamicCivilCalendar *self) {
  return new QString(self->name());
}

//  QStringList QIslamicCivilCalendar::nameList()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QIslamicCivilCalendar8nameListEv() {
  return new QList<QString>(QIslamicCivilCalendar::nameList());
}

//  bool QIslamicCivilCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QIslamicCivilCalendar10isLeapYearEi(
    const QIslamicCivilCalendar *self,
    int year) {
  return self->isLeapYear(year);
}

//  bool QIslamicCivilCalendar::dateToJulianDay(int year, int month, int day,
//      qint64 *jd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QIslamicCivilCalendar15dateToJulianDayEiiiPx(
    const QIslamicCivilCalendar *self,
    int year,
    int month,
    int day,
    qint64 *jd) {
  return self->dateToJulianDay(year, month, day, jd);
}

//  QCalendar::YearMonthDay QIslamicCivilCalendar::julianDayToDate(qint64 jd)
//      const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK21QIslamicCivilCalendar15julianDayToDateEx(
    const QIslamicCivilCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(self->julianDayToDate(jd));
}

//  a Python function taken by a CuteQIslamicCivilCalendar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIslamicCivilCalendar(
    QIslamicCivilCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIslamicCivilCalendar *>(self)->take(key, call);
}

//  QString QIslamicCivilCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QIslamicCivilCalendar4nameEv(
    const QIslamicCivilCalendar *self) {
  return new QString(self->QIslamicCivilCalendar::name());
}

//  bool QIslamicCivilCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QIslamicCivilCalendar10isLeapYearEi(
    const QIslamicCivilCalendar *self,
    int year) {
  return self->QIslamicCivilCalendar::isLeapYear(year);
}

//  QCalendar::YearMonthDay QIslamicCivilCalendar::julianDayToDate(qint64 jd)
//      const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_own_ZNK21QIslamicCivilCalendar15julianDayToDateEx(
    const QIslamicCivilCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(
      self->QIslamicCivilCalendar::julianDayToDate(
          jd));
}

#endif  // QT_CONFIG(islamiccivilcalendar)
#endif  // QT_CONFIG(islamiccivilcalendar)
