//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qabstract3dgraph.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/qabstract3dgraph.h>
#include <QtCore/qstring.h>
#include <QtDataVisualization/qabstract3dinputhandler.h>
#include <QtDataVisualization/q3dtheme.h>
#include <QtGui/qvectornd.h>
#include <QtDataVisualization/qcustom3ditem.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qlocale.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstract3DGraph may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstract3DGraph : QAbstract3DGraph {
  using QAbstract3DGraph::event;
  using QAbstract3DGraph::resizeEvent;
  using QAbstract3DGraph::exposeEvent;
  using QAbstract3DGraph::mouseDoubleClickEvent;
  using QAbstract3DGraph::touchEvent;
  using QAbstract3DGraph::mousePressEvent;
  using QAbstract3DGraph::mouseReleaseEvent;
  using QAbstract3DGraph::mouseMoveEvent;
  using QAbstract3DGraph::wheelEvent;
};

//  A QAbstract3DGraph that Python can take functions over in. Every QAbstract3DGraph
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstract3DGraphCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DGraphCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall2)(const void *, QResizeEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall3)(const void *, QExposeEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall5)(const void *, QTouchEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall8)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQAbstract3DGraphCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef int (*CuteQAbstract3DGraphCall10)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQAbstract3DGraphCall11)(const void *, int *);
typedef const QSize * (*CuteQAbstract3DGraphCall12)(const void *, int *);
typedef void * (*CuteQAbstract3DGraphCall13)(const void *, int *);
typedef void * (*CuteQAbstract3DGraphCall14)(const void *, int *);
typedef void (*CuteQAbstract3DGraphCall15)(const void *, QPaintEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall16)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall19)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall20)(const void *, QHideEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall21)(const void *, QCloseEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstract3DGraphCall23)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAbstract3DGraphCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQAbstract3DGraphCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DGraphCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DGraph : public QAbstract3DGraph {
public:
  using QAbstract3DGraph::QAbstract3DGraph;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QAbstract3DGraph16shadowsSupportedEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QAbstract3DGraph::shadowsSupported() const
  bool shadowsSupported() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DGraphCall0 call = reinterpret_cast<CuteQAbstract3DGraphCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstract3DGraph::shadowsSupported();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QAbstract3DGraph::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DGraphCall1 call = reinterpret_cast<CuteQAbstract3DGraphCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstract3DGraph::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QAbstract3DGraph::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DGraphCall2 call = reinterpret_cast<CuteQAbstract3DGraphCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::resizeEvent(event);
  }

  //  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
  void exposeEvent(QExposeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DGraphCall3 call = reinterpret_cast<CuteQAbstract3DGraphCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::exposeEvent(event);
  }

  //  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstract3DGraphCall4 call = reinterpret_cast<CuteQAbstract3DGraphCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstract3DGraphCall5 call = reinterpret_cast<CuteQAbstract3DGraphCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::touchEvent(event);
  }

  //  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstract3DGraphCall6 call = reinterpret_cast<CuteQAbstract3DGraphCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mousePressEvent(event);
  }

  //  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstract3DGraphCall7 call = reinterpret_cast<CuteQAbstract3DGraphCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseReleaseEvent(event);
  }

  //  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstract3DGraphCall8 call = reinterpret_cast<CuteQAbstract3DGraphCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QAbstract3DGraph::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstract3DGraphCall9 call = reinterpret_cast<CuteQAbstract3DGraphCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstract3DGraphCall10 call = reinterpret_cast<CuteQAbstract3DGraphCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstract3DGraphCall11 call = reinterpret_cast<CuteQAbstract3DGraphCall11>(taken[11]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstract3DGraphCall12 call = reinterpret_cast<CuteQAbstract3DGraphCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstract3DGraphCall13 call = reinterpret_cast<CuteQAbstract3DGraphCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstract3DGraphCall14 call = reinterpret_cast<CuteQAbstract3DGraphCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstract3DGraphCall15 call = reinterpret_cast<CuteQAbstract3DGraphCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstract3DGraphCall16 call = reinterpret_cast<CuteQAbstract3DGraphCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstract3DGraphCall17 call = reinterpret_cast<CuteQAbstract3DGraphCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstract3DGraphCall18 call = reinterpret_cast<CuteQAbstract3DGraphCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstract3DGraphCall19 call = reinterpret_cast<CuteQAbstract3DGraphCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstract3DGraphCall20 call = reinterpret_cast<CuteQAbstract3DGraphCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstract3DGraphCall21 call = reinterpret_cast<CuteQAbstract3DGraphCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstract3DGraphCall22 call = reinterpret_cast<CuteQAbstract3DGraphCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstract3DGraphCall23 call = reinterpret_cast<CuteQAbstract3DGraphCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstract3DGraphCall24 call = reinterpret_cast<CuteQAbstract3DGraphCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstract3DGraphCall25 call = reinterpret_cast<CuteQAbstract3DGraphCall25>(taken[25]);
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
      CuteQAbstract3DGraphCall26 call = reinterpret_cast<CuteQAbstract3DGraphCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstract3DGraphCall27 call = reinterpret_cast<CuteQAbstract3DGraphCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstract3DGraphCall28 call = reinterpret_cast<CuteQAbstract3DGraphCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstract3DGraphCall29 call = reinterpret_cast<CuteQAbstract3DGraphCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstract3DGraphCall30 call = reinterpret_cast<CuteQAbstract3DGraphCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstract3DGraphCall31 call = reinterpret_cast<CuteQAbstract3DGraphCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DGraph::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAbstract3DGraph10metaObjectEv(
    const QAbstract3DGraph *self) {
  return self->metaObject();
}

