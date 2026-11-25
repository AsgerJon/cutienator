//  Written by hand on 2026-11-25 from
//  QtQuick3DPhysicsHelpers/6.12.0/QtQuick3DPhysicsHelpers/private/
//  qcapsulegeometry_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  The class line has no export macro (the part is made with
//  NO_GENERATE_CPP_EXPORTS), so Qt's library offers nothing of this
//  class by name: only its inline functions are written, and its
//  virtual functions, called through the object: metaObject() and the
//  implicit destructor, virtual through QObject.
//  Not written: the constructor and 'tr'; the setters, which are
//  defined outside the header; the signals; the private updateData,
//  neither inline nor virtual.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3DPhysicsHelpers/6.12.0/QtQuick3DPhysicsHelpers/private/qcapsulegeometry_p.h>

//  const QMetaObject *CapsuleGeometryPhysics::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22CapsuleGeometryPhysics10metaObjectEv(
    const CapsuleGeometryPhysics *self) {
  return self->metaObject();
}

//  CapsuleGeometryPhysics::~CapsuleGeometryPhysics()
extern "C" Q_DECL_EXPORT
void ritual_ZN22CapsuleGeometryPhysicsD1Ev(CapsuleGeometryPhysics *self) {
  delete self;
}

//  bool CapsuleGeometryPhysics::enableNormals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22CapsuleGeometryPhysics13enableNormalsEv(
    const CapsuleGeometryPhysics *self) {
  return self->enableNormals();
}

//  bool CapsuleGeometryPhysics::enableUV() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22CapsuleGeometryPhysics8enableUVEv(
    const CapsuleGeometryPhysics *self) {
  return self->enableUV();
}

//  int CapsuleGeometryPhysics::longitudes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22CapsuleGeometryPhysics10longitudesEv(
    const CapsuleGeometryPhysics *self) {
  return self->longitudes();
}

//  int CapsuleGeometryPhysics::latitudes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22CapsuleGeometryPhysics9latitudesEv(
    const CapsuleGeometryPhysics *self) {
  return self->latitudes();
}

//  int CapsuleGeometryPhysics::rings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22CapsuleGeometryPhysics5ringsEv(
    const CapsuleGeometryPhysics *self) {
  return self->rings();
}

//  float CapsuleGeometryPhysics::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22CapsuleGeometryPhysics6heightEv(
    const CapsuleGeometryPhysics *self) {
  return self->height();
}

//  float CapsuleGeometryPhysics::diameter() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22CapsuleGeometryPhysics8diameterEv(
    const CapsuleGeometryPhysics *self) {
  return self->diameter();
}
