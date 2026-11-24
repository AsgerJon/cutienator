//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/private/qnmeapositioninfosource_p.h>
#include <QtPositioning/private/qgeopositioninfo_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtCore/QIODevice>
#include <QtCore/QBasicTimer>
#include <QtCore/QTimerEvent>
#include <QtCore/QTimer>
#include <array>
#include <QtCore/QDebug>
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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 269, as _ZN20QNmeaSimulatedReaderD1Ev
inline QNmeaSimulatedReader::~QNmeaSimulatedReader()
{
    if (m_currTimerId > 0)
        killTimer(m_currTimerId);
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 275, as _ZN20QNmeaSimulatedReader17readAvailableDataEv
inline void QNmeaSimulatedReader::readAvailableData()
{
    if (m_currTimerId > 0)     // we are already reading
        return;

    if (!m_hasValidDateTime) {      // first update
        Q_ASSERT(m_proxy->m_device && (m_proxy->m_device->openMode() & QIODevice::ReadOnly));

        if (!setFirstDateTime()) {
            //m_proxy->notifyReachedEndOfFile();
            qWarning("QNmeaPositionInfoSource: cannot find NMEA sentence with valid date & time");
            return;
        }

        m_hasValidDateTime = true;
        simulatePendingUpdate();

    } else {
        // previously read to EOF, but now new data has arrived
        processNextSentence();
    }
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 424, as _ZN20QNmeaSimulatedReader10timerEventEP11QTimerEvent
inline void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)
{
    killTimer(event->timerId());
    m_currTimerId = -1;
    simulatePendingUpdate();
}
//  -----------------------------------------------------------------------

//  A QNmeaSimulatedReader that Python can take functions over in. Every QNmeaSimulatedReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaSimulatedReaderCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSimulatedReaderCall1)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSimulatedReaderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSimulatedReaderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSimulatedReaderCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSimulatedReaderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSimulatedReaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSimulatedReaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNmeaSimulatedReader : public QNmeaSimulatedReader {
public:
  using QNmeaSimulatedReader::QNmeaSimulatedReader;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QNmeaReader17readAvailableDataEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNmeaSimulatedReader::readAvailableData()
  void readAvailableData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall0 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaSimulatedReader::readAvailableData();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall1 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QNmeaSimulatedReader::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall2 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall3 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall4 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall5 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall6 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNmeaSimulatedReaderCall7 call = reinterpret_cast<CuteQNmeaSimulatedReaderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNmeaSimulatedReader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QNmeaSimulatedReader10metaObjectEv(
    const QNmeaSimulatedReader *self) {
  return self->metaObject();
}

//  QNmeaSimulatedReader::~QNmeaSimulatedReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSimulatedReaderD1Ev(QNmeaSimulatedReader *self) {
  delete self;
}

//  void QNmeaSimulatedReader::readAvailableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSimulatedReader17readAvailableDataEv(
    QNmeaSimulatedReader *self) {
  self->readAvailableData();
}

//  void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSimulatedReader10timerEventEP11QTimerEvent(
    QNmeaSimulatedReader *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QNmeaSimulatedReader as the QNmeaReader it is built on
extern "C" Q_DECL_EXPORT
QNmeaReader *ritual_cast_QNmeaSimulatedReader_QNmeaReader(
    QNmeaSimulatedReader *self) {
  return static_cast<QNmeaReader *>(self);
}

//  a Python function taken by a CuteQNmeaSimulatedReader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaSimulatedReader(
    QNmeaSimulatedReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaSimulatedReader *>(self)->take(key, call);
}