//  QString QAbstract3DGraph::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAbstract3DGraph2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstract3DGraph::tr(s, c, n));
}

//  QAbstract3DGraph::QAbstract3DGraph(QAbstract3DGraphPrivate *d, const
//      QSurfaceFormat *format, QWindow *parent)
extern "C" Q_DECL_EXPORT
QAbstract3DGraph *ritual_ZN16QAbstract3DGraphC1EP23QAbstract3DGraphPrivatePK14QSurfaceFormatP7QWindow(
    QAbstract3DGraphPrivate *d,
    const QSurfaceFormat *format,
    QWindow *parent) {
  return new CuteQAbstract3DGraph(d, format, parent);
}

//  QAbstract3DGraph::~QAbstract3DGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraphD1Ev(QAbstract3DGraph *self) {
  delete self;
}

//  void QAbstract3DGraph::addInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph15addInputHandlerEP23QAbstract3DInputHandler(
    QAbstract3DGraph *self,
    QAbstract3DInputHandler *inputHandler) {
  self->addInputHandler(inputHandler);
}

//  void QAbstract3DGraph::releaseInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph19releaseInputHandlerEP23QAbstract3DInputHandler(
    QAbstract3DGraph *self,
    QAbstract3DInputHandler *inputHandler) {
  self->releaseInputHandler(inputHandler);
}

//  void QAbstract3DGraph::setActiveInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph21setActiveInputHandlerEP23QAbstract3DInputHandler(
    QAbstract3DGraph *self,
    QAbstract3DInputHandler *inputHandler) {
  self->setActiveInputHandler(inputHandler);
}

//  QAbstract3DInputHandler *QAbstract3DGraph::activeInputHandler() const
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_ZNK16QAbstract3DGraph18activeInputHandlerEv(
    const QAbstract3DGraph *self) {
  return self->activeInputHandler();
}

//  QList<QAbstract3DInputHandler *> QAbstract3DGraph::inputHandlers() const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DInputHandler *> *ritual_ZNK16QAbstract3DGraph13inputHandlersEv(
    const QAbstract3DGraph *self) {
  return new QList<QAbstract3DInputHandler *>(self->inputHandlers());
}

//  void QAbstract3DGraph::addTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph8addThemeEP8Q3DTheme(
    QAbstract3DGraph *self,
    Q3DTheme *theme) {
  self->addTheme(theme);
}

//  void QAbstract3DGraph::releaseTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph12releaseThemeEP8Q3DTheme(
    QAbstract3DGraph *self,
    Q3DTheme *theme) {
  self->releaseTheme(theme);
}

