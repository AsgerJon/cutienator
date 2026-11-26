//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickrendercontrol.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickrendercontrol.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickRenderControl that Python can take functions over in. Every QQuickRenderControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickRenderControlCall0)(const void *, QPoint *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRenderControlCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRenderControlCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRenderControlCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRenderControlCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRenderControlCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRenderControlCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRenderControlCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRenderControl : public QQuickRenderControl {
public:
  using QQuickRenderControl::QQuickRenderControl;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickRenderControl12renderWindowEP6QPoint")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QWindow *QQuickRenderControl::renderWindow(QPoint *offset)
  QWindow *renderWindow(QPoint *offset) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRenderControlCall0 call = reinterpret_cast<CuteQQuickRenderControlCall0>(taken[0]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QQuickRenderControl::renderWindow(offset);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRenderControlCall1 call = reinterpret_cast<CuteQQuickRenderControlCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRenderControlCall2 call = reinterpret_cast<CuteQQuickRenderControlCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRenderControlCall3 call = reinterpret_cast<CuteQQuickRenderControlCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRenderControlCall4 call = reinterpret_cast<CuteQQuickRenderControlCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRenderControlCall5 call = reinterpret_cast<CuteQQuickRenderControlCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRenderControlCall6 call = reinterpret_cast<CuteQQuickRenderControlCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRenderControlCall7 call = reinterpret_cast<CuteQQuickRenderControlCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRenderControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickRenderControl10metaObjectEv(
    const QQuickRenderControl *self) {
  return self->metaObject();
}

//  void *QQuickRenderControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickRenderControl11qt_metacastEPKc(
    QQuickRenderControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRenderControl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickRenderControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRenderControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRenderControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickRenderControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRenderControl::tr(s, c, n));
}

//  QQuickRenderControl::QQuickRenderControl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickRenderControl *ritual_ZN19QQuickRenderControlC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickRenderControl(parent);
}

//  QQuickRenderControl::~QQuickRenderControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControlD1Ev(QQuickRenderControl *self) {
  delete self;
}

//  void QQuickRenderControl::prepareThread(QThread *targetThread)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl13prepareThreadEP7QThread(
    QQuickRenderControl *self,
    QThread *targetThread) {
  self->prepareThread(targetThread);
}

//  void QQuickRenderControl::setSamples(int sampleCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl10setSamplesEi(
    QQuickRenderControl *self,
    int sampleCount) {
  self->setSamples(sampleCount);
}

//  int QQuickRenderControl::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickRenderControl7samplesEv(
    const QQuickRenderControl *self) {
  return self->samples();
}

//  bool QQuickRenderControl::initialize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickRenderControl10initializeEv(
    QQuickRenderControl *self) {
  return self->initialize();
}

//  void QQuickRenderControl::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl10invalidateEv(
    QQuickRenderControl *self) {
  self->invalidate();
}

//  void QQuickRenderControl::beginFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl10beginFrameEv(
    QQuickRenderControl *self) {
  self->beginFrame();
}

//  void QQuickRenderControl::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl8endFrameEv(QQuickRenderControl *self) {
  self->endFrame();
}

//  void QQuickRenderControl::polishItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl11polishItemsEv(
    QQuickRenderControl *self) {
  self->polishItems();
}

//  bool QQuickRenderControl::sync()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickRenderControl4syncEv(QQuickRenderControl *self) {
  return self->sync();
}

//  void QQuickRenderControl::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl6renderEv(QQuickRenderControl *self) {
  self->render();
}

//  QWindow *QQuickRenderControl::renderWindowFor(QQuickWindow *win, QPoint
//      *offset)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN19QQuickRenderControl15renderWindowForEP12QQuickWindowP6QPoint(
    QQuickWindow *win,
    QPoint *offset) {
  return QQuickRenderControl::renderWindowFor(win, offset);
}

//  QWindow *QQuickRenderControl::renderWindow(QPoint *offset)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN19QQuickRenderControl12renderWindowEP6QPoint(
    QQuickRenderControl *self,
    QPoint *offset) {
  return self->renderWindow(offset);
}

//  QQuickWindow *QQuickRenderControl::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK19QQuickRenderControl6windowEv(
    const QQuickRenderControl *self) {
  return self->window();
}

//  QRhi *QQuickRenderControl::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK19QQuickRenderControl3rhiEv(
    const QQuickRenderControl *self) {
  return self->rhi();
}

//  QRhiCommandBuffer *QQuickRenderControl::commandBuffer() const
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZNK19QQuickRenderControl13commandBufferEv(
    const QQuickRenderControl *self) {
  return self->commandBuffer();
}

//  QQuickRenderControl::QQuickRenderControl(QQuickRenderControlPrivate &dd,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickRenderControl *ritual_ZN19QQuickRenderControlC1ER26QQuickRenderControlPrivateP7QObject(
    QQuickRenderControlPrivate *dd,
    QObject *parent) {
  return new CuteQQuickRenderControl(*dd, parent);
}

//  void QQuickRenderControl::renderRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl15renderRequestedEv(
    QQuickRenderControl *self) {
  self->renderRequested();
}

//  void QQuickRenderControl::sceneChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickRenderControl12sceneChangedEv(
    QQuickRenderControl *self) {
  self->sceneChanged();
}

//  QQuickRenderControlPrivate *QQuickRenderControl::d_func()
extern "C" Q_DECL_EXPORT
QQuickRenderControlPrivate *ritual_ZN19QQuickRenderControl6d_funcEv(
    QQuickRenderControl *self) {
  return self->d_func();
}

//  const QQuickRenderControlPrivate *QQuickRenderControl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRenderControlPrivate *ritual_ZNK19QQuickRenderControl6d_funcEv(
    const QQuickRenderControl *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickRenderControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRenderControl(
    QQuickRenderControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRenderControl *>(self)->take(key, call);
}

//  QWindow *QQuickRenderControl::renderWindow(QPoint *offset)
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZN19QQuickRenderControl12renderWindowEP6QPoint(
    QQuickRenderControl *self,
    QPoint *offset) {
  return self->QQuickRenderControl::renderWindow(offset);
}
