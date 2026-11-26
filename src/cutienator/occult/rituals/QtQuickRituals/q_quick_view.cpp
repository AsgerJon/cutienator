//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickview.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qanystringview.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlerror.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QQuickView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickView : QQuickView {
  using QQuickView::resizeEvent;
  using QQuickView::timerEvent;
  using QQuickView::keyPressEvent;
  using QQuickView::keyReleaseEvent;
  using QQuickView::mousePressEvent;
  using QQuickView::mouseReleaseEvent;
  using QQuickView::mouseMoveEvent;
};

//  A QQuickView that Python can take functions over in. Every QQuickView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickViewCall0)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall1)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall2)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickViewCall3)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickViewCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickViewCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickViewCall6)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickViewCall7)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQQuickViewCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickViewCall9)(const void *, QExposeEvent *, int *);
typedef void (*CuteQQuickViewCall10)(const void *, QShowEvent *, int *);
typedef void (*CuteQQuickViewCall11)(const void *, QHideEvent *, int *);
typedef void (*CuteQQuickViewCall12)(const void *, QCloseEvent *, int *);
typedef void (*CuteQQuickViewCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickViewCall14)(const void *, QFocusEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickViewCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickViewCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQQuickViewCall18)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQQuickViewCall19)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQQuickViewCall20)(const void *, int *);
typedef const QSize * (*CuteQQuickViewCall21)(const void *, int *);
typedef void (*CuteQQuickViewCall22)(const void *, QPaintEvent *, int *);
typedef void (*CuteQQuickViewCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQQuickViewCall24)(const void *, QTouchEvent *, int *);
typedef void * (*CuteQQuickViewCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickViewCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickViewCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickView : public QQuickView {
public:
  using QQuickView::QQuickView;
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

  //  void QQuickView::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickViewCall0 call = reinterpret_cast<CuteQQuickViewCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::resizeEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickView::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickViewCall1 call = reinterpret_cast<CuteQQuickViewCall1>(taken[1]);
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
      CuteQQuickViewCall2 call = reinterpret_cast<CuteQQuickViewCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::keyPressEvent(a0);
  }

  //  void QQuickView::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickViewCall3 call = reinterpret_cast<CuteQQuickViewCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::keyReleaseEvent(a0);
  }

  //  void QQuickView::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickViewCall4 call = reinterpret_cast<CuteQQuickViewCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mousePressEvent(a0);
  }

  //  void QQuickView::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickViewCall5 call = reinterpret_cast<CuteQQuickViewCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mouseReleaseEvent(a0);
  }

  //  void QQuickView::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickViewCall6 call = reinterpret_cast<CuteQQuickViewCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickView::mouseMoveEvent(a0);
  }

  //  QObject *QQuickWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickViewCall7 call = reinterpret_cast<CuteQQuickViewCall7>(taken[7]);
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
      CuteQQuickViewCall8 call = reinterpret_cast<CuteQQuickViewCall8>(taken[8]);
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
      CuteQQuickViewCall9 call = reinterpret_cast<CuteQQuickViewCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::exposeEvent(a0);
  }

  //  void QQuickWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickViewCall10 call = reinterpret_cast<CuteQQuickViewCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::showEvent(a0);
  }

  //  void QQuickWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickViewCall11 call = reinterpret_cast<CuteQQuickViewCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::hideEvent(a0);
  }

  //  void QQuickWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickViewCall12 call = reinterpret_cast<CuteQQuickViewCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::closeEvent(a0);
  }

  //  void QQuickWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickViewCall13 call = reinterpret_cast<CuteQQuickViewCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusInEvent(a0);
  }

  //  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickViewCall14 call = reinterpret_cast<CuteQQuickViewCall14>(taken[14]);
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
      CuteQQuickViewCall15 call = reinterpret_cast<CuteQQuickViewCall15>(taken[15]);
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
      CuteQQuickViewCall16 call = reinterpret_cast<CuteQQuickViewCall16>(taken[16]);
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
      CuteQQuickViewCall17 call = reinterpret_cast<CuteQQuickViewCall17>(taken[17]);
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
      CuteQQuickViewCall18 call = reinterpret_cast<CuteQQuickViewCall18>(taken[18]);
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
      CuteQQuickViewCall19 call = reinterpret_cast<CuteQQuickViewCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickViewCall20 call = reinterpret_cast<CuteQQuickViewCall20>(taken[20]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickViewCall21 call = reinterpret_cast<CuteQQuickViewCall21>(taken[21]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickViewCall22 call = reinterpret_cast<CuteQQuickViewCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickViewCall23 call = reinterpret_cast<CuteQQuickViewCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickViewCall24 call = reinterpret_cast<CuteQQuickViewCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickViewCall25 call = reinterpret_cast<CuteQQuickViewCall25>(taken[25]);
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
      CuteQQuickViewCall26 call = reinterpret_cast<CuteQQuickViewCall26>(taken[26]);
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
      CuteQQuickViewCall27 call = reinterpret_cast<CuteQQuickViewCall27>(taken[27]);
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
      CuteQQuickViewCall28 call = reinterpret_cast<CuteQQuickViewCall28>(taken[28]);
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
      CuteQQuickViewCall29 call = reinterpret_cast<CuteQQuickViewCall29>(taken[29]);
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
      CuteQQuickViewCall30 call = reinterpret_cast<CuteQQuickViewCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickView10metaObjectEv(
    const QQuickView *self) {
  return self->metaObject();
}

//  void *QQuickView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QQuickView11qt_metacastEPKc(
    QQuickView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QQuickView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickView::tr(s, c, n));
}

