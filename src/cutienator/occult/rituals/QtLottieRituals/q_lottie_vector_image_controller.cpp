//  Written by hand on 2026-11-25 from
//  QtLottie/6.12.0/QtLottie/private/qlottievectorimagecontroller_p.h, Qt
//  6.12.0, as the Qt of macOS and of Windows installs it (the two texts
//  are the same). Kept as it is when the generator runs again. Linux's
//  reader refused the header in the folder it made from Qt's source; its
//  text compiles against an installed Qt, so the file stands under no
//  system '#if'. Not written: the signals.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottievectorimagecontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QLottieVectorImageController that Python can take functions over in. Every
//  QLottieVectorImageController Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQLottieVectorImageControllerCall0)(const void *, int *);
typedef void (*CuteQLottieVectorImageControllerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLottieVectorImageControllerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLottieVectorImageControllerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieVectorImageControllerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieVectorImageControllerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieVectorImageControllerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieVectorImageControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieVectorImageControllerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLottieVectorImageController : public QLottieVectorImageController {
public:
  using QLottieVectorImageController::QLottieVectorImageController;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QLottieVectorImageController::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall0 call = reinterpret_cast<CuteQLottieVectorImageControllerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QLottieVectorImageController::classBegin();
  }

  //  void QLottieVectorImageController::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall1 call = reinterpret_cast<CuteQLottieVectorImageControllerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QLottieVectorImageController::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall2 call = reinterpret_cast<CuteQLottieVectorImageControllerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall3 call = reinterpret_cast<CuteQLottieVectorImageControllerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall4 call = reinterpret_cast<CuteQLottieVectorImageControllerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall5 call = reinterpret_cast<CuteQLottieVectorImageControllerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall6 call = reinterpret_cast<CuteQLottieVectorImageControllerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall7 call = reinterpret_cast<CuteQLottieVectorImageControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieVectorImageControllerCall8 call = reinterpret_cast<CuteQLottieVectorImageControllerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLottieVectorImageController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QLottieVectorImageController10metaObjectEv(
    const QLottieVectorImageController *self) {
  return self->metaObject();
}

//  QString QLottieVectorImageController::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QLottieVectorImageController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLottieVectorImageController::tr(s, c, n));
}

//  QLottieVectorImageController::QLottieVectorImageController(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QLottieVectorImageController *ritual_ZN28QLottieVectorImageControllerC1EP7QObject(
    QObject *parent) {
  return new CuteQLottieVectorImageController(parent);
}

//  void QLottieVectorImageController::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController10classBeginEv(
    QLottieVectorImageController *self) {
  self->classBegin();
}

//  void QLottieVectorImageController::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController17componentCompleteEv(
    QLottieVectorImageController *self) {
  self->componentComplete();
}

//  QQuickVectorImage *QLottieVectorImageController::target() const
extern "C" Q_DECL_EXPORT
QQuickVectorImage *ritual_ZNK28QLottieVectorImageController6targetEv(
    const QLottieVectorImageController *self) {
  return self->target();
}

//  void QLottieVectorImageController::setTarget(QQuickVectorImage
//      *newTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController9setTargetEP17QQuickVectorImage(
    QLottieVectorImageController *self,
    QQuickVectorImage *newTarget) {
  self->setTarget(newTarget);
}

//  qreal QLottieVectorImageController::frameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieVectorImageController9frameRateEv(
    const QLottieVectorImageController *self) {
  return self->frameRate();
}

//  void QLottieVectorImageController::setFrameRate(qreal newFrameRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController12setFrameRateEd(
    QLottieVectorImageController *self,
    qreal newFrameRate) {
  self->setFrameRate(newFrameRate);
}

//  void QLottieVectorImageController::resetFrameRate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController14resetFrameRateEv(
    QLottieVectorImageController *self) {
  self->resetFrameRate();
}

//  qreal QLottieVectorImageController::startFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieVectorImageController10startFrameEv(
    const QLottieVectorImageController *self) {
  return self->startFrame();
}

//  qreal QLottieVectorImageController::endFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieVectorImageController8endFrameEv(
    const QLottieVectorImageController *self) {
  return self->endFrame();
}

//  qreal QLottieVectorImageController::currentFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieVectorImageController12currentFrameEv(
    const QLottieVectorImageController *self) {
  return self->currentFrame();
}

//  void QLottieVectorImageController::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController4playEv(
    QLottieVectorImageController *self) {
  self->play();
}

//  void QLottieVectorImageController::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController5pauseEv(
    QLottieVectorImageController *self) {
  self->pause();
}

//  void QLottieVectorImageController::togglePause()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController11togglePauseEv(
    QLottieVectorImageController *self) {
  self->togglePause();
}

//  void QLottieVectorImageController::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController5startEv(
    QLottieVectorImageController *self) {
  self->start();
}

//  void QLottieVectorImageController::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController4stopEv(
    QLottieVectorImageController *self) {
  self->stop();
}

//  void QLottieVectorImageController::gotoAndPlay(qreal frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController11gotoAndPlayEd(
    QLottieVectorImageController *self,
    qreal frame) {
  self->gotoAndPlay(frame);
}

//  void QLottieVectorImageController::gotoAndStop(qreal frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController11gotoAndStopEd(
    QLottieVectorImageController *self,
    qreal frame) {
  self->gotoAndStop(frame);
}

//  void QLottieVectorImageController::gotoFrame(qreal frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController9gotoFrameEd(
    QLottieVectorImageController *self,
    qreal frame) {
  self->gotoFrame(frame);
}

//  void QLottieVectorImageController::onGeneratedItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieVectorImageController22onGeneratedItemChangedEv(
    QLottieVectorImageController *self) {
  self->onGeneratedItemChanged();
}

//  a Python function taken by a CuteQLottieVectorImageController, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieVectorImageController(
    QLottieVectorImageController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieVectorImageController *>(self)->take(key, call);
}

//  void QLottieVectorImageController::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QLottieVectorImageController10classBeginEv(
    QLottieVectorImageController *self) {
  self->QLottieVectorImageController::classBegin();
}

//  void QLottieVectorImageController::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QLottieVectorImageController17componentCompleteEv(
    QLottieVectorImageController *self) {
  self->QLottieVectorImageController::componentComplete();
}
