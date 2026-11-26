//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QNmeaPositionInfoSourcePrivate' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 26, as local:qnmeapositioninfosource.cpp:QGeoPositionInfoPrivateNmea
#if USE_POSITION_NMEA_PIMPL
class QGeoPositionInfoPrivateNmea : public QGeoPositionInfoPrivate
{
public:
    virtual ~QGeoPositionInfoPrivateNmea();

    QList<QByteArray> nmeaSentences;
};
#endif  // USE_POSITION_NMEA_PIMPL

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 35, as local:qnmeapositioninfosource.cpp:QGeoPositionInfoPrivateNmea::~QGeoPositionInfoPrivateNmea
#if USE_POSITION_NMEA_PIMPL
inline QGeoPositionInfoPrivateNmea::~QGeoPositionInfoPrivateNmea()
{

}
#endif  // USE_POSITION_NMEA_PIMPL

//  from QtPositioning__QNmeaPositionInfoSourcePrivate.cpp, line 1, as moc:QNmeaPositionInfoSourcePrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QNmeaPositionInfoSourcePrivate::qt_create_metaobjectdata<qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNmeaPositionInfoSourcePrivate",
        "readyRead",
        "",
        "emitPendingUpdate",
        "sourceDataClosed",
        "updateRequestTimeout"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'readyRead'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'emitPendingUpdate'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'sourceDataClosed'
        QtMocHelpers::SlotData<void()>(4, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'updateRequestTimeout'
        QtMocHelpers::SlotData<void()>(5, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNmeaPositionInfoSourcePrivate, qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNmeaPositionInfoSourcePrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>.metaTypes,
    nullptr
} };

void QNmeaPositionInfoSourcePrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNmeaPositionInfoSourcePrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->readyRead(); break;
        case 1: _t->emitPendingUpdate(); break;
        case 2: _t->sourceDataClosed(); break;
        case 3: _t->updateRequestTimeout(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QNmeaPositionInfoSourcePrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNmeaPositionInfoSourcePrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN30QNmeaPositionInfoSourcePrivateE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QNmeaPositionInfoSourcePrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 677, as _ZN30QNmeaPositionInfoSourcePrivate10timerEventEP11QTimerEvent
inline void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent *)
{
    emitPendingUpdate();
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 497, as _ZN30QNmeaPositionInfoSourcePrivate16sourceDataClosedEv
inline void QNmeaPositionInfoSourcePrivate::sourceDataClosed()
{
    if (m_nmeaReader && m_device && m_device->bytesAvailable())
        m_nmeaReader->readAvailableData();
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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 622, as _ZN30QNmeaPositionInfoSourcePrivate20updateRequestTimeoutEv
inline void QNmeaPositionInfoSourcePrivate::updateRequestTimeout()
{
    m_requestTimer->stop();
    m_source->setError(QGeoPositionInfoSource::UpdateTimeoutError);
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 503, as _ZN30QNmeaPositionInfoSourcePrivate9readyReadEv
inline void QNmeaPositionInfoSourcePrivate::readyRead()
{
    if (m_nmeaReader)
        m_nmeaReader->readAvailableData();
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 262, as _ZN20QNmeaSimulatedReaderC1EP30QNmeaPositionInfoSourcePrivate
inline QNmeaSimulatedReader::QNmeaSimulatedReader(QNmeaPositionInfoSourcePrivate *sourcePrivate)
        : QNmeaReader(sourcePrivate),
        m_currTimerId(-1),
        m_hasValidDateTime(false)
{
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 453, as _ZN30QNmeaPositionInfoSourcePrivateC1EP23QNmeaPositionInfoSourceNS0_10UpdateModeE
inline QNmeaPositionInfoSourcePrivate::QNmeaPositionInfoSourcePrivate(QNmeaPositionInfoSource *parent, QNmeaPositionInfoSource::UpdateMode updateMode)
        : QObject(parent),
        m_updateMode(updateMode),
        m_device(0),
        m_invokedStart(false),
        m_positionError(QGeoPositionInfoSource::UnknownSourceError),
        m_userEquivalentRangeError(qQNaN()),
        m_source(parent),
        m_nmeaReader(0),
        m_updateTimer(0),
        m_requestTimer(0),
        m_horizontalAccuracy(qQNaN()),
        m_verticalAccuracy(qQNaN()),
        m_noUpdateLastInterval(false),
        m_updateTimeoutSent(false),
        m_connectedReadyRead(false)
{
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 472, as _ZN30QNmeaPositionInfoSourcePrivateD1Ev
inline QNmeaPositionInfoSourcePrivate::~QNmeaPositionInfoSourcePrivate()
{
    delete m_nmeaReader;
    delete m_updateTimer;
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 586, as _ZN30QNmeaPositionInfoSourcePrivate11stopUpdatesEv
inline void QNmeaPositionInfoSourcePrivate::stopUpdates()
{
    m_invokedStart = false;
    if (m_updateTimer)
        m_updateTimer->stop();
    m_pendingUpdate = QGeoPositionInfo();
    m_noUpdateLastInterval = false;
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 539, as _ZN30QNmeaPositionInfoSourcePrivate24parsePosInfoFromNmeaDataE14QByteArrayViewP16QGeoPositionInfoPb
inline bool QNmeaPositionInfoSourcePrivate::parsePosInfoFromNmeaData(QByteArrayView data,
        QGeoPositionInfo *posInfo, bool *hasFix)
{
    return m_source->parsePosInfoFromNmeaData(data, posInfo, hasFix);
}

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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 478, as _ZN30QNmeaPositionInfoSourcePrivate16openSourceDeviceEv
inline bool QNmeaPositionInfoSourcePrivate::openSourceDevice()
{
    if (!m_device) {
        qWarning("QNmeaPositionInfoSource: no QIODevice data source, call setDevice() first");
        return false;
    }

    if (!m_device->isOpen() && !m_device->open(QIODevice::ReadOnly)) {
        qWarning("QNmeaPositionInfoSource: cannot open QIODevice data source");
        return false;
    }

    connect(m_device, SIGNAL(aboutToClose()), SLOT(sourceDataClosed()));
    connect(m_device, SIGNAL(readChannelFinished()), SLOT(sourceDataClosed()));
    connect(m_device, SIGNAL(destroyed()), SLOT(sourceDataClosed()));

    return true;
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 525, as _ZN30QNmeaPositionInfoSourcePrivate19prepareSourceDeviceEv
inline void QNmeaPositionInfoSourcePrivate::prepareSourceDevice()
{
    // some data may already be available
    if (m_updateMode == QNmeaPositionInfoSource::SimulationMode) {
        if (m_nmeaReader && m_device->bytesAvailable())
            m_nmeaReader->readAvailableData();
    }

    if (!m_connectedReadyRead) {
        connect(m_device, SIGNAL(readyRead()), SLOT(readyRead()));
        m_connectedReadyRead = true;
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
//  -----------------------------------------------------------------------

//  Only a class built on QNmeaPositionInfoSourcePrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNmeaPositionInfoSourcePrivate : QNmeaPositionInfoSourcePrivate {
  using QNmeaPositionInfoSourcePrivate::timerEvent;
};

//  A QNmeaPositionInfoSourcePrivate that Python can take functions over in. Every QNmeaPositionInfoSourcePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourcePrivateCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaPositionInfoSourcePrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaPositionInfoSourcePrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourcePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourcePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourcePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourcePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNmeaPositionInfoSourcePrivate : public QNmeaPositionInfoSourcePrivate {
public:
  using QNmeaPositionInfoSourcePrivate::QNmeaPositionInfoSourcePrivate;
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
  //  void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourcePrivateCall0 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QNmeaPositionInfoSourcePrivate::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourcePrivateCall1 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall1>(taken[1]);
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
      CuteQNmeaPositionInfoSourcePrivateCall2 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall2>(taken[2]);
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
      CuteQNmeaPositionInfoSourcePrivateCall3 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall3>(taken[3]);
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
      CuteQNmeaPositionInfoSourcePrivateCall4 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall4>(taken[4]);
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
      CuteQNmeaPositionInfoSourcePrivateCall5 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall5>(taken[5]);
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
      CuteQNmeaPositionInfoSourcePrivateCall6 call = reinterpret_cast<CuteQNmeaPositionInfoSourcePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNmeaPositionInfoSourcePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QNmeaPositionInfoSourcePrivate10metaObjectEv(
    const QNmeaPositionInfoSourcePrivate *self) {
  return self->metaObject();
}

//  void *QNmeaPositionInfoSourcePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QNmeaPositionInfoSourcePrivate11qt_metacastEPKc(
    QNmeaPositionInfoSourcePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNmeaPositionInfoSourcePrivate::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QNmeaPositionInfoSourcePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QNmeaPositionInfoSourcePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNmeaPositionInfoSourcePrivate::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QNmeaPositionInfoSourcePrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNmeaPositionInfoSourcePrivate::tr(s, c, n));
}

//  QNmeaPositionInfoSourcePrivate::QNmeaPositionInfoSourcePrivate(QNmeaPosit
//      ionInfoSource *parent, QNmeaPositionInfoSource::UpdateMode
//      updateMode)
extern "C" Q_DECL_EXPORT
QNmeaPositionInfoSourcePrivate *ritual_ZN30QNmeaPositionInfoSourcePrivateC1EP23QNmeaPositionInfoSourceNS0_10UpdateModeE(
    QNmeaPositionInfoSource *parent,
    QNmeaPositionInfoSource::UpdateMode updateMode) {
  return new CuteQNmeaPositionInfoSourcePrivate(parent, updateMode);
}

//  QNmeaPositionInfoSourcePrivate::~QNmeaPositionInfoSourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivateD1Ev(
    QNmeaPositionInfoSourcePrivate *self) {
  delete self;
}

//  void QNmeaPositionInfoSourcePrivate::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate11stopUpdatesEv(
    QNmeaPositionInfoSourcePrivate *self) {
  self->stopUpdates();
}

//  bool
//      QNmeaPositionInfoSourcePrivate::parsePosInfoFromNmeaData(QByteArrayVi
//      ew data, QGeoPositionInfo *posInfo, bool *hasFix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QNmeaPositionInfoSourcePrivate24parsePosInfoFromNmeaDataE14QByteArrayViewP16QGeoPositionInfoPb(
    QNmeaPositionInfoSourcePrivate *self,
    const QByteArrayView *data,
    QGeoPositionInfo *posInfo,
    bool *hasFix) {
  return self->parsePosInfoFromNmeaData(*data, posInfo, hasFix);
}

//  void QNmeaPositionInfoSourcePrivate::notifyNewUpdate(QGeoPositionInfo
//      *update, bool fixStatus)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate15notifyNewUpdateEP16QGeoPositionInfob(
    QNmeaPositionInfoSourcePrivate *self,
    QGeoPositionInfo *update,
    bool fixStatus) {
  self->notifyNewUpdate(update, fixStatus);
}

//  void QNmeaPositionInfoSourcePrivate::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate9readyReadEv(
    QNmeaPositionInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaPositionInfoSourcePrivate")) {
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

//  void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate10timerEventEP11QTimerEvent(
    QNmeaPositionInfoSourcePrivate *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QNmeaPositionInfoSourcePrivate::emitPendingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate17emitPendingUpdateEv(
    QNmeaPositionInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaPositionInfoSourcePrivate")) {
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

//  void QNmeaPositionInfoSourcePrivate::sourceDataClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate16sourceDataClosedEv(
    QNmeaPositionInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaPositionInfoSourcePrivate")) {
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

//  void QNmeaPositionInfoSourcePrivate::updateRequestTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate20updateRequestTimeoutEv(
    QNmeaPositionInfoSourcePrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaPositionInfoSourcePrivate")) {
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

//  bool QNmeaPositionInfoSourcePrivate::openSourceDevice()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QNmeaPositionInfoSourcePrivate16openSourceDeviceEv(
    QNmeaPositionInfoSourcePrivate *self) {
  return self->openSourceDevice();
}

//  void QNmeaPositionInfoSourcePrivate::prepareSourceDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate19prepareSourceDeviceEv(
    QNmeaPositionInfoSourcePrivate *self) {
  self->prepareSourceDevice();
}

//  void QNmeaPositionInfoSourcePrivate::emitUpdated(const QGeoPositionInfo
//      &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QNmeaPositionInfoSourcePrivate11emitUpdatedERK16QGeoPositionInfo(
    QNmeaPositionInfoSourcePrivate *self,
    const QGeoPositionInfo *update) {
  self->emitUpdated(*update);
}

//  a Python function taken by a CuteQNmeaPositionInfoSourcePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaPositionInfoSourcePrivate(
    QNmeaPositionInfoSourcePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaPositionInfoSourcePrivate *>(self)->take(key, call);
}

//  void QNmeaPositionInfoSourcePrivate::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QNmeaPositionInfoSourcePrivate10timerEventEP11QTimerEvent(
    QNmeaPositionInfoSourcePrivate *self,
    QTimerEvent *event) {
  static_cast<OwnQNmeaPositionInfoSourcePrivate *>(self)->OwnQNmeaPositionInfoSourcePrivate::timerEvent(
      event);
}
