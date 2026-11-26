//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstringview.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCalendarBackend that Python can take functions over in. Every QCalendarBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQCalendarBackendCall0)(const void *, int *);
typedef int (*CuteQCalendarBackendCall1)(const void *, int, int, int *);
typedef int (*CuteQCalendarBackendCall2)(const void *, int, int *);
typedef int (*CuteQCalendarBackendCall3)(const void *, int, int *);
typedef bool (*CuteQCalendarBackendCall4)(const void *, int, int, int, int *);
typedef bool (*CuteQCalendarBackendCall5)(const void *, int, int *);
typedef bool (*CuteQCalendarBackendCall6)(const void *, int *);
typedef bool (*CuteQCalendarBackendCall7)(const void *, int *);
typedef bool (*CuteQCalendarBackendCall8)(const void *, int *);
typedef bool (*CuteQCalendarBackendCall9)(const void *, int *);
typedef bool (*CuteQCalendarBackendCall10)(const void *, int *);
typedef int (*CuteQCalendarBackendCall11)(const void *, int *);
typedef int (*CuteQCalendarBackendCall12)(const void *, int *);
typedef int (*CuteQCalendarBackendCall13)(const void *, int *);
typedef const QCalendar::YearMonthDay * (*CuteQCalendarBackendCall14)(const void *, qint64, int *);
typedef int (*CuteQCalendarBackendCall15)(const void *, qint64, int *);
typedef qint64 (*CuteQCalendarBackendCall16)(const void *, const QCalendar::YearMonthDay *, int, int *);
typedef QString * (*CuteQCalendarBackendCall17)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQCalendarBackendCall18)(const void *, const QLocale *, int, int, int, int *);
typedef QString * (*CuteQCalendarBackendCall19)(const void *, const QLocale *, int, int, int *);
typedef QString * (*CuteQCalendarBackendCall20)(const void *, const QLocale *, int, int, int *);
typedef void * (*CuteQCalendarBackendCall21)(const void *, int *);
typedef void * (*CuteQCalendarBackendCall22)(const void *, int *);
class CuteQCalendarBackend : public QCalendarBackend {
public:
  using QCalendarBackend::QCalendarBackend;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QCalendarBackend4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11daysInMonthEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10daysInYearEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend12monthsInYearEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isDateValidEiii")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend10isLeapYearEi")) {
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
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11isProlepticEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11hasYearZeroEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18maximumDaysInMonthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend18minimumDaysInMonthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19maximumMonthsInYearEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15julianDayToDateEx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9dayOfWeekEx")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend20localeMonthIndexDataEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QCalendarBackend15localeMonthDataEv")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  QString QCalendarBackend::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCalendarBackendCall0 call = reinterpret_cast<CuteQCalendarBackendCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QCalendarBackend::daysInMonth(int month, int year) const
  int daysInMonth(int month, int year) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCalendarBackendCall1 call = reinterpret_cast<CuteQCalendarBackendCall1>(taken[1]);
      int given = call(this, month, year, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QCalendarBackend::daysInYear(int year) const
  int daysInYear(int year) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCalendarBackendCall2 call = reinterpret_cast<CuteQCalendarBackendCall2>(taken[2]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::daysInYear(year);
  }

  //  int QCalendarBackend::monthsInYear(int year) const
  int monthsInYear(int year) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCalendarBackendCall3 call = reinterpret_cast<CuteQCalendarBackendCall3>(taken[3]);
      int given = call(this, year, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::monthsInYear(year);
  }

  //  bool QCalendarBackend::isDateValid(int year, int month, int day)
  //      const
  bool isDateValid(int year, int month, int day) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCalendarBackendCall4 call = reinterpret_cast<CuteQCalendarBackendCall4>(taken[4]);
      bool given = call(this, year, month, day, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isDateValid(year, month, day);
  }

  //  bool QCalendarBackend::isLeapYear(int year) const
  bool isLeapYear(int year) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCalendarBackendCall5 call = reinterpret_cast<CuteQCalendarBackendCall5>(taken[5]);
      bool given = call(this, year, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isLunar() const
  bool isLunar() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQCalendarBackendCall6 call = reinterpret_cast<CuteQCalendarBackendCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isLuniSolar() const
  bool isLuniSolar() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCalendarBackendCall7 call = reinterpret_cast<CuteQCalendarBackendCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isSolar() const
  bool isSolar() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCalendarBackendCall8 call = reinterpret_cast<CuteQCalendarBackendCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QCalendarBackend::isProleptic() const
  bool isProleptic() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCalendarBackendCall9 call = reinterpret_cast<CuteQCalendarBackendCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::isProleptic();
  }

  //  bool QCalendarBackend::hasYearZero() const
  bool hasYearZero() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCalendarBackendCall10 call = reinterpret_cast<CuteQCalendarBackendCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::hasYearZero();
  }

  //  int QCalendarBackend::maximumDaysInMonth() const
  int maximumDaysInMonth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQCalendarBackendCall11 call = reinterpret_cast<CuteQCalendarBackendCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumDaysInMonth();
  }

  //  int QCalendarBackend::minimumDaysInMonth() const
  int minimumDaysInMonth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQCalendarBackendCall12 call = reinterpret_cast<CuteQCalendarBackendCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::minimumDaysInMonth();
  }

  //  int QCalendarBackend::maximumMonthsInYear() const
  int maximumMonthsInYear() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQCalendarBackendCall13 call = reinterpret_cast<CuteQCalendarBackendCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCalendarBackend::maximumMonthsInYear();
  }

  //  QCalendar::YearMonthDay QCalendarBackend::julianDayToDate(qint64 jd)
  //      const
  QCalendar::YearMonthDay julianDayToDate(qint64 jd) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQCalendarBackendCall14 call = reinterpret_cast<CuteQCalendarBackendCall14>(taken[14]);
      const QCalendar::YearMonthDay * given = call(this, jd, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QCalendarBackend::dayOfWeek(qint64 jd) const
  int dayOfWeek(qint64 jd) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQCalendarBackendCall15 call = reinterpret_cast<CuteQCalendarBackendCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQCalendarBackendCall16 call = reinterpret_cast<CuteQCalendarBackendCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQCalendarBackendCall17 call = reinterpret_cast<CuteQCalendarBackendCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQCalendarBackendCall18 call = reinterpret_cast<CuteQCalendarBackendCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQCalendarBackendCall19 call = reinterpret_cast<CuteQCalendarBackendCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQCalendarBackendCall20 call = reinterpret_cast<CuteQCalendarBackendCall20>(taken[20]);
      QString * given = call(this, &locale, day, static_cast<int>(format), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCalendarBackend::standaloneWeekDayName(locale, day, format);
  }

  //  const QCalendarLocale *QCalendarBackend::localeMonthIndexData() const
  const QCalendarLocale *localeMonthIndexData() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQCalendarBackendCall21 call = reinterpret_cast<CuteQCalendarBackendCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QCalendarLocale *>(given);
    }
    return {};
  }

  //  const char16_t *QCalendarBackend::localeMonthData() const
  const char16_t *localeMonthData() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQCalendarBackendCall22 call = reinterpret_cast<CuteQCalendarBackendCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const char16_t *>(given);
    }
    return {};
  }
};

