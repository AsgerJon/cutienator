//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintdevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QOpenGLPaintDevicePrivate that Python can take functions over in. Every QOpenGLPaintDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpenGLPaintDevicePrivateCall0)(const void *, int *);
typedef void (*CuteQOpenGLPaintDevicePrivateCall1)(const void *, int *);
class CuteQOpenGLPaintDevicePrivate : public QOpenGLPaintDevicePrivate {
public:
  using QOpenGLPaintDevicePrivate::QOpenGLPaintDevicePrivate;
  CuteQOpenGLPaintDevicePrivate(const QOpenGLPaintDevicePrivate &other) : QOpenGLPaintDevicePrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QOpenGLPaintDevicePrivate10beginPaintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QOpenGLPaintDevicePrivate8endPaintEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QOpenGLPaintDevicePrivate::beginPaint()
  void beginPaint() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLPaintDevicePrivateCall0 call = reinterpret_cast<CuteQOpenGLPaintDevicePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLPaintDevicePrivate::beginPaint();
  }

  //  void QOpenGLPaintDevicePrivate::endPaint()
  void endPaint() override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLPaintDevicePrivateCall1 call = reinterpret_cast<CuteQOpenGLPaintDevicePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLPaintDevicePrivate::endPaint();
  }
};

//  QOpenGLPaintDevicePrivate::QOpenGLPaintDevicePrivate(const QSize &size)
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevicePrivate *ritual_ZN25QOpenGLPaintDevicePrivateC1ERK5QSize(
    const QSize *size) {
  return new CuteQOpenGLPaintDevicePrivate(*size);
}

//  QOpenGLPaintDevicePrivate::~QOpenGLPaintDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLPaintDevicePrivateD1Ev(
    QOpenGLPaintDevicePrivate *self) {
  delete self;
}

//  QOpenGLPaintDevicePrivate
//      *QOpenGLPaintDevicePrivate::get(QOpenGLPaintDevice *dev)
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevicePrivate *ritual_ZN25QOpenGLPaintDevicePrivate3getEP18QOpenGLPaintDevice(
    QOpenGLPaintDevice *dev) {
  return QOpenGLPaintDevicePrivate::get(dev);
}

//  void QOpenGLPaintDevicePrivate::beginPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLPaintDevicePrivate10beginPaintEv(
    QOpenGLPaintDevicePrivate *self) {
  self->beginPaint();
}

//  void QOpenGLPaintDevicePrivate::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLPaintDevicePrivate8endPaintEv(
    QOpenGLPaintDevicePrivate *self) {
  self->endPaint();
}

//  a Python function taken by a CuteQOpenGLPaintDevicePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLPaintDevicePrivate(
    QOpenGLPaintDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLPaintDevicePrivate *>(self)->take(key, call);
}

//  void QOpenGLPaintDevicePrivate::beginPaint()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QOpenGLPaintDevicePrivate10beginPaintEv(
    QOpenGLPaintDevicePrivate *self) {
  self->QOpenGLPaintDevicePrivate::beginPaint();
}

//  void QOpenGLPaintDevicePrivate::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QOpenGLPaintDevicePrivate8endPaintEv(
    QOpenGLPaintDevicePrivate *self) {
  self->QOpenGLPaintDevicePrivate::endPaint();
}
