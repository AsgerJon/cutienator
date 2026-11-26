//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickApplicationWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickApplicationWindow : QQuickApplicationWindow {
  using QQuickApplicationWindow::classBegin;
  using QQuickApplicationWindow::componentComplete;
  using QQuickApplicationWindow::resizeEvent;
};

//  A QQuickApplicationWindow that Python can take functions over in. Every QQuickApplicationWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickApplicationWindowCall0)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowCall1)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowCall2)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickApplicationWindowCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickApplicationWindowCall4)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQQuickApplicationWindowCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickApplicationWindowCall6)(const void *, QExposeEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall7)(const void *, QShowEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall8)(const void *, QHideEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall9)(const void *, QCloseEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall17)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickApplicationWindowCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQQuickApplicationWindowCall19)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQQuickApplicationWindowCall20)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQQuickApplicationWindowCall21)(const void *, int *);
typedef const QSize * (*CuteQQuickApplicationWindowCall22)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowCall23)(const void *, QPaintEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQQuickApplicationWindowCall25)(const void *, QTouchEvent *, int *);
typedef void * (*CuteQQuickApplicationWindowCall26)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickApplicationWindowCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationWindowCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationWindowCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationWindowCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationWindowCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickApplicationWindowCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickApplicationWindow : public QQuickApplicationWindow {
public:
  using QQuickApplicationWindow::QQuickApplicationWindow;
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
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
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

  //  void QQuickApplicationWindow::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall0 call = reinterpret_cast<CuteQQuickApplicationWindowCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickApplicationWindow::classBegin();
  }

  //  void QQuickApplicationWindow::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall1 call = reinterpret_cast<CuteQQuickApplicationWindowCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickApplicationWindow::componentComplete();
  }

  //  void QQuickApplicationWindow::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall2 call = reinterpret_cast<CuteQQuickApplicationWindowCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickApplicationWindow::resizeEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWindowQmlImpl::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall3 call = reinterpret_cast<CuteQQuickApplicationWindowCall3>(taken[3]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWindowQmlImpl::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QObject *QQuickWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall4 call = reinterpret_cast<CuteQQuickApplicationWindowCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQuickWindow::focusObject();
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QQuickWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall5 call = reinterpret_cast<CuteQQuickApplicationWindowCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QQuickWindow::accessibleRoot();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall6 call = reinterpret_cast<CuteQQuickApplicationWindowCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::exposeEvent(a0);
  }

  //  void QQuickWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall7 call = reinterpret_cast<CuteQQuickApplicationWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::showEvent(a0);
  }

  //  void QQuickWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall8 call = reinterpret_cast<CuteQQuickApplicationWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::hideEvent(a0);
  }

  //  void QQuickWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall9 call = reinterpret_cast<CuteQQuickApplicationWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::closeEvent(a0);
  }

  //  void QQuickWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall10 call = reinterpret_cast<CuteQQuickApplicationWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusInEvent(a0);
  }

  //  void QQuickWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall11 call = reinterpret_cast<CuteQQuickApplicationWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::focusOutEvent(a0);
  }

  //  void QQuickWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall12 call = reinterpret_cast<CuteQQuickApplicationWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyPressEvent(a0);
  }

  //  void QQuickWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall13 call = reinterpret_cast<CuteQQuickApplicationWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::keyReleaseEvent(a0);
  }

  //  void QQuickWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall14 call = reinterpret_cast<CuteQQuickApplicationWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mousePressEvent(a0);
  }

  //  void QQuickWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall15 call = reinterpret_cast<CuteQQuickApplicationWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseReleaseEvent(a0);
  }

  //  void QQuickWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall16 call = reinterpret_cast<CuteQQuickApplicationWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindow::mouseDoubleClickEvent(a0);
  }

  //  void QQuickWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall17 call = reinterpret_cast<CuteQQuickApplicationWindowCall17>(taken[17]);
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
      CuteQQuickApplicationWindowCall18 call = reinterpret_cast<CuteQQuickApplicationWindowCall18>(taken[18]);
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
      CuteQQuickApplicationWindowCall19 call = reinterpret_cast<CuteQQuickApplicationWindowCall19>(taken[19]);
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
      CuteQQuickApplicationWindowCall20 call = reinterpret_cast<CuteQQuickApplicationWindowCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall21 call = reinterpret_cast<CuteQQuickApplicationWindowCall21>(taken[21]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall22 call = reinterpret_cast<CuteQQuickApplicationWindowCall22>(taken[22]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall23 call = reinterpret_cast<CuteQQuickApplicationWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall24 call = reinterpret_cast<CuteQQuickApplicationWindowCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall25 call = reinterpret_cast<CuteQQuickApplicationWindowCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickApplicationWindowCall26 call = reinterpret_cast<CuteQQuickApplicationWindowCall26>(taken[26]);
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
      CuteQQuickApplicationWindowCall27 call = reinterpret_cast<CuteQQuickApplicationWindowCall27>(taken[27]);
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
      CuteQQuickApplicationWindowCall28 call = reinterpret_cast<CuteQQuickApplicationWindowCall28>(taken[28]);
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
      CuteQQuickApplicationWindowCall29 call = reinterpret_cast<CuteQQuickApplicationWindowCall29>(taken[29]);
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
      CuteQQuickApplicationWindowCall30 call = reinterpret_cast<CuteQQuickApplicationWindowCall30>(taken[30]);
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
      CuteQQuickApplicationWindowCall31 call = reinterpret_cast<CuteQQuickApplicationWindowCall31>(taken[31]);
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
      CuteQQuickApplicationWindowCall32 call = reinterpret_cast<CuteQQuickApplicationWindowCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickApplicationWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickApplicationWindow10metaObjectEv(
    const QQuickApplicationWindow *self) {
  return self->metaObject();
}

//  void *QQuickApplicationWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickApplicationWindow11qt_metacastEPKc(
    QQuickApplicationWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickApplicationWindow::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickApplicationWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickApplicationWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickApplicationWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickApplicationWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickApplicationWindow::tr(s, c, n));
}

