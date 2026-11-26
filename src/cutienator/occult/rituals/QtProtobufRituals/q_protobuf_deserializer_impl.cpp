//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/private/qprotobufdeserializerbase_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qtprotobuflogging_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtProtobuf/qprotobufserializer.h>
#include <QtProtobuf/private/protobufscalarserializers_p.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qprotobufserializer_p.h>
#include <QtProtobuf/private/qprotobufserializerbase_p.h>
#include <QtProtobuf/private/qtprotobufdefs_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/qprotobufmessage.h>
#include <QtProtobuf/qtprotobuftypes.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qlist.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qreadwritelock.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 18, as _ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16QProtobufMessage
inline bool QProtobufDeserializerBase::deserializeMessageField(QProtobufMessage *message)
{
    Q_ASSERT(message != nullptr);

    auto prevCachedRepeatedIterator = std::move(m_cachedRepeatedIterator);
    auto prevCachedPropertyValue = m_cachedPropertyValue;
    auto prevCachedIndex = m_cachedIndex;
    clearCachedValue();
    bool result = deserializeMessage(message);
    m_cachedPropertyValue = prevCachedPropertyValue;
    m_cachedIndex = prevCachedIndex;
    m_cachedRepeatedIterator = std::move(prevCachedRepeatedIterator);

    return result;
}

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 12, as _ZN25QProtobufDeserializerBaseC2Ev
inline QProtobufDeserializerBase::QProtobufDeserializerBase()
    = default;

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 15, as _ZN25QProtobufDeserializerBaseD1Ev
inline QProtobufDeserializerBase::~QProtobufDeserializerBase()
    = default;

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 129, as _ZN25QProtobufDeserializerBase16clearCachedValueEv
inline void QProtobufDeserializerBase::clearCachedValue()
{
    m_cachedPropertyValue.clear();
    m_cachedIndex = -1;
    m_cachedRepeatedIterator = {};
}

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 34, as _ZN25QProtobufDeserializerBase18deserializeMessageEP16QProtobufMessage
inline bool QProtobufDeserializerBase::deserializeMessage(QProtobufMessage *message)
{
    Q_ASSERT(message != nullptr);

    const auto *ordering = message->propertyOrdering();
    for (int fieldIndex = nextFieldIndex(message); fieldIndex >= 0;
         fieldIndex = nextFieldIndex(message)) {
        QtProtobufPrivate::QProtobufFieldInfo fieldInfo(*ordering, fieldIndex);
        if (m_cachedIndex != fieldIndex) {
            if (!storeCachedValue(message)) {
                setError(QAbstractProtobufSerializer::Error::InvalidFormat,
                         "Unable to store the property in message");
                return false;
            }

            m_cachedPropertyValue = QtProtobufSerializerHelpers::messageProperty(message, fieldInfo,
                                                                                 true);
            m_cachedIndex = fieldIndex;
        }

        QMetaType metaType = m_cachedPropertyValue.metaType();
        if (metaType.flags().testFlag(QMetaType::IsPointer)) {
            if (!deserializeMessageField(m_cachedPropertyValue.value<QProtobufMessage *>()))
                return false;

            continue;
        }

        const auto fieldFlags = fieldInfo.fieldFlags();
        if ((fieldFlags.testFlags(RepeatedMessageFlags)
             || fieldFlags.testFlags({ QtProtobufPrivate::FieldFlag::Map }))
            && m_cachedPropertyValue.canView(QMetaType::fromType<QProtobufRepeatedIterator>())) {
            if (!m_cachedRepeatedIterator.isValid())
                m_cachedRepeatedIterator = m_cachedPropertyValue.view<QProtobufRepeatedIterator>();

            if (!deserializeMessageField(m_cachedRepeatedIterator.addNext()))
                return false;

            m_cachedRepeatedIterator.push();
            continue;
        }

        if (fieldFlags.testFlag(QtProtobufPrivate::FieldFlag::Enum)) {
            if (!deserializeEnum(m_cachedPropertyValue, fieldInfo)) {
                setError(QAbstractProtobufSerializer::Error::UnknownType,
                         "Unable to covert enum field to compatible serialization format");
                return false;
            }
            continue;
        }

        if (deserializeScalarField(m_cachedPropertyValue, fieldInfo)) {
            if (!m_cachedPropertyValue.isValid())
                return false;

            continue;
        }

        auto handler = QtProtobufPrivate::findHandler(metaType);
        if (!handler.deserializer) {
            qProtoWarning() << "No deserializer for type" << metaType.name();
            setError(QAbstractProtobufSerializer::Error::UnknownType,
                     QString::fromUtf8("No deserializer is registered for type %1")
                         .arg(QString::fromUtf8(metaType.name())));
            return false;
        }

        handler.deserializer([this](QProtobufMessage *
                                        message) { return this->deserializeMessageField(message); },
                             m_cachedPropertyValue.data());
    }

    if (!storeCachedValue(message)) {
        setError(QAbstractProtobufSerializer::Error::InvalidFormat,
                 "Unable to store the property in message");
        return false;
    }

    return true;
}

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 115, as _ZN25QProtobufDeserializerBase16storeCachedValueEP16QProtobufMessage
inline bool QProtobufDeserializerBase::storeCachedValue(QProtobufMessage *message)
{
    bool ok = true;
    if (m_cachedIndex >= 0 && !m_cachedPropertyValue.isNull()) {
        const auto *ordering = message->propertyOrdering();
        QtProtobufPrivate::QProtobufFieldInfo fieldInfo(*ordering, m_cachedIndex);
        ok = QtProtobufSerializerHelpers::setMessageProperty(message, fieldInfo,
                                                             m_cachedPropertyValue);

        clearCachedValue();
    }
    return ok;
}