//  QCalendarBackend::~QCalendarBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCalendarBackendD1Ev(QCalendarBackend *self) {
  delete self;
}

//  QString QCalendarBackend::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend4nameEv(const QCalendarBackend *self) {
  return new QString(self->name());
}

//  QStringList QCalendarBackend::names() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QCalendarBackend5namesEv(
    const QCalendarBackend *self) {
  return new QList<QString>(self->names());
}

//  QCalendar::System QCalendarBackend::calendarSystem() const
extern "C" Q_DECL_EXPORT
QCalendar::System ritual_ZNK16QCalendarBackend14calendarSystemEv(
    const QCalendarBackend *self) {
  return self->calendarSystem();
}

//  QCalendar::SystemId QCalendarBackend::calendarId() const
extern "C" Q_DECL_EXPORT
QCalendar::SystemId *ritual_ZNK16QCalendarBackend10calendarIdEv(
    const QCalendarBackend *self) {
  return new QCalendar::SystemId(self->calendarId());
}

//  int QCalendarBackend::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend11daysInMonthEii(
    const QCalendarBackend *self,
    int month,
    int year) {
  return self->daysInMonth(month, year);
}

//  int QCalendarBackend::daysInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend10daysInYearEi(
    const QCalendarBackend *self,
    int year) {
  return self->daysInYear(year);
}

//  int QCalendarBackend::monthsInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend12monthsInYearEi(
    const QCalendarBackend *self,
    int year) {
  return self->monthsInYear(year);
}

//  bool QCalendarBackend::isDateValid(int year, int month, int day) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend11isDateValidEiii(
    const QCalendarBackend *self,
    int year,
    int month,
    int day) {
  return self->isDateValid(year, month, day);
}

//  bool QCalendarBackend::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend10isLeapYearEi(
    const QCalendarBackend *self,
    int year) {
  return self->isLeapYear(year);
}

//  bool QCalendarBackend::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend7isLunarEv(const QCalendarBackend *self) {
  return self->isLunar();
}

