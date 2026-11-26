//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qtasktree.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 1845, as local:qtasktree.cpp:ForPrivate
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
class ForPrivate : public QSharedData
{
public:
    ForPrivate(const Iterator &iterator) : m_iterator(iterator) {}
    Iterator m_iterator;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qtasktree.cpp, line 3903, as _ZN10QtTaskTree3ForaSERKS0_
namespace QtTaskTree {
using namespace std::chrono;
using namespace Qt::StringLiterals;
inline For &For::operator=(const For &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::For::For(const Iterator &loop)
extern "C" Q_DECL_EXPORT
QtTaskTree::For *ritual_ZN10QtTaskTree3ForC1ERKNS_8IteratorE(
    const QtTaskTree::Iterator *loop) {
  return new QtTaskTree::For(*loop);
}

//  QtTaskTree::For::For(qsizetype count)
extern "C" Q_DECL_EXPORT
QtTaskTree::For *ritual_ZN10QtTaskTree3ForC1Ex(qsizetype count) {
  return new QtTaskTree::For(count);
}

//  QtTaskTree::For::For(const For &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::For *ritual_ZN10QtTaskTree3ForC1ERKS0_(
    const QtTaskTree::For *other) {
  return new QtTaskTree::For(*other);
}

//  For &QtTaskTree::For::operator=(const For &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::For *ritual_ZN10QtTaskTree3ForaSERKS0_(
    QtTaskTree::For *self,
    const QtTaskTree::For *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::For::For(For &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::For *ritual_ZN10QtTaskTree3ForC1EOS0_(QtTaskTree::For *other) {
  return new QtTaskTree::For(std::move(*other));
}

//  void QtTaskTree::For::swap(For &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree3For4swapERS0_(
    QtTaskTree::For *self,
    QtTaskTree::For *other) {
  self->swap(*other);
}

//  Group operator>>(const For &forItem, const Do &doItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreersERKNS_3ForERKNS_2DoE(
    const QtTaskTree::For *forItem,
    const QtTaskTree::Do *doItem) {
  return new QtTaskTree::Group(operator>>(*forItem, *doItem));
}
