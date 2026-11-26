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

//  void *QVirtualKeyboardObserver::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QVirtualKeyboardObserver11qt_metacastEPKc(
    QVirtualKeyboardObserver *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVirtualKeyboardObserver::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QVirtualKeyboardObserver11qt_metacallEN11QMetaObject4CallEiPPv(
    QVirtualKeyboardObserver *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVirtualKeyboardObserver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QVirtualKeyboardObserver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardObserver::tr(s, c, n));
}

//  QVirtualKeyboardObserverPrivate *QVirtualKeyboardObserver::d_func()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardObserverPrivate *ritual_ZN24QVirtualKeyboardObserver6d_funcEv(
    QVirtualKeyboardObserver *self) {
  return self->d_func();
}

//  const QVirtualKeyboardObserverPrivate *QVirtualKeyboardObserver::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QVirtualKeyboardObserverPrivate *ritual_ZNK24QVirtualKeyboardObserver6d_funcEv(
    const QVirtualKeyboardObserver *self) {
  return self->d_func();
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

//  void QVirtualKeyboardObserver::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVirtualKeyboardObserver13layoutChangedEv(
    QVirtualKeyboardObserver *self) {
  self->layoutChanged();
}

//  void QVirtualKeyboardObserver::invalidateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVirtualKeyboardObserver16invalidateLayoutEv(
    QVirtualKeyboardObserver *self) {
  self->invalidateLayout();
}
