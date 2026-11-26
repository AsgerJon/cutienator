//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickDragMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickDragMimeData10metaObjectEv(
    const QQuickDragMimeData *self) {
  return self->metaObject();
}

//  void *QQuickDragMimeData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickDragMimeData11qt_metacastEPKc(
    QQuickDragMimeData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDragMimeData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDragMimeData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDragMimeData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QStringList QQuickDragMimeData::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QQuickDragMimeData4keysEv(
    const QQuickDragMimeData *self) {
  return new QList<QString>(self->keys());
}

//  QObject *QQuickDragMimeData::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQuickDragMimeData6sourceEv(
    const QQuickDragMimeData *self) {
  return self->source();
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
