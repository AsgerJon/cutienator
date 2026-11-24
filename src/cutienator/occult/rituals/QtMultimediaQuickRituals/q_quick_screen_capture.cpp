//  Written by dev_tooling.RitualGenerator from the records of QtMultimediaQu
//  ick/6.12.0/QtMultimediaQuick/private/qquickscreencapture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickscreencapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickScreenCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickScreenCapture10metaObjectEv(
    const QQuickScreenCapture *self) {
  return self->metaObject();
}

//  QString QQuickScreenCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickScreenCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScreenCapture::tr(s, c, n));
}

//  QQuickScreenCapture::QQuickScreenCapture(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScreenCapture *ritual_ZN19QQuickScreenCaptureC1EP7QObject(
    QObject *parent) {
  return new QQuickScreenCapture(parent);
}

//  void QQuickScreenCapture::qmlSetScreen(QQuickScreenInfo *newQmlScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickScreenCapture12qmlSetScreenEP16QQuickScreenInfo(
    QQuickScreenCapture *self,
    QQuickScreenInfo *newQmlScreen) {
  self->qmlSetScreen(newQmlScreen);
}

//  QQuickScreenInfo *QQuickScreenCapture::ensureQmlScreen()
extern "C" Q_DECL_EXPORT
QQuickScreenInfo *ritual_ZN19QQuickScreenCapture15ensureQmlScreenEv(
    QQuickScreenCapture *self) {
  return self->ensureQmlScreen();
}

//  void QQuickScreenCapture::qmlSetMaximumFrameRate(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickScreenCapture22qmlSetMaximumFrameRateEd(
    QQuickScreenCapture *self,
    qreal a0) {
  self->qmlSetMaximumFrameRate(a0);
}

//  qreal QQuickScreenCapture::qmlMaximumFrameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickScreenCapture19qmlMaximumFrameRateEv(
    const QQuickScreenCapture *self) {
  return self->qmlMaximumFrameRate();
}

//  void QQuickScreenCapture::qmlResetMaximumFrameRate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickScreenCapture24qmlResetMaximumFrameRateEv(
    QQuickScreenCapture *self) {
  self->qmlResetMaximumFrameRate();
}
