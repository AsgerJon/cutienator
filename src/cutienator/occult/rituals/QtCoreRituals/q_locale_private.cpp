//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qglobal.h"
#if defined(Q_OS_MACOS)
#   include "private/qcore_mac_p.h"
#   include <CoreFoundation/CoreFoundation.h>
#endif
#include "qplatformdefs.h"
#include "qcalendar.h"
#include "qdatastream.h"
#include "qdebug.h"
#include "private/qduplicatetracker_p.h"
#include "qhashfunctions.h"
#include "qstring.h"
#include "qstringiterator_p.h"
#include "qlocale.h"
#include "qlocale_p.h"
#include "qlocale_tools_p.h"
#include <private/qtools_p.h>
#if QT_CONFIG(datetimeparser)
#include "private/qdatetimeparser_p.h"
#endif
#include "qnamespace.h"
#include "qdatetime.h"
#include "qstringlist.h"
#include "qvariant.h"
#include "qvarlengtharray.h"
#include "qstringbuilder.h"
#if QT_CONFIG(timezone)
#   include "qtimezone.h"
#endif
#include "private/qnumeric_p.h"
#include "private/qtools_p.h"
#include <cmath>
#ifndef QT_NO_SYSTEMLOCALE
#   include "qmutex.h"
#endif
#ifdef Q_OS_WIN
#   include <qt_windows.h>
#   include <time.h>
#endif
#include "private/qcalendarbackend_p.h"
#include "private/qgregoriancalendar_p.h"
#if QT_CONFIG(timezone) && QT_CONFIG(timezone_locale) && !QT_CONFIG(icu)
#   include "private/qtimezonelocale_p.h"
#endif
#if QT_CONFIG(datestring)
#   include "private/qttemporalpattern_p.h"
#endif
#include <q20iterator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
