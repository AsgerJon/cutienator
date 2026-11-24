//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindowmodule_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindowmodule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWindowQmlImpl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWindowQmlImpl : QQuickWindowQmlImpl {
  using QQuickWindowQmlImpl::classBegin;
  using QQuickWindowQmlImpl::componentComplete;
  using QQuickWindowQmlImpl::event;
};

//  A QQuickWindowQmlImpl that Python can take functions over in. Every QQuickWindowQmlImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWindowQmlImplCall0)(const void *, int *);
typedef void (*CuteQQuickWindowQmlImplCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowQmlImplCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickWindowQmlImplCall3)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQQuickWindowQmlImplCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickWindowQmlImplCall5)(const void *, QExposeEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall6)(const void *, QResizeEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall7)(const void *, QShowEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall8)(const void *, QHideEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall9)(const void *, QCloseEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall17)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWindowQmlImplCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQQuickWindowQmlImplCall19)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQQuickWindowQmlImplCall20)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQQuickWindowQmlImplCall21)(const void *, int *);
typedef const QSize * (*CuteQQuickWindowQmlImplCall22)(const void *, int *);
typedef void (*CuteQQuickWindowQmlImplCall23)(const void *, QPaintEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQQuickWindowQmlImplCall25)(const void *, QTouchEvent *, int *);
typedef void * (*CuteQQuickWindowQmlImplCall26)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowQmlImplCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowQmlImplCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowQmlImplCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowQmlImplCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowQmlImplCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowQmlImplCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWindowQmlImpl : public QQuickWindowQmlImpl {
public:
  using QQuickWindowQmlImpl::QQuickWindowQmlImpl;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickWindowQmlImpl::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall0 call = reinterpret_cast<CuteQQuickWindowQmlImplCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowQmlImpl::classBegin();
  }

  //  void QQuickWindowQmlImpl::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall1 call = reinterpret_cast<CuteQQuickWindowQmlImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowQmlImpl::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWindowQmlImpl::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall2 call = reinterpret_cast<CuteQQuickWindowQmlImplCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWindowQmlImpl::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QObject *QQuickWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall3 call = reinterpret_cast<CuteQQuickWindowQmlImplCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQuickWindow::focusObject();
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QQuickWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall4 call = reinterpret_cast<CuteQQuickWindowQmlImplCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QQuickWindow::accessibleRoot();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall5 call = reinterpret_cast<CuteQQuickWindowQmlImplCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::exposeEvent(a0);
  }

  //  void QQuickWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall6 call = reinterpret_cast<CuteQQuickWindowQmlImplCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::resizeEvent(a0);
  }

  //  void QQuickWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall7 call = reinterpret_cast<CuteQQuickWindowQmlImplCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::showEvent(a0);
  }

  //  void QQuickWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall8 call = reinterpret_cast<CuteQQuickWindowQmlImplCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::hideEvent(a0);
  }

  //  void QQuickWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall9 call = reinterpret_cast<CuteQQuickWindowQmlImplCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::closeEvent(a0);
  }

  //  void QQuickWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall10 call = reinterpret_cast<CuteQQuickWindowQmlImplCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusInEvent(a0);
  }

  //  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall11 call = reinterpret_cast<CuteQQuickWindowQmlImplCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusOutEvent(a0);
  }

  //  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall12 call = reinterpret_cast<CuteQQuickWindowQmlImplCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyPressEvent(a0);
  }

  //  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall13 call = reinterpret_cast<CuteQQuickWindowQmlImplCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyReleaseEvent(a0);
  }

  //  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall14 call = reinterpret_cast<CuteQQuickWindowQmlImplCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mousePressEvent(a0);
  }

  //  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall15 call = reinterpret_cast<CuteQQuickWindowQmlImplCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseReleaseEvent(a0);
  }

  //  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall16 call = reinterpret_cast<CuteQQuickWindowQmlImplCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseDoubleClickEvent(a0);
  }

  //  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall17 call = reinterpret_cast<CuteQQuickWindowQmlImplCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall18 call = reinterpret_cast<CuteQQuickWindowQmlImplCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabletevent)
  //  void QQuickWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall19 call = reinterpret_cast<CuteQQuickWindowQmlImplCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall20 call = reinterpret_cast<CuteQQuickWindowQmlImplCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall21 call = reinterpret_cast<CuteQQuickWindowQmlImplCall21>(taken[21]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall22 call = reinterpret_cast<CuteQQuickWindowQmlImplCall22>(taken[22]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall23 call = reinterpret_cast<CuteQQuickWindowQmlImplCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall24 call = reinterpret_cast<CuteQQuickWindowQmlImplCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall25 call = reinterpret_cast<CuteQQuickWindowQmlImplCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall26 call = reinterpret_cast<CuteQQuickWindowQmlImplCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall27 call = reinterpret_cast<CuteQQuickWindowQmlImplCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall28 call = reinterpret_cast<CuteQQuickWindowQmlImplCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall29 call = reinterpret_cast<CuteQQuickWindowQmlImplCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall30 call = reinterpret_cast<CuteQQuickWindowQmlImplCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall31 call = reinterpret_cast<CuteQQuickWindowQmlImplCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickWindowQmlImplCall32 call = reinterpret_cast<CuteQQuickWindowQmlImplCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWindowQmlImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickWindowQmlImpl10metaObjectEv(
    const QQuickWindowQmlImpl *self) {
  return self->metaObject();
}

