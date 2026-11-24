//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicseffect.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGraphicsDropShadowEffect *QGraphicsDropShadowEffectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsDropShadowEffect *ritual_ZN32QGraphicsDropShadowEffectPrivate6q_funcEv(
    QGraphicsDropShadowEffectPrivate *self) {
  return self->q_func();
}

//  const QGraphicsDropShadowEffect
//      *QGraphicsDropShadowEffectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsDropShadowEffect *ritual_ZNK32QGraphicsDropShadowEffectPrivate6q_funcEv(
    const QGraphicsDropShadowEffectPrivate *self) {
  return self->q_func();
}

//  QGraphicsDropShadowEffectPrivate::QGraphicsDropShadowEffectPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsDropShadowEffectPrivate *ritual_ZN32QGraphicsDropShadowEffectPrivateC1Ev() {
  return new QGraphicsDropShadowEffectPrivate();
}

//  QGraphicsDropShadowEffectPrivate::~QGraphicsDropShadowEffectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGraphicsDropShadowEffectPrivateD1Ev(
    QGraphicsDropShadowEffectPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicseffect)
