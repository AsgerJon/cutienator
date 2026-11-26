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

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 166, as local:qconditional.cpp:ElsePrivate
namespace QtTaskTree {
class ElsePrivate : public QSharedData
{
public:
    ElsePrivate(const Group &body) : m_body(body) {}
    Group m_body;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 346, as _ZN10QtTaskTree4ElseaSERKS0_
namespace QtTaskTree {
inline Else &Else::operator=(const Else &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::Else::Else(const GroupItems &children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Else *ritual_ZN10QtTaskTree4ElseC1ERK5QListINS_9GroupItemEE(
    const QtTaskTree::GroupItems *children) {
  return new QtTaskTree::Else(*children);
}

//  QtTaskTree::Else::Else(std::initializer_list<GroupItem> children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Else *ritual_ZN10QtTaskTree4ElseC1ESt16initializer_listINS_9GroupItemEE(
    const std::initializer_list<QtTaskTree::GroupItem> *children) {
  return new QtTaskTree::Else(*children);
}

//  QtTaskTree::Else::Else(const Else &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Else *ritual_ZN10QtTaskTree4ElseC1ERKS0_(
    const QtTaskTree::Else *other) {
  return new QtTaskTree::Else(*other);
}

//  Else &QtTaskTree::Else::operator=(const Else &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Else *ritual_ZN10QtTaskTree4ElseaSERKS0_(
    QtTaskTree::Else *self,
    const QtTaskTree::Else *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::Else::Else(Else &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Else *ritual_ZN10QtTaskTree4ElseC1EOS0_(
    QtTaskTree::Else *other) {
  return new QtTaskTree::Else(std::move(*other));
}

//  void QtTaskTree::Else::swap(Else &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree4Else4swapERS0_(
    QtTaskTree::Else *self,
    QtTaskTree::Else *other) {
  self->swap(*other);
}
