//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamerinterface.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamerinterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qvideoframe.h>
#include <cstring>

//  A QGStreamerInterface that Python can take functions over in. Every QGStreamerInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGStreamerInterfaceCall0)(const void *, const QByteArray *, QObject *, int *);
typedef void * (*CuteQGStreamerInterfaceCall1)(const void *, GstElement *, QObject *, int *);
typedef const QAudioDevice * (*CuteQGStreamerInterfaceCall2)(const void *, const QByteArray *, int *);
typedef const QAudioDevice * (*CuteQGStreamerInterfaceCall3)(const void *, const QByteArray *, int *);
typedef void * (*CuteQGStreamerInterfaceCall4)(const void *, QMediaPlayer *, int *);
typedef void * (*CuteQGStreamerInterfaceCall5)(const void *, QMediaCaptureSession *, int *);
typedef void * (*CuteQGStreamerInterfaceCall6)(const void *, const QVideoFrame *, int *);
class CuteQGStreamerInterface : public QGStreamerInterface {
public:
  using QGStreamerInterface::QGStreamerInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QGStreamerInterface25makeCustomGStreamerCameraERK10QByteArrayP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface25makeCustomGStreamerCameraEP11_GstElementP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface29makeCustomGStreamerAudioInputERK10QByteArray")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface30makeCustomGStreamerAudioOutputERK10QByteArray")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface11gstPipelineEP12QMediaPlayer")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface11gstPipelineEP20QMediaCaptureSession")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface9gstBufferERK11QVideoFrame")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QCamera *QGStreamerInterface::makeCustomGStreamerCamera(const
  //      QByteArray &gstBinDescription, QObject *parent)
  QCamera *makeCustomGStreamerCamera(
      const QByteArray &gstBinDescription,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall0 call = reinterpret_cast<CuteQGStreamerInterfaceCall0>(taken[0]);
      void * given = call(this, &gstBinDescription, parent, &handled);
      if (handled) return static_cast<QCamera *>(given);
    }
    return {};
  }

  //  QCamera *QGStreamerInterface::makeCustomGStreamerCamera(GstElement
  //      *element, QObject *parent)
  QCamera *makeCustomGStreamerCamera(
      GstElement *element,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall1 call = reinterpret_cast<CuteQGStreamerInterfaceCall1>(taken[1]);
      void * given = call(this, element, parent, &handled);
      if (handled) return static_cast<QCamera *>(given);
    }
    return {};
  }

  //  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioInput(const
  //      QByteArray &gstreamerPipeline)
  QAudioDevice makeCustomGStreamerAudioInput(
      const QByteArray &gstreamerPipeline) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall2 call = reinterpret_cast<CuteQGStreamerInterfaceCall2>(taken[2]);
      const QAudioDevice * given = call(this, &gstreamerPipeline, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QAudioDevice
  //      QGStreamerInterface::makeCustomGStreamerAudioOutput(const
  //      QByteArray &gstreamerPipeline)
  QAudioDevice makeCustomGStreamerAudioOutput(
      const QByteArray &gstreamerPipeline) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall3 call = reinterpret_cast<CuteQGStreamerInterfaceCall3>(taken[3]);
      const QAudioDevice * given = call(this, &gstreamerPipeline, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *a0)
  GstPipeline *gstPipeline(QMediaPlayer *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall4 call = reinterpret_cast<CuteQGStreamerInterfaceCall4>(taken[4]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<GstPipeline *>(given);
    }
    return {};
  }

  //  GstPipeline *QGStreamerInterface::gstPipeline(QMediaCaptureSession
  //      *a0)
  GstPipeline *gstPipeline(QMediaCaptureSession *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall5 call = reinterpret_cast<CuteQGStreamerInterfaceCall5>(taken[5]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<GstPipeline *>(given);
    }
    return {};
  }

  //  GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame &frame)
  GstBuffer *gstBuffer(const QVideoFrame &frame) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall6 call = reinterpret_cast<CuteQGStreamerInterfaceCall6>(taken[6]);
      void * given = call(this, &frame, &handled);
      if (handled) return static_cast<GstBuffer *>(given);
    }
    return {};
  }
};

