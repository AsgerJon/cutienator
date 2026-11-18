//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>

//  QEvent::QEvent(Type type)
extern "C" QEvent *ritual_ZN6QEventC1ENS_4TypeE(QEvent::Type type) {
  return new QEvent(type);
}

//  QEvent::~QEvent()
extern "C" void ritual_ZN6QEventD1Ev(QEvent *self) {
  delete self;
}

//  Type QEvent::type() const
extern "C" QEvent::Type ritual_ZNK6QEvent4typeEv(const QEvent *self) {
  return self->type();
}

//  bool QEvent::spontaneous() const
extern "C" bool ritual_ZNK6QEvent11spontaneousEv(const QEvent *self) {
  return self->spontaneous();
}

//  void QEvent::setAccepted(bool accepted)
extern "C" void ritual_ZN6QEvent11setAcceptedEb(
    QEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  bool QEvent::isAccepted() const
extern "C" bool ritual_ZNK6QEvent10isAcceptedEv(const QEvent *self) {
  return self->isAccepted();
}

//  void QEvent::accept()
extern "C" void ritual_ZN6QEvent6acceptEv(QEvent *self) {
  self->accept();
}

//  void QEvent::ignore()
extern "C" void ritual_ZN6QEvent6ignoreEv(QEvent *self) {
  self->ignore();
}

//  bool QEvent::isInputEvent() const
extern "C" bool ritual_ZNK6QEvent12isInputEventEv(const QEvent *self) {
  return self->isInputEvent();
}

//  bool QEvent::isPointerEvent() const
extern "C" bool ritual_ZNK6QEvent14isPointerEventEv(const QEvent *self) {
  return self->isPointerEvent();
}

//  bool QEvent::isSinglePointEvent() const
extern "C" bool ritual_ZNK6QEvent18isSinglePointEventEv(const QEvent *self) {
  return self->isSinglePointEvent();
}

//  int QEvent::registerEventType(int hint)
extern "C" int ritual_ZN6QEvent17registerEventTypeEi(int hint) {
  return QEvent::registerEventType(hint);
}

//  QEvent *QEvent::clone() const
extern "C" QEvent *ritual_ZNK6QEvent5cloneEv(const QEvent *self) {
  return self->clone();
}
