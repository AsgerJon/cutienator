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
#include <cstring>

//  A QGStreamerInterface that Python can take functions over in. Every QGStreamerInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGStreamerInterfaceCall0)(const void *, const QByteArray *, QObject *, int *);
typedef const QAudioDevice * (*CuteQGStreamerInterfaceCall1)(const void *, const QByteArray *, int *);
typedef const QAudioDevice * (*CuteQGStreamerInterfaceCall2)(const void *, const QByteArray *, int *);
class CuteQGStreamerInterface : public QGStreamerInterface {
public:
  using QGStreamerInterface::QGStreamerInterface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QGStreamerInterface25makeCustomGStreamerCameraERK10QByteArrayP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface29makeCustomGStreamerAudioInputERK10QByteArray")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGStreamerInterface30makeCustomGStreamerAudioOutputERK10QByteArray")) {
      taken[2] = call;
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

  //  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioInput(const
  //      QByteArray &gstreamerPipeline)
  QAudioDevice makeCustomGStreamerAudioInput(
      const QByteArray &gstreamerPipeline) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall1 call = reinterpret_cast<CuteQGStreamerInterfaceCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQGStreamerInterfaceCall2 call = reinterpret_cast<CuteQGStreamerInterfaceCall2>(taken[2]);
      const QAudioDevice * given = call(this, &gstreamerPipeline, &handled);
      if (handled && given) return *given;
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
