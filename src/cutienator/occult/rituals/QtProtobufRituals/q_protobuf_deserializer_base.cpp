//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufdeserializerbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufdeserializerbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtProtobuf/private/qprotobufdeserializerbase_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qtprotobuflogging_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 15, as _ZN25QProtobufDeserializerBaseD1Ev
inline QProtobufDeserializerBase::~QProtobufDeserializerBase()
    = default;

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

//  from ../qtgrpc/src/protobuf/qtprotobufserializerhelpers.cpp, line 61, as _ZN27QtProtobufSerializerHelpers17messageMetaObjectEPK16QProtobufMessage
inline const QMetaObject *QtProtobufSerializerHelpers::messageMetaObject(const QProtobufMessage *message)
{
    Q_ASSERT(message);
    const auto *pMessage = QProtobufMessagePrivate::get(message);
    Q_ASSERT(pMessage);
    return pMessage->metaObject;
}

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 129, as _ZN25QProtobufDeserializerBase16clearCachedValueEv
inline void QProtobufDeserializerBase::clearCachedValue()
{
    m_cachedPropertyValue.clear();
    m_cachedIndex = -1;
    m_cachedRepeatedIterator = {};
}
//  -----------------------------------------------------------------------

//  A QProtobufDeserializerBase that Python can take functions over in. Every QProtobufDeserializerBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQProtobufDeserializerBaseCall0)(const void *, QProtobufMessage *, int *);
typedef int (*CuteQProtobufDeserializerBaseCall1)(const void *, QProtobufMessage *, int *);
class CuteQProtobufDeserializerBase : public QProtobufDeserializerBase {
public:
  using QProtobufDeserializerBase::QProtobufDeserializerBase;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16QProtobufMessage")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QProtobufDeserializerBase14nextFieldIndexEP16QProtobufMessage")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool
  //      QProtobufDeserializerBase::deserializeMessageField(QProtobufMessa
  //      ge *message)
  bool deserializeMessageField(QProtobufMessage *message) override {
    if (taken[0]) {
      int handled = 0;
      CuteQProtobufDeserializerBaseCall0 call = reinterpret_cast<CuteQProtobufDeserializerBaseCall0>(taken[0]);
      bool given = call(this, message, &handled);
      if (handled) return given;
    }
    return QProtobufDeserializerBase::deserializeMessageField(message);
  }

  //  int QProtobufDeserializerBase::nextFieldIndex(QProtobufMessage
  //      *message)
  int nextFieldIndex(QProtobufMessage *message) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProtobufDeserializerBaseCall1 call = reinterpret_cast<CuteQProtobufDeserializerBaseCall1>(taken[1]);
      int given = call(this, message, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  void QProtobufDeserializerBase::clearCachedValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerBase16clearCachedValueEv(
    QProtobufDeserializerBase *self) {
  self->clearCachedValue();
}

//  void
//      QProtobufDeserializerBase::setError(QAbstractProtobufSerializer::Erro
//      r error, QAnyStringView errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerBase8setErrorEN27QAbstractProtobufSerializer5ErrorE14QAnyStringView(
    QProtobufDeserializerBase *self,
    QAbstractProtobufSerializer::Error error,
    const QString *errorString) {
  self->setError(error, QAnyStringView(*errorString));
}

//  bool QProtobufDeserializerBase::deserializeMessageField(QProtobufMessage
//      *message)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16QProtobufMessage(
    QProtobufDeserializerBase *self,
    QProtobufMessage *message) {
  return self->deserializeMessageField(message);
}

//  bool QProtobufDeserializerBase::deserializeEnum(QVariant &value, const
//      QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QProtobufDeserializerBase15deserializeEnumER8QVariantRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufDeserializerBase *self,
    QVariant *value,
    const QtProtobufPrivate::QProtobufFieldInfo *fieldInfo) {
  return self->deserializeEnum(*value, *fieldInfo);
}

//  int QProtobufDeserializerBase::nextFieldIndex(QProtobufMessage *message)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QProtobufDeserializerBase14nextFieldIndexEP16QProtobufMessage(
    QProtobufDeserializerBase *self,
    QProtobufMessage *message) {
  return self->nextFieldIndex(message);
}

//  bool QProtobufDeserializerBase::deserializeScalarField(QVariant &value,
//      const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QProtobufDeserializerBase22deserializeScalarFieldER8QVariantRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufDeserializerBase *self,
    QVariant *value,
    const QtProtobufPrivate::QProtobufFieldInfo *fieldInfo) {
  return self->deserializeScalarField(*value, *fieldInfo);
}

//  a Python function taken by a CuteQProtobufDeserializerBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProtobufDeserializerBase(
    QProtobufDeserializerBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProtobufDeserializerBase *>(self)->take(key, call);
}
