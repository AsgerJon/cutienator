//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  qquick3drenderstatsmeshesmodel_p.h, Qt 6.12.0. Kept as it is
//  when the generator runs again.
//  The class line has no export macro, so Qt's library offers
//  nothing of this class by name: only its virtual functions are
//  written, called through the object, and the implicit destructor,
//  which is virtual, called through 'delete'.
//  Not written: the constructor, 'roleNames' (it returns a QHash),
//  the non-virtual 'meshData' and 'setMeshData', the signal
//  'meshDataChanged', and the macros Q_OBJECT, Q_PROPERTY and
//  QML_NAMED_ELEMENT.
#include <QtCore/qglobal.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qnamespace.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/qquick3drenderstatsmeshesmodel_p.h>

//  QQuick3DRenderStatsMeshesModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuick3DRenderStatsMeshesModel10metaObjectEv(
    const QQuick3DRenderStatsMeshesModel *self) {
  return self->metaObject();
}

//  QQuick3DRenderStatsMeshesModel::~QQuick3DRenderStatsMeshesModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DRenderStatsMeshesModelD1Ev(
    QQuick3DRenderStatsMeshesModel *self) {
  delete self;
}

//  int QQuick3DRenderStatsMeshesModel::rowCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DRenderStatsMeshesModel8rowCountERK11QModelIndex(
    const QQuick3DRenderStatsMeshesModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQuick3DRenderStatsMeshesModel::columnCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DRenderStatsMeshesModel11columnCountERK11QModelIndex(
    const QQuick3DRenderStatsMeshesModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QQuick3DRenderStatsMeshesModel::data(
//      const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QQuick3DRenderStatsMeshesModel4dataERK11QModelIndexi(
    const QQuick3DRenderStatsMeshesModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QVariant QQuick3DRenderStatsMeshesModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QQuick3DRenderStatsMeshesModel10headerDataEiN2Qt11OrientationEi(
    const QQuick3DRenderStatsMeshesModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->headerData(section, orientation, role));
}
