//  Written by dev_tooling.RitualGenerator from the records of QtQml/qqml.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqml.h>

//  const QMetaObject *QQmlTypeNotAvailable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlTypeNotAvailable10metaObjectEv(
    const QQmlTypeNotAvailable *self) {
  return self->metaObject();
}

//  void *QQmlTypeNotAvailable::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQmlTypeNotAvailable11qt_metacastEPKc(
    QQmlTypeNotAvailable *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTypeNotAvailable::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQmlTypeNotAvailable11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTypeNotAvailable *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQmlTypeNotAvailable::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeNotAvailable24qt_qmlMarker_uncreatableEv(
    QQmlTypeNotAvailable *self) {
  self->qt_qmlMarker_uncreatable();
}
