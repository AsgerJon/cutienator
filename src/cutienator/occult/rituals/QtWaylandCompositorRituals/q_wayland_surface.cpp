//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandsurface.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWaylandSurface that Python can take functions over in. Every QWaylandSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSurfaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSurfaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandSurface : public QWaylandSurface {
public:
  using QWaylandSurface::QWaylandSurface;
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
      CuteQWaylandSurfaceCall0 call = reinterpret_cast<CuteQWaylandSurfaceCall0>(taken[0]);
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
      CuteQWaylandSurfaceCall1 call = reinterpret_cast<CuteQWaylandSurfaceCall1>(taken[1]);
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
      CuteQWaylandSurfaceCall2 call = reinterpret_cast<CuteQWaylandSurfaceCall2>(taken[2]);
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
      CuteQWaylandSurfaceCall3 call = reinterpret_cast<CuteQWaylandSurfaceCall3>(taken[3]);
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
      CuteQWaylandSurfaceCall4 call = reinterpret_cast<CuteQWaylandSurfaceCall4>(taken[4]);
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
      CuteQWaylandSurfaceCall5 call = reinterpret_cast<CuteQWaylandSurfaceCall5>(taken[5]);
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
      CuteQWaylandSurfaceCall6 call = reinterpret_cast<CuteQWaylandSurfaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QWaylandSurface10metaObjectEv(
    const QWaylandSurface *self) {
  return self->metaObject();
}

//  QString QWaylandSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QWaylandSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandSurface::tr(s, c, n));
}

//  void QWaylandSurface::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface24qt_qmlMarker_uncreatableEv(
    QWaylandSurface *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandSurface::QWaylandSurface()
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZN15QWaylandSurfaceC1Ev() {
  return new CuteQWaylandSurface();
}

//  QWaylandSurface::QWaylandSurface(QWaylandCompositor *compositor,
//      QWaylandClient *client, uint id, int version)
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZN15QWaylandSurfaceC1EP18QWaylandCompositorP14QWaylandClientji(
    QWaylandCompositor *compositor,
    QWaylandClient *client,
    uint id,
    int version) {
  return new CuteQWaylandSurface(compositor, client, id, version);
}

//  QWaylandSurface::~QWaylandSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurfaceD1Ev(QWaylandSurface *self) {
  delete self;
}

//  void QWaylandSurface::initialize(QWaylandCompositor *compositor,
//      QWaylandClient *client, uint id, int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface10initializeEP18QWaylandCompositorP14QWaylandClientji(
    QWaylandSurface *self,
    QWaylandCompositor *compositor,
    QWaylandClient *client,
    uint id,
    int version) {
  self->initialize(compositor, client, id, version);
}

//  bool QWaylandSurface::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface13isInitializedEv(
    const QWaylandSurface *self) {
  return self->isInitialized();
}

//  QWaylandClient *QWaylandSurface::client() const
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_ZNK15QWaylandSurface6clientEv(
    const QWaylandSurface *self) {
  return self->client();
}

//  QWaylandSurfaceRole *QWaylandSurface::role() const
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZNK15QWaylandSurface4roleEv(
    const QWaylandSurface *self) {
  return self->role();
}

//  bool QWaylandSurface::hasContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface10hasContentEv(const QWaylandSurface *self) {
  return self->hasContent();
}

//  QRectF QWaylandSurface::sourceGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QWaylandSurface14sourceGeometryEv(
    const QWaylandSurface *self) {
  return new QRectF(self->sourceGeometry());
}

//  QSize QWaylandSurface::destinationSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QWaylandSurface15destinationSizeEv(
    const QWaylandSurface *self) {
  return new QSize(self->destinationSize());
}

//  QSize QWaylandSurface::bufferSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QWaylandSurface10bufferSizeEv(
    const QWaylandSurface *self) {
  return new QSize(self->bufferSize());
}

//  int QWaylandSurface::bufferScale() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QWaylandSurface11bufferScaleEv(const QWaylandSurface *self) {
  return self->bufferScale();
}

//  Qt::ScreenOrientation QWaylandSurface::contentOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK15QWaylandSurface18contentOrientationEv(
    const QWaylandSurface *self) {
  return self->contentOrientation();
}

