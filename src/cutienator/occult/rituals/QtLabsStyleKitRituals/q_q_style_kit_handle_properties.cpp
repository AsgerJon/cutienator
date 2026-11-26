//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQStyleKitHandleProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQStyleKitHandleProperties10metaObjectEv(
    const QQStyleKitHandleProperties *self) {
  return self->metaObject();
}

//  void *QQStyleKitHandleProperties::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQStyleKitHandleProperties11qt_metacastEPKc(
    QQStyleKitHandleProperties *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitHandleProperties::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQStyleKitHandleProperties11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitHandleProperties *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitHandleProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitHandleProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitHandleProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQStyleKitHandleProperties::firstChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitHandleProperties12firstChangedEv(
    QQStyleKitHandleProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitHandleProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "firstChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "firstChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitHandleProperties::secondChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitHandleProperties13secondChangedEv(
    QQStyleKitHandleProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitHandleProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "secondChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "secondChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
