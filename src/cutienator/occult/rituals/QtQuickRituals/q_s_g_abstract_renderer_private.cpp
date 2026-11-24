//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGAbstractRenderer *QSGAbstractRendererPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSGAbstractRenderer *ritual_ZN26QSGAbstractRendererPrivate6q_funcEv(
    QSGAbstractRendererPrivate *self) {
  return self->q_func();
}

//  const QSGAbstractRenderer *QSGAbstractRendererPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSGAbstractRenderer *ritual_ZNK26QSGAbstractRendererPrivate6q_funcEv(
    const QSGAbstractRendererPrivate *self) {
  return self->q_func();
}

//  const QSGAbstractRendererPrivate *QSGAbstractRendererPrivate::get(const
//      QSGAbstractRenderer *q)
extern "C" Q_DECL_EXPORT
const QSGAbstractRendererPrivate *ritual_ZN26QSGAbstractRendererPrivate3getEPK19QSGAbstractRenderer(
    const QSGAbstractRenderer *q) {
  return QSGAbstractRendererPrivate::get(q);
}

//  QSGAbstractRendererPrivate::QSGAbstractRendererPrivate()
extern "C" Q_DECL_EXPORT
QSGAbstractRendererPrivate *ritual_ZN26QSGAbstractRendererPrivateC1Ev() {
  return new QSGAbstractRendererPrivate();
}
