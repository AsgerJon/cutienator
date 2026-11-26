//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qscreen.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 4. Kept as it is when the generator
//  runs again.
#include <QtGui/qscreen.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtGui/qscreen_platform.h>

//  A QScreen that Python can take functions over in. Every QScreen
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScreenCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScreenCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScreen : public QScreen {
public:
  using QScreen::QScreen;
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
      CuteQScreenCall0 call = reinterpret_cast<CuteQScreenCall0>(taken[0]);
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
      CuteQScreenCall1 call = reinterpret_cast<CuteQScreenCall1>(taken[1]);
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
      CuteQScreenCall2 call = reinterpret_cast<CuteQScreenCall2>(taken[2]);
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
      CuteQScreenCall3 call = reinterpret_cast<CuteQScreenCall3>(taken[3]);
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
      CuteQScreenCall4 call = reinterpret_cast<CuteQScreenCall4>(taken[4]);
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
      CuteQScreenCall5 call = reinterpret_cast<CuteQScreenCall5>(taken[5]);
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
      CuteQScreenCall6 call = reinterpret_cast<CuteQScreenCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScreen::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QScreen10metaObjectEv(const QScreen *self) {
  return self->metaObject();
}

//  void *QScreen::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QScreen11qt_metacastEPKc(QScreen *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScreen::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QScreen11qt_metacallEN11QMetaObject4CallEiPPv(
    QScreen *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScreen::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QScreen2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QScreen::tr(s, c, n));
}

//  QScreenPrivate *QScreen::d_func()
extern "C" Q_DECL_EXPORT
QScreenPrivate *ritual_ZN7QScreen6d_funcEv(QScreen *self) {
  return self->d_func();
}

//  const QScreenPrivate *QScreen::d_func() const
extern "C" Q_DECL_EXPORT
const QScreenPrivate *ritual_ZNK7QScreen6d_funcEv(const QScreen *self) {
  return self->d_func();
}

//  QScreen::~QScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreenD1Ev(QScreen *self) {
  delete self;
}

//  QPlatformScreen *QScreen::handle() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZNK7QScreen6handleEv(const QScreen *self) {
  return self->handle();
}

//  QString QScreen::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QScreen4nameEv(const QScreen *self) {
  return new QString(self->name());
}

//  QString QScreen::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QScreen12manufacturerEv(const QScreen *self) {
  return new QString(self->manufacturer());
}

//  QString QScreen::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QScreen5modelEv(const QScreen *self) {
  return new QString(self->model());
}

//  QString QScreen::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QScreen12serialNumberEv(const QScreen *self) {
  return new QString(self->serialNumber());
}

//  int QScreen::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QScreen5depthEv(const QScreen *self) {
  return self->depth();
}

//  QSize QScreen::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QScreen4sizeEv(const QScreen *self) {
  return new QSize(self->size());
}

//  QRect QScreen::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QScreen8geometryEv(const QScreen *self) {
  return new QRect(self->geometry());
}

//  QSizeF QScreen::physicalSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK7QScreen12physicalSizeEv(const QScreen *self) {
  return new QSizeF(self->physicalSize());
}

//  qreal QScreen::physicalDotsPerInchX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen20physicalDotsPerInchXEv(const QScreen *self) {
  return self->physicalDotsPerInchX();
}

//  qreal QScreen::physicalDotsPerInchY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen20physicalDotsPerInchYEv(const QScreen *self) {
  return self->physicalDotsPerInchY();
}

//  qreal QScreen::physicalDotsPerInch() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen19physicalDotsPerInchEv(const QScreen *self) {
  return self->physicalDotsPerInch();
}

//  qreal QScreen::logicalDotsPerInchX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen19logicalDotsPerInchXEv(const QScreen *self) {
  return self->logicalDotsPerInchX();
}

//  qreal QScreen::logicalDotsPerInchY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen19logicalDotsPerInchYEv(const QScreen *self) {
  return self->logicalDotsPerInchY();
}

//  qreal QScreen::logicalDotsPerInch() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen18logicalDotsPerInchEv(const QScreen *self) {
  return self->logicalDotsPerInch();
}

//  qreal QScreen::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen16devicePixelRatioEv(const QScreen *self) {
  return self->devicePixelRatio();
}

//  QSize QScreen::availableSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QScreen13availableSizeEv(const QScreen *self) {
  return new QSize(self->availableSize());
}

