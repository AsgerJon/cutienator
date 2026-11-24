//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectreplica.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qvariant.h>
#include <QtCore/qthread.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 505, as _ZN34QRemoteObjectReplicaImplementation16configurePrivateEP20QRemoteObjectReplica
inline void QRemoteObjectReplicaImplementation::configurePrivate(QRemoteObjectReplica *rep)
{
    qCDebug(QT_REMOTEOBJECT) << "configurePrivate starting for" << this->m_objectName;
    //We need to connect the Replicant only signals too
    // Uncomment the following two lines if QRemoteObjectDynamicReplica gets a unique staticMetaObject (FIX #3)
    //const QMetaObject *m =  rep->inherits("QRemoteObjectDynamicReplica") ?
    //            &QRemoteObjectDynamicReplica::staticMetaObject : &QRemoteObjectReplica::staticMetaObject;
    const QMetaObject *m = &QRemoteObjectReplica::staticMetaObject;
    for (int i = m->methodOffset(); i < m->methodCount(); ++i)
    {
        const QMetaMethod mm = m->method(i);
        if (mm.methodType() == QMetaMethod::Signal) {
            const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
            qCDebug(QT_REMOTEOBJECT) << "  Rep connect"<<i<<res<<mm.name();
            Q_UNUSED(res)
        }
    }
    if (m_methodOffset == 0) //We haven't initialized the offsets yet
    {
        const int index = m_metaObject->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE);
        const QMetaObject *metaObject = m_metaObject;
        if (index != -1) { //We have an object created from repc or at least with QCLASSINFO defined
            while (true) {
                Q_ASSERT(metaObject->superClass()); //This recurses to QObject, which doesn't have QCLASSINFO_REMOTEOBJECT_TYPE
                if (index != metaObject->superClass()->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE)) //At the point we don't find the same QCLASSINFO_REMOTEOBJECT_TYPE,
                                //we have the metaobject we should work from
                    break;
                metaObject = metaObject->superClass();
            }
        }

        for (int i = m_signalOffset; i < metaObject->methodCount(); ++i) {
            const QMetaMethod mm = metaObject->method(i);
            if (mm.methodType() == QMetaMethod::Signal) {
                ++m_numSignals;
                const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
                qCDebug(QT_REMOTEOBJECT) << "  Connect"<<i<<res<<mm.name();
                Q_UNUSED(res)
            }
        }
        m_methodOffset = m_signalOffset + m_numSignals;
        qCDebug(QT_REMOTEOBJECT) << QStringLiteral("configurePrivate finished, signalOffset = %1, methodOffset = %2, #Signals = %3").arg(m_signalOffset).arg(m_methodOffset).arg(m_numSignals);
    } else { //We have initialized offsets, this is an additional Replica attaching
        for (int i = m_signalOffset; i < m_methodOffset; ++i) {
            const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
            qCDebug(QT_REMOTEOBJECT) << "  Connect"<<i<<res<<m_metaObject->method(i).name();
            Q_UNUSED(res)
        }
        if (isInitialized()) {
            qCDebug(QT_REMOTEOBJECT) << QStringLiteral("ReplicaImplementation initialized, emitting signal on replica");
            emit rep->initialized(); //Emit from new replica only
        }
        if (state() != QRemoteObjectReplica::Valid) {
            qCDebug(QT_REMOTEOBJECT) << QStringLiteral("ReplicaImplementation not currently valid, emitting signal on replica");
            emit rep->stateChanged(state(), m_metaObject ? QRemoteObjectReplica::Default : QRemoteObjectReplica::Uninitialized);
        }

        qCDebug(QT_REMOTEOBJECT) << QStringLiteral("configurePrivate finished, added replica to existing ReplicaImplementation");
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 253, as _ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject
inline void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const QMetaObject *meta)
{
    Q_ASSERT(!m_metaObject);

    m_metaObject = meta;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 55, as _ZN34QRemoteObjectReplicaImplementationD1Ev
inline QRemoteObjectReplicaImplementation::~QRemoteObjectReplicaImplementation()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 130, as _ZNK34QRemoteObjectReplicaImplementation26needsDynamicInitializationEv
inline bool QRemoteObjectReplicaImplementation::needsDynamicInitialization() const
{
    return m_metaObject == nullptr;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 135, as _ZN34QRemoteObjectReplicaImplementation8setStateEN20QRemoteObjectReplica5StateE
inline void QRemoteObjectReplicaImplementation::setState(QRemoteObjectReplica::State state)
{
    if (m_state.loadAcquire() != QRemoteObjectReplica::Suspect && m_state.loadAcquire() >= state)
        return;

    int oldState = m_state.loadAcquire();
    m_state.storeRelease(state);

    // We should emit initialized before emitting any changed signals in case connections are made in a
    // Slot responding to initialized/validChanged.
    if (m_state.loadAcquire() == QRemoteObjectReplica::Valid) {
        // we're initialized now, emit signal
        emitInitialized();
    }

    const static int stateChangedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("stateChanged(State,State)");
    Q_ASSERT(stateChangedIndex != -1);
    void *args[] = {nullptr, &state, &oldState};
    QMetaObject::activate(this, metaObject(), stateChangedIndex, args);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 221, as _ZN34QRemoteObjectReplicaImplementation15emitInitializedEv
inline void QRemoteObjectReplicaImplementation::emitInitialized()
{
    const static int initializedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("initialized()");
    Q_ASSERT(initializedIndex != -1);
    void *noArgs[] = {nullptr};
    QMetaObject::activate(this, metaObject(), initializedIndex, noArgs);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 156, as _ZN34QRemoteObjectReplicaImplementation12emitNotifiedEv
inline void QRemoteObjectReplicaImplementation::emitNotified()
{
    const static int notifiedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("notified()");
    Q_ASSERT(notifiedIndex != -1);
    void *args[] = {nullptr};
    QMetaObject::activate(this, metaObject(), notifiedIndex, args);
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectReplicaImplementation that Python can take functions over in. Every QRemoteObjectReplicaImplementation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQRemoteObjectReplicaImplementationCall0)(const void *, int, int *);
typedef void (*CuteQRemoteObjectReplicaImplementationCall1)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQRemoteObjectReplicaImplementationCall2)(const void *, int *);
typedef bool (*CuteQRemoteObjectReplicaImplementationCall3)(const void *, int *);
typedef int (*CuteQRemoteObjectReplicaImplementationCall4)(const void *, int *);
typedef bool (*CuteQRemoteObjectReplicaImplementationCall5)(const void *, int, int *);
typedef bool (*CuteQRemoteObjectReplicaImplementationCall6)(const void *, const QRemoteObjectPendingCall *, int, int *);
typedef void (*CuteQRemoteObjectReplicaImplementationCall7)(const void *, int, const QVariant *, int *);
typedef void (*CuteQRemoteObjectReplicaImplementationCall8)(const void *, QRemoteObjectReplica *, int *);
typedef void * (*CuteQRemoteObjectReplicaImplementationCall9)(const void *, int *);
typedef void (*CuteQRemoteObjectReplicaImplementationCall10)(const void *, const QMetaObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectReplicaImplementationCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectReplicaImplementationCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaImplementationCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaImplementationCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaImplementationCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaImplementationCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaImplementationCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectReplicaImplementation : public QRemoteObjectReplicaImplementation {
public:
  using QRemoteObjectReplicaImplementation::QRemoteObjectReplicaImplementation;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface11getPropertyEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QReplicaImplementationInterface11setPropertyEiRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QRemoteObjectReplicaImplementation14isShortCircuitEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface13isInitializedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface5stateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QReplicaImplementationInterface13waitForSourceEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QRemoteObjectReplicaImplementation15waitForFinishedERK24QRemoteObjectPendingCalli")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QRemoteObjectReplicaImplementation16notifyAboutReplyEiRK8QVariant")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QRemoteObjectReplicaImplementation16configurePrivateEP20QRemoteObjectReplica")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QReplicaImplementationInterface4nodeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  const QVariant QRemoteObjectReplicaImplementation::getProperty(int i)
  //      const
  const QVariant getProperty(int i) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall0 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall0>(taken[0]);
      const QVariant * given = call(this, i, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QRemoteObjectReplicaImplementation::setProperty(int i, const
  //      QVariant &a1)
  void setProperty(int i, const QVariant &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall1 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall1>(taken[1]);
      call(this, i, &a1, &handled);
      if (handled) return;
    }
  }

  //  bool QRemoteObjectReplicaImplementation::isShortCircuit() const
  bool isShortCircuit() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall2 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRemoteObjectReplicaImplementation::isInitialized() const
  bool isInitialized() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall3 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRemoteObjectReplicaImplementation::isInitialized();
  }

  //  QRemoteObjectReplica::State
  //      QRemoteObjectReplicaImplementation::state() const
  QRemoteObjectReplica::State state() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall4 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRemoteObjectReplica::State>(given);
    }
    return QRemoteObjectReplicaImplementation::state();
  }

  //  bool QRemoteObjectReplicaImplementation::waitForSource(int a0)
  bool waitForSource(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall5 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QRemoteObjectReplicaImplementation::waitForSource(a0);
  }

  //  bool QRemoteObjectReplicaImplementation::waitForFinished(const
  //      QRemoteObjectPendingCall &a0, int a1)
  bool waitForFinished(const QRemoteObjectPendingCall &a0, int a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall6 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall6>(taken[6]);
      bool given = call(this, &a0, a1, &handled);
      if (handled) return given;
    }
    return QRemoteObjectReplicaImplementation::waitForFinished(a0, a1);
  }

  //  void QRemoteObjectReplicaImplementation::notifyAboutReply(int a0,
  //      const QVariant &a1)
  void notifyAboutReply(int a0, const QVariant &a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall7 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall7>(taken[7]);
      call(this, a0, &a1, &handled);
      if (handled) return;
    }
    QRemoteObjectReplicaImplementation::notifyAboutReply(a0, a1);
  }

  //  void QRemoteObjectReplicaImplementation::configurePrivate(QRemoteObje
  //      ctReplica *a0)
  void configurePrivate(QRemoteObjectReplica *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall8 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRemoteObjectReplicaImplementation::configurePrivate(a0);
  }

  //  QRemoteObjectNode *QRemoteObjectReplicaImplementation::node() const
  QRemoteObjectNode *node() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall9 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRemoteObjectNode *>(given);
    }
    return QRemoteObjectReplicaImplementation::node();
  }

  //  void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const
  //      QMetaObject *meta)
  void setDynamicMetaObject(const QMetaObject *meta) override {
    if (taken[10]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall10 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall10>(taken[10]);
      call(this, meta, &handled);
      if (handled) return;
    }
    QRemoteObjectReplicaImplementation::setDynamicMetaObject(meta);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall11 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall12 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall13 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall14 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall15 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall16 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRemoteObjectReplicaImplementationCall17 call = reinterpret_cast<CuteQRemoteObjectReplicaImplementationCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectReplicaImplementation::~QRemoteObjectReplicaImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementationD1Ev(
    QRemoteObjectReplicaImplementation *self) {
  delete self;
}

//  bool QRemoteObjectReplicaImplementation::needsDynamicInitialization()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QRemoteObjectReplicaImplementation26needsDynamicInitializationEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->needsDynamicInitialization();
}

