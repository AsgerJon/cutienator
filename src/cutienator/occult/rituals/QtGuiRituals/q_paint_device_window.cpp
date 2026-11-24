//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintdevicewindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintdevicewindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>

//  Only a class built on QPaintDeviceWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPaintDeviceWindow : QPaintDeviceWindow {
  using QPaintDeviceWindow::exposeEvent;
  using QPaintDeviceWindow::paintEvent;
  using QPaintDeviceWindow::metric;
  using QPaintDeviceWindow::event;
};

//  const QMetaObject *QPaintDeviceWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPaintDeviceWindow10metaObjectEv(
    const QPaintDeviceWindow *self) {
  return self->metaObject();
}

//  QString QPaintDeviceWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPaintDeviceWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPaintDeviceWindow::tr(s, c, n));
}

//  QPaintDeviceWindowPrivate *QPaintDeviceWindow::d_func()
extern "C" Q_DECL_EXPORT
QPaintDeviceWindowPrivate *ritual_ZN18QPaintDeviceWindow6d_funcEv(
    QPaintDeviceWindow *self) {
  return self->d_func();
}

//  const QPaintDeviceWindowPrivate *QPaintDeviceWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QPaintDeviceWindowPrivate *ritual_ZNK18QPaintDeviceWindow6d_funcEv(
    const QPaintDeviceWindow *self) {
  return self->d_func();
}

//  void QPaintDeviceWindow::update(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPaintDeviceWindow6updateERK5QRect(
    QPaintDeviceWindow *self,
    const QRect *rect) {
  self->update(*rect);
}

//  void QPaintDeviceWindow::update(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPaintDeviceWindow6updateERK7QRegion(
    QPaintDeviceWindow *self,
    const QRegion *region) {
  self->update(*region);
}

//  void QPaintDeviceWindow::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPaintDeviceWindow6updateEv(QPaintDeviceWindow *self) {
  self->update();
}

//  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPaintDeviceWindow11exposeEventEP12QExposeEvent(
    QPaintDeviceWindow *self,
    QExposeEvent *a0) {
  self->exposeEvent(a0);
}

//  void QPaintDeviceWindow::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPaintDeviceWindow10paintEventEP11QPaintEvent(
    QPaintDeviceWindow *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  int QPaintDeviceWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QPaintDeviceWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPaintDeviceWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  bool QPaintDeviceWindow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QPaintDeviceWindow5eventEP6QEvent(
    QPaintDeviceWindow *self,
    QEvent *event) {
  return self->event(event);
}

//  QPaintEngine *QPaintDeviceWindow::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK18QPaintDeviceWindow11paintEngineEv(
    const QPaintDeviceWindow *self) {
  return self->paintEngine();
}

//  QPaintDeviceWindow as the QPaintDevice it is built on
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_cast_QPaintDeviceWindow_QPaintDevice(
    QPaintDeviceWindow *self) {
  return static_cast<QPaintDevice *>(self);
}

//  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPaintDeviceWindow11exposeEventEP12QExposeEvent(
    QPaintDeviceWindow *self,
    QExposeEvent *a0) {
  static_cast<OwnQPaintDeviceWindow *>(self)->OwnQPaintDeviceWindow::exposeEvent(
      a0);
}

//  void QPaintDeviceWindow::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPaintDeviceWindow10paintEventEP11QPaintEvent(
    QPaintDeviceWindow *self,
    QPaintEvent *event) {
  static_cast<OwnQPaintDeviceWindow *>(self)->OwnQPaintDeviceWindow::paintEvent(
      event);
}

//  int QPaintDeviceWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QPaintDeviceWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPaintDeviceWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQPaintDeviceWindow *>(self)->OwnQPaintDeviceWindow::metric(
      metric);
}

//  bool QPaintDeviceWindow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QPaintDeviceWindow5eventEP6QEvent(
    QPaintDeviceWindow *self,
    QEvent *event) {
  return static_cast<OwnQPaintDeviceWindow *>(self)->OwnQPaintDeviceWindow::event(
      event);
}

//  QPaintEngine *QPaintDeviceWindow::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK18QPaintDeviceWindow11paintEngineEv(
    const QPaintDeviceWindow *self) {
  return self->QPaintDeviceWindow::paintEngine();
}
