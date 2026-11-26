//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtparsetemporal_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtparsetemporal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcalendar.h>
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qtparsetemporal_p.h>
#include <QtCore/private/qcalendarmath_p.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/private/qstringiterator_p.h>
#include <QtCore/private/qttemporalpattern_p.h>
#include <algorithm> // sort, stable_sort
#include <QtCore/qxpfunctional.h>
#include <optional>
#include <utility> // exchange, move, pair
#include <vector>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/parse/qtparsetemporal.cpp, line 940, as _ZNK15QtParseTemporal14ParsedTemporal4dateE9QCalendar5QDate
namespace QtParseTemporal {
inline QDate ParsedTemporal::date(QCalendar cal, QDate defaults) const
{
    if (defaults.isValid()) {
        QDate draft(year ? *year : defaults.year(cal), month ? month : defaults.month(cal),
                    dayOfMonth ? dayOfMonth : defaults.day(cal), cal);

        if (dayOfWeek && draft.isValid() && draft.dayOfWeek(cal) != dayOfWeek) {
            // Defaults conflict with parsed day of the week.
            if (!dayOfMonth) {
                // (Assumes no intercalary days.)
                // Number of days to the nearest with the right day of the week:
                const int offset = (dayOfWeek + 10 - draft.dayOfWeek(cal)) % 7 - 3;
                Q_ASSERT(offset != 0); // Otherwise, day of week matched, already.
                Q_ASSERT(-4 < offset && offset < 4);
                // Prefer closer unless nearby has more in common with what we asked for:
                QDate closer = draft.addDays(offset);
                QDate nearby = draft.addDays(offset < 0 ? offset + 7 : offset - 7);
                if (nearby.isValid()
                    && (!closer.isValid()
                        || (closer.dayOfWeek(cal) != dayOfWeek
                            && nearby.dayOfWeek(cal) == dayOfWeek)
                        || (closer.month(cal) != draft.month(cal)
                            && nearby.month(cal) == draft.month(cal)))) {
                    // (We could also give year(cal) the same treatment, but
                    // different year, for dates within ten days of one another,
                    // plies different month, so check would be redundant.)
                    std::swap(nearby, draft);
                } else if (closer.isValid() && closer.dayOfWeek(cal) == dayOfWeek) {
                    std::swap(closer, draft);
                }

            } else if (!month) {
                Q_ASSERT(draft.day() == dayOfMonth);
                auto use = [&draft, cal, dow=dayOfWeek](int yr, int mon, int day) {
                    QDate maybe(yr, mon, day, cal);
                    if (!maybe.isValid() || maybe.dayOfWeek(cal) != dow)
                        return false;
                    std::swap(maybe, draft);
                    return true;
                };
                // Find nearest month with the right dayOfMonth and dayOfWeek.
                // If year was specified we're limited to it; otherwise,
                // draft.year() is derived from defaults so the search can
                // spread to nearby years.
                int loYear = draft.year(cal), hiYear = loYear;
                int loMon = draft.month(cal), hiMon = loMon;
                bool maybeLo = true, maybeHi = true;
                while (maybeLo || maybeHi) {
                    if (maybeHi) {
                        if (hiMon < cal.monthsInYear(hiYear)) {
                            ++hiMon;
                        } else if (year) {
                            Q_ASSERT(hiYear == *year);
                            maybeHi = false;
                        } else if (hiYear + 1 || cal.hasYearZero()) {
                            ++hiYear;
                            hiMon = 1;
                        } else if (cal.isProleptic()) {
                            hiYear = +1;
                            hiMon = 1;
                        } else {
                            maybeHi = false;
                        }
                    }
                    if (maybeHi && use(hiYear, hiMon, dayOfMonth))
                        break;

                    if (maybeLo) {
                        if (loMon > 1) {
                            --loMon;
                        } else if (year) {
                            Q_ASSERT(loYear == *year);
                            maybeLo = false;
                        } else if (loYear - 1 || cal.hasYearZero()) {
                            --loYear;
                            loMon = cal.monthsInYear(loYear);
                        } else if (cal.isProleptic()) {
                            loYear = -1;
                            loMon = cal.monthsInYear(loYear);
                        } else {
                            maybeLo = false;
                        }
                    }
                    if (maybeLo && use(loYear, loMon, dayOfMonth))
                        break;

                    // Avoid looping for ever: if we can't find a match within a
                    // 30 year window we probably never shall. If we haven't
                    // found a match by then, the likelihood that the input has
                    // a typo in it is fairly high, in any case.
                    if (hiYear - loYear > 30)
                        break;
                }
            } else if (!year) {
                // As for resolve()'s handling of two-digit centuries:
                QCalendar::YearMonthDay ymd = { draft.year(cal), month, dayOfMonth };
                QDate maybe = cal.matchCenturyToWeekday(ymd, dayOfWeek);
                if (maybe.isValid() && maybe.dayOfWeek(cal) == dayOfWeek)
                    std::swap(maybe, draft);
            }
            if (draft.dayOfWeek(cal) != dayOfWeek)
                return {};
        }
        return draft;
    }
    if (year && month && dayOfMonth)
        return QDate(*year, month, dayOfMonth, cal);
    return {};
}
}  // namespace QtParseTemporal

//  from src/corelib/parse/qtparsetemporal.cpp, line 1050, as _ZNK15QtParseTemporal14ParsedTemporal4timeE5QTime
namespace QtParseTemporal {
inline QTime ParsedTemporal::time(QTime defaults) const
{
    if (defaults.isValid()) {
        int hr = defaults.hour();
        // hour: -1 means we have no information, less means unknown am, > 24 means unknown pm.
        if (hour < -1) // UnknownAmHour
            hr = hr % 12;
        else if (hour > 24) // UnknownPmHour
            hr = hr % 12 + 12;
        else if (hour >= 0)
            hr = hour;
        // (Note: hour == 24 is currently unused but may be relevant for 24:00:00 in future.)
        return QTime(hr,
                     minute < 0 ? defaults.minute() : minute,
                     second < 0 ? defaults.second() : second,
                     millis < 0 ? defaults.msec() : millis);
    }

    if (hour < 0 || hour > 24)
        return {};
    if (minute < 0)
        return QTime(hour, 0);
    if (second < 0)
        return QTime(hour, minute);
    if (millis < 0)
        return QTime(hour, minute, second);
    return QTime(hour, minute, second, millis);
}
}  // namespace QtParseTemporal
//  -----------------------------------------------------------------------

//  QDate QtParseTemporal::ParsedTemporal::date(QCalendar cal, QDate
//      defaults) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QtParseTemporal14ParsedTemporal4dateE9QCalendar5QDate(
    const QtParseTemporal::ParsedTemporal *self,
    const QCalendar *cal,
    const QDate *defaults) {
  return new QDate(self->date(*cal, *defaults));
}

//  QTime QtParseTemporal::ParsedTemporal::time(QTime defaults) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK15QtParseTemporal14ParsedTemporal4timeE5QTime(
    const QtParseTemporal::ParsedTemporal *self,
    const QTime *defaults) {
  return new QTime(self->time(*defaults));
}

//  QtParseTemporal::ParsedTemporal::~ParsedTemporal()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtParseTemporal14ParsedTemporalD1Ev(
    QtParseTemporal::ParsedTemporal *self) {
  delete self;
}

#endif  // QT_CONFIG(datetimeparser)
#endif  // QT_CONFIG(datetimeparser)
