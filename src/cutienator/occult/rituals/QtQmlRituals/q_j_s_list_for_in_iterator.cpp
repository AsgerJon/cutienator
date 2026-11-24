//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjslist.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjslist.h>

//  bool QJSListForInIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QJSListForInIterator7hasNextEv(
    const QJSListForInIterator *self) {
  return self->hasNext();
}

//  qsizetype QJSListForInIterator::next()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QJSListForInIterator4nextEv(
    QJSListForInIterator *self) {
  return self->next();
}

//  QJSListForInIterator::~QJSListForInIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QJSListForInIteratorD1Ev(QJSListForInIterator *self) {
  delete self;
}