//  bool QCalendarBackend::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend11isLuniSolarEv(
    const QCalendarBackend *self) {
  return self->isLuniSolar();
}

//  bool QCalendarBackend::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend7isSolarEv(const QCalendarBackend *self) {
  return self->isSolar();
}

//  bool QCalendarBackend::isProleptic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend11isProlepticEv(
    const QCalendarBackend *self) {
  return self->isProleptic();
}

//  bool QCalendarBackend::hasYearZero() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend11hasYearZeroEv(
    const QCalendarBackend *self) {
  return self->hasYearZero();
}

//  int QCalendarBackend::maximumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend18maximumDaysInMonthEv(
    const QCalendarBackend *self) {
  return self->maximumDaysInMonth();
}

//  int QCalendarBackend::minimumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend18minimumDaysInMonthEv(
    const QCalendarBackend *self) {
  return self->minimumDaysInMonth();
}

//  int QCalendarBackend::maximumMonthsInYear() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend19maximumMonthsInYearEv(
    const QCalendarBackend *self) {
  return self->maximumMonthsInYear();
}

//  bool QCalendarBackend::dateToJulianDay(int year, int month, int day,
//      qint64 *jd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend15dateToJulianDayEiiiPx(
    const QCalendarBackend *self,
    int year,
    int month,
    int day,
    qint64 *jd) {
  return self->dateToJulianDay(year, month, day, jd);
}

//  QCalendar::YearMonthDay QCalendarBackend::julianDayToDate(qint64 jd)
//      const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK16QCalendarBackend15julianDayToDateEx(
    const QCalendarBackend *self,
    qint64 jd) {
  return new QCalendar::YearMonthDay(self->julianDayToDate(jd));
}

//  int QCalendarBackend::dayOfWeek(qint64 jd) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCalendarBackend9dayOfWeekEx(
    const QCalendarBackend *self,
    qint64 jd) {
  return self->dayOfWeek(jd);
}

//  qint64 QCalendarBackend::matchCenturyToWeekday(const
//      QCalendar::YearMonthDay &parts, int dow) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi(
    const QCalendarBackend *self,
    const QCalendar::YearMonthDay *parts,
    int dow) {
  return self->matchCenturyToWeekday(*parts, dow);
}

//  QString QCalendarBackend::monthName(const QLocale &locale, int month, int
//      year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(self->monthName(*locale, month, year, format));
}

//  QString QCalendarBackend::standaloneMonthName(const QLocale &locale, int
//      month, int year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendarBackend *self,
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

//  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(self->weekDayName(*locale, day, format));
}

//  QString QCalendarBackend::standaloneWeekDayName(const QLocale &locale,
//      int day, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(self->standaloneWeekDayName(*locale, day, format));
}

//  QString QCalendarBackend::dateTimeToString(QStringView format, const
//      QDateTime &datetime, QDate dateOnly, QTime timeOnly, const QLocale
//      &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCalendarBackend16dateTimeToStringE11QStringViewRK9QDateTime5QDate5QTimeRK7QLocale(
    const QCalendarBackend *self,
    const QString *format,
    const QDateTime *datetime,
    const QDate *dateOnly,
    const QTime *timeOnly,
    const QLocale *locale) {
  return new QString(
      self->dateTimeToString(
          QStringView(*format),
          *datetime,
          *dateOnly,
          *timeOnly,
          *locale));
}

//  bool QCalendarBackend::isGregorian() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCalendarBackend11isGregorianEv(
    const QCalendarBackend *self) {
  return self->isGregorian();
}

//  QCalendar::SystemId QCalendarBackend::registerCustomBackend(const
//      QStringList &names)
extern "C" Q_DECL_EXPORT
QCalendar::SystemId *ritual_ZN16QCalendarBackend21registerCustomBackendERK5QListI7QStringE(
    QCalendarBackend *self,
    const QList<QString> *names) {
  return new QCalendar::SystemId(self->registerCustomBackend(*names));
}

//  QStringList QCalendarBackend::availableCalendars()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QCalendarBackend18availableCalendarsEv() {
  return new QList<QString>(QCalendarBackend::availableCalendars());
}

//  const QCalendarLocale *QCalendarBackend::localeMonthIndexData() const
extern "C" Q_DECL_EXPORT
const QCalendarLocale *ritual_ZNK16QCalendarBackend20localeMonthIndexDataEv(
    const QCalendarBackend *self) {
  return self->localeMonthIndexData();
}

//  const char16_t *QCalendarBackend::localeMonthData() const
extern "C" Q_DECL_EXPORT
const char16_t *ritual_ZNK16QCalendarBackend15localeMonthDataEv(
    const QCalendarBackend *self) {
  return self->localeMonthData();
}

