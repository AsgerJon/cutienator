//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgplaintexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgplaintexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGPlainTexture *QSGPlainTexturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSGPlainTexture *ritual_ZN22QSGPlainTexturePrivate6q_funcEv(
    QSGPlainTexturePrivate *self) {
  return self->q_func();
}

//  const QSGPlainTexture *QSGPlainTexturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSGPlainTexture *ritual_ZNK22QSGPlainTexturePrivate6q_funcEv(
    const QSGPlainTexturePrivate *self) {
  return self->q_func();
}

//  QSGPlainTexturePrivate::QSGPlainTexturePrivate(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGPlainTexturePrivate *ritual_ZN22QSGPlainTexturePrivateC1EP10QSGTexture(
    QSGTexture *t) {
  return new QSGPlainTexturePrivate(t);
}
