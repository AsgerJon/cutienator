//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtQml/QQmlListProperty>

//  const QMetaObject *ProceduralMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14ProceduralMesh10metaObjectEv(
    const ProceduralMesh *self) {
  return self->metaObject();
}

//  void *ProceduralMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14ProceduralMesh11qt_metacastEPKc(
    ProceduralMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ProceduralMesh::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14ProceduralMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    ProceduralMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ProceduralMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14ProceduralMesh2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ProceduralMesh::tr(s, c, n));
}

//  ProceduralMesh::ProceduralMesh()
extern "C" Q_DECL_EXPORT
ProceduralMesh *ritual_ZN14ProceduralMeshC1Ev() {
  return new ProceduralMesh();
}

//  QList<QVector3D> ProceduralMesh::positions() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK14ProceduralMesh9positionsEv(
    const ProceduralMesh *self) {
  return new QList<QVector3D>(self->positions());
}

//  void ProceduralMesh::setPositions(const QList<QVector3D> &newPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh12setPositionsERK5QListI9QVector3DE(
    ProceduralMesh *self,
    const QList<QVector3D> *newPositions) {
  self->setPositions(*newPositions);
}

//  PrimitiveMode ProceduralMesh::primitiveMode() const
extern "C" Q_DECL_EXPORT
ProceduralMesh::PrimitiveMode ritual_ZNK14ProceduralMesh13primitiveModeEv(
    const ProceduralMesh *self) {
  return self->primitiveMode();
}

//  void ProceduralMesh::setPrimitiveMode(PrimitiveMode newPrimitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh16setPrimitiveModeENS_13PrimitiveModeE(
    ProceduralMesh *self,
    ProceduralMesh::PrimitiveMode newPrimitiveMode) {
  self->setPrimitiveMode(newPrimitiveMode);
}

//  QList<unsigned int> ProceduralMesh::indexes() const
extern "C" Q_DECL_EXPORT
QList<unsigned int> *ritual_ZNK14ProceduralMesh7indexesEv(
    const ProceduralMesh *self) {
  return new QList<unsigned int>(self->indexes());
}

//  void ProceduralMesh::setIndexes(const QList<unsigned int> &newIndexes)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh10setIndexesERK5QListIjE(
    ProceduralMesh *self,
    const QList<unsigned int> *newIndexes) {
  self->setIndexes(*newIndexes);
}

//  QList<QVector3D> ProceduralMesh::normals() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK14ProceduralMesh7normalsEv(
    const ProceduralMesh *self) {
  return new QList<QVector3D>(self->normals());
}

//  void ProceduralMesh::setNormals(const QList<QVector3D> &newNormals)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh10setNormalsERK5QListI9QVector3DE(
    ProceduralMesh *self,
    const QList<QVector3D> *newNormals) {
  self->setNormals(*newNormals);
}

//  QList<QVector3D> ProceduralMesh::tangents() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK14ProceduralMesh8tangentsEv(
    const ProceduralMesh *self) {
  return new QList<QVector3D>(self->tangents());
}

//  void ProceduralMesh::setTangents(const QList<QVector3D> &newTangents)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh11setTangentsERK5QListI9QVector3DE(
    ProceduralMesh *self,
    const QList<QVector3D> *newTangents) {
  self->setTangents(*newTangents);
}

//  QList<QVector3D> ProceduralMesh::binormals() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK14ProceduralMesh9binormalsEv(
    const ProceduralMesh *self) {
  return new QList<QVector3D>(self->binormals());
}

//  void ProceduralMesh::setBinormals(const QList<QVector3D> &newBinormals)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh12setBinormalsERK5QListI9QVector3DE(
    ProceduralMesh *self,
    const QList<QVector3D> *newBinormals) {
  self->setBinormals(*newBinormals);
}

//  QList<QVector2D> ProceduralMesh::uv0s() const
extern "C" Q_DECL_EXPORT
QList<QVector2D> *ritual_ZNK14ProceduralMesh4uv0sEv(
    const ProceduralMesh *self) {
  return new QList<QVector2D>(self->uv0s());
}

//  void ProceduralMesh::setUv0s(const QList<QVector2D> &newUv0s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh7setUv0sERK5QListI9QVector2DE(
    ProceduralMesh *self,
    const QList<QVector2D> *newUv0s) {
  self->setUv0s(*newUv0s);
}

//  QList<QVector2D> ProceduralMesh::uv1s() const
extern "C" Q_DECL_EXPORT
QList<QVector2D> *ritual_ZNK14ProceduralMesh4uv1sEv(
    const ProceduralMesh *self) {
  return new QList<QVector2D>(self->uv1s());
}

//  void ProceduralMesh::setUv1s(const QList<QVector2D> &newUv1s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh7setUv1sERK5QListI9QVector2DE(
    ProceduralMesh *self,
    const QList<QVector2D> *newUv1s) {
  self->setUv1s(*newUv1s);
}

//  QList<QVector4D> ProceduralMesh::colors() const
extern "C" Q_DECL_EXPORT
QList<QVector4D> *ritual_ZNK14ProceduralMesh6colorsEv(
    const ProceduralMesh *self) {
  return new QList<QVector4D>(self->colors());
}

//  void ProceduralMesh::setColors(const QList<QVector4D> &newColors)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh9setColorsERK5QListI9QVector4DE(
    ProceduralMesh *self,
    const QList<QVector4D> *newColors) {
  self->setColors(*newColors);
}

//  QList<QVector4D> ProceduralMesh::joints() const
extern "C" Q_DECL_EXPORT
QList<QVector4D> *ritual_ZNK14ProceduralMesh6jointsEv(
    const ProceduralMesh *self) {
  return new QList<QVector4D>(self->joints());
}

