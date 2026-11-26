//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjslist.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 2. Kept as it is when the generator
//  runs again.
#include <QtQml/QtQml>
#include <QtQml/qjslist.h>

//  void QJSListForOfIterator::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QJSListForOfIterator4initEv(QJSListForOfIterator *self) {
  self->init();
}

//  QJSListForOfIterator::~QJSListForOfIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QJSListForOfIteratorD1Ev(QJSListForOfIterator *self) {
  delete self;
}

typedef QJSList<QQmlListProperty<QObject>, QObject *> CuteQJSListOfObject;

//  bool QJSListForOfIterator::hasNext<QQmlListProperty<QObject>, QObject
//      *>(const QJSList<QQmlListProperty<QObject>, QObject *> &list) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QJSListForOfIterator7hasNextI16QQmlListPropertyI7QObjectEPS2_EEbRK7QJSListIT_T0_E(
    const QJSListForOfIterator *self,
    const CuteQJSListOfObject *list) {
  return self->hasNext<QQmlListProperty<QObject>, QObject *>(*list);
}

//  QObject *QJSListForOfIterator::next<QQmlListProperty<QObject>, QObject
//      *>(const QJSList<QQmlListProperty<QObject>, QObject *> &list)
extern "C" Q_DECL_EXPORT
QObject * ritual_ZN20QJSListForOfIterator4nextI16QQmlListPropertyI7QObjectEPS2_EET0_RK7QJSListIT_S5_E(
    QJSListForOfIterator *self,
    const CuteQJSListOfObject *list) {
  return self->next<QQmlListProperty<QObject>, QObject *>(*list);
}