//  void QCalendarBackend::setIndex(size_t index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCalendarBackend8setIndexEm(
    QCalendarBackend *self,
    size_t index) {
  self->setIndex(index);
}

//  const QCalendarBackend *QCalendarBackend::fromName(QAnyStringView name)
extern "C" Q_DECL_EXPORT
const QCalendarBackend *ritual_ZN16QCalendarBackend8fromNameE14QAnyStringView(
    const QString *name) {
  return QCalendarBackend::fromName(QAnyStringView(*name));
}

//  const QCalendarBackend *QCalendarBackend::fromId(QCalendar::SystemId id)
extern "C" Q_DECL_EXPORT
const QCalendarBackend *ritual_ZN16QCalendarBackend6fromIdEN9QCalendar8SystemIdE(
    const QCalendar::SystemId *id) {
  return QCalendarBackend::fromId(*id);
}

//  const QCalendarBackend *QCalendarBackend::fromEnum(QCalendar::System
//      system)
extern "C" Q_DECL_EXPORT
const QCalendarBackend *ritual_ZN16QCalendarBackend8fromEnumEN9QCalendar6SystemE(
    QCalendar::System system) {
  return QCalendarBackend::fromEnum(system);
}

//  const QCalendarBackend *QCalendarBackend::gregorian()
extern "C" Q_DECL_EXPORT
const QCalendarBackend *ritual_ZN16QCalendarBackend9gregorianEv() {
  return QCalendarBackend::gregorian();
}

//  a Python function taken by a CuteQCalendarBackend, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCalendarBackend(
    QCalendarBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCalendarBackend *>(self)->take(key, call);
}

//  int QCalendarBackend::daysInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend10daysInYearEi(
    const QCalendarBackend *self,
    int year) {
  return self->QCalendarBackend::daysInYear(year);
}

//  int QCalendarBackend::monthsInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend12monthsInYearEi(
    const QCalendarBackend *self,
    int year) {
  return self->QCalendarBackend::monthsInYear(year);
}

//  bool QCalendarBackend::isDateValid(int year, int month, int day) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QCalendarBackend11isDateValidEiii(
    const QCalendarBackend *self,
    int year,
    int month,
    int day) {
  return self->QCalendarBackend::isDateValid(year, month, day);
}

//  bool QCalendarBackend::isProleptic() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QCalendarBackend11isProlepticEv(
    const QCalendarBackend *self) {
  return self->QCalendarBackend::isProleptic();
}

//  bool QCalendarBackend::hasYearZero() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QCalendarBackend11hasYearZeroEv(
    const QCalendarBackend *self) {
  return self->QCalendarBackend::hasYearZero();
}

//  int QCalendarBackend::maximumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend18maximumDaysInMonthEv(
    const QCalendarBackend *self) {
  return self->QCalendarBackend::maximumDaysInMonth();
}

//  int QCalendarBackend::minimumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend18minimumDaysInMonthEv(
    const QCalendarBackend *self) {
  return self->QCalendarBackend::minimumDaysInMonth();
}

//  int QCalendarBackend::maximumMonthsInYear() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend19maximumMonthsInYearEv(
    const QCalendarBackend *self) {
  return self->QCalendarBackend::maximumMonthsInYear();
}

//  int QCalendarBackend::dayOfWeek(qint64 jd) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCalendarBackend9dayOfWeekEx(
    const QCalendarBackend *self,
    qint64 jd) {
  return self->QCalendarBackend::dayOfWeek(jd);
}

//  qint64 QCalendarBackend::matchCenturyToWeekday(const
//      QCalendar::YearMonthDay &parts, int dow) const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12YearMonthDayEi(
    const QCalendarBackend *self,
    const QCalendar::YearMonthDay *parts,
    int dow) {
  return self->QCalendarBackend::matchCenturyToWeekday(*parts, dow);
}

//  QString QCalendarBackend::monthName(const QLocale &locale, int month, int
//      year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->QCalendarBackend::monthName(
          *locale,
          month,
          year,
          format));
}

//  QString QCalendarBackend::standaloneMonthName(const QLocale &locale, int
//      month, int year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->QCalendarBackend::standaloneMonthName(
          *locale,
          month,
          year,
          format));
}

//  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(
      self->QCalendarBackend::weekDayName(
          *locale,
          day,
          format));
}

//  QString QCalendarBackend::standaloneWeekDayName(const QLocale &locale,
//      int day, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendarBackend *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(
      self->QCalendarBackend::standaloneWeekDayName(
          *locale,
          day,
          format));
}