//  QRect QScreen::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QScreen17availableGeometryEv(const QScreen *self) {
  return new QRect(self->availableGeometry());
}

//  QList<QScreen *> QScreen::virtualSiblings() const
extern "C" Q_DECL_EXPORT
QList<QScreen *> *ritual_ZNK7QScreen15virtualSiblingsEv(
    const QScreen *self) {
  return new QList<QScreen *>(self->virtualSiblings());
}

//  QScreen *QScreen::virtualSiblingAt(QPoint point)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN7QScreen16virtualSiblingAtE6QPoint(
    QScreen *self,
    const QPoint *point) {
  return self->virtualSiblingAt(*point);
}

//  QSize QScreen::virtualSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QScreen11virtualSizeEv(const QScreen *self) {
  return new QSize(self->virtualSize());
}

//  QRect QScreen::virtualGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QScreen15virtualGeometryEv(const QScreen *self) {
  return new QRect(self->virtualGeometry());
}

//  QSize QScreen::availableVirtualSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QScreen20availableVirtualSizeEv(const QScreen *self) {
  return new QSize(self->availableVirtualSize());
}

//  QRect QScreen::availableVirtualGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QScreen24availableVirtualGeometryEv(const QScreen *self) {
  return new QRect(self->availableVirtualGeometry());
}

//  Qt::ScreenOrientation QScreen::primaryOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK7QScreen18primaryOrientationEv(
    const QScreen *self) {
  return self->primaryOrientation();
}

//  Qt::ScreenOrientation QScreen::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK7QScreen11orientationEv(
    const QScreen *self) {
  return self->orientation();
}

//  Qt::ScreenOrientation QScreen::nativeOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK7QScreen17nativeOrientationEv(
    const QScreen *self) {
  return self->nativeOrientation();
}

//  int QScreen::angleBetween(Qt::ScreenOrientation a, Qt::ScreenOrientation
//      b) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QScreen12angleBetweenEN2Qt17ScreenOrientationES1_(
    const QScreen *self,
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b) {
  return self->angleBetween(a, b);
}

//  QTransform QScreen::transformBetween(Qt::ScreenOrientation a,
//      Qt::ScreenOrientation b, const QRect &target) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK7QScreen16transformBetweenEN2Qt17ScreenOrientationES1_RK5QRect(
    const QScreen *self,
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b,
    const QRect *target) {
  return new QTransform(self->transformBetween(a, b, *target));
}

//  QRect QScreen::mapBetween(Qt::ScreenOrientation a, Qt::ScreenOrientation
//      b, const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QScreen10mapBetweenEN2Qt17ScreenOrientationES1_RK5QRect(
    const QScreen *self,
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b,
    const QRect *rect) {
  return new QRect(self->mapBetween(a, b, *rect));
}

//  bool QScreen::isPortrait(Qt::ScreenOrientation orientation) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QScreen10isPortraitEN2Qt17ScreenOrientationE(
    const QScreen *self,
    Qt::ScreenOrientation orientation) {
  return self->isPortrait(orientation);
}

//  bool QScreen::isLandscape(Qt::ScreenOrientation orientation) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QScreen11isLandscapeEN2Qt17ScreenOrientationE(
    const QScreen *self,
    Qt::ScreenOrientation orientation) {
  return self->isLandscape(orientation);
}

//  QPixmap QScreen::grabWindow(WId window, int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QScreen10grabWindowEyiiii(
    QScreen *self,
    WId window,
    int x,
    int y,
    int w,
    int h) {
  return new QPixmap(self->grabWindow(window, x, y, w, h));
}

//  qreal QScreen::refreshRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QScreen11refreshRateEv(const QScreen *self) {
  return self->refreshRate();
}

//  void *QScreen::resolveInterface(const char *name, int revision) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK7QScreen16resolveInterfaceEPKci(
    const QScreen *self,
    const char *name,
    int revision) {
  return self->resolveInterface(name, revision);
}

//  void QScreen::geometryChanged(const QRect &geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen15geometryChangedERK5QRect(
    QScreen *self,
    const QRect *geometry) {
  self->geometryChanged(*geometry);
}

//  void QScreen::availableGeometryChanged(const QRect &geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen24availableGeometryChangedERK5QRect(
    QScreen *self,
    const QRect *geometry) {
  self->availableGeometryChanged(*geometry);
}

