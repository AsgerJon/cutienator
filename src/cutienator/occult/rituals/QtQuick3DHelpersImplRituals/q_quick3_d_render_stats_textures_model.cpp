//  Written by hand on 2026-11-25 from the header path as installed,
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  qquick3drenderstatstexturesmodel_p.h, Qt 6.12.0, as the Linux kit
//  installs it. Kept as it is when the generator runs again.
//  The class has no Q_..._EXPORT macro, so Qt's library offers nothing
//  of it by name: only its virtual functions are called, through the
//  object. Not written: the constructor (none is declared here) and
//  'tr'; 'roleNames' (returns a QHash); 'textureData' and
//  'setTextureData' (not virtual, defined outside the header); the
//  signal 'textureDataChanged'. The destructor is implicit in the
//  header and is written as the virtual destructor it inherits.
#include <QtCore/qglobal.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/qquick3drenderstatstexturesmodel_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QQuick3DRenderStatsTexturesModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuick3DRenderStatsTexturesModel10metaObjectEv(
    const QQuick3DRenderStatsTexturesModel *self) {
  return self->metaObject();
}

//  QQuick3DRenderStatsTexturesModel::~QQuick3DRenderStatsTexturesModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DRenderStatsTexturesModelD1Ev(
    QQuick3DRenderStatsTexturesModel *self) {
  delete self;
}

//  int QQuick3DRenderStatsTexturesModel::rowCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuick3DRenderStatsTexturesModel8rowCountERK11QModelIndex(
    const QQuick3DRenderStatsTexturesModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQuick3DRenderStatsTexturesModel::columnCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuick3DRenderStatsTexturesModel11columnCountERK11QModelIndex(
    const QQuick3DRenderStatsTexturesModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QQuick3DRenderStatsTexturesModel::data(
//      const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK32QQuick3DRenderStatsTexturesModel4dataERK11QModelIndexi(
    const QQuick3DRenderStatsTexturesModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QVariant QQuick3DRenderStatsTexturesModel::headerData(
//      int section, Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK32QQuick3DRenderStatsTexturesModel10headerDataEiN2Qt11OrientationEi(
    const QQuick3DRenderStatsTexturesModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}
