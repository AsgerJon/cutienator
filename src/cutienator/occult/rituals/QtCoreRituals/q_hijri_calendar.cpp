//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qhijricalendar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qhijricalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlocale.h>
#include <cstring>

//  Only a class built on QHijriCalendar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQHijriCalendar : QHijriCalendar {
  using QHijriCalendar::localeMonthIndexData;
  using QHijriCalendar::localeMonthData;
};

//  A QHijriCalendar that Python can take functions over in. Every QHijriCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQHijriCalendarCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQHijriCalendarCall1)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef int (*CuteQHijriCalendarCall2)(const void *, int, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQHijriCalendarCall3)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQHijriCalendarCall4)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef bool (*CuteQHijriCalendarCall5)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef void * (*CuteQHijriCalendarCall6)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
typedef void * (*CuteQHijriCalendarCall7)(const void *, int *);
#endif  // QT_CONFIG(hijricalendar)
typedef QString * (*CuteQHijriCalendarCall8)(const void *, int *);
typedef int (*CuteQHijriCalendarCall9)(const void *, int, int *);
typedef bool (*CuteQHijriCalendarCall10)(const void *, int, int, int, int *);
typedef bool (*CuteQHijriCalendarCall11)(const void *, int, int *);
typedef bool (*CuteQHijriCalendarCall12)(const void *, int *);
typedef bool (*CuteQHijriCalendarCall13)(const void *, int *);
typedef int (*CuteQHijriCalendarCall14)(const void *, int *);
typedef int (*CuteQHijriCalendarCall15)(const void *, int *);
typedef const QCalendar::YearMonthDay * (*CuteQHijriCalendarCall16)(const void *, qint64, int *);
typedef int (*CuteQHijriCalendarCall17)(const void *, qint64, int *);
typedef qint64 (*CuteQHijriCalendarCall18)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQHijriCalendarCall19)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQHijriCalendarCall20)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQHijriCalendarCall21)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQHijriCalendarCall22)(const void *, const QLocale *, int, int, int *);
class CuteQHijriCalendar : public QHijriCalendar {
public:
  using QHijriCalendar::QHijriCalendar;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
#if QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15localeMonthDataEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(hijricalendar)
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
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
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
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
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
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

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHijriCalendarCall0 call = reinterpret_cast<CuteQHijriCalendarCall0>(taken[0]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::daysInMonth(month, year);
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHijriCalendarCall1 call = reinterpret_cast<CuteQHijriCalendarCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::maximumDaysInMonth();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  int QHijriCalendar::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHijriCalendarCall2 call = reinterpret_cast<CuteQHijriCalendarCall2>(taken[2]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::daysInYear(year);
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHijriCalendarCall3 call = reinterpret_cast<CuteQHijriCalendarCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isLunar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHijriCalendarCall4 call = reinterpret_cast<CuteQHijriCalendarCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isLuniSolar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  bool QHijriCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHijriCalendarCall5 call = reinterpret_cast<CuteQHijriCalendarCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHijriCalendar::isSolar();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  const QCalendarLocale *QHijriCalendar::localeMonthIndexData() const
  const QCalendarLocale *localeMonthIndexData() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHijriCalendarCall6 call = reinterpret_cast<CuteQHijriCalendarCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QHijriCalendar::localeMonthIndexData();
  }
#endif  // QT_CONFIG(hijricalendar)

#if QT_CONFIG(hijricalendar)
  //  const char16_t *QHijriCalendar::localeMonthData() const
  const char16_t *localeMonthData() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHijriCalendarCall7 call = reinterpret_cast<CuteQHijriCalendarCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const char16_t *>(given);
    }
    return QHijriCalendar::localeMonthData();
  }
