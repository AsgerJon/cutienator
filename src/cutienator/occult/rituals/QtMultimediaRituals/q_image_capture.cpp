//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qimagecapture.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qimagecapture.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QImageCapture that Python can take functions over in. Every QImageCapture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQImageCaptureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQImageCaptureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageCaptureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageCaptureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageCaptureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageCaptureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageCaptureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQImageCapture : public QImageCapture {
public:
  using QImageCapture::QImageCapture;
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
      CuteQImageCaptureCall0 call = reinterpret_cast<CuteQImageCaptureCall0>(taken[0]);
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
      CuteQImageCaptureCall1 call = reinterpret_cast<CuteQImageCaptureCall1>(taken[1]);
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
      CuteQImageCaptureCall2 call = reinterpret_cast<CuteQImageCaptureCall2>(taken[2]);
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
      CuteQImageCaptureCall3 call = reinterpret_cast<CuteQImageCaptureCall3>(taken[3]);
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
      CuteQImageCaptureCall4 call = reinterpret_cast<CuteQImageCaptureCall4>(taken[4]);
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
      CuteQImageCaptureCall5 call = reinterpret_cast<CuteQImageCaptureCall5>(taken[5]);
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
      CuteQImageCaptureCall6 call = reinterpret_cast<CuteQImageCaptureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QImageCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QImageCapture10metaObjectEv(
    const QImageCapture *self) {
  return self->metaObject();
}

//  QString QImageCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QImageCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QImageCapture::tr(s, c, n));
}

//  QImageCapture::QImageCapture(QObject *parent)
extern "C" Q_DECL_EXPORT
QImageCapture *ritual_ZN13QImageCaptureC1EP7QObject(QObject *parent) {
  return new CuteQImageCapture(parent);
}

//  QImageCapture::~QImageCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCaptureD1Ev(QImageCapture *self) {
  delete self;
}

//  bool QImageCapture::isAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QImageCapture11isAvailableEv(const QImageCapture *self) {
  return self->isAvailable();
}

//  QMediaCaptureSession *QImageCapture::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK13QImageCapture14captureSessionEv(
    const QImageCapture *self) {
  return self->captureSession();
}

//  Error QImageCapture::error() const
extern "C" Q_DECL_EXPORT
QImageCapture::Error ritual_ZNK13QImageCapture5errorEv(
    const QImageCapture *self) {
  return self->error();
}

//  QString QImageCapture::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QImageCapture11errorStringEv(
    const QImageCapture *self) {
  return new QString(self->errorString());
}

//  bool QImageCapture::isReadyForCapture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QImageCapture17isReadyForCaptureEv(
    const QImageCapture *self) {
  return self->isReadyForCapture();
}

//  FileFormat QImageCapture::fileFormat() const
extern "C" Q_DECL_EXPORT
QImageCapture::FileFormat ritual_ZNK13QImageCapture10fileFormatEv(
    const QImageCapture *self) {
  return self->fileFormat();
}

//  void QImageCapture::setFileFormat(FileFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture13setFileFormatENS_10FileFormatE(
    QImageCapture *self,
    QImageCapture::FileFormat format) {
  self->setFileFormat(format);
}

//  QString QImageCapture::fileFormatName(FileFormat c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QImageCapture14fileFormatNameENS_10FileFormatE(
    QImageCapture::FileFormat c) {
  return new QString(QImageCapture::fileFormatName(c));
}

//  QString QImageCapture::fileFormatDescription(FileFormat c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QImageCapture21fileFormatDescriptionENS_10FileFormatE(
    QImageCapture::FileFormat c) {
  return new QString(QImageCapture::fileFormatDescription(c));
}

//  QSize QImageCapture::resolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QImageCapture10resolutionEv(const QImageCapture *self) {
  return new QSize(self->resolution());
}

//  void QImageCapture::setResolution(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture13setResolutionERK5QSize(
    QImageCapture *self,
    const QSize *a0) {
  self->setResolution(*a0);
}

//  void QImageCapture::setResolution(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture13setResolutionEii(
    QImageCapture *self,
    int width,
    int height) {
  self->setResolution(width, height);
}

//  Quality QImageCapture::quality() const
extern "C" Q_DECL_EXPORT
QImageCapture::Quality ritual_ZNK13QImageCapture7qualityEv(
    const QImageCapture *self) {
  return self->quality();
}

//  void QImageCapture::setQuality(Quality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture10setQualityENS_7QualityE(
    QImageCapture *self,
    QImageCapture::Quality quality) {
  self->setQuality(quality);
}

//  QMediaMetaData QImageCapture::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZNK13QImageCapture8metaDataEv(
    const QImageCapture *self) {
  return new QMediaMetaData(self->metaData());
}

//  void QImageCapture::setMetaData(const QMediaMetaData &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture11setMetaDataERK14QMediaMetaData(
    QImageCapture *self,
    const QMediaMetaData *metaData) {
  self->setMetaData(*metaData);
}

//  void QImageCapture::addMetaData(const QMediaMetaData &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture11addMetaDataERK14QMediaMetaData(
    QImageCapture *self,
    const QMediaMetaData *metaData) {
  self->addMetaData(*metaData);
}

//  int QImageCapture::captureToFile(const QString &location)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QImageCapture13captureToFileERK7QString(
    QImageCapture *self,
    const QString *location) {
  return self->captureToFile(*location);
}

//  int QImageCapture::capture()
extern "C" Q_DECL_EXPORT
int ritual_ZN13QImageCapture7captureEv(QImageCapture *self) {
  return self->capture();
}

//  void QImageCapture::setCaptureSession(QMediaCaptureSession *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QImageCapture17setCaptureSessionEP20QMediaCaptureSession(
    QImageCapture *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  a Python function taken by a CuteQImageCapture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QImageCapture(
    QImageCapture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQImageCapture *>(self)->take(key, call);
}
