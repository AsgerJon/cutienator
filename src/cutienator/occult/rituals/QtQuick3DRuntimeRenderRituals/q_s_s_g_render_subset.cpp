//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderSubset::QSSGRenderSubset()
extern "C" Q_DECL_EXPORT
QSSGRenderSubset *ritual_ZN16QSSGRenderSubsetC1Ev() {
  return new QSSGRenderSubset();
}

//  QSSGRenderSubset::QSSGRenderSubset(const QSSGRenderSubset &inOther)
extern "C" Q_DECL_EXPORT
QSSGRenderSubset *ritual_ZN16QSSGRenderSubsetC1ERKS_(
    const QSSGRenderSubset *inOther) {
  return new QSSGRenderSubset(*inOther);
}

//  QSSGRenderSubset &QSSGRenderSubset::operator=(const QSSGRenderSubset
//      &inOther)
extern "C" Q_DECL_EXPORT
QSSGRenderSubset *ritual_ZN16QSSGRenderSubsetaSERKS_(
    QSSGRenderSubset *self,
    const QSSGRenderSubset *inOther) {
  return &(self->operator=(*inOther));
}

//  quint32 QSSGRenderSubset::lodCount(int lodLevel) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QSSGRenderSubset8lodCountEi(
    const QSSGRenderSubset *self,
    int lodLevel) {
  return self->lodCount(lodLevel);
}

//  quint32 QSSGRenderSubset::lodOffset(int lodLevel) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QSSGRenderSubset9lodOffsetEi(
    const QSSGRenderSubset *self,
    int lodLevel) {
  return self->lodOffset(lodLevel);
}

//  QSSGRenderSubset::~QSSGRenderSubset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderSubsetD1Ev(QSSGRenderSubset *self) {
  delete self;
}