#endif  // QT_CONFIG(hijricalendar)

  //  QString QCalendarBackend::name() const
  QString name() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQHijriCalendarCall8 call = reinterpret_cast<CuteQHijriCalendarCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQHijriCalendarCall9 call = reinterpret_cast<CuteQHijriCalendarCall9>(taken[9]);
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
      CuteQHijriCalendarCall10 call = reinterpret_cast<CuteQHijriCalendarCall10>(taken[10]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQHijriCalendarCall11 call = reinterpret_cast<CuteQHijriCalendarCall11>(taken[11]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQHijriCalendarCall12 call = reinterpret_cast<CuteQHijriCalendarCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHijriCalendarCall13 call = reinterpret_cast<CuteQHijriCalendarCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQHijriCalendarCall14 call = reinterpret_cast<CuteQHijriCalendarCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::minimumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQHijriCalendarCall15 call = reinterpret_cast<CuteQHijriCalendarCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  QCalendar::YearMonthDay QCalendarBackend::julianDayToDate(qint64 jd)
  //      const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQHijriCalendarCall16 call = reinterpret_cast<CuteQHijriCalendarCall16>(taken[16]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQHijriCalendarCall17 call = reinterpret_cast<CuteQHijriCalendarCall17>(taken[17]);
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
      CuteQHijriCalendarCall18 call = reinterpret_cast<CuteQHijriCalendarCall18>(taken[18]);
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
      CuteQHijriCalendarCall19 call = reinterpret_cast<CuteQHijriCalendarCall19>(taken[19]);
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
      CuteQHijriCalendarCall20 call = reinterpret_cast<CuteQHijriCalendarCall20>(taken[20]);
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
      CuteQHijriCalendarCall21 call = reinterpret_cast<CuteQHijriCalendarCall21>(taken[21]);
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
      CuteQHijriCalendarCall22 call = reinterpret_cast<CuteQHijriCalendarCall22>(taken[22]);
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

//  int QHijriCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QHijriCalendar11daysInMonthEii(
    const QHijriCalendar *self,
    int month,
    int year) {
  return self->daysInMonth(month, year);
}

//  int QHijriCalendar::maximumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QHijriCalendar18maximumDaysInMonthEv(
    const QHijriCalendar *self) {
  return self->maximumDaysInMonth();
}

//  int QHijriCalendar::daysInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QHijriCalendar10daysInYearEi(
    const QHijriCalendar *self,
    int year) {
  return self->daysInYear(year);
}

//  bool QHijriCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QHijriCalendar7isLunarEv(const QHijriCalendar *self) {
  return self->isLunar();
}

//  bool QHijriCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QHijriCalendar11isLuniSolarEv(const QHijriCalendar *self) {
  return self->isLuniSolar();
}

//  bool QHijriCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QHijriCalendar7isSolarEv(const QHijriCalendar *self) {
  return self->isSolar();
}

//  const QCalendarLocale *QHijriCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_ZNK14QHijriCalendar20localeMonthIndexDataEv(
    const QHijriCalendar *self) {
  return self->localeMonthIndexData();
}

//  const char16_t *QHijriCalendar::localeMonthData() const
extern "C" Q_DECL_EXPORT
const char16_t *ritual_ZNK14QHijriCalendar15localeMonthDataEv(
    const QHijriCalendar *self) {
  return self->localeMonthData();
}

//  a Python function taken by a CuteQHijriCalendar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHijriCalendar(
    QHijriCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHijriCalendar *>(self)->take(key, call);
}

//  int QHijriCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QHijriCalendar11daysInMonthEii(
    const QHijriCalendar *self,
    int month,
    int year) {
  return self->QHijriCalendar::daysInMonth(month, year);
}

//  int QHijriCalendar::maximumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QHijriCalendar18maximumDaysInMonthEv(
    const QHijriCalendar *self) {
  return self->QHijriCalendar::maximumDaysInMonth();
}

//  int QHijriCalendar::daysInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QHijriCalendar10daysInYearEi(
    const QHijriCalendar *self,
    int year) {
  return self->QHijriCalendar::daysInYear(year);
}

//  bool QHijriCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QHijriCalendar7isLunarEv(const QHijriCalendar *self) {
  return self->QHijriCalendar::isLunar();
}

//  bool QHijriCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QHijriCalendar11isLuniSolarEv(
    const QHijriCalendar *self) {
  return self->QHijriCalendar::isLuniSolar();
}

//  bool QHijriCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QHijriCalendar7isSolarEv(const QHijriCalendar *self) {
  return self->QHijriCalendar::isSolar();
}

//  const QCalendarLocale *QHijriCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_own_ZNK14QHijriCalendar20localeMonthIndexDataEv(
    const QHijriCalendar *self) {
  return static_cast<const OwnQHijriCalendar *>(self)->OwnQHijriCalendar::localeMonthIndexData();
}

//  const char16_t *QHijriCalendar::localeMonthData() const
extern "C" Q_DECL_EXPORT
const char16_t *ritual_own_ZNK14QHijriCalendar15localeMonthDataEv(
    const QHijriCalendar *self) {
  return static_cast<const OwnQHijriCalendar *>(self)->OwnQHijriCalendar::localeMonthData();
}

#endif  // QT_CONFIG(hijricalendar)
#endif  // QT_CONFIG(hijricalendar)
