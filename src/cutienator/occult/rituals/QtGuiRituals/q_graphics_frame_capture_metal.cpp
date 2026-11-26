//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgraphicsframecapturemetal_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (QT_CONFIG(graphicsframecapture)) && (defined(Q_OS_IOS) || defined(Q_OS_MACOS))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgraphicsframecapturemetal_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QGraphicsFrameCaptureMetal that Python can take functions over in. Every QGraphicsFrameCaptureMetal
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsFrameCaptureMetalCall0)(const void *, QRhi *, int *);
typedef void (*CuteQGraphicsFrameCaptureMetalCall1)(const void *, int *);
typedef void (*CuteQGraphicsFrameCaptureMetalCall2)(const void *, int *);
typedef bool (*CuteQGraphicsFrameCaptureMetalCall3)(const void *, int *);
typedef bool (*CuteQGraphicsFrameCaptureMetalCall4)(const void *, int *);
typedef void (*CuteQGraphicsFrameCaptureMetalCall5)(const void *, int *);
typedef void (*CuteQGraphicsFrameCaptureMetalCall6)(const void *, const QString *, int *);
typedef void (*CuteQGraphicsFrameCaptureMetalCall7)(const void *, const QString *, int *);
typedef QString * (*CuteQGraphicsFrameCaptureMetalCall8)(const void *, int *);
class CuteQGraphicsFrameCaptureMetal : public QGraphicsFrameCaptureMetal {
public:
  using QGraphicsFrameCaptureMetal::QGraphicsFrameCaptureMetal;
  CuteQGraphicsFrameCaptureMetal(const QGraphicsFrameCaptureMetal & other) : QGraphicsFrameCaptureMetal(other) {}
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate6setRhiEP4QRhi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate17startCaptureFrameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate15endCaptureFrameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate11initializedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate11isCapturingEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate11openCaptureEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsFrameCaptureMetal::setRhi(QRhi *rhi)
  void setRhi(QRhi *rhi) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall0 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall0>(taken[0]);
      call(this, rhi, &handled);
      if (handled) return;
    }
    QGraphicsFrameCaptureMetal::setRhi(rhi);
  }

  //  void QGraphicsFrameCaptureMetal::startCaptureFrame()
  void startCaptureFrame() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall1 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsFrameCaptureMetal::startCaptureFrame();
  }

  //  void QGraphicsFrameCaptureMetal::endCaptureFrame()
  void endCaptureFrame() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall2 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsFrameCaptureMetal::endCaptureFrame();
  }

  //  bool QGraphicsFrameCaptureMetal::initialized() const
  bool initialized() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall3 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsFrameCaptureMetal::initialized();
  }

  //  bool QGraphicsFrameCaptureMetal::isCapturing() const
  bool isCapturing() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall4 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsFrameCaptureMetal::isCapturing();
  }

  //  void QGraphicsFrameCaptureMetal::openCapture()
  void openCapture() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall5 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsFrameCaptureMetal::openCapture();
  }

  //  void QGraphicsFrameCapturePrivate::setCapturePath(const QString
  //      &path)
  void setCapturePath(const QString &path) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall6 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall6>(taken[6]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QGraphicsFrameCapturePrivate::setCapturePath(path);
  }

  //  void QGraphicsFrameCapturePrivate::setCapturePrefix(const QString
  //      &prefix)
  void setCapturePrefix(const QString &prefix) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall7 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall7>(taken[7]);
      call(this, &prefix, &handled);
      if (handled) return;
    }
    QGraphicsFrameCapturePrivate::setCapturePrefix(prefix);
  }

  //  QString QGraphicsFrameCapturePrivate::capturedFileName() const
  QString capturedFileName() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsFrameCaptureMetalCall8 call = reinterpret_cast<CuteQGraphicsFrameCaptureMetalCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGraphicsFrameCapturePrivate::capturedFileName();
  }
};

//  void QGraphicsFrameCaptureMetal::setRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsFrameCaptureMetal6setRhiEP4QRhi(
    QGraphicsFrameCaptureMetal *self,
    QRhi *rhi) {
  self->setRhi(rhi);
}

//  void QGraphicsFrameCaptureMetal::startCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsFrameCaptureMetal17startCaptureFrameEv(
    QGraphicsFrameCaptureMetal *self) {
  self->startCaptureFrame();
}

//  void QGraphicsFrameCaptureMetal::endCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsFrameCaptureMetal15endCaptureFrameEv(
    QGraphicsFrameCaptureMetal *self) {
  self->endCaptureFrame();
}

//  bool QGraphicsFrameCaptureMetal::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QGraphicsFrameCaptureMetal11initializedEv(
    const QGraphicsFrameCaptureMetal *self) {
  return self->initialized();
}

//  bool QGraphicsFrameCaptureMetal::isCapturing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QGraphicsFrameCaptureMetal11isCapturingEv(
    const QGraphicsFrameCaptureMetal *self) {
  return self->isCapturing();
}

//  void QGraphicsFrameCaptureMetal::openCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsFrameCaptureMetal11openCaptureEv(
    QGraphicsFrameCaptureMetal *self) {
  self->openCapture();
}

//  a Python function taken by a CuteQGraphicsFrameCaptureMetal, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsFrameCaptureMetal(
    QGraphicsFrameCaptureMetal *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsFrameCaptureMetal *>(self)->take(key, call);
}

//  void QGraphicsFrameCaptureMetal::setRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGraphicsFrameCaptureMetal6setRhiEP4QRhi(
    QGraphicsFrameCaptureMetal *self,
    QRhi *rhi) {
  self->QGraphicsFrameCaptureMetal::setRhi(rhi);
}

//  void QGraphicsFrameCaptureMetal::startCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGraphicsFrameCaptureMetal17startCaptureFrameEv(
    QGraphicsFrameCaptureMetal *self) {
  self->QGraphicsFrameCaptureMetal::startCaptureFrame();
}

//  void QGraphicsFrameCaptureMetal::endCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGraphicsFrameCaptureMetal15endCaptureFrameEv(
    QGraphicsFrameCaptureMetal *self) {
  self->QGraphicsFrameCaptureMetal::endCaptureFrame();
}

//  bool QGraphicsFrameCaptureMetal::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QGraphicsFrameCaptureMetal11initializedEv(
    const QGraphicsFrameCaptureMetal *self) {
  return self->QGraphicsFrameCaptureMetal::initialized();
}

//  bool QGraphicsFrameCaptureMetal::isCapturing() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QGraphicsFrameCaptureMetal11isCapturingEv(
    const QGraphicsFrameCaptureMetal *self) {
  return self->QGraphicsFrameCaptureMetal::isCapturing();
}

//  void QGraphicsFrameCaptureMetal::openCapture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGraphicsFrameCaptureMetal11openCaptureEv(
    QGraphicsFrameCaptureMetal *self) {
  self->QGraphicsFrameCaptureMetal::openCapture();
}

#endif  // (QT_CONFIG(graphicsframecapture)) && (defined(Q_OS_IOS) || defined(Q_OS_MACOS))
