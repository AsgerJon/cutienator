//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const std::unique_ptr<QRhiTexture> &QSSGManagedRhiTexture::texture()
//      const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QRhiTexture> *ritual_ZNK21QSSGManagedRhiTexture7textureEv(
    const QSSGManagedRhiTexture *self) {
  return &(self->texture());
}

//  bool QSSGManagedRhiTexture::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGManagedRhiTexture7isValidEv(
    const QSSGManagedRhiTexture *self) {
  return self->isValid();
}

//  QSSGManagedRhiTexture::QSSGManagedRhiTexture()
extern "C" Q_DECL_EXPORT
QSSGManagedRhiTexture *ritual_ZN21QSSGManagedRhiTextureC1Ev() {
  return new QSSGManagedRhiTexture();
}

//  QSSGManagedRhiTexture::QSSGManagedRhiTexture(const
//      std::shared_ptr<QSSGUserRenderPassManager> &manager, QRhiTexture
//      *texture, Private a2)
extern "C" Q_DECL_EXPORT
QSSGManagedRhiTexture *ritual_ZN21QSSGManagedRhiTextureC1ERKSt10shared_ptrI25QSSGUserRenderPassManagerEP11QRhiTextureNS_7PrivateE(
    const std::shared_ptr<QSSGUserRenderPassManager> *manager,
    QRhiTexture *texture,
    QSSGManagedRhiTexture::Private a2) {
  return new QSSGManagedRhiTexture(*manager, texture, a2);
}

//  QSSGManagedRhiTexture::~QSSGManagedRhiTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGManagedRhiTextureD1Ev(QSSGManagedRhiTexture *self) {
  delete self;
}

//  Ptr QSSGManagedRhiTexture::make_copy(const Ptr &other)
extern "C" Q_DECL_EXPORT
QSSGManagedRhiTexture::Ptr *ritual_ZN21QSSGManagedRhiTexture9make_copyERKSt10unique_ptrIS_St14default_deleteIS_EE(
    const QSSGManagedRhiTexture::Ptr *other) {
  return new QSSGManagedRhiTexture::Ptr(
      QSSGManagedRhiTexture::make_copy(
          *other));
}

//  void QSSGManagedRhiTexture::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGManagedRhiTexture10invalidateEv(
    QSSGManagedRhiTexture *self) {
  self->invalidate();
}

//  a QSSGManagedRhiTexture::Ptr a ritual of QSSGManagedRhiTexture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGManagedRhiTexture__QSSGManagedRhiTexture_Ptr(
    QSSGManagedRhiTexture::Ptr *self) {
  delete self;
}
