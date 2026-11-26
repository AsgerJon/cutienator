//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowcapture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowcapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowCapturePrivate *QWindowCapturePrivate::get(QWindowCapture
//      &capture)
extern "C" Q_DECL_EXPORT
QWindowCapturePrivate *ritual_ZN21QWindowCapturePrivate3getER14QWindowCapture(
    QWindowCapture *capture) {
  return QWindowCapturePrivate::get(*capture);
}

//  void QWindowCapturePrivate::setIgnoreCursor(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWindowCapturePrivate15setIgnoreCursorEb(
    QWindowCapturePrivate *self,
    bool a0) {
  self->setIgnoreCursor(a0);
}

//  void QWindowCapturePrivate::setIgnoreDropShadow(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWindowCapturePrivate19setIgnoreDropShadowEb(
    QWindowCapturePrivate *self,
    bool a0) {
  self->setIgnoreDropShadow(a0);
}
