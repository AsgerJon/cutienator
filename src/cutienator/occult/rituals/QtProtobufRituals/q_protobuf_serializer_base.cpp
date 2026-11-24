//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializerbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializerbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtProtobuf/private/qprotobufserializerbase_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qtprotobufdefs_p.h>
#include <QtProtobuf/private/qtprotobuflogging_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/qprotobufmessage.h>
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <QtProtobuf/qprotobufrepeatediterator.h>
#include <QtProtobuf/qtprotobuftypes.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from ../qtgrpc/src/protobuf/qprotobufserializerbase.cpp, line 76, as _ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE
inline void QProtobufSerializerBase::serializeMessageField(const QProtobufMessage *message,
                                                    const QtProtobufPrivate::QProtobufFieldInfo
                                                        &fieldInfo)
{
    serializeMessageFieldBegin();
    serializeMessage(message);
    serializeMessageFieldEnd(message, fieldInfo);
}

//  from ../qtgrpc/src/protobuf/qtprotobufserializerhelpers.cpp, line 61, as _ZN27QtProtobufSerializerHelpers17messageMetaObjectEPK16QProtobufMessage
inline const QMetaObject *QtProtobufSerializerHelpers::messageMetaObject(const QProtobufMessage *message)
{
    Q_ASSERT(message);
    const auto *pMessage = QProtobufMessagePrivate::get(message);
    Q_ASSERT(pMessage);
    return pMessage->metaObject;
}

