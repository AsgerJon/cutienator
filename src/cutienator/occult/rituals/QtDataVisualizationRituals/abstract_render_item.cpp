//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstractrenderitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstractrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>

//  AbstractRenderItem::~AbstractRenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItemD1Ev(AbstractRenderItem *self) {
  delete self;
}

//  void AbstractRenderItem::setTranslation(const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItem14setTranslationERK9QVector3D(
    AbstractRenderItem *self,
    const QVector3D *translation) {
  self->setTranslation(*translation);
}

//  const QVector3D &AbstractRenderItem::translation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18AbstractRenderItem11translationEv(
    const AbstractRenderItem *self) {
  return new QVector3D(self->translation());
}

//  const QQuaternion &AbstractRenderItem::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK18AbstractRenderItem8rotationEv(
    const AbstractRenderItem *self) {
  return new QQuaternion(self->rotation());
}

//  void AbstractRenderItem::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItem11setRotationERK11QQuaternion(
    AbstractRenderItem *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}
