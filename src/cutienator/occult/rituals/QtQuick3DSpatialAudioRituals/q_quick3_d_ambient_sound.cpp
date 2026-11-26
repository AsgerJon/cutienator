//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DSpati
//  alAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dambientsound_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qtquick3daudioglobal_p.h>
#include <QtQuick3DSpatialAudio/QtQuick3DSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dambientsound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/private/qquick3dambientsound_p.h>
#include <QtMultimediaQuick/private/qqmlcontext_source_resolver_p.h>
#include <QtQuick3DSpatialAudio/private/qquick3daudioengine_p.h>
#include <QtSpatialAudio/qambientsound.h>
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 55, as _ZN20QQuick3DAmbientSound9setSourceERK4QUrl
inline void QQuick3DAmbientSound::setSource(const QUrl& source)
{
    m_sound->setSource(source);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 50, as _ZNK20QQuick3DAmbientSound6sourceEv
inline QUrl QQuick3DAmbientSound::source() const
{
    return m_sound->source();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 65, as _ZN20QQuick3DAmbientSound9setVolumeEf
inline void QQuick3DAmbientSound::setVolume(float volume)
{
    m_sound->setVolume(volume);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 70, as _ZNK20QQuick3DAmbientSound6volumeEv
inline float QQuick3DAmbientSound::volume() const
{
    return m_sound->volume();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 83, as _ZNK20QQuick3DAmbientSound5loopsEv
inline int QQuick3DAmbientSound::loops() const
{
    return m_sound->loops();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 88, as _ZN20QQuick3DAmbientSound8setLoopsEi
inline void QQuick3DAmbientSound::setLoops(int loops)
{
    m_sound->setLoops(loops);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 101, as _ZNK20QQuick3DAmbientSound8autoPlayEv
inline bool QQuick3DAmbientSound::autoPlay() const
{
    return m_sound->autoPlay();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3dambientsound.cpp, line 106, as _ZN20QQuick3DAmbientSound11setAutoPlayEb
inline void QQuick3DAmbientSound::setAutoPlay(bool autoPlay)
{
    m_sound->setAutoPlay(autoPlay);
}
//  -----------------------------------------------------------------------

//  A QQuick3DAmbientSound that Python can take functions over in. Every QQuick3DAmbientSound
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAmbientSoundCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAmbientSoundCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAmbientSoundCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAmbientSoundCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAmbientSoundCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAmbientSoundCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAmbientSoundCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DAmbientSound : public QQuick3DAmbientSound {
public:
  using QQuick3DAmbientSound::QQuick3DAmbientSound;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall0 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall1 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall2 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall3 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall4 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall5 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DAmbientSoundCall6 call = reinterpret_cast<CuteQQuick3DAmbientSoundCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DAmbientSound::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DAmbientSound10metaObjectEv(
    const QQuick3DAmbientSound *self) {
  return self->metaObject();
}

//  void *QQuick3DAmbientSound::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DAmbientSound11qt_metacastEPKc(
    QQuick3DAmbientSound *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DAmbientSound::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DAmbientSound11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DAmbientSound *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DAmbientSound::~QQuick3DAmbientSound()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSoundD1Ev(QQuick3DAmbientSound *self) {
  delete self;
}

//  void QQuick3DAmbientSound::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound9setSourceERK4QUrl(
    QQuick3DAmbientSound *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QUrl QQuick3DAmbientSound::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuick3DAmbientSound6sourceEv(
    const QQuick3DAmbientSound *self) {
  return new QUrl(self->source());
}

//  void QQuick3DAmbientSound::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound9setVolumeEf(
    QQuick3DAmbientSound *self,
    float volume) {
  self->setVolume(volume);
}

//  float QQuick3DAmbientSound::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuick3DAmbientSound6volumeEv(
    const QQuick3DAmbientSound *self) {
  return self->volume();
}

//  int QQuick3DAmbientSound::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuick3DAmbientSound5loopsEv(
    const QQuick3DAmbientSound *self) {
  return self->loops();
}

//  void QQuick3DAmbientSound::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound8setLoopsEi(
    QQuick3DAmbientSound *self,
    int loops) {
  self->setLoops(loops);
}

//  bool QQuick3DAmbientSound::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuick3DAmbientSound8autoPlayEv(
    const QQuick3DAmbientSound *self) {
  return self->autoPlay();
}

//  void QQuick3DAmbientSound::setAutoPlay(bool autoPlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound11setAutoPlayEb(
    QQuick3DAmbientSound *self,
    bool autoPlay) {
  self->setAutoPlay(autoPlay);
}

//  void QQuick3DAmbientSound::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound4playEv(QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "play()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "play()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound5pauseEv(QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pause()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pause()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound4stopEv(QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stop()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stop()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound13sourceChangedEv(
    QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::volumeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound13volumeChangedEv(
    QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "volumeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "volumeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::loopsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound12loopsChangedEv(
    QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "loopsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "loopsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DAmbientSound::autoPlayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DAmbientSound15autoPlayChangedEv(
    QQuick3DAmbientSound *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DAmbientSound")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "autoPlayChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "autoPlayChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuick3DAmbientSound, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DAmbientSound(
    QQuick3DAmbientSound *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DAmbientSound *>(self)->take(key, call);
}
