//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/inputselectionhandle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputselectionhandle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  Only a class built on QtVirtualKeyboard::InputSelectionHandle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtVirtualKeyboard_InputSelectionHandle : QtVirtualKeyboard::InputSelectionHandle {
  using QtVirtualKeyboard::InputSelectionHandle::paintEvent;
  using QtVirtualKeyboard::InputSelectionHandle::event;
};

//  const QMetaObject *QtVirtualKeyboard::InputSelectionHandle::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard20InputSelectionHandle10metaObjectEv(
    const QtVirtualKeyboard::InputSelectionHandle *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::InputSelectionHandle::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard20InputSelectionHandle11qt_metacastEPKc(
    QtVirtualKeyboard::InputSelectionHandle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QtVirtualKeyboard::InputSelectionHandle::qt_metacall(QMetaObject::Cal
//      l a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard20InputSelectionHandle11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::InputSelectionHandle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::InputSelectionHandle::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard20InputSelectionHandle2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::InputSelectionHandle::tr(s, c, n));
}

//  QtVirtualKeyboard::InputSelectionHandle::InputSelectionHandle(DesktopInpu
//      tSelectionControl *control, QWindow *eventWindow)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::InputSelectionHandle *ritual_ZN17QtVirtualKeyboard20InputSelectionHandleC1EPNS_28DesktopInputSelectionControlEP7QWindow(
    QtVirtualKeyboard::DesktopInputSelectionControl *control,
    QWindow *eventWindow) {
  return new QtVirtualKeyboard::InputSelectionHandle(control, eventWindow);
}

//  void QtVirtualKeyboard::InputSelectionHandle::applyImage(const QSize
//      &windowSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard20InputSelectionHandle10applyImageERK5QSize(
    QtVirtualKeyboard::InputSelectionHandle *self,
    const QSize *windowSize) {
  self->applyImage(*windowSize);
}

//  void QtVirtualKeyboard::InputSelectionHandle::paintEvent(QPaintEvent *pe)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard20InputSelectionHandle10paintEventEP11QPaintEvent(
    QtVirtualKeyboard::InputSelectionHandle *self,
    QPaintEvent *pe) {
  self->paintEvent(pe);
}

//  bool QtVirtualKeyboard::InputSelectionHandle::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard20InputSelectionHandle5eventEP6QEvent(
    QtVirtualKeyboard::InputSelectionHandle *self,
    QEvent *event) {
  return self->event(event);
}

//  void QtVirtualKeyboard::InputSelectionHandle::paintEvent(QPaintEvent *pe)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20InputSelectionHandle10paintEventEP11QPaintEvent(
    QtVirtualKeyboard::InputSelectionHandle *self,
    QPaintEvent *pe) {
  static_cast<OwnQtVirtualKeyboard_InputSelectionHandle *>(self)->OwnQtVirtualKeyboard_InputSelectionHandle::paintEvent(
      pe);
}

//  bool QtVirtualKeyboard::InputSelectionHandle::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard20InputSelectionHandle5eventEP6QEvent(
    QtVirtualKeyboard::InputSelectionHandle *self,
    QEvent *event) {
  return static_cast<OwnQtVirtualKeyboard_InputSelectionHandle *>(self)->OwnQtVirtualKeyboard_InputSelectionHandle::event(
      event);
}
