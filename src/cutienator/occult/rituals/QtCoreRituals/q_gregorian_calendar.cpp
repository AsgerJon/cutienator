//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qgregoriancalendar_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qgregoriancalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGregorianCalendar that Python can take functions over in. Every QGregorianCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQGregorianCalendarCall0)(const void *, int *);
typedef bool (*CuteQGregorianCalendarCall1)(const void *, int, int *);
typedef const QCalendar::YearMonthDay * (*CuteQGregorianCalendarCall2)(const void *, qint64, int *);
typedef qint64 (*CuteQGregorianCalendarCall3)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef int (*CuteQGregorianCalendarCall4)(const void *, int, int, int *);
typedef int (*CuteQGregorianCalendarCall5)(const void *, int *);
typedef bool (*CuteQGregorianCalendarCall6)(const void *, int *);
typedef bool (*CuteQGregorianCalendarCall7)(const void *, int *);
typedef bool (*CuteQGregorianCalendarCall8)(const void *, int *);
typedef QString * (*CuteQGregorianCalendarCall9)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQGregorianCalendarCall10)(const void *, const QLocale *, int, int, int, int *);
typedef void * (*CuteQGregorianCalendarCall11)(const void *, int *);
typedef int (*CuteQGregorianCalendarCall12)(const void *, int, int *);
typedef int (*CuteQGregorianCalendarCall13)(const void *, int, int *);
typedef bool (*CuteQGregorianCalendarCall14)(const void *, int, int, int, int *);
typedef bool (*CuteQGregorianCalendarCall15)(const void *, int *);
typedef bool (*CuteQGregorianCalendarCall16)(const void *, int *);
typedef int (*CuteQGregorianCalendarCall17)(const void *, int *);
typedef int (*CuteQGregorianCalendarCall18)(const void *, int *);
typedef int (*CuteQGregorianCalendarCall19)(const void *, qint64, int *);
typedef QString * (*CuteQGregorianCalendarCall20)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQGregorianCalendarCall21)(const void *, const QLocale *, int, int, int *);
class CuteQGregorianCalendar : public QGregorianCalendar {
public:
  using QGregorianCalendar::QGregorianCalendar;
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
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9dayOfWeekEx")) {
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

  //  QString QGregorianCalendar::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGregorianCalendarCall0 call = reinterpret_cast<CuteQGregorianCalendarCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGregorianCalendar::name();
  }

  //  bool QGregorianCalendar::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGregorianCalendarCall1 call = reinterpret_cast<CuteQGregorianCalendarCall1>(taken[1]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return QGregorianCalendar::isLeapYear(year);
  }

  //  QCalendar::YearMonthDay QGregorianCalendar::julianDayToDate(qint64
  //      jd) const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGregorianCalendarCall2 call = reinterpret_cast<CuteQGregorianCalendarCall2>(taken[2]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return QGregorianCalendar::julianDayToDate(jd);
  }

  //  qint64 QGregorianCalendar::matchCenturyToWeekday(const
  //      QCalendar::YearMonthDay &parts, int dow) const
  qint64 matchCenturyToWeekday(
      const QCalendar::YearMonthDay &parts,
      int dow) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGregorianCalendarCall3 call = reinterpret_cast<CuteQGregorianCalendarCall3>(taken[3]);
      qint64 given = call(this, &parts, dow, &handled);
      if (handled) return given;
    }
    return QGregorianCalendar::matchCenturyToWeekday(parts, dow);
  }

  //  int QRomanCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGregorianCalendarCall4 call = reinterpret_cast<CuteQGregorianCalendarCall4>(taken[4]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::daysInMonth(month, year);
  }

  //  int QRomanCalendar::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGregorianCalendarCall5 call = reinterpret_cast<CuteQGregorianCalendarCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::minimumDaysInMonth();
  }

  //  bool QRomanCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGregorianCalendarCall6 call = reinterpret_cast<CuteQGregorianCalendarCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLunar();
  }

  //  bool QRomanCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGregorianCalendarCall7 call = reinterpret_cast<CuteQGregorianCalendarCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLuniSolar();
  }

  //  bool QRomanCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGregorianCalendarCall8 call = reinterpret_cast<CuteQGregorianCalendarCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQGregorianCalendarCall9 call = reinterpret_cast<CuteQGregorianCalendarCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQGregorianCalendarCall10 call = reinterpret_cast<CuteQGregorianCalendarCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQGregorianCalendarCall11 call = reinterpret_cast<CuteQGregorianCalendarCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QRomanCalendar::localeMonthIndexData();
  }

  //  int QCalendarBackend::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGregorianCalendarCall12 call = reinterpret_cast<CuteQGregorianCalendarCall12>(taken[12]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::daysInYear(year);
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGregorianCalendarCall13 call = reinterpret_cast<CuteQGregorianCalendarCall13>(taken[13]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGregorianCalendarCall14 call = reinterpret_cast<CuteQGregorianCalendarCall14>(taken[14]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGregorianCalendarCall15 call = reinterpret_cast<CuteQGregorianCalendarCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGregorianCalendarCall16 call = reinterpret_cast<CuteQGregorianCalendarCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGregorianCalendarCall17 call = reinterpret_cast<CuteQGregorianCalendarCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGregorianCalendarCall18 call = reinterpret_cast<CuteQGregorianCalendarCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQGregorianCalendarCall19 call = reinterpret_cast<CuteQGregorianCalendarCall19>(taken[19]);
      int given = call(this, jd, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::dayOfWeek(jd);
  }

  //  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
  //      QLocale::FormatType format) const
  QString weekDayName(
      const QLocale &locale,
      int day,
      QLocale::FormatType format) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQGregorianCalendarCall20 call = reinterpret_cast<CuteQGregorianCalendarCall20>(taken[20]);
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
      CuteQGregorianCalendarCall21 call = reinterpret_cast<CuteQGregorianCalendarCall21>(taken[21]);
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

//  QString QGregorianCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QGregorianCalendar4nameEv(
    const QGregorianCalendar *self) {
  return new QString(self->name());
}

//  QStringList QGregorianCalendar::nameList()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18QGregorianCalendar8nameListEv() {
  return new QList<QString>(QGregorianCalendar::nameList());
}

