//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qtasktree.h>
#include <QtTaskTree/QtTaskTree>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTaskTree/qtasktree.h>
#include <QtTaskTree/qbarriertask.h>
#include <QtTaskTree/qconditional.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/QDebug>
#include <QtCore/QEventLoop>
#if QT_CONFIG(future)
#  include <QtCore/QFutureWatcher>
#endif
#include <QtCore/QHash>
#include <QtCore/QMap>
#include <QtCore/QMetaEnum>
#include <QtCore/QMutex>
#include <QtCore/QPointer>
#include <QtCore/QSet>
#include <QtCore/QThread>
#include <QtCore/QTime>
#include <QtCore/QTimer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 2627, as local:qtasktree.cpp:GroupItemPrivate
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
class GroupItemPrivate : public QSharedData
{
public:
    GroupItem::Type m_type = GroupItem::Type::Group;
    GroupItems m_children;
    GroupItem::GroupData m_groupData;
    QList<StorageBase> m_storageList;
    GroupItem::TaskHandler m_taskHandler;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 3904, as _ZN10QtTaskTree9GroupItemaSERKS0_
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
inline GroupItem &GroupItem::operator=(const GroupItem &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::GroupItem::GroupItem(const GroupItems &children)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERK5QListIS0_E(
    const QtTaskTree::GroupItems *children) {
  return new QtTaskTree::GroupItem(*children);
}

//  QtTaskTree::GroupItem::GroupItem(std::initializer_list<GroupItem>
//      children)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ESt16initializer_listIS0_E(
    const std::initializer_list<QtTaskTree::GroupItem> *children) {
  return new QtTaskTree::GroupItem(*children);
}

//  QtTaskTree::GroupItem::GroupItem(const GroupItem &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERKS0_(
    const QtTaskTree::GroupItem *other) {
  return new QtTaskTree::GroupItem(*other);
}

//  GroupItem &QtTaskTree::GroupItem::operator=(const GroupItem &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemaSERKS0_(
    QtTaskTree::GroupItem *self,
    const QtTaskTree::GroupItem *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::GroupItem::GroupItem(GroupItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1EOS0_(
    QtTaskTree::GroupItem *other) {
  return new QtTaskTree::GroupItem(std::move(*other));
}

//  void QtTaskTree::GroupItem::swap(GroupItem &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree9GroupItem4swapERS0_(
    QtTaskTree::GroupItem *self,
    QtTaskTree::GroupItem *other) {
  self->swap(*other);
}

//  QtTaskTree::GroupItem::GroupItem(const Iterator &loop)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERKNS_8IteratorE(
    const QtTaskTree::Iterator *loop) {
  return new QtTaskTree::GroupItem(*loop);
}

//  QtTaskTree::GroupItem::GroupItem()
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1Ev() {
  return new QtTaskTree::GroupItem();
}

//  QtTaskTree::GroupItem::GroupItem(Type type)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ENS0_4TypeE(
    QtTaskTree::GroupItem::Type type) {
  return new QtTaskTree::GroupItem(type);
}

//  QtTaskTree::GroupItem::GroupItem(const GroupData &data)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERKNS0_9GroupDataE(
    const QtTaskTree::GroupItem::GroupData *data) {
  return new QtTaskTree::GroupItem(*data);
}

//  QtTaskTree::GroupItem::GroupItem(const TaskHandler &handler)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERKNS0_11TaskHandlerE(
    const QtTaskTree::GroupItem::TaskHandler *handler) {
  return new QtTaskTree::GroupItem(*handler);
}

//  void QtTaskTree::GroupItem::addChildren(const GroupItems &children)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree9GroupItem11addChildrenERK5QListIS0_E(
    QtTaskTree::GroupItem *self,
    const QtTaskTree::GroupItems *children) {
  self->addChildren(*children);
}

//  GroupItem QtTaskTree::GroupItem::groupHandler(const GroupHandler
//      &handler)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItem12groupHandlerERKNS0_12GroupHandlerE(
    const QtTaskTree::GroupItem::GroupHandler *handler) {
  return new QtTaskTree::GroupItem(
      QtTaskTree::GroupItem::groupHandler(
          *handler));
}

//  TaskHandler QtTaskTree::GroupItem::taskHandler() const
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem::TaskHandler *ritual_ZNK10QtTaskTree9GroupItem11taskHandlerEv(
    const QtTaskTree::GroupItem *self) {
  return new QtTaskTree::GroupItem::TaskHandler(self->taskHandler());
}

//  QtTaskTree::GroupItem::GroupItem(const StorageBase &storage)
extern "C" Q_DECL_EXPORT
QtTaskTree::GroupItem *ritual_ZN10QtTaskTree9GroupItemC1ERKNS_11StorageBaseE(
    const QtTaskTree::StorageBase *storage) {
  return new QtTaskTree::GroupItem(*storage);
}

//  a QtTaskTree::GroupItem::TaskHandler a ritual of QtTaskTree::GroupItem
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtTaskTree_GroupItem__QtTaskTree_GroupItem_TaskHandler(
    QtTaskTree::GroupItem::TaskHandler *self) {
  delete self;
}
