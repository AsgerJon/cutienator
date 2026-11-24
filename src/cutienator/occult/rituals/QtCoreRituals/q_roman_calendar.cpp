//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qromancalendar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qromancalendar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <cstring>

//  Only a class built on QRomanCalendar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRomanCalendar : QRomanCalendar {
  using QRomanCalendar::localeMonthIndexData;
};

//  A QRomanCalendar that Python can take functions over in. Every QRomanCalendar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRomanCalendarCall0)(const void *, int, int, int *);
typedef int (*CuteQRomanCalendarCall1)(const void *, int *);
typedef bool (*CuteQRomanCalendarCall2)(const void *, int *);
typedef bool (*CuteQRomanCalendarCall3)(const void *, int *);
typedef bool (*CuteQRomanCalendarCall4)(const void *, int *);
typedef QString * (*CuteQRomanCalendarCall5)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQRomanCalendarCall6)(const void *, const QLocale *, int, int, int, int *);
typedef void * (*CuteQRomanCalendarCall7)(const void *, int *);
typedef QString * (*CuteQRomanCalendarCall8)(const void *, int *);
typedef int (*CuteQRomanCalendarCall9)(const void *, int, int *);
typedef int (*CuteQRomanCalendarCall10)(const void *, int, int *);
typedef bool (*CuteQRomanCalendarCall11)(const void *, int, int, int, int *);
typedef bool (*CuteQRomanCalendarCall12)(const void *, int, int *);
typedef bool (*CuteQRomanCalendarCall13)(const void *, int *);
typedef bool (*CuteQRomanCalendarCall14)(const void *, int *);
typedef int (*CuteQRomanCalendarCall15)(const void *, int *);
typedef int (*CuteQRomanCalendarCall16)(const void *, int *);
typedef const QCalendar::YearMonthDay * (*CuteQRomanCalendarCall17)(const void *, qint64, int *);
typedef int (*CuteQRomanCalendarCall18)(const void *, qint64, int *);
typedef qint64 (*CuteQRomanCalendarCall19)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQRomanCalendarCall20)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQRomanCalendarCall21)(const void *, const QLocale *, int, int, int *);
class CuteQRomanCalendar : public QRomanCalendar {
public:
  using QRomanCalendar::QRomanCalendar;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isLunarEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isLuniSolarEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend7isSolarEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
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
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
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

  //  int QRomanCalendar::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRomanCalendarCall0 call = reinterpret_cast<CuteQRomanCalendarCall0>(taken[0]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::daysInMonth(month, year);
  }

  //  int QRomanCalendar::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRomanCalendarCall1 call = reinterpret_cast<CuteQRomanCalendarCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::minimumDaysInMonth();
  }

  //  bool QRomanCalendar::isLunar() const
  bool isLunar() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRomanCalendarCall2 call = reinterpret_cast<CuteQRomanCalendarCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLunar();
  }

  //  bool QRomanCalendar::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRomanCalendarCall3 call = reinterpret_cast<CuteQRomanCalendarCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRomanCalendar::isLuniSolar();
  }

  //  bool QRomanCalendar::isSolar() const
  bool isSolar() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQRomanCalendarCall4 call = reinterpret_cast<CuteQRomanCalendarCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQRomanCalendarCall5 call = reinterpret_cast<CuteQRomanCalendarCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQRomanCalendarCall6 call = reinterpret_cast<CuteQRomanCalendarCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQRomanCalendarCall7 call = reinterpret_cast<CuteQRomanCalendarCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return QRomanCalendar::localeMonthIndexData();
  }

  //  QString QCalendarBackend::name() const
  QString name() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRomanCalendarCall8 call = reinterpret_cast<CuteQRomanCalendarCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QCalendarBackend::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRomanCalendarCall9 call = reinterpret_cast<CuteQRomanCalendarCall9>(taken[9]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::daysInYear(year);
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQRomanCalendarCall10 call = reinterpret_cast<CuteQRomanCalendarCall10>(taken[10]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRomanCalendarCall11 call = reinterpret_cast<CuteQRomanCalendarCall11>(taken[11]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQRomanCalendarCall12 call = reinterpret_cast<CuteQRomanCalendarCall12>(taken[12]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQRomanCalendarCall13 call = reinterpret_cast<CuteQRomanCalendarCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQRomanCalendarCall14 call = reinterpret_cast<CuteQRomanCalendarCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQRomanCalendarCall15 call = reinterpret_cast<CuteQRomanCalendarCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQRomanCalendarCall16 call = reinterpret_cast<CuteQRomanCalendarCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  QCalendar::YearMonthDay QCalendarBackend::julianDayToDate(qint64 jd)
  //      const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQRomanCalendarCall17 call = reinterpret_cast<CuteQRomanCalendarCall17>(taken[17]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQRomanCalendarCall18 call = reinterpret_cast<CuteQRomanCalendarCall18>(taken[18]);
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
      CuteQRomanCalendarCall19 call = reinterpret_cast<CuteQRomanCalendarCall19>(taken[19]);
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
      CuteQRomanCalendarCall20 call = reinterpret_cast<CuteQRomanCalendarCall20>(taken[20]);
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
      CuteQRomanCalendarCall21 call = reinterpret_cast<CuteQRomanCalendarCall21>(taken[21]);
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

//  int QRomanCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QRomanCalendar11daysInMonthEii(
    const QRomanCalendar *self,
    int month,
    int year) {
  return self->daysInMonth(month, year);
}

//  int QRomanCalendar::minimumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QRomanCalendar18minimumDaysInMonthEv(
    const QRomanCalendar *self) {
  return self->minimumDaysInMonth();
}

//  bool QRomanCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QRomanCalendar7isLunarEv(const QRomanCalendar *self) {
  return self->isLunar();
}

//  bool QRomanCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QRomanCalendar11isLuniSolarEv(const QRomanCalendar *self) {
  return self->isLuniSolar();
}

