//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediarecorder.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediarecorder.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtMultimedia/qmediaformat.h>
#include <QtCore/qsize.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMediaRecorder that Python can take functions over in. Every QMediaRecorder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaRecorderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaRecorderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaRecorderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaRecorderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaRecorderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaRecorderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaRecorderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMediaRecorder : public QMediaRecorder {
public:
  using QMediaRecorder::QMediaRecorder;
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
      CuteQMediaRecorderCall0 call = reinterpret_cast<CuteQMediaRecorderCall0>(taken[0]);
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
      CuteQMediaRecorderCall1 call = reinterpret_cast<CuteQMediaRecorderCall1>(taken[1]);
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
      CuteQMediaRecorderCall2 call = reinterpret_cast<CuteQMediaRecorderCall2>(taken[2]);
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
      CuteQMediaRecorderCall3 call = reinterpret_cast<CuteQMediaRecorderCall3>(taken[3]);
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
      CuteQMediaRecorderCall4 call = reinterpret_cast<CuteQMediaRecorderCall4>(taken[4]);
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
      CuteQMediaRecorderCall5 call = reinterpret_cast<CuteQMediaRecorderCall5>(taken[5]);
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
      CuteQMediaRecorderCall6 call = reinterpret_cast<CuteQMediaRecorderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMediaRecorder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QMediaRecorder10metaObjectEv(
    const QMediaRecorder *self) {
  return self->metaObject();
}

//  QString QMediaRecorder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QMediaRecorder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMediaRecorder::tr(s, c, n));
}

//  QMediaRecorder::QMediaRecorder(QObject *parent)
extern "C" Q_DECL_EXPORT
QMediaRecorder *ritual_ZN14QMediaRecorderC1EP7QObject(QObject *parent) {
  return new CuteQMediaRecorder(parent);
}

//  QMediaRecorder::~QMediaRecorder()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorderD1Ev(QMediaRecorder *self) {
  delete self;
}

//  bool QMediaRecorder::isAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMediaRecorder11isAvailableEv(const QMediaRecorder *self) {
  return self->isAvailable();
}

//  QUrl QMediaRecorder::outputLocation() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QMediaRecorder14outputLocationEv(
    const QMediaRecorder *self) {
  return new QUrl(self->outputLocation());
}

//  void QMediaRecorder::setOutputLocation(const QUrl &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder17setOutputLocationERK4QUrl(
    QMediaRecorder *self,
    const QUrl *location) {
  self->setOutputLocation(*location);
}

//  void QMediaRecorder::setOutputDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder15setOutputDeviceEP9QIODevice(
    QMediaRecorder *self,
    QIODevice *device) {
  self->setOutputDevice(device);
}

//  QIODevice *QMediaRecorder::outputDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK14QMediaRecorder12outputDeviceEv(
    const QMediaRecorder *self) {
  return self->outputDevice();
}

//  QUrl QMediaRecorder::actualLocation() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QMediaRecorder14actualLocationEv(
    const QMediaRecorder *self) {
  return new QUrl(self->actualLocation());
}

//  RecorderState QMediaRecorder::recorderState() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::RecorderState ritual_ZNK14QMediaRecorder13recorderStateEv(
    const QMediaRecorder *self) {
  return self->recorderState();
}

//  Error QMediaRecorder::error() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::Error ritual_ZNK14QMediaRecorder5errorEv(
    const QMediaRecorder *self) {
  return self->error();
}

//  QString QMediaRecorder::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QMediaRecorder11errorStringEv(
    const QMediaRecorder *self) {
  return new QString(self->errorString());
}

//  qint64 QMediaRecorder::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QMediaRecorder8durationEv(const QMediaRecorder *self) {
  return self->duration();
}

//  QMediaFormat QMediaRecorder::mediaFormat() const
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZNK14QMediaRecorder11mediaFormatEv(
    const QMediaRecorder *self) {
  return new QMediaFormat(self->mediaFormat());
}

//  void QMediaRecorder::setMediaFormat(const QMediaFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder14setMediaFormatERK12QMediaFormat(
    QMediaRecorder *self,
    const QMediaFormat *format) {
  self->setMediaFormat(*format);
}

//  EncodingMode QMediaRecorder::encodingMode() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::EncodingMode ritual_ZNK14QMediaRecorder12encodingModeEv(
    const QMediaRecorder *self) {
  return self->encodingMode();
}

//  void QMediaRecorder::setEncodingMode(EncodingMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder15setEncodingModeENS_12EncodingModeE(
    QMediaRecorder *self,
    QMediaRecorder::EncodingMode a0) {
  self->setEncodingMode(a0);
}

//  Quality QMediaRecorder::quality() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::Quality ritual_ZNK14QMediaRecorder7qualityEv(
    const QMediaRecorder *self) {
  return self->quality();
}

//  void QMediaRecorder::setQuality(Quality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder10setQualityENS_7QualityE(
    QMediaRecorder *self,
    QMediaRecorder::Quality quality) {
  self->setQuality(quality);
}

