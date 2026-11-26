//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QList>
#include <QtCore/QSize>
#include <QtCore/QVariant>
#include <QtCore/Qt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qitemselectionmodel.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 9, as local:qremoteobjectabstractitemmodeladapter.cpp:createModelRoleData
inline QList<QModelRoleData> createModelRoleData(const QList<int> &roles)
{
    QList<QModelRoleData> roleData;
    roleData.reserve(roles.size());
    for (int role : roles)
        roleData.emplace_back(role);
    return roleData;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 19, as local:qremoteobjectabstractitemmodeladapter.cpp:collectData
inline QVariantList collectData(const QModelIndex &index, const QAbstractItemModel *model,
                                QModelRoleDataSpan roleDataSpan)
{
    model->multiData(index, roleDataSpan);

    QVariantList result;
    result.reserve(roleDataSpan.size());
    for (auto &roleData : roleDataSpan)
        result.push_back(std::move(roleData.data()));

    return result;
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 14, as _Z22QT_REMOTEOBJECT_MODELSv
inline const QLoggingCategory &QT_REMOTEOBJECT_MODELS()
{
    static const QLoggingCategory category("qt.remoteobjects.models", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 236, as _ZN31QAbstractItemModelSourceAdapter9fetchTreeERK11QModelIndexRmRK5QListIiE
inline QList<QtPrivate::IndexValuePair> QAbstractItemModelSourceAdapter::fetchTree(const QModelIndex &parent, size_t &size, const QList<int> &roles)
{
    QList<QtPrivate::IndexValuePair> entries;
    const int rowCount = m_model->rowCount(parent);
    const int columnCount = m_model->columnCount(parent);
    if (!columnCount || !rowCount)
        return entries;
    entries.reserve(std::min(rowCount * columnCount, int(size)));
    auto roleData = createModelRoleData(roles);
    for (int row = 0; row < rowCount && size > 0; ++row)
        for (int column = 0; column < columnCount && size > 0; ++column) {
            const auto index = m_model->index(row, column, parent);
            const QtPrivate::IndexList currentList = QtPrivate::toModelIndexList(index, m_model);
            const QVariantList data = collectData(index, m_model, roleData);
            const bool hasChildren = m_model->hasChildren(index);
            const Qt::ItemFlags flags = m_model->flags(index);
            int rc = m_model->rowCount(index);
            int cc = m_model->columnCount(index);
            QtPrivate::IndexValuePair rowData(currentList, data, hasChildren, flags, QSize{cc, rc});
            --size;
            if (hasChildren)
                rowData.children = fetchTree(index, size, roles);
            entries.push_back(rowData);
        }
    return entries;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 85, as _ZNK31QAbstractItemModelSourceAdapter14selectionModelEv
inline QItemSelectionModel* QAbstractItemModelSourceAdapter::selectionModel() const
{
    return m_selectionModel;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 90, as _ZN31QAbstractItemModelSourceAdapter18replicaSizeRequestE5QListIN9QtPrivate10ModelIndexEE
inline QSize QAbstractItemModelSourceAdapter::replicaSizeRequest(QtPrivate::IndexList parentList)
{
    QModelIndex parent = toQModelIndex(parentList, m_model);
    const int rowCount = m_model->rowCount(parent);
    const int columnCount = m_model->columnCount(parent);
    const QSize size(columnCount, rowCount);
    qCDebug(QT_REMOTEOBJECT_MODELS) << "parent" << parentList << "size=" << size;
    return size;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 109, as _ZN31QAbstractItemModelSourceAdapter17replicaRowRequestE5QListIN9QtPrivate10ModelIndexEES3_S0_IiE
inline QtPrivate::DataEntries QAbstractItemModelSourceAdapter::replicaRowRequest(QtPrivate::IndexList start, QtPrivate::IndexList end, QList<int> roles)
{
    qCDebug(QT_REMOTEOBJECT_MODELS) << "Requested rows" << "start=" << start << "end=" << end << "roles=" << roles;

    Q_ASSERT(start.size() == end.size());
    Q_ASSERT(!start.isEmpty());

    if (roles.isEmpty())
        roles << m_availableRoles;

    QtPrivate::IndexList parentList = start;
    Q_ASSERT(!parentList.isEmpty());
    parentList.pop_back();
    QModelIndex parent = toQModelIndex(parentList, m_model);

    const int startRow = start.last().row;
    const int startColumn = start.last().column;
    const int rowCount = m_model->rowCount(parent);
    const int columnCount = m_model->columnCount(parent);

    QtPrivate::DataEntries entries;
    if (rowCount <= 0)
        return entries;
    const int endRow = std::min(end.last().row, rowCount - 1);
    const int endColumn = std::min(end.last().column, columnCount - 1);
    Q_ASSERT_X(endRow >= 0 && endRow < rowCount, __FUNCTION__, qPrintable(QString(QLatin1String("0 <= %1 < %2")).arg(endRow).arg(rowCount)));
    Q_ASSERT_X(endColumn >= 0 && endColumn < columnCount, __FUNCTION__, qPrintable(QString(QLatin1String("0 <= %1 < %2")).arg(endColumn).arg(columnCount)));

    auto roleData = createModelRoleData(roles);
    for (int row = startRow; row <= endRow; ++row) {
        for (int column = startColumn; column <= endColumn; ++column) {
            const QModelIndex current = m_model->index(row, column, parent);
            Q_ASSERT(current.isValid());
            const QtPrivate::IndexList currentList = QtPrivate::toModelIndexList(current, m_model);
            const QVariantList data = collectData(current, m_model, roleData);
            const bool hasChildren = m_model->hasChildren(current);
            const Qt::ItemFlags flags = m_model->flags(current);
            qCDebug(QT_REMOTEOBJECT_MODELS) << Q_FUNC_INFO << "current=" << currentList << "data=" << data;
            entries.data << QtPrivate::IndexValuePair(currentList, data, hasChildren, flags);
        }
    }
    return entries;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 164, as _ZN31QAbstractItemModelSourceAdapter20replicaHeaderRequestE5QListIN2Qt11OrientationEES0_IiES4_
inline QVariantList QAbstractItemModelSourceAdapter::replicaHeaderRequest(QList<Qt::Orientation> orientations, QList<int> sections, QList<int> roles)
{
    qCDebug(QT_REMOTEOBJECT_MODELS) << Q_FUNC_INFO << "orientations=" << orientations << "sections=" << sections << "roles=" << roles;
    QVariantList data;
    Q_ASSERT(roles.size() == sections.size());
    Q_ASSERT(roles.size() == orientations.size());
    for (int i = 0; i < roles.size(); ++i) {
        data << m_model->headerData(sections[i], orientations[i], roles[i]);
    }
    return data;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 153, as _ZN31QAbstractItemModelSourceAdapter19replicaCacheRequestEmRK5QListIiE
inline QtPrivate::MetaAndDataEntries QAbstractItemModelSourceAdapter::replicaCacheRequest(size_t size, const QList<int> &roles)
{
    QtPrivate::MetaAndDataEntries res;
    res.roles = roles.isEmpty() ? m_availableRoles : roles;
    res.data = fetchTree(QModelIndex {}, size, res.roles);
    const int rowCount = m_model->rowCount(QModelIndex{});
    const int columnCount = m_model->columnCount(QModelIndex{});
    res.size = QSize{columnCount, rowCount};
    return res;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractItemModelSourceAdapter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QAbstractItemModelSourceAdapter10metaObjectEv(
    const QAbstractItemModelSourceAdapter *self) {
  return self->metaObject();
}

//  void *QAbstractItemModelSourceAdapter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QAbstractItemModelSourceAdapter11qt_metacastEPKc(
    QAbstractItemModelSourceAdapter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractItemModelSourceAdapter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QAbstractItemModelSourceAdapter11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractItemModelSourceAdapter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QItemSelectionModel *QAbstractItemModelSourceAdapter::selectionModel()
//      const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK31QAbstractItemModelSourceAdapter14selectionModelEv(
    const QAbstractItemModelSourceAdapter *self) {
  return self->selectionModel();
}

//  QList<int> QAbstractItemModelSourceAdapter::availableRoles() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK31QAbstractItemModelSourceAdapter14availableRolesEv(
    const QAbstractItemModelSourceAdapter *self) {
  return new QList<int>(self->availableRoles());
}

//  QIntHash QAbstractItemModelSourceAdapter::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK31QAbstractItemModelSourceAdapter9roleNamesEv(
    const QAbstractItemModelSourceAdapter *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QSize
//      QAbstractItemModelSourceAdapter::replicaSizeRequest(QtPrivate::IndexL
//      ist parentList)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN31QAbstractItemModelSourceAdapter18replicaSizeRequestE5QListIN9QtPrivate10ModelIndexEE(
    QAbstractItemModelSourceAdapter *self,
    const QtPrivate::IndexList *parentList) {
  return new QSize(self->replicaSizeRequest(*parentList));
}

//  QtPrivate::DataEntries
//      QAbstractItemModelSourceAdapter::replicaRowRequest(QtPrivate::IndexLi
//      st start, QtPrivate::IndexList end, QList<int> roles)
extern "C" Q_DECL_EXPORT
QtPrivate::DataEntries *ritual_ZN31QAbstractItemModelSourceAdapter17replicaRowRequestE5QListIN9QtPrivate10ModelIndexEES3_S0_IiE(
    QAbstractItemModelSourceAdapter *self,
    const QtPrivate::IndexList *start,
    const QtPrivate::IndexList *end,
    const QList<int> *roles) {
  return new QtPrivate::DataEntries(
      self->replicaRowRequest(
          *start,
          *end,
          *roles));
}

//  QVariantList QAbstractItemModelSourceAdapter::replicaHeaderRequest(QList<
//      Qt::Orientation> orientations, QList<int> sections, QList<int> roles)
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN31QAbstractItemModelSourceAdapter20replicaHeaderRequestE5QListIN2Qt11OrientationEES0_IiES4_(
    QAbstractItemModelSourceAdapter *self,
    const QList<Qt::Orientation> *orientations,
    const QList<int> *sections,
    const QList<int> *roles) {
  return new QList<QVariant>(
      self->replicaHeaderRequest(
          *orientations,
          *sections,
          *roles));
}

//  QtPrivate::MetaAndDataEntries
//      QAbstractItemModelSourceAdapter::replicaCacheRequest(size_t size,
//      const QList<int> &roles)
extern "C" Q_DECL_EXPORT
QtPrivate::MetaAndDataEntries *ritual_ZN31QAbstractItemModelSourceAdapter19replicaCacheRequestEmRK5QListIiE(
    QAbstractItemModelSourceAdapter *self,
    size_t size,
    const QList<int> *roles) {
  return new QtPrivate::MetaAndDataEntries(
      self->replicaCacheRequest(
          size,
          *roles));
}

//  void QAbstractItemModelSourceAdapter::sourceRowsInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter18sourceRowsInsertedERK11QModelIndexii(
    QAbstractItemModelSourceAdapter *self,
    const QModelIndex *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceRowsInserted(const QModelIndex &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceRowsInserted(const QModelIndex &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::sourceColumnsInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter21sourceColumnsInsertedERK11QModelIndexii(
    QAbstractItemModelSourceAdapter *self,
    const QModelIndex *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceColumnsInserted(const QModelIndex &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceColumnsInserted(const QModelIndex &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::sourceRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter17sourceRowsRemovedERK11QModelIndexii(
    QAbstractItemModelSourceAdapter *self,
    const QModelIndex *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceRowsRemoved(const QModelIndex &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceRowsRemoved(const QModelIndex &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::sourceCurrentChanged(const
//      QModelIndex &current, const QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter20sourceCurrentChangedERK11QModelIndexS2_(
    QAbstractItemModelSourceAdapter *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceCurrentChanged(const QModelIndex &,const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceCurrentChanged(const QModelIndex &,const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(current)),
      const_cast<void *>(static_cast<const void *>(previous)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::sourceLayoutChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter19sourceLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QAbstractItemModelSourceAdapter *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceLayoutChanged(const QList<QPersistentModelIndex> &,QAbstractItemModel::LayoutChangeHint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceLayoutChanged(const QList<QPersistentModelIndex> &,QAbstractItemModel::LayoutChangeHint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parents)),
      const_cast<void *>(static_cast<const void *>(&hint)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::availableRolesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter21availableRolesChangedEv(
    QAbstractItemModelSourceAdapter *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "availableRolesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "availableRolesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::currentChanged(QtPrivate::IndexList
//      current, QtPrivate::IndexList previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter14currentChangedE5QListIN9QtPrivate10ModelIndexEES3_(
    QAbstractItemModelSourceAdapter *self,
    const QtPrivate::IndexList *current,
    const QtPrivate::IndexList *previous) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentChanged(QtPrivate::IndexList,QtPrivate::IndexList)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentChanged(QtPrivate::IndexList,QtPrivate::IndexList)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(current)),
      const_cast<void *>(static_cast<const void *>(previous)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelSourceAdapter::layoutChanged(QtPrivate::IndexList
//      parents, QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractItemModelSourceAdapter13layoutChangedE5QListIN9QtPrivate10ModelIndexEEN18QAbstractItemModel16LayoutChangeHintE(
    QAbstractItemModelSourceAdapter *self,
    const QtPrivate::IndexList *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelSourceAdapter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "layoutChanged(QtPrivate::IndexList,QAbstractItemModel::LayoutChangeHint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "layoutChanged(QtPrivate::IndexList,QAbstractItemModel::LayoutChangeHint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parents)),
      const_cast<void *>(static_cast<const void *>(&hint)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QList<int> a ritual of QAbstractItemModelSourceAdapter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelSourceAdapter__QList_int(
    QList<int> *self) {
  delete self;
}

//  a QList<QtPrivate::IndexValuePair> a ritual of
//      QAbstractItemModelSourceAdapter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelSourceAdapter__QList_QtPrivate_IndexValuePair(
    QList<QtPrivate::IndexValuePair> *self) {
  delete self;
}
