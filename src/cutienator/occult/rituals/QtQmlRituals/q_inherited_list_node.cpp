//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qdoubleendedlist_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qdoubleendedlist_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QInheritedListNode::~QInheritedListNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QInheritedListNodeD1Ev(QInheritedListNode *self) {
  delete self;
}

//  bool QInheritedListNode::isInList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QInheritedListNode8isInListEv(
    const QInheritedListNode *self) {
  return self->isInList();
}

//  void QInheritedListNode::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QInheritedListNode6removeEv(QInheritedListNode *self) {
  self->remove();
}
