//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandwlshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandwlshell.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A QWaylandWlShellSurface that Python can take functions over in. Every QWaylandWlShellSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQWaylandWlShellSurfaceCall0)(const void *, int *);
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandWlShellSurfaceCall1)(const void *, QWaylandQuickShellSurfaceItem *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandWlShellSurfaceCall2)(const void *, int *);
class CuteQWaylandWlShellSurface : public QWaylandWlShellSurface {
public:
  using QWaylandWlShellSurface::QWaylandWlShellSurface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QWaylandWlShellSurface10windowTypeEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN22QWaylandWlShellSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN22QWaylandWlShellSurface10initializeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Qt::WindowType QWaylandWlShellSurface::windowType() const
  Qt::WindowType windowType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandWlShellSurfaceCall0 call = reinterpret_cast<CuteQWaylandWlShellSurfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::WindowType>(given);
    }
    return QWaylandWlShellSurface::windowType();
  }

#if QT_CONFIG(wayland_compositor_quick)
  //  QWaylandQuickShellIntegration *QWaylandWlShellSurface::createIntegrat
  //      ion(QWaylandQuickShellSurfaceItem *item)
  QWaylandQuickShellIntegration *createIntegration(
      QWaylandQuickShellSurfaceItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandWlShellSurfaceCall1 call = reinterpret_cast<CuteQWaylandWlShellSurfaceCall1>(taken[1]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<QWaylandQuickShellIntegration *>(given);
    }
    return QWaylandWlShellSurface::createIntegration(item);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

  //  void QWaylandWlShellSurface::initialize()
  void initialize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandWlShellSurfaceCall2 call = reinterpret_cast<CuteQWaylandWlShellSurfaceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandWlShellSurface::initialize();
  }
};

//  const QMetaObject *QWaylandWlShellSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QWaylandWlShellSurface10metaObjectEv(
    const QWaylandWlShellSurface *self) {
  return self->metaObject();
}

//  void *QWaylandWlShellSurface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QWaylandWlShellSurface11qt_metacastEPKc(
    QWaylandWlShellSurface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandWlShellSurface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWaylandWlShellSurface11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandWlShellSurface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandWlShellSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWaylandWlShellSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandWlShellSurface::tr(s, c, n));
}

//  QWaylandWlShellSurfacePrivate *QWaylandWlShellSurface::d_func()
extern "C" Q_DECL_EXPORT
QWaylandWlShellSurfacePrivate *ritual_ZN22QWaylandWlShellSurface6d_funcEv(
    QWaylandWlShellSurface *self) {
  return self->d_func();
}

//  const QWaylandWlShellSurfacePrivate *QWaylandWlShellSurface::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWaylandWlShellSurfacePrivate *ritual_ZNK22QWaylandWlShellSurface6d_funcEv(
    const QWaylandWlShellSurface *self) {
  return self->d_func();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QQmlListProperty<QObject> QWaylandWlShellSurface::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN22QWaylandWlShellSurface4dataEv(
    QWaylandWlShellSurface *self) {
  return new QQmlListProperty<QObject>(self->data());
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandWlShellSurface::appendFunction(QQmlListProperty<QObject>
//      *list, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface14appendFunctionEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *object) {
  QWaylandWlShellSurface::appendFunction(list, object);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  qsizetype QWaylandWlShellSurface::countFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QWaylandWlShellSurface13countFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  return QWaylandWlShellSurface::countFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  QObject *QWaylandWlShellSurface::atFunction(QQmlListProperty<QObject>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QWaylandWlShellSurface10atFunctionEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *list,
    qsizetype index) {
  return QWaylandWlShellSurface::atFunction(list, index);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandWlShellSurface::clearFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface13clearFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  QWaylandWlShellSurface::clearFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  QWaylandWlShellSurface::QWaylandWlShellSurface()
extern "C" Q_DECL_EXPORT
QWaylandWlShellSurface *ritual_ZN22QWaylandWlShellSurfaceC1Ev() {
  return new CuteQWaylandWlShellSurface();
}

//  QWaylandWlShellSurface::QWaylandWlShellSurface(QWaylandWlShell *shell,
//      QWaylandSurface *surface, const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
QWaylandWlShellSurface *ritual_ZN22QWaylandWlShellSurfaceC1EP15QWaylandWlShellP15QWaylandSurfaceRK16QWaylandResource(
    QWaylandWlShell *shell,
    QWaylandSurface *surface,
    const QWaylandResource *resource) {
  return new CuteQWaylandWlShellSurface(shell, surface, *resource);
}

//  QWaylandWlShellSurface::~QWaylandWlShellSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurfaceD1Ev(QWaylandWlShellSurface *self) {
  delete self;
}

//  void QWaylandWlShellSurface::initialize(QWaylandWlShell *shell,
//      QWaylandSurface *surface, const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface10initializeEP15QWaylandWlShellP15QWaylandSurfaceRK16QWaylandResource(
    QWaylandWlShellSurface *self,
    QWaylandWlShell *shell,
    QWaylandSurface *surface,
    const QWaylandResource *resource) {
  self->initialize(shell, surface, *resource);
}

//  QString QWaylandWlShellSurface::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWaylandWlShellSurface5titleEv(
    const QWaylandWlShellSurface *self) {
  return new QString(self->title());
}

//  QString QWaylandWlShellSurface::className() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWaylandWlShellSurface9classNameEv(
    const QWaylandWlShellSurface *self) {
  return new QString(self->className());
}

