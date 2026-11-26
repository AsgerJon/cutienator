//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtQuick/qquickrendertarget.h>
#include <QtGui/qcolor.h>
#include <QtQuick/qquickgraphicsdevice.h>
#include <QtQuick/qquickgraphicsconfiguration.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWindow : QQuickWindow {
  using QQuickWindow::exposeEvent;
  using QQuickWindow::resizeEvent;
  using QQuickWindow::showEvent;
  using QQuickWindow::hideEvent;
  using QQuickWindow::closeEvent;
  using QQuickWindow::focusInEvent;
  using QQuickWindow::focusOutEvent;
  using QQuickWindow::event;
  using QQuickWindow::keyPressEvent;
  using QQuickWindow::keyReleaseEvent;
  using QQuickWindow::mousePressEvent;
  using QQuickWindow::mouseReleaseEvent;
  using QQuickWindow::mouseDoubleClickEvent;
  using QQuickWindow::mouseMoveEvent;
  using QQuickWindow::wheelEvent;
  using QQuickWindow::tabletEvent;
};

//  A QQuickWindow that Python can take functions over in. Every QQuickWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickWindowCall0)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQQuickWindowCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickWindowCall2)(const void *, QExposeEvent *, int *);
typedef void (*CuteQQuickWindowCall3)(const void *, QResizeEvent *, int *);
typedef void (*CuteQQuickWindowCall4)(const void *, QShowEvent *, int *);
typedef void (*CuteQQuickWindowCall5)(const void *, QHideEvent *, int *);
typedef void (*CuteQQuickWindowCall6)(const void *, QCloseEvent *, int *);
typedef void (*CuteQQuickWindowCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWindowCall8)(const void *, QFocusEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall10)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWindowCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWindowCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWindowCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQQuickWindowCall17)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQQuickWindowCall18)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQQuickWindowCall19)(const void *, int *);
typedef const QSize * (*CuteQQuickWindowCall20)(const void *, int *);
typedef void (*CuteQQuickWindowCall21)(const void *, QPaintEvent *, int *);
typedef void (*CuteQQuickWindowCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQQuickWindowCall23)(const void *, QTouchEvent *, int *);
typedef void * (*CuteQQuickWindowCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWindow : public QQuickWindow {
public:
  using QQuickWindow::QQuickWindow;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
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

  //  QObject *QQuickWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowCall0 call = reinterpret_cast<CuteQQuickWindowCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQuickWindow::focusObject();
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QQuickWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWindowCall1 call = reinterpret_cast<CuteQQuickWindowCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QQuickWindow::accessibleRoot();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWindowCall2 call = reinterpret_cast<CuteQQuickWindowCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::exposeEvent(a0);
  }

  //  void QQuickWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWindowCall3 call = reinterpret_cast<CuteQQuickWindowCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::resizeEvent(a0);
  }

  //  void QQuickWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWindowCall4 call = reinterpret_cast<CuteQQuickWindowCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::showEvent(a0);
  }

  //  void QQuickWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWindowCall5 call = reinterpret_cast<CuteQQuickWindowCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::hideEvent(a0);
  }

  //  void QQuickWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWindowCall6 call = reinterpret_cast<CuteQQuickWindowCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::closeEvent(a0);
  }

  //  void QQuickWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWindowCall7 call = reinterpret_cast<CuteQQuickWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusInEvent(a0);
  }

  //  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWindowCall8 call = reinterpret_cast<CuteQQuickWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusOutEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWindowCall9 call = reinterpret_cast<CuteQQuickWindowCall9>(taken[9]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWindow::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWindowCall10 call = reinterpret_cast<CuteQQuickWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyPressEvent(a0);
  }

  //  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWindowCall11 call = reinterpret_cast<CuteQQuickWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyReleaseEvent(a0);
  }

  //  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWindowCall12 call = reinterpret_cast<CuteQQuickWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mousePressEvent(a0);
  }

  //  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWindowCall13 call = reinterpret_cast<CuteQQuickWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseReleaseEvent(a0);
  }

  //  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWindowCall14 call = reinterpret_cast<CuteQQuickWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseDoubleClickEvent(a0);
  }

  //  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWindowCall15 call = reinterpret_cast<CuteQQuickWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWindowCall16 call = reinterpret_cast<CuteQQuickWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabletevent)
  //  void QQuickWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickWindowCall17 call = reinterpret_cast<CuteQQuickWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWindowCall18 call = reinterpret_cast<CuteQQuickWindowCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWindowCall19 call = reinterpret_cast<CuteQQuickWindowCall19>(taken[19]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWindowCall20 call = reinterpret_cast<CuteQQuickWindowCall20>(taken[20]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWindowCall21 call = reinterpret_cast<CuteQQuickWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWindowCall22 call = reinterpret_cast<CuteQQuickWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWindowCall23 call = reinterpret_cast<CuteQQuickWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWindowCall24 call = reinterpret_cast<CuteQQuickWindowCall24>(taken[24]);
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
      CuteQQuickWindowCall25 call = reinterpret_cast<CuteQQuickWindowCall25>(taken[25]);
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
      CuteQQuickWindowCall26 call = reinterpret_cast<CuteQQuickWindowCall26>(taken[26]);
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
      CuteQQuickWindowCall27 call = reinterpret_cast<CuteQQuickWindowCall27>(taken[27]);
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
      CuteQQuickWindowCall28 call = reinterpret_cast<CuteQQuickWindowCall28>(taken[28]);
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
      CuteQQuickWindowCall29 call = reinterpret_cast<CuteQQuickWindowCall29>(taken[29]);
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
      CuteQQuickWindowCall30 call = reinterpret_cast<CuteQQuickWindowCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickWindow10metaObjectEv(
    const QQuickWindow *self) {
  return self->metaObject();
}

