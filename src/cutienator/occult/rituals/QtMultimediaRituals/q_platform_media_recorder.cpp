//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QPlatformMediaRecorder that Python can take functions over in. Every QPlatformMediaRecorder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformMediaRecorderCall0)(const void *, const QUrl *, int *);
typedef int (*CuteQPlatformMediaRecorderCall1)(const void *, int *);
typedef void (*CuteQPlatformMediaRecorderCall2)(const void *, int *);
typedef void (*CuteQPlatformMediaRecorderCall3)(const void *, int *);
typedef void (*CuteQPlatformMediaRecorderCall4)(const void *, int *);
typedef qint64 (*CuteQPlatformMediaRecorderCall5)(const void *, int *);
typedef void (*CuteQPlatformMediaRecorderCall6)(const void *, const QMediaMetaData *, int *);
typedef const QMediaMetaData * (*CuteQPlatformMediaRecorderCall7)(const void *, int *);
typedef void (*CuteQPlatformMediaRecorderCall8)(const void *, const QUrl *, int *);
typedef void (*CuteQPlatformMediaRecorderCall9)(const void *, int *);
class CuteQPlatformMediaRecorder : public QPlatformMediaRecorder {
public:
  using QPlatformMediaRecorder::QPlatformMediaRecorder;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QPlatformMediaRecorder18isLocationWritableERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QPlatformMediaRecorder5stateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder5pauseEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder6resumeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder4stopEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QPlatformMediaRecorder8durationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMetaData")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QPlatformMediaRecorder8metaDataEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QPlatformMediaRecorder14updateAutoStopEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  bool QPlatformMediaRecorder::isLocationWritable(const QUrl &location)
  //      const
  bool isLocationWritable(const QUrl &location) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall0 call = reinterpret_cast<CuteQPlatformMediaRecorderCall0>(taken[0]);
      bool given = call(this, &location, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QMediaRecorder::RecorderState QPlatformMediaRecorder::state() const
  QMediaRecorder::RecorderState state() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall1 call = reinterpret_cast<CuteQPlatformMediaRecorderCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QMediaRecorder::RecorderState>(given);
    }
    return QPlatformMediaRecorder::state();
  }

  //  void QPlatformMediaRecorder::pause()
  void pause() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall2 call = reinterpret_cast<CuteQPlatformMediaRecorderCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformMediaRecorder::pause();
  }

  //  void QPlatformMediaRecorder::resume()
  void resume() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall3 call = reinterpret_cast<CuteQPlatformMediaRecorderCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformMediaRecorder::resume();
  }

  //  void QPlatformMediaRecorder::stop()
  void stop() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall4 call = reinterpret_cast<CuteQPlatformMediaRecorderCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qint64 QPlatformMediaRecorder::duration() const
  qint64 duration() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall5 call = reinterpret_cast<CuteQPlatformMediaRecorderCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaRecorder::duration();
  }

  //  void QPlatformMediaRecorder::setMetaData(const QMediaMetaData &a0)
  void setMetaData(const QMediaMetaData &a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall6 call = reinterpret_cast<CuteQPlatformMediaRecorderCall6>(taken[6]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformMediaRecorder::setMetaData(a0);
  }

  //  QMediaMetaData QPlatformMediaRecorder::metaData() const
  QMediaMetaData metaData() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall7 call = reinterpret_cast<CuteQPlatformMediaRecorderCall7>(taken[7]);
      const QMediaMetaData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformMediaRecorder::metaData();
  }

  //  void QPlatformMediaRecorder::setOutputLocation(const QUrl &location)
  void setOutputLocation(const QUrl &location) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall8 call = reinterpret_cast<CuteQPlatformMediaRecorderCall8>(taken[8]);
      call(this, &location, &handled);
      if (handled) return;
    }
    QPlatformMediaRecorder::setOutputLocation(location);
  }

  //  void QPlatformMediaRecorder::updateAutoStop()
  void updateAutoStop() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformMediaRecorderCall9 call = reinterpret_cast<CuteQPlatformMediaRecorderCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformMediaRecorder::updateAutoStop();
  }
};

