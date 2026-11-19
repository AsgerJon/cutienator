//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qnamespace.h>

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
  return new QKeyEvent(
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
  return new QKeyEvent(
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

//  bool QKeyEvent::matches(QKeySequence::StandardKey key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QKeyEvent7matchesEN12QKeySequence11StandardKeyE(
    const QKeyEvent *self,
    QKeySequence::StandardKey key) {
  return self->matches(key);
}

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