//  void *QQuickWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickWindow11qt_metacastEPKc(
    QQuickWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWindow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWindow::tr(s, c, n));
}

//  QQuickWindowPrivate *QQuickWindow::d_func()
extern "C" Q_DECL_EXPORT
QQuickWindowPrivate *ritual_ZN12QQuickWindow6d_funcEv(QQuickWindow *self) {
  return self->d_func();
}

//  const QQuickWindowPrivate *QQuickWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWindowPrivate *ritual_ZNK12QQuickWindow6d_funcEv(
    const QQuickWindow *self) {
  return self->d_func();
}

//  QQuickWindow::QQuickWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN12QQuickWindowC1EP7QWindow(QWindow *parent) {
  return new CuteQQuickWindow(parent);
}

//  QQuickWindow::QQuickWindow(QQuickRenderControl *renderControl)
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN12QQuickWindowC1EP19QQuickRenderControl(
    QQuickRenderControl *renderControl) {
  return new CuteQQuickWindow(renderControl);
}

//  QQuickWindow::~QQuickWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindowD1Ev(QQuickWindow *self) {
  delete self;
}

//  QQuickItem *QQuickWindow::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickWindow11contentItemEv(
    const QQuickWindow *self) {
  return self->contentItem();
}

//  QQuickItem *QQuickWindow::activeFocusItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickWindow15activeFocusItemEv(
    const QQuickWindow *self) {
  return self->activeFocusItem();
}

//  QObject *QQuickWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QQuickWindow11focusObjectEv(const QQuickWindow *self) {
  return self->focusObject();
}

//  QQuickItem *QQuickWindow::mouseGrabberItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickWindow16mouseGrabberItemEv(
    const QQuickWindow *self) {
  return self->mouseGrabberItem();
}

//  QImage QQuickWindow::grabWindow()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN12QQuickWindow10grabWindowEv(QQuickWindow *self) {
  return new QImage(self->grabWindow());
}

//  void QQuickWindow::setRenderTarget(const QQuickRenderTarget &target)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow15setRenderTargetERK18QQuickRenderTarget(
    QQuickWindow *self,
    const QQuickRenderTarget *target) {
  self->setRenderTarget(*target);
}

//  QQuickRenderTarget QQuickWindow::renderTarget() const
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZNK12QQuickWindow12renderTargetEv(
    const QQuickWindow *self) {
  return new QQuickRenderTarget(self->renderTarget());
}

//  const GraphicsStateInfo &QQuickWindow::graphicsStateInfo()
extern "C" Q_DECL_EXPORT
QQuickWindow::GraphicsStateInfo *ritual_ZN12QQuickWindow17graphicsStateInfoEv(
    QQuickWindow *self) {
  return new QQuickWindow::GraphicsStateInfo(self->graphicsStateInfo());
}

//  void QQuickWindow::beginExternalCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21beginExternalCommandsEv(QQuickWindow *self) {
  self->beginExternalCommands();
}

//  void QQuickWindow::endExternalCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow19endExternalCommandsEv(QQuickWindow *self) {
  self->endExternalCommands();
}

