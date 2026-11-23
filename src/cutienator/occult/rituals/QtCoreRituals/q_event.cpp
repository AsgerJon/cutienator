//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>
#include <cstring>

//  A QEvent that Python can take functions over in. Every QEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQEventCall0)(const void *, bool, int *);
typedef void * (*CuteQEventCall1)(const void *, int *);
class CuteQEvent : public QEvent {
public:
  using QEvent::QEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventCall0 call = reinterpret_cast<CuteQEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventCall1 call = reinterpret_cast<CuteQEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QEvent::QEvent(Type type)
extern "C" Q_DECL_EXPORT
QEvent *ritual_ZN6QEventC1ENS_4TypeE(QEvent::Type type) {
  return new CuteQEvent(type);
}

//  QEvent::~QEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QEventD1Ev(QEvent *self) {
  delete self;
}

//  Type QEvent::type() const
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZNK6QEvent4typeEv(const QEvent *self) {
  return self->type();
}

//  bool QEvent::spontaneous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QEvent11spontaneousEv(const QEvent *self) {
  return self->spontaneous();
}

//  void QEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QEvent11setAcceptedEb(QEvent *self, bool accepted) {
  self->setAccepted(accepted);
}

//  bool QEvent::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QEvent10isAcceptedEv(const QEvent *self) {
  return self->isAccepted();
}

//  void QEvent::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QEvent6acceptEv(QEvent *self) {
  self->accept();
}

//  void QEvent::ignore()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QEvent6ignoreEv(QEvent *self) {
  self->ignore();
}

//  bool QEvent::isInputEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QEvent12isInputEventEv(const QEvent *self) {
  return self->isInputEvent();
}

//  bool QEvent::isPointerEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QEvent14isPointerEventEv(const QEvent *self) {
  return self->isPointerEvent();
}

//  bool QEvent::isSinglePointEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QEvent18isSinglePointEventEv(const QEvent *self) {
  return self->isSinglePointEvent();
}

//  int QEvent::registerEventType(int hint)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QEvent17registerEventTypeEi(int hint) {
  return QEvent::registerEventType(hint);
}

//  QEvent *QEvent::clone() const
extern "C" Q_DECL_EXPORT
QEvent *ritual_ZNK6QEvent5cloneEv(const QEvent *self) {
  return self->clone();
}

//  void QEvent::setSpontaneous()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QEvent14setSpontaneousEv(QEvent *self) {
  self->setSpontaneous();
}

//  a Python function taken by a CuteQEvent, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEvent(QEvent *self, const char *key, void *call) {
  return static_cast<CuteQEvent *>(self)->take(key, call);
}

//  void QEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QEvent11setAcceptedEb(QEvent *self, bool accepted) {
  self->QEvent::setAccepted(accepted);
}

//  QEvent *QEvent::clone() const
extern "C" Q_DECL_EXPORT
QEvent *ritual_own_ZNK6QEvent5cloneEv(const QEvent *self) {
  return self->QEvent::clone();
}
