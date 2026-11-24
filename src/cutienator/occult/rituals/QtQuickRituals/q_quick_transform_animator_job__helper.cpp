//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickanimator_p.h>
#include <QtQuick/private/qquickanimator_p_p.h>
#include <QtQuick/private/qquickitem_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffect_p.h>
#endif
#include <QtQml/private/qanimationgroupjob_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 347, as _ZN26QQuickTransformAnimatorJob6Helper4syncEv
inline void QQuickTransformAnimatorJob::Helper::sync()
{
    const quint32 mask = QQuickItemPrivate::Position
            | QQuickItemPrivate::BasicTransform
            | QQuickItemPrivate::TransformOrigin
            | QQuickItemPrivate::Size;

    QQuickItemPrivate *d = QQuickItemPrivate::get(item);
#if QT_CONFIG(quick_shadereffect)
    if (d->extra.isAllocated()
            && d->extra->layer
            && d->extra->layer->enabled()) {
        d = QQuickItemPrivate::get(d->extra->layer->m_effectSource);
    }
#endif

    quint32 dirty = mask & d->dirtyAttributes;

    if (!wasSynced) {
        dirty = 0xffffffffu;
        wasSynced = true;
    }

    // We update the node before checking on dirty, as the node might have changed without the animator running
    node = d->itemNode();

    if (dirty == 0)
        return;

    if (dirty & QQuickItemPrivate::Position) {
        dx = item->x();
        dy = item->y();
    }

    if (dirty & QQuickItemPrivate::BasicTransform) {
        scale = item->scale();
        rotation = item->rotation();
    }

    if (dirty & (QQuickItemPrivate::TransformOrigin | QQuickItemPrivate::Size)) {
        QPointF o = item->transformOriginPoint();
        ox = o.x();
        oy = o.y();
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 393, as _ZN26QQuickTransformAnimatorJob6Helper6commitEv
inline void QQuickTransformAnimatorJob::Helper::commit()
{
    if (!wasChanged || !node)
        return;

    QMatrix4x4 m;
    m.translate(dx, dy);
    m.translate(ox, oy);
    m.scale(scale);
    m.rotate(rotation, 0, 0, 1);
    m.translate(-ox, -oy);
    node->setMatrix(m);

    wasChanged = false;
}
//  -----------------------------------------------------------------------

//  QQuickTransformAnimatorJob::Helper::Helper()
extern "C" Q_DECL_EXPORT
QQuickTransformAnimatorJob::Helper *ritual_ZN26QQuickTransformAnimatorJob6HelperC1Ev() {
  return new QQuickTransformAnimatorJob::Helper();
}

//  void QQuickTransformAnimatorJob::Helper::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob6Helper4syncEv(
    QQuickTransformAnimatorJob::Helper *self) {
  self->sync();
}

//  void QQuickTransformAnimatorJob::Helper::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob6Helper6commitEv(
    QQuickTransformAnimatorJob::Helper *self) {
  self->commit();
}

//  QQuickTransformAnimatorJob::Helper::~Helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob6HelperD1Ev(
    QQuickTransformAnimatorJob::Helper *self) {
  delete self;
}
