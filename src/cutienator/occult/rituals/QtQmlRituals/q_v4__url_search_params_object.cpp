//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4urlobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <QtCore/QStringList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtCore/QUrl>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 715, as _ZN3QV421UrlSearchParamsObject16initializeParamsEv
namespace QV4 {
inline void UrlSearchParamsObject::initializeParams()
{
    auto *arrayObject = engine()->newArrayObject(0);
    auto *keys = engine()->newArrayObject(0);
    auto *values = engine()->newArrayObject(0);

    d()->params.set(engine(), arrayObject);
    d()->keys.set(engine(), keys);
    d()->values.set(engine(), values);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 726, as _ZN3QV421UrlSearchParamsObject16initializeParamsE7QString
namespace QV4 {
inline void UrlSearchParamsObject::initializeParams(QString value)
{
    Q_ASSERT(d()->params == nullptr);

    initializeParams();

    if (value.startsWith(QLatin1Char('?')))
        value = value.mid(1);

    const QStringList params = value.split(QLatin1Char('&'));

    for (const QString& param : params) {
        if (param.isEmpty())
            continue;

        QString key, value;

        int equalsIndex = param.indexOf(QLatin1Char('='));
        if (equalsIndex != -1) {
            key = param.left(equalsIndex);
            value = param.mid(equalsIndex+1);
        } else {
            key = param;
        }

        append(engine()->newString(key), engine()->newString(value));
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 755, as _ZN3QV421UrlSearchParamsObject16initializeParamsERNS_6ScopedINS_11ArrayObjectEEE
namespace QV4 {
inline void UrlSearchParamsObject::initializeParams(ScopedArrayObject& params)
{
    Q_ASSERT(d()->params == nullptr);

    Scope scope(engine());

    uint len = params->getLength();
    auto *keys = engine()->newArrayObject(len);
    auto *values = engine()->newArrayObject(len);

    ScopedArrayObject scopedKeys(scope, keys);
    ScopedArrayObject scopedValues(scope, values);

    for (uint i = 0; i < len; i++)
    {
        // fromReturnedValue is safe; everything is reachable via params
        // so the gc won't collect it; we control params, so there can't be
        // any weird proxy magic
        QV4::Value pair = Value::fromReturnedValue(params->get(i));
        auto *pairArrayObject = pair.as<ArrayObject>();

        QV4::Value key = Value::fromReturnedValue(pairArrayObject->get(uint(0)));
        QV4::Value value = Value::fromReturnedValue(pairArrayObject->get(uint(1)));

        scopedKeys->put(i, key);
        scopedValues->put(i, value);
    }


    d()->params.set(engine(), params->d());
    d()->keys.set(engine(), keys);
    d()->values.set(engine(), values);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 789, as _ZN3QV421UrlSearchParamsObject16initializeParamsERNS_6ScopedINS_6ObjectEEE
namespace QV4 {
inline void UrlSearchParamsObject::initializeParams(ScopedObject& params)
{
    Q_ASSERT(d()->params == nullptr);

    initializeParams();

    Scope scope(engine());
    ObjectIterator it(scope, params, ObjectIterator::EnumerableOnly);

    ScopedValue name(scope);
    ScopedValue val(scope);

    while (true) {
        name = it.nextPropertyNameAsString(val);
        if (name->isNull())
            break;

        Heap::String *nameStr = name->as<String>()->d();
        Heap::String *valStr = val->toString(engine());

        append(nameStr, valStr);
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 881, as _ZNK3QV421UrlSearchParamsObject6paramsEv
namespace QV4 {
inline QList<QStringList> UrlSearchParamsObject::params() const
{
    auto *arrayObject = d()->params.get();
    Scope scope(engine());
    ScopedArrayObject scopedArray(scope, arrayObject);

    QList<QStringList> result;

    uint len = scopedArray->getLength();

    for (uint i = 0; i < len; i++) {
        QV4::Value pair = Value::fromReturnedValue(scopedArray->get(i));
        auto *pairArrayObject = pair.as<ArrayObject>();

        QV4::Value key = Value::fromReturnedValue(pairArrayObject->get(uint(0)));
        QV4::Value value = Value::fromReturnedValue(pairArrayObject->get(uint(1)));

        result << QStringList { key.toQString(), value.toQString() };
    }

    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 813, as _ZN3QV421UrlSearchParamsObject9setParamsERK5QListIS1_I7QStringEE
namespace QV4 {
inline void UrlSearchParamsObject::setParams(const QList<QStringList> &params)
{
    auto *arrayObject = engine()->newArrayObject(0);
    auto *keys = engine()->newArrayObject(0);
    auto *values = engine()->newArrayObject(0);

    Scope scope(engine());

    ScopedArrayObject scopedArray(scope, arrayObject);

    ScopedArrayObject scopedKeys(scope, keys);
    ScopedArrayObject scopedValues(scope, values);

    uint len = 0;

    for (const QStringList& param : params) {

        auto *valuePair = engine()->newArrayObject(2);

        ScopedArrayObject valuePairObject(scope, valuePair);

        ScopedValue key(scope, Value::fromHeapObject(engine()->newString(param[0])));
        ScopedValue value(scope, Value::fromHeapObject(engine()->newString(param[1])));
        valuePairObject->put(uint(0), key);
        valuePairObject->put(uint(1), value);

        scopedKeys->put(len, key);
        scopedValues->put(len, value);

        scopedArray->put(len, valuePairObject);
        len++;
    }

    d()->params.set(engine(), arrayObject);
    d()->keys.set(engine(), keys);
    d()->values.set(engine(), values);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 904, as _ZNK3QV421UrlSearchParamsObject9urlObjectEv
namespace QV4 {
inline Heap::UrlObject *UrlSearchParamsObject::urlObject() const
{
    return d()->url.get();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 851, as _ZN3QV421UrlSearchParamsObject12setUrlObjectEPKNS_9UrlObjectE
namespace QV4 {
inline void UrlSearchParamsObject::setUrlObject(const UrlObject *url)
{
    d()->url.set(engine(), url->d());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 909, as _ZNK3QV421UrlSearchParamsObject12searchStringEv
namespace QV4 {
inline QString UrlSearchParamsObject::searchString() const
{
    QString search = QLatin1String("");
    auto params = this->params();
    auto len = params.size();
    for (int i = 0; i < len; ++i) {
        const QStringList &param = params[i];
        search += param[0] + QLatin1Char('=') + param[1];
        if (i != len - 1)
            search += QLatin1Char('&');
    }
    return search;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 988, as _ZNK3QV421UrlSearchParamsObject6nameAtEi
namespace QV4 {
inline QString UrlSearchParamsObject::nameAt(int index) const
{
    return stringAt(index, 0);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 993, as _ZNK3QV421UrlSearchParamsObject9nameAtRawEi
namespace QV4 {
inline QV4::Heap::String * UrlSearchParamsObject::nameAtRaw(int index) const
{
    return stringAtRaw(index, 0);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 999, as _ZNK3QV421UrlSearchParamsObject7valueAtEi
namespace QV4 {
inline QString UrlSearchParamsObject::valueAt(int index) const
{
    return stringAt(index, 1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 1004, as _ZNK3QV421UrlSearchParamsObject10valueAtRawEi
namespace QV4 {
inline QV4::Heap::String * UrlSearchParamsObject::valueAtRaw(int index) const
{
    return stringAtRaw(index, 1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 856, as _ZN3QV421UrlSearchParamsObject6appendEPNS_4Heap6StringES3_
namespace QV4 {
inline void UrlSearchParamsObject::append(Heap::String *name, Heap::String *value)
{
    Scope scope(engine());

    ScopedArrayObject scopedArray(scope, d()->params);
    ScopedArrayObject scopedKeys(scope, d()->keys);
    ScopedArrayObject scopedValues(scope, d()->values);

    auto *valuePair = engine()->newArrayObject(2);

    ScopedArrayObject valuePairObject(scope, valuePair);

    ScopedValue keyScoped(scope, Value::fromHeapObject(name));
    ScopedValue valueScoped(scope, Value::fromHeapObject(value));
    valuePairObject->put(uint(0), keyScoped);
    valuePairObject->put(uint(1), valueScoped);

    uint len = scopedArray->getLength();

    scopedKeys->put(len, keyScoped);
    scopedValues->put(len, valueScoped);

    scopedArray->put(len, valuePairObject);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 932, as _ZNK3QV421UrlSearchParamsObject7indexOfE7QStringi
namespace QV4 {
inline int UrlSearchParamsObject::indexOf(QString name, int last) const
{
    auto *arrayObject = d()->params.get();
    Scope scope(engine());
    ScopedArrayObject scopedArray(scope, arrayObject);

    int len = scopedArray->getLength();

    for (int i = last + 1; i < len; i++) {
        // fromReturnedValue is safe, scopedArray is a normal array and takes care of marking
        QV4::Value pair = Value::fromReturnedValue(scopedArray->get(i));
        auto *pairArrayObject = pair.as<ArrayObject>();

        QV4::Value key = Value::fromReturnedValue(pairArrayObject->get(uint(0)));

        if (key.toQString() == name)
            return i;
    }

    return -1;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 923, as _ZNK3QV421UrlSearchParamsObject6lengthEv
namespace QV4 {
inline int UrlSearchParamsObject::length() const
{
    auto *arrayObject = d()->params.get();
    Scope scope(engine());
    ScopedArrayObject scopedArray(scope, arrayObject);

    return scopedArray->getLength();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 1046, as _ZN3QV421UrlSearchParamsObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE
namespace QV4 {
inline PropertyAttributes UrlSearchParamsObject::virtualGetOwnProperty(const Managed *m, PropertyKey id,
                                                                Property *p)
{
    PropertyAttributes attributes = Object::virtualGetOwnProperty(m, id, p);
    if (attributes != Attr_Invalid)
        return attributes;

    if (id.isArrayIndex()) {
        const int index = id.asArrayIndex();
        const auto usp = static_cast<const UrlSearchParamsObject *>(m);
        if (index < usp->length()) {
            if (p)
                p->value = usp->engine()->newString(usp->nameAt(index));
            return Attr_NotConfigurable | Attr_NotWritable;
        }
    }

    return Object::virtualGetOwnProperty(m, id, p);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 954, as _ZNK3QV421UrlSearchParamsObject8stringAtEii
namespace QV4 {
inline QString UrlSearchParamsObject::stringAt(int index, int pairIndex) const
{
    auto *arrayObject = d()->params.get();
    Scope scope(engine());
    ScopedArrayObject scopedArray(scope, arrayObject);

    if (index >= scopedArray->getLength())
        return {};

    QV4::Value pair = Value::fromReturnedValue(scopedArray->get(index));
    auto *pairArrayObject = pair.as<ArrayObject>();

    QV4::Value value = Value::fromReturnedValue(pairArrayObject->get(pairIndex));

    return value.toQString();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 971, as _ZNK3QV421UrlSearchParamsObject11stringAtRawEii
namespace QV4 {
inline QV4::Heap::String * UrlSearchParamsObject::stringAtRaw(int index, int pairIndex) const
{
    auto *arrayObject = d()->params.get();
    Scope scope(engine());
    ScopedArrayObject scopedArray(scope, arrayObject);

    if (index >= scopedArray->getLength())
        return nullptr;

    QV4::Value pair = Value::fromReturnedValue(scopedArray->get(index));
    auto *pairArrayObject = pair.as<ArrayObject>();

    QV4::Value value = Value::fromReturnedValue(pairArrayObject->get(pairIndex));

    return value.as<String>()->d();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::UrlSearchParamsObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject10__dataTestEv(
    QV4::UrlSearchParamsObject *self) {
  self->__dataTest();
}

//  QV4::Heap::UrlSearchParamsObject
//      *QV4::UrlSearchParamsObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlSearchParamsObject *ritual_ZNK3QV421UrlSearchParamsObject11d_uncheckedEv(
    const QV4::UrlSearchParamsObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::UrlSearchParamsObject *QV4::UrlSearchParamsObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlSearchParamsObject *ritual_ZNK3QV421UrlSearchParamsObject1dEv(
    const QV4::UrlSearchParamsObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::UrlSearchParamsObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV421UrlSearchParamsObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::UrlSearchParamsObject::defaultPrototype(e);
}

//  void QV4::UrlSearchParamsObject::initializeParams()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject16initializeParamsEv(
    QV4::UrlSearchParamsObject *self) {
  self->initializeParams();
}

//  void QV4::UrlSearchParamsObject::initializeParams(QString params)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject16initializeParamsE7QString(
    QV4::UrlSearchParamsObject *self,
    const QString *params) {
  self->initializeParams(*params);
}

//  void QV4::UrlSearchParamsObject::initializeParams(ScopedArrayObject
//      &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject16initializeParamsERNS_6ScopedINS_11ArrayObjectEEE(
    QV4::UrlSearchParamsObject *self,
    QV4::ScopedArrayObject *params) {
  self->initializeParams(*params);
}

//  void QV4::UrlSearchParamsObject::initializeParams(ScopedObject &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject16initializeParamsERNS_6ScopedINS_6ObjectEEE(
    QV4::UrlSearchParamsObject *self,
    QV4::ScopedObject *params) {
  self->initializeParams(*params);
}

//  QList<QStringList> QV4::UrlSearchParamsObject::params() const
extern "C" Q_DECL_EXPORT
QList<QStringList> *ritual_ZNK3QV421UrlSearchParamsObject6paramsEv(
    const QV4::UrlSearchParamsObject *self) {
  return new QList<QStringList>(self->params());
}

//  void QV4::UrlSearchParamsObject::setParams(const QList<QStringList>
//      &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject9setParamsERK5QListIS1_I7QStringEE(
    QV4::UrlSearchParamsObject *self,
    const QList<QStringList> *params) {
  self->setParams(*params);
}

//  Heap::UrlObject *QV4::UrlSearchParamsObject::urlObject() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZNK3QV421UrlSearchParamsObject9urlObjectEv(
    const QV4::UrlSearchParamsObject *self) {
  return self->urlObject();
}

//  void QV4::UrlSearchParamsObject::setUrlObject(const UrlObject *url)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject12setUrlObjectEPKNS_9UrlObjectE(
    QV4::UrlSearchParamsObject *self,
    const QV4::UrlObject *url) {
  self->setUrlObject(url);
}

//  QString QV4::UrlSearchParamsObject::searchString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV421UrlSearchParamsObject12searchStringEv(
    const QV4::UrlSearchParamsObject *self) {
  return new QString(self->searchString());
}

//  QString QV4::UrlSearchParamsObject::nameAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV421UrlSearchParamsObject6nameAtEi(
    const QV4::UrlSearchParamsObject *self,
    int index) {
  return new QString(self->nameAt(index));
}

//  Heap::String *QV4::UrlSearchParamsObject::nameAtRaw(int index) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV421UrlSearchParamsObject9nameAtRawEi(
    const QV4::UrlSearchParamsObject *self,
    int index) {
  return self->nameAtRaw(index);
}

//  QString QV4::UrlSearchParamsObject::valueAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV421UrlSearchParamsObject7valueAtEi(
    const QV4::UrlSearchParamsObject *self,
    int index) {
  return new QString(self->valueAt(index));
}

//  Heap::String *QV4::UrlSearchParamsObject::valueAtRaw(int index) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV421UrlSearchParamsObject10valueAtRawEi(
    const QV4::UrlSearchParamsObject *self,
    int index) {
  return self->valueAtRaw(index);
}

//  void QV4::UrlSearchParamsObject::append(Heap::String *name, Heap::String
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421UrlSearchParamsObject6appendEPNS_4Heap6StringES3_(
    QV4::UrlSearchParamsObject *self,
    QV4::Heap::String *name,
    QV4::Heap::String *value) {
  self->append(name, value);
}

//  int QV4::UrlSearchParamsObject::indexOf(QString name, int last) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV421UrlSearchParamsObject7indexOfE7QStringi(
    const QV4::UrlSearchParamsObject *self,
    const QString *name,
    int last) {
  return self->indexOf(*name, last);
}

//  int QV4::UrlSearchParamsObject::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV421UrlSearchParamsObject6lengthEv(
    const QV4::UrlSearchParamsObject *self) {
  return self->length();
}

//  PropertyAttributes
//      QV4::UrlSearchParamsObject::virtualGetOwnProperty(const Managed *m,
//      PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV421UrlSearchParamsObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::UrlSearchParamsObject::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  QString QV4::UrlSearchParamsObject::stringAt(int index, int pairIndex)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV421UrlSearchParamsObject8stringAtEii(
    const QV4::UrlSearchParamsObject *self,
    int index,
    int pairIndex) {
  return new QString(self->stringAt(index, pairIndex));
}

//  Heap::String *QV4::UrlSearchParamsObject::stringAtRaw(int index, int
//      pairIndex) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV421UrlSearchParamsObject11stringAtRawEii(
    const QV4::UrlSearchParamsObject *self,
    int index,
    int pairIndex) {
  return self->stringAtRaw(index, pairIndex);
}

//  a QList<QStringList> a ritual of QV4::UrlSearchParamsObject gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_UrlSearchParamsObject__QList_QStringList(
    QList<QStringList> *self) {
  delete self;
}