//  void QQuickApplicationWindow::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow21qt_qmlMarker_attachedEv(
    QQuickApplicationWindow *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickApplicationWindow::QQuickApplicationWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickApplicationWindow *ritual_ZN23QQuickApplicationWindowC1EP7QWindow(
    QWindow *parent) {
  return new CuteQQuickApplicationWindow(parent);
}

//  QQuickApplicationWindow::~QQuickApplicationWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindowD1Ev(QQuickApplicationWindow *self) {
  delete self;
}

//  QQuickApplicationWindowAttached
//      *QQuickApplicationWindow::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickApplicationWindowAttached *ritual_ZN23QQuickApplicationWindow21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickApplicationWindow::qmlAttachedProperties(object);
}

//  QQuickItem *QQuickApplicationWindow::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow10backgroundEv(
    const QQuickApplicationWindow *self) {
  return self->background();
}

//  void QQuickApplicationWindow::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow13setBackgroundEP10QQuickItem(
    QQuickApplicationWindow *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  QQuickItem *QQuickApplicationWindow::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow11contentItemEv(
    const QQuickApplicationWindow *self) {
  return self->contentItem();
}

//  QQuickItem *QQuickApplicationWindow::activeFocusControl() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow18activeFocusControlEv(
    const QQuickApplicationWindow *self) {
  return self->activeFocusControl();
}

//  QQuickItem *QQuickApplicationWindow::header() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow6headerEv(
    const QQuickApplicationWindow *self) {
  return self->header();
}

//  void QQuickApplicationWindow::setHeader(QQuickItem *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow9setHeaderEP10QQuickItem(
    QQuickApplicationWindow *self,
    QQuickItem *header) {
  self->setHeader(header);
}

//  QQuickItem *QQuickApplicationWindow::footer() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow6footerEv(
    const QQuickApplicationWindow *self) {
  return self->footer();
}

//  void QQuickApplicationWindow::setFooter(QQuickItem *footer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow9setFooterEP10QQuickItem(
    QQuickApplicationWindow *self,
    QQuickItem *footer) {
  self->setFooter(footer);
}

//  QFont QQuickApplicationWindow::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QQuickApplicationWindow4fontEv(
    const QQuickApplicationWindow *self) {
  return new QFont(self->font());
}

//  void QQuickApplicationWindow::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow7setFontERK5QFont(
    QQuickApplicationWindow *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QQuickApplicationWindow::resetFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow9resetFontEv(
    QQuickApplicationWindow *self) {
  self->resetFont();
}

//  QLocale QQuickApplicationWindow::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK23QQuickApplicationWindow6localeEv(
    const QQuickApplicationWindow *self) {
  return new QLocale(self->locale());
}

