//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

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

//  void *qdesigner_internal::ZoomView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal8ZoomView11qt_metacastEPKc(
    qdesigner_internal::ZoomView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ZoomView::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal8ZoomView11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ZoomView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  qdesigner_internal::ZoomView::ZoomView(QWidget *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ZoomView *ritual_ZN18qdesigner_internal8ZoomViewC1EP7QWidget(
    QWidget *parent) {
  return new qdesigner_internal::ZoomView(parent);
}

//  int qdesigner_internal::ZoomView::zoom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal8ZoomView4zoomEv(
    const qdesigner_internal::ZoomView *self) {
  return self->zoom();
}

//  qreal qdesigner_internal::ZoomView::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18qdesigner_internal8ZoomView10zoomFactorEv(
    const qdesigner_internal::ZoomView *self) {
  return self->zoomFactor();
}

//  bool qdesigner_internal::ZoomView::isZoomContextMenuEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal8ZoomView24isZoomContextMenuEnabledEv(
    const qdesigner_internal::ZoomView *self) {
  return self->isZoomContextMenuEnabled();
}

//  void qdesigner_internal::ZoomView::setZoomContextMenuEnabled(bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView25setZoomContextMenuEnabledEb(
    qdesigner_internal::ZoomView *self,
    bool e) {
  self->setZoomContextMenuEnabled(e);
}

//  QGraphicsScene &qdesigner_internal::ZoomView::scene()
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN18qdesigner_internal8ZoomView5sceneEv(
    qdesigner_internal::ZoomView *self) {
  return &(self->scene());
}

//  const QGraphicsScene &qdesigner_internal::ZoomView::scene() const
extern "C" Q_DECL_EXPORT
const QGraphicsScene *ritual_ZNK18qdesigner_internal8ZoomView5sceneEv(
    const qdesigner_internal::ZoomView *self) {
  return &(self->scene());
}

//  ZoomMenu *qdesigner_internal::ZoomView::zoomMenu()
extern "C" Q_DECL_EXPORT
qdesigner_internal::ZoomMenu *ritual_ZN18qdesigner_internal8ZoomView8zoomMenuEv(
    qdesigner_internal::ZoomView *self) {
  return self->zoomMenu();
}

//  QPoint qdesigner_internal::ZoomView::scrollPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal8ZoomView14scrollPositionEv(
    const qdesigner_internal::ZoomView *self) {
  return new QPoint(self->scrollPosition());
}

//  void qdesigner_internal::ZoomView::setScrollPosition(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView17setScrollPositionERK6QPoint(
    qdesigner_internal::ZoomView *self,
    const QPoint *pos) {
  self->setScrollPosition(*pos);
}

//  void qdesigner_internal::ZoomView::scrollToOrigin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView14scrollToOriginEv(
    qdesigner_internal::ZoomView *self) {
  self->scrollToOrigin();
}

//  void qdesigner_internal::ZoomView::setZoom(int percent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView7setZoomEi(
    qdesigner_internal::ZoomView *self,
    int percent) {
  self->setZoom(percent);
}

//  void qdesigner_internal::ZoomView::showContextMenu(const QPoint
//      &globalPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView15showContextMenuERK6QPoint(
    qdesigner_internal::ZoomView *self,
    const QPoint *globalPos) {
  self->showContextMenu(*globalPos);
}

//  void qdesigner_internal::ZoomView::contextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomView16contextMenuEventEP17QContextMenuEvent(
    qdesigner_internal::ZoomView *self,
    QContextMenuEvent *event) {
  self->contextMenuEvent(event);
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
