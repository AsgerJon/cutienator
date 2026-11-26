//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeosatelliteinfo.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qnmeasatelliteinfosource.h>
#include <QtPositioning/private/qnmeasatelliteinfosource_p.h>
#include <QtPositioning/private/qgeosatelliteinfo_p.h>
#include <QtPositioning/private/qgeosatelliteinfosource_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtCore/QIODevice>
#include <QtCore/QBasicTimer>
#include <QtCore/QTimerEvent>
#include <QtCore/QTimer>
#include <array>
#include <QtCore/QDebug>
#include <QtCore/QtNumeric>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 657, as _ZNK24QNmeaSatelliteInfoUpdate18allSatellitesInUseEv
inline QList<QGeoSatelliteInfo> QNmeaSatelliteInfoUpdate::allSatellitesInUse() const
{
    QList<QGeoSatelliteInfo> result;
    for (const auto &s : m_satellites)
        result.append(s.satellitesInUse);
    return result;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 665, as _ZNK24QNmeaSatelliteInfoUpdate19allSatellitesInViewEv
inline QList<QGeoSatelliteInfo> QNmeaSatelliteInfoUpdate::allSatellitesInView() const
{
    QList<QGeoSatelliteInfo> result;
    for (const auto &s : m_satellites)
        result.append(s.satellitesInView);
    return result;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 673, as _ZN24QNmeaSatelliteInfoUpdate19setSatellitesInViewEN17QGeoSatelliteInfo15SatelliteSystemERK5QListIS0_E
inline void QNmeaSatelliteInfoUpdate::setSatellitesInView(QGeoSatelliteInfo::SatelliteSystem system,
                                                   const QList<QGeoSatelliteInfo> &inView)
{
    auto &info = m_satellites[system];
    info.updatingGSV = false;

    info.satellitesInView = inView;
    info.validInView = true;

    if (!info.satellitesInUseReceived) {
        // Normally a GSA message should come after a GSV message. If this flag
        // is not set, we have received 2 consecutive GSV messages for this
        // system without a GSA in between.
        // This means that we could actually receive a $GNGSA empty message for
        // this specific type. As it had no ids and GN talker id, we could not
        // determine system type. This most probably means that we have no
        // satellites in use for this system type.
        // Clear satellites in use, if any.
        info.satellitesInUse.clear();
        info.inUseIds.clear();
        info.validInUse = true;
    }
    info.satellitesInUseReceived = false;

    if (info.satellitesInView.isEmpty()) {
        // If we received an empty list of satellites in view, then the list of
        // satellites in use will also be empty, so we would not be able to
        // match it with correct system type in case of $GNGSA message. Clear
        // the list in advance.
        info.satellitesInUse.clear();
        info.inUseIds.clear();
        info.validInUse = true;
    } else if (!info.inUseIds.isEmpty()) {
        // We have some satellites in use cached. Check if we have received the
        // proper GSV for them.
        info.satellitesInUse.clear();
        info.validInUse = false;
        bool corrupt = false;
        const auto inUseIds = std::exchange(info.inUseIds, {});
        for (const auto id : inUseIds) {
            bool found = false;
            for (const auto &s : std::as_const(info.satellitesInView)) {
                if (s.satelliteIdentifier() == id) {
                    info.satellitesInUse.append(s);
                    found = true;
                    break;
                }
            }
            if (!found) {
                // The previoulsy received GSA is incorrect or not related to
                // this GSV
                info.satellitesInUse.clear();
                corrupt = true;
                break;
            }
        }
        info.validInUse = !corrupt;
    }

    m_validInUse = calculateValidInUse();
    m_validInView = calculateValidInView();
    m_fresh = true;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 737, as _ZN24QNmeaSatelliteInfoUpdate18setSatellitesInUseEN17QGeoSatelliteInfo15SatelliteSystemERK5QListIiE
inline bool QNmeaSatelliteInfoUpdate::setSatellitesInUse(QGeoSatelliteInfo::SatelliteSystem system,
                                                  const QList<int> &inUse)
{
    if (system == QGeoSatelliteInfo::Undefined || system == QGeoSatelliteInfo::Multiple)
        return false; // No way to determine satellite system

    SatelliteInfo &info = m_satellites[system];
    info.satellitesInUse.clear();

    info.satellitesInUseReceived = true;
    info.inUseIds = inUse;

    if (info.updatingGSV) {
        info.validInView = false;
        m_validInView = false;
        return false;
    }

    for (const auto id : inUse) {
        bool found = false;
        for (const auto &s : std::as_const(info.satellitesInView)) {
            if (s.satelliteIdentifier() == id) {
                info.satellitesInUse.append(s);
                found = true;
                break;
            }
        }
        if (!found) {
            // satellites in use are not in view -> related GSV is not yet received
            info.satellitesInView.clear();
            info.validInView = false;
            m_validInView = false;
            return false;
        }
    }

    info.inUseIds.clear(); // make sure we remove all obsolete cache

    info.validInUse = true;
    m_fresh = true;
    m_validInUse = calculateValidInUse();

    return true;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 782, as _ZN24QNmeaSatelliteInfoUpdate7consumeEv
inline void QNmeaSatelliteInfoUpdate::consume()
{
    m_fresh = false;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 787, as _ZNK24QNmeaSatelliteInfoUpdate7isFreshEv
inline bool QNmeaSatelliteInfoUpdate::isFresh() const
{
    return m_fresh;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 792, as _ZN24QNmeaSatelliteInfoUpdate5clearEv
inline void QNmeaSatelliteInfoUpdate::clear()
{
    m_satellites.clear();
    m_satellitesInViewParsed.clear();
    m_validInView = false;
    m_validInUse = false;
    m_fresh = false;
#if USE_SATELLITE_NMEA_PIMPL
    gsa.clear();
    gsv.clear();
#endif
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 805, as _ZNK24QNmeaSatelliteInfoUpdate7isValidEv
inline bool QNmeaSatelliteInfoUpdate::isValid() const
{
    // GSV without GSA is valid. GSA with outdated but still matching GSV also valid.
    return m_validInView || m_validInUse;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 811, as _ZNK24QNmeaSatelliteInfoUpdate19calculateValidInUseEv
inline bool QNmeaSatelliteInfoUpdate::calculateValidInUse() const
{
    for (const auto &s : m_satellites) {
        if (!s.validInUse)
            return false;
    }
    return true;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 820, as _ZNK24QNmeaSatelliteInfoUpdate20calculateValidInViewEv
inline bool QNmeaSatelliteInfoUpdate::calculateValidInView() const
{
    for (const auto &s : m_satellites) {
        if (!s.validInView)
            return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QList<QGeoSatelliteInfo> QNmeaSatelliteInfoUpdate::allSatellitesInUse()
//      const
extern "C" Q_DECL_EXPORT
QList<QGeoSatelliteInfo> *ritual_ZNK24QNmeaSatelliteInfoUpdate18allSatellitesInUseEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return new QList<QGeoSatelliteInfo>(self->allSatellitesInUse());
}

//  QList<QGeoSatelliteInfo> QNmeaSatelliteInfoUpdate::allSatellitesInView()
//      const
extern "C" Q_DECL_EXPORT
QList<QGeoSatelliteInfo> *ritual_ZNK24QNmeaSatelliteInfoUpdate19allSatellitesInViewEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return new QList<QGeoSatelliteInfo>(self->allSatellitesInView());
}

//  void QNmeaSatelliteInfoUpdate::setSatellitesInView(QGeoSatelliteInfo::Sat
//      elliteSystem system, const QList<QGeoSatelliteInfo> &inView)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoUpdate19setSatellitesInViewEN17QGeoSatelliteInfo15SatelliteSystemERK5QListIS0_E(
    QNmeaSatelliteInfoUpdate *self,
    QGeoSatelliteInfo::SatelliteSystem system,
    const QList<QGeoSatelliteInfo> *inView) {
  self->setSatellitesInView(system, *inView);
}

//  bool QNmeaSatelliteInfoUpdate::setSatellitesInUse(QGeoSatelliteInfo::Sate
//      lliteSystem system, const QList<int> &inUse)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNmeaSatelliteInfoUpdate18setSatellitesInUseEN17QGeoSatelliteInfo15SatelliteSystemERK5QListIiE(
    QNmeaSatelliteInfoUpdate *self,
    QGeoSatelliteInfo::SatelliteSystem system,
    const QList<int> *inUse) {
  return self->setSatellitesInUse(system, *inUse);
}

//  void QNmeaSatelliteInfoUpdate::consume()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoUpdate7consumeEv(
    QNmeaSatelliteInfoUpdate *self) {
  self->consume();
}

//  bool QNmeaSatelliteInfoUpdate::isFresh() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNmeaSatelliteInfoUpdate7isFreshEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return self->isFresh();
}

//  void QNmeaSatelliteInfoUpdate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoUpdate5clearEv(
    QNmeaSatelliteInfoUpdate *self) {
  self->clear();
}

//  bool QNmeaSatelliteInfoUpdate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNmeaSatelliteInfoUpdate7isValidEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return self->isValid();
}

//  bool QNmeaSatelliteInfoUpdate::calculateValidInUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNmeaSatelliteInfoUpdate19calculateValidInUseEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return self->calculateValidInUse();
}

//  bool QNmeaSatelliteInfoUpdate::calculateValidInView() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNmeaSatelliteInfoUpdate20calculateValidInViewEv(
    const QNmeaSatelliteInfoUpdate *self) {
  return self->calculateValidInView();
}

//  QNmeaSatelliteInfoUpdate::~QNmeaSatelliteInfoUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoUpdateD1Ev(
    QNmeaSatelliteInfoUpdate *self) {
  delete self;
}
