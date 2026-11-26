//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals whose code, copied from
//  Qt's source, reads constant data Qt keeps to itself
//  ('QRemoteObjectSourceBase::qobjectPropertyOffset'), copied with it
//  'inline' from Qt's source, drafted by a copy of the generator that takes
//  it along. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractitemmodel.h>
#include <algorithm>
#include <iterator>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 26, as _ZN23QRemoteObjectSourceBase21qobjectPropertyOffsetE
inline const int QRemoteObjectSourceBase::qobjectPropertyOffset = QObject::staticMetaObject.propertyCount();

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 401, as _ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5QListI8QVariantEPS3_
inline bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index, const QVariantList &args, QVariant* returnValue)
{
    int status = -1;
    int flags = 0;
    bool forAdapter = (c == QMetaObject::InvokeMetaMethod ? m_api->isAdapterMethod(index) : m_api->isAdapterProperty(index));
    int resolvedIndex = (c == QMetaObject::InvokeMetaMethod ? m_api->sourceMethodIndex(index) : m_api->sourcePropertyIndex(index));
    if (resolvedIndex < 0)
        return false;
    QVarLengthArray<void*, 10> param(args.size() + 1);

    if (c == QMetaObject::InvokeMetaMethod) {
        QMetaMethod method;
        if (!forAdapter)
            method = parent()->metaObject()->method(resolvedIndex);

        if (returnValue) {
            if (!forAdapter && method.isValid() && method.returnType() == QMetaType::QVariant)
                param[0] = const_cast<void*>(reinterpret_cast<const void*>(returnValue));
            else
                param[0] = returnValue->data();
        } else {
            param[0] = nullptr;
        }

        auto argument = [&](int i) -> void * {
            if ((forAdapter && m_api->methodParameterType(index, i) == QMetaType::QVariant) ||
                    (method.isValid() && method.parameterType(i) == QMetaType::QVariant)) {
                return const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            }
            return const_cast<void*>(args.at(i).data());
        };

        for (int i = 0; i < args.size(); ++i) {
            param[i + 1] = argument(i);
        }
    } else if (c == QMetaObject::WriteProperty || c == QMetaObject::ReadProperty) {
        bool isQVariant = !forAdapter && parent()->metaObject()->property(resolvedIndex).userType() == QMetaType::QVariant;
        for (int i = 0; i < args.size(); ++i) {
            if (isQVariant)
                param[i] = const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            else
                param[i] = const_cast<void*>(args.at(i).data());
        }
        if (c == QMetaObject::WriteProperty) {
            Q_ASSERT(param.size() == 2); // for return-value and setter value
            // check QMetaProperty::write for an explanation of these
            param.append(&status);
            param.append(&flags);
        }
    } else {
        // Better safe than sorry
        return false;
    }
    int r = -1;
    if (forAdapter)
        r = m_adapter->qt_metacall(c, resolvedIndex, param.data());
    else
        r = parent()->qt_metacall(c, resolvedIndex, param.data());
    return r == -1 && status == -1;
}

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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 271, as _ZN34QRemoteObjectReplicaImplementation20setDynamicPropertiesEO5QListI8QVariantE
inline void QRemoteObjectReplicaImplementation::setDynamicProperties(QVariantList &&values)
{
    const int offset = m_propertyOffset;
    int propertyIndex = -1;
    for (auto &prop : values) {
        propertyIndex++;
        const QMetaProperty property = m_metaObject->property(propertyIndex+offset);
        prop = QRemoteObjectPackets::decodeVariant(std::move(prop), property.metaType());
    }
    //rely on order of properties;
    setProperties(std::move(values));
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 42, as _ZN34QRemoteObjectReplicaImplementationC2ERK7QStringPK11QMetaObjectP17QRemoteObjectNode
inline QRemoteObjectReplicaImplementation::QRemoteObjectReplicaImplementation(const QString &name, const QMetaObject *meta, QRemoteObjectNode *_node)
    : QObject(nullptr), m_objectName(name), m_metaObject(meta), m_numSignals(0), m_methodOffset(0)
    // Uncomment the following two lines if QRemoteObjectDynamicReplica gets a unique staticMetaObject (FIX #1, #2)
    //, m_signalOffset(meta ? QRemoteObjectReplica::staticMetaObject.methodCount() : QRemoteObjectDynamicReplica::staticMetaObject.methodCount())
    //, m_propertyOffset(meta ? QRemoteObjectReplica::staticMetaObject.propertyCount() : QRemoteObjectDynamicReplica::staticMetaObject.propertyCount())
    , m_signalOffset(QRemoteObjectReplica::staticMetaObject.methodCount())
    , m_propertyOffset(QRemoteObjectReplica::staticMetaObject.propertyCount())
    , m_node(_node)
    , m_objectSignature(QtPrivate::qtro_classinfo_signature(m_metaObject))
    , m_state(meta ? QRemoteObjectReplica::Default : QRemoteObjectReplica::Uninitialized)
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 55, as _ZN34QRemoteObjectReplicaImplementationD2Ev
inline QRemoteObjectReplicaImplementation::~QRemoteObjectReplicaImplementation()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 851, as _ZNK31QInProcessReplicaImplementation11getPropertyEi
inline const QVariant QInProcessReplicaImplementation::getProperty(int i) const
{
    Q_ASSERT(connectionToSource);
    Q_ASSERT(connectionToSource->m_object);
    const int index = i + QRemoteObjectSource::qobjectPropertyOffset;
    Q_ASSERT(index >= 0 && index < connectionToSource->m_object->metaObject()->propertyCount());
    return connectionToSource->m_object->metaObject()->property(index).read(connectionToSource->m_object);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 860, as _ZN31QInProcessReplicaImplementation13setPropertiesEO5QListI8QVariantE
inline void QInProcessReplicaImplementation::setProperties(QVariantList &&)
{
    //TODO some verification here maybe?
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 865, as _ZN31QInProcessReplicaImplementation11setPropertyEiRK8QVariant
inline void QInProcessReplicaImplementation::setProperty(int i, const QVariant &property)
{
    Q_ASSERT(connectionToSource);
    Q_ASSERT(connectionToSource->m_object);
    const int index = i + QRemoteObjectSource::qobjectPropertyOffset;
    Q_ASSERT(index >= 0 && index < connectionToSource->m_object->metaObject()->propertyCount());
    connectionToSource->m_object->metaObject()->property(index).write(connectionToSource->m_object, property);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 874, as _ZN31QInProcessReplicaImplementation7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE
inline void QInProcessReplicaImplementation::_q_send(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_ASSERT(call == QMetaObject::InvokeMetaMethod || call == QMetaObject::WriteProperty);

    const SourceApiMap *api = connectionToSource->m_api;
    if (call == QMetaObject::InvokeMetaMethod) {
        const int resolvedIndex = api->sourceMethodIndex(index - m_methodOffset);
        if (resolvedIndex < 0)
            qCWarning(QT_REMOTEOBJECT) << "Skipping invalid invocation.  Index not found:" << index - m_methodOffset;
        else
            connectionToSource->invoke(call, index - m_methodOffset, args);
    } else {
        const int resolvedIndex = connectionToSource->m_api->sourcePropertyIndex(index - m_propertyOffset);
        if (resolvedIndex < 0)
            qCWarning(QT_REMOTEOBJECT) << "Skipping invalid property setter.  Index not found:" << index - m_propertyOffset;
        else
            connectionToSource->invoke(call, index - m_propertyOffset, args);
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 894, as _ZN31QInProcessReplicaImplementation16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE
inline QRemoteObjectPendingCall QInProcessReplicaImplementation::_q_sendWithReply(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_ASSERT(call == QMetaObject::InvokeMetaMethod);

    const int ReplicaIndex = index - m_methodOffset;
    auto metaType = QMetaType::fromName(connectionToSource->m_api->typeName(ReplicaIndex).constData());
    if (!metaType.sizeOf())
        metaType = QMetaType(QMetaType::UnknownType);
    QVariant returnValue(metaType, nullptr);

    const int resolvedIndex = connectionToSource->m_api->sourceMethodIndex(ReplicaIndex);
    if (resolvedIndex < 0) {
        qCWarning(QT_REMOTEOBJECT) << "Skipping invalid invocation.  Index not found:" << ReplicaIndex;
        return QRemoteObjectPendingCall();
    }

    connectionToSource->invoke(call, ReplicaIndex, args, &returnValue);
    return QRemoteObjectPendingCall::fromCompletedCall(returnValue);
}
//  -----------------------------------------------------------------------

//  const QVariant QInProcessReplicaImplementation::getProperty(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QInProcessReplicaImplementation11getPropertyEi(
    const QInProcessReplicaImplementation *self,
    int i) {
  return new QVariant(self->getProperty(i));
}

//  void QInProcessReplicaImplementation::setProperties(QVariantList &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QInProcessReplicaImplementation13setPropertiesEO5QListI8QVariantE(
    QInProcessReplicaImplementation *self,
    QVariantList *a0) {
  self->setProperties(std::move(*a0));
}

//  void QInProcessReplicaImplementation::setProperty(int i, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QInProcessReplicaImplementation11setPropertyEiRK8QVariant(
    QInProcessReplicaImplementation *self,
    int i,
    const QVariant *a1) {
  self->setProperty(i, *a1);
}

//  bool QInProcessReplicaImplementation::isShortCircuit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QInProcessReplicaImplementation14isShortCircuitEv(
    const QInProcessReplicaImplementation *self) {
  return self->isShortCircuit();
}

//  void QInProcessReplicaImplementation::_q_send(QMetaObject::Call call, int
//      index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QInProcessReplicaImplementation7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QInProcessReplicaImplementation *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  self->_q_send(call, index, *args);
}

//  QRemoteObjectPendingCall
//      QInProcessReplicaImplementation::_q_sendWithReply(QMetaObject::Call
//      call, int index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN31QInProcessReplicaImplementation16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QInProcessReplicaImplementation *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  return new QRemoteObjectPendingCall(
      self->_q_sendWithReply(
          call,
          index,
          *args));
}
