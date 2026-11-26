//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextutil_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextutil_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextutil_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextutil.cpp, line 48, as _ZN14QQuickTextUtil8alignedXEddi
inline qreal QQuickTextUtil::alignedX(const qreal textWidth, const qreal itemWidth, int alignment)
{
    qreal x = 0;
    switch (alignment) {
    case Qt::AlignLeft:
    case Qt::AlignJustify:
        break;
    case Qt::AlignRight:
        x = itemWidth - textWidth;
        break;
    case Qt::AlignHCenter:
        x = (itemWidth - textWidth) / 2;
        break;
    }
    return x;
}

//  from ../qtdeclarative/src/quick/items/qquicktextutil.cpp, line 65, as _ZN14QQuickTextUtil8alignedYEddi
inline qreal QQuickTextUtil::alignedY(const qreal textHeight, const qreal itemHeight, int alignment)
{
    qreal y = 0;
    switch (alignment) {
    case Qt::AlignTop:
        break;
    case Qt::AlignBottom:
        y = itemHeight - textHeight;
        break;
    case Qt::AlignVCenter:
        y = (itemHeight - textHeight) / 2;
        break;
    }
    return y;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickTextUtil::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTextUtil10metaObjectEv(
    const QQuickTextUtil *self) {
  return self->metaObject();
}

//  void *QQuickTextUtil::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickTextUtil11qt_metacastEPKc(
    QQuickTextUtil *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextUtil::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextUtil11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextUtil *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  qreal QQuickTextUtil::alignedX(qreal textWidth, qreal itemWidth, int
//      alignment)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QQuickTextUtil8alignedXEddi(
    qreal textWidth,
    qreal itemWidth,
    int alignment) {
  return QQuickTextUtil::alignedX(textWidth, itemWidth, alignment);
}

//  qreal QQuickTextUtil::alignedY(qreal textHeight, qreal itemHeight, int
//      alignment)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QQuickTextUtil8alignedYEddi(
    qreal textHeight,
    qreal itemHeight,
    int alignment) {
  return QQuickTextUtil::alignedY(textHeight, itemHeight, alignment);
}
