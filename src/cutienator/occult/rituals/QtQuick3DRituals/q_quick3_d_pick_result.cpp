//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpickresult_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpickresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>

//  QQuick3DPickResult::QQuick3DPickResult()
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZN18QQuick3DPickResultC1Ev() {
  return new QQuick3DPickResult();
}

//  QQuick3DPickResult::QQuick3DPickResult(QQuick3DModel *hitObject, float
//      distanceFromCamera, const QVector2D &uvPosition, const QVector3D
//      &scenePosition, const QVector3D &position, const QVector3D &normal,
//      const QVector3D &sceneNormal, int instanceIndex, QQuickItem *itemHit)
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZN18QQuick3DPickResultC1EP13QQuick3DModelfRK9QVector2DRK9QVector3DS7_S7_S7_iP10QQuickItem(
    QQuick3DModel *hitObject,
    float distanceFromCamera,
    const QVector2D *uvPosition,
    const QVector3D *scenePosition,
    const QVector3D *position,
    const QVector3D *normal,
    const QVector3D *sceneNormal,
    int instanceIndex,
    QQuickItem *itemHit) {
  return new QQuick3DPickResult(
      hitObject,
      distanceFromCamera,
      *uvPosition,
      *scenePosition,
      *position,
      *normal,
      *sceneNormal,
      instanceIndex,
      itemHit);
}

//  QQuick3DPickResult::QQuick3DPickResult(QQuickItem *itemHit, float
//      distanceFromCamera, const QVector2D &uvPosition, const QVector3D
//      &scenePosition, const QVector3D &position, const QVector3D
//      &sceneNormal)
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZN18QQuick3DPickResultC1EP10QQuickItemfRK9QVector2DRK9QVector3DS7_S7_(
    QQuickItem *itemHit,
    float distanceFromCamera,
    const QVector2D *uvPosition,
    const QVector3D *scenePosition,
    const QVector3D *position,
    const QVector3D *sceneNormal) {
  return new QQuick3DPickResult(
      itemHit,
      distanceFromCamera,
      *uvPosition,
      *scenePosition,
      *position,
      *sceneNormal);
}

//  QQuick3DModel *QQuick3DPickResult::objectHit() const
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZNK18QQuick3DPickResult9objectHitEv(
    const QQuick3DPickResult *self) {
  return self->objectHit();
}

//  float QQuick3DPickResult::distance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QQuick3DPickResult8distanceEv(
    const QQuick3DPickResult *self) {
  return self->distance();
}

//  QVector2D QQuick3DPickResult::uvPosition() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK18QQuick3DPickResult10uvPositionEv(
    const QQuick3DPickResult *self) {
  return new QVector2D(self->uvPosition());
}

//  QVector3D QQuick3DPickResult::scenePosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DPickResult13scenePositionEv(
    const QQuick3DPickResult *self) {
  return new QVector3D(self->scenePosition());
}

//  QVector3D QQuick3DPickResult::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DPickResult8positionEv(
    const QQuick3DPickResult *self) {
  return new QVector3D(self->position());
}

//  QVector3D QQuick3DPickResult::normal() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DPickResult6normalEv(
    const QQuick3DPickResult *self) {
  return new QVector3D(self->normal());
}

//  QVector3D QQuick3DPickResult::sceneNormal() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DPickResult11sceneNormalEv(
    const QQuick3DPickResult *self) {
  return new QVector3D(self->sceneNormal());
}

//  int QQuick3DPickResult::instanceIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuick3DPickResult13instanceIndexEv(
    const QQuick3DPickResult *self) {
  return self->instanceIndex();
}

//  QQuickItem *QQuick3DPickResult::itemHit() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuick3DPickResult7itemHitEv(
    const QQuick3DPickResult *self) {
  return self->itemHit();
}

//  QQuick3DPickResultEnums::HitType QQuick3DPickResult::hitType() const
extern "C" Q_DECL_EXPORT
QQuick3DPickResultEnums::HitType ritual_ZNK18QQuick3DPickResult7hitTypeEv(
    const QQuick3DPickResult *self) {
  return self->hitType();
}

//  QQuick3DPickResult::~QQuick3DPickResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPickResultD1Ev(QQuick3DPickResult *self) {
  delete self;
}

//  QList<QQuick3DPickResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuick3DPickResult> *ritual_list_make_QQuick3DPickResult() {
  return new QList<QQuick3DPickResult>();
}

//  void QList<QQuick3DPickResult>::append(const QQuick3DPickResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuick3DPickResult(
    QList<QQuick3DPickResult> *self,
    const QQuick3DPickResult *element) {
  self->append(*element);
}

//  qsizetype QList<QQuick3DPickResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuick3DPickResult(
    const QList<QQuick3DPickResult> *self) {
  return self->size();
}

//  const QQuick3DPickResult &QList<QQuick3DPickResult>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_list_at_QQuick3DPickResult(
    const QList<QQuick3DPickResult> *self,
    long long index) {
  return new QQuick3DPickResult(self->at(index));
}

//  QList<QQuick3DPickResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuick3DPickResult(QList<QQuick3DPickResult> *self) {
  delete self;
}
