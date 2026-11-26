//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonvalue.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4jsonobject_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4booleanobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qstack.h>
#include <QtCore/qstringlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 28, as local:qv4jsonobject.cpp:DEBUG
#if defined(PARSER_DEBUG)
#define DEBUG qDebug() << QByteArray(4*indent, ' ').constData()
#endif  // defined(PARSER_DEBUG)

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 959, as _ZN3QV410JsonObject13fromJsonValueEPNS_15ExecutionEngineERK10QJsonValue
namespace QV4 {
inline ReturnedValue JsonObject::fromJsonValue(ExecutionEngine *engine, const QJsonValue &value)
{
    if (value.isString())
        return engine->newString(value.toString())->asReturnedValue();
    else if (value.isDouble())
        return Encode(value.toDouble());
    else if (value.isBool())
        return Encode(value.toBool());
    else if (value.isArray())
        return fromJsonArray(engine, value.toArray());
    else if (value.isObject())
        return fromJsonObject(engine, value.toObject());
    else if (value.isNull())
        return Encode::null();
    else
        return Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 1005, as _ZN3QV410JsonObject14fromJsonObjectEPNS_15ExecutionEngineERK11QJsonObject
namespace QV4 {
inline QV4::ReturnedValue JsonObject::fromJsonObject(ExecutionEngine *engine, const QJsonObject &object)
{
    Scope scope(engine);
    ScopedObject o(scope, engine->newObject());
    ScopedString s(scope);
    ScopedValue v(scope);
    for (QJsonObject::const_iterator it = object.begin(), cend = object.end(); it != cend; ++it) {
        v = fromJsonValue(engine, it.value());
        o->put((s = engine->newString(it.key())), v);
    }
    return o.asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 1053, as _ZN3QV410JsonObject13fromJsonArrayEPNS_15ExecutionEngineERK10QJsonArray
namespace QV4 {
inline QV4::ReturnedValue JsonObject::fromJsonArray(ExecutionEngine *engine, const QJsonArray &array)
{
    Scope scope(engine);
    int size = array.size();
    ScopedArrayObject a(scope, engine->newArrayObject());
    a->arrayReserve(size);
    ScopedValue v(scope);
    for (int i = 0; i < size; i++)
        a->arrayPut(i, (v = fromJsonValue(engine, array.at(i))));
    a->setArrayLengthUnchecked(size);
    return a.asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 977, as _ZN3QV410JsonObject11toJsonValueERKNS_5ValueER4QSetINS_10ObjectItemEE
namespace QV4 {
inline QJsonValue JsonObject::toJsonValue(const Value &value, V4ObjectSet &visitedObjects)
{
    if (value.isNumber())
        return QJsonValue(value.toNumber());
    else if (value.isBoolean())
        return QJsonValue((bool)value.booleanValue());
    else if (value.isNull())
        return QJsonValue(QJsonValue::Null);
    else if (value.isUndefined())
        return QJsonValue(QJsonValue::Undefined);
    else if (String *s = value.stringValue())
        return QJsonValue(s->toQString());

    Q_ASSERT(value.isObject());
    Scope scope(value.as<Object>()->engine());
    if (ScopedArrayObject a{ scope, value }) {
        return toJsonArray(a, visitedObjects);
    } else if (Scoped<QV4::Sequence> a{ scope, value }) {
        return toJsonArray(a, visitedObjects);
    } else if (Scoped<QmlListWrapper> lw{ scope, value }) {
        return toJsonArray(lw, visitedObjects);
    } else if (ScopedObject o{ scope, value }) {
        return toJsonObject(o, visitedObjects);
    }

    return QJsonValue(value.toQString());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 1018, as _ZN3QV410JsonObject12toJsonObjectEPKNS_6ObjectER4QSetINS_10ObjectItemEE
namespace QV4 {
inline QJsonObject JsonObject::toJsonObject(const Object *o, V4ObjectSet &visitedObjects)
{
    QJsonObject result;
    if (!o || o->as<FunctionObject>())
        return result;

    Scope scope(o->engine());

    if (visitedObjects.contains(ObjectItem(o))) {
        // Avoid recursion.
        // For compatibility with QVariant{List,Map} conversion, we return an
        // empty object (and no error is thrown).
        return result;
    }

    visitedObjects.insert(ObjectItem(o));

    ObjectIterator it(scope, o, ObjectIterator::EnumerableOnly);
    ScopedValue name(scope);
    QV4::ScopedValue val(scope);
    while (1) {
        name = it.nextPropertyNameAsString(val);
        if (name->isNull())
            break;

        QString key = name->toQStringNoThrow();
        if (!val->as<FunctionObject>())
            result.insert(key, toJsonValue(val, visitedObjects));
    }

    visitedObjects.remove(ObjectItem(o));

    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 1066, as _ZN3QV410JsonObject11toJsonArrayEPKNS_6ObjectER4QSetINS_10ObjectItemEE
namespace QV4 {
inline QJsonArray JsonObject::toJsonArray(const Object *a, V4ObjectSet &visitedObjects)
{
    QJsonArray result;
    if (!a)
        return result;

    Scope scope(a->engine());

    if (visitedObjects.contains(ObjectItem(a))) {
        // Avoid recursion.
        // For compatibility with QVariant{List,Map} conversion, we return an
        // empty array (and no error is thrown).
        return result;
    }

    visitedObjects.insert(ObjectItem(a));

    ScopedValue v(scope);
    quint32 length = a->getLength();
    for (quint32 i = 0; i < length; ++i) {
        v = a->get(i);
        if (v->as<FunctionObject>())
            v = Encode::null();
        result.append(toJsonValue(v, visitedObjects));
    }

    visitedObjects.remove(ObjectItem(a));

    return result;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::JsonObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410JsonObject10__dataTestEv(QV4::JsonObject *self) {
  self->__dataTest();
}

//  QV4::Heap::JsonObject *QV4::JsonObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::JsonObject *ritual_ZNK3QV410JsonObject11d_uncheckedEv(
    const QV4::JsonObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::JsonObject *QV4::JsonObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::JsonObject *ritual_ZNK3QV410JsonObject1dEv(
    const QV4::JsonObject *self) {
  return self->d();
}

//  ReturnedValue QV4::JsonObject::fromJsonValue(ExecutionEngine *engine,
//      const QJsonValue &value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410JsonObject13fromJsonValueEPNS_15ExecutionEngineERK10QJsonValue(
    QV4::ExecutionEngine *engine,
    const QJsonValue *value) {
  return QV4::JsonObject::fromJsonValue(engine, *value);
}

//  ReturnedValue QV4::JsonObject::fromJsonObject(ExecutionEngine *engine,
//      const QJsonObject &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410JsonObject14fromJsonObjectEPNS_15ExecutionEngineERK11QJsonObject(
    QV4::ExecutionEngine *engine,
    const QJsonObject *object) {
  return QV4::JsonObject::fromJsonObject(engine, *object);
}

//  ReturnedValue QV4::JsonObject::fromJsonArray(ExecutionEngine *engine,
//      const QJsonArray &array)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410JsonObject13fromJsonArrayEPNS_15ExecutionEngineERK10QJsonArray(
    QV4::ExecutionEngine *engine,
    const QJsonArray *array) {
  return QV4::JsonObject::fromJsonArray(engine, *array);
}

//  QJsonValue QV4::JsonObject::toJsonValue(const QV4::Value &value)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN3QV410JsonObject11toJsonValueERKNS_5ValueE(
    const QV4::Value *value) {
  return new QJsonValue(QV4::JsonObject::toJsonValue(*value));
}

//  QJsonObject QV4::JsonObject::toJsonObject(const QV4::Object *o)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN3QV410JsonObject12toJsonObjectEPKNS_6ObjectE(
    const QV4::Object *o) {
  return new QJsonObject(QV4::JsonObject::toJsonObject(o));
}

//  QJsonArray QV4::JsonObject::toJsonArray(const QV4::Object *o)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN3QV410JsonObject11toJsonArrayEPKNS_6ObjectE(
    const QV4::Object *o) {
  return new QJsonArray(QV4::JsonObject::toJsonArray(o));
}

//  QJsonValue QV4::JsonObject::toJsonValue(const QV4::Value &value,
//      V4ObjectSet &visitedObjects)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN3QV410JsonObject11toJsonValueERKNS_5ValueER4QSetINS_10ObjectItemEE(
    const QV4::Value *value,
    QV4::JsonObject::V4ObjectSet *visitedObjects) {
  return new QJsonValue(
      QV4::JsonObject::toJsonValue(
          *value,
          *visitedObjects));
}

//  QJsonObject QV4::JsonObject::toJsonObject(const Object *o, V4ObjectSet
//      &visitedObjects)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN3QV410JsonObject12toJsonObjectEPKNS_6ObjectER4QSetINS_10ObjectItemEE(
    const QV4::Object *o,
    QV4::JsonObject::V4ObjectSet *visitedObjects) {
  return new QJsonObject(QV4::JsonObject::toJsonObject(o, *visitedObjects));
}

//  QJsonArray QV4::JsonObject::toJsonArray(const Object *o, V4ObjectSet
//      &visitedObjects)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN3QV410JsonObject11toJsonArrayEPKNS_6ObjectER4QSetINS_10ObjectItemEE(
    const QV4::Object *o,
    QV4::JsonObject::V4ObjectSet *visitedObjects) {
  return new QJsonArray(QV4::JsonObject::toJsonArray(o, *visitedObjects));
}
