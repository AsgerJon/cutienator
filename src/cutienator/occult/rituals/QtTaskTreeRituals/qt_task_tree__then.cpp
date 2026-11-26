//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qconditional.h>
#include <QtTaskTree/QtTaskTree>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTaskTree/qconditional.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 207, as local:qconditional.cpp:ThenPrivate
namespace QtTaskTree {
class ThenPrivate : public QSharedData
{
public:
    ThenPrivate(const Group &body) : m_body(body) {}
    Group m_body;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 351, as _ZN10QtTaskTree4ThenaSERKS0_
namespace QtTaskTree {
inline Then &Then::operator=(const Then &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::Then::Then(const GroupItems &children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Then *ritual_ZN10QtTaskTree4ThenC1ERK5QListINS_9GroupItemEE(
    const QtTaskTree::GroupItems *children) {
  return new QtTaskTree::Then(*children);
}

//  QtTaskTree::Then::Then(std::initializer_list<GroupItem> children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Then *ritual_ZN10QtTaskTree4ThenC1ESt16initializer_listINS_9GroupItemEE(
    const std::initializer_list<QtTaskTree::GroupItem> *children) {
  return new QtTaskTree::Then(*children);
}

//  QtTaskTree::Then::Then(const Then &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Then *ritual_ZN10QtTaskTree4ThenC1ERKS0_(
    const QtTaskTree::Then *other) {
  return new QtTaskTree::Then(*other);
}

//  Then &QtTaskTree::Then::operator=(const Then &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Then *ritual_ZN10QtTaskTree4ThenaSERKS0_(
    QtTaskTree::Then *self,
    const QtTaskTree::Then *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::Then::Then(Then &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Then *ritual_ZN10QtTaskTree4ThenC1EOS0_(
    QtTaskTree::Then *other) {
  return new QtTaskTree::Then(std::move(*other));
}

//  void QtTaskTree::Then::swap(Then &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree4Then4swapERS0_(
    QtTaskTree::Then *self,
    QtTaskTree::Then *other) {
  self->swap(*other);
}
