//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjslist.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 1. Kept as it is when the generator
//  runs again.
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

typedef QJSList<QQmlListProperty<QObject>, QObject *> CuteQJSListOfObject;

//  void QJSListForInIterator::init<QQmlListProperty<QObject>, QObject
//      *>(const QJSList<QQmlListProperty<QObject>, QObject *> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QJSListForInIterator4initI16QQmlListPropertyI7QObjectEPS2_EEvRK7QJSListIT_T0_E(
    QJSListForInIterator *self,
    const CuteQJSListOfObject *list) {
  self->init<QQmlListProperty<QObject>, QObject *>(*list);
}