//  from ../qtgrpc/src/protobuf/qtprotobufserializerhelpers.cpp, line 9, as _ZN27QtProtobufSerializerHelpers15messagePropertyEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoEb
inline QVariant
QtProtobufSerializerHelpers::messageProperty(const QProtobufMessage *message,
                                             const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo,
                                             bool allowInitialize)
{
    const auto *metaObject = QtProtobufSerializerHelpers::messageMetaObject(message);
    int propertyIndex = fieldInfo.propertyIndex() + metaObject->propertyOffset();
    QMetaProperty metaProperty = metaObject->property(propertyIndex);

    if (!metaProperty.isValid())
        return {};

    if (fieldInfo.fieldFlags() & QtProtobufPrivate::FieldFlag::ExplicitPresence
        && !allowInitialize) {
        int hasPropertyIndex = propertyIndex + 1;
        QMetaProperty hasProperty = metaObject->property(hasPropertyIndex);
        Q_ASSERT_X(hasProperty.isValid() && hasProperty.metaType().id() == QMetaType::Bool,
                   "QProtobufMessage",
                   "The field with the explicit presence requirement doesn't have the follow 'has' "
                   "property.");
        if (!hasProperty.readOnGadget(message).toBool())
            return QVariant(metaProperty.metaType());
    }

    QVariant propertyValue = metaProperty.readOnGadget(message);
    return propertyValue;
}

//  from ../qtgrpc/src/protobuf/qtprotobufserializerhelpers.cpp, line 61, as _ZN27QtProtobufSerializerHelpers17messageMetaObjectEPK16QProtobufMessage
inline const QMetaObject *QtProtobufSerializerHelpers::messageMetaObject(const QProtobufMessage *message)
{
    Q_ASSERT(message);
    const auto *pMessage = QProtobufMessagePrivate::get(message);
    Q_ASSERT(pMessage);
    return pMessage->metaObject;
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 303, as _ZN25QProtobufDeserializerImpl5resetE14QByteArrayView
inline void QProtobufDeserializerImpl::reset(QByteArrayView data)
{
    m_it = QProtobufSelfcheckIterator::fromView(data);
    m_state.push_back(data.end());
    clearCachedValue();
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 310, as _ZN25QProtobufDeserializerImpl8setErrorEN27QAbstractProtobufSerializer5ErrorE14QAnyStringView
inline void QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::Error error,
                                         QAnyStringView errorString)
{
    m_parent->lastError = error;
    m_parent->lastErrorString = errorString.toString();
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 466, as _ZN25QProtobufDeserializerImpl10skipVarintEv
inline void QProtobufDeserializerImpl::skipVarint()
{
    while ((*m_it) & 0x80)
        ++m_it;
    ++m_it;
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 485, as _ZN25QProtobufDeserializerImpl29setUnexpectedEndOfStreamErrorEv
inline void QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()
{
    setError(QAbstractProtobufSerializer::Error::UnexpectedEndOfStream,
             QCoreApplication::translate("QtProtobuf", "Unexpected end of stream"));
}
//  -----------------------------------------------------------------------

//  void QProtobufDeserializerImpl::reset(QByteArrayView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl5resetE14QByteArrayView(
    QProtobufDeserializerImpl *self,
    const QByteArrayView *data) {
  self->reset(*data);
}

//  void
//      QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::Erro
//      r error, QAnyStringView errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl8setErrorEN27QAbstractProtobufSerializer5ErrorE14QAnyStringView(
    QProtobufDeserializerImpl *self,
    QAbstractProtobufSerializer::Error error,
    const QString *errorString) {
  self->setError(error, QAnyStringView(*errorString));
}

//  void QProtobufDeserializerImpl::skipVarint()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl10skipVarintEv(
    QProtobufDeserializerImpl *self) {
  self->skipVarint();
}

//  void QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl29setUnexpectedEndOfStreamErrorEv(
    QProtobufDeserializerImpl *self) {
  self->setUnexpectedEndOfStreamError();
}
