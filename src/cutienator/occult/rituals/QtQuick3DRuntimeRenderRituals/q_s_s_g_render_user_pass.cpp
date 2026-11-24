//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderUserPass::QSSGRenderUserPass()
extern "C" Q_DECL_EXPORT
QSSGRenderUserPass *ritual_ZN18QSSGRenderUserPassC1Ev() {
  return new QSSGRenderUserPass();
}

//  QSSGRenderUserPass::~QSSGRenderUserPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderUserPassD1Ev(QSSGRenderUserPass *self) {
  delete self;
}

//  bool QSSGRenderUserPass::isDirty(DirtyFlag flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGRenderUserPass7isDirtyENS_9DirtyFlagE(
    const QSSGRenderUserPass *self,
    QSSGRenderUserPass::DirtyFlag flag) {
  return self->isDirty(flag);
}

//  void QSSGRenderUserPass::markDirty(DirtyFlag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderUserPass9markDirtyENS_9DirtyFlagE(
    QSSGRenderUserPass *self,
    QSSGRenderUserPass::DirtyFlag flag) {
  self->markDirty(flag);
}

//  void QSSGRenderUserPass::clearDirty(DirtyFlag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderUserPass10clearDirtyENS_9DirtyFlagE(
    QSSGRenderUserPass *self,
    QSSGRenderUserPass::DirtyFlag flag) {
  self->clearDirty(flag);
}

//  bool QSSGRenderUserPass::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGRenderUserPass7isReadyEv(
    const QSSGRenderUserPass *self) {
  return self->isReady();
}

//  void QSSGRenderUserPass::setDependencyIndex(quint32 index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderUserPass18setDependencyIndexEj(
    QSSGRenderUserPass *self,
    quint32 index) {
  self->setDependencyIndex(index);
}

//  void QSSGRenderUserPass::resetCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderUserPass13resetCommandsEv(
    QSSGRenderUserPass *self) {
  self->resetCommands();
}
