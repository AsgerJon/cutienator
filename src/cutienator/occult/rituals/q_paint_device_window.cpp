//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintdevicewindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintdevicewindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>

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
