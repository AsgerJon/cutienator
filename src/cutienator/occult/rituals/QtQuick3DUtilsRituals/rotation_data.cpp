//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>

//  RotationData::RotationData()
extern "C" Q_DECL_EXPORT
RotationData *ritual_ZN12RotationDataC1Ev() {
  return new RotationData();
}

//  RotationData::RotationData(const QVector3D &r)
extern "C" Q_DECL_EXPORT
RotationData *ritual_ZN12RotationDataC1ERK9QVector3D(const QVector3D *r) {
  return new RotationData(*r);
}

//  RotationData::RotationData(const QQuaternion &r)
extern "C" Q_DECL_EXPORT
RotationData *ritual_ZN12RotationDataC1ERK11QQuaternion(
    const QQuaternion *r) {
  return new RotationData(*r);
}

//  bool operator==(const RotationData &a, const RotationData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12RotationDataS1_(
    const RotationData *a,
    const RotationData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const RotationData &a, const RotationData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12RotationDataS1_(
    const RotationData *a,
    const RotationData *b) {
  return operator!=(*a, *b);
}

//  bool operator==(const RotationData &a, const QVector3D &eulerRotation)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12RotationDataRK9QVector3D(
    const RotationData *a,
    const QVector3D *eulerRotation) {
  return operator==(*a, *eulerRotation);
}

//  bool operator!=(const RotationData &a, const QVector3D &eulerRotation)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12RotationDataRK9QVector3D(
    const RotationData *a,
    const QVector3D *eulerRotation) {
  return operator!=(*a, *eulerRotation);
}

//  bool operator==(const QVector3D &eulerRotation, const RotationData &a)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QVector3DRK12RotationData(
    const QVector3D *eulerRotation,
    const RotationData *a) {
  return operator==(*eulerRotation, *a);
}

//  bool operator!=(const QVector3D &eulerRotation, const RotationData &a)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QVector3DRK12RotationData(
    const QVector3D *eulerRotation,
    const RotationData *a) {
  return operator!=(*eulerRotation, *a);
}

//  bool operator==(const RotationData &a, const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12RotationDataRK11QQuaternion(
    const RotationData *a,
    const QQuaternion *rotation) {
  return operator==(*a, *rotation);
}

//  bool operator!=(const RotationData &a, const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12RotationDataRK11QQuaternion(
    const RotationData *a,
    const QQuaternion *rotation) {
  return operator!=(*a, *rotation);
}

//  bool operator==(const QQuaternion &rotation, const RotationData &a)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QQuaternionRK12RotationData(
    const QQuaternion *rotation,
    const RotationData *a) {
  return operator==(*rotation, *a);
}

//  bool operator!=(const QQuaternion &rotation, const RotationData &a)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QQuaternionRK12RotationData(
    const QQuaternion *rotation,
    const RotationData *a) {
  return operator!=(*rotation, *a);
}

//  QVector3D RotationData::toEulerAngles() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12RotationData13toEulerAnglesEv(
    const RotationData *self) {
  return new QVector3D(self->toEulerAngles());
}

//  QQuaternion RotationData::toQuaternion() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK12RotationData12toQuaternionEv(
    const RotationData *self) {
  return new QQuaternion(self->toQuaternion());
}

//  double RotationData::dotProduct(const QQuaternion &q1, const QQuaternion
//      &q2)
extern "C" Q_DECL_EXPORT
double ritual_ZN12RotationData10dotProductERK11QQuaternionS2_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return RotationData::dotProduct(*q1, *q2);
}

//  bool RotationData::fuzzyQuaternionCompare(const QQuaternion &a, const
//      QQuaternion &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12RotationData22fuzzyQuaternionCompareERK11QQuaternionS2_(
    const QQuaternion *a,
    const QQuaternion *b) {
  return RotationData::fuzzyQuaternionCompare(*a, *b);
}

//  RotationData::~RotationData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12RotationDataD1Ev(RotationData *self) {
  delete self;
}
