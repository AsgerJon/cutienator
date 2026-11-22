//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QTouchEvent *QTouchEvent::clone() const
extern "C" Q_DECL_EXPORT
QTouchEvent *ritual_ZNK11QTouchEvent5cloneEv(const QTouchEvent *self) {
  return self->clone();
}

//  QTouchEvent::~QTouchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTouchEventD1Ev(QTouchEvent *self) {
  delete self;
}

//  QObject *QTouchEvent::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QTouchEvent6targetEv(const QTouchEvent *self) {
  return self->target();
}

//  QEventPoint::States QTouchEvent::touchPointStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTouchEvent16touchPointStatesEv(const QTouchEvent *self) {
  return static_cast<int>(self->touchPointStates().toInt());
}

//  bool QTouchEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent12isBeginEventEv(const QTouchEvent *self) {
  return self->isBeginEvent();
}

//  bool QTouchEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent13isUpdateEventEv(const QTouchEvent *self) {
  return self->isUpdateEvent();
}

//  bool QTouchEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent10isEndEventEv(const QTouchEvent *self) {
  return self->isEndEvent();
}
