//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  A QNmeaSatelliteRealTimeReader that Python can take functions over in. Every QNmeaSatelliteRealTimeReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaSatelliteRealTimeReaderCall0)(const void *, int *);
class CuteQNmeaSatelliteRealTimeReader : public QNmeaSatelliteRealTimeReader {
public:
  using QNmeaSatelliteRealTimeReader::QNmeaSatelliteRealTimeReader;
  CuteQNmeaSatelliteRealTimeReader(const QNmeaSatelliteRealTimeReader & other) : QNmeaSatelliteRealTimeReader(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QNmeaSatelliteReader17readAvailableDataEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QNmeaSatelliteRealTimeReader::readAvailableData()
  void readAvailableData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaSatelliteRealTimeReaderCall0 call = reinterpret_cast<CuteQNmeaSatelliteRealTimeReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaSatelliteRealTimeReader::readAvailableData();
  }
};

//  void QNmeaSatelliteRealTimeReader::readAvailableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNmeaSatelliteRealTimeReader17readAvailableDataEv(
    QNmeaSatelliteRealTimeReader *self) {
  self->readAvailableData();
}

//  QNmeaSatelliteRealTimeReader::~QNmeaSatelliteRealTimeReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNmeaSatelliteRealTimeReaderD1Ev(
    QNmeaSatelliteRealTimeReader *self) {
  delete self;
}

//  a Python function taken by a CuteQNmeaSatelliteRealTimeReader, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaSatelliteRealTimeReader(
    QNmeaSatelliteRealTimeReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaSatelliteRealTimeReader *>(self)->take(key, call);
}
