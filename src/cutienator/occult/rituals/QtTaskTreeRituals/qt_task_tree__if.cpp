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

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 50, as local:qconditional.cpp:IfPrivate
namespace QtTaskTree {
class IfPrivate : public QSharedData
{
public:
    IfPrivate(const ExecutableItem &condition) : m_condition(condition) {}
    ExecutableItem m_condition;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qconditional.cpp, line 350, as _ZN10QtTaskTree2IfaSERKS0_
namespace QtTaskTree {
inline If &If::operator=(const If &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::If::If(const ExecutableItem &condition)
extern "C" Q_DECL_EXPORT
QtTaskTree::If *ritual_ZN10QtTaskTree2IfC1ERKNS_14ExecutableItemE(
    const QtTaskTree::ExecutableItem *condition) {
  return new QtTaskTree::If(*condition);
}

//  QtTaskTree::If::If(const If &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::If *ritual_ZN10QtTaskTree2IfC1ERKS0_(
    const QtTaskTree::If *other) {
  return new QtTaskTree::If(*other);
}

//  If &QtTaskTree::If::operator=(const If &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::If *ritual_ZN10QtTaskTree2IfaSERKS0_(
    QtTaskTree::If *self,
    const QtTaskTree::If *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::If::If(If &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::If *ritual_ZN10QtTaskTree2IfC1EOS0_(QtTaskTree::If *other) {
  return new QtTaskTree::If(std::move(*other));
}

//  void QtTaskTree::If::swap(If &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree2If4swapERS0_(
    QtTaskTree::If *self,
    QtTaskTree::If *other) {
  self->swap(*other);
}

//  ThenItem operator>>(const If &ifItem, const Then &thenItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTreersERKNS_2IfERKNS_4ThenE(
    const QtTaskTree::If *ifItem,
    const QtTaskTree::Then *thenItem) {
  return new QtTaskTree::ThenItem(operator>>(*ifItem, *thenItem));
}
