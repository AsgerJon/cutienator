//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#endif
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicseffect_p.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/effects/qgraphicseffect.cpp, line 355, as _ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16InvalidateReasonE
inline void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason reason) const
{
    if (m_cachedMode != QGraphicsEffect::PadToEffectiveBoundingRect
        && (reason == EffectRectChanged
            || (reason == TransformChanged && m_cachedSystem == Qt::LogicalCoordinates))) {
        return;
    }

    QPixmapCache::remove(m_cacheKey);
}
//  -----------------------------------------------------------------------

//  QGraphicsEffect *QGraphicsEffectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsEffect *ritual_ZN22QGraphicsEffectPrivate6q_funcEv(
    QGraphicsEffectPrivate *self) {
  return self->q_func();
}

//  const QGraphicsEffect *QGraphicsEffectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsEffect *ritual_ZNK22QGraphicsEffectPrivate6q_funcEv(
    const QGraphicsEffectPrivate *self) {
  return self->q_func();
}

//  QGraphicsEffectPrivate::QGraphicsEffectPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsEffectPrivate *ritual_ZN22QGraphicsEffectPrivateC1Ev() {
  return new QGraphicsEffectPrivate();
}

//  QGraphicsEffectPrivate::~QGraphicsEffectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsEffectPrivateD1Ev(QGraphicsEffectPrivate *self) {
  delete self;
}

//  void
//      QGraphicsEffectPrivate::setGraphicsEffectSource(QGraphicsEffectSource
//      *newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsEffectPrivate23setGraphicsEffectSourceEP21QGraphicsEffectSource(
    QGraphicsEffectPrivate *self,
    QGraphicsEffectSource *newSource) {
  self->setGraphicsEffectSource(newSource);
}

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicseffect)
