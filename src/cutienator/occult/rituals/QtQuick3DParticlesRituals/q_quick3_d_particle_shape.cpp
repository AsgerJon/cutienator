//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QQuick3DParticleShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DParticleShape10metaObjectEv(
    const QQuick3DParticleShape *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DParticleShape11qt_metacastEPKc(
    QQuick3DParticleShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleShape::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DParticleShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DParticleShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleShape::tr(s, c, n));
}

//  QQuick3DParticleShape::QQuick3DParticleShape(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleShape *ritual_ZN21QQuick3DParticleShapeC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleShape(parent);
}

//  bool QQuick3DParticleShape::fill() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DParticleShape4fillEv(
    const QQuick3DParticleShape *self) {
  return self->fill();
}

//  ShapeType QQuick3DParticleShape::type() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleShape::ShapeType ritual_ZNK21QQuick3DParticleShape4typeEv(
    const QQuick3DParticleShape *self) {
  return self->type();
}

//  QVector3D QQuick3DParticleShape::extents() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK21QQuick3DParticleShape7extentsEv(
    const QQuick3DParticleShape *self) {
  return new QVector3D(self->extents());
}

//  QVector3D QQuick3DParticleShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN21QQuick3DParticleShape11getPositionEi(
    QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(self->getPosition(particleIndex));
}

//  QVector3D QQuick3DParticleShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN21QQuick3DParticleShape16getSurfaceNormalEi(
    QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(self->getSurfaceNormal(particleIndex));
}

//  void QQuick3DParticleShape::setFill(bool fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape7setFillEb(
    QQuick3DParticleShape *self,
    bool fill) {
  self->setFill(fill);
}

//  void QQuick3DParticleShape::setType(QQuick3DParticleShape::ShapeType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape7setTypeENS_9ShapeTypeE(
    QQuick3DParticleShape *self,
    QQuick3DParticleShape::ShapeType type) {
  self->setType(type);
}

//  void QQuick3DParticleShape::setExtents(QVector3D extends)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape10setExtentsE9QVector3D(
    QQuick3DParticleShape *self,
    const QVector3D *extends) {
  self->setExtents(*extends);
}

//  void QQuick3DParticleShape::fillChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape11fillChangedEv(
    QQuick3DParticleShape *self) {
  self->fillChanged();
}

//  void QQuick3DParticleShape::typeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape11typeChangedEv(
    QQuick3DParticleShape *self) {
  self->typeChanged();
}

//  void QQuick3DParticleShape::extentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DParticleShape14extentsChangedEv(
    QQuick3DParticleShape *self) {
  self->extentsChanged();
}

//  QVector3D QQuick3DParticleShape::randomPositionCube(int particleIndex)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK21QQuick3DParticleShape18randomPositionCubeEi(
    const QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(self->randomPositionCube(particleIndex));
}

//  QVector3D QQuick3DParticleShape::randomPositionSphere(int particleIndex)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK21QQuick3DParticleShape20randomPositionSphereEi(
    const QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(self->randomPositionSphere(particleIndex));
}

//  QVector3D QQuick3DParticleShape::randomPositionCylinder(int
//      particleIndex) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK21QQuick3DParticleShape22randomPositionCylinderEi(
    const QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(self->randomPositionCylinder(particleIndex));
}

//  QVector3D QQuick3DParticleShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN21QQuick3DParticleShape11getPositionEi(
    QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleShape::getPosition(
          particleIndex));
}

//  QVector3D QQuick3DParticleShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN21QQuick3DParticleShape16getSurfaceNormalEi(
    QQuick3DParticleShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleShape::getSurfaceNormal(
          particleIndex));
}
