//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4identifiertable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4identifiertable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::IdentifierTable::addEntry(Heap::StringOrSymbol *str)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable8addEntryEPNS_4Heap14StringOrSymbolE(
    QV4::IdentifierTable *self,
    QV4::Heap::StringOrSymbol *str) {
  self->addEntry(str);
}

//  QV4::IdentifierTable::IdentifierTable(ExecutionEngine *engine, int
//      numBits)
extern "C" Q_DECL_EXPORT
QV4::IdentifierTable *ritual_ZN3QV415IdentifierTableC1EPNS_15ExecutionEngineEi(
    QV4::ExecutionEngine *engine,
    int numBits) {
  return new QV4::IdentifierTable(engine, numBits);
}

//  QV4::IdentifierTable::~IdentifierTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTableD1Ev(QV4::IdentifierTable *self) {
  delete self;
}

//  Heap::String *QV4::IdentifierTable::insertString(const QString &s)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV415IdentifierTable12insertStringERK7QString(
    QV4::IdentifierTable *self,
    const QString *s) {
  return self->insertString(*s);
}

//  Heap::Symbol *QV4::IdentifierTable::insertSymbol(const QString &s)
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZN3QV415IdentifierTable12insertSymbolERK7QString(
    QV4::IdentifierTable *self,
    const QString *s) {
  return self->insertSymbol(*s);
}

//  PropertyKey QV4::IdentifierTable::asPropertyKey(const Heap::String *str)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_4Heap6StringE(
    QV4::IdentifierTable *self,
    const QV4::Heap::String *str) {
  return new QV4::PropertyKey(self->asPropertyKey(str));
}

//  PropertyKey QV4::IdentifierTable::asPropertyKey(const QV4::String *str)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_6StringE(
    QV4::IdentifierTable *self,
    const QV4::String *str) {
  return new QV4::PropertyKey(self->asPropertyKey(str));
}

//  PropertyKey QV4::IdentifierTable::asPropertyKey(const QString &s,
//      KeyConversionBehavior conversionBehavior)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable13asPropertyKeyERK7QStringNS0_21KeyConversionBehaviorE(
    QV4::IdentifierTable *self,
    const QString *s,
    QV4::IdentifierTable::KeyConversionBehavior conversionBehavior) {
  return new QV4::PropertyKey(self->asPropertyKey(*s, conversionBehavior));
}

//  PropertyKey QV4::IdentifierTable::asPropertyKeyImpl(const Heap::String
//      *str)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable17asPropertyKeyImplEPKNS_4Heap6StringE(
    QV4::IdentifierTable *self,
    const QV4::Heap::String *str) {
  return new QV4::PropertyKey(self->asPropertyKeyImpl(str));
}

//  Heap::StringOrSymbol *QV4::IdentifierTable::resolveId(PropertyKey i)
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringOrSymbol *ritual_ZNK3QV415IdentifierTable9resolveIdENS_11PropertyKeyE(
    const QV4::IdentifierTable *self,
    const QV4::PropertyKey *i) {
  return self->resolveId(*i);
}

//  Heap::String *QV4::IdentifierTable::stringForId(PropertyKey i) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV415IdentifierTable11stringForIdENS_11PropertyKeyE(
    const QV4::IdentifierTable *self,
    const QV4::PropertyKey *i) {
  return self->stringForId(*i);
}

//  Heap::Symbol *QV4::IdentifierTable::symbolForId(PropertyKey i) const
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZNK3QV415IdentifierTable11symbolForIdENS_11PropertyKeyE(
    const QV4::IdentifierTable *self,
    const QV4::PropertyKey *i) {
  return self->symbolForId(*i);
}

//  void QV4::IdentifierTable::markObjects(MarkStack *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV415IdentifierTable11markObjectsEPNS_9MarkStackE(
    const QV4::IdentifierTable *self,
    QV4::MarkStack *markStack) {
  self->markObjects(markStack);
}

//  void QV4::IdentifierTable::sweep()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable5sweepEv(QV4::IdentifierTable *self) {
  self->sweep();
}

//  void QV4::IdentifierTable::addIdentifierHash(IdentifierHashData *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable17addIdentifierHashEPNS_18IdentifierHashDataE(
    QV4::IdentifierTable *self,
    QV4::IdentifierHashData *h) {
  self->addIdentifierHash(h);
}

//  void QV4::IdentifierTable::removeIdentifierHash(IdentifierHashData *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable20removeIdentifierHashEPNS_18IdentifierHashDataE(
    QV4::IdentifierTable *self,
    QV4::IdentifierHashData *h) {
  self->removeIdentifierHash(h);
}

//  Heap::String *QV4::IdentifierTable::resolveStringEntry(const QString &s,
//      uint hash, uint subtype)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV415IdentifierTable18resolveStringEntryERK7QStringjj(
    QV4::IdentifierTable *self,
    const QString *s,
    uint hash,
    uint subtype) {
  return self->resolveStringEntry(*s, hash, subtype);
}
