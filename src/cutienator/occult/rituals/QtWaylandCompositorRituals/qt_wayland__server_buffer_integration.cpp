//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QtWayland::ServerBufferIntegration that Python can take functions over in. Every QtWayland::ServerBufferIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQtWayland_ServerBufferIntegrationCall0)(const void *, QWaylandCompositor *, int *);
typedef bool (*CuteQtWayland_ServerBufferIntegrationCall1)(const void *, int, int *);
typedef void * (*CuteQtWayland_ServerBufferIntegrationCall2)(const void *, const QImage *, int, int *);
typedef void * (*CuteQtWayland_ServerBufferIntegrationCall3)(const void *, const QByteArrayView *, const QSize *, uint, int *);
class CuteQtWayland_ServerBufferIntegration : public QtWayland::ServerBufferIntegration {
public:
  using QtWayland::ServerBufferIntegration::ServerBufferIntegration;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtWayland23ServerBufferIntegration18initializeHardwareEP18QWaylandCompositor")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland23ServerBufferIntegration14supportsFormatENS_12ServerBuffer6FormatE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland23ServerBufferIntegration27createServerBufferFromImageERK6QImageNS_12ServerBuffer6FormatE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland23ServerBufferIntegration26createServerBufferFromDataE14QByteArrayViewRK5QSizej")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QtWayland::ServerBufferIntegration::initializeHardware(QWaylandC
  //      ompositor *a0)
  bool initializeHardware(QWaylandCompositor *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_ServerBufferIntegrationCall0 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QtWayland::ServerBufferIntegration::initializeHardware(a0);
  }

  //  bool QtWayland::ServerBufferIntegration::supportsFormat(ServerBuffer:
  //      :Format format) const
  bool supportsFormat(
      QtWayland::ServerBuffer::Format format) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_ServerBufferIntegrationCall1 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationCall1>(taken[1]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  ServerBuffer *QtWayland::ServerBufferIntegration::createServerBufferF
  //      romImage(const QImage &qimage, ServerBuffer::Format format)
  QtWayland::ServerBuffer *createServerBufferFromImage(
      const QImage &qimage,
      QtWayland::ServerBuffer::Format format) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_ServerBufferIntegrationCall2 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationCall2>(taken[2]);
      void * given = call(this, &qimage, static_cast<int>(format), &handled);
      if (handled) return static_cast<QtWayland::ServerBuffer *>(given);
    }
    return {};
  }

  //  ServerBuffer *QtWayland::ServerBufferIntegration::createServerBufferF
  //      romData(QByteArrayView view, const QSize &size, uint
  //      glInternalFormat)
  QtWayland::ServerBuffer *createServerBufferFromData(
      QByteArrayView view,
      const QSize &size,
      uint glInternalFormat) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_ServerBufferIntegrationCall3 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationCall3>(taken[3]);
      void * given = call(this, &view, &size, glInternalFormat, &handled);
      if (handled) return static_cast<QtWayland::ServerBuffer *>(given);
    }
    return QtWayland::ServerBufferIntegration::createServerBufferFromData(view, size, glInternalFormat);
  }
};

//  QtWayland::ServerBufferIntegration::ServerBufferIntegration()
extern "C" Q_DECL_EXPORT
QtWayland::ServerBufferIntegration *ritual_ZN9QtWayland23ServerBufferIntegrationC1Ev() {
  return new CuteQtWayland_ServerBufferIntegration();
}

//  QtWayland::ServerBufferIntegration::~ServerBufferIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland23ServerBufferIntegrationD1Ev(
    QtWayland::ServerBufferIntegration *self) {
  delete self;
}

//  bool
//      QtWayland::ServerBufferIntegration::initializeHardware(QWaylandCompos
//      itor *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland23ServerBufferIntegration18initializeHardwareEP18QWaylandCompositor(
    QtWayland::ServerBufferIntegration *self,
    QWaylandCompositor *a0) {
  return self->initializeHardware(a0);
}

//  bool
//      QtWayland::ServerBufferIntegration::supportsFormat(ServerBuffer::Form
//      at format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtWayland23ServerBufferIntegration14supportsFormatENS_12ServerBuffer6FormatE(
    const QtWayland::ServerBufferIntegration *self,
    QtWayland::ServerBuffer::Format format) {
  return self->supportsFormat(format);
}

//  ServerBuffer
//      *QtWayland::ServerBufferIntegration::createServerBufferFromImage(cons
//      t QImage &qimage, ServerBuffer::Format format)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBuffer *ritual_ZN9QtWayland23ServerBufferIntegration27createServerBufferFromImageERK6QImageNS_12ServerBuffer6FormatE(
    QtWayland::ServerBufferIntegration *self,
    const QImage *qimage,
    QtWayland::ServerBuffer::Format format) {
  return self->createServerBufferFromImage(*qimage, format);
}

//  ServerBuffer *QtWayland::ServerBufferIntegration::createServerBufferFromD
//      ata(QByteArrayView view, const QSize &size, uint glInternalFormat)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBuffer *ritual_ZN9QtWayland23ServerBufferIntegration26createServerBufferFromDataE14QByteArrayViewRK5QSizej(
    QtWayland::ServerBufferIntegration *self,
    const QByteArrayView *view,
    const QSize *size,
    uint glInternalFormat) {
  return self->createServerBufferFromData(*view, *size, glInternalFormat);
}

//  a Python function taken by a CuteQtWayland_ServerBufferIntegration, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_ServerBufferIntegration(
    QtWayland::ServerBufferIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_ServerBufferIntegration *>(self)->take(key, call);
}

//  bool
//      QtWayland::ServerBufferIntegration::initializeHardware(QWaylandCompos
//      itor *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland23ServerBufferIntegration18initializeHardwareEP18QWaylandCompositor(
    QtWayland::ServerBufferIntegration *self,
    QWaylandCompositor *a0) {
  return self->QtWayland::ServerBufferIntegration::initializeHardware(a0);
}

//  ServerBuffer *QtWayland::ServerBufferIntegration::createServerBufferFromD
//      ata(QByteArrayView view, const QSize &size, uint glInternalFormat)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBuffer *ritual_own_ZN9QtWayland23ServerBufferIntegration26createServerBufferFromDataE14QByteArrayViewRK5QSizej(
    QtWayland::ServerBufferIntegration *self,
    const QByteArrayView *view,
    const QSize *size,
    uint glInternalFormat) {
  return self->QtWayland::ServerBufferIntegration::createServerBufferFromData(
      *view,
      *size,
      glInternalFormat);
}

#endif  // QT_CONFIG(opengl)
