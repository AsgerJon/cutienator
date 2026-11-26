//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qgstreamervideosource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamervideosource.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qgstreamervideosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGStreamerVideoSource *QGStreamerVideoSourcePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGStreamerVideoSource *ritual_ZN28QGStreamerVideoSourcePrivate6q_funcEv(
    QGStreamerVideoSourcePrivate *self) {
  return self->q_func();
}

//  const QGStreamerVideoSource *QGStreamerVideoSourcePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGStreamerVideoSource *ritual_ZNK28QGStreamerVideoSourcePrivate6q_funcEv(
    const QGStreamerVideoSourcePrivate *self) {
  return self->q_func();
}

//  QGStreamerVideoSourcePrivate
//      *QGStreamerVideoSourcePrivate::get(QGStreamerVideoSource *source)
extern "C" Q_DECL_EXPORT
QGStreamerVideoSourcePrivate *ritual_ZN28QGStreamerVideoSourcePrivate3getEP21QGStreamerVideoSource(
    QGStreamerVideoSource *source) {
  return QGStreamerVideoSourcePrivate::get(source);
}

//  void
//      QGStreamerVideoSourcePrivate::createPlatformCamera(QGStreamerVideoSou
//      rce *source, GstElementOrDescription elementOrDesc, bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGStreamerVideoSourcePrivate20createPlatformCameraEP21QGStreamerVideoSourceSt7variantIJ7QStringP11_GstElementEEb(
    QGStreamerVideoSourcePrivate *self,
    QGStreamerVideoSource *source,
    const GstElementOrDescription *elementOrDesc,
    bool active) {
  self->createPlatformCamera(source, *elementOrDesc, active);
}

#endif  // QT_CONFIG(gstreamer_qt_api)
