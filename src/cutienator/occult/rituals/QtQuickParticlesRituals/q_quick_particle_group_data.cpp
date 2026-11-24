//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQuickParticleGroupData::QQuickParticleGroupData(const QString &name,
//      QQuickParticleSystem *sys)
extern "C" Q_DECL_EXPORT
QQuickParticleGroupData *ritual_ZN23QQuickParticleGroupDataC1ERK7QStringP20QQuickParticleSystem(
    const QString *name,
    QQuickParticleSystem *sys) {
  return new QQuickParticleGroupData(*name, sys);
}

//  QQuickParticleGroupData::~QQuickParticleGroupData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParticleGroupDataD1Ev(QQuickParticleGroupData *self) {
  delete self;
}

//  int QQuickParticleGroupData::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickParticleGroupData4sizeEv(
    const QQuickParticleGroupData *self) {
  return self->size();
}

//  bool QQuickParticleGroupData::isActive()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickParticleGroupData8isActiveEv(
    QQuickParticleGroupData *self) {
  return self->isActive();
}

//  QString QQuickParticleGroupData::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickParticleGroupData4nameEv(
    const QQuickParticleGroupData *self) {
  return new QString(self->name());
}

//  void QQuickParticleGroupData::setSize(int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParticleGroupData7setSizeEi(
    QQuickParticleGroupData *self,
    int newSize) {
  self->setSize(newSize);
}

//  bool QQuickParticleGroupData::recycle()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickParticleGroupData7recycleEv(
    QQuickParticleGroupData *self) {
  return self->recycle();
}

//  void QQuickParticleGroupData::initList()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParticleGroupData8initListEv(
    QQuickParticleGroupData *self) {
  self->initList();
}

//  void QQuickParticleGroupData::kill(QQuickParticleData *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParticleGroupData4killEP18QQuickParticleData(
    QQuickParticleGroupData *self,
    QQuickParticleData *d) {
  self->kill(d);
}

//  QQuickParticleData *QQuickParticleGroupData::newDatum(bool
//      respectsLimits)
extern "C" Q_DECL_EXPORT
QQuickParticleData *ritual_ZN23QQuickParticleGroupData8newDatumEb(
    QQuickParticleGroupData *self,
    bool respectsLimits) {
  return self->newDatum(respectsLimits);
}

//  void QQuickParticleGroupData::prepareRecycler(QQuickParticleData *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParticleGroupData15prepareRecyclerEP18QQuickParticleData(
    QQuickParticleGroupData *self,
    QQuickParticleData *d) {
  self->prepareRecycler(d);
}
