//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qintrusivelist_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qintrusivelist_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QIntrusiveListNode::~QIntrusiveListNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QIntrusiveListNodeD1Ev(QIntrusiveListNode *self) {
  delete self;
}

//  void QIntrusiveListNode::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QIntrusiveListNode6removeEv(QIntrusiveListNode *self) {
  self->remove();
}

//  bool QIntrusiveListNode::isInList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QIntrusiveListNode8isInListEv(
    const QIntrusiveListNode *self) {
  return self->isInList();
}
