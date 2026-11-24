//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderinstancetable_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderinstancetable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qvectornd.h>

//  QSSGRenderInstanceTable::QSSGRenderInstanceTable()
extern "C" Q_DECL_EXPORT
QSSGRenderInstanceTable *ritual_ZN23QSSGRenderInstanceTableC1Ev() {
  return new QSSGRenderInstanceTable();
}

//  int QSSGRenderInstanceTable::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSSGRenderInstanceTable5countEv(
    const QSSGRenderInstanceTable *self) {
  return self->count();
}

//  qsizetype QSSGRenderInstanceTable::dataSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QSSGRenderInstanceTable8dataSizeEv(
    const QSSGRenderInstanceTable *self) {
  return self->dataSize();
}

//  void QSSGRenderInstanceTable::setData(const QByteArray &data, int count,
//      int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable7setDataERK10QByteArrayii(
    QSSGRenderInstanceTable *self,
    const QByteArray *data,
    int count,
    int stride) {
  self->setData(*data, count, stride);
}

//  void QSSGRenderInstanceTable::setInstanceCountOverride(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable24setInstanceCountOverrideEi(
    QSSGRenderInstanceTable *self,
    int count) {
  self->setInstanceCountOverride(count);
}

//  int QSSGRenderInstanceTable::serial() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSSGRenderInstanceTable6serialEv(
    const QSSGRenderInstanceTable *self) {
  return self->serial();
}

//  int QSSGRenderInstanceTable::stride() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSSGRenderInstanceTable6strideEv(
    const QSSGRenderInstanceTable *self) {
  return self->stride();
}

//  bool QSSGRenderInstanceTable::hasTransparency()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QSSGRenderInstanceTable15hasTransparencyEv(
    QSSGRenderInstanceTable *self) {
  return self->hasTransparency();
}

//  void QSSGRenderInstanceTable::setHasTransparency(bool t)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable18setHasTransparencyEb(
    QSSGRenderInstanceTable *self,
    bool t) {
  self->setHasTransparency(t);
}

//  void QSSGRenderInstanceTable::setDepthSorting(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable15setDepthSortingEb(
    QSSGRenderInstanceTable *self,
    bool enable) {
  self->setDepthSorting(enable);
}

//  bool QSSGRenderInstanceTable::isDepthSortingEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QSSGRenderInstanceTable21isDepthSortingEnabledEv(
    QSSGRenderInstanceTable *self) {
  return self->isDepthSortingEnabled();
}

//  QMatrix4x4 QSSGRenderInstanceTable::getTransform(int index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK23QSSGRenderInstanceTable12getTransformEi(
    const QSSGRenderInstanceTable *self,
    int index) {
  return new QMatrix4x4(self->getTransform(index));
}

//  void QSSGRenderInstanceTable::setShadowBoundsMinimum(const QVector3D
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable22setShadowBoundsMinimumERK9QVector3D(
    QSSGRenderInstanceTable *self,
    const QVector3D *value) {
  self->setShadowBoundsMinimum(*value);
}

//  void QSSGRenderInstanceTable::setShadowBoundsMaximum(const QVector3D
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderInstanceTable22setShadowBoundsMaximumERK9QVector3D(
    QSSGRenderInstanceTable *self,
    const QVector3D *value) {
  self->setShadowBoundsMaximum(*value);
}

//  QVector3D QSSGRenderInstanceTable::getShadowBoundsMinimum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QSSGRenderInstanceTable22getShadowBoundsMinimumEv(
    const QSSGRenderInstanceTable *self) {
  return new QVector3D(self->getShadowBoundsMinimum());
}

//  QVector3D QSSGRenderInstanceTable::getShadowBoundsMaximum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QSSGRenderInstanceTable22getShadowBoundsMaximumEv(
    const QSSGRenderInstanceTable *self) {
  return new QVector3D(self->getShadowBoundsMaximum());
}