//  QSize QMediaRecorder::videoResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QMediaRecorder15videoResolutionEv(
    const QMediaRecorder *self) {
  return new QSize(self->videoResolution());
}

//  void QMediaRecorder::setVideoResolution(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder18setVideoResolutionERK5QSize(
    QMediaRecorder *self,
    const QSize *a0) {
  self->setVideoResolution(*a0);
}

//  void QMediaRecorder::setVideoResolution(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder18setVideoResolutionEii(
    QMediaRecorder *self,
    int width,
    int height) {
  self->setVideoResolution(width, height);
}

//  qreal QMediaRecorder::videoFrameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QMediaRecorder14videoFrameRateEv(
    const QMediaRecorder *self) {
  return self->videoFrameRate();
}

//  void QMediaRecorder::setVideoFrameRate(qreal frameRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder17setVideoFrameRateEd(
    QMediaRecorder *self,
    qreal frameRate) {
  self->setVideoFrameRate(frameRate);
}

//  int QMediaRecorder::videoBitRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMediaRecorder12videoBitRateEv(const QMediaRecorder *self) {
  return self->videoBitRate();
}

//  void QMediaRecorder::setVideoBitRate(int bitRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder15setVideoBitRateEi(
    QMediaRecorder *self,
    int bitRate) {
  self->setVideoBitRate(bitRate);
}

//  int QMediaRecorder::audioBitRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMediaRecorder12audioBitRateEv(const QMediaRecorder *self) {
  return self->audioBitRate();
}

//  void QMediaRecorder::setAudioBitRate(int bitRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder15setAudioBitRateEi(
    QMediaRecorder *self,
    int bitRate) {
  self->setAudioBitRate(bitRate);
}

//  int QMediaRecorder::audioChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMediaRecorder17audioChannelCountEv(
    const QMediaRecorder *self) {
  return self->audioChannelCount();
}

//  void QMediaRecorder::setAudioChannelCount(int channels)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder20setAudioChannelCountEi(
    QMediaRecorder *self,
    int channels) {
  self->setAudioChannelCount(channels);
}

//  int QMediaRecorder::audioSampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMediaRecorder15audioSampleRateEv(
    const QMediaRecorder *self) {
  return self->audioSampleRate();
}

//  void QMediaRecorder::setAudioSampleRate(int sampleRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder18setAudioSampleRateEi(
    QMediaRecorder *self,
    int sampleRate) {
  self->setAudioSampleRate(sampleRate);
}

//  QMediaMetaData QMediaRecorder::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZNK14QMediaRecorder8metaDataEv(
    const QMediaRecorder *self) {
  return new QMediaMetaData(self->metaData());
}

//  void QMediaRecorder::setMetaData(const QMediaMetaData &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder11setMetaDataERK14QMediaMetaData(
    QMediaRecorder *self,
    const QMediaMetaData *metaData) {
  self->setMetaData(*metaData);
}

//  void QMediaRecorder::addMetaData(const QMediaMetaData &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder11addMetaDataERK14QMediaMetaData(
    QMediaRecorder *self,
    const QMediaMetaData *metaData) {
  self->addMetaData(*metaData);
}

//  bool QMediaRecorder::autoStop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMediaRecorder8autoStopEv(const QMediaRecorder *self) {
  return self->autoStop();
}

//  void QMediaRecorder::setAutoStop(bool autoStop)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder11setAutoStopEb(
    QMediaRecorder *self,
    bool autoStop) {
  self->setAutoStop(autoStop);
}

//  QMediaCaptureSession *QMediaRecorder::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK14QMediaRecorder14captureSessionEv(
    const QMediaRecorder *self) {
  return self->captureSession();
}

//  QPlatformMediaRecorder *QMediaRecorder::platformRecoder() const
extern "C" Q_DECL_EXPORT
QPlatformMediaRecorder *ritual_ZNK14QMediaRecorder15platformRecoderEv(
    const QMediaRecorder *self) {
  return self->platformRecoder();
}

//  void QMediaRecorder::record()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder6recordEv(QMediaRecorder *self) {
  self->record();
}

//  void QMediaRecorder::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder5pauseEv(QMediaRecorder *self) {
  self->pause();
}

//  void QMediaRecorder::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder4stopEv(QMediaRecorder *self) {
  self->stop();
}

//  void QMediaRecorder::setCaptureSession(QMediaCaptureSession *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaRecorder17setCaptureSessionEP20QMediaCaptureSession(
    QMediaRecorder *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  QMediaRecorderPrivate *QMediaRecorder::d_func()
extern "C" Q_DECL_EXPORT
QMediaRecorderPrivate *ritual_ZN14QMediaRecorder6d_funcEv(
    QMediaRecorder *self) {
  return self->d_func();
}

//  const QMediaRecorderPrivate *QMediaRecorder::d_func() const
extern "C" Q_DECL_EXPORT
const QMediaRecorderPrivate *ritual_ZNK14QMediaRecorder6d_funcEv(
    const QMediaRecorder *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMediaRecorder, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMediaRecorder(
    QMediaRecorder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMediaRecorder *>(self)->take(key, call);
}
