//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputmethod_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputmethod_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QInputMethod *QInputMethodPrivate::q_func()
extern "C" Q_DECL_EXPORT
QInputMethod *ritual_ZN19QInputMethodPrivate6q_funcEv(
    QInputMethodPrivate *self) {
  return self->q_func();
}

//  const QInputMethod *QInputMethodPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QInputMethod *ritual_ZNK19QInputMethodPrivate6q_funcEv(
    const QInputMethodPrivate *self) {
  return self->q_func();
}

//  QInputMethodPrivate::QInputMethodPrivate()
extern "C" Q_DECL_EXPORT
QInputMethodPrivate *ritual_ZN19QInputMethodPrivateC1Ev() {
  return new QInputMethodPrivate();
}

//  QPlatformInputContext *QInputMethodPrivate::platformInputContext() const
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZNK19QInputMethodPrivate20platformInputContextEv(
    const QInputMethodPrivate *self) {
  return self->platformInputContext();
}

//  QInputMethodPrivate *QInputMethodPrivate::get(QInputMethod *inputMethod)
extern "C" Q_DECL_EXPORT
QInputMethodPrivate *ritual_ZN19QInputMethodPrivate3getEP12QInputMethod(
    QInputMethod *inputMethod) {
  return QInputMethodPrivate::get(inputMethod);
}
