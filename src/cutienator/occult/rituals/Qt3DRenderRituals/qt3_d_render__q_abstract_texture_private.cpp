//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qabstracttexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qabstracttexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  Qt3DRender::QAbstractTexturePrivate::QAbstractTexturePrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexturePrivate *ritual_ZN10Qt3DRender23QAbstractTexturePrivateC1Ev() {
  return new Qt3DRender::QAbstractTexturePrivate();
}

//  QAbstractTexture *Qt3DRender::QAbstractTexturePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZN10Qt3DRender23QAbstractTexturePrivate6q_funcEv(
    Qt3DRender::QAbstractTexturePrivate *self) {
  return self->q_func();
}

//  const QAbstractTexture *Qt3DRender::QAbstractTexturePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender23QAbstractTexturePrivate6q_funcEv(
    const Qt3DRender::QAbstractTexturePrivate *self) {
  return self->q_func();
}

//  QTextureGeneratorPtr Qt3DRender::QAbstractTexturePrivate::dataFunctor()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureGeneratorPtr *ritual_ZNK10Qt3DRender23QAbstractTexturePrivate11dataFunctorEv(
    const Qt3DRender::QAbstractTexturePrivate *self) {
  return new Qt3DRender::QTextureGeneratorPtr(self->dataFunctor());
}

//  void Qt3DRender::QAbstractTexturePrivate::setDataFunctor(const
//      QTextureGeneratorPtr &generator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAbstractTexturePrivate14setDataFunctorERK14QSharedPointerINS_17QTextureGeneratorEE(
    Qt3DRender::QAbstractTexturePrivate *self,
    const Qt3DRender::QTextureGeneratorPtr *generator) {
  self->setDataFunctor(*generator);
}

//  void
//      Qt3DRender::QAbstractTexturePrivate::setStatus(QAbstractTexture::Stat
//      us status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAbstractTexturePrivate9setStatusENS_16QAbstractTexture6StatusE(
    Qt3DRender::QAbstractTexturePrivate *self,
    Qt3DRender::QAbstractTexture::Status status) {
  self->setStatus(status);
}

//  void Qt3DRender::QAbstractTexturePrivate::setHandle(const QVariant
//      &handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAbstractTexturePrivate9setHandleERK8QVariant(
    Qt3DRender::QAbstractTexturePrivate *self,
    const QVariant *handle) {
  self->setHandle(*handle);
}

//  void Qt3DRender::QAbstractTexturePrivate::setHandleType(QAbstractTexture:
//      :HandleType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QAbstractTexturePrivate13setHandleTypeENS_16QAbstractTexture10HandleTypeE(
    Qt3DRender::QAbstractTexturePrivate *self,
    Qt3DRender::QAbstractTexture::HandleType type) {
  self->setHandleType(type);
}

//  a Qt3DRender::QTextureGeneratorPtr a ritual of
//      Qt3DRender::QAbstractTexturePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractTexturePrivate__Qt3DRender_QTextureGeneratorPtr(
    Qt3DRender::QTextureGeneratorPtr *self) {
  delete self;
}
