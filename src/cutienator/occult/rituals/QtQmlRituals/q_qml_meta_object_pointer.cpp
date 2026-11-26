//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlMetaObjectPointer::QQmlMetaObjectPointer()
extern "C" Q_DECL_EXPORT
QQmlMetaObjectPointer *ritual_ZN21QQmlMetaObjectPointerC1Ev() {
  return new QQmlMetaObjectPointer();
}

//  QQmlMetaObjectPointer::QQmlMetaObjectPointer(const QMetaObject
//      *staticMetaObject)
extern "C" Q_DECL_EXPORT
QQmlMetaObjectPointer *ritual_ZN21QQmlMetaObjectPointerC1EPK11QMetaObject(
    const QMetaObject *staticMetaObject) {
  return new QQmlMetaObjectPointer(staticMetaObject);
}

//  QQmlMetaObjectPointer::~QQmlMetaObjectPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlMetaObjectPointerD1Ev(QQmlMetaObjectPointer *self) {
  delete self;
}

//  QQmlMetaObjectPointer::QQmlMetaObjectPointer(const QQmlMetaObjectPointer
//      &other)
extern "C" Q_DECL_EXPORT
QQmlMetaObjectPointer *ritual_ZN21QQmlMetaObjectPointerC1ERKS_(
    const QQmlMetaObjectPointer *other) {
  return new QQmlMetaObjectPointer(*other);
}

//  void QQmlMetaObjectPointer::setSharedOnce(QMetaObject *shared) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQmlMetaObjectPointer13setSharedOnceEP11QMetaObject(
    const QQmlMetaObjectPointer *self,
    QMetaObject *shared) {
  self->setSharedOnce(shared);
}

//  const QMetaObject *QQmlMetaObjectPointer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlMetaObjectPointer10metaObjectEv(
    const QQmlMetaObjectPointer *self) {
  return self->metaObject();
}

//  bool QQmlMetaObjectPointer::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlMetaObjectPointer8isSharedEv(
    const QQmlMetaObjectPointer *self) {
  return self->isShared();
}

//  bool QQmlMetaObjectPointer::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlMetaObjectPointer6isNullEv(
    const QQmlMetaObjectPointer *self) {
  return self->isNull();
}
