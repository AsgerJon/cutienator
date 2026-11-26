//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtVirtualKeyboard/qvirtualkeyboard_global.h>
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#if QT_CONFIG(vkb_desktop)
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtVirtualKeyboard::InputView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtVirtualKeyboard_InputView : QtVirtualKeyboard::InputView {
  using QtVirtualKeyboard::InputView::resizeEvent;
};

//  A QtVirtualKeyboard::InputView that Python can take functions over in. Every QtVirtualKeyboard::InputView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtVirtualKeyboard_InputViewCall0)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall1)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall2)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall3)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall6)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQtVirtualKeyboard_InputViewCall7)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQtVirtualKeyboard_InputViewCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQtVirtualKeyboard_InputViewCall9)(const void *, QExposeEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall10)(const void *, QShowEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall11)(const void *, QHideEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall12)(const void *, QCloseEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall14)(const void *, QFocusEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_InputViewCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQtVirtualKeyboard_InputViewCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQtVirtualKeyboard_InputViewCall18)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQtVirtualKeyboard_InputViewCall19)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQtVirtualKeyboard_InputViewCall20)(const void *, int *);
typedef const QSize * (*CuteQtVirtualKeyboard_InputViewCall21)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall22)(const void *, QPaintEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQtVirtualKeyboard_InputViewCall24)(const void *, QTouchEvent *, int *);
typedef void * (*CuteQtVirtualKeyboard_InputViewCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_InputViewCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputViewCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_InputView : public QtVirtualKeyboard::InputView {
public:
  using QtVirtualKeyboard::InputView::InputView;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  void QtVirtualKeyboard::InputView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::InputView::resizeEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickView::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickView::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::keyPressEvent(a0);
  }

  //  void QQuickView::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::keyReleaseEvent(a0);
  }

  //  void QQuickView::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mousePressEvent(a0);
  }

  //  void QQuickView::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mouseReleaseEvent(a0);
  }

  //  void QQuickView::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mouseMoveEvent(a0);
  }

  //  QObject *QQuickWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQuickWindow::focusObject();
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QQuickWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QQuickWindow::accessibleRoot();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::exposeEvent(a0);
  }

  //  void QQuickWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::showEvent(a0);
  }

  //  void QQuickWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::hideEvent(a0);
  }

  //  void QQuickWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::closeEvent(a0);
  }

  //  void QQuickWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall13 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusInEvent(a0);
  }

  //  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall14 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusOutEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall15 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall15>(taken[15]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWindow::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall16 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseDoubleClickEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall17 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabletevent)
  //  void QQuickWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall18 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall19 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall20 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall20>(taken[20]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall21 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall21>(taken[21]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall22 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall23 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall24 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall25 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall25>(taken[25]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall26 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputViewCall27 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall27>(taken[27]);
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
      CuteQtVirtualKeyboard_InputViewCall28 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall28>(taken[28]);
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
      CuteQtVirtualKeyboard_InputViewCall29 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall29>(taken[29]);
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
      CuteQtVirtualKeyboard_InputViewCall30 call = reinterpret_cast<CuteQtVirtualKeyboard_InputViewCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::InputView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard9InputView10metaObjectEv(
    const QtVirtualKeyboard::InputView *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::InputView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard9InputView11qt_metacastEPKc(
    QtVirtualKeyboard::InputView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::InputView::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard9InputView11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::InputView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::InputView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard9InputView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::InputView::tr(s, c, n));
}

//  QtVirtualKeyboard::InputView::InputView(QWindow *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::InputView *ritual_ZN17QtVirtualKeyboard9InputViewC1EP7QWindow(
    QWindow *parent) {
  return new CuteQtVirtualKeyboard_InputView(parent);
}

//  void QtVirtualKeyboard::InputView::sizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard9InputView11sizeChangedEv(
    QtVirtualKeyboard::InputView *self) {
  self->sizeChanged();
}

//  void QtVirtualKeyboard::InputView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard9InputView11resizeEventEP12QResizeEvent(
    QtVirtualKeyboard::InputView *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  a Python function taken by a CuteQtVirtualKeyboard_InputView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_InputView(
    QtVirtualKeyboard::InputView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_InputView *>(self)->take(key, call);
}

//  void QtVirtualKeyboard::InputView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard9InputView11resizeEventEP12QResizeEvent(
    QtVirtualKeyboard::InputView *self,
    QResizeEvent *event) {
  static_cast<OwnQtVirtualKeyboard_InputView *>(self)->OwnQtVirtualKeyboard_InputView::resizeEvent(
      event);
}

#endif  // QT_CONFIG(vkb_desktop)
