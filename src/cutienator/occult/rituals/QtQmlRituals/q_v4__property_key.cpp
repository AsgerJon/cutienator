//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4propertykey_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qv4propertykey_p.h"
#include <QtCore/qstring.h>
#include <qv4string_p.h>
#include <qv4engine_p.h>
#include <qv4scopedvalue_p.h>
#include <private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4propertykey.cpp, line 32, as _ZNK3QV411PropertyKey29isCanonicalNumericIndexStringEv
inline bool QV4::PropertyKey::isCanonicalNumericIndexString() const
{
    if (isArrayIndex())
        return true;
    if (isSymbol())
        return false;
    Heap::String *s = static_cast<Heap::String *>(asStringOrSymbol());
    Scope scope(s->internalClass->engine);
    ScopedString str(scope, s);
    double d = str->toNumber();
    if (d == 0. && std::signbit(d))
        return true;
    ScopedString converted(scope, Value::fromDouble(d).toString(scope.engine));
    if (converted->equals(str))
        return true;
    return false;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4propertykey.cpp, line 15, as _ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngineE
inline QV4::Heap::StringOrSymbol *QV4::PropertyKey::toStringOrSymbol(QV4::ExecutionEngine *e)
{
    if (isArrayIndex())
        return Value::fromUInt32(asArrayIndex()).toString(e);
    return asStringOrSymbol();
}
//  -----------------------------------------------------------------------

//  bool QV4::PropertyKey::isManaged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey9isManagedEv(const QV4::PropertyKey *self) {
  return self->isManaged();
}

//  quint32 QV4::PropertyKey::value() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV411PropertyKey5valueEv(const QV4::PropertyKey *self) {
  return self->value();
}

//  PropertyKey QV4::PropertyKey::invalid()
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV411PropertyKey7invalidEv() {
  return new QV4::PropertyKey(QV4::PropertyKey::invalid());
}

//  PropertyKey QV4::PropertyKey::fromArrayIndex(uint idx)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV411PropertyKey14fromArrayIndexEj(uint idx) {
  return new QV4::PropertyKey(QV4::PropertyKey::fromArrayIndex(idx));
}

//  bool QV4::PropertyKey::isStringOrSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey16isStringOrSymbolEv(
    const QV4::PropertyKey *self) {
  return self->isStringOrSymbol();
}

//  uint QV4::PropertyKey::asArrayIndex() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV411PropertyKey12asArrayIndexEv(
    const QV4::PropertyKey *self) {
  return self->asArrayIndex();
}

//  bool QV4::PropertyKey::isArrayIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey12isArrayIndexEv(
    const QV4::PropertyKey *self) {
  return self->isArrayIndex();
}

//  bool QV4::PropertyKey::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey7isValidEv(const QV4::PropertyKey *self) {
  return self->isValid();
}

//  bool QV4::PropertyKey::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey8isStringEv(const QV4::PropertyKey *self) {
  return self->isString();
}

//  bool QV4::PropertyKey::isSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey8isSymbolEv(const QV4::PropertyKey *self) {
  return self->isSymbol();
}

//  bool QV4::PropertyKey::isCanonicalNumericIndexString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKey29isCanonicalNumericIndexStringEv(
    const QV4::PropertyKey *self) {
  return self->isCanonicalNumericIndexString();
}

//  QString QV4::PropertyKey::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV411PropertyKey9toQStringEv(
    const QV4::PropertyKey *self) {
  return new QString(self->toQString());
}

//  Heap::StringOrSymbol *QV4::PropertyKey::toStringOrSymbol(ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::StringOrSymbol *ritual_ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngineE(
    QV4::PropertyKey *self,
    QV4::ExecutionEngine *e) {
  return self->toStringOrSymbol(e);
}

//  quint64 QV4::PropertyKey::id() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK3QV411PropertyKey2idEv(const QV4::PropertyKey *self) {
  return self->id();
}

//  PropertyKey QV4::PropertyKey::fromId(quint64 id)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV411PropertyKey6fromIdEy(quint64 id) {
  return new QV4::PropertyKey(QV4::PropertyKey::fromId(id));
}

//  bool QV4::PropertyKey::operator==(const PropertyKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKeyeqERKS0_(
    const QV4::PropertyKey *self,
    const QV4::PropertyKey *other) {
  return self->operator==(*other);
}

//  bool QV4::PropertyKey::operator!=(const PropertyKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKeyneERKS0_(
    const QV4::PropertyKey *self,
    const QV4::PropertyKey *other) {
  return self->operator!=(*other);
}

//  bool QV4::PropertyKey::operator<(const PropertyKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411PropertyKeyltERKS0_(
    const QV4::PropertyKey *self,
    const QV4::PropertyKey *other) {
  return self->operator<(*other);
}

//  QV4::PropertyKey::~PropertyKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411PropertyKeyD1Ev(QV4::PropertyKey *self) {
  delete self;
}
