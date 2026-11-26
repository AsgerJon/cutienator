//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlecustomshape_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlecustomshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QQuick3DParticleCustomShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuick3DParticleCustomShape10metaObjectEv(
    const QQuick3DParticleCustomShape *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleCustomShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuick3DParticleCustomShape11qt_metacastEPKc(
    QQuick3DParticleCustomShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleCustomShape::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuick3DParticleCustomShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleCustomShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleCustomShape::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuick3DParticleCustomShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleCustomShape::tr(s, c, n));
}

//  QQuick3DParticleCustomShape::QQuick3DParticleCustomShape(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleCustomShape *ritual_ZN27QQuick3DParticleCustomShapeC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleCustomShape(parent);
}

//  QUrl QQuick3DParticleCustomShape::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK27QQuick3DParticleCustomShape6sourceEv(
    const QQuick3DParticleCustomShape *self) {
  return new QUrl(self->source());
}

//  bool QQuick3DParticleCustomShape::randomizeData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuick3DParticleCustomShape13randomizeDataEv(
    const QQuick3DParticleCustomShape *self) {
  return self->randomizeData();
}

//  QVector3D QQuick3DParticleCustomShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN27QQuick3DParticleCustomShape11getPositionEi(
    QQuick3DParticleCustomShape *self,
    int particleIndex) {
  return new QVector3D(self->getPosition(particleIndex));
}

//  QVector3D QQuick3DParticleCustomShape::getSurfaceNormal(int
//      particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN27QQuick3DParticleCustomShape16getSurfaceNormalEi(
    QQuick3DParticleCustomShape *self,
    int particleIndex) {
  return new QVector3D(self->getSurfaceNormal(particleIndex));
}

//  void QQuick3DParticleCustomShape::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape9setSourceERK4QUrl(
    QQuick3DParticleCustomShape *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QQuick3DParticleCustomShape::setRandomizeData(bool random)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape16setRandomizeDataEb(
    QQuick3DParticleCustomShape *self,
    bool random) {
  self->setRandomizeData(random);
}

//  void QQuick3DParticleCustomShape::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape13sourceChangedEv(
    QQuick3DParticleCustomShape *self) {
  self->sourceChanged();
}

//  void QQuick3DParticleCustomShape::randomizeDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape20randomizeDataChangedEv(
    QQuick3DParticleCustomShape *self) {
  self->randomizeDataChanged();
}

//  void QQuick3DParticleCustomShape::loadFromSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape14loadFromSourceEv(
    QQuick3DParticleCustomShape *self) {
  self->loadFromSource();
}

//  void QQuick3DParticleCustomShape::doRandomizeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DParticleCustomShape15doRandomizeDataEv(
    QQuick3DParticleCustomShape *self) {
  self->doRandomizeData();
}

//  QVector3D QQuick3DParticleCustomShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN27QQuick3DParticleCustomShape11getPositionEi(
    QQuick3DParticleCustomShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleCustomShape::getPosition(
          particleIndex));
}

//  QVector3D QQuick3DParticleCustomShape::getSurfaceNormal(int
//      particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN27QQuick3DParticleCustomShape16getSurfaceNormalEi(
    QQuick3DParticleCustomShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleCustomShape::getSurfaceNormal(
          particleIndex));
}
