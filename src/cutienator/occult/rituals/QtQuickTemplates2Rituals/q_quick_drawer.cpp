//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickDrawer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDrawer : QQuickDrawer {
  using QQuickDrawer::childMouseEventFilter;
  using QQuickDrawer::mouseMoveEvent;
  using QQuickDrawer::overlayEvent;
  using QQuickDrawer::touchEvent;
  using QQuickDrawer::geometryChange;
};

//  const QMetaObject *QQuickDrawer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickDrawer10metaObjectEv(
    const QQuickDrawer *self) {
  return self->metaObject();
}

//  QString QQuickDrawer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickDrawer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDrawer::tr(s, c, n));
}

//  QQuickDrawer::QQuickDrawer(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDrawer *ritual_ZN12QQuickDrawerC1EP7QObject(QObject *parent) {
  return new QQuickDrawer(parent);
}

//  Qt::Edge QQuickDrawer::edge() const
extern "C" Q_DECL_EXPORT
Qt::Edge ritual_ZNK12QQuickDrawer4edgeEv(const QQuickDrawer *self) {
  return self->edge();
}

//  void QQuickDrawer::setEdge(Qt::Edge edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer7setEdgeEN2Qt4EdgeE(
    QQuickDrawer *self,
    Qt::Edge edge) {
  self->setEdge(edge);
}

//  qreal QQuickDrawer::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDrawer8positionEv(const QQuickDrawer *self) {
  return self->position();
}

//  void QQuickDrawer::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer11setPositionEd(
    QQuickDrawer *self,
    qreal position) {
  self->setPosition(position);
}

//  qreal QQuickDrawer::dragMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDrawer10dragMarginEv(const QQuickDrawer *self) {
  return self->dragMargin();
}

//  void QQuickDrawer::setDragMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer13setDragMarginEd(
    QQuickDrawer *self,
    qreal margin) {
  self->setDragMargin(margin);
}

//  void QQuickDrawer::resetDragMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer15resetDragMarginEv(QQuickDrawer *self) {
  self->resetDragMargin();
}

//  bool QQuickDrawer::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickDrawer13isInteractiveEv(const QQuickDrawer *self) {
  return self->isInteractive();
}

//  void QQuickDrawer::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer14setInteractiveEb(
    QQuickDrawer *self,
    bool interactive) {
  self->setInteractive(interactive);
}

//  bool QQuickDrawer::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickDrawer21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickDrawer *self,
    QQuickItem *child,
    QEvent *event) {
  return self->childMouseEventFilter(child, event);
}

//  void QQuickDrawer::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer14mouseMoveEventEP11QMouseEvent(
    QQuickDrawer *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  bool QQuickDrawer::overlayEvent(QQuickItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickDrawer12overlayEventEP10QQuickItemP6QEvent(
    QQuickDrawer *self,
    QQuickItem *item,
    QEvent *event) {
  return self->overlayEvent(item, event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickDrawer::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer10touchEventEP11QTouchEvent(
    QQuickDrawer *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickDrawer::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDrawer14geometryChangeERK6QRectFS2_(
    QQuickDrawer *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QQuickDrawerPrivate *QQuickDrawer::d_func()
extern "C" Q_DECL_EXPORT
QQuickDrawerPrivate *ritual_ZN12QQuickDrawer6d_funcEv(QQuickDrawer *self) {
  return self->d_func();
}

//  const QQuickDrawerPrivate *QQuickDrawer::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDrawerPrivate *ritual_ZNK12QQuickDrawer6d_funcEv(
    const QQuickDrawer *self) {
  return self->d_func();
}

//  bool QQuickDrawer::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickDrawer21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickDrawer *self,
    QQuickItem *child,
    QEvent *event) {
  return static_cast<OwnQQuickDrawer *>(self)->OwnQQuickDrawer::childMouseEventFilter(
      child,
      event);
}

//  void QQuickDrawer::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDrawer14mouseMoveEventEP11QMouseEvent(
    QQuickDrawer *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickDrawer *>(self)->OwnQQuickDrawer::mouseMoveEvent(
      event);
}

//  bool QQuickDrawer::overlayEvent(QQuickItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickDrawer12overlayEventEP10QQuickItemP6QEvent(
    QQuickDrawer *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQQuickDrawer *>(self)->OwnQQuickDrawer::overlayEvent(
      item,
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickDrawer::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDrawer10touchEventEP11QTouchEvent(
    QQuickDrawer *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickDrawer *>(self)->OwnQQuickDrawer::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickDrawer::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDrawer14geometryChangeERK6QRectFS2_(
    QQuickDrawer *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickDrawer *>(self)->OwnQQuickDrawer::geometryChange(
      *newGeometry,
      *oldGeometry);
}
