//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuickPositionerAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickPositionerAttached10metaObjectEv(
    const QQuickPositionerAttached *self) {
  return self->metaObject();
}

//  void *QQuickPositionerAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickPositionerAttached11qt_metacastEPKc(
    QQuickPositionerAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPositionerAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickPositionerAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPositionerAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  int QQuickPositionerAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickPositionerAttached5indexEv(
    const QQuickPositionerAttached *self) {
  return self->index();
}

//  bool QQuickPositionerAttached::isFirstItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPositionerAttached11isFirstItemEv(
    const QQuickPositionerAttached *self) {
  return self->isFirstItem();
}

//  bool QQuickPositionerAttached::isLastItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPositionerAttached10isLastItemEv(
    const QQuickPositionerAttached *self) {
  return self->isLastItem();
}

//  void QQuickPositionerAttached::indexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached12indexChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "indexChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "indexChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickPositionerAttached::isFirstItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached18isFirstItemChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isFirstItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isFirstItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickPositionerAttached::isLastItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached17isLastItemChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isLastItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isLastItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)
