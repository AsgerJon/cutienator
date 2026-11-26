//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsondocument.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore5Compat/private/qbinaryjsonarray_p.h>
#include <QtCore5Compat/private/qbinaryjsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 527, as local:qbinaryjson.cpp:isValidValueOffset
namespace QBinaryJsonPrivate {
inline bool isValidValueOffset(uint offset, uint tableOffset)
{
    return offset >= sizeof(Base)
        && isAlignedOffset(offset)
        && offset + sizeof(uint) <= tableOffset;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 461, as _ZNK18QBinaryJsonPrivate5Array13isValidHelperEjR15QVarLengthArrayINS_12IsValidFrameELx16EE
namespace QBinaryJsonPrivate {
inline bool Array::isValidHelper(uint maxSize, IsValidStack &stack) const
{
    if (!isAlignedOffset(tableOffset))
        return false;

    if (size > maxSize || tableOffset + length() * sizeof(offset) > size)
        return false;

    const offset *values = table();
    for (uint i = 0; i < length(); ++i) {
        if (!reinterpret_cast<const Value *>(values + i)->isValidHelper(this, stack))
            return false;
    }
    return true;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 435, as _ZNK18QBinaryJsonPrivate6Object13isValidHelperEjR15QVarLengthArrayINS_12IsValidFrameELx16EE
namespace QBinaryJsonPrivate {
inline bool Object::isValidHelper(uint maxSize, IsValidStack &stack) const
{
    if (!isAlignedOffset(tableOffset))
        return false;

    if (size > maxSize || tableOffset + length() * sizeof(offset) > size)
        return false;

    QString lastKey;
    for (uint i = 0; i < length(); ++i) {
        const uint entryOffset = table()[i];
        if (!isAlignedOffset(entryOffset) || entryOffset + sizeof(Entry) >= tableOffset)
            return false;
        const Entry *e = entryAt(i);
        if (!e->isValid(tableOffset - entryOffset))
            return false;
        const QString key = e->key();
        if (key < lastKey)
            return false;
        if (!e->value.isValidHelper(this, stack))
            return false;
        lastKey = key;
    }
    return true;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 506, as _ZNK18QBinaryJsonPrivate5Value17toScalarJsonValueEPKNS_4BaseE
namespace QBinaryJsonPrivate {
inline QJsonValue Value::toScalarJsonValue(const Base *b) const
{
    Q_ASSERT(type() != QJsonValue::Array && type() != QJsonValue::Object);

    switch (type()) {
    case QJsonValue::Null:
        return QJsonValue(QJsonValue::Null);
    case QJsonValue::Bool:
        return QJsonValue(toBoolean());
    case QJsonValue::Double:
        return QJsonValue(toDouble(b));
    case QJsonValue::String:
        return QJsonValue(toString(b));
    default:
        // This handled Undefined, and the out-of-range type codes 6 and 7,
        // which fit the three bit type field.
        // We should handle them gracefully, rather than trigger Q_UNREACHABLE()
        return QJsonValue(QJsonValue::Undefined);
    }
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 328, as _ZNK18QBinaryJsonPrivate9ConstData14toJsonDocumentEv
namespace QBinaryJsonPrivate {
inline QJsonDocument ConstData::toJsonDocument() const
{
    DocumentStack stack;
    stack.push_back(DocumentFrame(header->root()));

    while (true) {
        DocumentFrame &frame = stack.last();

        if (frame.index < frame.base->length()) {
            const uint i = frame.index++;

            const Value *value = nullptr;
            QString key;
            if (frame.isObject) {
                const Entry *e = static_cast<const Object *>(frame.base)->entryAt(i);
                value = &e->value;
                key = e->key();
            } else {
                value = static_cast<const Array *>(frame.base)->at(i);
            }

            const uint type = value->type();
            if (type == QJsonValue::Array || type == QJsonValue::Object) {
                const Base *child = value->base(frame.base);
                // This may reallocate, so frame must not be touched afterwards.
                stack.push_back(DocumentFrame(child, std::move(key)));
                continue;
            }

            const QJsonValue scalar = value->toScalarJsonValue(frame.base);
            if (frame.isObject)
                frame.object.insert(key, scalar);
            else
                frame.array.append(scalar);
            continue;
        }

        // This container is complete: hand it to its parent, or return it.
        if (stack.size() == 1) {
            return frame.isObject ? QJsonDocument(std::move(frame.object))
                                  : QJsonDocument(std::move(frame.array));
        } else {
            const QJsonValue val = frame.isObject ? QJsonValue(std::move(frame.object))
                                                  : QJsonValue(std::move(frame.array));
            const QString key = std::move(frame.key);
            stack.removeLast();

            DocumentFrame &parent = stack.last();
            if (parent.isObject)
                parent.object.insert(key, val);
            else
                parent.array.append(val);
        }
    }
}
}  // namespace QBinaryJsonPrivate
//  -----------------------------------------------------------------------

//  QBinaryJsonPrivate::ConstData::ConstData(const char *raw, uint a)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::ConstData *ritual_ZN18QBinaryJsonPrivate9ConstDataC1EPKcj(
    const char *raw,
    uint a) {
  return new QBinaryJsonPrivate::ConstData(raw, a);
}

//  QJsonDocument QBinaryJsonPrivate::ConstData::toJsonDocument() const
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZNK18QBinaryJsonPrivate9ConstData14toJsonDocumentEv(
    const QBinaryJsonPrivate::ConstData *self) {
  return new QJsonDocument(self->toJsonDocument());
}
