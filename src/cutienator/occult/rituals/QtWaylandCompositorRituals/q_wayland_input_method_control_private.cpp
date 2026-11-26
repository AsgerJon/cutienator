//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(im)
#if QT_CONFIG(im)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(im)
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#endif
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWaylandInputMethodControl *QWaylandInputMethodControlPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControl *ritual_ZN33QWaylandInputMethodControlPrivate6q_funcEv(
    QWaylandInputMethodControlPrivate *self) {
  return self->q_func();
}

//  const QWaylandInputMethodControl
//      *QWaylandInputMethodControlPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandInputMethodControl *ritual_ZNK33QWaylandInputMethodControlPrivate6q_funcEv(
    const QWaylandInputMethodControlPrivate *self) {
  return self->q_func();
}

//  QWaylandInputMethodControlPrivate::QWaylandInputMethodControlPrivate(QWay
//      landSurface *surface)
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControlPrivate *ritual_ZN33QWaylandInputMethodControlPrivateC1EP15QWaylandSurface(
    QWaylandSurface *surface) {
  return new QWaylandInputMethodControlPrivate(surface);
}

//  QWaylandTextInput *QWaylandInputMethodControlPrivate::textInput() const
extern "C" Q_DECL_EXPORT
QWaylandTextInput *ritual_ZNK33QWaylandInputMethodControlPrivate9textInputEv(
    const QWaylandInputMethodControlPrivate *self) {
  return self->textInput();
}

//  QWaylandTextInputV3 *QWaylandInputMethodControlPrivate::textInputV3()
//      const
extern "C" Q_DECL_EXPORT
QWaylandTextInputV3 *ritual_ZNK33QWaylandInputMethodControlPrivate11textInputV3Ev(
    const QWaylandInputMethodControlPrivate *self) {
  return self->textInputV3();
}

//  QWaylandQtTextInputMethod
//      *QWaylandInputMethodControlPrivate::textInputMethod() const
extern "C" Q_DECL_EXPORT
QWaylandQtTextInputMethod *ritual_ZNK33QWaylandInputMethodControlPrivate15textInputMethodEv(
    const QWaylandInputMethodControlPrivate *self) {
  return self->textInputMethod();
}

#endif  // QT_CONFIG(im)
#endif  // QT_CONFIG(im)