//  QString QQuickWindowQmlImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickWindowQmlImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWindowQmlImpl::tr(s, c, n));
}

//  void QQuickWindowQmlImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl21qt_qmlMarker_attachedEv(
    QQuickWindowQmlImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickWindowQmlImpl::QQuickWindowQmlImpl(QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickWindowQmlImpl *ritual_ZN19QQuickWindowQmlImplC1EP7QWindow(
    QWindow *parent) {
  return new CuteQQuickWindowQmlImpl(parent);
}

//  QQuickWindowQmlImpl::~QQuickWindowQmlImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImplD1Ev(QQuickWindowQmlImpl *self) {
  delete self;
}

//  void QQuickWindowQmlImpl::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl10setVisibleEb(
    QQuickWindowQmlImpl *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QQuickWindowQmlImpl::setVisibility(QWindow::Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl13setVisibilityEN7QWindow10VisibilityE(
    QQuickWindowQmlImpl *self,
    QWindow::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QQuickScreenInfo *QQuickWindowQmlImpl::screen() const
extern "C" Q_DECL_EXPORT
QQuickScreenInfo *ritual_ZNK19QQuickWindowQmlImpl6screenEv(
    const QQuickWindowQmlImpl *self) {
  return self->screen();
}

//  void QQuickWindowQmlImpl::setScreen(QQuickScreenInfo *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl9setScreenEP16QQuickScreenInfo(
    QQuickWindowQmlImpl *self,
    QQuickScreenInfo *screen) {
  self->setScreen(screen);
}

//  QObject *QQuickWindowQmlImpl::visualParent() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK19QQuickWindowQmlImpl12visualParentEv(
    const QQuickWindowQmlImpl *self) {
  return self->visualParent();
}

//  void QQuickWindowQmlImpl::setVisualParent(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl15setVisualParentEP7QObject(
    QQuickWindowQmlImpl *self,
    QObject *parent) {
  self->setVisualParent(parent);
}

//  void QQuickWindowQmlImpl::visualParentChanged(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl19visualParentChangedEP7QObject(
    QQuickWindowQmlImpl *self,
    QObject *a0) {
  self->visualParentChanged(a0);
}

//  void QQuickWindowQmlImpl::setX(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl4setXEi(
    QQuickWindowQmlImpl *self,
    int arg) {
  self->setX(arg);
}

//  int QQuickWindowQmlImpl::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickWindowQmlImpl1xEv(const QQuickWindowQmlImpl *self) {
  return self->x();
}