//  bool QRemoteObjectReplicaImplementation::isShortCircuit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QRemoteObjectReplicaImplementation14isShortCircuitEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->isShortCircuit();
}

//  bool QRemoteObjectReplicaImplementation::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QRemoteObjectReplicaImplementation13isInitializedEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->isInitialized();
}

//  QRemoteObjectReplica::State QRemoteObjectReplicaImplementation::state()
//      const
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica::State ritual_ZNK34QRemoteObjectReplicaImplementation5stateEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->state();
}

//  void
//      QRemoteObjectReplicaImplementation::setState(QRemoteObjectReplica::St
//      ate state)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation8setStateEN20QRemoteObjectReplica5StateE(
    QRemoteObjectReplicaImplementation *self,
    QRemoteObjectReplica::State state) {
  self->setState(state);
}

//  bool QRemoteObjectReplicaImplementation::waitForSource(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QRemoteObjectReplicaImplementation13waitForSourceEi(
    QRemoteObjectReplicaImplementation *self,
    int a0) {
  return self->waitForSource(a0);
}

//  bool QRemoteObjectReplicaImplementation::waitForFinished(const
//      QRemoteObjectPendingCall &a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QRemoteObjectReplicaImplementation15waitForFinishedERK24QRemoteObjectPendingCalli(
    QRemoteObjectReplicaImplementation *self,
    const QRemoteObjectPendingCall *a0,
    int a1) {
  return self->waitForFinished(*a0, a1);
}

