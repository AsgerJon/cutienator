//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QVideoWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVideoWindow : QVideoWindow {
  using QVideoWindow::event;
  using QVideoWindow::resizeEvent;
};

//  A QVideoWindow that Python can take functions over in. Every QVideoWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoWindowCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall1)(const void *, QResizeEvent *, int *);
typedef int (*CuteQVideoWindowCall2)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQVideoWindowCall3)(const void *, int *);
typedef const QSize * (*CuteQVideoWindowCall4)(const void *, int *);
typedef void * (*CuteQVideoWindowCall5)(const void *, int *);
typedef void * (*CuteQVideoWindowCall6)(const void *, int *);
typedef void (*CuteQVideoWindowCall7)(const void *, QExposeEvent *, int *);
typedef void (*CuteQVideoWindowCall8)(const void *, QPaintEvent *, int *);
typedef void (*CuteQVideoWindowCall9)(const void *, QMoveEvent *, int *);
typedef void (*CuteQVideoWindowCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVideoWindowCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVideoWindowCall12)(const void *, QShowEvent *, int *);
typedef void (*CuteQVideoWindowCall13)(const void *, QHideEvent *, int *);
typedef void (*CuteQVideoWindowCall14)(const void *, QCloseEvent *, int *);
typedef void (*CuteQVideoWindowCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVideoWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVideoWindowCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWindowCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWindowCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWindowCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQVideoWindowCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQVideoWindowCall22)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQVideoWindowCall23)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQVideoWindowCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoWindowCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWindowCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVideoWindow : public QVideoWindow {
public:
  using QVideoWindow::QVideoWindow;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QVideoWindow::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQVideoWindowCall0 call = reinterpret_cast<CuteQVideoWindowCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QVideoWindow::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QVideoWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoWindowCall1 call = reinterpret_cast<CuteQVideoWindowCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVideoWindow::resizeEvent(a0);
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVideoWindowCall2 call = reinterpret_cast<CuteQVideoWindowCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVideoWindowCall3 call = reinterpret_cast<CuteQVideoWindowCall3>(taken[3]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVideoWindowCall4 call = reinterpret_cast<CuteQVideoWindowCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVideoWindowCall5 call = reinterpret_cast<CuteQVideoWindowCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVideoWindowCall6 call = reinterpret_cast<CuteQVideoWindowCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQVideoWindowCall7 call = reinterpret_cast<CuteQVideoWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::exposeEvent(a0);
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQVideoWindowCall8 call = reinterpret_cast<CuteQVideoWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQVideoWindowCall9 call = reinterpret_cast<CuteQVideoWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQVideoWindowCall10 call = reinterpret_cast<CuteQVideoWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQVideoWindowCall11 call = reinterpret_cast<CuteQVideoWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQVideoWindowCall12 call = reinterpret_cast<CuteQVideoWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQVideoWindowCall13 call = reinterpret_cast<CuteQVideoWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQVideoWindowCall14 call = reinterpret_cast<CuteQVideoWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQVideoWindowCall15 call = reinterpret_cast<CuteQVideoWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQVideoWindowCall16 call = reinterpret_cast<CuteQVideoWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQVideoWindowCall17 call = reinterpret_cast<CuteQVideoWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQVideoWindowCall18 call = reinterpret_cast<CuteQVideoWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQVideoWindowCall19 call = reinterpret_cast<CuteQVideoWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQVideoWindowCall20 call = reinterpret_cast<CuteQVideoWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQVideoWindowCall21 call = reinterpret_cast<CuteQVideoWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQVideoWindowCall22 call = reinterpret_cast<CuteQVideoWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQVideoWindowCall23 call = reinterpret_cast<CuteQVideoWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQVideoWindowCall24 call = reinterpret_cast<CuteQVideoWindowCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQVideoWindowCall25 call = reinterpret_cast<CuteQVideoWindowCall25>(taken[25]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQVideoWindowCall26 call = reinterpret_cast<CuteQVideoWindowCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQVideoWindowCall27 call = reinterpret_cast<CuteQVideoWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQVideoWindowCall28 call = reinterpret_cast<CuteQVideoWindowCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQVideoWindowCall29 call = reinterpret_cast<CuteQVideoWindowCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQVideoWindowCall30 call = reinterpret_cast<CuteQVideoWindowCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVideoWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QVideoWindow10metaObjectEv(
    const QVideoWindow *self) {
  return self->metaObject();
}

//  void *QVideoWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QVideoWindow11qt_metacastEPKc(
    QVideoWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVideoWindow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QVideoWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QVideoWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVideoWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QVideoWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVideoWindow::tr(s, c, n));
}

//  QVideoWindow::QVideoWindow(QScreen *screen)
extern "C" Q_DECL_EXPORT
QVideoWindow *ritual_ZN12QVideoWindowC1EP7QScreen(QScreen *screen) {
  return new CuteQVideoWindow(screen);
}

//  QVideoWindow::QVideoWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QVideoWindow *ritual_ZN12QVideoWindowC1EP7QWindow(QWindow *parent) {
  return new CuteQVideoWindow(parent);
}

//  QVideoWindow::~QVideoWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWindowD1Ev(QVideoWindow *self) {
  delete self;
}

//  QVideoSink *QVideoWindow::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK12QVideoWindow9videoSinkEv(const QVideoWindow *self) {
  return self->videoSink();
}

//  Qt::AspectRatioMode QVideoWindow::aspectRatioMode() const
extern "C" Q_DECL_EXPORT
Qt::AspectRatioMode ritual_ZNK12QVideoWindow15aspectRatioModeEv(
    const QVideoWindow *self) {
  return self->aspectRatioMode();
}

//  void QVideoWindow::setAspectRatioMode(Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWindow18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QVideoWindow *self,
    Qt::AspectRatioMode mode) {
  self->setAspectRatioMode(mode);
}

//  void QVideoWindow::aspectRatioModeChanged(Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWindow22aspectRatioModeChangedEN2Qt15AspectRatioModeE(
    QVideoWindow *self,
    Qt::AspectRatioMode mode) {
  self->aspectRatioModeChanged(mode);
}

//  bool QVideoWindow::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QVideoWindow5eventEP6QEvent(QVideoWindow *self, QEvent *e) {
  return self->event(e);
}

//  void QVideoWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWindow11resizeEventEP12QResizeEvent(
    QVideoWindow *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QVideoWindow::setVideoFrame(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWindow13setVideoFrameERK11QVideoFrame(
    QVideoWindow *self,
    const QVideoFrame *frame) {
  self->setVideoFrame(*frame);
}

//  a Python function taken by a CuteQVideoWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoWindow(
    QVideoWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoWindow *>(self)->take(key, call);
}

//  bool QVideoWindow::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QVideoWindow5eventEP6QEvent(
    QVideoWindow *self,
    QEvent *e) {
  return static_cast<OwnQVideoWindow *>(self)->OwnQVideoWindow::event(e);
}

//  void QVideoWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QVideoWindow11resizeEventEP12QResizeEvent(
    QVideoWindow *self,
    QResizeEvent *a0) {
  static_cast<OwnQVideoWindow *>(self)->OwnQVideoWindow::resizeEvent(a0);
}
