//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQStyleKitIndicatorProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQStyleKitIndicatorProperties10metaObjectEv(
    const QQStyleKitIndicatorProperties *self) {
  return self->metaObject();
}

//  void *QQStyleKitIndicatorProperties::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQStyleKitIndicatorProperties11qt_metacastEPKc(
    QQStyleKitIndicatorProperties *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitIndicatorProperties::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQStyleKitIndicatorProperties11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitIndicatorProperties *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitIndicatorProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQStyleKitIndicatorProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitIndicatorProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQStyleKitIndicatorProperties::foregroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQStyleKitIndicatorProperties17foregroundChangedEv(
    QQStyleKitIndicatorProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitIndicatorProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "foregroundChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "foregroundChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
