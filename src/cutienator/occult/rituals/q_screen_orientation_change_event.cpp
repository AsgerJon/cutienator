//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QScreenOrientationChangeEvent *QScreenOrientationChangeEvent::clone()
//      const
extern "C" Q_DECL_EXPORT
QScreenOrientationChangeEvent *ritual_ZNK29QScreenOrientationChangeEvent5cloneEv(
    const QScreenOrientationChangeEvent *self) {
  return self->clone();
}

//  QScreenOrientationChangeEvent::~QScreenOrientationChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QScreenOrientationChangeEventD1Ev(
    QScreenOrientationChangeEvent *self) {
  delete self;
}

//  QScreenOrientationChangeEvent::QScreenOrientationChangeEvent(QScreen
//      *screen, Qt::ScreenOrientation orientation)
extern "C" Q_DECL_EXPORT
QScreenOrientationChangeEvent *ritual_ZN29QScreenOrientationChangeEventC1EP7QScreenN2Qt17ScreenOrientationE(
    QScreen *screen,
    Qt::ScreenOrientation orientation) {
  return new QScreenOrientationChangeEvent(screen, orientation);
}

//  QScreen *QScreenOrientationChangeEvent::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK29QScreenOrientationChangeEvent6screenEv(
    const QScreenOrientationChangeEvent *self) {
  return self->screen();
}

//  Qt::ScreenOrientation QScreenOrientationChangeEvent::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK29QScreenOrientationChangeEvent11orientationEv(
    const QScreenOrientationChangeEvent *self) {
  return self->orientation();
}
