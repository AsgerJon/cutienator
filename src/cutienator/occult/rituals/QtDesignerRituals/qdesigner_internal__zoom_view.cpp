//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on qdesigner_internal::ZoomView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_ZoomView : qdesigner_internal::ZoomView {
  using qdesigner_internal::ZoomView::contextMenuEvent;
  using qdesigner_internal::ZoomView::applyZoom;
};

//  const QMetaObject *qdesigner_internal::ZoomView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal8ZoomView10metaObjectEv(
    const qdesigner_internal::ZoomView *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ZoomView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal8ZoomView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ZoomView::tr(s, c, n));
}

//  void qdesigner_internal::ZoomView::applyZoom()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView9applyZoomEv(
    qdesigner_internal::ZoomView *self) {
  self->applyZoom();
}

//  void qdesigner_internal::ZoomView::contextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal8ZoomView16contextMenuEventEP17QContextMenuEvent(
    qdesigner_internal::ZoomView *self,
    QContextMenuEvent *event) {
  static_cast<Ownqdesigner_internal_ZoomView *>(self)->Ownqdesigner_internal_ZoomView::contextMenuEvent(
      event);
}

//  void qdesigner_internal::ZoomView::applyZoom()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal8ZoomView9applyZoomEv(
    qdesigner_internal::ZoomView *self) {
  static_cast<Ownqdesigner_internal_ZoomView *>(self)->Ownqdesigner_internal_ZoomView::applyZoom();
}
