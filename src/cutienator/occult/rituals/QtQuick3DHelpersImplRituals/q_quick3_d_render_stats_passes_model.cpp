//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  qquick3drenderstatspassesmodel_p.h, Qt 6.12.0.
//  Kept as it is when the generator runs again.
//  Not written: the constructor and 'tr'; roleNames, which returns a
//  QHash; passData and setPassData, which are not virtual; the signal
//  passDataChanged. Qt's library offers nothing of this class by name:
//  only its virtual functions are called, through the object.
#include <QtQuick3DHelpersImpl/qtquick3dhelpersimplversion.h>
#include <QtCore/qobject.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/qquick3drenderstatspassesmodel_p.h>

//  const QMetaObject *QQuick3DRenderStatsPassesModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuick3DRenderStatsPassesModel10metaObjectEv(
    const QQuick3DRenderStatsPassesModel *self) {
  return self->metaObject();
}

//  QQuick3DRenderStatsPassesModel::~QQuick3DRenderStatsPassesModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DRenderStatsPassesModelD1Ev(
    QQuick3DRenderStatsPassesModel *self) {
  delete self;
}

//  int QQuick3DRenderStatsPassesModel::rowCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DRenderStatsPassesModel8rowCountERK11QModelIndex(
    const QQuick3DRenderStatsPassesModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQuick3DRenderStatsPassesModel::columnCount(
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DRenderStatsPassesModel11columnCountERK11QModelIndex(
    const QQuick3DRenderStatsPassesModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QQuick3DRenderStatsPassesModel::data(
//      const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QQuick3DRenderStatsPassesModel4dataERK11QModelIndexi(
    const QQuick3DRenderStatsPassesModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QVariant QQuick3DRenderStatsPassesModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QQuick3DRenderStatsPassesModel10headerDataEiN2Qt11OrientationEi(
    const QQuick3DRenderStatsPassesModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->headerData(section, orientation, role));
}