//  Origin QWaylandSurface::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface::Origin ritual_ZNK15QWaylandSurface6originEv(
    const QWaylandSurface *self) {
  return self->origin();
}

//  QWaylandCompositor *QWaylandSurface::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK15QWaylandSurface10compositorEv(
    const QWaylandSurface *self) {
  return self->compositor();
}

//  bool QWaylandSurface::inputRegionContains(const QPoint &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface19inputRegionContainsERK6QPoint(
    const QWaylandSurface *self,
    const QPoint *p) {
  return self->inputRegionContains(*p);
}

//  bool QWaylandSurface::inputRegionContains(const QPointF &position) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface19inputRegionContainsERK7QPointF(
    const QWaylandSurface *self,
    const QPointF *position) {
  return self->inputRegionContains(*position);
}

//  void QWaylandSurface::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface7destroyEv(QWaylandSurface *self) {
  self->destroy();
}

//  bool QWaylandSurface::isDestroyed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface11isDestroyedEv(
    const QWaylandSurface *self) {
  return self->isDestroyed();
}

//  void QWaylandSurface::frameStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface12frameStartedEv(QWaylandSurface *self) {
  self->frameStarted();
}

//  void QWaylandSurface::sendFrameCallbacks()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface18sendFrameCallbacksEv(
    QWaylandSurface *self) {
  self->sendFrameCallbacks();
}

//  QWaylandView *QWaylandSurface::primaryView() const
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZNK15QWaylandSurface11primaryViewEv(
    const QWaylandSurface *self) {
  return self->primaryView();
}

//  void QWaylandSurface::setPrimaryView(QWaylandView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface14setPrimaryViewEP12QWaylandView(
    QWaylandSurface *self,
    QWaylandView *view) {
  self->setPrimaryView(view);
}

//  QList<QWaylandView *> QWaylandSurface::views() const
extern "C" Q_DECL_EXPORT
QList<QWaylandView *> *ritual_ZNK15QWaylandSurface5viewsEv(
    const QWaylandSurface *self) {
  return new QList<QWaylandView *>(self->views());
}

//  void QWaylandSurface::markAsCursorSurface(bool cursorSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface19markAsCursorSurfaceEb(
    QWaylandSurface *self,
    bool cursorSurface) {
  self->markAsCursorSurface(cursorSurface);
}

//  bool QWaylandSurface::isCursorSurface() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface15isCursorSurfaceEv(
    const QWaylandSurface *self) {
  return self->isCursorSurface();
}

//  bool QWaylandSurface::inhibitsIdle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface12inhibitsIdleEv(
    const QWaylandSurface *self) {
  return self->inhibitsIdle();
}

//  bool QWaylandSurface::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandSurface8isOpaqueEv(const QWaylandSurface *self) {
  return self->isOpaque();
}

#if QT_CONFIG(im)
//  QWaylandInputMethodControl *QWaylandSurface::inputMethodControl() const
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControl *ritual_ZNK15QWaylandSurface18inputMethodControlEv(
    const QWaylandSurface *self) {
  return self->inputMethodControl();
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(clipboard)
//  void QWaylandSurface::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandSurface15updateSelectionEv(QWaylandSurface *self) {
  self->updateSelection();
}
#endif  // QT_CONFIG(clipboard)

//  a Python function taken by a CuteQWaylandSurface, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandSurface(
    QWaylandSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandSurface *>(self)->take(key, call);
}

//  QList<QWaylandSurface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandSurface *> *ritual_list_make_QWaylandSurface_ptr() {
  return new QList<QWaylandSurface *>();
}

//  void QList<QWaylandSurface *>::append(const QWaylandSurface * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandSurface_ptr(
    QList<QWaylandSurface *> *self,
    QWaylandSurface *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandSurface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandSurface_ptr(
    const QList<QWaylandSurface *> *self) {
  return self->size();
}

//  const QWaylandSurface * &QList<QWaylandSurface *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_list_at_QWaylandSurface_ptr(
    const QList<QWaylandSurface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandSurface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandSurface_ptr(QList<QWaylandSurface *> *self) {
  delete self;
}
