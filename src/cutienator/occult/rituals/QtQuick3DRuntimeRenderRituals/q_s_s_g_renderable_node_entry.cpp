//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGRenderableNodeEntry::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderableNodeEntry6isNullEv(
    const QSSGRenderableNodeEntry *self) {
  return self->isNull();
}

//  QSSGRenderableNodeEntry::QSSGRenderableNodeEntry()
extern "C" Q_DECL_EXPORT
QSSGRenderableNodeEntry *ritual_ZN23QSSGRenderableNodeEntryC1Ev() {
  return new QSSGRenderableNodeEntry();
}

//  QSSGRenderableNodeEntry::QSSGRenderableNodeEntry(QSSGRenderNode &inNode)
extern "C" Q_DECL_EXPORT
QSSGRenderableNodeEntry *ritual_ZN23QSSGRenderableNodeEntryC1ER14QSSGRenderNode(
    QSSGRenderNode *inNode) {
  return new QSSGRenderableNodeEntry(*inNode);
}

//  QSSGRenderableNodeEntry::QSSGRenderableNodeEntry(QSSGRenderNode *inNode)
extern "C" Q_DECL_EXPORT
QSSGRenderableNodeEntry *ritual_ZN23QSSGRenderableNodeEntryC1EP14QSSGRenderNode(
    QSSGRenderNode *inNode) {
  return new QSSGRenderableNodeEntry(inNode);
}

//  QSSGRenderableNodeEntry::~QSSGRenderableNodeEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderableNodeEntryD1Ev(QSSGRenderableNodeEntry *self) {
  delete self;
}
