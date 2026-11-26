//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuick3DPropertyWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DPropertyWatcher10metaObjectEv(
    const QQuick3DPropertyWatcher *self) {
  return self->metaObject();
}

//  void *QQuick3DPropertyWatcher::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DPropertyWatcher11qt_metacastEPKc(
    QQuick3DPropertyWatcher *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DPropertyWatcher::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DPropertyWatcher11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DPropertyWatcher *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuick3DPropertyWatcher::onValuePropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher22onValuePropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DPropertyWatcher")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onValuePropertyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onValuePropertyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DPropertyWatcher::onPointerPropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher24onPointerPropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DPropertyWatcher")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onPointerPropertyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onPointerPropertyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
