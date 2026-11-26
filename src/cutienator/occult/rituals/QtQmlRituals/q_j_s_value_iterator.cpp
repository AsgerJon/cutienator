//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsvalueiterator.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjsvalueiterator.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qstring.h>

//  QJSValueIterator::QJSValueIterator(const QJSValue &value)
extern "C" Q_DECL_EXPORT
QJSValueIterator *ritual_ZN16QJSValueIteratorC1ERK8QJSValue(
    const QJSValue *value) {
  return new QJSValueIterator(*value);
}

//  QJSValueIterator::~QJSValueIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QJSValueIteratorD1Ev(QJSValueIterator *self) {
  delete self;
}

//  bool QJSValueIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QJSValueIterator7hasNextEv(const QJSValueIterator *self) {
  return self->hasNext();
}

//  bool QJSValueIterator::next()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QJSValueIterator4nextEv(QJSValueIterator *self) {
  return self->next();
}

//  QString QJSValueIterator::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QJSValueIterator4nameEv(const QJSValueIterator *self) {
  return new QString(self->name());
}

//  QJSValue QJSValueIterator::value() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK16QJSValueIterator5valueEv(
    const QJSValueIterator *self) {
  return new QJSValue(self->value());
}

//  QJSValueIterator &QJSValueIterator::operator=(QJSValue &value)
extern "C" Q_DECL_EXPORT
QJSValueIterator *ritual_ZN16QJSValueIteratoraSER8QJSValue(
    QJSValueIterator *self,
    QJSValue *value) {
  return &(self->operator=(*value));
}

//  QJSValueIteratorPrivate *QJSValueIterator::d_func()
extern "C" Q_DECL_EXPORT
QJSValueIteratorPrivate *ritual_ZN16QJSValueIterator6d_funcEv(
    QJSValueIterator *self) {
  return self->d_func();
}

//  const QJSValueIteratorPrivate *QJSValueIterator::d_func() const
extern "C" Q_DECL_EXPORT
const QJSValueIteratorPrivate *ritual_ZNK16QJSValueIterator6d_funcEv(
    const QJSValueIterator *self) {
  return self->d_func();
}
