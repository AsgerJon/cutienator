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
#include <QtQuick3DXr/private/qquick3dxrspatialanchorlistmodel_p.h>
#include <QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxranchormanager_visionos_p.h"
#else
#endif
#include <QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxranchormanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 44, as local:qquick3dxrspatialanchorlistmodel.cpp:getClassificationString
static QString getClassificationString(QQuick3DXrSpatialAnchorListModel::ClassificationFlag classification)
{
    switch (classification) {
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Wall:
            return QStringLiteral("wall");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Ceiling:
            return QStringLiteral("ceiling");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Floor:
            return QStringLiteral("floor");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Table:
            return QStringLiteral("table");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Seat:
            return QStringLiteral("seat");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Window:
            return QStringLiteral("window");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Door:
            return QStringLiteral("door");
        case QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Other:
            return QStringLiteral("other");
    }

    return {};
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 68, as local:qquick3dxrspatialanchorlistmodel.cpp:getClassificationFlagType
static QQuick3DXrSpatialAnchorListModel::ClassificationFlag getClassificationFlagType(QQuick3DXrSpatialAnchor::Classification classification)
{
    switch (classification) {
        case QQuick3DXrSpatialAnchor::Classification::Unknown:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Other;
        case QQuick3DXrSpatialAnchor::Classification::Wall:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Wall;
        case QQuick3DXrSpatialAnchor::Classification::Ceiling:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Ceiling;
        case QQuick3DXrSpatialAnchor::Classification::Floor:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Floor;
        case QQuick3DXrSpatialAnchor::Classification::Table:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Table;
        case QQuick3DXrSpatialAnchor::Classification::Seat:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Seat;
        case QQuick3DXrSpatialAnchor::Classification::Window:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Window;
        case QQuick3DXrSpatialAnchor::Classification::Door:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Door;
        case QQuick3DXrSpatialAnchor::Classification::Other:
            return QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Other;
    }

        Q_UNREACHABLE_RETURN(QQuick3DXrSpatialAnchorListModel::ClassificationFlag::Other);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 185, as _ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorRemovedE5QUuid
inline void QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)
{
    Q_UNUSED(uuid)
    // Brute Force :-p
    beginResetModel();
    endResetModel();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 390, as _ZNK23QQuick3DXrSpatialAnchor10identifierEv
inline QString QQuick3DXrSpatialAnchor::identifier() const
{
    return QString::fromLatin1(m_uuid.toRfc4122());
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 243, as _ZNK23QQuick3DXrSpatialAnchor14classificationEv
inline QQuick3DXrSpatialAnchor::Classification QQuick3DXrSpatialAnchor::classification() const
{
    return m_classification;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 271, as _ZNK23QQuick3DXrSpatialAnchor20classificationStringEv
inline QString QQuick3DXrSpatialAnchor::classificationString() const
{
    return m_classificationString;
}

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

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchorlistmodel.cpp, line 330, as _ZNK32QQuick3DXrSpatialAnchorListModel19matchesAnchorFilterEP23QQuick3DXrSpatialAnchor
inline bool QQuick3DXrSpatialAnchorListModel::matchesAnchorFilter(QQuick3DXrSpatialAnchor *anchor) const
{
    if (m_filterMode == FilterMode::Classification) {
        QString classificationString;
        const auto classification = anchor->classification();
        if (classification != QQuick3DXrSpatialAnchor::Classification::Other) {
            const auto classificationFlagType = getClassificationFlagType(classification);
            classificationString = getClassificationString(classificationFlagType);
        } else {
            // NOTE: Other can mean there is no classification or the classification is not one that
            // we have defined in our enums, so we will use the string as the user can specify any string.
            classificationString = anchor->classificationString().toLower();
        }
        return m_classStringFilter.contains(classificationString.toLower());
    } else if (m_filterMode == FilterMode::Identifier) {
        const auto uuid = anchor->identifier();
        return m_uuids.contains(uuid);
    }

    // 'All' mode
    return true;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrSpatialAnchorListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuick3DXrSpatialAnchorListModel10metaObjectEv(
    const QQuick3DXrSpatialAnchorListModel *self) {
  return self->metaObject();
}

//  void *QQuick3DXrSpatialAnchorListModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuick3DXrSpatialAnchorListModel11qt_metacastEPKc(
    QQuick3DXrSpatialAnchorListModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrSpatialAnchorListModel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuick3DXrSpatialAnchorListModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrSpatialAnchorListModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuick3DXrSpatialAnchorListModel::requestSceneCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel19requestSceneCaptureEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestSceneCapture()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestSceneCapture()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::queryAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel12queryAnchorsEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "queryAnchors()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "queryAnchors()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

//  void QQuick3DXrSpatialAnchorListModel::filterModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel17filterModeChangedEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filterModeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filterModeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::identifierFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel23identifierFilterChangedEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "identifierFilterChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "identifierFilterChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::classificationFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel27classificationFilterChangedEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "classificationFilterChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "classificationFilterChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QQuick3DXrSpatialAnchorListModel::classificationStringFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel33classificationStringFilterChangedEv(
    QQuick3DXrSpatialAnchorListModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "classificationStringFilterChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "classificationStringFilterChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::handleAnchorAdded(QQuick3DXrSpatia
//      lAnchor *anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel17handleAnchorAddedEP23QQuick3DXrSpatialAnchor(
    QQuick3DXrSpatialAnchorListModel *self,
    QQuick3DXrSpatialAnchor *anchor) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleAnchorAdded(QQuick3DXrSpatialAnchor *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleAnchorAdded(QQuick3DXrSpatialAnchor *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&anchor)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorRemovedE5QUuid(
    QQuick3DXrSpatialAnchorListModel *self,
    const QUuid *uuid) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleAnchorRemoved(QUuid)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleAnchorRemoved(QUuid)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(uuid)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSpatialAnchorListModel::handleAnchorUpdated(QQuick3DXrSpat
//      ialAnchor *anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorUpdatedEP23QQuick3DXrSpatialAnchor(
    QQuick3DXrSpatialAnchorListModel *self,
    QQuick3DXrSpatialAnchor *anchor) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSpatialAnchorListModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleAnchorUpdated(QQuick3DXrSpatialAnchor *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleAnchorUpdated(QQuick3DXrSpatialAnchor *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&anchor)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QQuick3DXrSpatialAnchorListModel::matchesAnchorFilter(QQuick3DXrSpat
//      ialAnchor *anchor) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuick3DXrSpatialAnchorListModel19matchesAnchorFilterEP23QQuick3DXrSpatialAnchor(
    const QQuick3DXrSpatialAnchorListModel *self,
    QQuick3DXrSpatialAnchor *anchor) {
  return self->matchesAnchorFilter(anchor);
}
