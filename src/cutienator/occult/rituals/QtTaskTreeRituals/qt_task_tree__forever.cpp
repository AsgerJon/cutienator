//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>
#include <QtTaskTree/QtTaskTree>

//  QtTaskTree::Forever::Forever(const GroupItems &children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Forever *ritual_ZN10QtTaskTree7ForeverC1ERK5QListINS_9GroupItemEE(
    const QtTaskTree::GroupItems *children) {
  return new QtTaskTree::Forever(*children);
}

//  QtTaskTree::Forever::Forever(std::initializer_list<GroupItem> children)
extern "C" Q_DECL_EXPORT
QtTaskTree::Forever *ritual_ZN10QtTaskTree7ForeverC1ESt16initializer_listINS_9GroupItemEE(
    const std::initializer_list<QtTaskTree::GroupItem> *children) {
  return new QtTaskTree::Forever(*children);
}

//  Group QtTaskTree::Forever::operator Group() const
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZNK10QtTaskTree7ForevercvNS_5GroupEEv(
    const QtTaskTree::Forever *self) {
  return new QtTaskTree::Group(self->operator QtTaskTree::Group());
}

//  QtTaskTree::Forever::~Forever()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree7ForeverD1Ev(QtTaskTree::Forever *self) {
  delete self;
}
