//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  QSSGManagedRhiTexture::~QSSGManagedRhiTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGManagedRhiTextureD1Ev(QSSGManagedRhiTexture *self) {
  delete self;
}

//  void QSSGManagedRhiTexture::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGManagedRhiTexture10invalidateEv(
    QSSGManagedRhiTexture *self) {
  self->invalidate();
}
