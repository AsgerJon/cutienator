//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearrayview.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <cstring>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 38, as local:qremoteobjectpacket.cpp:isSequentialGadgetType
static bool isSequentialGadgetType(QMetaType metaType)
{
    if (QMetaType::canConvert(metaType, QMetaType::fromType<QMetaSequence::Iterable>())) {
        static QHash<int, bool> lookup;
        if (!lookup.contains(metaType.id())) {
            auto stubVariant = QVariant(metaType, nullptr);
            auto asIterable = stubVariant.value<QMetaSequence::Iterable>();
            auto valueMetaType = asIterable.metaContainer().valueMetaType();
            lookup[metaType.id()] = valueMetaType.flags().testFlag(QMetaType::IsGadget);
        }
        return lookup[metaType.id()];
    }
    return false;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 53, as local:qremoteobjectpacket.cpp:isAssociativeGadgetType
static bool isAssociativeGadgetType(QMetaType metaType)
{
    if (QMetaType::canConvert(metaType, QMetaType::fromType<QMetaAssociation::Iterable>())) {
        static QHash<int, bool> lookup;
        if (!lookup.contains(metaType.id())) {
            auto stubVariant = QVariant(metaType, nullptr);
            auto asIterable = stubVariant.value<QMetaAssociation::Iterable>();
            auto valueMetaType = asIterable.metaContainer().mappedMetaType();
            lookup[metaType.id()] = valueMetaType.flags().testFlag(QMetaType::IsGadget);
        }
        return lookup[metaType.id()];
    }
    return false;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 416, as local:qremoteobjectpacket.cpp:resolveEnumName
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
static QByteArrayView resolveEnumName(QMetaType t, bool &isFlag)
{
    // Takes types like `MyPOD::Position` or `QFlags<MyPOD::Position>` and returns 'Position`
    QByteArrayView enumName(t.name());
    isFlag = enumName.startsWith("QFlags<");
    auto lastColon = enumName.lastIndexOf(':');
    if (lastColon >= 0)
        enumName = QByteArrayView(t.name() + lastColon + 1);
    if (isFlag)
        enumName.chop(1);
    return enumName;
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 429, as local:qremoteobjectpacket.cpp:metaEnumFromType
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
static QMetaEnum metaEnumFromType(QMetaType t)
{
    if (t.flags().testFlag(QMetaType::IsEnumeration)) {
        if (const QMetaObject *m = t.metaObject()) {
            bool isFlag;
            auto enumName = resolveEnumName(t, isFlag);
            if (isFlag) {
                for (int i = m->enumeratorOffset(); i < m->enumeratorCount(); i++) {
                    auto testType = m->enumerator(i);
                    if (testType.isFlag() &&
                        enumName.compare(QByteArrayView(testType.enumName())) == 0)
                        return testType;
                }
            }
            return m->enumerator(m->indexOfEnumerator(enumName.data()));
        }
    }
    return QMetaEnum();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 544, as local:qremoteobjectpacket.cpp:checkForEnumsInSource
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
static bool checkForEnumsInSource(const QMetaObject *meta, const QRemoteObjectSourceBase *source)
{
    if (source->m_object->inherits(meta->className()))
        return true;
    for (const auto &child : source->m_children) {
        if (child->m_object && checkForEnumsInSource(meta, child))
            return true;
    }
    return false;
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 555, as local:qremoteobjectpacket.cpp:serializeEnum
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
static void serializeEnum(QDataStream &ds, const QMetaEnum &enumerator)
{
    ds << QByteArray::fromRawData(enumerator.name(), qsizetype(qstrlen(enumerator.name())));
    ds << enumerator.isFlag();
    ds << enumerator.isScoped();
    const auto typeName = QByteArray(enumerator.scope()).append("::").append(enumerator.name());
    const quint32 size = quint32(QMetaType::fromName(typeName.constData()).sizeOf());
    ds << size;
#ifdef QTRO_VERBOSE_PROTOCOL
    qDebug("  Enum (name = %s, size = %d, isFlag = %s, isScoped = %s):", enumerator.name(), size, enumerator.isFlag() ? "true" : "false", enumerator.isScoped() ? "true" : "false");
#endif
    const int keyCount = enumerator.keyCount();
    ds << keyCount;
    for (int k = 0; k < keyCount; ++k) {
        ds << QByteArray::fromRawData(enumerator.key(k), qsizetype(qstrlen(enumerator.key(k))));
        ds << enumerator.value(k);
#ifdef QTRO_VERBOSE_PROTOCOL
        qDebug("    Key %d (name = %s, value = %d):", k, enumerator.key(k), enumerator.value(k));
#endif
    }
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 338, as _ZN20QRemoteObjectPackets16QDataStreamCodec19serializeInitPacketEPK23QRemoteObjectRootSource
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeInitPacket(const QRemoteObjectRootSource *source)
{
    m_packet.setId(InitPacket);
    m_packet << source->name();
    serializeProperties(source);
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 393, as _ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInitDynamicPacketEPK23QRemoteObjectRootSource
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeInitDynamicPacket(const QRemoteObjectRootSource *source)
{
    m_packet.setId(InitDynamicPacket);
    m_packet << source->name();
    serializeDefinition(m_packet, source);
    serializeProperties(source);
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 833, as _ZN20QRemoteObjectPackets16QDataStreamCodec29serializePropertyChangePacketEP23QRemoteObjectSourceBasei
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializePropertyChangePacket(QRemoteObjectSourceBase *source, int signalIndex)
{
    int internalIndex = source->m_api->propertyRawIndexFromSignal(signalIndex);
    m_packet.setId(PropertyChangePacket);
    m_packet << source->name();
    m_packet << internalIndex;
    serializeProperty(source, internalIndex);
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 281, as _ZN20QRemoteObjectPackets16QDataStreamCodec17serializePropertyEPK23QRemoteObjectSourceBasei
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeProperty(const QRemoteObjectSourceBase *source, int internalIndex)
{
    serializeProperty(m_packet, source, internalIndex);
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 861, as _ZN20QRemoteObjectPackets16QDataStreamCodec19serializePingPacketERK7QString
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializePingPacket(const QString &name)
{
    m_packet.setId(Ping);
    m_packet << name;
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 868, as _ZN20QRemoteObjectPackets16QDataStreamCodec19serializePongPacketERK7QString
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializePongPacket(const QString &name)
{
    m_packet.setId(Pong);
    m_packet << name;
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 819, as _ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInvokeReplyPacketERK7QStringiRK8QVariant
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeInvokeReplyPacket(const QString &name, int ackedSerialId, const QVariant &value)
{
    m_packet.setId(InvokeReplyPacket);
    m_packet << name;
    m_packet << ackedSerialId;
    m_packet << value;
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 331, as _ZN20QRemoteObjectPackets16QDataStreamCodec24serializeHandshakePacketEv
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeHandshakePacket()
{
    m_packet.setId(Handshake);
    m_packet << QString(protocolVersion);
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 784, as _ZN20QRemoteObjectPackets16QDataStreamCodec27serializeRemoveObjectPacketERK7QString
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeRemoveObjectPacket(const QString &name)
{
    m_packet.setId(RemoveObject);
    m_packet << name;
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 771, as _ZN20QRemoteObjectPackets16QDataStreamCodec24serializeAddObjectPacketERK7QStringb
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeAddObjectPacket(const QString &name, bool isDynamic)
{
    m_packet.setId(AddObject);
    m_packet << name;
    m_packet << isDynamic;
    m_packet.finishPacket();
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 286, as _ZN20QRemoteObjectPackets16QDataStreamCodec17serializePropertyER11QDataStreamPK23QRemoteObjectSourceBasei
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeProperty(QDataStream &ds, const QRemoteObjectSourceBase *source, int internalIndex)
{
    const int propertyIndex = source->m_api->sourcePropertyIndex(internalIndex);
    Q_ASSERT (propertyIndex >= 0);
    const auto target = source->m_api->isAdapterProperty(internalIndex) ? source->m_adapter : source->m_object;
    const auto property = target->metaObject()->property(propertyIndex);
    const QVariant value = property.read(target);
    if (property.metaType().flags().testFlag(QMetaType::PointerToQObject)) {
        auto const childSource = source->m_children.value(internalIndex);
        auto valueAsPointerToQObject = qvariant_cast<QObject *>(value);
        if (childSource->m_object != valueAsPointerToQObject)
            childSource->resetObject(valueAsPointerToQObject);
        QRO_ qro(childSource);
        if (source->d->isDynamic && qro.type == ObjectType::CLASS && childSource->m_object && !source->d->sentTypes.contains(qro.typeName)) {
            QDataStream classDef(&qro.classDefinition, QIODevice::WriteOnly);
            serializeDefinition(classDef, childSource);
            source->d->sentTypes.insert(qro.typeName);
        }
        ds << QVariant::fromValue<QRO_>(qro);
        if (qro.isNull)
            return;
        const int propertyCount = childSource->m_api->propertyCount();
        // Put the properties in a buffer, the receiver may not know how to
        // interpret the types until it registers new ones.
        QDataStream params(&qro.parameters, QIODevice::WriteOnly);
        params << propertyCount;
        for (int internalIndex = 0; internalIndex < propertyCount; ++internalIndex)
            serializeProperty(params, childSource, internalIndex);
        ds << qro.parameters;
        return;
    }
    if (source->d->isDynamic && property.userType() == QMetaType::QVariant
        && value.metaType().flags().testFlag(QMetaType::IsGadget)) {
        const auto typeName = QString::fromLatin1(value.metaType().name());
        if (!source->d->sentTypes.contains(typeName)) {
            QRO_ qro(value);
            ds << QVariant::fromValue<QRO_>(qro);
            ds << qro.parameters;
            source->d->sentTypes.insert(typeName);
            return;
        }
    }
    ds << encodeVariant(value);
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 346, as _ZN20QRemoteObjectPackets16QDataStreamCodec19serializePropertiesEPK23QRemoteObjectSourceBase
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline void QDataStreamCodec::serializeProperties(const QRemoteObjectSourceBase *source)
{
    const SourceApiMap *api = source->m_api;

    //Now copy the property data
    const int numProperties = api->propertyCount();
    m_packet << quint32(numProperties);  //Number of properties

    for (int internalIndex = 0; internalIndex < numProperties; ++internalIndex)
        serializeProperty(source, internalIndex);
}
}  // namespace QRemoteObjectPackets
//  -----------------------------------------------------------------------

//  Only a class built on QRemoteObjectPackets::QDataStreamCodec may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectPackets_QDataStreamCodec : QRemoteObjectPackets::QDataStreamCodec {
  using QRemoteObjectPackets::QDataStreamCodec::getPayload;
  using QRemoteObjectPackets::QDataStreamCodec::reset;
};

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeObjectListPacket(con
//      st ObjectInfoList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec25serializeObjectListPacketERK5QListINS_10ObjectInfoEE(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectPackets::ObjectInfoList *a0) {
  self->serializeObjectListPacket(*a0);
}

//  void QRemoteObjectPackets::QDataStreamCodec::deserializeObjectListPacket(
//      QDataStream &in, ObjectInfoList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec27deserializeObjectListPacketER11QDataStreamR5QListINS_10ObjectInfoEE(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *in,
    QRemoteObjectPackets::ObjectInfoList *a1) {
  self->deserializeObjectListPacket(*in, *a1);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeInitPacket(const
//      QRemoteObjectRootSource *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializeInitPacketEPK23QRemoteObjectRootSource(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectRootSource *a0) {
  self->serializeInitPacket(a0);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeInitDynamicPacket(co
//      nst QRemoteObjectRootSource *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInitDynamicPacketEPK23QRemoteObjectRootSource(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectRootSource *a0) {
  self->serializeInitDynamicPacket(a0);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePropertyChangePacke
//      t(QRemoteObjectSourceBase *source, int signalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec29serializePropertyChangePacketEP23QRemoteObjectSourceBasei(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QRemoteObjectSourceBase *source,
    int signalIndex) {
  self->serializePropertyChangePacket(source, signalIndex);
}

//  void QRemoteObjectPackets::QDataStreamCodec::deserializePropertyChangePac
//      ket(QDataStream &in, int &index, QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec31deserializePropertyChangePacketER11QDataStreamRiR8QVariant(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *in,
    int *index,
    QVariant *value) {
  self->deserializePropertyChangePacket(*in, *index, *value);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeProperty(const
//      QRemoteObjectSourceBase *source, int internalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec17serializePropertyEPK23QRemoteObjectSourceBasei(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectSourceBase *source,
    int internalIndex) {
  self->serializeProperty(source, internalIndex);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePingPacket(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePingPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->serializePingPacket(*name);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePongPacket(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePongPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->serializePongPacket(*name);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeInvokePacket(const
//      QString &name, int call, int index, const QVariantList &args, int
//      serialId, int propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec21serializeInvokePacketERK7QStringiiRK5QListI8QVariantEii(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name,
    int call,
    int index,
    const QList<QVariant> *args,
    int serialId,
    int propertyIndex) {
  self->serializeInvokePacket(
      *name,
      call,
      index,
      *args,
      serialId,
      propertyIndex);
}

//  void QRemoteObjectPackets::QDataStreamCodec::deserializeInvokePacket(QDat
//      aStream &in, int &call, int &index, QVariantList &args, int
//      &serialId, int &propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec23deserializeInvokePacketER11QDataStreamRiS3_R5QListI8QVariantES3_S3_(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *in,
    int *call,
    int *index,
    QVariantList *args,
    int *serialId,
    int *propertyIndex) {
  self->deserializeInvokePacket(
      *in,
      *call,
      *index,
      *args,
      *serialId,
      *propertyIndex);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeInvokeReplyPacket(co
//      nst QString &name, int ackedSerialId, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInvokeReplyPacketERK7QStringiRK8QVariant(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name,
    int ackedSerialId,
    const QVariant *value) {
  self->serializeInvokeReplyPacket(*name, ackedSerialId, *value);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeHandshakePacket()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeHandshakePacketEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  self->serializeHandshakePacket();
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeRemoveObjectPacket(c
//      onst QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec27serializeRemoveObjectPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->serializeRemoveObjectPacket(*name);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeAddObjectPacket(cons
//      t QString &name, bool isDynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeAddObjectPacketERK7QStringb(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name,
    bool isDynamic) {
  self->serializeAddObjectPacket(*name, isDynamic);
}

//  void QRemoteObjectPackets::QDataStreamCodec::deserializeAddObjectPacket(Q
//      DataStream &a0, bool &isDynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec26deserializeAddObjectPacketER11QDataStreamRb(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *a0,
    bool *isDynamic) {
  self->deserializeAddObjectPacket(*a0, *isDynamic);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::deserializeInitPacket(QDataSt
//      ream &a0, QVariantList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec21deserializeInitPacketER11QDataStreamR5QListI8QVariantE(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *a0,
    QVariantList *a1) {
  self->deserializeInitPacket(*a0, *a1);
}

//  void QRemoteObjectPackets::QDataStreamCodec::deserializeInvokeReplyPacket
//      (QDataStream &in, int &ackedSerialId, QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec28deserializeInvokeReplyPacketER11QDataStreamRiR8QVariant(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QDataStream *in,
    int *ackedSerialId,
    QVariant *value) {
  self->deserializeInvokeReplyPacket(*in, *ackedSerialId, *value);
}

//  const QByteArray &QRemoteObjectPackets::QDataStreamCodec::getPayload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloadEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  return new QByteArray(self->getPayload());
}

//  void QRemoteObjectPackets::QDataStreamCodec::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  self->reset();
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeProperties(const
//      QRemoteObjectSourceBase *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePropertiesEPK23QRemoteObjectSourceBase(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectSourceBase *source) {
  self->serializeProperties(source);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeInitPacket(const
//      QRemoteObjectRootSource *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serializeInitPacketEPK23QRemoteObjectRootSource(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QRemoteObjectRootSource *a0) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializeInitPacket(a0);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePropertyChangePacke
//      t(QRemoteObjectSourceBase *source, int signalIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec29serializePropertyChangePacketEP23QRemoteObjectSourceBasei(
    QRemoteObjectPackets::QDataStreamCodec *self,
    QRemoteObjectSourceBase *source,
    int signalIndex) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializePropertyChangePacket(
      source,
      signalIndex);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePingPacket(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePingPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializePingPacket(*name);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializePongPacket(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec19serializePongPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializePongPacket(*name);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeInvokeReplyPacket(co
//      nst QString &name, int ackedSerialId, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec26serializeInvokeReplyPacketERK7QStringiRK8QVariant(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name,
    int ackedSerialId,
    const QVariant *value) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializeInvokeReplyPacket(
      *name,
      ackedSerialId,
      *value);
}

//  void QRemoteObjectPackets::QDataStreamCodec::serializeHandshakePacket()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeHandshakePacketEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializeHandshakePacket();
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeRemoveObjectPacket(c
//      onst QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec27serializeRemoveObjectPacketERK7QString(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializeRemoveObjectPacket(
      *name);
}

//  void
//      QRemoteObjectPackets::QDataStreamCodec::serializeAddObjectPacket(cons
//      t QString &name, bool isDynamic)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec24serializeAddObjectPacketERK7QStringb(
    QRemoteObjectPackets::QDataStreamCodec *self,
    const QString *name,
    bool isDynamic) {
  self->QRemoteObjectPackets::QDataStreamCodec::serializeAddObjectPacket(
      *name,
      isDynamic);
}

//  const QByteArray &QRemoteObjectPackets::QDataStreamCodec::getPayload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloadEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  return new QByteArray(
      static_cast<OwnQRemoteObjectPackets_QDataStreamCodec *>(self)->OwnQRemoteObjectPackets_QDataStreamCodec::getPayload());
}

//  void QRemoteObjectPackets::QDataStreamCodec::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  static_cast<OwnQRemoteObjectPackets_QDataStreamCodec *>(self)->OwnQRemoteObjectPackets_QDataStreamCodec::reset();
}
