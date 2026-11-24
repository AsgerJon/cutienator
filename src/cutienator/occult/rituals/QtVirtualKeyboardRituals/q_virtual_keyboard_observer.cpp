//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboardobserver.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardobserver.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QVirtualKeyboardObserver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QVirtualKeyboardObserver10metaObjectEv(
    const QVirtualKeyboardObserver *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardObserver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QVirtualKeyboardObserver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardObserver::tr(s, c, n));
}

//  QVirtualKeyboardObserver::QVirtualKeyboardObserver(QObject *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardObserver *ritual_ZN24QVirtualKeyboardObserverC1EP7QObject(
    QObject *parent) {
  return new QVirtualKeyboardObserver(parent);
}

//  QVariant QVirtualKeyboardObserver::layout()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QVirtualKeyboardObserver6layoutEv(
    QVirtualKeyboardObserver *self) {
  return new QVariant(self->layout());
}

//  void QVirtualKeyboardObserver::invalidateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVirtualKeyboardObserver16invalidateLayoutEv(
    QVirtualKeyboardObserver *self) {
  self->invalidateLayout();
}
