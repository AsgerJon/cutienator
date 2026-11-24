//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qjalalicalendar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(jalalicalendar)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qjalalicalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlocale.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QJalaliCalendar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQJalaliCalendar : QJalaliCalendar {
  using QJalaliCalendar::localeMonthIndexData;
};

//  A QJalaliCalendar that Python can take functions over in. Every QJalaliCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(jalalicalendar)
typedef QString * (*CuteQJalaliCalendarCall0)(const void *, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef int (*CuteQJalaliCalendarCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef bool (*CuteQJalaliCalendarCall2)(const void *, int, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef bool (*CuteQJalaliCalendarCall3)(const void *, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef bool (*CuteQJalaliCalendarCall4)(const void *, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef bool (*CuteQJalaliCalendarCall5)(const void *, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef const QCalendar::YearMonthDay * (*CuteQJalaliCalendarCall6)(const void *, qint64, int *);
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
typedef void * (*CuteQJalaliCalendarCall7)(const void *, int *);
#endif  // QT_CONFIG(jalalicalendar)
typedef int (*CuteQJalaliCalendarCall8)(const void *, int, int *);
typedef int (*CuteQJalaliCalendarCall9)(const void *, int, int *);
typedef bool (*CuteQJalaliCalendarCall10)(const void *, int, int, int, int *);
typedef bool (*CuteQJalaliCalendarCall11)(const void *, int *);
typedef bool (*CuteQJalaliCalendarCall12)(const void *, int *);
typedef int (*CuteQJalaliCalendarCall13)(const void *, int *);
typedef int (*CuteQJalaliCalendarCall14)(const void *, int *);
typedef int (*CuteQJalaliCalendarCall15)(const void *, int *);
typedef int (*CuteQJalaliCalendarCall16)(const void *, qint64, int *);
typedef qint64 (*CuteQJalaliCalendarCall17)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQJalaliCalendarCall18)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQJalaliCalendarCall19)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQJalaliCalendarCall20)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQJalaliCalendarCall21)(const void *, const QLocale *, int, int, int *);
class CuteQJalaliCalendar : public QJalaliCalendar {
public:
  using QJalaliCalendar::QJalaliCalendar;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
#if QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(jalalicalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9dayOfWeekEx")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
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

#if QT_CONFIG(jalalicalendar)
  //  QString QJalaliCalendar::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQJalaliCalendarCall0 call = reinterpret_cast<CuteQJalaliCalendarCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QJalaliCalendar::name();
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  int QJalaliCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQJalaliCalendarCall1 call = reinterpret_cast<CuteQJalaliCalendarCall1>(taken[1]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QJalaliCalendar::daysInMonth(month, year);
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  bool QJalaliCalendar::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQJalaliCalendarCall2 call = reinterpret_cast<CuteQJalaliCalendarCall2>(taken[2]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return QJalaliCalendar::isLeapYear(year);
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  bool QJalaliCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQJalaliCalendarCall3 call = reinterpret_cast<CuteQJalaliCalendarCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QJalaliCalendar::isLunar();
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  bool QJalaliCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQJalaliCalendarCall4 call = reinterpret_cast<CuteQJalaliCalendarCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QJalaliCalendar::isLuniSolar();
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  bool QJalaliCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQJalaliCalendarCall5 call = reinterpret_cast<CuteQJalaliCalendarCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QJalaliCalendar::isSolar();
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  QCalendar::YearMonthDay QJalaliCalendar::julianDayToDate(qint64 jd)
  //      const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQJalaliCalendarCall6 call = reinterpret_cast<CuteQJalaliCalendarCall6>(taken[6]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return QJalaliCalendar::julianDayToDate(jd);
  }
#endif  // QT_CONFIG(jalalicalendar)

#if QT_CONFIG(jalalicalendar)
  //  const QCalendarLocale *QJalaliCalendar::localeMonthIndexData() const
  const QCalendarLocale *localeMonthIndexData() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQJalaliCalendarCall7 call = reinterpret_cast<CuteQJalaliCalendarCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QJalaliCalendar::localeMonthIndexData();
  }
#endif  // QT_CONFIG(jalalicalendar)

  //  int QCalendarBackend::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQJalaliCalendarCall8 call = reinterpret_cast<CuteQJalaliCalendarCall8>(taken[8]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::daysInYear(year);
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQJalaliCalendarCall9 call = reinterpret_cast<CuteQJalaliCalendarCall9>(taken[9]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQJalaliCalendarCall10 call = reinterpret_cast<CuteQJalaliCalendarCall10>(taken[10]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQJalaliCalendarCall11 call = reinterpret_cast<CuteQJalaliCalendarCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQJalaliCalendarCall12 call = reinterpret_cast<CuteQJalaliCalendarCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQJalaliCalendarCall13 call = reinterpret_cast<CuteQJalaliCalendarCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumDaysInMonth();
  }

  //  int QCalendarBackend::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQJalaliCalendarCall14 call = reinterpret_cast<CuteQJalaliCalendarCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::minimumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQJalaliCalendarCall15 call = reinterpret_cast<CuteQJalaliCalendarCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQJalaliCalendarCall16 call = reinterpret_cast<CuteQJalaliCalendarCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQJalaliCalendarCall17 call = reinterpret_cast<CuteQJalaliCalendarCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQJalaliCalendarCall18 call = reinterpret_cast<CuteQJalaliCalendarCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQJalaliCalendarCall19 call = reinterpret_cast<CuteQJalaliCalendarCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQJalaliCalendarCall20 call = reinterpret_cast<CuteQJalaliCalendarCall20>(taken[20]);
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
      CuteQJalaliCalendarCall21 call = reinterpret_cast<CuteQJalaliCalendarCall21>(taken[21]);
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

//  QString QJalaliCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QJalaliCalendar4nameEv(const QJalaliCalendar *self) {
  return new QString(self->name());
}

//  QStringList QJalaliCalendar::nameList()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN15QJalaliCalendar8nameListEv() {
  return new QList<QString>(QJalaliCalendar::nameList());
}

//  int QJalaliCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QJalaliCalendar11daysInMonthEii(
    const QJalaliCalendar *self,
    int month,
    int year) {
  return self->daysInMonth(month, year);
}

//  bool QJalaliCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJalaliCalendar10isLeapYearEi(
    const QJalaliCalendar *self,
    int year) {
  return self->isLeapYear(year);
}

