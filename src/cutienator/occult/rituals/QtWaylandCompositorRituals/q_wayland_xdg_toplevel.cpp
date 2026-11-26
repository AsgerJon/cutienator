//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtWaylandCompositor/QWaylandXdgToplevel>

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

//  void *QWaylandXdgToplevel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QWaylandXdgToplevel11qt_metacastEPKc(
    QWaylandXdgToplevel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandXdgToplevel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QWaylandXdgToplevel11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandXdgToplevel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandXdgToplevel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QWaylandXdgToplevel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgToplevel::tr(s, c, n));
}

//  QWaylandXdgToplevelPrivate *QWaylandXdgToplevel::d_func()
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevelPrivate *ritual_ZN19QWaylandXdgToplevel6d_funcEv(
    QWaylandXdgToplevel *self) {
  return self->d_func();
}

//  const QWaylandXdgToplevelPrivate *QWaylandXdgToplevel::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandXdgToplevelPrivate *ritual_ZNK19QWaylandXdgToplevel6d_funcEv(
    const QWaylandXdgToplevel *self) {
  return self->d_func();
}

//  QWaylandXdgToplevel::QWaylandXdgToplevel(QWaylandXdgSurface *xdgSurface,
//      QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel *ritual_ZN19QWaylandXdgToplevelC1EP18QWaylandXdgSurfaceR16QWaylandResource(
    QWaylandXdgSurface *xdgSurface,
    QWaylandResource *resource) {
  return new CuteQWaylandXdgToplevel(xdgSurface, *resource);
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

//  QList<QWaylandXdgToplevel::State> QWaylandXdgToplevel::states() const
extern "C" Q_DECL_EXPORT
QList<QWaylandXdgToplevel::State> *ritual_ZNK19QWaylandXdgToplevel6statesEv(
    const QWaylandXdgToplevel *self) {
  return new QList<QWaylandXdgToplevel::State>(self->states());
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

//  uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
//      QList<State> &states)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel13sendConfigureERK5QSizeRK5QListINS_5StateEE(
    QWaylandXdgToplevel *self,
    const QSize *size,
    const QList<QWaylandXdgToplevel::State> *states) {
  return self->sendConfigure(*size, *states);
}

//  uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
//      QList<int> &states)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QWaylandXdgToplevel13sendConfigureERK5QSizeRK5QListIiE(
    QWaylandXdgToplevel *self,
    const QSize *size,
    const QList<int> *states) {
  return self->sendConfigure(*size, *states);
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

//  QWaylandXdgToplevel *QWaylandXdgToplevel::fromResource(::wl_resource
//      *resource)
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel *ritual_ZN19QWaylandXdgToplevel12fromResourceEP11wl_resource(
    ::wl_resource *resource) {
  return QWaylandXdgToplevel::fromResource(resource);
}

//  bool QWaylandXdgToplevel::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandXdgToplevel7isModalEv(
    const QWaylandXdgToplevel *self) {
  return self->isModal();
}

//  void QWaylandXdgToplevel::parentToplevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel21parentToplevelChangedEv(
    QWaylandXdgToplevel *self) {
  self->parentToplevelChanged();
}

//  void QWaylandXdgToplevel::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel12titleChangedEv(
    QWaylandXdgToplevel *self) {
  self->titleChanged();
}

//  void QWaylandXdgToplevel::appIdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel12appIdChangedEv(
    QWaylandXdgToplevel *self) {
  self->appIdChanged();
}

//  void QWaylandXdgToplevel::maxSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel14maxSizeChangedEv(
    QWaylandXdgToplevel *self) {
  self->maxSizeChanged();
}

//  void QWaylandXdgToplevel::minSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel14minSizeChangedEv(
    QWaylandXdgToplevel *self) {
  self->minSizeChanged();
}

//  void QWaylandXdgToplevel::startMove(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel9startMoveEP12QWaylandSeat(
    QWaylandXdgToplevel *self,
    QWaylandSeat *seat) {
  self->startMove(seat);
}

//  void QWaylandXdgToplevel::startResize(QWaylandSeat *seat, Qt::Edges
//      edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel11startResizeEP12QWaylandSeat6QFlagsIN2Qt4EdgeEE(
    QWaylandXdgToplevel *self,
    QWaylandSeat *seat,
    int edges) {
  self->startResize(seat, QFlags<Qt::Edge>::fromInt(edges));
}

//  void QWaylandXdgToplevel::statesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel13statesChangedEv(
    QWaylandXdgToplevel *self) {
  self->statesChanged();
}

//  void QWaylandXdgToplevel::maximizedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel16maximizedChangedEv(
    QWaylandXdgToplevel *self) {
  self->maximizedChanged();
}

//  void QWaylandXdgToplevel::fullscreenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel17fullscreenChangedEv(
    QWaylandXdgToplevel *self) {
  self->fullscreenChanged();
}

//  void QWaylandXdgToplevel::resizingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel15resizingChangedEv(
    QWaylandXdgToplevel *self) {
  self->resizingChanged();
}

//  void QWaylandXdgToplevel::activatedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel16activatedChangedEv(
    QWaylandXdgToplevel *self) {
  self->activatedChanged();
}

//  void QWaylandXdgToplevel::showWindowMenu(QWaylandSeat *seat, const QPoint
//      &localSurfacePosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel14showWindowMenuEP12QWaylandSeatRK6QPoint(
    QWaylandXdgToplevel *self,
    QWaylandSeat *seat,
    const QPoint *localSurfacePosition) {
  self->showWindowMenu(seat, *localSurfacePosition);
}

//  void QWaylandXdgToplevel::setMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel12setMaximizedEv(
    QWaylandXdgToplevel *self) {
  self->setMaximized();
}

//  void QWaylandXdgToplevel::unsetMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel14unsetMaximizedEv(
    QWaylandXdgToplevel *self) {
  self->unsetMaximized();
}

//  void QWaylandXdgToplevel::setFullscreen(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel13setFullscreenEP14QWaylandOutput(
    QWaylandXdgToplevel *self,
    QWaylandOutput *output) {
  self->setFullscreen(output);
}

//  void QWaylandXdgToplevel::unsetFullscreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel15unsetFullscreenEv(
    QWaylandXdgToplevel *self) {
  self->unsetFullscreen();
}

//  void QWaylandXdgToplevel::setMinimized()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel12setMinimizedEv(
    QWaylandXdgToplevel *self) {
  self->setMinimized();
}

//  void QWaylandXdgToplevel::decorationModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel21decorationModeChangedEv(
    QWaylandXdgToplevel *self) {
  self->decorationModeChanged();
}

//  void QWaylandXdgToplevel::modalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgToplevel12modalChangedEv(
    QWaylandXdgToplevel *self) {
  self->modalChanged();
}

//  QList<int> QWaylandXdgToplevel::statesAsInts() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK19QWaylandXdgToplevel12statesAsIntsEv(
    const QWaylandXdgToplevel *self) {
  return new QList<int>(self->statesAsInts());
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

//  a QList<QWaylandXdgToplevel::State> a ritual of QWaylandXdgToplevel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandXdgToplevel__QList_QWaylandXdgToplevel_State(
    QList<QWaylandXdgToplevel::State> *self) {
  delete self;
}

//  a QList<int> a ritual of QWaylandXdgToplevel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandXdgToplevel__QList_int(QList<int> *self) {
  delete self;
}
