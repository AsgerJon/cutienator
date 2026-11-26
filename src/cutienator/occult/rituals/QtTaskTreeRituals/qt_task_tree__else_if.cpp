//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qconditional.h>
#include <QtTaskTree/qtasktree.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTaskTree/qconditional.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 119, as local:qconditional.cpp:ElseIfPrivate
namespace QtTaskTree {
class ElseIfPrivate : public QSharedData
{
public:
    ElseIfPrivate(const ExecutableItem &condition) : m_condition(condition) {}
    ExecutableItem m_condition;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 347, as _ZN10QtTaskTree6ElseIfaSERKS0_
namespace QtTaskTree {
inline ElseIf &ElseIf::operator=(const ElseIf &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::ElseIf::ElseIf(const ExecutableItem &condition)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIf *ritual_ZN10QtTaskTree6ElseIfC1ERKNS_14ExecutableItemE(
    const QtTaskTree::ExecutableItem *condition) {
  return new QtTaskTree::ElseIf(*condition);
}

//  QtTaskTree::ElseIf::ElseIf(const ElseIf &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIf *ritual_ZN10QtTaskTree6ElseIfC1ERKS0_(
    const QtTaskTree::ElseIf *other) {
  return new QtTaskTree::ElseIf(*other);
}

//  ElseIf &QtTaskTree::ElseIf::operator=(const ElseIf &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIf *ritual_ZN10QtTaskTree6ElseIfaSERKS0_(
    QtTaskTree::ElseIf *self,
    const QtTaskTree::ElseIf *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::ElseIf::ElseIf(ElseIf &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIf *ritual_ZN10QtTaskTree6ElseIfC1EOS0_(
    QtTaskTree::ElseIf *other) {
  return new QtTaskTree::ElseIf(std::move(*other));
}

//  void QtTaskTree::ElseIf::swap(ElseIf &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree6ElseIf4swapERS0_(
    QtTaskTree::ElseIf *self,
    QtTaskTree::ElseIf *other) {
  self->swap(*other);
}
