//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickmediaplayer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickmediaplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickMediaPlayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickMediaPlayer10metaObjectEv(
    const QQuickMediaPlayer *self) {
  return self->metaObject();
}

//  void *QQuickMediaPlayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickMediaPlayer11qt_metacastEPKc(
    QQuickMediaPlayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMediaPlayer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickMediaPlayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMediaPlayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMediaPlayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickMediaPlayer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMediaPlayer::tr(s, c, n));
}

//  QQuickMediaPlayer::QQuickMediaPlayer(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMediaPlayer *ritual_ZN17QQuickMediaPlayerC1EP7QObject(
    QObject *parent) {
  return new QQuickMediaPlayer(parent);
}

//  bool QQuickMediaPlayer::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMediaPlayer8autoPlayEv(
    const QQuickMediaPlayer *self) {
  return self->autoPlay();
}

//  void QQuickMediaPlayer::setAutoPlay(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMediaPlayer11setAutoPlayEb(
    QQuickMediaPlayer *self,
    bool autoPlay) {
  self->setAutoPlay(autoPlay);
}

//  void QQuickMediaPlayer::onMediaStatusChanged(QMediaPlayer::MediaStatus
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMediaPlayer20onMediaStatusChangedEN12QMediaPlayer11MediaStatusE(
    QQuickMediaPlayer *self,
    QMediaPlayer::MediaStatus status) {
  self->onMediaStatusChanged(status);
}

//  void QQuickMediaPlayer::autoPlayChanged(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMediaPlayer15autoPlayChangedEb(
    QQuickMediaPlayer *self,
    bool autoPlay) {
  self->autoPlayChanged(autoPlay);
}
