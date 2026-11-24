//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmediaplayer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qmediaplayer.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmediaplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qmediaplayer_p.h>
#include <QtMultimedia/qaudiooutput.h>
#include <QtMultimedia/qvideosink.h>
#include <QtMultimedia/private/qaudiobufferoutput_p.h>
#include <QtMultimedia/private/qmultimediautils_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtemporaryfile.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/playback/qmediaplayer.cpp, line 171, as _ZNK19QMediaPlayerPrivate13trackMetaDataEN20QPlatformMediaPlayer9TrackTypeE
inline QList<QMediaMetaData> QMediaPlayerPrivate::trackMetaData(QPlatformMediaPlayer::TrackType s) const
{
    QList<QMediaMetaData> tracks;
    if (control) {
        int count = control->trackCount(s);
        for (int i = 0; i < count; ++i) {
            tracks.append(control->trackMetaData(s, i));
        }
    }
    return tracks;
}

//  from ../qtmultimedia/src/multimedia/playback/qmediaplayer.cpp, line 91, as _ZN19QMediaPlayerPrivate8setStateEN12QMediaPlayer13PlaybackStateE
inline void QMediaPlayerPrivate::setState(QMediaPlayer::PlaybackState toState)
{
    Q_Q(QMediaPlayer);

    if (toState != state) {
        const auto fromState = std::exchange(state, toState);
        if (toState == QMediaPlayer::PlayingState || fromState == QMediaPlayer::PlayingState)
            emit q->playingChanged(toState == QMediaPlayer::PlayingState);
        emit q->playbackStateChanged(toState);
    }
}

//  from ../qtmultimedia/src/multimedia/playback/qmediaplayer.cpp, line 103, as _ZN19QMediaPlayerPrivate9setStatusEN12QMediaPlayer11MediaStatusE
inline void QMediaPlayerPrivate::setStatus(QMediaPlayer::MediaStatus s)
{
    Q_Q(QMediaPlayer);

    emit q->mediaStatusChanged(s);
}

//  from ../qtmultimedia/src/multimedia/playback/qmediaplayer.cpp, line 110, as _ZN19QMediaPlayerPrivate8setErrorEN12QMediaPlayer5ErrorERK7QString
inline void QMediaPlayerPrivate::setError(QMediaPlayer::Error error, const QString &errorString)
{
    Q_Q(QMediaPlayer);

    this->error.setAndNotify(error, errorString, *q);
}
//  -----------------------------------------------------------------------

//  QMediaPlayer *QMediaPlayerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMediaPlayer *ritual_ZN19QMediaPlayerPrivate6q_funcEv(
    QMediaPlayerPrivate *self) {
  return self->q_func();
}

//  const QMediaPlayer *QMediaPlayerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMediaPlayer *ritual_ZNK19QMediaPlayerPrivate6q_funcEv(
    const QMediaPlayerPrivate *self) {
  return self->q_func();
}

//  QMediaPlayerPrivate *QMediaPlayerPrivate::get(QMediaPlayer *session)
extern "C" Q_DECL_EXPORT
QMediaPlayerPrivate *ritual_ZN19QMediaPlayerPrivate3getEP12QMediaPlayer(
    QMediaPlayer *session) {
  return QMediaPlayerPrivate::get(session);
}

//  QMediaPlayerPrivate::QMediaPlayerPrivate()
extern "C" Q_DECL_EXPORT
QMediaPlayerPrivate *ritual_ZN19QMediaPlayerPrivateC1Ev() {
  return new QMediaPlayerPrivate();
}

//  QList<QMediaMetaData>
//      QMediaPlayerPrivate::trackMetaData(QPlatformMediaPlayer::TrackType s)
//      const
extern "C" Q_DECL_EXPORT
QList<QMediaMetaData> *ritual_ZNK19QMediaPlayerPrivate13trackMetaDataEN20QPlatformMediaPlayer9TrackTypeE(
    const QMediaPlayerPrivate *self,
    QPlatformMediaPlayer::TrackType s) {
  return new QList<QMediaMetaData>(self->trackMetaData(s));
}

//  void QMediaPlayerPrivate::setState(QMediaPlayer::PlaybackState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMediaPlayerPrivate8setStateEN12QMediaPlayer13PlaybackStateE(
    QMediaPlayerPrivate *self,
    QMediaPlayer::PlaybackState state) {
  self->setState(state);
}

//  void QMediaPlayerPrivate::setStatus(QMediaPlayer::MediaStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMediaPlayerPrivate9setStatusEN12QMediaPlayer11MediaStatusE(
    QMediaPlayerPrivate *self,
    QMediaPlayer::MediaStatus status) {
  self->setStatus(status);
}

//  void QMediaPlayerPrivate::setError(QMediaPlayer::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMediaPlayerPrivate8setErrorEN12QMediaPlayer5ErrorERK7QString(
    QMediaPlayerPrivate *self,
    QMediaPlayer::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QMediaPlayerPrivate::setVideoSink(QVideoSink *sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMediaPlayerPrivate12setVideoSinkEP10QVideoSink(
    QMediaPlayerPrivate *self,
    QVideoSink *sink) {
  self->setVideoSink(sink);
}