//  void QRemoteObjectReplicaImplementation::notifyAboutReply(int a0, const
//      QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation16notifyAboutReplyEiRK8QVariant(
    QRemoteObjectReplicaImplementation *self,
    int a0,
    const QVariant *a1) {
  self->notifyAboutReply(a0, *a1);
}

//  void
//      QRemoteObjectReplicaImplementation::configurePrivate(QRemoteObjectRep
//      lica *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation16configurePrivateEP20QRemoteObjectReplica(
    QRemoteObjectReplicaImplementation *self,
    QRemoteObjectReplica *a0) {
  self->configurePrivate(a0);
}

//  void QRemoteObjectReplicaImplementation::emitInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation15emitInitializedEv(
    QRemoteObjectReplicaImplementation *self) {
  self->emitInitialized();
}

//  void QRemoteObjectReplicaImplementation::emitNotified()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation12emitNotifiedEv(
    QRemoteObjectReplicaImplementation *self) {
  self->emitNotified();
}

//  QRemoteObjectNode *QRemoteObjectReplicaImplementation::node() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZNK34QRemoteObjectReplicaImplementation4nodeEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->node();
}

//  void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const
//      QMetaObject *meta)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject(
    QRemoteObjectReplicaImplementation *self,
    const QMetaObject *meta) {
  self->setDynamicMetaObject(meta);
}