//  QQuickView::QQuickView(QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN10QQuickViewC1EP7QWindow(QWindow *parent) {
  return new CuteQQuickView(parent);
}

//  QQuickView::QQuickView(QQmlEngine *engine, QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN10QQuickViewC1EP10QQmlEngineP7QWindow(
    QQmlEngine *engine,
    QWindow *parent) {
  return new CuteQQuickView(engine, parent);
}

//  QQuickView::QQuickView(const QUrl &source, QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN10QQuickViewC1ERK4QUrlP7QWindow(
    const QUrl *source,
    QWindow *parent) {
  return new CuteQQuickView(*source, parent);
}

//  QQuickView::QQuickView(QAnyStringView uri, QAnyStringView typeName,
//      QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN10QQuickViewC1E14QAnyStringViewS0_P7QWindow(
    const QString *uri,
    const QString *typeName,
    QWindow *parent) {
  return new CuteQQuickView(
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      parent);
}

//  QQuickView::QQuickView(const QUrl &source, QQuickRenderControl
//      *renderControl)
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN10QQuickViewC1ERK4QUrlP19QQuickRenderControl(
    const QUrl *source,
    QQuickRenderControl *renderControl) {
  return new CuteQQuickView(*source, renderControl);
}

//  QQuickView::~QQuickView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickViewD1Ev(QQuickView *self) {
  delete self;
}

//  QUrl QQuickView::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQuickView6sourceEv(const QQuickView *self) {
  return new QUrl(self->source());
}

//  QQmlEngine *QQuickView::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK10QQuickView6engineEv(const QQuickView *self) {
  return self->engine();
}

//  QQmlContext *QQuickView::rootContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK10QQuickView11rootContextEv(const QQuickView *self) {
  return self->rootContext();
}

//  QQuickItem *QQuickView::rootObject() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickView10rootObjectEv(const QQuickView *self) {
  return self->rootObject();
}

//  ResizeMode QQuickView::resizeMode() const
extern "C" Q_DECL_EXPORT
QQuickView::ResizeMode ritual_ZNK10QQuickView10resizeModeEv(
    const QQuickView *self) {
  return self->resizeMode();
}

//  void QQuickView::setResizeMode(ResizeMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView13setResizeModeENS_10ResizeModeE(
    QQuickView *self,
    QQuickView::ResizeMode a0) {
  self->setResizeMode(a0);
}

