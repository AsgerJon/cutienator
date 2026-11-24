//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufrepeatediterator.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtProtobuf/qprotobufrepeatediterator.h>

//  QProtobufRepeatedIterator::QProtobufRepeatedIterator()
extern "C" Q_DECL_EXPORT
QProtobufRepeatedIterator *ritual_ZN25QProtobufRepeatedIteratorC1Ev() {
  return new QProtobufRepeatedIterator();
}

//  QProtobufRepeatedIterator::~QProtobufRepeatedIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufRepeatedIteratorD1Ev(
    QProtobufRepeatedIterator *self) {
  delete self;
}

//  bool QProtobufRepeatedIterator::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QProtobufRepeatedIterator7isValidEv(
    const QProtobufRepeatedIterator *self) {
  return self->isValid();
}

//  bool QProtobufRepeatedIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QProtobufRepeatedIterator7hasNextEv(
    const QProtobufRepeatedIterator *self) {
  return self->hasNext();
}

//  QProtobufMessage *QProtobufRepeatedIterator::next()
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN25QProtobufRepeatedIterator4nextEv(
    QProtobufRepeatedIterator *self) {
  return self->next();
}

//  QProtobufMessage *QProtobufRepeatedIterator::addNext()
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN25QProtobufRepeatedIterator7addNextEv(
    QProtobufRepeatedIterator *self) {
  return self->addNext();
}

//  void QProtobufRepeatedIterator::push()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufRepeatedIterator4pushEv(
    QProtobufRepeatedIterator *self) {
  self->push();
}