//  void QQuickWindowQmlImpl::setY(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl4setYEi(
    QQuickWindowQmlImpl *self,
    int arg) {
  self->setY(arg);
}

//  int QQuickWindowQmlImpl::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickWindowQmlImpl1yEv(const QQuickWindowQmlImpl *self) {
  return self->y();
}

//  void QQuickWindowQmlImpl::setZ(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl4setZEd(
    QQuickWindowQmlImpl *self,
    qreal arg) {
  self->setZ(arg);
}

//  qreal QQuickWindowQmlImpl::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickWindowQmlImpl1zEv(const QQuickWindowQmlImpl *self) {
  return self->z();
}

//  void QQuickWindowQmlImpl::zChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl8zChangedEv(QQuickWindowQmlImpl *self) {
  self->zChanged();
}

//  QQuickWindowAttached *QQuickWindowQmlImpl::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickWindowAttached *ritual_ZN19QQuickWindowQmlImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickWindowQmlImpl::qmlAttachedProperties(object);
}

//  void QQuickWindowQmlImpl::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl10classBeginEv(
    QQuickWindowQmlImpl *self) {
  self->classBegin();
}

//  void QQuickWindowQmlImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl17componentCompleteEv(
    QQuickWindowQmlImpl *self) {
  self->componentComplete();
}

//  bool QQuickWindowQmlImpl::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickWindowQmlImpl5eventEP6QEvent(
    QQuickWindowQmlImpl *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuickWindowQmlImpl::applyWindowVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl21applyWindowVisibilityEv(
    QQuickWindowQmlImpl *self) {
  self->applyWindowVisibility();
}

//  void QQuickWindowQmlImpl::updateTransientParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl21updateTransientParentEv(
    QQuickWindowQmlImpl *self) {
  self->updateTransientParent();
}

//  bool QQuickWindowQmlImpl::transientParentVisible()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickWindowQmlImpl22transientParentVisibleEv(
    QQuickWindowQmlImpl *self) {
  return self->transientParentVisible();
}

//  void QQuickWindowQmlImpl::applyVisualParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowQmlImpl17applyVisualParentEv(
    QQuickWindowQmlImpl *self) {
  self->applyVisualParent();
}

//  QQuickWindowQmlImplPrivate *QQuickWindowQmlImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickWindowQmlImplPrivate *ritual_ZN19QQuickWindowQmlImpl6d_funcEv(
    QQuickWindowQmlImpl *self) {
  return self->d_func();
}

//  const QQuickWindowQmlImplPrivate *QQuickWindowQmlImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWindowQmlImplPrivate *ritual_ZNK19QQuickWindowQmlImpl6d_funcEv(
    const QQuickWindowQmlImpl *self) {
  return self->d_func();
}

//  QQuickWindowQmlImpl as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickWindowQmlImpl_QQmlParserStatus(
    QQuickWindowQmlImpl *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickWindowQmlImpl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindowQmlImpl(
    QQuickWindowQmlImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindowQmlImpl *>(self)->take(key, call);
}

//  void QQuickWindowQmlImpl::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowQmlImpl10classBeginEv(
    QQuickWindowQmlImpl *self) {
  static_cast<OwnQQuickWindowQmlImpl *>(self)->OwnQQuickWindowQmlImpl::classBegin();
}

//  void QQuickWindowQmlImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowQmlImpl17componentCompleteEv(
    QQuickWindowQmlImpl *self) {
  static_cast<OwnQQuickWindowQmlImpl *>(self)->OwnQQuickWindowQmlImpl::componentComplete();
}

//  bool QQuickWindowQmlImpl::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickWindowQmlImpl5eventEP6QEvent(
    QQuickWindowQmlImpl *self,
    QEvent *a0) {
  return static_cast<OwnQQuickWindowQmlImpl *>(self)->OwnQQuickWindowQmlImpl::event(
      a0);
}
