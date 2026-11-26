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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 126, as _ZN11QNmeaReaderD2Ev
inline QNmeaReader::~QNmeaReader()
    = default;

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 424, as _ZN20QNmeaSimulatedReader10timerEventEP11QTimerEvent
inline void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)
{
    killTimer(event->timerId());
    m_currTimerId = -1;
    simulatePendingUpdate();
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

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 413, as _ZN20QNmeaSimulatedReader21simulatePendingUpdateEv
inline void QNmeaSimulatedReader::simulatePendingUpdate()
{
    if (!m_pendingUpdates.isEmpty()) {
        // will be dequeued in processNextSentence()
        QPendingGeoPositionInfo &pending = m_pendingUpdates.head();
        m_proxy->notifyNewUpdate(&pending.info, pending.hasFix);
    }

    processNextSentence();
}

//  from ../qtpositioning/src/positioning/qnmeapositioninfosource.cpp, line 269, as _ZN20QNmeaSimulatedReaderD1Ev
inline QNmeaSimulatedReader::~QNmeaSimulatedReader()
{
    if (m_currTimerId > 0)
        killTimer(m_currTimerId);
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

//  void *QNmeaSimulatedReader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QNmeaSimulatedReader11qt_metacastEPKc(
    QNmeaSimulatedReader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNmeaSimulatedReader::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QNmeaSimulatedReader11qt_metacallEN11QMetaObject4CallEiPPv(
    QNmeaSimulatedReader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QNmeaSimulatedReader::simulatePendingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSimulatedReader21simulatePendingUpdateEv(
    QNmeaSimulatedReader *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNmeaSimulatedReader")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "simulatePendingUpdate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "simulatePendingUpdate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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