//  from ../qtgrpc/src/protobuf/qprotobufserializerbase.cpp, line 21, as _ZN23QProtobufSerializerBase16serializeMessageEPK16QProtobufMessage
inline void QProtobufSerializerBase::serializeMessage(const QProtobufMessage *message)
{
    Q_ASSERT(message != nullptr);

    const auto *ordering = message->propertyOrdering();
    Q_ASSERT(ordering != nullptr);

    for (int index = 0; index < ordering->fieldCount(); ++index) {
        int fieldNumber = ordering->fieldNumber(index);
        Q_ASSERT_X(fieldNumber <= ProtobufFieldNumMax && fieldNumber >= ProtobufFieldNumMin, "",
                   "Protobuf field number is out of range");
        QtProtobufPrivate::QProtobufFieldInfo fieldInfo(*ordering, index);
        QVariant value = QtProtobufSerializerHelpers::messageProperty(message, fieldInfo);
        QMetaType metaType = value.metaType();

        // Empty value
        if (metaType.id() == QMetaType::UnknownType || value.isNull())
            continue;

        if (metaType.flags().testFlag(QMetaType::IsPointer)) {
            serializeMessageField(value.value<QProtobufMessage *>(), fieldInfo);
            continue;
        }

        if (value.canView(QMetaType::fromType<QProtobufRepeatedIterator>())) {
            QProtobufRepeatedIterator propertyIt = value.view<QProtobufRepeatedIterator>();
            while (propertyIt.hasNext())
                serializeMessageField(propertyIt.next(), fieldInfo);
            continue;
        }

        QtProtobufPrivate::FieldFlags flags = fieldInfo.fieldFlags();
        // Convert enums to something known by scalar type serializers
        if (flags.testFlag(QtProtobufPrivate::FieldFlag::Enum)) {
            if (!serializeEnum(value, fieldInfo))
                qProtoWarning() << metaType << " is not registered as protobuf enum";
            continue;
        }

        if (serializeScalarField(value, fieldInfo))
            continue;

        auto handler = QtProtobufPrivate::findHandler(metaType);
        if (!handler.serializer) {
            qProtoWarning("No serializer found for type %s", value.typeName());
            continue;
        }

        handler.serializer([this](const QProtobufMessage *message,
                                  const QtProtobufPrivate::QProtobufFieldInfo
                                      &fieldInfo) { serializeMessageField(message, fieldInfo); },
                           value.constData(), fieldInfo);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QProtobufSerializerBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQProtobufSerializerBase : QProtobufSerializerBase {
  using QProtobufSerializerBase::serializeMessageField;
};

//  A QProtobufSerializerBase that Python can take functions over in. Every QProtobufSerializerBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQProtobufSerializerBaseCall0)(const void *, const QProtobufMessage *, const QtProtobufPrivate::QProtobufFieldInfo *, int *);
typedef bool (*CuteQProtobufSerializerBaseCall1)(const void *, const QVariant *, const QtProtobufPrivate::QProtobufFieldInfo *, int *);
typedef void (*CuteQProtobufSerializerBaseCall2)(const void *, int *);
typedef void (*CuteQProtobufSerializerBaseCall3)(const void *, const QProtobufMessage *, const QtProtobufPrivate::QProtobufFieldInfo *, int *);
class CuteQProtobufSerializerBase : public QProtobufSerializerBase {
public:
  using QProtobufSerializerBase::QProtobufSerializerBase;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QProtobufSerializerBase20serializeScalarFieldERK8QVariantRKN17QtProtobufPrivate18QProtobufFieldInfoE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QProtobufSerializerBase26serializeMessageFieldBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QProtobufSerializerBase24serializeMessageFieldEndEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QProtobufSerializerBase::serializeMessageField(const
  //      QProtobufMessage *message, const
  //      QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
  void serializeMessageField(
      const QProtobufMessage *message,
      const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo) override {
    if (taken[0]) {
      int handled = 0;
      CuteQProtobufSerializerBaseCall0 call = reinterpret_cast<CuteQProtobufSerializerBaseCall0>(taken[0]);
      call(this, message, &fieldInfo, &handled);
      if (handled) return;
    }
    QProtobufSerializerBase::serializeMessageField(message, fieldInfo);
  }

  //  bool QProtobufSerializerBase::serializeScalarField(const QVariant
  //      &value, const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
  bool serializeScalarField(
      const QVariant &value,
      const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProtobufSerializerBaseCall1 call = reinterpret_cast<CuteQProtobufSerializerBaseCall1>(taken[1]);
      bool given = call(this, &value, &fieldInfo, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QProtobufSerializerBase::serializeMessageFieldBegin()
  void serializeMessageFieldBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQProtobufSerializerBaseCall2 call = reinterpret_cast<CuteQProtobufSerializerBaseCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QProtobufSerializerBase::serializeMessageFieldEnd(const
  //      QProtobufMessage *a0, const QtProtobufPrivate::QProtobufFieldInfo
  //      &a1)
  void serializeMessageFieldEnd(
      const QProtobufMessage *a0,
      const QtProtobufPrivate::QProtobufFieldInfo &a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQProtobufSerializerBaseCall3 call = reinterpret_cast<CuteQProtobufSerializerBaseCall3>(taken[3]);
      call(this, a0, &a1, &handled);
      if (handled) return;
    }
  }
};

//  void QProtobufSerializerBase::serializeMessage(const QProtobufMessage
//      *message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerBase16serializeMessageEPK16QProtobufMessage(
    QProtobufSerializerBase *self,
    const QProtobufMessage *message) {
  self->serializeMessage(message);
}

//  bool QProtobufSerializerBase::isOneofOrOptionalField(QtProtobufPrivate::F
//      ieldFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QProtobufSerializerBase22isOneofOrOptionalFieldE6QFlagsIN17QtProtobufPrivate9FieldFlagEE(
    int flags) {
  return QProtobufSerializerBase::isOneofOrOptionalField(
      QFlags<QtProtobufPrivate::FieldFlag>::fromInt(flags));
}

//  void QProtobufSerializerBase::serializeMessageField(const
//      QProtobufMessage *message, const
//      QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufSerializerBase *self,
    const QProtobufMessage *message,
    const QtProtobufPrivate::QProtobufFieldInfo *fieldInfo) {
  self->serializeMessageField(message, *fieldInfo);
}

//  bool QProtobufSerializerBase::serializeScalarField(const QVariant &value,
//      const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QProtobufSerializerBase20serializeScalarFieldERK8QVariantRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufSerializerBase *self,
    const QVariant *value,
    const QtProtobufPrivate::QProtobufFieldInfo *fieldInfo) {
  return self->serializeScalarField(*value, *fieldInfo);
}

//  void QProtobufSerializerBase::serializeMessageFieldBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerBase26serializeMessageFieldBeginEv(
    QProtobufSerializerBase *self) {
  self->serializeMessageFieldBegin();
}

//  void QProtobufSerializerBase::serializeMessageFieldEnd(const
//      QProtobufMessage *a0, const QtProtobufPrivate::QProtobufFieldInfo
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerBase24serializeMessageFieldEndEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufSerializerBase *self,
    const QProtobufMessage *a0,
    const QtProtobufPrivate::QProtobufFieldInfo *a1) {
  self->serializeMessageFieldEnd(a0, *a1);
}

//  a Python function taken by a CuteQProtobufSerializerBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProtobufSerializerBase(
    QProtobufSerializerBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProtobufSerializerBase *>(self)->take(key, call);
}

//  void QProtobufSerializerBase::serializeMessageField(const
//      QProtobufMessage *message, const
//      QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE(
    QProtobufSerializerBase *self,
    const QProtobufMessage *message,
    const QtProtobufPrivate::QProtobufFieldInfo *fieldInfo) {
  static_cast<OwnQProtobufSerializerBase *>(self)->OwnQProtobufSerializerBase::serializeMessageField(
      message,
      *fieldInfo);
}
