//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 1. Kept as it is when the generator runs again.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlStateMachinePrivate::HistoryContent::HistoryContent()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::HistoryContent *ritual_ZN25QScxmlStateMachinePrivate14HistoryContentC1Ev() {
  return new QScxmlStateMachinePrivate::HistoryContent();
}

//  int QScxmlStateMachinePrivate::HistoryContent::value(int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QScxmlStateMachinePrivate14HistoryContent5valueEi(
    const QScxmlStateMachinePrivate::HistoryContent *self,
    int idx) {
  return self->value(idx);
}

//  QScxmlStateMachinePrivate::HistoryContent::~HistoryContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate14HistoryContentD1Ev(
    QScxmlStateMachinePrivate::HistoryContent *self) {
  delete self;
}

//  int &QScxmlStateMachinePrivate::HistoryContent::operator[](int idx)
extern "C" Q_DECL_EXPORT
int *ritual_ZN25QScxmlStateMachinePrivate14HistoryContentixEi(
    QScxmlStateMachinePrivate::HistoryContent *self,
    int idx) {
  return &((*self)[idx]);
}