//  Status QQuickView::status() const
extern "C" Q_DECL_EXPORT
QQuickView::Status ritual_ZNK10QQuickView6statusEv(const QQuickView *self) {
  return self->status();
}

//  QList<QQmlError> QQuickView::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK10QQuickView6errorsEv(const QQuickView *self) {
  return new QList<QQmlError>(self->errors());
}

//  QSize QQuickView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QQuickView8sizeHintEv(const QQuickView *self) {
  return new QSize(self->sizeHint());
}

//  QSize QQuickView::initialSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QQuickView11initialSizeEv(const QQuickView *self) {
  return new QSize(self->initialSize());
}

//  void QQuickView::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView9setSourceERK4QUrl(
    QQuickView *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  void QQuickView::loadFromModule(QAnyStringView uri, QAnyStringView
//      typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView14loadFromModuleE14QAnyStringViewS0_(
    QQuickView *self,
    const QString *uri,
    const QString *typeName) {
  self->loadFromModule(QAnyStringView(*uri), QAnyStringView(*typeName));
}

//  void QQuickView::setInitialProperties(const QVariantMap
//      &initialProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView20setInitialPropertiesERK4QMapI7QString8QVariantE(
    QQuickView *self,
    const QMap<QString, QVariant> *initialProperties) {
  self->setInitialProperties(*initialProperties);
}

//  void QQuickView::setContent(const QUrl &url, QQmlComponent *component,
//      QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView10setContentERK4QUrlP13QQmlComponentP7QObject(
    QQuickView *self,
    const QUrl *url,
    QQmlComponent *component,
    QObject *item) {
  self->setContent(*url, component, item);
}

//  void QQuickView::statusChanged(QQuickView::Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView13statusChangedENS_6StatusE(
    QQuickView *self,
    QQuickView::Status a0) {
  self->statusChanged(a0);
}

//  void QQuickView::continueExecute()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView15continueExecuteEv(QQuickView *self) {
  self->continueExecute();
}

//  void QQuickView::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView11resizeEventEP12QResizeEvent(
    QQuickView *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QQuickView::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView10timerEventEP11QTimerEvent(
    QQuickView *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QQuickView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView13keyPressEventEP9QKeyEvent(
    QQuickView *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickView::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView15keyReleaseEventEP9QKeyEvent(
    QQuickView *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QQuickView::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView15mousePressEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QQuickView::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView17mouseReleaseEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QQuickView::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickView14mouseMoveEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  QQuickViewPrivate *QQuickView::d_func()
extern "C" Q_DECL_EXPORT
QQuickViewPrivate *ritual_ZN10QQuickView6d_funcEv(QQuickView *self) {
  return self->d_func();
}

//  const QQuickViewPrivate *QQuickView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickViewPrivate *ritual_ZNK10QQuickView6d_funcEv(
    const QQuickView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickView(QQuickView *self, const char *key, void *call) {
  return static_cast<CuteQQuickView *>(self)->take(key, call);
}

//  void QQuickView::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView11resizeEventEP12QResizeEvent(
    QQuickView *self,
    QResizeEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::resizeEvent(a0);
}

//  void QQuickView::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView10timerEventEP11QTimerEvent(
    QQuickView *self,
    QTimerEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::timerEvent(a0);
}

//  void QQuickView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView13keyPressEventEP9QKeyEvent(
    QQuickView *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::keyPressEvent(a0);
}

//  void QQuickView::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView15keyReleaseEventEP9QKeyEvent(
    QQuickView *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::keyReleaseEvent(a0);
}

//  void QQuickView::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView15mousePressEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::mousePressEvent(a0);
}

//  void QQuickView::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView17mouseReleaseEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::mouseReleaseEvent(a0);
}

//  void QQuickView::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickView14mouseMoveEventEP11QMouseEvent(
    QQuickView *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickView *>(self)->OwnQQuickView::mouseMoveEvent(a0);
}
