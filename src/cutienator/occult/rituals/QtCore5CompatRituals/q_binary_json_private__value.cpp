//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsonvalue.h>
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

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 477, as _ZNK18QBinaryJsonPrivate5Value11usedStorageEPKNS_4BaseE
namespace QBinaryJsonPrivate {
inline uint Value::usedStorage(const Base *b) const
{
    uint s = 0;
    switch (type()) {
    case QJsonValue::Double:
        if (!isLatinOrIntValue())
            s = sizeof(double);
        break;
    case QJsonValue::String: {
        const char *d = data(b);
        s = isLatinOrIntValue()
                ? (sizeof(ushort)
                   + qFromLittleEndian(*reinterpret_cast<const ushort *>(d)))
                : (sizeof(int)
                   + sizeof(ushort) * qFromLittleEndian(*reinterpret_cast<const int *>(d)));
        break;
    }
    case QJsonValue::Array:
    case QJsonValue::Object:
        s = base(b)->size;
        break;
    case QJsonValue::Null:
    case QJsonValue::Bool:
    default:
        break;
    }
    return alignedSize(s);
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

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 563, as _ZN18QBinaryJsonPrivate5Value15requiredStorageERK16QBinaryJsonValuePb
namespace QBinaryJsonPrivate {
inline uint Value::requiredStorage(const QBinaryJsonValue &v, bool *compressed)
{
    *compressed = false;
    switch (v.type()) {
    case QJsonValue::Double:
        if (QBinaryJsonPrivate::compressedNumber(v.toDouble()) != INT_MAX) {
            *compressed = true;
            return 0;
        }
        return sizeof(double);
    case QJsonValue::String: {
        QString s = v.toString();
        *compressed = QBinaryJsonPrivate::useCompressed(s);
        return QBinaryJsonPrivate::qStringSize(s, *compressed);
    }
    case QJsonValue::Array:
    case QJsonValue::Object:
        return v.base ? uint(v.base->size) : sizeof(QBinaryJsonPrivate::Base);
    case QJsonValue::Undefined:
    case QJsonValue::Null:
    case QJsonValue::Bool:
        break;
    }
    return 0;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 589, as _ZN18QBinaryJsonPrivate5Value12valueToStoreERK16QBinaryJsonValuej
namespace QBinaryJsonPrivate {
inline uint Value::valueToStore(const QBinaryJsonValue &v, uint offset)
{
    switch (v.type()) {
    case QJsonValue::Undefined:
    case QJsonValue::Null:
        break;
    case QJsonValue::Bool:
        return v.toBool();
    case QJsonValue::Double: {
        int c = QBinaryJsonPrivate::compressedNumber(v.toDouble());
        if (c != INT_MAX)
            return c;
    }
        Q_FALLTHROUGH();
    case QJsonValue::String:
    case QJsonValue::Array:
    case QJsonValue::Object:
        return offset;
    }
    return 0;
}
}  // namespace QBinaryJsonPrivate
//  -----------------------------------------------------------------------

//  int QBinaryJsonPrivate::Value::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QBinaryJsonPrivate5Value8intValueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->intValue();
}

//  const char *QBinaryJsonPrivate::Value::data(const Base *b) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK18QBinaryJsonPrivate5Value4dataEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->data(b);
}

//  uint QBinaryJsonPrivate::Value::usedStorage(const Base *b) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Value11usedStorageEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->usedStorage(b);
}

//  bool QBinaryJsonPrivate::Value::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value9toBooleanEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->toBoolean();
}

//  double QBinaryJsonPrivate::Value::toDouble(const Base *b) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK18QBinaryJsonPrivate5Value8toDoubleEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->toDouble(b);
}

//  QString QBinaryJsonPrivate::Value::toString(const Base *b) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBinaryJsonPrivate5Value8toStringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QString(self->toString(b));
}

//  String QBinaryJsonPrivate::Value::asString(const Base *b) const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::String *ritual_ZNK18QBinaryJsonPrivate5Value8asStringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QBinaryJsonPrivate::String(self->asString(b));
}

//  Latin1String QBinaryJsonPrivate::Value::asLatin1String(const Base *b)
//      const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Latin1String *ritual_ZNK18QBinaryJsonPrivate5Value14asLatin1StringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QBinaryJsonPrivate::Latin1String(self->asLatin1String(b));
}

//  const Base *QBinaryJsonPrivate::Value::base(const Base *b) const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Base *ritual_ZNK18QBinaryJsonPrivate5Value4baseEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->base(b);
}

//  QJsonValue QBinaryJsonPrivate::Value::toScalarJsonValue(const Base *b)
//      const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QBinaryJsonPrivate5Value17toScalarJsonValueEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QJsonValue(self->toScalarJsonValue(b));
}

//  uint QBinaryJsonPrivate::Value::requiredStorage(const QBinaryJsonValue
//      &v, bool *compressed)
extern "C" Q_DECL_EXPORT
uint ritual_ZN18QBinaryJsonPrivate5Value15requiredStorageERK16QBinaryJsonValuePb(
    const QBinaryJsonValue *v,
    bool *compressed) {
  return QBinaryJsonPrivate::Value::requiredStorage(*v, compressed);
}

//  uint QBinaryJsonPrivate::Value::valueToStore(const QBinaryJsonValue &v,
//      uint offset)
extern "C" Q_DECL_EXPORT
uint ritual_ZN18QBinaryJsonPrivate5Value12valueToStoreERK16QBinaryJsonValuej(
    const QBinaryJsonValue *v,
    uint offset) {
  return QBinaryJsonPrivate::Value::valueToStore(*v, offset);
}

//  void QBinaryJsonPrivate::Value::setIsLatinKey(bool isLatinKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value13setIsLatinKeyEb(
    QBinaryJsonPrivate::Value *self,
    bool isLatinKey) {
  self->setIsLatinKey(isLatinKey);
}

//  bool QBinaryJsonPrivate::Value::isLatinKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value10isLatinKeyEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->isLatinKey();
}

//  void QBinaryJsonPrivate::Value::setIsLatinOrIntValue(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value20setIsLatinOrIntValueEb(
    QBinaryJsonPrivate::Value *self,
    bool v) {
  self->setIsLatinOrIntValue(v);
}

//  bool QBinaryJsonPrivate::Value::isLatinOrIntValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value17isLatinOrIntValueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->isLatinOrIntValue();
}

//  void QBinaryJsonPrivate::Value::setType(uint type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value7setTypeEj(
    QBinaryJsonPrivate::Value *self,
    uint type) {
  self->setType(type);
}

//  uint QBinaryJsonPrivate::Value::type() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Value4typeEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->type();
}

//  void QBinaryJsonPrivate::Value::setValue(uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value8setValueEj(
    QBinaryJsonPrivate::Value *self,
    uint value) {
  self->setValue(value);
}

//  uint QBinaryJsonPrivate::Value::value() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Value5valueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->value();
}

//  QBinaryJsonPrivate::Value::~Value()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5ValueD1Ev(
    QBinaryJsonPrivate::Value *self) {
  delete self;
}