//  void QScreen::physicalSizeChanged(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen19physicalSizeChangedERK6QSizeF(
    QScreen *self,
    const QSizeF *size) {
  self->physicalSizeChanged(*size);
}

//  void QScreen::physicalDotsPerInchChanged(qreal dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen26physicalDotsPerInchChangedEd(
    QScreen *self,
    qreal dpi) {
  self->physicalDotsPerInchChanged(dpi);
}

//  void QScreen::logicalDotsPerInchChanged(qreal dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen25logicalDotsPerInchChangedEd(
    QScreen *self,
    qreal dpi) {
  self->logicalDotsPerInchChanged(dpi);
}

//  void QScreen::virtualGeometryChanged(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen22virtualGeometryChangedERK5QRect(
    QScreen *self,
    const QRect *rect) {
  self->virtualGeometryChanged(*rect);
}

//  void QScreen::primaryOrientationChanged(Qt::ScreenOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen25primaryOrientationChangedEN2Qt17ScreenOrientationE(
    QScreen *self,
    Qt::ScreenOrientation orientation) {
  self->primaryOrientationChanged(orientation);
}

//  void QScreen::orientationChanged(Qt::ScreenOrientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen18orientationChangedEN2Qt17ScreenOrientationE(
    QScreen *self,
    Qt::ScreenOrientation orientation) {
  self->orientationChanged(orientation);
}

//  void QScreen::refreshRateChanged(qreal refreshRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QScreen18refreshRateChangedEd(
    QScreen *self,
    qreal refreshRate) {
  self->refreshRateChanged(refreshRate);
}

//  QScreen::QScreen(QPlatformScreen *screen)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN7QScreenC1EP15QPlatformScreen(QPlatformScreen *screen) {
  return new CuteQScreen(screen);
}

//  a Python function taken by a CuteQScreen, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScreen(QScreen *self, const char *key, void *call) {
  return static_cast<CuteQScreen *>(self)->take(key, call);
}

//  QList<QScreen *>::QList()
extern "C" Q_DECL_EXPORT
QList<QScreen *> *ritual_list_make_QScreen_ptr() {
  return new QList<QScreen *>();
}

//  void QList<QScreen *>::append(const QScreen * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScreen_ptr(QList<QScreen *> *self, QScreen *element) {
  self->append(element);
}

//  qsizetype QList<QScreen *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScreen_ptr(const QList<QScreen *> *self) {
  return self->size();
}

//  const QScreen * &QList<QScreen *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QScreen *ritual_list_at_QScreen_ptr(
    const QList<QScreen *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QScreen *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScreen_ptr(QList<QScreen *> *self) {
  delete self;
}

#if defined(Q_OS_WIN32)
//  QNativeInterface::QWindowsScreen
//      *QScreen::nativeInterface<QNativeInterface::QWindowsScreen>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QWindowsScreen *ritual_ZNK7QScreen15nativeInterfaceIN16QNativeInterface14QWindowsScreenENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QScreen *self) {
  return self->nativeInterface<QNativeInterface::QWindowsScreen>();
}
#endif  // defined(Q_OS_WIN32)

#if QT_CONFIG(wayland)
//  QNativeInterface::QWaylandScreen
//      *QScreen::nativeInterface<QNativeInterface::QWaylandScreen>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QWaylandScreen *ritual_ZNK7QScreen15nativeInterfaceIN16QNativeInterface14QWaylandScreenENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QScreen *self) {
  return self->nativeInterface<QNativeInterface::QWaylandScreen>();
}
#endif  // QT_CONFIG(wayland)

#if defined(Q_OS_ANDROID)
//  QNativeInterface::QAndroidScreen
//      *QScreen::nativeInterface<QNativeInterface::QAndroidScreen>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QAndroidScreen *ritual_ZNK7QScreen15nativeInterfaceIN16QNativeInterface14QAndroidScreenENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QScreen *self) {
  return self->nativeInterface<QNativeInterface::QAndroidScreen>();
}
#endif  // defined(Q_OS_ANDROID)

#if defined(Q_OS_MACOS)
//  QNativeInterface::QCocoaScreen
//      *QScreen::nativeInterface<QNativeInterface::QCocoaScreen>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QCocoaScreen *ritual_ZNK7QScreen15nativeInterfaceIN16QNativeInterface12QCocoaScreenENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QScreen *self) {
  return self->nativeInterface<QNativeInterface::QCocoaScreen>();
}
#endif  // defined(Q_OS_MACOS)
