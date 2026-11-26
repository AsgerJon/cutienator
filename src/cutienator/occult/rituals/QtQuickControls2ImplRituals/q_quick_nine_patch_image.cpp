//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickninepatchimage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickninepatchimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuickNinePatchImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickNinePatchImage10metaObjectEv(
    const QQuickNinePatchImage *self) {
  return self->metaObject();
}

//  void *QQuickNinePatchImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickNinePatchImage11qt_metacastEPKc(
    QQuickNinePatchImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickNinePatchImage::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickNinePatchImage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickNinePatchImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickNinePatchImage::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage17topPaddingChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "topPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "topPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage18leftPaddingChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "leftPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "leftPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage19rightPaddingChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rightPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rightPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage20bottomPaddingChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "bottomPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "bottomPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::topInsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage15topInsetChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "topInsetChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "topInsetChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::leftInsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage16leftInsetChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "leftInsetChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "leftInsetChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::rightInsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage17rightInsetChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rightInsetChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rightInsetChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::bottomInsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage18bottomInsetChangedEv(
    QQuickNinePatchImage *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickNinePatchImage")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "bottomInsetChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "bottomInsetChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickNinePatchImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickNinePatchImage12pixmapChangeEv(
    QQuickNinePatchImage *self) {
  self->pixmapChange();
}

//  QSGNode *QQuickNinePatchImage::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN20QQuickNinePatchImage15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickNinePatchImage *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updatePaintNode(oldNode, data);
}

//  QQuickNinePatchImagePrivate *QQuickNinePatchImage::d_func()
extern "C" Q_DECL_EXPORT
QQuickNinePatchImagePrivate *ritual_ZN20QQuickNinePatchImage6d_funcEv(
    QQuickNinePatchImage *self) {
  return self->d_func();
}

//  const QQuickNinePatchImagePrivate *QQuickNinePatchImage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickNinePatchImagePrivate *ritual_ZNK20QQuickNinePatchImage6d_funcEv(
    const QQuickNinePatchImage *self) {
  return self->d_func();
}