//  QRemoteObjectReplicaImplementation as the QReplicaImplementationInterface
//      it is built on
extern "C" Q_DECL_EXPORT
QReplicaImplementationInterface *ritual_cast_QRemoteObjectReplicaImplementation_QReplicaImplementationInterface(
    QRemoteObjectReplicaImplementation *self) {
  return static_cast<QReplicaImplementationInterface *>(self);
}

//  a Python function taken by a CuteQRemoteObjectReplicaImplementation, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectReplicaImplementation(
    QRemoteObjectReplicaImplementation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectReplicaImplementation *>(self)->take(key, call);
}

//  bool QRemoteObjectReplicaImplementation::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK34QRemoteObjectReplicaImplementation13isInitializedEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->QRemoteObjectReplicaImplementation::isInitialized();
}

//  QRemoteObjectReplica::State QRemoteObjectReplicaImplementation::state()
//      const
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica::State ritual_own_ZNK34QRemoteObjectReplicaImplementation5stateEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->QRemoteObjectReplicaImplementation::state();
}

//  bool QRemoteObjectReplicaImplementation::waitForSource(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN34QRemoteObjectReplicaImplementation13waitForSourceEi(
    QRemoteObjectReplicaImplementation *self,
    int a0) {
  return self->QRemoteObjectReplicaImplementation::waitForSource(a0);
}

//  bool QRemoteObjectReplicaImplementation::waitForFinished(const
//      QRemoteObjectPendingCall &a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN34QRemoteObjectReplicaImplementation15waitForFinishedERK24QRemoteObjectPendingCalli(
    QRemoteObjectReplicaImplementation *self,
    const QRemoteObjectPendingCall *a0,
    int a1) {
  return self->QRemoteObjectReplicaImplementation::waitForFinished(*a0, a1);
}

//  void QRemoteObjectReplicaImplementation::notifyAboutReply(int a0, const
//      QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QRemoteObjectReplicaImplementation16notifyAboutReplyEiRK8QVariant(
    QRemoteObjectReplicaImplementation *self,
    int a0,
    const QVariant *a1) {
  self->QRemoteObjectReplicaImplementation::notifyAboutReply(a0, *a1);
}

//  QRemoteObjectNode *QRemoteObjectReplicaImplementation::node() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_own_ZNK34QRemoteObjectReplicaImplementation4nodeEv(
    const QRemoteObjectReplicaImplementation *self) {
  return self->QRemoteObjectReplicaImplementation::node();
}

//  void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const
//      QMetaObject *meta)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject(
    QRemoteObjectReplicaImplementation *self,
    const QMetaObject *meta) {
  self->QRemoteObjectReplicaImplementation::setDynamicMetaObject(meta);
}