//  void QAbstract3DGraph::setActiveTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph14setActiveThemeEP8Q3DTheme(
    QAbstract3DGraph *self,
    Q3DTheme *theme) {
  self->setActiveTheme(theme);
}

//  Q3DTheme *QAbstract3DGraph::activeTheme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZNK16QAbstract3DGraph11activeThemeEv(
    const QAbstract3DGraph *self) {
  return self->activeTheme();
}

//  QList<Q3DTheme *> QAbstract3DGraph::themes() const
extern "C" Q_DECL_EXPORT
QList<Q3DTheme *> *ritual_ZNK16QAbstract3DGraph6themesEv(
    const QAbstract3DGraph *self) {
  return new QList<Q3DTheme *>(self->themes());
}

//  void QAbstract3DGraph::setSelectionMode(SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph16setSelectionModeE6QFlagsINS_13SelectionFlagEE(
    QAbstract3DGraph *self,
    int mode) {
  self->setSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  SelectionFlags QAbstract3DGraph::selectionMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstract3DGraph13selectionModeEv(
    const QAbstract3DGraph *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  void QAbstract3DGraph::setShadowQuality(ShadowQuality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph16setShadowQualityENS_13ShadowQualityE(
    QAbstract3DGraph *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->setShadowQuality(quality);
}

//  ShadowQuality QAbstract3DGraph::shadowQuality() const
extern "C" Q_DECL_EXPORT
QAbstract3DGraph::ShadowQuality ritual_ZNK16QAbstract3DGraph13shadowQualityEv(
    const QAbstract3DGraph *self) {
  return self->shadowQuality();
}

//  bool QAbstract3DGraph::shadowsSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph16shadowsSupportedEv(
    const QAbstract3DGraph *self) {
  return self->shadowsSupported();
}

//  Q3DScene *QAbstract3DGraph::scene() const
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZNK16QAbstract3DGraph5sceneEv(
    const QAbstract3DGraph *self) {
  return self->scene();
}

//  void QAbstract3DGraph::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph14clearSelectionEv(QAbstract3DGraph *self) {
  self->clearSelection();
}

//  bool QAbstract3DGraph::hasSeries(QAbstract3DSeries *series) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph9hasSeriesEP17QAbstract3DSeries(
    const QAbstract3DGraph *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  int QAbstract3DGraph::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QAbstract3DGraph13addCustomItemEP13QCustom3DItem(
    QAbstract3DGraph *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void QAbstract3DGraph::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph17removeCustomItemsEv(
    QAbstract3DGraph *self) {
  self->removeCustomItems();
}

//  void QAbstract3DGraph::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph16removeCustomItemEP13QCustom3DItem(
    QAbstract3DGraph *self,
    QCustom3DItem *item) {
  self->removeCustomItem(item);
}

//  void QAbstract3DGraph::removeCustomItemAt(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph18removeCustomItemAtERK9QVector3D(
    QAbstract3DGraph *self,
    const QVector3D *position) {
  self->removeCustomItemAt(*position);
}

//  void QAbstract3DGraph::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph17releaseCustomItemEP13QCustom3DItem(
    QAbstract3DGraph *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  QList<QCustom3DItem *> QAbstract3DGraph::customItems() const
extern "C" Q_DECL_EXPORT
QList<QCustom3DItem *> *ritual_ZNK16QAbstract3DGraph11customItemsEv(
    const QAbstract3DGraph *self) {
  return new QList<QCustom3DItem *>(self->customItems());
}

//  int QAbstract3DGraph::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstract3DGraph18selectedLabelIndexEv(
    const QAbstract3DGraph *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *QAbstract3DGraph::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QAbstract3DGraph12selectedAxisEv(
    const QAbstract3DGraph *self) {
  return self->selectedAxis();
}

//  int QAbstract3DGraph::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstract3DGraph23selectedCustomItemIndexEv(
    const QAbstract3DGraph *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *QAbstract3DGraph::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK16QAbstract3DGraph18selectedCustomItemEv(
    const QAbstract3DGraph *self) {
  return self->selectedCustomItem();
}