//  void QQuickApplicationWindow::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow9setLocaleERK7QLocale(
    QQuickApplicationWindow *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QQuickApplicationWindow::resetLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow11resetLocaleEv(
    QQuickApplicationWindow *self) {
  self->resetLocale();
}

//  QQuickItem *QQuickApplicationWindow::menuBar() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickApplicationWindow7menuBarEv(
    const QQuickApplicationWindow *self) {
  return self->menuBar();
}

//  void QQuickApplicationWindow::setMenuBar(QQuickItem *menuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow10setMenuBarEP10QQuickItem(
    QQuickApplicationWindow *self,
    QQuickItem *menuBar) {
  self->setMenuBar(menuBar);
}

//  void QQuickApplicationWindow::backgroundChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow17backgroundChangedEv(
    QQuickApplicationWindow *self) {
  self->backgroundChanged();
}

//  void QQuickApplicationWindow::activeFocusControlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow25activeFocusControlChangedEv(
    QQuickApplicationWindow *self) {
  self->activeFocusControlChanged();
}

//  void QQuickApplicationWindow::headerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow13headerChangedEv(
    QQuickApplicationWindow *self) {
  self->headerChanged();
}

//  void QQuickApplicationWindow::footerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow13footerChangedEv(
    QQuickApplicationWindow *self) {
  self->footerChanged();
}

//  void QQuickApplicationWindow::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow11fontChangedEv(
    QQuickApplicationWindow *self) {
  self->fontChanged();
}

//  void QQuickApplicationWindow::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow13localeChangedEv(
    QQuickApplicationWindow *self) {
  self->localeChanged();
}

//  void QQuickApplicationWindow::menuBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow14menuBarChangedEv(
    QQuickApplicationWindow *self) {
  self->menuBarChanged();
}

//  void QQuickApplicationWindow::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow17topPaddingChangedEv(
    QQuickApplicationWindow *self) {
  self->topPaddingChanged();
}

//  void QQuickApplicationWindow::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow18leftPaddingChangedEv(
    QQuickApplicationWindow *self) {
  self->leftPaddingChanged();
}

//  void QQuickApplicationWindow::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow19rightPaddingChangedEv(
    QQuickApplicationWindow *self) {
  self->rightPaddingChanged();
}

//  void QQuickApplicationWindow::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow20bottomPaddingChangedEv(
    QQuickApplicationWindow *self) {
  self->bottomPaddingChanged();
}

//  bool QQuickApplicationWindow::isComponentComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickApplicationWindow19isComponentCompleteEv(
    const QQuickApplicationWindow *self) {
  return self->isComponentComplete();
}

//  void QQuickApplicationWindow::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow10classBeginEv(
    QQuickApplicationWindow *self) {
  self->classBegin();
}

//  void QQuickApplicationWindow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow17componentCompleteEv(
    QQuickApplicationWindow *self) {
  self->componentComplete();
}

//  void QQuickApplicationWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickApplicationWindow11resizeEventEP12QResizeEvent(
    QQuickApplicationWindow *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  QQuickApplicationWindowPrivate *QQuickApplicationWindow::d_func()
extern "C" Q_DECL_EXPORT
QQuickApplicationWindowPrivate *ritual_ZN23QQuickApplicationWindow6d_funcEv(
    QQuickApplicationWindow *self) {
  return self->d_func();
}

//  const QQuickApplicationWindowPrivate *QQuickApplicationWindow::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickApplicationWindowPrivate *ritual_ZNK23QQuickApplicationWindow6d_funcEv(
    const QQuickApplicationWindow *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickApplicationWindow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickApplicationWindow(
    QQuickApplicationWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickApplicationWindow *>(self)->take(key, call);
}

//  void QQuickApplicationWindow::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickApplicationWindow10classBeginEv(
    QQuickApplicationWindow *self) {
  static_cast<OwnQQuickApplicationWindow *>(self)->OwnQQuickApplicationWindow::classBegin();
}

//  void QQuickApplicationWindow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickApplicationWindow17componentCompleteEv(
    QQuickApplicationWindow *self) {
  static_cast<OwnQQuickApplicationWindow *>(self)->OwnQQuickApplicationWindow::componentComplete();
}

//  void QQuickApplicationWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickApplicationWindow11resizeEventEP12QResizeEvent(
    QQuickApplicationWindow *self,
    QResizeEvent *event) {
  static_cast<OwnQQuickApplicationWindow *>(self)->OwnQQuickApplicationWindow::resizeEvent(
      event);
}
