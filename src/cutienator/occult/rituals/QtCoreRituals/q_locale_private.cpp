//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <array>
#include <QtCore/QLocale>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#if defined(Q_OS_MACOS)
#   include <QtCore/private/qcore_mac_p.h>
#   include <CoreFoundation/CoreFoundation.h>
#endif
#include "qplatformdefs.h"
#include <QtCore/qcalendar.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/qhashfunctions.h>
#include <QtCore/qstring.h>
#include <QtCore/private/qstringiterator_p.h>
#include <QtCore/qlocale.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/private/qtools_p.h>
#if QT_CONFIG(datetimeparser)
#include <QtCore/private/qdatetimeparser_p.h>
#endif
#include <QtCore/qnamespace.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qvariant.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qstringbuilder.h>
#if QT_CONFIG(timezone)
#   include <QtCore/qtimezone.h>
#endif
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qtools_p.h>
#include <cmath>
#ifndef QT_NO_SYSTEMLOCALE
#   include <QtCore/qmutex.h>
#endif
#ifdef Q_OS_WIN
#   include <QtCore/qt_windows.h>
#   include <time.h>
#endif
#include <QtCore/private/qcalendarbackend_p.h>
#include <QtCore/private/qgregoriancalendar_p.h>
#if QT_CONFIG(timezone) && QT_CONFIG(timezone_locale) && !QT_CONFIG(icu)
#   include <QtCore/private/qtimezonelocale_p.h>
#endif
#if QT_CONFIG(datestring)
#   include <QtCore/private/qttemporalpattern_p.h>
#endif
#include <QtCore/q20iterator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/text/qlocale.cpp, line 419, as _ZNK9QLocaleId24withLikelySubtagsRemovedEv
inline QLocaleId QLocaleId::withLikelySubtagsRemoved() const noexcept
{
    QLocaleId max = withLikelySubtagsAdded();
    // language
    {
        QLocaleId id { language_id, 0, 0 };
        if (id.withLikelySubtagsAdded() == max)
            return id;
    }
    // language_region
    if (territory_id) {
        QLocaleId id { language_id, 0, territory_id };
        if (id.withLikelySubtagsAdded() == max)
            return id;
    }
    // language_script
    if (script_id) {
        QLocaleId id { language_id, script_id, 0 };
        if (id.withLikelySubtagsAdded() == max)
            return id;
    }
    return max;
}

//  from src/corelib/text/qlocale.cpp, line 3549, as _ZNK14QLocalePrivate17measurementSystemEv
inline QLocale::MeasurementSystem QLocalePrivate::measurementSystem() const
{
    /* Unicode CLDR's information about measurement systems doesn't say which to
       use by default in each locale. Even if it did, adding another entry in
       every locale's row of locale_data[] would take up much more memory than
       the small table below.
    */
    struct TerritoryLanguage
    {
        quint16 languageId;
        quint16 territoryId;
        QLocale::MeasurementSystem system;
    };
    // TODO: research how realistic and/or complete this is:
    constexpr TerritoryLanguage ImperialMeasurementSystems[] = {
        { QLocale::English, QLocale::UnitedStates, QLocale::ImperialUSSystem },
        { QLocale::English, QLocale::UnitedStatesMinorOutlyingIslands, QLocale::ImperialUSSystem },
        { QLocale::Spanish, QLocale::UnitedStates, QLocale::ImperialUSSystem },
        { QLocale::Hawaiian, QLocale::UnitedStates, QLocale::ImperialUSSystem },
        { QLocale::English, QLocale::UnitedKingdom, QLocale::ImperialUKSystem }
    };

    for (const auto &system : ImperialMeasurementSystems) {
        if (system.languageId == m_data->m_language_id
            && system.territoryId == m_data->m_territory_id) {
            return system.system;
        }
    }
    return QLocale::MetricSystem;
}
//  -----------------------------------------------------------------------

//  QLocalePrivate::QLocalePrivate(const QLocaleData *data, qsizetype index,
//      QLocale::NumberOptions numberOptions, int refs)
extern "C" Q_DECL_EXPORT
QLocalePrivate *ritual_ZN14QLocalePrivateC1EPK11QLocaleDatax6QFlagsIN7QLocale12NumberOptionEEi(
    const QLocaleData *data,
    qsizetype index,
    int numberOptions,
    int refs) {
  return new QLocalePrivate(
      data,
      index,
      QFlags<QLocale::NumberOption>::fromInt(numberOptions),
      refs);
}

//  quint16 QLocalePrivate::languageId() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK14QLocalePrivate10languageIdEv(
    const QLocalePrivate *self) {
  return self->languageId();
}

//  quint16 QLocalePrivate::territoryId() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK14QLocalePrivate11territoryIdEv(
    const QLocalePrivate *self) {
  return self->territoryId();
}

//  const QLocalePrivate *QLocalePrivate::get(const QLocale &l)
extern "C" Q_DECL_EXPORT
const QLocalePrivate *ritual_ZN14QLocalePrivate3getERK7QLocale(
    const QLocale *l) {
  return QLocalePrivate::get(*l);
}

//  QLocale::MeasurementSystem QLocalePrivate::measurementSystem() const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK14QLocalePrivate17measurementSystemEv(
    const QLocalePrivate *self) {
  return self->measurementSystem();
}

//  a std::array<char, 4> a ritual of QLocalePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLocalePrivate__std_array_char_4(
    std::array<char, 4> *self) {
  delete self;
}

//  a QLocale::Territory a ritual of QLocalePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLocalePrivate__QLocale_Territory(
    QLocale::Territory *self) {
  delete self;
}