//  bool QJalaliCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJalaliCalendar7isLunarEv(const QJalaliCalendar *self) {
  return self->isLunar();
}

//  bool QJalaliCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJalaliCalendar11isLuniSolarEv(
    const QJalaliCalendar *self) {
  return self->isLuniSolar();
}

//  bool QJalaliCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJalaliCalendar7isSolarEv(const QJalaliCalendar *self) {
  return self->isSolar();
}

//  bool QJalaliCalendar::dateToJulianDay(int year, int month, int day,
//      qint64 *jd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJalaliCalendar15dateToJulianDayEiiiPx(
    const QJalaliCalendar *self,
    int year,
    int month,
    int day,
    qint64 *jd) {
  return self->dateToJulianDay(year, month, day, jd);
}

//  QCalendar::YearMonthDay QJalaliCalendar::julianDayToDate(qint64 jd) const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK15QJalaliCalendar15julianDayToDateEx(
    const QJalaliCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(self->julianDayToDate(jd));
}

//  const QCalendarLocale *QJalaliCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_ZNK15QJalaliCalendar20localeMonthIndexDataEv(
    const QJalaliCalendar *self) {
  return self->localeMonthIndexData();
}

//  a Python function taken by a CuteQJalaliCalendar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJalaliCalendar(
    QJalaliCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQJalaliCalendar *>(self)->take(key, call);
}

//  QString QJalaliCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QJalaliCalendar4nameEv(
    const QJalaliCalendar *self) {
  return new QString(self->QJalaliCalendar::name());
}

//  int QJalaliCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QJalaliCalendar11daysInMonthEii(
    const QJalaliCalendar *self,
    int month,
    int year) {
  return self->QJalaliCalendar::daysInMonth(month, year);
}

//  bool QJalaliCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QJalaliCalendar10isLeapYearEi(
    const QJalaliCalendar *self,
    int year) {
  return self->QJalaliCalendar::isLeapYear(year);
}

//  bool QJalaliCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QJalaliCalendar7isLunarEv(const QJalaliCalendar *self) {
  return self->QJalaliCalendar::isLunar();
}

//  bool QJalaliCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QJalaliCalendar11isLuniSolarEv(
    const QJalaliCalendar *self) {
  return self->QJalaliCalendar::isLuniSolar();
}

//  bool QJalaliCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QJalaliCalendar7isSolarEv(const QJalaliCalendar *self) {
  return self->QJalaliCalendar::isSolar();
}

//  QCalendar::YearMonthDay QJalaliCalendar::julianDayToDate(qint64 jd) const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_own_ZNK15QJalaliCalendar15julianDayToDateEx(
    const QJalaliCalendar *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(
      self->QJalaliCalendar::julianDayToDate(
          jd));
}

//  const QCalendarLocale *QJalaliCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_own_ZNK15QJalaliCalendar20localeMonthIndexDataEv(
    const QJalaliCalendar *self) {
  return static_cast<const OwnQJalaliCalendar *>(self)->OwnQJalaliCalendar::localeMonthIndexData();
}

#endif  // QT_CONFIG(jalalicalendar)
