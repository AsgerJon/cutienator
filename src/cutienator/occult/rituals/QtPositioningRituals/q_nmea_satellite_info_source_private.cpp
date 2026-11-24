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
#include "qnmeasatelliteinfosource.h"
#include "private/qnmeasatelliteinfosource_p.h"
#include <QtPositioning/private/qgeosatelliteinfo_p.h>
#include <QtPositioning/private/qgeosatelliteinfosource_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QIODevice>
#include <QBasicTimer>
#include <QTimerEvent>
#include <QTimer>
#include <array>
#include <QDebug>
#include <QtCore/QtNumeric>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 782, as _ZN24QNmeaSatelliteInfoUpdate7consumeEv
inline void QNmeaSatelliteInfoUpdate::consume()
{
    m_fresh = false;
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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 134, as _ZN31QNmeaSatelliteInfoSourcePrivateD1Ev
inline QNmeaSatelliteInfoSourcePrivate::~QNmeaSatelliteInfoSourcePrivate()
{
    delete m_updateTimer;
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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 214, as _ZN31QNmeaSatelliteInfoSourcePrivate9readyReadEv
inline void QNmeaSatelliteInfoSourcePrivate::readyRead()
{
    if (m_nmeaReader)
        m_nmeaReader->readAvailableData();
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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 237, as _ZN31QNmeaSatelliteInfoSourcePrivate16sourceDataClosedEv
inline void QNmeaSatelliteInfoSourcePrivate::sourceDataClosed()
{
    if (m_nmeaReader && m_device && m_device->bytesAvailable())
        m_nmeaReader->readAvailableData();
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 243, as _ZN31QNmeaSatelliteInfoSourcePrivate20updateRequestTimeoutEv
inline void QNmeaSatelliteInfoSourcePrivate::updateRequestTimeout()
{
    m_requestTimer->stop();
    m_source->setError(QGeoSatelliteInfoSource::UpdateTimeoutError);
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

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 336, as _ZN31QNmeaSatelliteInfoSourcePrivate10timerEventEP11QTimerEvent
inline void QNmeaSatelliteInfoSourcePrivate::timerEvent(QTimerEvent * /*event*/)
{
    emitPendingUpdate();
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

//  QNmeaSatelliteInfoSourcePrivate::~QNmeaSatelliteInfoSourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivateD1Ev(
    QNmeaSatelliteInfoSourcePrivate *self) {
  delete self;
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
  self->readyRead();
}

//  void QNmeaSatelliteInfoSourcePrivate::emitPendingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate17emitPendingUpdateEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->emitPendingUpdate();
}

//  void QNmeaSatelliteInfoSourcePrivate::sourceDataClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate16sourceDataClosedEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->sourceDataClosed();
}

//  void QNmeaSatelliteInfoSourcePrivate::updateRequestTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNmeaSatelliteInfoSourcePrivate20updateRequestTimeoutEv(
    QNmeaSatelliteInfoSourcePrivate *self) {
  self->updateRequestTimeout();
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