//  QPlatformMediaRecorder::~QPlatformMediaRecorder()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorderD1Ev(QPlatformMediaRecorder *self) {
  delete self;
}

//  bool QPlatformMediaRecorder::isLocationWritable(const QUrl &location)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPlatformMediaRecorder18isLocationWritableERK4QUrl(
    const QPlatformMediaRecorder *self,
    const QUrl *location) {
  return self->isLocationWritable(*location);
}

//  QMediaRecorder::RecorderState QPlatformMediaRecorder::state() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::RecorderState ritual_ZNK22QPlatformMediaRecorder5stateEv(
    const QPlatformMediaRecorder *self) {
  return self->state();
}

//  void QPlatformMediaRecorder::record(QMediaEncoderSettings &settings)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder6recordER21QMediaEncoderSettings(
    QPlatformMediaRecorder *self,
    QMediaEncoderSettings *settings) {
  self->record(*settings);
}

//  void QPlatformMediaRecorder::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder5pauseEv(
    QPlatformMediaRecorder *self) {
  self->pause();
}

//  void QPlatformMediaRecorder::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder6resumeEv(
    QPlatformMediaRecorder *self) {
  self->resume();
}

//  void QPlatformMediaRecorder::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder4stopEv(QPlatformMediaRecorder *self) {
  self->stop();
}

//  qint64 QPlatformMediaRecorder::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QPlatformMediaRecorder8durationEv(
    const QPlatformMediaRecorder *self) {
  return self->duration();
}

//  void QPlatformMediaRecorder::setMetaData(const QMediaMetaData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMetaData(
    QPlatformMediaRecorder *self,
    const QMediaMetaData *a0) {
  self->setMetaData(*a0);
}

//  QMediaMetaData QPlatformMediaRecorder::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZNK22QPlatformMediaRecorder8metaDataEv(
    const QPlatformMediaRecorder *self) {
  return new QMediaMetaData(self->metaData());
}

//  QMediaRecorder::Error QPlatformMediaRecorder::error() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::Error ritual_ZNK22QPlatformMediaRecorder5errorEv(
    const QPlatformMediaRecorder *self) {
  return self->error();
}

//  QString QPlatformMediaRecorder::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QPlatformMediaRecorder11errorStringEv(
    const QPlatformMediaRecorder *self) {
  return new QString(self->errorString());
}

//  QUrl QPlatformMediaRecorder::outputLocation() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QPlatformMediaRecorder14outputLocationEv(
    const QPlatformMediaRecorder *self) {
  return new QUrl(self->outputLocation());
}

//  void QPlatformMediaRecorder::setOutputLocation(const QUrl &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl(
    QPlatformMediaRecorder *self,
    const QUrl *location) {
  self->setOutputLocation(*location);
}

//  QUrl QPlatformMediaRecorder::actualLocation() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QPlatformMediaRecorder14actualLocationEv(
    const QPlatformMediaRecorder *self) {
  return new QUrl(self->actualLocation());
}

//  void QPlatformMediaRecorder::clearActualLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder19clearActualLocationEv(
    QPlatformMediaRecorder *self) {
  self->clearActualLocation();
}

//  void QPlatformMediaRecorder::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder10clearErrorEv(
    QPlatformMediaRecorder *self) {
  self->clearError();
}

//  QIODevice *QPlatformMediaRecorder::outputDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK22QPlatformMediaRecorder12outputDeviceEv(
    const QPlatformMediaRecorder *self) {
  return self->outputDevice();
}

//  void QPlatformMediaRecorder::setOutputDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder15setOutputDeviceEP9QIODevice(
    QPlatformMediaRecorder *self,
    QIODevice *device) {
  self->setOutputDevice(device);
}

//  void QPlatformMediaRecorder::updateAutoStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder14updateAutoStopEv(
    QPlatformMediaRecorder *self) {
  self->updateAutoStop();
}

