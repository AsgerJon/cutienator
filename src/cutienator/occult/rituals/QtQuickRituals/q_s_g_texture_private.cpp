//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGTexture *QSGTexturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN17QSGTexturePrivate6q_funcEv(QSGTexturePrivate *self) {
  return self->q_func();
}

//  const QSGTexture *QSGTexturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSGTexture *ritual_ZNK17QSGTexturePrivate6q_funcEv(
    const QSGTexturePrivate *self) {
  return self->q_func();
}

//  QSGTexturePrivate::QSGTexturePrivate(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePrivate *ritual_ZN17QSGTexturePrivateC1EP10QSGTexture(
    QSGTexture *t) {
  return new QSGTexturePrivate(t);
}

//  QSGTexturePrivate *QSGTexturePrivate::get(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePrivate *ritual_ZN17QSGTexturePrivate3getEP10QSGTexture(
    QSGTexture *t) {
  return QSGTexturePrivate::get(t);
}

//  void QSGTexturePrivate::resetDirtySamplerOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGTexturePrivate24resetDirtySamplerOptionsEv(
    QSGTexturePrivate *self) {
  self->resetDirtySamplerOptions();
}

//  bool QSGTexturePrivate::hasDirtySamplerOptions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSGTexturePrivate22hasDirtySamplerOptionsEv(
    const QSGTexturePrivate *self) {
  return self->hasDirtySamplerOptions();
}
