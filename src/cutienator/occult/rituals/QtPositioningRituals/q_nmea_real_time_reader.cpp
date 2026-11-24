//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qnmeapositioninfosource_p.h"
#include "qgeopositioninfo_p.h"
#include "qlocationutils_p.h"
#include <QIODevice>
#include <QBasicTimer>
#include <QTimerEvent>
#include <QTimer>
#include <array>
#include <QDebug>
#include <QtCore/QtNumeric>
#include <QtCore/QDateTime>
#include <QtCore/QTimeZone>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 628, as _ZN30QNmeaPositionInfoSourcePrivate15notifyNewUpdateEP16QGeoPositionInfob
inline void QNmeaPositionInfoSourcePrivate::notifyNewUpdate(QGeoPositionInfo *update, bool hasFix)
{
    // include <QDebug> before uncommenting
    //qDebug() << "QNmeaPositionInfoSourcePrivate::notifyNewUpdate()" << update->timestamp() << hasFix << m_invokedStart << (m_requestTimer && m_requestTimer->isActive());

    QDate date = update->timestamp().date();
    if (date.isValid()) {
        m_currentDate = date;
    } else {
        // some sentence have time but no date
        QTime time = update->timestamp().time();
        if (time.isValid() && m_currentDate.isValid())
            update->setTimestamp(QDateTime(m_currentDate, time, QTimeZone::UTC));
    }

    // Some attributes are sent in separate NMEA sentences. Save and restore the accuracy
    // measurements.
    if (update->hasAttribute(QGeoPositionInfo::HorizontalAccuracy))
        m_horizontalAccuracy = update->attribute(QGeoPositionInfo::HorizontalAccuracy);
    else if (!qIsNaN(m_horizontalAccuracy))
        update->setAttribute(QGeoPositionInfo::HorizontalAccuracy, m_horizontalAccuracy);

    if (update->hasAttribute(QGeoPositionInfo::VerticalAccuracy))
        m_verticalAccuracy = update->attribute(QGeoPositionInfo::VerticalAccuracy);
    else if (!qIsNaN(m_verticalAccuracy))
        update->setAttribute(QGeoPositionInfo::VerticalAccuracy, m_verticalAccuracy);

    if (hasFix && update->isValid()) {
        if (m_requestTimer && m_requestTimer->isActive()) { // User called requestUpdate()
            m_requestTimer->stop();
            emitUpdated(*update);
        } else if (m_invokedStart) { // user called startUpdates()
            if (m_updateTimer && m_updateTimer->isActive()) { // update interval > 0
                // for periodic updates, only want the most recent update
                m_pendingUpdate = *update; // Set what to send in timerEvent()
                if (m_noUpdateLastInterval) {
                    // if the update was invalid when timerEvent was last called, a valid update
                    // should be sent ASAP
                    emitPendingUpdate();
                    m_noUpdateLastInterval = false;
                }
            } else { // update interval <= 0
                emitUpdated(*update);
            }
        }
        m_lastUpdate = *update; // Set in any case, if update is valid. Used in lastKnownPosition().
    }
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 699, as _ZN30QNmeaPositionInfoSourcePrivate11emitUpdatedERK16QGeoPositionInfo
inline void QNmeaPositionInfoSourcePrivate::emitUpdated(const QGeoPositionInfo &update)
{
    // check for duplication already done in QNmeaRealTimeReader::notifyNewUpdate
    // and QNmeaRealTimeReader::readAvailableData
    m_lastUpdate = update;
    emit m_source->positionUpdated(update);
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 682, as _ZN30QNmeaPositionInfoSourcePrivate17emitPendingUpdateEv
inline void QNmeaPositionInfoSourcePrivate::emitPendingUpdate()
{
    if (m_pendingUpdate.isValid()) {
        m_updateTimeoutSent = false;
        m_noUpdateLastInterval = false;
        emitUpdated(m_pendingUpdate);
        m_pendingUpdate = QGeoPositionInfo();
    } else { // invalid update
        if (m_noUpdateLastInterval && !m_updateTimeoutSent) {
            m_updateTimeoutSent = true;
            m_pendingUpdate = QGeoPositionInfo(); // Invalid already, but clear just in case.
            m_source->setError(QGeoPositionInfoSource::UpdateTimeoutError);
        }
        m_noUpdateLastInterval = true;
    }
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 246, as _ZN19QNmeaRealTimeReader15notifyNewUpdateEv
inline void QNmeaRealTimeReader::notifyNewUpdate()
{
    const bool newerTime = m_update.timestamp().time() > m_lastPushedTS.time();
    const bool newerDate = (m_update.timestamp().date().isValid()
                            && m_lastPushedTS.date().isValid()
                            && m_update.timestamp().date() > m_lastPushedTS.date());
    if (newerTime || newerDate) {
        m_proxy->notifyNewUpdate(&m_update, m_hasFix);
        m_lastPushedTS = m_update.timestamp();
    }
    m_timer.stop();
}
//  -----------------------------------------------------------------------

//  A QNmeaRealTimeReader that Python can take functions over in. Every QNmeaRealTimeReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaRealTimeReaderCall0)(const void *, int *);
class CuteQNmeaRealTimeReader : public QNmeaRealTimeReader {
public:
  using QNmeaRealTimeReader::QNmeaRealTimeReader;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QNmeaReader17readAvailableDataEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QNmeaRealTimeReader::readAvailableData()
  void readAvailableData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaRealTimeReaderCall0 call = reinterpret_cast<CuteQNmeaRealTimeReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaRealTimeReader::readAvailableData();
  }
};

//  void QNmeaRealTimeReader::notifyNewUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNmeaRealTimeReader15notifyNewUpdateEv(
    QNmeaRealTimeReader *self) {
  self->notifyNewUpdate();
}

//  a Python function taken by a CuteQNmeaRealTimeReader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaRealTimeReader(
    QNmeaRealTimeReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaRealTimeReader *>(self)->take(key, call);
}
