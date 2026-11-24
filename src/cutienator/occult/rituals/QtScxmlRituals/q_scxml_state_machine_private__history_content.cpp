//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
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
