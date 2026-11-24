//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qnamespace.h>
#include <cstring>

//  A QKeyEvent that Python can take functions over in. Every QKeyEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQKeyEventCall0)(const void *, int *);
typedef void (*CuteQKeyEventCall1)(const void *, quint64, int *);
typedef void (*CuteQKeyEventCall2)(const void *, bool, int *);
class CuteQKeyEvent : public QKeyEvent {
public:
  using QKeyEvent::QKeyEvent;
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

  //  QKeyEvent *QKeyEvent::clone() const
  QKeyEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQKeyEventCall0 call = reinterpret_cast<CuteQKeyEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QKeyEvent *>(given);
    }
    return QKeyEvent::clone();
  }

  //  void QInputEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQKeyEventCall1 call = reinterpret_cast<CuteQKeyEventCall1>(taken[1]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QInputEvent::setTimestamp(timestamp);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[2]) {
      int handled = 0;
      CuteQKeyEventCall2 call = reinterpret_cast<CuteQKeyEventCall2>(taken[2]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QKeyEvent *QKeyEvent::clone() const
extern "C" Q_DECL_EXPORT
QKeyEvent *ritual_ZNK9QKeyEvent5cloneEv(const QKeyEvent *self) {
  return self->clone();
}

//  QKeyEvent::~QKeyEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QKeyEventD1Ev(QKeyEvent *self) {
  delete self;
}

//  QKeyEvent::QKeyEvent(Type type, int key, Qt::KeyboardModifiers modifiers,
//      const QString &text, bool autorep, quint16 count)
extern "C" Q_DECL_EXPORT
QKeyEvent *ritual_ZN9QKeyEventC1EN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QEvent::Type type,
    int key,
    int modifiers,
    const QString *text,
    bool autorep,
    quint16 count) {
  return new CuteQKeyEvent(
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      *text,
      autorep,
      count);
}

//  QKeyEvent::QKeyEvent(Type type, int key, Qt::KeyboardModifiers modifiers,
//      quint32 nativeScanCode, quint32 nativeVirtualKey, quint32
//      nativeModifiers, const QString &text, bool autorep, quint16 count,
//      const QInputDevice *device)
extern "C" Q_DECL_EXPORT
QKeyEvent *ritual_ZN9QKeyEventC1EN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbtPK12QInputDevice(
    QEvent::Type type,
    int key,
    int modifiers,
    quint32 nativeScanCode,
    quint32 nativeVirtualKey,
    quint32 nativeModifiers,
    const QString *text,
    bool autorep,
    quint16 count,
    const QInputDevice *device) {
  return new CuteQKeyEvent(
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      nativeScanCode,
      nativeVirtualKey,
      nativeModifiers,
      *text,
      autorep,
      count,
      device);
}

//  int QKeyEvent::key() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QKeyEvent3keyEv(const QKeyEvent *self) {
  return self->key();
}

#if QT_CONFIG(shortcut)
//  bool QKeyEvent::matches(QKeySequence::StandardKey key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QKeyEvent7matchesEN12QKeySequence11StandardKeyE(
    const QKeyEvent *self,
    QKeySequence::StandardKey key) {
  return self->matches(key);
}
#endif  // QT_CONFIG(shortcut)

//  Qt::KeyboardModifiers QKeyEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QKeyEvent9modifiersEv(const QKeyEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  QKeyCombination QKeyEvent::keyCombination() const
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZNK9QKeyEvent14keyCombinationEv(
    const QKeyEvent *self) {
  return new QKeyCombination(self->keyCombination());
}

//  QString QKeyEvent::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QKeyEvent4textEv(const QKeyEvent *self) {
  return new QString(self->text());
}

//  bool QKeyEvent::isAutoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QKeyEvent12isAutoRepeatEv(const QKeyEvent *self) {
  return self->isAutoRepeat();
}

//  int QKeyEvent::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QKeyEvent5countEv(const QKeyEvent *self) {
  return self->count();
}

//  quint32 QKeyEvent::nativeScanCode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK9QKeyEvent14nativeScanCodeEv(const QKeyEvent *self) {
  return self->nativeScanCode();
}

//  quint32 QKeyEvent::nativeVirtualKey() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK9QKeyEvent16nativeVirtualKeyEv(const QKeyEvent *self) {
  return self->nativeVirtualKey();
}

//  quint32 QKeyEvent::nativeModifiers() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK9QKeyEvent15nativeModifiersEv(const QKeyEvent *self) {
  return self->nativeModifiers();
}

#if QT_CONFIG(shortcut)
//  bool operator==(QKeyEvent *e, QKeySequence::StandardKey key)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqP9QKeyEventN12QKeySequence11StandardKeyE(
    QKeyEvent *e,
    QKeySequence::StandardKey key) {
  return operator==(e, key);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  bool operator==(QKeySequence::StandardKey key, QKeyEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN12QKeySequence11StandardKeyEP9QKeyEvent(
    QKeySequence::StandardKey key,
    QKeyEvent *e) {
  return operator==(key, e);
}
#endif  // QT_CONFIG(shortcut)

//  a Python function taken by a CuteQKeyEvent, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKeyEvent(QKeyEvent *self, const char *key, void *call) {
  return static_cast<CuteQKeyEvent *>(self)->take(key, call);
}

//  QKeyEvent *QKeyEvent::clone() const
extern "C" Q_DECL_EXPORT
QKeyEvent *ritual_own_ZNK9QKeyEvent5cloneEv(const QKeyEvent *self) {
  return self->QKeyEvent::clone();
}
