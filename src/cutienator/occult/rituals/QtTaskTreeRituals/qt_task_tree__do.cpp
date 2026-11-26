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

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 1897, as local:qtasktree.cpp:DoPrivate
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
class DoPrivate : public QSharedData
{
public:
    DoPrivate(const GroupItem &children) : m_children(children) {}
    GroupItem m_children;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 3902, as _ZN10QtTaskTree2DoaSERKS0_
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
inline Do &Do::operator=(const Do &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::Do::Do(const GroupItems &children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Do *ritual_ZN10QtTaskTree2DoC1ERK5QListINS_9GroupItemEE(
    const QtTaskTree::GroupItems *children) {
  return new QtTaskTree::Do(*children);
}

//  QtTaskTree::Do::Do(std::initializer_list<GroupItem> children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Do *ritual_ZN10QtTaskTree2DoC1ESt16initializer_listINS_9GroupItemEE(
    const std::initializer_list<QtTaskTree::GroupItem> *children) {
  return new QtTaskTree::Do(*children);
}

//  QtTaskTree::Do::Do(const Do &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Do *ritual_ZN10QtTaskTree2DoC1ERKS0_(
    const QtTaskTree::Do *other) {
  return new QtTaskTree::Do(*other);
}

//  Do &QtTaskTree::Do::operator=(const Do &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Do *ritual_ZN10QtTaskTree2DoaSERKS0_(
    QtTaskTree::Do *self,
    const QtTaskTree::Do *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::Do::Do(Do &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Do *ritual_ZN10QtTaskTree2DoC1EOS0_(QtTaskTree::Do *other) {
  return new QtTaskTree::Do(std::move(*other));
}

//  void QtTaskTree::Do::swap(Do &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree2Do4swapERS0_(
    QtTaskTree::Do *self,
    QtTaskTree::Do *other) {
  self->swap(*other);
}
