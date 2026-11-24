//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandXdgToplevel that Python can take functions over in. Every QWaylandXdgToplevel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandXdgToplevelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandXdgToplevelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgToplevelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgToplevelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgToplevelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgToplevelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgToplevelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandXdgToplevel : public QWaylandXdgToplevel {
public:
  using QWaylandXdgToplevel::QWaylandXdgToplevel;
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
      CuteQWaylandXdgToplevelCall0 call = reinterpret_cast<CuteQWaylandXdgToplevelCall0>(taken[0]);
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
      CuteQWaylandXdgToplevelCall1 call = reinterpret_cast<CuteQWaylandXdgToplevelCall1>(taken[1]);
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
      CuteQWaylandXdgToplevelCall2 call = reinterpret_cast<CuteQWaylandXdgToplevelCall2>(taken[2]);
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
      CuteQWaylandXdgToplevelCall3 call = reinterpret_cast<CuteQWaylandXdgToplevelCall3>(taken[3]);
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
      CuteQWaylandXdgToplevelCall4 call = reinterpret_cast<CuteQWaylandXdgToplevelCall4>(taken[4]);
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
      CuteQWaylandXdgToplevelCall5 call = reinterpret_cast<CuteQWaylandXdgToplevelCall5>(taken[5]);
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
      CuteQWaylandXdgToplevelCall6 call = reinterpret_cast<CuteQWaylandXdgToplevelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandXdgToplevel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QWaylandXdgToplevel10metaObjectEv(
    const QWaylandXdgToplevel *self) {
  return self->metaObject();
}

//  QString QWaylandXdgToplevel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QWaylandXdgToplevel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgToplevel::tr(s, c, n));
}

//  QWaylandXdgToplevel::~QWaylandXdgToplevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevelD1Ev(QWaylandXdgToplevel *self) {
  delete self;
}

//  QWaylandXdgSurface *QWaylandXdgToplevel::xdgSurface() const
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZNK19QWaylandXdgToplevel10xdgSurfaceEv(
    const QWaylandXdgToplevel *self) {
  return self->xdgSurface();
}

//  QWaylandXdgToplevel *QWaylandXdgToplevel::parentToplevel() const
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel *ritual_ZNK19QWaylandXdgToplevel14parentToplevelEv(
    const QWaylandXdgToplevel *self) {
  return self->parentToplevel();
}

//  QString QWaylandXdgToplevel::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWaylandXdgToplevel5titleEv(
    const QWaylandXdgToplevel *self) {
  return new QString(self->title());
}

//  QString QWaylandXdgToplevel::appId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWaylandXdgToplevel5appIdEv(
    const QWaylandXdgToplevel *self) {
  return new QString(self->appId());
}

//  QSize QWaylandXdgToplevel::maxSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWaylandXdgToplevel7maxSizeEv(
    const QWaylandXdgToplevel *self) {
  return new QSize(self->maxSize());
}

//  QSize QWaylandXdgToplevel::minSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWaylandXdgToplevel7minSizeEv(
    const QWaylandXdgToplevel *self) {
  return new QSize(self->minSize());
}

//  bool QWaylandXdgToplevel::maximized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel9maximizedEv(
    const QWaylandXdgToplevel *self) {
  return self->maximized();
}

//  bool QWaylandXdgToplevel::fullscreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel10fullscreenEv(
    const QWaylandXdgToplevel *self) {
  return self->fullscreen();
}

//  bool QWaylandXdgToplevel::resizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel8resizingEv(
    const QWaylandXdgToplevel *self) {
  return self->resizing();
}

//  bool QWaylandXdgToplevel::activated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel9activatedEv(
    const QWaylandXdgToplevel *self) {
  return self->activated();
}

//  DecorationMode QWaylandXdgToplevel::decorationMode() const
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel::DecorationMode ritual_ZNK19QWaylandXdgToplevel14decorationModeEv(
    const QWaylandXdgToplevel *self) {
  return self->decorationMode();
}

//  QSize QWaylandXdgToplevel::sizeForResize(const QSizeF &size, const
//      QPointF &delta, Qt::Edges edges) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWaylandXdgToplevel13sizeForResizeERK6QSizeFRK7QPointF6QFlagsIN2Qt4EdgeEE(
    const QWaylandXdgToplevel *self,
    const QSizeF *size,
    const QPointF *delta,
    int edges) {
  return new QSize(
      self->sizeForResize(
          *size,
          *delta,
          QFlags<Qt::Edge>::fromInt(edges)));
}

//  void QWaylandXdgToplevel::sendClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel9sendCloseEv(QWaylandXdgToplevel *self) {
  self->sendClose();
}

//  uint QWaylandXdgToplevel::sendMaximized(const QSize &size)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel13sendMaximizedERK5QSize(
    QWaylandXdgToplevel *self,
    const QSize *size) {
  return self->sendMaximized(*size);
}

//  uint QWaylandXdgToplevel::sendUnmaximized(const QSize &size)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel15sendUnmaximizedERK5QSize(
    QWaylandXdgToplevel *self,
    const QSize *size) {
  return self->sendUnmaximized(*size);
}

//  uint QWaylandXdgToplevel::sendFullscreen(const QSize &size)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel14sendFullscreenERK5QSize(
    QWaylandXdgToplevel *self,
    const QSize *size) {
  return self->sendFullscreen(*size);
}

//  uint QWaylandXdgToplevel::sendResizing(const QSize &size)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel12sendResizingERK5QSize(
    QWaylandXdgToplevel *self,
    const QSize *size) {
  return self->sendResizing(*size);
}

//  QWaylandSurfaceRole *QWaylandXdgToplevel::role()
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZN19QWaylandXdgToplevel4roleEv() {
  return QWaylandXdgToplevel::role();
}

//  bool QWaylandXdgToplevel::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel7isModalEv(
    const QWaylandXdgToplevel *self) {
  return self->isModal();
}

//  void QWaylandXdgToplevel::setModal(bool newModal)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel8setModalEb(
    QWaylandXdgToplevel *self,
    bool newModal) {
  self->setModal(newModal);
}

//  a Python function taken by a CuteQWaylandXdgToplevel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandXdgToplevel(
    QWaylandXdgToplevel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandXdgToplevel *>(self)->take(key, call);
}
