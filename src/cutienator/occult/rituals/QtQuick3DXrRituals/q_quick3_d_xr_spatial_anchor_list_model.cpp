//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxrspatialanchorlistmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchorlistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/quuid.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dxrspatialanchorlistmodel_p.h"
#include "qquick3dxrspatialanchor_p.h"
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxranchormanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 109, as _ZNK32QQuick3DXrSpatialAnchorListModel8rowCountERK11QModelIndex
inline int QQuick3DXrSpatialAnchorListModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid() || m_anchorManager == nullptr)
        return 0;

    const auto &anchors = anchorsFiltered();

    return anchors.size();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 119, as _ZNK32QQuick3DXrSpatialAnchorListModel4dataERK11QModelIndexi
inline QVariant QQuick3DXrSpatialAnchorListModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || m_anchorManager == nullptr)
        return QVariant();

    const auto &anchors = anchorsFiltered();

    // check bounds
    if (index.row() < 0 || index.row() >= anchors.count())
        return QVariant();

    const auto &anchor = anchors.at(index.row());

    if (role == Anchor)
        return QVariant::fromValue(anchor);

    // shouldn't be reachable under normal circumstances.
    return QVariant();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 139, as _ZNK32QQuick3DXrSpatialAnchorListModel9roleNamesEv
inline QHash<int, QByteArray> QQuick3DXrSpatialAnchorListModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[Anchor] = "anchor";
    return roles;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 214, as _ZNK32QQuick3DXrSpatialAnchorListModel10filterModeEv
inline QQuick3DXrSpatialAnchorListModel::FilterMode QQuick3DXrSpatialAnchorListModel::filterMode() const
{
    return m_filterMode;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 236, as _ZNK32QQuick3DXrSpatialAnchorListModel16identifierFilterEv
inline QStringList QQuick3DXrSpatialAnchorListModel::identifierFilter() const
{
    return m_uuids.values();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 272, as _ZNK32QQuick3DXrSpatialAnchorListModel20classificationFilterEv
inline QQuick3DXrSpatialAnchorListModel::ClassificationFlags QQuick3DXrSpatialAnchorListModel::classificationFilter() const
{
    return m_classFilter;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 312, as _ZNK32QQuick3DXrSpatialAnchorListModel26classificationStringFilterEv
inline QStringList QQuick3DXrSpatialAnchorListModel::classificationStringFilter() const
{
    return m_classStringFilter.values();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 185, as _ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorRemovedE5QUuid
inline void QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)
{
    Q_UNUSED(uuid)
    // Brute Force :-p
    beginResetModel();
    endResetModel();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrSpatialAnchorListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuick3DXrSpatialAnchorListModel10metaObjectEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return self->metaObject();
}

//  int QQuick3DXrSpatialAnchorListModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuick3DXrSpatialAnchorListModel8rowCountERK11QModelIndex(
    const QQuick3DXrSpatialAnchorListModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QQuick3DXrSpatialAnchorListModel::data(const QModelIndex &index,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK32QQuick3DXrSpatialAnchorListModel4dataERK11QModelIndexi(
    const QQuick3DXrSpatialAnchorListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QQuick3DXrSpatialAnchorListModel::roleNames()
//      const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK32QQuick3DXrSpatialAnchorListModel9roleNamesEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  FilterMode QQuick3DXrSpatialAnchorListModel::filterMode() const
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchorListModel::FilterMode ritual_ZNK32QQuick3DXrSpatialAnchorListModel10filterModeEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return self->filterMode();
}

//  QStringList QQuick3DXrSpatialAnchorListModel::identifierFilter() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuick3DXrSpatialAnchorListModel16identifierFilterEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return new QList<QString>(self->identifierFilter());
}

//  ClassificationFlags
//      QQuick3DXrSpatialAnchorListModel::classificationFilter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuick3DXrSpatialAnchorListModel20classificationFilterEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return static_cast<int>(self->classificationFilter().toInt());
}

//  QStringList
//      QQuick3DXrSpatialAnchorListModel::classificationStringFilter() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuick3DXrSpatialAnchorListModel26classificationStringFilterEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return new QList<QString>(self->classificationStringFilter());
}

//  void QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorRemovedE5QUuid(
    QQuick3DXrSpatialAnchorListModel *self,
    const QUuid *uuid) {
  self->handleAnchorRemoved(*uuid);
}
