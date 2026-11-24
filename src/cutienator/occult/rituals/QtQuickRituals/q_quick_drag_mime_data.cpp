//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
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
