//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry(const QByteArray
//      &nm, QSSGRenderComponentType type, quint32 numComponents, quint32
//      firstItemOffset)
extern "C" Q_DECL_EXPORT
QSSGRenderVertexBufferEntry *ritual_ZN27QSSGRenderVertexBufferEntryC1ERK10QByteArray23QSSGRenderComponentTypejj(
    const QByteArray *nm,
    QSSGRenderComponentType type,
    quint32 numComponents,
    quint32 firstItemOffset) {
  return new QSSGRenderVertexBufferEntry(
      *nm,
      type,
      numComponents,
      firstItemOffset);
}

//  QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry()
extern "C" Q_DECL_EXPORT
QSSGRenderVertexBufferEntry *ritual_ZN27QSSGRenderVertexBufferEntryC1Ev() {
  return new QSSGRenderVertexBufferEntry();
}

//  QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry(const
//      QSSGRenderVertexBufferEntry &inOther)
extern "C" Q_DECL_EXPORT
QSSGRenderVertexBufferEntry *ritual_ZN27QSSGRenderVertexBufferEntryC1ERKS_(
    const QSSGRenderVertexBufferEntry *inOther) {
  return new QSSGRenderVertexBufferEntry(*inOther);
}

//  QSSGRenderVertexBufferEntry::~QSSGRenderVertexBufferEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderVertexBufferEntryD1Ev(
    QSSGRenderVertexBufferEntry *self) {
  delete self;
}
