//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  Only a class built on qdesigner_internal::ZoomWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_ZoomWidget : qdesigner_internal::ZoomWidget {
  using qdesigner_internal::ZoomWidget::resizeEvent;
  using qdesigner_internal::ZoomWidget::applyZoom;
  using qdesigner_internal::ZoomWidget::doResize;
};

//  const QMetaObject *qdesigner_internal::ZoomWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal10ZoomWidget10metaObjectEv(
    const qdesigner_internal::ZoomWidget *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ZoomWidget::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal10ZoomWidget2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ZoomWidget::tr(s, c, n));
}

//  const QGraphicsProxyWidget *qdesigner_internal::ZoomWidget::proxy() const
extern "C" Q_DECL_EXPORT
const QGraphicsProxyWidget *ritual_ZNK18qdesigner_internal10ZoomWidget5proxyEv(
    const qdesigner_internal::ZoomWidget *self) {
  return self->proxy();
}

//  QGraphicsProxyWidget *qdesigner_internal::ZoomWidget::proxy()
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN18qdesigner_internal10ZoomWidget5proxyEv(
    qdesigner_internal::ZoomWidget *self) {
  return self->proxy();
}

//  void qdesigner_internal::ZoomWidget::doResize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget8doResizeERK5QSize(
    qdesigner_internal::ZoomWidget *self,
    const QSize *s) {
  self->doResize(*s);
}

//  QGraphicsProxyWidget
//      *qdesigner_internal::ZoomWidget::createProxyWidget(QGraphicsItem
//      *parent, Qt::WindowFlags wFlags) const
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZNK18qdesigner_internal10ZoomWidget17createProxyWidgetEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    const qdesigner_internal::ZoomWidget *self,
    QGraphicsItem *parent,
    int wFlags) {
  return self->createProxyWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QSize qdesigner_internal::ZoomWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18qdesigner_internal10ZoomWidget15minimumSizeHintEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->qdesigner_internal::ZoomWidget::minimumSizeHint());
}

//  QSize qdesigner_internal::ZoomWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18qdesigner_internal10ZoomWidget8sizeHintEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->qdesigner_internal::ZoomWidget::sizeHint());
}

//  void qdesigner_internal::ZoomWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10ZoomWidget11resizeEventEP12QResizeEvent(
    qdesigner_internal::ZoomWidget *self,
    QResizeEvent *event) {
  static_cast<Ownqdesigner_internal_ZoomWidget *>(self)->Ownqdesigner_internal_ZoomWidget::resizeEvent(
      event);
}

//  void qdesigner_internal::ZoomWidget::applyZoom()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10ZoomWidget9applyZoomEv(
    qdesigner_internal::ZoomWidget *self) {
  static_cast<Ownqdesigner_internal_ZoomWidget *>(self)->Ownqdesigner_internal_ZoomWidget::applyZoom();
}

//  void qdesigner_internal::ZoomWidget::doResize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10ZoomWidget8doResizeERK5QSize(
    qdesigner_internal::ZoomWidget *self,
    const QSize *s) {
  static_cast<Ownqdesigner_internal_ZoomWidget *>(self)->Ownqdesigner_internal_ZoomWidget::doResize(
      *s);
}

//  QGraphicsProxyWidget
//      *qdesigner_internal::ZoomWidget::createProxyWidget(QGraphicsItem
//      *parent, Qt::WindowFlags wFlags) const
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_own_ZNK18qdesigner_internal10ZoomWidget17createProxyWidgetEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    const qdesigner_internal::ZoomWidget *self,
    QGraphicsItem *parent,
    int wFlags) {
  return self->qdesigner_internal::ZoomWidget::createProxyWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}
