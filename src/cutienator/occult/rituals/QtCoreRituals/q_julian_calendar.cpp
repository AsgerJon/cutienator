//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qjuliancalendar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qjuliancalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlocale.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QJulianCalendar that Python can take functions over in. Every QJulianCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQJulianCalendarCall0)(const void *, int *);
typedef bool (*CuteQJulianCalendarCall1)(const void *, int, int *);
typedef const QCalendar::YearMonthDay * (*CuteQJulianCalendarCall2)(const void *, qint64, int *);
typedef int (*CuteQJulianCalendarCall3)(const void *, int, int, int *);
typedef int (*CuteQJulianCalendarCall4)(const void *, int *);
typedef bool (*CuteQJulianCalendarCall5)(const void *, int *);
typedef bool (*CuteQJulianCalendarCall6)(const void *, int *);
typedef bool (*CuteQJulianCalendarCall7)(const void *, int *);
typedef QString * (*CuteQJulianCalendarCall8)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQJulianCalendarCall9)(const void *, const QLocale *, int, int, int, int *);
typedef void * (*CuteQJulianCalendarCall10)(const void *, int *);
typedef int (*CuteQJulianCalendarCall11)(const void *, int, int *);
typedef int (*CuteQJulianCalendarCall12)(const void *, int, int *);
typedef bool (*CuteQJulianCalendarCall13)(const void *, int, int, int, int *);
typedef bool (*CuteQJulianCalendarCall14)(const void *, int *);
typedef bool (*CuteQJulianCalendarCall15)(const void *, int *);
typedef int (*CuteQJulianCalendarCall16)(const void *, int *);
typedef int (*CuteQJulianCalendarCall17)(const void *, int *);
typedef int (*CuteQJulianCalendarCall18)(const void *, qint64, int *);
typedef qint64 (*CuteQJulianCalendarCall19)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQJulianCalendarCall20)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQJulianCalendarCall21)(const void *, const QLocale *, int, int, int *);
class CuteQJulianCalendar : public QJulianCalendar {
public:
  using QJulianCalendar::QJulianCalendar;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9dayOfWeekEx")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[21] = call;
      return true;
    }
    return false;
  }

  //  QString QJulianCalendar::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQJulianCalendarCall0 call = reinterpret_cast<CuteQJulianCalendarCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QJulianCalendar::name();
  }

  //  bool QJulianCalendar::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQJulianCalendarCall1 call = reinterpret_cast<CuteQJulianCalendarCall1>(taken[1]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return QJulianCalendar::isLeapYear(year);
  }

  //  QCalendar::YearMonthDay QJulianCalendar::julianDayToDate(qint64 jd)
  //      const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQJulianCalendarCall2 call = reinterpret_cast<CuteQJulianCalendarCall2>(taken[2]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return QJulianCalendar::julianDayToDate(jd);
  }

  //  int QRomanCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQJulianCalendarCall3 call = reinterpret_cast<CuteQJulianCalendarCall3>(taken[3]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::daysInMonth(month, year);
  }

  //  int QRomanCalendar::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQJulianCalendarCall4 call = reinterpret_cast<CuteQJulianCalendarCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::minimumDaysInMonth();
  }

  //  bool QRomanCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQJulianCalendarCall5 call = reinterpret_cast<CuteQJulianCalendarCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLunar();
  }

  //  bool QRomanCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQJulianCalendarCall6 call = reinterpret_cast<CuteQJulianCalendarCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLuniSolar();
  }

  //  bool QRomanCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQJulianCalendarCall7 call = reinterpret_cast<CuteQJulianCalendarCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isSolar();
  }

  //  QString QRomanCalendar::monthName(const QLocale &locale, int month,
  //      int year, QLocale::FormatType format) const
  QString monthName(
      const QLocale &locale,
      int month,
      int year,
      QLocale::FormatType format) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQJulianCalendarCall8 call = reinterpret_cast<CuteQJulianCalendarCall8>(taken[8]);
      QString * given = call(this, &locale, month, year, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QRomanCalendar::monthName(locale, month, year, format);
  }

  //  QString QRomanCalendar::standaloneMonthName(const QLocale &locale,
  //      int month, int year, QLocale::FormatType format) const
  QString standaloneMonthName(
      const QLocale &locale,
      int month,
      int year,
      QLocale::FormatType format) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQJulianCalendarCall9 call = reinterpret_cast<CuteQJulianCalendarCall9>(taken[9]);
      QString * given = call(this, &locale, month, year, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QRomanCalendar::standaloneMonthName(locale, month, year, format);
  }

  //  const QCalendarLocale *QRomanCalendar::localeMonthIndexData() const
  const QCalendarLocale *localeMonthIndexData() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQJulianCalendarCall10 call = reinterpret_cast<CuteQJulianCalendarCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QRomanCalendar::localeMonthIndexData();
  }

  //  int QCalendarBackend::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQJulianCalendarCall11 call = reinterpret_cast<CuteQJulianCalendarCall11>(taken[11]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::daysInYear(year);
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQJulianCalendarCall12 call = reinterpret_cast<CuteQJulianCalendarCall12>(taken[12]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQJulianCalendarCall13 call = reinterpret_cast<CuteQJulianCalendarCall13>(taken[13]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQJulianCalendarCall14 call = reinterpret_cast<CuteQJulianCalendarCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQJulianCalendarCall15 call = reinterpret_cast<CuteQJulianCalendarCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQJulianCalendarCall16 call = reinterpret_cast<CuteQJulianCalendarCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQJulianCalendarCall17 call = reinterpret_cast<CuteQJulianCalendarCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQJulianCalendarCall18 call = reinterpret_cast<CuteQJulianCalendarCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQJulianCalendarCall19 call = reinterpret_cast<CuteQJulianCalendarCall19>(taken[19]);
      qint64 given = call(this, &parts, dow, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::matchCenturyToWeekday(parts, dow);
  }

  //  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
  //      QLocale::FormatType format) const
  QString weekDayName(
      const QLocale &locale,
      int day,
      QLocale::FormatType format) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQJulianCalendarCall20 call = reinterpret_cast<CuteQJulianCalendarCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQJulianCalendarCall21 call = reinterpret_cast<CuteQJulianCalendarCall21>(taken[21]);
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

//  QString QJulianCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QJulianCalendar4nameEv(const QJulianCalendar *self) {
  return new QString(self->name());
}

//  QStringList QJulianCalendar::nameList()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN15QJulianCalendar8nameListEv() {
  return new QList<QString>(QJulianCalendar::nameList());
}

