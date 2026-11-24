//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickExtras/qt3dquickwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <Qt3DQuickExtras/Qt3DQuickExtras>
#include <Qt3DQuickExtras/qt3dquickwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on Qt3DExtras::Quick::Qt3DQuickWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQt3DExtras_Quick_Qt3DQuickWindow : Qt3DExtras::Quick::Qt3DQuickWindow {
  using Qt3DExtras::Quick::Qt3DQuickWindow::showEvent;
};

//  A Qt3DExtras::Quick::Qt3DQuickWindow that Python can take functions over in. Every Qt3DExtras::Quick::Qt3DQuickWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall0)(const void *, QShowEvent *, int *);
typedef int (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall1)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall2)(const void *, int *);
typedef const QSize * (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall3)(const void *, int *);
typedef void * (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall4)(const void *, int *);
typedef void * (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall5)(const void *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall6)(const void *, QExposeEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall7)(const void *, QResizeEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall8)(const void *, QPaintEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall9)(const void *, QMoveEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall12)(const void *, QHideEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall13)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall22)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall23)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Quick_Qt3DQuickWindowCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_Quick_Qt3DQuickWindow : public Qt3DExtras::Quick::Qt3DQuickWindow {
public:
  using Qt3DExtras::Quick::Qt3DQuickWindow::Qt3DQuickWindow;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  void Qt3DExtras::Quick::Qt3DQuickWindow::showEvent(QShowEvent *e)
  void showEvent(QShowEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall0 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    Qt3DExtras::Quick::Qt3DQuickWindow::showEvent(e);
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall1 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall2 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall2>(taken[2]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall3 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall4 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall5 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall6 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::exposeEvent(a0);
  }

  //  void QWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall7 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::resizeEvent(a0);
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall8 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall9 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall10 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall11 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall12 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall13 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall14 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWindow::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall15 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall16 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall17 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall18 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall19 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall20 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall20>(taken[20]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall21 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall21>(taken[21]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall22 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall22>(taken[22]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall23 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall23>(taken[23]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall24 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall24>(taken[24]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall25 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall25>(taken[25]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall26 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall26>(taken[26]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall27 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall27>(taken[27]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall28 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall28>(taken[28]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall29 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall29>(taken[29]);
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
      CuteQt3DExtras_Quick_Qt3DQuickWindowCall30 call = reinterpret_cast<CuteQt3DExtras_Quick_Qt3DQuickWindowCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::Quick::Qt3DQuickWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras5Quick15Qt3DQuickWindow10metaObjectEv(
    const Qt3DExtras::Quick::Qt3DQuickWindow *self) {
  return self->metaObject();
}

//  QString Qt3DExtras::Quick::Qt3DQuickWindow::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::Quick::Qt3DQuickWindow::tr(s, c, n));
}

//  Qt3DQuickWindowPrivate *Qt3DExtras::Quick::Qt3DQuickWindow::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::Quick::Qt3DQuickWindowPrivate *ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow6d_funcEv(
    Qt3DExtras::Quick::Qt3DQuickWindow *self) {
  return self->d_func();
}

//  const Qt3DQuickWindowPrivate
//      *Qt3DExtras::Quick::Qt3DQuickWindow::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::Quick::Qt3DQuickWindowPrivate *ritual_ZNK10Qt3DExtras5Quick15Qt3DQuickWindow6d_funcEv(
    const Qt3DExtras::Quick::Qt3DQuickWindow *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_Quick_Qt3DQuickWindow, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_Quick_Qt3DQuickWindow(
    Qt3DExtras::Quick::Qt3DQuickWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_Quick_Qt3DQuickWindow *>(self)->take(key, call);
}

//  void Qt3DExtras::Quick::Qt3DQuickWindow::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras5Quick15Qt3DQuickWindow9showEventEP10QShowEvent(
    Qt3DExtras::Quick::Qt3DQuickWindow *self,
    QShowEvent *e) {
  static_cast<OwnQt3DExtras_Quick_Qt3DQuickWindow *>(self)->OwnQt3DExtras_Quick_Qt3DQuickWindow::showEvent(
      e);
}
