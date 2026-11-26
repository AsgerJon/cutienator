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

//  void *qdesigner_internal::ZoomWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal10ZoomWidget11qt_metacastEPKc(
    qdesigner_internal::ZoomWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ZoomWidget::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal10ZoomWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ZoomWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  qdesigner_internal::ZoomWidget::ZoomWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ZoomWidget *ritual_ZN18qdesigner_internal10ZoomWidgetC1EP7QWidget(
    QWidget *parent) {
  return new qdesigner_internal::ZoomWidget(parent);
}

//  void qdesigner_internal::ZoomWidget::setWidget(QWidget *w,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget9setWidgetEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    qdesigner_internal::ZoomWidget *self,
    QWidget *w,
    int wFlags) {
  self->setWidget(w, QFlags<Qt::WindowType>::fromInt(wFlags));
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

//  bool qdesigner_internal::ZoomWidget::isWidgetZoomContextMenuEnabled()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal10ZoomWidget30isWidgetZoomContextMenuEnabledEv(
    const qdesigner_internal::ZoomWidget *self) {
  return self->isWidgetZoomContextMenuEnabled();
}

//  void qdesigner_internal::ZoomWidget::setWidgetZoomContextMenuEnabled(bool
//      e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget31setWidgetZoomContextMenuEnabledEb(
    qdesigner_internal::ZoomWidget *self,
    bool e) {
  self->setWidgetZoomContextMenuEnabled(e);
}

//  void qdesigner_internal::ZoomWidget::setItemAcceptDrops(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget18setItemAcceptDropsEb(
    qdesigner_internal::ZoomWidget *self,
    bool a0) {
  self->setItemAcceptDrops(a0);
}

//  bool qdesigner_internal::ZoomWidget::itemAcceptDrops() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal10ZoomWidget15itemAcceptDropsEv(
    const qdesigner_internal::ZoomWidget *self) {
  return self->itemAcceptDrops();
}

//  QSize qdesigner_internal::ZoomWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal10ZoomWidget15minimumSizeHintEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSize qdesigner_internal::ZoomWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal10ZoomWidget8sizeHintEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->sizeHint());
}

//  bool qdesigner_internal::ZoomWidget::zoomedEventFilter(QObject *watched,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal10ZoomWidget17zoomedEventFilterEP7QObjectP6QEvent(
    qdesigner_internal::ZoomWidget *self,
    QObject *watched,
    QEvent *event) {
  return self->zoomedEventFilter(watched, event);
}

//  void qdesigner_internal::ZoomWidget::dump() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal10ZoomWidget4dumpEv(
    const qdesigner_internal::ZoomWidget *self) {
  self->dump();
}

//  void qdesigner_internal::ZoomWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget11resizeEventEP12QResizeEvent(
    qdesigner_internal::ZoomWidget *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void qdesigner_internal::ZoomWidget::applyZoom()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget9applyZoomEv(
    qdesigner_internal::ZoomWidget *self) {
  self->applyZoom();
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

//  QSize qdesigner_internal::ZoomWidget::widgetSizeToViewSize(const QSize
//      &s, bool *ptrToValid) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal10ZoomWidget20widgetSizeToViewSizeERK5QSizePb(
    const qdesigner_internal::ZoomWidget *self,
    const QSize *s,
    bool *ptrToValid) {
  return new QSize(self->widgetSizeToViewSize(*s, ptrToValid));
}

//  void qdesigner_internal::ZoomWidget::resizeToWidgetSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ZoomWidget18resizeToWidgetSizeEv(
    qdesigner_internal::ZoomWidget *self) {
  self->resizeToWidgetSize();
}

//  QSize qdesigner_internal::ZoomWidget::viewPortMargin() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal10ZoomWidget14viewPortMarginEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->viewPortMargin());
}

//  QSize qdesigner_internal::ZoomWidget::widgetSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal10ZoomWidget10widgetSizeEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSize(self->widgetSize());
}

//  QSizeF qdesigner_internal::ZoomWidget::widgetDecorationSizeF() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18qdesigner_internal10ZoomWidget21widgetDecorationSizeFEv(
    const qdesigner_internal::ZoomWidget *self) {
  return new QSizeF(self->widgetDecorationSizeF());
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