//  QQmlIncubationController *QQuickWindow::incubationController() const
extern "C" Q_DECL_EXPORT
QQmlIncubationController *ritual_ZNK12QQuickWindow20incubationControllerEv(
    const QQuickWindow *self) {
  return self->incubationController();
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QQuickWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK12QQuickWindow14accessibleRootEv(
    const QQuickWindow *self) {
  return self->accessibleRoot();
}
#endif  // QT_CONFIG(accessibility)

//  QSGTexture *QQuickWindow::createTextureFromImage(const QImage &image)
//      const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK12QQuickWindow22createTextureFromImageERK6QImage(
    const QQuickWindow *self,
    const QImage *image) {
  return self->createTextureFromImage(*image);
}

//  QSGTexture *QQuickWindow::createTextureFromImage(const QImage &image,
//      CreateTextureOptions options) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK12QQuickWindow22createTextureFromImageERK6QImage6QFlagsINS_19CreateTextureOptionEE(
    const QQuickWindow *self,
    const QImage *image,
    int options) {
  return self->createTextureFromImage(
      *image,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  QSGTexture *QQuickWindow::createTextureFromRhiTexture(QRhiTexture
//      *texture, CreateTextureOptions options) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK12QQuickWindow27createTextureFromRhiTextureEP11QRhiTexture6QFlagsINS_19CreateTextureOptionEE(
    const QQuickWindow *self,
    QRhiTexture *texture,
    int options) {
  return self->createTextureFromRhiTexture(
      texture,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  void QQuickWindow::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow8setColorERK6QColor(
    QQuickWindow *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QQuickWindow::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QQuickWindow5colorEv(const QQuickWindow *self) {
  return new QColor(self->color());
}

//  bool QQuickWindow::hasDefaultAlphaBuffer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickWindow21hasDefaultAlphaBufferEv() {
  return QQuickWindow::hasDefaultAlphaBuffer();
}

//  void QQuickWindow::setDefaultAlphaBuffer(bool useAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21setDefaultAlphaBufferEb(bool useAlpha) {
  QQuickWindow::setDefaultAlphaBuffer(useAlpha);
}

//  void QQuickWindow::setPersistentGraphics(bool persistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21setPersistentGraphicsEb(
    QQuickWindow *self,
    bool persistent) {
  self->setPersistentGraphics(persistent);
}

//  bool QQuickWindow::isPersistentGraphics() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickWindow20isPersistentGraphicsEv(
    const QQuickWindow *self) {
  return self->isPersistentGraphics();
}

//  void QQuickWindow::setPersistentSceneGraph(bool persistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow23setPersistentSceneGraphEb(
    QQuickWindow *self,
    bool persistent) {
  self->setPersistentSceneGraph(persistent);
}

//  bool QQuickWindow::isPersistentSceneGraph() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickWindow22isPersistentSceneGraphEv(
    const QQuickWindow *self) {
  return self->isPersistentSceneGraph();
}

//  bool QQuickWindow::isSceneGraphInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickWindow23isSceneGraphInitializedEv(
    const QQuickWindow *self) {
  return self->isSceneGraphInitialized();
}

//  void QQuickWindow::scheduleRenderJob(QRunnable *job, RenderStage
//      schedule)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17scheduleRenderJobEP9QRunnableNS_11RenderStageE(
    QQuickWindow *self,
    QRunnable *job,
    QQuickWindow::RenderStage schedule) {
  self->scheduleRenderJob(job, schedule);
}

//  qreal QQuickWindow::effectiveDevicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickWindow25effectiveDevicePixelRatioEv(
    const QQuickWindow *self) {
  return self->effectiveDevicePixelRatio();
}

//  QSGRendererInterface *QQuickWindow::rendererInterface() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_ZNK12QQuickWindow17rendererInterfaceEv(
    const QQuickWindow *self) {
  return self->rendererInterface();
}

//  void QQuickWindow::setGraphicsApi(QSGRendererInterface::GraphicsApi api)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14setGraphicsApiEN20QSGRendererInterface11GraphicsApiE(
    QSGRendererInterface::GraphicsApi api) {
  QQuickWindow::setGraphicsApi(api);
}

//  QSGRendererInterface::GraphicsApi QQuickWindow::graphicsApi()
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_ZN12QQuickWindow11graphicsApiEv() {
  return QQuickWindow::graphicsApi();
}

//  void QQuickWindow::setSceneGraphBackend(const QString &backend)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow20setSceneGraphBackendERK7QString(
    const QString *backend) {
  QQuickWindow::setSceneGraphBackend(*backend);
}