//  QWaylandSurface *QWaylandWlShellSurface::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK22QWaylandWlShellSurface7surfaceEv(
    const QWaylandWlShellSurface *self) {
  return self->surface();
}

//  QWaylandWlShell *QWaylandWlShellSurface::shell() const
extern "C" Q_DECL_EXPORT
QWaylandWlShell *ritual_ZNK22QWaylandWlShellSurface5shellEv(
    const QWaylandWlShellSurface *self) {
  return self->shell();
}

//  Qt::WindowType QWaylandWlShellSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK22QWaylandWlShellSurface10windowTypeEv(
    const QWaylandWlShellSurface *self) {
  return self->windowType();
}

//  const struct wl_interface *QWaylandWlShellSurface::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN22QWaylandWlShellSurface9interfaceEv() {
  return QWaylandWlShellSurface::interface();
}

//  QByteArray QWaylandWlShellSurface::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QWaylandWlShellSurface13interfaceNameEv() {
  return new QByteArray(QWaylandWlShellSurface::interfaceName());
}

//  QWaylandSurfaceRole *QWaylandWlShellSurface::role()
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZN22QWaylandWlShellSurface4roleEv() {
  return QWaylandWlShellSurface::role();
}

//  QWaylandWlShellSurface *QWaylandWlShellSurface::fromResource(wl_resource
//      *res)
extern "C" Q_DECL_EXPORT
QWaylandWlShellSurface *ritual_ZN22QWaylandWlShellSurface12fromResourceEP11wl_resource(
    wl_resource *res) {
  return QWaylandWlShellSurface::fromResource(res);
}

//  QSize QWaylandWlShellSurface::sizeForResize(const QSizeF &size, const
//      QPointF &delta, ResizeEdge edges)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN22QWaylandWlShellSurface13sizeForResizeERK6QSizeFRK7QPointFNS_10ResizeEdgeE(
    QWaylandWlShellSurface *self,
    const QSizeF *size,
    const QPointF *delta,
    QWaylandWlShellSurface::ResizeEdge edges) {
  return new QSize(self->sizeForResize(*size, *delta, edges));
}

//  void QWaylandWlShellSurface::sendConfigure(const QSize &size, ResizeEdge
//      edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface13sendConfigureERK5QSizeNS_10ResizeEdgeE(
    QWaylandWlShellSurface *self,
    const QSize *size,
    QWaylandWlShellSurface::ResizeEdge edges) {
  self->sendConfigure(*size, edges);
}

//  void QWaylandWlShellSurface::sendPopupDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface13sendPopupDoneEv(
    QWaylandWlShellSurface *self) {
  self->sendPopupDone();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandWlShellSurface::createIntegration(QWaylandQuickShellSurfaceI
//      tem *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_ZN22QWaylandWlShellSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandWlShellSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandWlShellSurface::ping()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface4pingEv(QWaylandWlShellSurface *self) {
  self->ping();
}

//  void QWaylandWlShellSurface::surfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface14surfaceChangedEv(
    QWaylandWlShellSurface *self) {
  self->surfaceChanged();
}

//  void QWaylandWlShellSurface::shellChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface12shellChangedEv(
    QWaylandWlShellSurface *self) {
  self->shellChanged();
}

//  void QWaylandWlShellSurface::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface12titleChangedEv(
    QWaylandWlShellSurface *self) {
  self->titleChanged();
}

//  void QWaylandWlShellSurface::classNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface16classNameChangedEv(
    QWaylandWlShellSurface *self) {
  self->classNameChanged();
}