//  void QPlatformMediaRecorder::stateChanged(QMediaRecorder::RecorderState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder12stateChangedEN14QMediaRecorder13RecorderStateE(
    QPlatformMediaRecorder *self,
    QMediaRecorder::RecorderState state) {
  self->stateChanged(state);
}

//  void QPlatformMediaRecorder::durationChanged(qint64 position)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder15durationChangedEx(
    QPlatformMediaRecorder *self,
    qint64 position) {
  self->durationChanged(position);
}

//  void QPlatformMediaRecorder::actualLocationChanged(const QUrl &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder21actualLocationChangedERK4QUrl(
    QPlatformMediaRecorder *self,
    const QUrl *location) {
  self->actualLocationChanged(*location);
}

//  void QPlatformMediaRecorder::updateError(QMediaRecorder::Error error,
//      const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder11updateErrorEN14QMediaRecorder5ErrorERK7QString(
    QPlatformMediaRecorder *self,
    QMediaRecorder::Error error,
    const QString *errorString) {
  self->updateError(error, *errorString);
}

//  void QPlatformMediaRecorder::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformMediaRecorder15metaDataChangedEv(
    QPlatformMediaRecorder *self) {
  self->metaDataChanged();
}

//  QMediaRecorder *QPlatformMediaRecorder::mediaRecorder()
extern "C" Q_DECL_EXPORT
QMediaRecorder *ritual_ZN22QPlatformMediaRecorder13mediaRecorderEv(
    QPlatformMediaRecorder *self) {
  return self->mediaRecorder();
}

//  QString QPlatformMediaRecorder::findActualLocation(const
//      QMediaEncoderSettings &settings) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QPlatformMediaRecorder18findActualLocationERK21QMediaEncoderSettings(
    const QPlatformMediaRecorder *self,
    const QMediaEncoderSettings *settings) {
  return new QString(self->findActualLocation(*settings));
}

//  a Python function taken by a CuteQPlatformMediaRecorder, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMediaRecorder(
    QPlatformMediaRecorder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMediaRecorder *>(self)->take(key, call);
}

//  QMediaRecorder::RecorderState QPlatformMediaRecorder::state() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::RecorderState ritual_own_ZNK22QPlatformMediaRecorder5stateEv(
    const QPlatformMediaRecorder *self) {
  return self->QPlatformMediaRecorder::state();
}

//  void QPlatformMediaRecorder::pause()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformMediaRecorder5pauseEv(
    QPlatformMediaRecorder *self) {
  self->QPlatformMediaRecorder::pause();
}

//  void QPlatformMediaRecorder::resume()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformMediaRecorder6resumeEv(
    QPlatformMediaRecorder *self) {
  self->QPlatformMediaRecorder::resume();
}

//  qint64 QPlatformMediaRecorder::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK22QPlatformMediaRecorder8durationEv(
    const QPlatformMediaRecorder *self) {
  return self->QPlatformMediaRecorder::duration();
}

//  void QPlatformMediaRecorder::setMetaData(const QMediaMetaData &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformMediaRecorder11setMetaDataERK14QMediaMetaData(
    QPlatformMediaRecorder *self,
    const QMediaMetaData *a0) {
  self->QPlatformMediaRecorder::setMetaData(*a0);
}

//  QMediaMetaData QPlatformMediaRecorder::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_own_ZNK22QPlatformMediaRecorder8metaDataEv(
    const QPlatformMediaRecorder *self) {
  return new QMediaMetaData(self->QPlatformMediaRecorder::metaData());
}

//  void QPlatformMediaRecorder::setOutputLocation(const QUrl &location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformMediaRecorder17setOutputLocationERK4QUrl(
    QPlatformMediaRecorder *self,
    const QUrl *location) {
  self->QPlatformMediaRecorder::setOutputLocation(*location);
}

//  void QPlatformMediaRecorder::updateAutoStop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformMediaRecorder14updateAutoStopEv(
    QPlatformMediaRecorder *self) {
  self->QPlatformMediaRecorder::updateAutoStop();
}