//  QGStreamerInterface::~QGStreamerInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGStreamerInterfaceD1Ev(QGStreamerInterface *self) {
  delete self;
}

//  QGStreamerInterface *QGStreamerInterface::instance()
extern "C" Q_DECL_EXPORT
QGStreamerInterface *ritual_ZN19QGStreamerInterface8instanceEv() {
  return QGStreamerInterface::instance();
}

//  QCamera *QGStreamerInterface::makeCustomGStreamerCamera(const QByteArray
//      &gstBinDescription, QObject *parent)
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN19QGStreamerInterface25makeCustomGStreamerCameraERK10QByteArrayP7QObject(
    QGStreamerInterface *self,
    const QByteArray *gstBinDescription,
    QObject *parent) {
  return self->makeCustomGStreamerCamera(*gstBinDescription, parent);
}

//  QCamera *QGStreamerInterface::makeCustomGStreamerCamera(GstElement
//      *element, QObject *parent)
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN19QGStreamerInterface25makeCustomGStreamerCameraEP11_GstElementP7QObject(
    QGStreamerInterface *self,
    GstElement *element,
    QObject *parent) {
  return self->makeCustomGStreamerCamera(element, parent);
}

//  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioInput(const
//      QByteArray &gstreamerPipeline)
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN19QGStreamerInterface29makeCustomGStreamerAudioInputERK10QByteArray(
    QGStreamerInterface *self,
    const QByteArray *gstreamerPipeline) {
  return new QAudioDevice(
      self->makeCustomGStreamerAudioInput(
          *gstreamerPipeline));
}

//  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioOutput(const
//      QByteArray &gstreamerPipeline)
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN19QGStreamerInterface30makeCustomGStreamerAudioOutputERK10QByteArray(
    QGStreamerInterface *self,
    const QByteArray *gstreamerPipeline) {
  return new QAudioDevice(
      self->makeCustomGStreamerAudioOutput(
          *gstreamerPipeline));
}

//  GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *a0)
extern "C" Q_DECL_EXPORT
GstPipeline *ritual_ZN19QGStreamerInterface11gstPipelineEP12QMediaPlayer(
    QGStreamerInterface *self,
    QMediaPlayer *a0) {
  return self->gstPipeline(a0);
}

//  GstPipeline *QGStreamerInterface::gstPipeline(QMediaCaptureSession *a0)
extern "C" Q_DECL_EXPORT
GstPipeline *ritual_ZN19QGStreamerInterface11gstPipelineEP20QMediaCaptureSession(
    QGStreamerInterface *self,
    QMediaCaptureSession *a0) {
  return self->gstPipeline(a0);
}

//  GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
GstBuffer *ritual_ZN19QGStreamerInterface9gstBufferERK11QVideoFrame(
    QGStreamerInterface *self,
    const QVideoFrame *frame) {
  return self->gstBuffer(*frame);
}

//  QVideoFrame QGStreamerInterface::createFrameFromGstBuffer(GstBuffer
//      *buffer, const GstVideoInfo &videoInfo)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN19QGStreamerInterface24createFrameFromGstBufferEP10_GstBufferRK13_GstVideoInfo(
    QGStreamerInterface *self,
    GstBuffer *buffer,
    const GstVideoInfo *videoInfo) {
  return new QVideoFrame(self->createFrameFromGstBuffer(buffer, *videoInfo));
}

//  QVideoFrame QGStreamerInterface::createFrameFromGstBuffer(GstBuffer
//      *buffer, const GstVideoInfoDmaDrm &videoInfo)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN19QGStreamerInterface24createFrameFromGstBufferEP10_GstBufferRK19_GstVideoInfoDmaDrm(
    QGStreamerInterface *self,
    GstBuffer *buffer,
    const GstVideoInfoDmaDrm *videoInfo) {
  return new QVideoFrame(self->createFrameFromGstBuffer(buffer, *videoInfo));
}

//  a Python function taken by a CuteQGStreamerInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGStreamerInterface(
    QGStreamerInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGStreamerInterface *>(self)->take(key, call);
}

#endif  // QT_CONFIG(gstreamer_qt_api)