//  QString QQuickWindow::sceneGraphBackend()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickWindow17sceneGraphBackendEv() {
  return new QString(QQuickWindow::sceneGraphBackend());
}

//  void QQuickWindow::setGraphicsDevice(const QQuickGraphicsDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17setGraphicsDeviceERK20QQuickGraphicsDevice(
    QQuickWindow *self,
    const QQuickGraphicsDevice *device) {
  self->setGraphicsDevice(*device);
}

//  QQuickGraphicsDevice QQuickWindow::graphicsDevice() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZNK12QQuickWindow14graphicsDeviceEv(
    const QQuickWindow *self) {
  return new QQuickGraphicsDevice(self->graphicsDevice());
}

//  void QQuickWindow::setGraphicsConfiguration(const
//      QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow24setGraphicsConfigurationERK27QQuickGraphicsConfiguration(
    QQuickWindow *self,
    const QQuickGraphicsConfiguration *config) {
  self->setGraphicsConfiguration(*config);
}

//  QQuickGraphicsConfiguration QQuickWindow::graphicsConfiguration() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfiguration *ritual_ZNK12QQuickWindow21graphicsConfigurationEv(
    const QQuickWindow *self) {
  return new QQuickGraphicsConfiguration(self->graphicsConfiguration());
}

//  QSGRectangleNode *QQuickWindow::createRectangleNode() const
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_ZNK12QQuickWindow19createRectangleNodeEv(
    const QQuickWindow *self) {
  return self->createRectangleNode();
}

//  QSGImageNode *QQuickWindow::createImageNode() const
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_ZNK12QQuickWindow15createImageNodeEv(
    const QQuickWindow *self) {
  return self->createImageNode();
}

//  QSGNinePatchNode *QQuickWindow::createNinePatchNode() const
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_ZNK12QQuickWindow19createNinePatchNodeEv(
    const QQuickWindow *self) {
  return self->createNinePatchNode();
}

//  QSGTextNode *QQuickWindow::createTextNode() const
extern "C" Q_DECL_EXPORT
QSGTextNode *ritual_ZNK12QQuickWindow14createTextNodeEv(
    const QQuickWindow *self) {
  return self->createTextNode();
}

//  TextRenderType QQuickWindow::textRenderType()
extern "C" Q_DECL_EXPORT
QQuickWindow::TextRenderType ritual_ZN12QQuickWindow14textRenderTypeEv() {
  return QQuickWindow::textRenderType();
}

//  void QQuickWindow::setTextRenderType(TextRenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17setTextRenderTypeENS_14TextRenderTypeE(
    QQuickWindow::TextRenderType renderType) {
  QQuickWindow::setTextRenderType(renderType);
}

//  QRhi *QQuickWindow::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK12QQuickWindow3rhiEv(const QQuickWindow *self) {
  return self->rhi();
}

//  QRhiSwapChain *QQuickWindow::swapChain() const
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZNK12QQuickWindow9swapChainEv(
    const QQuickWindow *self) {
  return self->swapChain();
}

//  void QQuickWindow::frameSwapped()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow12frameSwappedEv(QQuickWindow *self) {
  self->frameSwapped();
}

//  void QQuickWindow::sceneGraphInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21sceneGraphInitializedEv(QQuickWindow *self) {
  self->sceneGraphInitialized();
}

//  void QQuickWindow::sceneGraphInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21sceneGraphInvalidatedEv(QQuickWindow *self) {
  self->sceneGraphInvalidated();
}

//  void QQuickWindow::beforeSynchronizing()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow19beforeSynchronizingEv(QQuickWindow *self) {
  self->beforeSynchronizing();
}

//  void QQuickWindow::afterSynchronizing()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow18afterSynchronizingEv(QQuickWindow *self) {
  self->afterSynchronizing();
}

//  void QQuickWindow::beforeRendering()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow15beforeRenderingEv(QQuickWindow *self) {
  self->beforeRendering();
}

//  void QQuickWindow::afterRendering()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14afterRenderingEv(QQuickWindow *self) {
  self->afterRendering();
}

//  void QQuickWindow::afterAnimating()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14afterAnimatingEv(QQuickWindow *self) {
  self->afterAnimating();
}

//  void QQuickWindow::sceneGraphAboutToStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21sceneGraphAboutToStopEv(QQuickWindow *self) {
  self->sceneGraphAboutToStop();
}

