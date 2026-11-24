//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4property_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4property_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::PropertyIndex::set(EngineBase *e, Value newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413PropertyIndex3setEPNS_10EngineBaseENS_5ValueE(
    QV4::PropertyIndex *self,
    QV4::EngineBase *e,
    const QV4::Value *newVal) {
  self->set(e, *newVal);
}

//  const Value *QV4::PropertyIndex::operator->() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV413PropertyIndexptEv(
    const QV4::PropertyIndex *self) {
  return self->operator->();
}

//  const Value &QV4::PropertyIndex::operator*() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV413PropertyIndexdeEv(
    const QV4::PropertyIndex *self) {
  return new QV4::Value(self->operator*());
}

//  bool QV4::PropertyIndex::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV413PropertyIndex6isNullEv(const QV4::PropertyIndex *self) {
  return self->isNull();
}

//  QV4::PropertyIndex::~PropertyIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413PropertyIndexD1Ev(QV4::PropertyIndex *self) {
  delete self;
}
