//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *ProceduralMeshSubset::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20ProceduralMeshSubset10metaObjectEv(
    const ProceduralMeshSubset *self) {
  return self->metaObject();
}

//  QString ProceduralMeshSubset::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20ProceduralMeshSubset2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ProceduralMeshSubset::tr(s, c, n));
}

//  int ProceduralMeshSubset::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20ProceduralMeshSubset6offsetEv(
    const ProceduralMeshSubset *self) {
  return self->offset();
}

//  void ProceduralMeshSubset::setOffset(int newOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ProceduralMeshSubset9setOffsetEi(
    ProceduralMeshSubset *self,
    int newOffset) {
  self->setOffset(newOffset);
}

//  int ProceduralMeshSubset::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20ProceduralMeshSubset5countEv(
    const ProceduralMeshSubset *self) {
  return self->count();
}

//  void ProceduralMeshSubset::setCount(int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ProceduralMeshSubset8setCountEi(
    ProceduralMeshSubset *self,
    int newCount) {
  self->setCount(newCount);
}

//  QString ProceduralMeshSubset::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20ProceduralMeshSubset4nameEv(
    const ProceduralMeshSubset *self) {
  return new QString(self->name());
}

//  void ProceduralMeshSubset::setName(const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ProceduralMeshSubset7setNameERK7QString(
    ProceduralMeshSubset *self,
    const QString *newName) {
  self->setName(*newName);
}