//  void QQuickWindow::closing(QQuickCloseEvent *close)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow7closingEP16QQuickCloseEvent(
    QQuickWindow *self,
    QQuickCloseEvent *close) {
  self->closing(close);
}

//  void QQuickWindow::colorChanged(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow12colorChangedERK6QColor(
    QQuickWindow *self,
    const QColor *a0) {
  self->colorChanged(*a0);
}

//  void QQuickWindow::activeFocusItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow22activeFocusItemChangedEv(QQuickWindow *self) {
  self->activeFocusItemChanged();
}

//  void QQuickWindow::sceneGraphError(QQuickWindow::SceneGraphError error,
//      const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow15sceneGraphErrorENS_15SceneGraphErrorERK7QString(
    QQuickWindow *self,
    QQuickWindow::SceneGraphError error,
    const QString *message) {
  self->sceneGraphError(error, *message);
}

//  void QQuickWindow::beforeRenderPassRecording()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow25beforeRenderPassRecordingEv(
    QQuickWindow *self) {
  self->beforeRenderPassRecording();
}

//  void QQuickWindow::afterRenderPassRecording()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow24afterRenderPassRecordingEv(
    QQuickWindow *self) {
  self->afterRenderPassRecording();
}

//  void QQuickWindow::paletteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14paletteChangedEv(QQuickWindow *self) {
  self->paletteChanged();
}

//  void QQuickWindow::paletteCreated()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14paletteCreatedEv(QQuickWindow *self) {
  self->paletteCreated();
}

//  void QQuickWindow::beforeFrameBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow16beforeFrameBeginEv(QQuickWindow *self) {
  self->beforeFrameBegin();
}

//  void QQuickWindow::afterFrameEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow13afterFrameEndEv(QQuickWindow *self) {
  self->afterFrameEnd();
}

//  void QQuickWindow::devicePixelRatioChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow23devicePixelRatioChangedEv(QQuickWindow *self) {
  self->devicePixelRatioChanged();
}

//  void QQuickWindow::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow6updateEv(QQuickWindow *self) {
  self->update();
}

//  void QQuickWindow::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow16releaseResourcesEv(QQuickWindow *self) {
  self->releaseResources();
}

//  QQuickWindow::QQuickWindow(QQuickWindowPrivate &dd, QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN12QQuickWindowC1ER19QQuickWindowPrivateP7QWindow(
    QQuickWindowPrivate *dd,
    QWindow *parent) {
  return new CuteQQuickWindow(*dd, parent);
}

//  QQuickWindow::QQuickWindow(QQuickWindowPrivate &dd, QQuickRenderControl
//      *control)
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN12QQuickWindowC1ER19QQuickWindowPrivateP19QQuickRenderControl(
    QQuickWindowPrivate *dd,
    QQuickRenderControl *control) {
  return new CuteQQuickWindow(*dd, control);
}

//  void QQuickWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow11exposeEventEP12QExposeEvent(
    QQuickWindow *self,
    QExposeEvent *a0) {
  self->exposeEvent(a0);
}

//  void QQuickWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow11resizeEventEP12QResizeEvent(
    QQuickWindow *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QQuickWindow::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow9showEventEP10QShowEvent(
    QQuickWindow *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QQuickWindow::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow9hideEventEP10QHideEvent(
    QQuickWindow *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QQuickWindow::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow10closeEventEP11QCloseEvent(
    QQuickWindow *self,
    QCloseEvent *a0) {
  self->closeEvent(a0);
}

//  void QQuickWindow::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow12focusInEventEP11QFocusEvent(
    QQuickWindow *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow13focusOutEventEP11QFocusEvent(
    QQuickWindow *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  bool QQuickWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickWindow5eventEP6QEvent(QQuickWindow *self, QEvent *a0) {
  return self->event(a0);
}

//  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow13keyPressEventEP9QKeyEvent(
    QQuickWindow *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow15keyReleaseEventEP9QKeyEvent(
    QQuickWindow *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow15mousePressEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17mouseReleaseEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow21mouseDoubleClickEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

//  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow14mouseMoveEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

#if QT_CONFIG(wheelevent)
//  void QQuickWindow::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow10wheelEventEP11QWheelEvent(
    QQuickWindow *self,
    QWheelEvent *a0) {
  self->wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabletevent)
//  void QQuickWindow::tabletEvent(QTabletEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow11tabletEventEP12QTabletEvent(
    QQuickWindow *self,
    QTabletEvent *a0) {
  self->tabletEvent(a0);
}
#endif  // QT_CONFIG(tabletevent)

//  void QQuickWindow::maybeUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow11maybeUpdateEv(QQuickWindow *self) {
  self->maybeUpdate();
}

//  void QQuickWindow::cleanupSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17cleanupSceneGraphEv(QQuickWindow *self) {
  self->cleanupSceneGraph();
}