//  QImage QAbstract3DGraph::renderToImage(int msaaSamples, const QSize
//      &imageSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QAbstract3DGraph13renderToImageEiRK5QSize(
    QAbstract3DGraph *self,
    int msaaSamples,
    const QSize *imageSize) {
  return new QImage(self->renderToImage(msaaSamples, *imageSize));
}

//  void QAbstract3DGraph::setMeasureFps(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph13setMeasureFpsEb(
    QAbstract3DGraph *self,
    bool enable) {
  self->setMeasureFps(enable);
}

//  bool QAbstract3DGraph::measureFps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph10measureFpsEv(
    const QAbstract3DGraph *self) {
  return self->measureFps();
}

//  qreal QAbstract3DGraph::currentFps() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QAbstract3DGraph10currentFpsEv(
    const QAbstract3DGraph *self) {
  return self->currentFps();
}

//  void QAbstract3DGraph::setOrthoProjection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph18setOrthoProjectionEb(
    QAbstract3DGraph *self,
    bool enable) {
  self->setOrthoProjection(enable);
}

//  bool QAbstract3DGraph::isOrthoProjection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph17isOrthoProjectionEv(
    const QAbstract3DGraph *self) {
  return self->isOrthoProjection();
}

//  ElementType QAbstract3DGraph::selectedElement() const
extern "C" Q_DECL_EXPORT
QAbstract3DGraph::ElementType ritual_ZNK16QAbstract3DGraph15selectedElementEv(
    const QAbstract3DGraph *self) {
  return self->selectedElement();
}

//  void QAbstract3DGraph::setAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph14setAspectRatioEd(
    QAbstract3DGraph *self,
    qreal ratio) {
  self->setAspectRatio(ratio);
}

//  qreal QAbstract3DGraph::aspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QAbstract3DGraph11aspectRatioEv(
    const QAbstract3DGraph *self) {
  return self->aspectRatio();
}

//  void QAbstract3DGraph::setOptimizationHints(OptimizationHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph20setOptimizationHintsE6QFlagsINS_16OptimizationHintEE(
    QAbstract3DGraph *self,
    int hints) {
  self->setOptimizationHints(
      QFlags<QAbstract3DGraph::OptimizationHint>::fromInt(hints));
}

//  OptimizationHints QAbstract3DGraph::optimizationHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstract3DGraph17optimizationHintsEv(
    const QAbstract3DGraph *self) {
  return static_cast<int>(self->optimizationHints().toInt());
}

//  void QAbstract3DGraph::setPolar(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph8setPolarEb(
    QAbstract3DGraph *self,
    bool enable) {
  self->setPolar(enable);
}

//  bool QAbstract3DGraph::isPolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph7isPolarEv(const QAbstract3DGraph *self) {
  return self->isPolar();
}

//  void QAbstract3DGraph::setRadialLabelOffset(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph20setRadialLabelOffsetEf(
    QAbstract3DGraph *self,
    float offset) {
  self->setRadialLabelOffset(offset);
}

//  float QAbstract3DGraph::radialLabelOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QAbstract3DGraph17radialLabelOffsetEv(
    const QAbstract3DGraph *self) {
  return self->radialLabelOffset();
}

//  void QAbstract3DGraph::setHorizontalAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph24setHorizontalAspectRatioEd(
    QAbstract3DGraph *self,
    qreal ratio) {
  self->setHorizontalAspectRatio(ratio);
}

//  qreal QAbstract3DGraph::horizontalAspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QAbstract3DGraph21horizontalAspectRatioEv(
    const QAbstract3DGraph *self) {
  return self->horizontalAspectRatio();
}

//  void QAbstract3DGraph::setReflection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph13setReflectionEb(
    QAbstract3DGraph *self,
    bool enable) {
  self->setReflection(enable);
}

//  bool QAbstract3DGraph::isReflection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph12isReflectionEv(
    const QAbstract3DGraph *self) {
  return self->isReflection();
}

