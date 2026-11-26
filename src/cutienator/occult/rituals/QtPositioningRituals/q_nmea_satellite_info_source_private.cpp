//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
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
#include <QtPositioning/qgeosatelliteinfo.h>
#include <QtPositioning/private/qgeosatelliteinfo_p.h>
#include <QtCore/QHash>
#include <QtCore/QDebug>
#include <QtCore/QDataStream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 22, as local:qnmeasatelliteinfosource.cpp:QGeoSatelliteInfoPrivateNmea
#if USE_SATELLITE_NMEA_PIMPL
class QGeoSatelliteInfoPrivateNmea : public QGeoSatelliteInfoPrivate
{
public:
    QGeoSatelliteInfoPrivateNmea(const QGeoSatelliteInfoPrivate &other);
    QGeoSatelliteInfoPrivateNmea(const QGeoSatelliteInfoPrivateNmea &other);
    virtual ~QGeoSatelliteInfoPrivateNmea();

    QList<QByteArray> nmeaSentences;
};
#endif  // USE_SATELLITE_NMEA_PIMPL

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 32, as local:qnmeasatelliteinfosource.cpp:QGeoSatelliteInfoPrivateNmea::QGeoSatelliteInfoPrivateNmea
#if USE_SATELLITE_NMEA_PIMPL
inline QGeoSatelliteInfoPrivateNmea::QGeoSatelliteInfoPrivateNmea(const QGeoSatelliteInfoPrivate &other)
    : QGeoSatelliteInfoPrivate(other)
{
}
#endif  // USE_SATELLITE_NMEA_PIMPL

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 43, as local:qnmeasatelliteinfosource.cpp:QGeoSatelliteInfoPrivateNmea::~QGeoSatelliteInfoPrivateNmea
#if USE_SATELLITE_NMEA_PIMPL
inline QGeoSatelliteInfoPrivateNmea::~QGeoSatelliteInfoPrivateNmea() {}
#endif  // USE_SATELLITE_NMEA_PIMPL

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 336, as _ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QTimerEvent
inline void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent * /*event*/)
{
    emitPendingUpdate();
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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 838, as _ZN28QNmeaSatelliteRealTimeReaderC1EP31QNmeaSatelliteInfoSourcePrivate
inline QNmeaSatelliteRealTimeReader::QNmeaSatelliteRealTimeReader(QNmeaSatelliteInfoSourcePrivate *sourcePrivate)
    : QNmeaSatelliteReader(sourcePrivate)
{
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 850, as _ZN30QNmeaSatelliteSimulationReaderC1EP31QNmeaSatelliteInfoSourcePrivate
inline QNmeaSatelliteSimulationReader::QNmeaSatelliteSimulationReader(QNmeaSatelliteInfoSourcePrivate *sourcePrivate)
    : QNmeaSatelliteReader(sourcePrivate)
{
    m_timer.reset(new QTimer);
    QObject::connect(m_timer.get(), &QTimer::timeout, m_timer.get(), [this]() {
        readAvailableData();
    });
    m_updateInterval =
            qMax(m_proxy->m_simulationUpdateInterval, m_proxy->m_source->minimumUpdateInterval());
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 782, as _ZN24QNmeaSatelliteInfoUpdate7consumeEv
inline void QNmeaSatelliteInfoUpdate::consume()
{
    m_fresh = false;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 220, as _ZN31QNmeaSatelliteInfoSourcePrivate17emitPendingUpdateEv
inline void QNmeaSatelliteInfoSourcePrivate::emitPendingUpdate()
{
    if (m_pendingUpdate.isValid() && m_pendingUpdate.isFresh()) {
        m_updateTimeoutSent = false;
        m_noUpdateLastInterval = false;
        if (!emitUpdated(m_pendingUpdate, false))
            m_noUpdateLastInterval = true;
        // m_pendingUpdate.clear(); // Do not clear, it will be incrementally updated
    } else { // invalid or not fresh update
        if (m_noUpdateLastInterval && !m_updateTimeoutSent) {
            m_updateTimeoutSent = true;
            m_source->setError(QGeoSatelliteInfoSource::UpdateTimeoutError);
        }
        m_noUpdateLastInterval = true;
    }
}

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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 787, as _ZNK24QNmeaSatelliteInfoUpdate7isFreshEv
inline bool QNmeaSatelliteInfoUpdate::isFresh() const
{
    return m_fresh;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 805, as _ZNK24QNmeaSatelliteInfoUpdate7isValidEv
inline bool QNmeaSatelliteInfoUpdate::isValid() const
{
    // GSV without GSA is valid. GSA with outdated but still matching GSV also valid.
    return m_validInView || m_validInUse;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 829, as _ZN20QNmeaSatelliteReaderC2EP31QNmeaSatelliteInfoSourcePrivate
inline QNmeaSatelliteReader::QNmeaSatelliteReader(QNmeaSatelliteInfoSourcePrivate *sourcePrivate)
    : m_proxy(sourcePrivate)
{
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 834, as _ZN20QNmeaSatelliteReaderD2Ev
inline QNmeaSatelliteReader::~QNmeaSatelliteReader()
{
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 843, as _ZN28QNmeaSatelliteRealTimeReader17readAvailableDataEv
inline void QNmeaSatelliteRealTimeReader::readAvailableData()
{
    while (m_proxy->m_device->canReadLine())
        m_proxy->processNmeaData(m_proxy->m_pendingUpdate);
    m_proxy->notifyNewUpdate();
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 861, as _ZN30QNmeaSatelliteSimulationReader17readAvailableDataEv
inline void QNmeaSatelliteSimulationReader::readAvailableData()
{
    if (!m_timer->isActive()) {
        // At the very first start we just start a timer to simulate a short
        // delay for overlapping requestUpdate() calls.
        // See TestQGeoSatelliteInfoSource::requestUpdate_overlappingCalls and
        // TestQGeoSatelliteInfoSource::requestUpdate_overlappingCallsWithTimeout
        m_timer->start(m_updateInterval);
    } else {
        // Here we try to get both satellites in view and satellites in use.
        // We behave like that because according to the QGeoSatelliteInfoSource
        // tests each call to requestUpdate() should return both satellites in
        // view and satellites in use. Same is expected on each interval for
        // startUpdates().
        // However user-provided NMEA logs might not contain some of the
        // messages, so we will try not to get stuck here infinitely.
        int numSatInUseMsgs = 0;
        int numSatInViewMsgs = 0;
        while (!m_proxy->m_device->atEnd() && (!numSatInUseMsgs || !numSatInViewMsgs)) {
            m_proxy->processNmeaData(m_proxy->m_pendingUpdate);
            if (m_proxy->m_pendingUpdate.m_validInUse)
                numSatInUseMsgs++;
            if (m_proxy->m_pendingUpdate.m_validInView)
                numSatInViewMsgs++;
            // if we got the second message for one of them, but still didn't
            // receive any for the other - break.
            // We use 2 in the comparison, because, as soon as the m_validIn*
            // flag is set, it will stay true until we receive invalid message.
            if (numSatInUseMsgs > 2 || numSatInViewMsgs > 2) {
                const QString msgType = (numSatInUseMsgs > numSatInViewMsgs)
                        ? QStringLiteral("GSA")
                        : QStringLiteral("GSV");
                qWarning() << "nmea simulation reader: possibly incorrect message order. Got too "
                              "many consecutive"
                           << msgType << "messages";
                break;
            }
        }
        m_proxy->notifyNewUpdate();
    }
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 268, as _ZN31QNmeaSatelliteInfoSourcePrivate10initializeEv
inline bool QNmeaSatelliteInfoSourcePrivate::initialize()
{
    if (m_nmeaReader)
        return true;

    if (!openSourceDevice())
        return false;

    if (m_updateMode == QNmeaSatelliteInfoSource::UpdateMode::RealTimeMode)
        m_nmeaReader.reset(new QNmeaSatelliteRealTimeReader(this));
    else
        m_nmeaReader.reset(new QNmeaSatelliteSimulationReader(this));

    return true;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 75, as _ZN31QNmeaSatelliteInfoSourcePrivate15processNmeaDataER24QNmeaSatelliteInfoUpdate
inline void QNmeaSatelliteInfoSourcePrivate::processNmeaData(QNmeaSatelliteInfoUpdate &updateInfo)
{
    char buf[1024];
    qint64 size = m_device->readLine(buf, sizeof(buf));
    if (size <= 0)
        return;

    QList<int> satInUse;
    const auto satSystemType = m_source->parseSatellitesInUseFromNmea(QByteArrayView{buf,static_cast<qsizetype>(size)},
                                                                      satInUse);
    if (satSystemType != QGeoSatelliteInfo::Undefined) {
        const bool res = updateInfo.setSatellitesInUse(satSystemType, satInUse);
#if USE_SATELLITE_NMEA_PIMPL
        if (res) {
            updateInfo.gsa = QByteArray(buf, size);
            auto &info = updateInfo.m_satellites[satSystemType];
            if (!info.satellitesInUse.isEmpty()) {
                for (auto &s : info.satellitesInUse) {
                    static_cast<QGeoSatelliteInfoPrivateNmea *>(QGeoSatelliteInfoPrivate::get(s))
                            ->nmeaSentences.append(updateInfo.gsa);
                }
                for (auto &s : info.satellitesInView) {
                    static_cast<QGeoSatelliteInfoPrivateNmea *>(QGeoSatelliteInfoPrivate::get(s))
                            ->nmeaSentences.append(updateInfo.gsa);
                }
            }
        }
#else
        Q_UNUSED(res)
#endif // USE_SATELLITE_NMEA_PIMPL
    } else {
        // Here we have the assumption that multiple parts of GSV sentence
        // come one after another. At least this is how it should be.
        auto systemType = QGeoSatelliteInfo::Undefined;
        const auto parserStatus = m_source->parseSatelliteInfoFromNmea(
                QByteArrayView{buf,static_cast<qsizetype>(size)}, updateInfo.m_satellitesInViewParsed, systemType);
        if (parserStatus == QNmeaSatelliteInfoSource::PartiallyParsed) {
            updateInfo.m_satellites[systemType].updatingGSV = true;
#if USE_SATELLITE_NMEA_PIMPL
            updateInfo.gsv.append(QByteArray(buf, size));
#endif
        } else if (parserStatus == QNmeaSatelliteInfoSource::FullyParsed) {
#if USE_SATELLITE_NMEA_PIMPL
            updateInfo.gsv.append(QByteArray(buf, size));
            for (int i = 0; i < updateInfo.m_satellitesInViewParsed.size(); i++) {
                const QGeoSatelliteInfo &s = updateInfo.m_satellitesInViewParsed.at(i);
                QGeoSatelliteInfoPrivateNmea *pimpl =
                        new QGeoSatelliteInfoPrivateNmea(*QGeoSatelliteInfoPrivate::get(s));
                pimpl->nmeaSentences.append(updateInfo.gsa);
                pimpl->nmeaSentences.append(updateInfo.gsv);
                updateInfo.m_satellitesInViewParsed.replace(i, QGeoSatelliteInfo(*pimpl));
            }
            updateInfo.gsv.clear();
#endif
            updateInfo.setSatellitesInView(systemType, updateInfo.m_satellitesInViewParsed);
        }
    }
}

//  from ../qtpositioning/src/positioning/qgeosatelliteinfo.cpp, line 397, as _ZN24QGeoSatelliteInfoPrivate3getERK17QGeoSatelliteInfo
inline QGeoSatelliteInfoPrivate *QGeoSatelliteInfoPrivate::get(const QGeoSatelliteInfo &info)
{
    return info.d.data();
}

//  from ../qtpositioning/src/positioning/qgeosatelliteinfo.cpp, line 378, as _ZN24QGeoSatelliteInfoPrivateC2ERKS_
inline QGeoSatelliteInfoPrivate::QGeoSatelliteInfoPrivate(const QGeoSatelliteInfoPrivate &other)
    : QSharedData(other)
{
    signal = other.signal;
    satId = other.satId;
    system = other.system;
    doubleAttribs = other.doubleAttribs;
}

//  from ../qtpositioning/src/positioning/qgeosatelliteinfo.cpp, line 387, as _ZN24QGeoSatelliteInfoPrivateD2Ev
inline QGeoSatelliteInfoPrivate::~QGeoSatelliteInfoPrivate() {}

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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 134, as _ZN31QNmeaSatelliteInfoSourcePrivateD1Ev
inline QNmeaSatelliteInfoSourcePrivate::~QNmeaSatelliteInfoSourcePrivate()
{
    delete m_updateTimer;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 139, as _ZN31QNmeaSatelliteInfoSourcePrivate12startUpdatesEv
inline void QNmeaSatelliteInfoSourcePrivate::startUpdates()
{
    if (m_invokedStart)
        return;

    m_satelliteError = QGeoSatelliteInfoSource::NoError;

    m_invokedStart = true;
    m_pendingUpdate.clear();
    m_noUpdateLastInterval = false;

    bool initialized = initialize();
    if (!initialized)
        return;

    if (m_updateMode == QNmeaSatelliteInfoSource::UpdateMode::RealTimeMode) {
        // skip over any buffered data - we only want the newest data.
        // Don't do this in requestUpdate. In that case bufferedData is good to have/use.
        if (m_device->bytesAvailable()) {
            if (m_device->isSequential())
                m_device->readAll();
            else
                m_device->seek(m_device->bytesAvailable());
        }
    }

    if (m_updateTimer)
        m_updateTimer->stop();

    if (m_source->updateInterval() > 0) {
        if (!m_updateTimer)
            m_updateTimer = new QBasicTimer;
        m_updateTimer->start(m_source->updateInterval(), this);
    }

    if (initialized)
        prepareSourceDevice();
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 178, as _ZN31QNmeaSatelliteInfoSourcePrivate11stopUpdatesEv
inline void QNmeaSatelliteInfoSourcePrivate::stopUpdates()
{
    m_invokedStart = false;
    if (m_updateTimer)
        m_updateTimer->stop();
    m_pendingUpdate.clear();
    m_noUpdateLastInterval = false;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 54, as _ZN31QNmeaSatelliteInfoSourcePrivate15notifyNewUpdateEv
inline void QNmeaSatelliteInfoSourcePrivate::notifyNewUpdate()
{
    if (m_pendingUpdate.isValid() && m_pendingUpdate.isFresh()) {
        if (m_requestTimer && m_requestTimer->isActive()) { // User called requestUpdate()
            m_requestTimer->stop();
            emitUpdated(m_pendingUpdate, true);
        } else if (m_invokedStart) { // user called startUpdates()
            if (m_updateTimer && m_updateTimer->isActive()) { // update interval > 0
                // for periodic updates, only want the most recent update
                if (m_noUpdateLastInterval) {
                    // if the update was invalid when timerEvent was last called, a valid update
                    // should be sent ASAP
                    emitPendingUpdate(); // m_noUpdateLastInterval handled in there.
                }
            } else { // update interval <= 0, send anything new ASAP
                m_noUpdateLastInterval = !emitUpdated(m_pendingUpdate, false);
            }
        }
    }
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 249, as _ZN31QNmeaSatelliteInfoSourcePrivate16openSourceDeviceEv
inline bool QNmeaSatelliteInfoSourcePrivate::openSourceDevice()
{
    if (!m_device) {
        qWarning("QNmeaSatelliteInfoSource: no QIODevice data source, call setDevice() first");
        return false;
    }

    if (!m_device->isOpen() && !m_device->open(QIODevice::ReadOnly)) {
        qWarning("QNmeaSatelliteInfoSource: cannot open QIODevice data source");
        return false;
    }

    connect(m_device, SIGNAL(aboutToClose()), SLOT(sourceDataClosed()));
    connect(m_device, SIGNAL(readChannelFinished()), SLOT(sourceDataClosed()));
    connect(m_device, SIGNAL(destroyed()), SLOT(sourceDataClosed()));

    return true;
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 284, as _ZN31QNmeaSatelliteInfoSourcePrivate19prepareSourceDeviceEv
inline void QNmeaSatelliteInfoSourcePrivate::prepareSourceDevice()
{
    // some data may already be available
    if (m_updateMode == QNmeaSatelliteInfoSource::UpdateMode::SimulationMode) {
        if (m_nmeaReader && m_device->bytesAvailable())
            m_nmeaReader->readAvailableData();
    }

    if (!m_connectedReadyRead) {
        connect(m_device, SIGNAL(readyRead()), SLOT(readyRead()));
        m_connectedReadyRead = true;
    }
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 298, as _ZN31QNmeaSatelliteInfoSourcePrivate11emitUpdatedER24QNmeaSatelliteInfoUpdateb
inline bool QNmeaSatelliteInfoSourcePrivate::emitUpdated(QNmeaSatelliteInfoUpdate &update,
                                                  bool fromRequestUpdate)
{
    bool emitted = false;
    if (!update.isFresh())
        return emitted;

    update.consume();
    bool inUseUpdated = false;
    bool inViewUpdated = false;
    if (!fromRequestUpdate) {
        // we need to send update if information from at least one satellite
        // systems has changed
        for (auto it = update.m_satellites.cbegin(); it != update.m_satellites.cend(); ++it) {
            inUseUpdated |=
                    it->satellitesInUse != m_lastUpdate.m_satellites[it.key()].satellitesInUse;
            inViewUpdated |=
                    it->satellitesInView != m_lastUpdate.m_satellites[it.key()].satellitesInView;
        }
    } else {
        // if we come here from requestUpdate(), we need to emit, even if the data
        // didn't really change
        inUseUpdated = true;
        inViewUpdated = true;
    }

    m_lastUpdate = update;
    if (update.m_validInUse && inUseUpdated) {
        emit m_source->satellitesInUseUpdated(update.allSatellitesInUse());
        emitted = true;
    }
    if (update.m_validInView && inViewUpdated) {
        emit m_source->satellitesInViewUpdated(update.allSatellitesInView());
        emitted = true;
    }
    return emitted;
}
//  -----------------------------------------------------------------------

//  Only a class built on QNmeaSatelliteInfoSourcePrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNmeaSatelliteInfoSourcePrivate : QNmeaSatelliteInfoSourcePrivate {
  using QNmeaSatelliteInfoSourcePrivate::timerEvent;
};

//  A QNmeaSatelliteInfoSourcePrivate that Python can take functions over in. Every QNmeaSatelliteInfoSourcePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourcePrivateCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSatelliteInfoSourcePrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSatelliteInfoSourcePrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourcePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourcePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourcePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourcePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNmeaSatelliteInfoSourcePrivate : public QNmeaSatelliteInfoSourcePrivate {
public:
  using QNmeaSatelliteInfoSourcePrivate::QNmeaSatelliteInfoSourcePrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall0 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QNmeaSatelliteInfoSourcePrivate::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall1 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall2 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall3 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall4 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall5 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourcePrivateCall6 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourcePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNmeaSatelliteInfoSourcePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QNmeaSatelliteInfoSourcePrivate10metaObjectEv(
    const QNmeaSatelliteInfoSourcePrivate *self) {
  return self->metaObject();
}

//  void *QNmeaSatelliteInfoSourcePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QNmeaSatelliteInfoSourcePrivate11qt_metacastEPKc(
    QNmeaSatelliteInfoSourcePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNmeaSatelliteInfoSourcePrivate::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QNmeaSatelliteInfoSourcePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QNmeaSatelliteInfoSourcePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNmeaSatelliteInfoSourcePrivate::~QNmeaSatelliteInfoSourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivateD1Ev(
    QNmeaSatelliteInfoSourcePrivate *self) {
  delete self;
}

//  void QNmeaSatelliteInfoSourcePrivate::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate12startUpdatesEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->startUpdates();
}

//  void QNmeaSatelliteInfoSourcePrivate::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate11stopUpdatesEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->stopUpdates();
}

//  void QNmeaSatelliteInfoSourcePrivate::notifyNewUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate15notifyNewUpdateEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->notifyNewUpdate();
}

//  void QNmeaSatelliteInfoSourcePrivate::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate9readyReadEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaSatelliteInfoSourcePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readyRead()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readyRead()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNmeaSatelliteInfoSourcePrivate::emitPendingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate17emitPendingUpdateEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaSatelliteInfoSourcePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "emitPendingUpdate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "emitPendingUpdate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNmeaSatelliteInfoSourcePrivate::sourceDataClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate16sourceDataClosedEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaSatelliteInfoSourcePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceDataClosed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceDataClosed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNmeaSatelliteInfoSourcePrivate::updateRequestTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate20updateRequestTimeoutEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaSatelliteInfoSourcePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateRequestTimeout()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateRequestTimeout()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QNmeaSatelliteInfoSourcePrivate::openSourceDevice()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QNmeaSatelliteInfoSourcePrivate16openSourceDeviceEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  return self->openSourceDevice();
}

//  void QNmeaSatelliteInfoSourcePrivate::prepareSourceDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate19prepareSourceDeviceEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->prepareSourceDevice();
}

//  bool
//      QNmeaSatelliteInfoSourcePrivate::emitUpdated(QNmeaSatelliteInfoUpdate
//      &update, bool fromRequestUpdate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QNmeaSatelliteInfoSourcePrivate11emitUpdatedER24QNmeaSatelliteInfoUpdateb(
    QNmeaSatelliteInfoSourcePrivate *self,
    QNmeaSatelliteInfoUpdate *update,
    bool fromRequestUpdate) {
  return self->emitUpdated(*update, fromRequestUpdate);
}

//  void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QTimerEvent(
    QNmeaSatelliteInfoSourcePrivate *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  a Python function taken by a CuteQNmeaSatelliteInfoSourcePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaSatelliteInfoSourcePrivate(
    QNmeaSatelliteInfoSourcePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaSatelliteInfoSourcePrivate *>(self)->take(key, call);
}

//  void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QTimerEvent(
    QNmeaSatelliteInfoSourcePrivate *self,
    QTimerEvent *event) {
  static_cast<OwnQNmeaSatelliteInfoSourcePrivate *>(self)->OwnQNmeaSatelliteInfoSourcePrivate::timerEvent(
      event);
}