//  void QWaylandWlShellSurface::pong()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface4pongEv(QWaylandWlShellSurface *self) {
  self->pong();
}

//  void QWaylandWlShellSurface::startMove(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface9startMoveEP12QWaylandSeat(
    QWaylandWlShellSurface *self,
    QWaylandSeat *seat) {
  self->startMove(seat);
}

//  void QWaylandWlShellSurface::startResize(QWaylandSeat *seat, ResizeEdge
//      edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface11startResizeEP12QWaylandSeatNS_10ResizeEdgeE(
    QWaylandWlShellSurface *self,
    QWaylandSeat *seat,
    QWaylandWlShellSurface::ResizeEdge edges) {
  self->startResize(seat, edges);
}

//  void QWaylandWlShellSurface::setDefaultToplevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface18setDefaultToplevelEv(
    QWaylandWlShellSurface *self) {
  self->setDefaultToplevel();
}

//  void QWaylandWlShellSurface::setTransient(QWaylandSurface *parentSurface,
//      const QPoint &relativeToParent, bool inactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface12setTransientEP15QWaylandSurfaceRK6QPointb(
    QWaylandWlShellSurface *self,
    QWaylandSurface *parentSurface,
    const QPoint *relativeToParent,
    bool inactive) {
  self->setTransient(parentSurface, *relativeToParent, inactive);
}

//  void QWaylandWlShellSurface::setFullScreen(FullScreenMethod method, uint
//      framerate, QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface13setFullScreenENS_16FullScreenMethodEjP14QWaylandOutput(
    QWaylandWlShellSurface *self,
    QWaylandWlShellSurface::FullScreenMethod method,
    uint framerate,
    QWaylandOutput *output) {
  self->setFullScreen(method, framerate, output);
}

//  void QWaylandWlShellSurface::setPopup(QWaylandSeat *seat, QWaylandSurface
//      *parentSurface, const QPoint &relativeToParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface8setPopupEP12QWaylandSeatP15QWaylandSurfaceRK6QPoint(
    QWaylandWlShellSurface *self,
    QWaylandSeat *seat,
    QWaylandSurface *parentSurface,
    const QPoint *relativeToParent) {
  self->setPopup(seat, parentSurface, *relativeToParent);
}

//  void QWaylandWlShellSurface::setMaximized(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface12setMaximizedEP14QWaylandOutput(
    QWaylandWlShellSurface *self,
    QWaylandOutput *output) {
  self->setMaximized(output);
}

//  void QWaylandWlShellSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandWlShellSurface10initializeEv(
    QWaylandWlShellSurface *self) {
  self->initialize();
}

//  a Python function taken by a CuteQWaylandWlShellSurface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandWlShellSurface(
    QWaylandWlShellSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandWlShellSurface *>(self)->take(key, call);
}

//  Qt::WindowType QWaylandWlShellSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_own_ZNK22QWaylandWlShellSurface10windowTypeEv(
    const QWaylandWlShellSurface *self) {
  return self->QWaylandWlShellSurface::windowType();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandWlShellSurface::createIntegration(QWaylandQuickShellSurfaceI
//      tem *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_own_ZN22QWaylandWlShellSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandWlShellSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->QWaylandWlShellSurface::createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandWlShellSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QWaylandWlShellSurface10initializeEv(
    QWaylandWlShellSurface *self) {
  self->QWaylandWlShellSurface::initialize();
}

//  QList<QWaylandWlShellSurface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandWlShellSurface *> *ritual_list_make_QWaylandWlShellSurface_ptr() {
  return new QList<QWaylandWlShellSurface *>();
}

//  void QList<QWaylandWlShellSurface *>::append(const QWaylandWlShellSurface
//      * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandWlShellSurface_ptr(
    QList<QWaylandWlShellSurface *> *self,
    QWaylandWlShellSurface *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandWlShellSurface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandWlShellSurface_ptr(
    const QList<QWaylandWlShellSurface *> *self) {
  return self->size();
}

//  const QWaylandWlShellSurface * &QList<QWaylandWlShellSurface
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandWlShellSurface *ritual_list_at_QWaylandWlShellSurface_ptr(
    const QList<QWaylandWlShellSurface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandWlShellSurface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandWlShellSurface_ptr(
    QList<QWaylandWlShellSurface *> *self) {
  delete self;
}

//  a QQmlListProperty<QObject> a ritual of QWaylandWlShellSurface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandWlShellSurface__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