//  void QQuickWindow::physicalDpiChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow18physicalDpiChangedEv(QQuickWindow *self) {
  self->physicalDpiChanged();
}

//  void QQuickWindow::handleScreenChanged(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow19handleScreenChangedEP7QScreen(
    QQuickWindow *self,
    QScreen *screen) {
  self->handleScreenChanged(screen);
}

//  void QQuickWindow::runJobsAfterSwap()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow16runJobsAfterSwapEv(QQuickWindow *self) {
  self->runJobsAfterSwap();
}

//  void QQuickWindow::handleApplicationStateChanged(Qt::ApplicationState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow29handleApplicationStateChangedEN2Qt16ApplicationStateE(
    QQuickWindow *self,
    Qt::ApplicationState state) {
  self->handleApplicationStateChanged(state);
}

//  void QQuickWindow::handleFontDatabaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow25handleFontDatabaseChangedEv(
    QQuickWindow *self) {
  self->handleFontDatabaseChanged();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QQmlInfo operator<<(QQmlInfo info, const QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_Zls8QQmlInfoPK12QQuickWindow(
    const QQmlInfo *info,
    const QQuickWindow *window) {
  return new QQmlInfo(operator<<(*info, window));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a Python function taken by a CuteQQuickWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindow(
    QQuickWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindow *>(self)->take(key, call);
}

//  QObject *QQuickWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK12QQuickWindow11focusObjectEv(
    const QQuickWindow *self) {
  return self->QQuickWindow::focusObject();
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QQuickWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK12QQuickWindow14accessibleRootEv(
    const QQuickWindow *self) {
  return self->QQuickWindow::accessibleRoot();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow11exposeEventEP12QExposeEvent(
    QQuickWindow *self,
    QExposeEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::exposeEvent(a0);
}

//  void QQuickWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow11resizeEventEP12QResizeEvent(
    QQuickWindow *self,
    QResizeEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::resizeEvent(a0);
}

//  void QQuickWindow::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow9showEventEP10QShowEvent(
    QQuickWindow *self,
    QShowEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::showEvent(a0);
}

//  void QQuickWindow::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow9hideEventEP10QHideEvent(
    QQuickWindow *self,
    QHideEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::hideEvent(a0);
}

//  void QQuickWindow::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow10closeEventEP11QCloseEvent(
    QQuickWindow *self,
    QCloseEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::closeEvent(a0);
}

//  void QQuickWindow::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow12focusInEventEP11QFocusEvent(
    QQuickWindow *self,
    QFocusEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::focusInEvent(a0);
}

//  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow13focusOutEventEP11QFocusEvent(
    QQuickWindow *self,
    QFocusEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::focusOutEvent(a0);
}

//  bool QQuickWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickWindow5eventEP6QEvent(
    QQuickWindow *self,
    QEvent *a0) {
  return static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::event(a0);
}

//  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow13keyPressEventEP9QKeyEvent(
    QQuickWindow *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::keyPressEvent(a0);
}

//  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow15keyReleaseEventEP9QKeyEvent(
    QQuickWindow *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::keyReleaseEvent(a0);
}

//  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow15mousePressEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::mousePressEvent(a0);
}

//  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow17mouseReleaseEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::mouseReleaseEvent(
      a0);
}

//  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow21mouseDoubleClickEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::mouseDoubleClickEvent(
      a0);
}

//  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow14mouseMoveEventEP11QMouseEvent(
    QQuickWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::mouseMoveEvent(a0);
}

#if QT_CONFIG(wheelevent)
//  void QQuickWindow::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow10wheelEventEP11QWheelEvent(
    QQuickWindow *self,
    QWheelEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabletevent)
//  void QQuickWindow::tabletEvent(QTabletEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWindow11tabletEventEP12QTabletEvent(
    QQuickWindow *self,
    QTabletEvent *a0) {
  static_cast<OwnQQuickWindow *>(self)->OwnQQuickWindow::tabletEvent(a0);
}
#endif  // QT_CONFIG(tabletevent)
