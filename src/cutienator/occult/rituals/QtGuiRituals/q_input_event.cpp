//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QInputEvent that Python can take functions over in. Every QInputEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQInputEventCall0)(const void *, int *);
typedef void (*CuteQInputEventCall1)(const void *, quint64, int *);
typedef void (*CuteQInputEventCall2)(const void *, bool, int *);
class CuteQInputEvent : public QInputEvent {
public:
  using QInputEvent::QInputEvent;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QInputEvent12setTimestampEy")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QInputEvent *QInputEvent::clone() const
  QInputEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQInputEventCall0 call = reinterpret_cast<CuteQInputEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QInputEvent *>(given);
    }
    return QInputEvent::clone();
  }

  //  void QInputEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQInputEventCall1 call = reinterpret_cast<CuteQInputEventCall1>(taken[1]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QInputEvent::setTimestamp(timestamp);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[2]) {
      int handled = 0;
      CuteQInputEventCall2 call = reinterpret_cast<CuteQInputEventCall2>(taken[2]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QInputEvent *QInputEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputEvent *ritual_ZNK11QInputEvent5cloneEv(const QInputEvent *self) {
  return self->clone();
}

//  QInputEvent::~QInputEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEventD1Ev(QInputEvent *self) {
  delete self;
}

//  QInputEvent::QInputEvent(Type type, const QInputDevice *m_dev,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QInputEvent *ritual_ZN11QInputEventC1EN6QEvent4TypeEPK12QInputDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QEvent::Type type,
    const QInputDevice *m_dev,
    int modifiers) {
  return new CuteQInputEvent(
      type,
      m_dev,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  const QInputDevice *QInputEvent::device() const
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZNK11QInputEvent6deviceEv(
    const QInputEvent *self) {
  return self->device();
}

//  QInputDevice::DeviceType QInputEvent::deviceType() const
extern "C" Q_DECL_EXPORT
QInputDevice::DeviceType ritual_ZNK11QInputEvent10deviceTypeEv(
    const QInputEvent *self) {
  return self->deviceType();
}

//  Qt::KeyboardModifiers QInputEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QInputEvent9modifiersEv(const QInputEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QInputEvent::setModifiers(Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QInputEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  quint64 QInputEvent::timestamp() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK11QInputEvent9timestampEv(const QInputEvent *self) {
  return self->timestamp();
}

//  void QInputEvent::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEvent12setTimestampEy(
    QInputEvent *self,
    quint64 timestamp) {
  self->setTimestamp(timestamp);
}

//  a Python function taken by a CuteQInputEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputEvent(
    QInputEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputEvent *>(self)->take(key, call);
}

//  QInputEvent *QInputEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputEvent *ritual_own_ZNK11QInputEvent5cloneEv(const QInputEvent *self) {
  return self->QInputEvent::clone();
}

//  void QInputEvent::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QInputEvent12setTimestampEy(
    QInputEvent *self,
    quint64 timestamp) {
  self->QInputEvent::setTimestamp(timestamp);
}
