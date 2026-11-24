//  Written by dev_tooling.RitualGenerator from the records of QtMultimediaQu
//  ick/6.12.0/QtMultimediaQuick/private/qquickgstreamervideosource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimediaQuick/qtmultimediaquickglobal.h>
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickgstreamervideosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickGStreamerVideoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickGStreamerVideoSource10metaObjectEv(
    const QQuickGStreamerVideoSource *self) {
  return self->metaObject();
}

//  QString QQuickGStreamerVideoSource::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickGStreamerVideoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGStreamerVideoSource::tr(s, c, n));
}

//  QQuickGStreamerVideoSource::QQuickGStreamerVideoSource(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickGStreamerVideoSource *ritual_ZN26QQuickGStreamerVideoSourceC1EP7QObject(
    QObject *parent) {
  return new QQuickGStreamerVideoSource(parent);
}

//  bool QQuickGStreamerVideoSource::qmlIsActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickGStreamerVideoSource11qmlIsActiveEv(
    const QQuickGStreamerVideoSource *self) {
  return self->qmlIsActive();
}

//  void QQuickGStreamerVideoSource::qmlSetActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickGStreamerVideoSource12qmlSetActiveEb(
    QQuickGStreamerVideoSource *self,
    bool active) {
  self->qmlSetActive(active);
}

//  void QQuickGStreamerVideoSource::setQmlGstBinDescription(QString
//      gstBinDescription)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickGStreamerVideoSource23setQmlGstBinDescriptionE7QString(
    QQuickGStreamerVideoSource *self,
    const QString *gstBinDescription) {
  self->setQmlGstBinDescription(*gstBinDescription);
}

#endif  // QT_CONFIG(gstreamer_qt_api)
