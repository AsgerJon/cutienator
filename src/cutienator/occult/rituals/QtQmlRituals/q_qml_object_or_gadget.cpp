//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlObjectOrGadget::QQmlObjectOrGadget(QObject *obj)
extern "C" Q_DECL_EXPORT
QQmlObjectOrGadget *ritual_ZN18QQmlObjectOrGadgetC1EP7QObject(QObject *obj) {
  return new QQmlObjectOrGadget(obj);
}

//  QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
QQmlObjectOrGadget *ritual_ZN18QQmlObjectOrGadgetC1EPK11QMetaObject(
    const QMetaObject *metaObject) {
  return new QQmlObjectOrGadget(metaObject);
}

//  bool QQmlObjectOrGadget::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlObjectOrGadget6isNullEv(
    const QQmlObjectOrGadget *self) {
  return self->isNull();
}

//  QObject *QQmlObjectOrGadget::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQmlObjectOrGadget7qObjectEv(
    const QQmlObjectOrGadget *self) {
  return self->qObject();
}

//  QQmlObjectOrGadget::~QQmlObjectOrGadget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlObjectOrGadgetD1Ev(QQmlObjectOrGadget *self) {
  delete self;
}
