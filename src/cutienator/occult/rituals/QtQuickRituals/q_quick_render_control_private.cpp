//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrendercontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickrendercontrol.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrendercontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquickgraphicsconfiguration.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QQuickRenderControlPrivate that Python can take functions over in. Every QQuickRenderControlPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickRenderControlPrivateCall0)(const void *, const QWindow *, int *);
class CuteQQuickRenderControlPrivate : public QQuickRenderControlPrivate {
public:
  using QQuickRenderControlPrivate::QQuickRenderControlPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWindow")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QQuickRenderControlPrivate::isRenderWindow(const QWindow *w)
  bool isRenderWindow(const QWindow *w) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRenderControlPrivateCall0 call = reinterpret_cast<CuteQQuickRenderControlPrivateCall0>(taken[0]);
      bool given = call(this, w, &handled);
      if (handled) return given;
    }
    return QQuickRenderControlPrivate::isRenderWindow(w);
  }
};

//  QQuickRenderControl *QQuickRenderControlPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickRenderControl *ritual_ZN26QQuickRenderControlPrivate6q_funcEv(
    QQuickRenderControlPrivate *self) {
  return self->q_func();
}

//  const QQuickRenderControl *QQuickRenderControlPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickRenderControl *ritual_ZNK26QQuickRenderControlPrivate6q_funcEv(
    const QQuickRenderControlPrivate *self) {
  return self->q_func();
}

//  QQuickRenderControlPrivate::QQuickRenderControlPrivate(QQuickRenderContro
//      l *renderControl)
extern "C" Q_DECL_EXPORT
QQuickRenderControlPrivate *ritual_ZN26QQuickRenderControlPrivateC1EP19QQuickRenderControl(
    QQuickRenderControl *renderControl) {
  return new CuteQQuickRenderControlPrivate(renderControl);
}

//  QQuickRenderControlPrivate
//      *QQuickRenderControlPrivate::get(QQuickRenderControl *renderControl)
extern "C" Q_DECL_EXPORT
QQuickRenderControlPrivate *ritual_ZN26QQuickRenderControlPrivate3getEP19QQuickRenderControl(
    QQuickRenderControl *renderControl) {
  return QQuickRenderControlPrivate::get(renderControl);
}

//  bool QQuickRenderControlPrivate::isRenderWindowFor(QQuickWindow
//      *quickWin, const QWindow *renderWin)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickRenderControlPrivate17isRenderWindowForEP12QQuickWindowPK7QWindow(
    QQuickWindow *quickWin,
    const QWindow *renderWin) {
  return QQuickRenderControlPrivate::isRenderWindowFor(quickWin, renderWin);
}

//  bool QQuickRenderControlPrivate::isFocusWindowFor(QQuickWindow
//      *quickWindow, const QWindow *focusWindow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickRenderControlPrivate16isFocusWindowForEP12QQuickWindowPK7QWindow(
    QQuickWindow *quickWindow,
    const QWindow *focusWindow) {
  return QQuickRenderControlPrivate::isFocusWindowFor(
      quickWindow,
      focusWindow);
}

//  bool QQuickRenderControlPrivate::isRenderWindow(const QWindow *w)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWindow(
    QQuickRenderControlPrivate *self,
    const QWindow *w) {
  return self->isRenderWindow(w);
}

//  void QQuickRenderControlPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickRenderControlPrivate7cleanupEv() {
  QQuickRenderControlPrivate::cleanup();
}

//  void QQuickRenderControlPrivate::windowDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickRenderControlPrivate15windowDestroyedEv(
    QQuickRenderControlPrivate *self) {
  self->windowDestroyed();
}

//  void QQuickRenderControlPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickRenderControlPrivate6updateEv(
    QQuickRenderControlPrivate *self) {
  self->update();
}

//  void QQuickRenderControlPrivate::maybeUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickRenderControlPrivate11maybeUpdateEv(
    QQuickRenderControlPrivate *self) {
  self->maybeUpdate();
}

//  bool QQuickRenderControlPrivate::initRhi()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickRenderControlPrivate7initRhiEv(
    QQuickRenderControlPrivate *self) {
  return self->initRhi();
}

//  void QQuickRenderControlPrivate::resetRhi(const
//      QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickRenderControlPrivate8resetRhiERK27QQuickGraphicsConfiguration(
    QQuickRenderControlPrivate *self,
    const QQuickGraphicsConfiguration *config) {
  self->resetRhi(*config);
}

//  QImage QQuickRenderControlPrivate::grab()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN26QQuickRenderControlPrivate4grabEv(
    QQuickRenderControlPrivate *self) {
  return new QImage(self->grab());
}

//  a Python function taken by a CuteQQuickRenderControlPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRenderControlPrivate(
    QQuickRenderControlPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRenderControlPrivate *>(self)->take(key, call);
}

//  bool QQuickRenderControlPrivate::isRenderWindow(const QWindow *w)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWindow(
    QQuickRenderControlPrivate *self,
    const QWindow *w) {
  return self->QQuickRenderControlPrivate::isRenderWindow(w);
}
