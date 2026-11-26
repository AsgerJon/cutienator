//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qbarriertask.h>
#include <QtTaskTree/qtasktree.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTaskTree/qbarriertask.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttasktree/src/tasktree/qbarriertask.cpp, line 255, as local:qbarriertask.cpp:WhenPrivate
namespace QtTaskTree {
class WhenPrivate : public QSharedData
{
public:
    WhenPrivate(const BarrierKickerGetter &kicker, WorkflowPolicy policy)
        : m_barrierKicker(kicker)
        , m_workflowPolicy(policy)
    {}
    BarrierKickerGetter m_barrierKicker;
    WorkflowPolicy m_workflowPolicy = WorkflowPolicy::StopOnError;
};
}  // namespace QtTaskTree

//  from ../qttasktree/src/tasktree/qbarriertask.cpp, line 348, as _ZN10QtTaskTree4WhenaSERKS0_
namespace QtTaskTree {
inline When &When::operator=(const When &other) = default;
}  // namespace QtTaskTree
//  -----------------------------------------------------------------------

//  QtTaskTree::When::When(const BarrierKickerGetter &kicker, WorkflowPolicy
//      policy)
extern "C" Q_DECL_EXPORT
QtTaskTree::When *ritual_ZN10QtTaskTree4WhenC1ERKSt8functionIFNS_14ExecutableItemERKNS_7StorageINS_15QStartedBarrierEEEEENS_14WorkflowPolicyE(
    const QtTaskTree::BarrierKickerGetter *kicker,
    QtTaskTree::WorkflowPolicy policy) {
  return new QtTaskTree::When(*kicker, policy);
}

//  QtTaskTree::When::When(const When &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::When *ritual_ZN10QtTaskTree4WhenC1ERKS0_(
    const QtTaskTree::When *other) {
  return new QtTaskTree::When(*other);
}

//  When &QtTaskTree::When::operator=(const When &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::When *ritual_ZN10QtTaskTree4WhenaSERKS0_(
    QtTaskTree::When *self,
    const QtTaskTree::When *other) {
  return &(self->operator=(*other));
}

//  QtTaskTree::When::When(When &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::When *ritual_ZN10QtTaskTree4WhenC1EOS0_(
    QtTaskTree::When *other) {
  return new QtTaskTree::When(std::move(*other));
}

//  void QtTaskTree::When::swap(When &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree4When4swapERS0_(
    QtTaskTree::When *self,
    QtTaskTree::When *other) {
  self->swap(*other);
}

//  Group operator>>(const When &whenItem, const Do &doItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreersERKNS_4WhenERKNS_2DoE(
    const QtTaskTree::When *whenItem,
    const QtTaskTree::Do *doItem) {
  return new QtTaskTree::Group(operator>>(*whenItem, *doItem));
}