//  bool QGregorianCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGregorianCalendar10isLeapYearEi(
    const QGregorianCalendar *self,
    int year) {
  return self->isLeapYear(year);
}

//  bool QGregorianCalendar::dateToJulianDay(int year, int month, int day,
//      qint64 *jd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGregorianCalendar15dateToJulianDayEiiiPx(
    const QGregorianCalendar *self,
    int year,
    int month,
    int day,
    qint64 *jd) {
  return self->dateToJulianDay(year, month, day, jd);
}

//  QCalendar::YearMonthDay QGregorianCalendar::julianDayToDate(qint64 jd)
//      const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK18QGregorianCalendar15julianDayToDateEx(
    const QGregorianCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(self->julianDayToDate(jd));
}

//  qint64 QGregorianCalendar::matchCenturyToWeekday(const
//      QCalendar::YearMonthDay &parts, int dow) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QGregorianCalendar21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi(
    const QGregorianCalendar *self,
    const QCalendar::YearMonthDay *parts,
    int dow) {
  return self->matchCenturyToWeekday(*parts, dow);
}

//  int QGregorianCalendar::weekDayOfJulian(qint64 jd)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGregorianCalendar15weekDayOfJulianEx(qint64 jd) {
  return QGregorianCalendar::weekDayOfJulian(jd);
}

//  bool QGregorianCalendar::leapTest(int year)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QGregorianCalendar8leapTestEi(int year) {
  return QGregorianCalendar::leapTest(year);
}

//  int QGregorianCalendar::monthLength(int month, int year)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGregorianCalendar11monthLengthEii(int month, int year) {
  return QGregorianCalendar::monthLength(month, year);
}

//  bool QGregorianCalendar::validParts(int year, int month, int day)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QGregorianCalendar10validPartsEiii(
    int year,
    int month,
    int day) {
  return QGregorianCalendar::validParts(year, month, day);
}

//  QCalendar::YearMonthDay QGregorianCalendar::partsFromJulian(qint64 jd)
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZN18QGregorianCalendar15partsFromJulianEx(
    qint64 jd) {
  return new QCalendar::YearMonthDay(
      QGregorianCalendar::partsFromJulian(
          jd));
}

//  int QGregorianCalendar::yearStartWeekDay(int year)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGregorianCalendar16yearStartWeekDayEi(int year) {
  return QGregorianCalendar::yearStartWeekDay(year);
}

//  int QGregorianCalendar::yearSharingWeekDays(QDate date)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGregorianCalendar19yearSharingWeekDaysE5QDate(
    const QDate *date) {
  return QGregorianCalendar::yearSharingWeekDays(*date);
}

//  a Python function taken by a CuteQGregorianCalendar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGregorianCalendar(
    QGregorianCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGregorianCalendar *>(self)->take(key, call);
}

//  QString QGregorianCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QGregorianCalendar4nameEv(
    const QGregorianCalendar *self) {
  return new QString(self->QGregorianCalendar::name());
}

//  bool QGregorianCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QGregorianCalendar10isLeapYearEi(
    const QGregorianCalendar *self,
    int year) {
  return self->QGregorianCalendar::isLeapYear(year);
}

//  QCalendar::YearMonthDay QGregorianCalendar::julianDayToDate(qint64 jd)
//      const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_own_ZNK18QGregorianCalendar15julianDayToDateEx(
    const QGregorianCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(
      self->QGregorianCalendar::julianDayToDate(
          jd));
}

//  qint64 QGregorianCalendar::matchCenturyToWeekday(const
//      QCalendar::YearMonthDay &parts, int dow) const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK18QGregorianCalendar21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi(
    const QGregorianCalendar *self,
    const QCalendar::YearMonthDay *parts,
    int dow) {
  return self->QGregorianCalendar::matchCenturyToWeekday(*parts, dow);
}