//  bool QJulianCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJulianCalendar10isLeapYearEi(
    const QJulianCalendar *self,
    int year) {
  return self->isLeapYear(year);
}

//  bool QJulianCalendar::dateToJulianDay(int year, int month, int day,
//      qint64 *jd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJulianCalendar15dateToJulianDayEiiiPx(
    const QJulianCalendar *self,
    int year,
    int month,
    int day,
    qint64 *jd) {
  return self->dateToJulianDay(year, month, day, jd);
}

//  QCalendar::YearMonthDay QJulianCalendar::julianDayToDate(qint64 jd) const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK15QJulianCalendar15julianDayToDateEx(
    const QJulianCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(self->julianDayToDate(jd));
}

//  a Python function taken by a CuteQJulianCalendar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJulianCalendar(
    QJulianCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQJulianCalendar *>(self)->take(key, call);
}

//  QString QJulianCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QJulianCalendar4nameEv(
    const QJulianCalendar *self) {
  return new QString(self->QJulianCalendar::name());
}

//  bool QJulianCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QJulianCalendar10isLeapYearEi(
    const QJulianCalendar *self,
    int year) {
  return self->QJulianCalendar::isLeapYear(year);
}

//  QCalendar::YearMonthDay QJulianCalendar::julianDayToDate(qint64 jd) const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_own_ZNK15QJulianCalendar15julianDayToDateEx(
    const QJulianCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(
      self->QJulianCalendar::julianDayToDate(
          jd));
}