//  void ProceduralMesh::setJoints(const QList<QVector4D> &newJoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh9setJointsERK5QListI9QVector4DE(
    ProceduralMesh *self,
    const QList<QVector4D> *newJoints) {
  self->setJoints(*newJoints);
}

//  QList<QVector4D> ProceduralMesh::weights() const
extern "C" Q_DECL_EXPORT
QList<QVector4D> *ritual_ZNK14ProceduralMesh7weightsEv(
    const ProceduralMesh *self) {
  return new QList<QVector4D>(self->weights());
}

//  void ProceduralMesh::setWeights(const QList<QVector4D> &newWeights)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh10setWeightsERK5QListI9QVector4DE(
    ProceduralMesh *self,
    const QList<QVector4D> *newWeights) {
  self->setWeights(*newWeights);
}

//  QQmlListProperty<ProceduralMeshSubset> ProceduralMesh::subsets()
extern "C" Q_DECL_EXPORT
QQmlListProperty<ProceduralMeshSubset> *ritual_ZN14ProceduralMesh7subsetsEv(
    ProceduralMesh *self) {
  return new QQmlListProperty<ProceduralMeshSubset>(self->subsets());
}

//  void ProceduralMesh::positionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh16positionsChangedEv(ProceduralMesh *self) {
  self->positionsChanged();
}

//  void ProceduralMesh::primitiveModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh20primitiveModeChangedEv(
    ProceduralMesh *self) {
  self->primitiveModeChanged();
}

//  void ProceduralMesh::indexesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh14indexesChangedEv(ProceduralMesh *self) {
  self->indexesChanged();
}

//  void ProceduralMesh::normalsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh14normalsChangedEv(ProceduralMesh *self) {
  self->normalsChanged();
}

//  void ProceduralMesh::tangentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh15tangentsChangedEv(ProceduralMesh *self) {
  self->tangentsChanged();
}

//  void ProceduralMesh::binormalsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh16binormalsChangedEv(ProceduralMesh *self) {
  self->binormalsChanged();
}

//  void ProceduralMesh::uv0sChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh11uv0sChangedEv(ProceduralMesh *self) {
  self->uv0sChanged();
}

//  void ProceduralMesh::uv1sChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh11uv1sChangedEv(ProceduralMesh *self) {
  self->uv1sChanged();
}

//  void ProceduralMesh::colorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh13colorsChangedEv(ProceduralMesh *self) {
  self->colorsChanged();
}

//  void ProceduralMesh::jointsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh13jointsChangedEv(ProceduralMesh *self) {
  self->jointsChanged();
}

//  void ProceduralMesh::weightsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh14weightsChangedEv(ProceduralMesh *self) {
  self->weightsChanged();
}

//  void ProceduralMesh::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh13requestUpdateEv(ProceduralMesh *self) {
  self->requestUpdate();
}

//  void ProceduralMesh::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh14updateGeometryEv(ProceduralMesh *self) {
  self->updateGeometry();
}

//  void ProceduralMesh::subsetDestroyed(QObject *subset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh15subsetDestroyedEP7QObject(
    ProceduralMesh *self,
    QObject *subset) {
  self->subsetDestroyed(subset);
}

//  bool ProceduralMesh::supportsTriangleFanPrimitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ProceduralMesh28supportsTriangleFanPrimitiveEv(
    const ProceduralMesh *self) {
  return self->supportsTriangleFanPrimitive();
}

//  void ProceduralMesh::qmlAppendProceduralMeshSubset(QQmlListProperty<Proce
//      duralMeshSubset> *list, ProceduralMeshSubset *subset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh29qmlAppendProceduralMeshSubsetEP16QQmlListPropertyI20ProceduralMeshSubsetEPS1_(
    QQmlListProperty<ProceduralMeshSubset> *list,
    ProceduralMeshSubset *subset) {
  ProceduralMesh::qmlAppendProceduralMeshSubset(list, subset);
}

//  ProceduralMeshSubset *ProceduralMesh::qmlProceduralMeshSubsetAt(QQmlListP
//      roperty<ProceduralMeshSubset> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
ProceduralMeshSubset *ritual_ZN14ProceduralMesh25qmlProceduralMeshSubsetAtEP16QQmlListPropertyI20ProceduralMeshSubsetEx(
    QQmlListProperty<ProceduralMeshSubset> *list,
    qsizetype index) {
  return ProceduralMesh::qmlProceduralMeshSubsetAt(list, index);
}

//  qsizetype ProceduralMesh::qmlProceduralMeshSubsetCount(QQmlListProperty<P
//      roceduralMeshSubset> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14ProceduralMesh28qmlProceduralMeshSubsetCountEP16QQmlListPropertyI20ProceduralMeshSubsetE(
    QQmlListProperty<ProceduralMeshSubset> *list) {
  return ProceduralMesh::qmlProceduralMeshSubsetCount(list);
}

//  void ProceduralMesh::qmlClearProceduralMeshSubset(QQmlListProperty<Proced
//      uralMeshSubset> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ProceduralMesh28qmlClearProceduralMeshSubsetEP16QQmlListPropertyI20ProceduralMeshSubsetE(
    QQmlListProperty<ProceduralMeshSubset> *list) {
  ProceduralMesh::qmlClearProceduralMeshSubset(list);
}

//  a QList<unsigned int> a ritual of ProceduralMesh gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ProceduralMesh__QList_unsigned_int(
    QList<unsigned int> *self) {
  delete self;
}

//  a QQmlListProperty<ProceduralMeshSubset> a ritual of ProceduralMesh gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ProceduralMesh__QQmlListProperty_ProceduralMeshSubset(
    QQmlListProperty<ProceduralMeshSubset> *self) {
  delete self;
}
