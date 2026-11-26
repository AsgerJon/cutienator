//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/QList>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickitemviewtransition_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQuick/private/qquicktransitionmanager_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemviewtransition.cpp, line 933, as _ZN28QQuickViewTransitionAttached11targetItemsEv
inline QQmlListProperty<QObject> QQuickViewTransitionAttached::targetItems()
{
    return QQmlListProperty<QObject>(this, &m_targetItems);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickViewTransitionAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickViewTransitionAttached10metaObjectEv(
    const QQuickViewTransitionAttached *self) {
  return self->metaObject();
}

//  void *QQuickViewTransitionAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickViewTransitionAttached11qt_metacastEPKc(
    QQuickViewTransitionAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickViewTransitionAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickViewTransitionAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickViewTransitionAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickViewTransitionAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached24qt_qmlMarker_uncreatableEv(
    QQuickViewTransitionAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickViewTransitionAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached21qt_qmlMarker_attachedEv(
    QQuickViewTransitionAttached *self) {
  self->qt_qmlMarker_attached();
}

//  int QQuickViewTransitionAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickViewTransitionAttached5indexEv(
    const QQuickViewTransitionAttached *self) {
  return self->index();
}

//  QQuickItem *QQuickViewTransitionAttached::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK28QQuickViewTransitionAttached4itemEv(
    const QQuickViewTransitionAttached *self) {
  return self->item();
}

//  QPointF QQuickViewTransitionAttached::destination() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QQuickViewTransitionAttached11destinationEv(
    const QQuickViewTransitionAttached *self) {
  return new QPointF(self->destination());
}

//  QList<int> QQuickViewTransitionAttached::targetIndexes() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK28QQuickViewTransitionAttached13targetIndexesEv(
    const QQuickViewTransitionAttached *self) {
  return new QList<int>(self->targetIndexes());
}

//  QQmlListProperty<QObject> QQuickViewTransitionAttached::targetItems()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN28QQuickViewTransitionAttached11targetItemsEv(
    QQuickViewTransitionAttached *self) {
  return new QQmlListProperty<QObject>(self->targetItems());
}

//  void QQuickViewTransitionAttached::indexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached12indexChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
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

//  void QQuickViewTransitionAttached::itemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached11itemChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::destinationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached18destinationChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "destinationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "destinationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::targetIndexesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached20targetIndexesChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetIndexesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetIndexesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::targetItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached18targetItemsChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetItemsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetItemsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QList<int> a ritual of QQuickViewTransitionAttached gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickViewTransitionAttached__QList_int(QList<int> *self) {
  delete self;
}

//  a QQmlListProperty<QObject> a ritual of QQuickViewTransitionAttached gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickViewTransitionAttached__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_viewtransitions)
