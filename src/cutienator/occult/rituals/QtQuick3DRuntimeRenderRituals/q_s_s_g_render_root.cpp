//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderroot_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderroot_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderRoot::QSSGRenderRoot()
extern "C" Q_DECL_EXPORT
QSSGRenderRoot *ritual_ZN14QSSGRenderRootC1Ev() {
  return new QSSGRenderRoot();
}

//  QSSGRenderRoot::~QSSGRenderRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderRootD1Ev(QSSGRenderRoot *self) {
  delete self;
}

//  bool QSSGRenderRoot::isDirty(DirtyFlag dirtyFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderRoot7isDirtyENS_9DirtyFlagE(
    const QSSGRenderRoot *self,
    QSSGRenderRoot::DirtyFlag dirtyFlag) {
  return self->isDirty(dirtyFlag);
}

//  void QSSGRenderRoot::markDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderRoot9markDirtyENS_9DirtyFlagE(
    QSSGRenderRoot *self,
    QSSGRenderRoot::DirtyFlag dirtyFlag) {
  self->markDirty(dirtyFlag);
}

//  void QSSGRenderRoot::clearDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderRoot10clearDirtyENS_9DirtyFlagE(
    QSSGRenderRoot *self,
    QSSGRenderRoot::DirtyFlag dirtyFlag) {
  self->clearDirty(dirtyFlag);
}

//  const std::shared_ptr<QSSGGlobalRenderNodeData>
//      &QSSGRenderRoot::globalNodeData() const
extern "C" Q_DECL_EXPORT
const std::shared_ptr<QSSGGlobalRenderNodeData> *ritual_ZNK14QSSGRenderRoot14globalNodeDataEv(
    const QSSGRenderRoot *self) {
  return &(self->globalNodeData());
}

//  void QSSGRenderRoot::setStartVersion(VersionType startVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderRoot15setStartVersionEt(
    QSSGRenderRoot *self,
    QSSGRenderRoot::VersionType startVersion) {
  self->setStartVersion(startVersion);
}

//  VersionType QSSGRenderRoot::startVersion() const
extern "C" Q_DECL_EXPORT
QSSGRenderRoot::VersionType ritual_ZNK14QSSGRenderRoot12startVersionEv(
    const QSSGRenderRoot *self) {
  return self->startVersion();
}

//  QSSGRenderRoot *QSSGRenderRoot::get(QSSGRenderRoot **ref)
extern "C" Q_DECL_EXPORT
QSSGRenderRoot *ritual_ZN14QSSGRenderRoot3getEPPS_(QSSGRenderRoot **ref) {
  return QSSGRenderRoot::get(ref);
}

//  void QSSGRenderRoot::reindex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderRoot7reindexEv(QSSGRenderRoot *self) {
  self->reindex();
}
