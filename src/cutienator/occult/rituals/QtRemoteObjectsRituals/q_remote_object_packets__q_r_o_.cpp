//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 402, as local:qremoteobjectpacket.cpp:getObjectType
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
static ObjectType getObjectType(const QString &typeName)
{
    if (typeName == QLatin1String("QAbstractItemModelAdapter"))
        return ObjectType::MODEL;
    auto tid = QMetaType::fromName(typeName.toUtf8()).id();
    if (tid == QMetaType::UnknownType)
        return ObjectType::CLASS;
    QMetaType type(tid);
    auto mo = type.metaObject();
    if (mo && mo->inherits(&QAbstractItemModel::staticMetaObject))
        return ObjectType::MODEL;
    return ObjectType::CLASS;
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 875, as _ZN20QRemoteObjectPackets4QRO_C1EP23QRemoteObjectSourceBase
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline QRO_::QRO_(QRemoteObjectSourceBase *source)
    : name(source->name())
    , typeName(source->m_api->typeName())
    , type(source->m_adapter ? ObjectType::MODEL : getObjectType(typeName))
    , isNull(source->m_object == nullptr)
    , classDefinition()
    , parameters()
{}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 884, as _ZN20QRemoteObjectPackets4QRO_C1ERK8QVariant
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline QRO_::QRO_(const QVariant &value)
    : type(ObjectType::GADGET)
    , isNull(false)
{
    const auto metaType = value.metaType();
    auto meta = metaType.metaObject();
    QDataStream out(&classDefinition, QIODevice::WriteOnly);
    const int numProperties = meta->propertyCount();
    const auto name = metaType.name();
    const auto typeName = QByteArray::fromRawData(name, qsizetype(qstrlen(name)));
    out << quint32(0) << quint32(1);
    out << typeName;
    out << numProperties;
#ifdef QTRO_VERBOSE_PROTOCOL
    qDebug("Serializing POD definition to QRO_ (name = %s)", typeName.constData());
#endif
    for (int i = 0; i < numProperties; ++i) {
        const auto property = meta->property(i);
#ifdef QTRO_VERBOSE_PROTOCOL
        qDebug("  Data member %d (name = %s, type = %s):", i, property.name(), property.typeName());
#endif
        out << QByteArray::fromRawData(property.name(), qsizetype(qstrlen(property.name())));
        out << QByteArray::fromRawData(property.typeName(), qsizetype(qstrlen(property.typeName())));
    }
    int enumCount = meta->enumeratorCount() - meta->enumeratorOffset();
    out << quint32(enumCount);
    for (int j = meta->enumeratorOffset(); j < meta->enumeratorCount(); j++) {
        auto const enumMeta = meta->enumerator(j);
        serializeEnum(out, enumMeta);
    }
    QDataStream ds(&parameters, QIODevice::WriteOnly);
    ds << value;
#ifdef QTRO_VERBOSE_PROTOCOL
    qDebug() << "  Value:" << value;
#endif
}
}  // namespace QRemoteObjectPackets
//  -----------------------------------------------------------------------

//  QRemoteObjectPackets::QRO_::QRO_()
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::QRO_ *ritual_ZN20QRemoteObjectPackets4QRO_C1Ev() {
  return new QRemoteObjectPackets::QRO_();
}

//  QRemoteObjectPackets::QRO_::QRO_(QRemoteObjectSourceBase *source)
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::QRO_ *ritual_ZN20QRemoteObjectPackets4QRO_C1EP23QRemoteObjectSourceBase(
    QRemoteObjectSourceBase *source) {
  return new QRemoteObjectPackets::QRO_(source);
}

//  QRemoteObjectPackets::QRO_::QRO_(const QVariant &value)
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::QRO_ *ritual_ZN20QRemoteObjectPackets4QRO_C1ERK8QVariant(
    const QVariant *value) {
  return new QRemoteObjectPackets::QRO_(*value);
}

//  QRemoteObjectPackets::QRO_::~QRO_()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets4QRO_D1Ev(
    QRemoteObjectPackets::QRO_ *self) {
  delete self;
}
