//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdatetime_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetime_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QDateTime>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlocale.h>
#include <QtCore/qset.h>
#include <QtCore/private/qcalendarmath_p.h>
#include <QtCore/private/qdatetime_p.h>
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/private/qgregoriancalendar_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/private/qlocaltime_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/private/qstringiterator_p.h>
#if QT_CONFIG(timezone)
#endif
#if QT_CONFIG(datestring)
#  include <QtCore/private/qttemporalpattern_p.h>
#endif
#include <cmath>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#include <QtCore/private/qtools_p.h>
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

//  from src/corelib/time/qdatetime.cpp, line 2759, as local:qdatetime.cpp:QDateTimeData
typedef QDateTimePrivate::QDateTimeData QDateTimeData;

//  from src/corelib/time/qdatetime.cpp, line 2818, as local:qdatetime.cpp:millisInSystemRange
static inline bool millisInSystemRange(qint64 millis, qint64 slack = 0)
{
    static const auto bounds = QLocalTime::computeSystemMillisRange();
    return (bounds.minClip || millis >= bounds.min - slack)
        && (bounds.maxClip || millis <= bounds.max + slack);
}

//  from src/corelib/time/qdatetime.cpp, line 2982, as local:qdatetime.cpp:toTransitionOptions
constexpr static QDateTimePrivate::TransitionOptions
toTransitionOptions(QDateTime::TransitionResolution res)
{
    switch (res) {
    case QDateTime::TransitionResolution::RelativeToBefore:
        return QDateTimePrivate::GapUseAfter | QDateTimePrivate::FoldUseBefore;
    case QDateTime::TransitionResolution::RelativeToAfter:
        return QDateTimePrivate::GapUseBefore | QDateTimePrivate::FoldUseAfter;
    case QDateTime::TransitionResolution::PreferBefore:
        return QDateTimePrivate::GapUseBefore | QDateTimePrivate::FoldUseBefore;
    case QDateTime::TransitionResolution::PreferAfter:
        return QDateTimePrivate::GapUseAfter | QDateTimePrivate::FoldUseAfter;
    case QDateTime::TransitionResolution::PreferStandard:
        return QDateTimePrivate::GapUseBefore
            | QDateTimePrivate::FoldUseAfter
            | QDateTimePrivate::FlipForReverseDst;
    case QDateTime::TransitionResolution::PreferDaylightSaving:
        return QDateTimePrivate::GapUseAfter
            | QDateTimePrivate::FoldUseBefore
            | QDateTimePrivate::FlipForReverseDst;
    case QDateTime::TransitionResolution::Reject: break;
    }
    return {};
}

//  from src/corelib/time/qdatetime.cpp, line 3135, as local:qdatetime.cpp:extractSpec
static constexpr inline Qt::TimeSpec extractSpec(QDateTimePrivate::StatusFlags status)
{
    return Qt::TimeSpec((status & QDateTimePrivate::TimeSpecMask).toInt() >> QDateTimePrivate::TimeSpecShift);
}

//  from src/corelib/time/qdatetime.cpp, line 3174, as local:qdatetime.cpp:getStatus
static inline QDateTimePrivate::StatusFlags getStatus(const QDateTimeData &d)
{
    if (d.isShort()) {
        // same as, but producing better code
        //return StatusFlag(d.data.status);
        return QDateTimePrivate::StatusFlag(qintptr(d.d) & 0xFF);
    }
    return d->m_status;
}

//  from src/corelib/time/qdatetime.cpp, line 3300, as local:qdatetime.cpp:refreshSimpleDateTime
static void refreshSimpleDateTime(QDateTimeData &d)
{
    auto status = getStatus(d);
    Q_ASSERT(QTimeZone::isUtcOrFixedOffset(extractSpec(status)));
    status.setFlag(QDateTimePrivate::ValidDateTime,
                   status.testFlags(QDateTimePrivate::ValidDate | QDateTimePrivate::ValidTime));

    if (status.testFlag(QDateTimePrivate::ShortData))
        d.data.status = status.toInt();
    else
        d->m_status = status;
}

//  from src/corelib/time/qdatetime.cpp, line 3527, as _ZN9QDateTime4DataD1Ev
inline QDateTime::Data::~Data()
{
    if (!isShort() && !d->ref.deref())
        delete d;
}

//  from src/corelib/time/qdatetime.cpp, line 3533, as _ZNK9QDateTime4Data7isShortEv
inline bool QDateTime::Data::isShort() const
{
    bool b = quintptr(d) & QDateTimePrivate::ShortData;

    // sanity check:
    Q_ASSERT(b || !d->m_status.testFlag(QDateTimePrivate::ShortData));

    // even if CanBeSmall = false, we have short data for a default-constructed
    // QDateTime object. But it's unlikely.
    if constexpr (CanBeSmall)
        return Q_LIKELY(b);
    return Q_UNLIKELY(b);
}
//  -----------------------------------------------------------------------

//  QDateTimePrivate::~QDateTimePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDateTimePrivateD1Ev(QDateTimePrivate *self) {
  delete self;
}

//  a QDateTime::Data a ritual of QDateTimePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDateTimePrivate__QDateTime_Data(QDateTime::Data *self) {
  delete self;
}