//  bool QRomanCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QRomanCalendar7isSolarEv(const QRomanCalendar *self) {
  return self->isSolar();
}

//  QString QRomanCalendar::monthName(const QLocale &locale, int month, int
//      year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QRomanCalendar9monthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QRomanCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(self->monthName(*locale, month, year, format));
}

//  QString QRomanCalendar::standaloneMonthName(const QLocale &locale, int
//      month, int year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QRomanCalendar19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QRomanCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->standaloneMonthName(
          *locale,
          month,
          year,
          format));
}

//  const QCalendarLocale *QRomanCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_ZNK14QRomanCalendar20localeMonthIndexDataEv(
    const QRomanCalendar *self) {
  return self->localeMonthIndexData();
}

//  a Python function taken by a CuteQRomanCalendar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRomanCalendar(
    QRomanCalendar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRomanCalendar *>(self)->take(key, call);
}

//  int QRomanCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QRomanCalendar11daysInMonthEii(
    const QRomanCalendar *self,
    int month,
    int year) {
  return self->QRomanCalendar::daysInMonth(month, year);
}

//  int QRomanCalendar::minimumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QRomanCalendar18minimumDaysInMonthEv(
    const QRomanCalendar *self) {
  return self->QRomanCalendar::minimumDaysInMonth();
}

//  bool QRomanCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QRomanCalendar7isLunarEv(const QRomanCalendar *self) {
  return self->QRomanCalendar::isLunar();
}

//  bool QRomanCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QRomanCalendar11isLuniSolarEv(
    const QRomanCalendar *self) {
  return self->QRomanCalendar::isLuniSolar();
}

//  bool QRomanCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QRomanCalendar7isSolarEv(const QRomanCalendar *self) {
  return self->QRomanCalendar::isSolar();
}

//  QString QRomanCalendar::monthName(const QLocale &locale, int month, int
//      year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QRomanCalendar9monthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QRomanCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->QRomanCalendar::monthName(
          *locale,
          month,
          year,
          format));
}

//  QString QRomanCalendar::standaloneMonthName(const QLocale &locale, int
//      month, int year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QRomanCalendar19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QRomanCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->QRomanCalendar::standaloneMonthName(
          *locale,
          month,
          year,
          format));
}

//  const QCalendarLocale *QRomanCalendar::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_own_ZNK14QRomanCalendar20localeMonthIndexDataEv(
    const QRomanCalendar *self) {
  return static_cast<const OwnQRomanCalendar *>(self)->OwnQRomanCalendar::localeMonthIndexData();
}
