//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssguserrenderpassmanager_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssguserrenderpassmanager_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <memory>

//  QSSGUserRenderPassManager::QSSGUserRenderPassManager(Private a0)
extern "C" Q_DECL_EXPORT
QSSGUserRenderPassManager *ritual_ZN25QSSGUserRenderPassManagerC1ENS_7PrivateE(
    QSSGUserRenderPassManager::Private a0) {
  return new QSSGUserRenderPassManager(a0);
}

//  QSSGUserRenderPassManager::~QSSGUserRenderPassManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManagerD1Ev(
    QSSGUserRenderPassManager *self) {
  delete self;
}

//  std::shared_ptr<QSSGUserRenderPassManager>
//      QSSGUserRenderPassManager::create()
extern "C" Q_DECL_EXPORT
std::shared_ptr<QSSGUserRenderPassManager> *ritual_ZN25QSSGUserRenderPassManager6createEv() {
  return new std::shared_ptr<QSSGUserRenderPassManager>(
      QSSGUserRenderPassManager::create());
}

//  void QSSGUserRenderPassManager::scheduleUserPass(QSSGRenderUserPass
//      *userPasses)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager16scheduleUserPassEP18QSSGRenderUserPass(
    QSSGUserRenderPassManager *self,
    QSSGRenderUserPass *userPasses) {
  self->scheduleUserPass(userPasses);
}

//  void QSSGUserRenderPassManager::unscheduleUserPass(const
//      QSSGRenderUserPass *userPasses)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager18unscheduleUserPassEPK18QSSGRenderUserPass(
    QSSGUserRenderPassManager *self,
    const QSSGRenderUserPass *userPasses) {
  self->unscheduleUserPass(userPasses);
}

//  QSSGRhiRenderableTextureV2Ptr
//      QSSGUserRenderPassManager::getOrCreateRenderableTexture(const
//      QSSGRenderUserPass &userPass)
extern "C" Q_DECL_EXPORT
QSSGRhiRenderableTextureV2Ptr *ritual_ZN25QSSGUserRenderPassManager28getOrCreateRenderableTextureERK18QSSGRenderUserPass(
    QSSGUserRenderPassManager *self,
    const QSSGRenderUserPass *userPass) {
  return new QSSGRhiRenderableTextureV2Ptr(
      self->getOrCreateRenderableTexture(
          *userPass));
}

//  QSSGRhiRenderableTextureV2Ptr
//      QSSGUserRenderPassManager::getUserPassTexureResult(const
//      QSSGRenderUserPass &userPass) const
extern "C" Q_DECL_EXPORT
QSSGRhiRenderableTextureV2Ptr *ritual_ZNK25QSSGUserRenderPassManager23getUserPassTexureResultERK18QSSGRenderUserPass(
    const QSSGUserRenderPassManager *self,
    const QSSGRenderUserPass *userPass) {
  return new QSSGRhiRenderableTextureV2Ptr(
      self->getUserPassTexureResult(
          *userPass));
}

//  void QSSGUserRenderPassManager::updateUserPassOrder(bool forceUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager19updateUserPassOrderEb(
    QSSGUserRenderPassManager *self,
    bool forceUpdate) {
  self->updateUserPassOrder(forceUpdate);
}

//  const UserPassSet &QSSGUserRenderPassManager::scheduledUserPasses() const
extern "C" Q_DECL_EXPORT
QList<QSSGRenderUserPass *> *ritual_ZNK25QSSGUserRenderPassManager19scheduledUserPassesEv(
    const QSSGUserRenderPassManager *self) {
  return new QList<QSSGRenderUserPass *>(self->scheduledUserPasses());
}

//  void QSSGUserRenderPassManager::releaseAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager10releaseAllEv(
    QSSGUserRenderPassManager *self) {
  self->releaseAll();
}

//  void
//      QSSGUserRenderPassManager::unregisterManagedTexture(QSSGManagedRhiTex
//      ture *textureWrapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager24unregisterManagedTextureEP21QSSGManagedRhiTexture(
    QSSGUserRenderPassManager *self,
    QSSGManagedRhiTexture *textureWrapper) {
  self->unregisterManagedTexture(textureWrapper);
}

//  void
//      QSSGUserRenderPassManager::registerManagedTexture(QSSGManagedRhiTextu
//      re *textureWrapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager22registerManagedTextureEP21QSSGManagedRhiTexture(
    QSSGUserRenderPassManager *self,
    QSSGManagedRhiTexture *textureWrapper) {
  self->registerManagedTexture(textureWrapper);
}

//  size_t QSSGUserRenderPassManager::maxUserPassSlots()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QSSGUserRenderPassManager16maxUserPassSlotsEv() {
  return QSSGUserRenderPassManager::maxUserPassSlots();
}

//  qsizetype QSSGUserRenderPassManager::acquireUserPassSlot()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN25QSSGUserRenderPassManager19acquireUserPassSlotEv(
    QSSGUserRenderPassManager *self) {
  return self->acquireUserPassSlot();
}

//  void QSSGUserRenderPassManager::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager13resetForFrameEv(
    QSSGUserRenderPassManager *self) {
  self->resetForFrame();
}

//  bool QSSGUserRenderPassManager::derefTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGUserRenderPassManager12derefTextureEP11QRhiTexture(
    QSSGUserRenderPassManager *self,
    QRhiTexture *texture) {
  return self->derefTexture(texture);
}

//  void QSSGUserRenderPassManager::refTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager10refTextureEP11QRhiTexture(
    QSSGUserRenderPassManager *self,
    QRhiTexture *texture) {
  self->refTexture(texture);
}

//  bool QSSGUserRenderPassManager::derefTexture(const
//      std::unique_ptr<QRhiTexture> &texture)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGUserRenderPassManager12derefTextureERKSt10unique_ptrI11QRhiTextureSt14default_deleteIS1_EE(
    QSSGUserRenderPassManager *self,
    const std::unique_ptr<QRhiTexture> *texture) {
  return self->derefTexture(*texture);
}

//  void QSSGUserRenderPassManager::refTexture(const
//      std::unique_ptr<QRhiTexture> &texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGUserRenderPassManager10refTextureERKSt10unique_ptrI11QRhiTextureSt14default_deleteIS1_EE(
    QSSGUserRenderPassManager *self,
    const std::unique_ptr<QRhiTexture> *texture) {
  self->refTexture(*texture);
}

//  a std::shared_ptr<QSSGUserRenderPassManager> a ritual of
//      QSSGUserRenderPassManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGUserRenderPassManager__std_shared_ptr_QSSGUserRenderPassManager(
    std::shared_ptr<QSSGUserRenderPassManager> *self) {
  delete self;
}

//  a QSSGRhiRenderableTextureV2Ptr a ritual of QSSGUserRenderPassManager
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGUserRenderPassManager__QSSGRhiRenderableTextureV2Ptr(
    QSSGRhiRenderableTextureV2Ptr *self) {
  delete self;
}
