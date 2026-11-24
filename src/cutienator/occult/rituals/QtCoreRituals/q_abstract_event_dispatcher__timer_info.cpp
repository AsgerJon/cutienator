//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstracteventdispatcher.h>

#if !defined(Q_QDOC)
#if !defined(__cpp_aggregate_paren_init)
//  QAbstractEventDispatcher::TimerInfo::TimerInfo()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher::TimerInfo *ritual_ZN24QAbstractEventDispatcher9TimerInfoC1Ev() {
  return new QAbstractEventDispatcher::TimerInfo();
}
#endif  // !defined(__cpp_aggregate_paren_init)
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
#if !defined(__cpp_aggregate_paren_init)
//  QAbstractEventDispatcher::TimerInfo::TimerInfo(int id, int i,
//      Qt::TimerType t)
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher::TimerInfo *ritual_ZN24QAbstractEventDispatcher9TimerInfoC1EiiN2Qt9TimerTypeE(
    int id,
    int i,
    Qt::TimerType t) {
  return new QAbstractEventDispatcher::TimerInfo(id, i, t);
}
#endif  // !defined(__cpp_aggregate_paren_init)
#endif  // !defined(Q_QDOC)

//  QAbstractEventDispatcher::TimerInfo::~TimerInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher9TimerInfoD1Ev(
    QAbstractEventDispatcher::TimerInfo *self) {
  delete self;
}
