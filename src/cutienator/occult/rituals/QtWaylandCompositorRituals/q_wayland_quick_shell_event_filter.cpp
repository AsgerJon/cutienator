//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QWaylandQuickShellEventFilter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandQuickShellEventFilter : QWaylandQuickShellEventFilter {
  using QWaylandQuickShellEventFilter::timerEvent;
};

//  const QMetaObject *QWaylandQuickShellEventFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QWaylandQuickShellEventFilter10metaObjectEv(
    const QWaylandQuickShellEventFilter *self) {
  return self->metaObject();
}

//  void *QWaylandQuickShellEventFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QWaylandQuickShellEventFilter11qt_metacastEPKc(
    QWaylandQuickShellEventFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickShellEventFilter::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QWaylandQuickShellEventFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickShellEventFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickShellEventFilter::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QWaylandQuickShellEventFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickShellEventFilter::tr(s, c, n));
}

//  void QWaylandQuickShellEventFilter::startFilter(QWaylandClient *client,
//      CallbackFunction closePopupCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellEventFilter11startFilterEP14QWaylandClientSt8functionIFvvEE(
    QWaylandClient *client,
    const QWaylandQuickShellEventFilter::CallbackFunction *closePopupCallback) {
  QWaylandQuickShellEventFilter::startFilter(client, *closePopupCallback);
}

//  void QWaylandQuickShellEventFilter::cancelFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellEventFilter12cancelFilterEv() {
  QWaylandQuickShellEventFilter::cancelFilter();
}

//  void QWaylandQuickShellEventFilter::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellEventFilter10timerEventEP11QTimerEvent(
    QWaylandQuickShellEventFilter *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QWaylandQuickShellEventFilter::stopFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellEventFilter10stopFilterEv(
    QWaylandQuickShellEventFilter *self) {
  self->stopFilter();
}

//  QWaylandQuickShellEventFilter::QWaylandQuickShellEventFilter(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellEventFilter *ritual_ZN29QWaylandQuickShellEventFilterC1EP7QObject(
    QObject *parent) {
  return new QWaylandQuickShellEventFilter(parent);
}

//  bool QWaylandQuickShellEventFilter::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QWaylandQuickShellEventFilter11eventFilterEP7QObjectP6QEvent(
    QWaylandQuickShellEventFilter *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  void QWaylandQuickShellEventFilter::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QWaylandQuickShellEventFilter10timerEventEP11QTimerEvent(
    QWaylandQuickShellEventFilter *self,
    QTimerEvent *event) {
  static_cast<OwnQWaylandQuickShellEventFilter *>(self)->OwnQWaylandQuickShellEventFilter::timerEvent(
      event);
}

//  bool QWaylandQuickShellEventFilter::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN29QWaylandQuickShellEventFilter11eventFilterEP7QObjectP6QEvent(
    QWaylandQuickShellEventFilter *self,
    QObject *a0,
    QEvent *a1) {
  return self->QWaylandQuickShellEventFilter::eventFilter(a0, a1);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