//  void QAbstract3DGraph::setReflectivity(qreal reflectivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph15setReflectivityEd(
    QAbstract3DGraph *self,
    qreal reflectivity) {
  self->setReflectivity(reflectivity);
}

//  qreal QAbstract3DGraph::reflectivity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QAbstract3DGraph12reflectivityEv(
    const QAbstract3DGraph *self) {
  return self->reflectivity();
}

//  void QAbstract3DGraph::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph9setLocaleERK7QLocale(
    QAbstract3DGraph *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QAbstract3DGraph::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16QAbstract3DGraph6localeEv(
    const QAbstract3DGraph *self) {
  return new QLocale(self->locale());
}

//  QVector3D QAbstract3DGraph::queriedGraphPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QAbstract3DGraph20queriedGraphPositionEv(
    const QAbstract3DGraph *self) {
  return new QVector3D(self->queriedGraphPosition());
}

//  void QAbstract3DGraph::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph9setMarginEd(
    QAbstract3DGraph *self,
    qreal margin) {
  self->setMargin(margin);
}

//  qreal QAbstract3DGraph::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QAbstract3DGraph6marginEv(const QAbstract3DGraph *self) {
  return self->margin();
}

//  bool QAbstract3DGraph::hasContext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstract3DGraph10hasContextEv(
    const QAbstract3DGraph *self) {
  return self->hasContext();
}

//  bool QAbstract3DGraph::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAbstract3DGraph5eventEP6QEvent(
    QAbstract3DGraph *self,
    QEvent *event) {
  return self->event(event);
}

//  void QAbstract3DGraph::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph11resizeEventEP12QResizeEvent(
    QAbstract3DGraph *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph11exposeEventEP12QExposeEvent(
    QAbstract3DGraph *self,
    QExposeEvent *event) {
  self->exposeEvent(event);
}

//  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph21mouseDoubleClickEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph10touchEventEP11QTouchEvent(
    QAbstract3DGraph *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph15mousePressEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph17mouseReleaseEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph14mouseMoveEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QAbstract3DGraph::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstract3DGraph10wheelEventEP11QWheelEvent(
    QAbstract3DGraph *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  QAbstract3DGraph as the QOpenGLFunctions it is built on
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_cast_QAbstract3DGraph_QOpenGLFunctions(
    QAbstract3DGraph *self) {
  return static_cast<QOpenGLFunctions *>(self);
}

//  a Python function taken by a CuteQAbstract3DGraph, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DGraph(
    QAbstract3DGraph *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DGraph *>(self)->take(key, call);
}

//  bool QAbstract3DGraph::shadowsSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QAbstract3DGraph16shadowsSupportedEv(
    const QAbstract3DGraph *self) {
  return self->QAbstract3DGraph::shadowsSupported();
}

//  bool QAbstract3DGraph::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAbstract3DGraph5eventEP6QEvent(
    QAbstract3DGraph *self,
    QEvent *event) {
  return static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::event(
      event);
}

//  void QAbstract3DGraph::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph11resizeEventEP12QResizeEvent(
    QAbstract3DGraph *self,
    QResizeEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::resizeEvent(
      event);
}

//  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph11exposeEventEP12QExposeEvent(
    QAbstract3DGraph *self,
    QExposeEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::exposeEvent(
      event);
}

//  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph21mouseDoubleClickEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::mouseDoubleClickEvent(
      event);
}

//  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph10touchEventEP11QTouchEvent(
    QAbstract3DGraph *self,
    QTouchEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::touchEvent(
      event);
}

//  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph15mousePressEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::mousePressEvent(
      event);
}

//  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph17mouseReleaseEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::mouseReleaseEvent(
      event);
}

//  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph14mouseMoveEventEP11QMouseEvent(
    QAbstract3DGraph *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::mouseMoveEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QAbstract3DGraph::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstract3DGraph10wheelEventEP11QWheelEvent(
    QAbstract3DGraph *self,
    QWheelEvent *event) {
  static_cast<OwnQAbstract3DGraph *>(self)->OwnQAbstract3DGraph::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)
