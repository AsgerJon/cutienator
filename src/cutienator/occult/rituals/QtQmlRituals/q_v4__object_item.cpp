//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ObjectItem::ObjectItem(const QV4::Object *o)
extern "C" Q_DECL_EXPORT
QV4::ObjectItem *ritual_ZN3QV410ObjectItemC1EPKNS_6ObjectE(
    const QV4::Object *o) {
  return new QV4::ObjectItem(o);
}

//  QV4::ObjectItem::~ObjectItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410ObjectItemD1Ev(QV4::ObjectItem *self) {
  delete self;
}
