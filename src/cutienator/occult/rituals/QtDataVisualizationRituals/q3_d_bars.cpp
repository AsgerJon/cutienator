//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dbars.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/q3dbars.h>
#include <QtCore/qstring.h>
#include <QtDataVisualization/qbar3dseries.h>
#include <QtCore/qsize.h>
#include <QtDataVisualization/qabstract3daxis.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Q3DBars that Python can take functions over in. Every Q3DBars
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQ3DBarsCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall2)(const void *, QResizeEvent *, int *);
typedef void (*CuteQ3DBarsCall3)(const void *, QExposeEvent *, int *);
typedef void (*CuteQ3DBarsCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DBarsCall5)(const void *, QTouchEvent *, int *);
typedef void (*CuteQ3DBarsCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DBarsCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DBarsCall8)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQ3DBarsCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef int (*CuteQ3DBarsCall10)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQ3DBarsCall11)(const void *, int *);
typedef const QSize * (*CuteQ3DBarsCall12)(const void *, int *);
typedef void * (*CuteQ3DBarsCall13)(const void *, int *);
typedef void * (*CuteQ3DBarsCall14)(const void *, int *);
typedef void (*CuteQ3DBarsCall15)(const void *, QPaintEvent *, int *);
typedef void (*CuteQ3DBarsCall16)(const void *, QMoveEvent *, int *);
typedef void (*CuteQ3DBarsCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DBarsCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DBarsCall19)(const void *, QShowEvent *, int *);
typedef void (*CuteQ3DBarsCall20)(const void *, QHideEvent *, int *);
typedef void (*CuteQ3DBarsCall21)(const void *, QCloseEvent *, int *);
typedef void (*CuteQ3DBarsCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQ3DBarsCall23)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQ3DBarsCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQ3DBarsCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DBars : public Q3DBars {
public:
  using Q3DBars::Q3DBars;
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
      CuteQ3DBarsCall0 call = reinterpret_cast<CuteQ3DBarsCall0>(taken[0]);
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
      CuteQ3DBarsCall1 call = reinterpret_cast<CuteQ3DBarsCall1>(taken[1]);
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
      CuteQ3DBarsCall2 call = reinterpret_cast<CuteQ3DBarsCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::resizeEvent(event);
  }

  //  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
  void exposeEvent(QExposeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DBarsCall3 call = reinterpret_cast<CuteQ3DBarsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::exposeEvent(event);
  }

  //  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DBarsCall4 call = reinterpret_cast<CuteQ3DBarsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DBarsCall5 call = reinterpret_cast<CuteQ3DBarsCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::touchEvent(event);
  }

  //  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DBarsCall6 call = reinterpret_cast<CuteQ3DBarsCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mousePressEvent(event);
  }

  //  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DBarsCall7 call = reinterpret_cast<CuteQ3DBarsCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseReleaseEvent(event);
  }

  //  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DBarsCall8 call = reinterpret_cast<CuteQ3DBarsCall8>(taken[8]);
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
      CuteQ3DBarsCall9 call = reinterpret_cast<CuteQ3DBarsCall9>(taken[9]);
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
      CuteQ3DBarsCall10 call = reinterpret_cast<CuteQ3DBarsCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQ3DBarsCall11 call = reinterpret_cast<CuteQ3DBarsCall11>(taken[11]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQ3DBarsCall12 call = reinterpret_cast<CuteQ3DBarsCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQ3DBarsCall13 call = reinterpret_cast<CuteQ3DBarsCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQ3DBarsCall14 call = reinterpret_cast<CuteQ3DBarsCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQ3DBarsCall15 call = reinterpret_cast<CuteQ3DBarsCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQ3DBarsCall16 call = reinterpret_cast<CuteQ3DBarsCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQ3DBarsCall17 call = reinterpret_cast<CuteQ3DBarsCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQ3DBarsCall18 call = reinterpret_cast<CuteQ3DBarsCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQ3DBarsCall19 call = reinterpret_cast<CuteQ3DBarsCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQ3DBarsCall20 call = reinterpret_cast<CuteQ3DBarsCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQ3DBarsCall21 call = reinterpret_cast<CuteQ3DBarsCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQ3DBarsCall22 call = reinterpret_cast<CuteQ3DBarsCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQ3DBarsCall23 call = reinterpret_cast<CuteQ3DBarsCall23>(taken[23]);
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
      CuteQ3DBarsCall24 call = reinterpret_cast<CuteQ3DBarsCall24>(taken[24]);
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
      CuteQ3DBarsCall25 call = reinterpret_cast<CuteQ3DBarsCall25>(taken[25]);
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
      CuteQ3DBarsCall26 call = reinterpret_cast<CuteQ3DBarsCall26>(taken[26]);
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
      CuteQ3DBarsCall27 call = reinterpret_cast<CuteQ3DBarsCall27>(taken[27]);
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
      CuteQ3DBarsCall28 call = reinterpret_cast<CuteQ3DBarsCall28>(taken[28]);
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
      CuteQ3DBarsCall29 call = reinterpret_cast<CuteQ3DBarsCall29>(taken[29]);
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
      CuteQ3DBarsCall30 call = reinterpret_cast<CuteQ3DBarsCall30>(taken[30]);
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
      CuteQ3DBarsCall31 call = reinterpret_cast<CuteQ3DBarsCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DBars::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7Q3DBars10metaObjectEv(const Q3DBars *self) {
  return self->metaObject();
}

//  void *Q3DBars::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7Q3DBars11qt_metacastEPKc(Q3DBars *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DBars::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7Q3DBars11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DBars *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DBars::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7Q3DBars2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Q3DBars::tr(s, c, n));
}

//  Q3DBars::Q3DBars(const QSurfaceFormat *format, QWindow *parent)
extern "C" Q_DECL_EXPORT
Q3DBars *ritual_ZN7Q3DBarsC1EPK14QSurfaceFormatP7QWindow(
    const QSurfaceFormat *format,
    QWindow *parent) {
  return new CuteQ3DBars(format, parent);
}

//  Q3DBars::~Q3DBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBarsD1Ev(Q3DBars *self) {
  delete self;
}

//  void Q3DBars::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars16setPrimarySeriesEP12QBar3DSeries(
    Q3DBars *self,
    QBar3DSeries *series) {
  self->setPrimarySeries(series);
}

//  QBar3DSeries *Q3DBars::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK7Q3DBars13primarySeriesEv(const Q3DBars *self) {
  return self->primarySeries();
}

//  void Q3DBars::addSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars9addSeriesEP12QBar3DSeries(
    Q3DBars *self,
    QBar3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DBars::removeSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars12removeSeriesEP12QBar3DSeries(
    Q3DBars *self,
    QBar3DSeries *series) {
  self->removeSeries(series);
}

//  void Q3DBars::insertSeries(int index, QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars12insertSeriesEiP12QBar3DSeries(
    Q3DBars *self,
    int index,
    QBar3DSeries *series) {
  self->insertSeries(index, series);
}

//  QList<QBar3DSeries *> Q3DBars::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_ZNK7Q3DBars10seriesListEv(
    const Q3DBars *self) {
  return new QList<QBar3DSeries *>(self->seriesList());
}

//  void Q3DBars::setMultiSeriesUniform(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars21setMultiSeriesUniformEb(
    Q3DBars *self,
    bool uniform) {
  self->setMultiSeriesUniform(uniform);
}

//  bool Q3DBars::isMultiSeriesUniform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7Q3DBars20isMultiSeriesUniformEv(const Q3DBars *self) {
  return self->isMultiSeriesUniform();
}

//  void Q3DBars::setBarThickness(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars15setBarThicknessEf(
    Q3DBars *self,
    float thicknessRatio) {
  self->setBarThickness(thicknessRatio);
}

//  float Q3DBars::barThickness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7Q3DBars12barThicknessEv(const Q3DBars *self) {
  return self->barThickness();
}

//  void Q3DBars::setBarSpacing(const QSizeF &spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars13setBarSpacingERK6QSizeF(
    Q3DBars *self,
    const QSizeF *spacing) {
  self->setBarSpacing(*spacing);
}

//  QSizeF Q3DBars::barSpacing() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK7Q3DBars10barSpacingEv(const Q3DBars *self) {
  return new QSizeF(self->barSpacing());
}

//  void Q3DBars::setBarSpacingRelative(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars21setBarSpacingRelativeEb(
    Q3DBars *self,
    bool relative) {
  self->setBarSpacingRelative(relative);
}

//  bool Q3DBars::isBarSpacingRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7Q3DBars20isBarSpacingRelativeEv(const Q3DBars *self) {
  return self->isBarSpacingRelative();
}

//  void Q3DBars::setBarSeriesMargin(const QSizeF &margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars18setBarSeriesMarginERK6QSizeF(
    Q3DBars *self,
    const QSizeF *margin) {
  self->setBarSeriesMargin(*margin);
}

//  QSizeF Q3DBars::barSeriesMargin() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK7Q3DBars15barSeriesMarginEv(const Q3DBars *self) {
  return new QSizeF(self->barSeriesMargin());
}

//  void Q3DBars::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars10setRowAxisEP15QCategory3DAxis(
    Q3DBars *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  QCategory3DAxis *Q3DBars::rowAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK7Q3DBars7rowAxisEv(const Q3DBars *self) {
  return self->rowAxis();
}

//  void Q3DBars::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars13setColumnAxisEP15QCategory3DAxis(
    Q3DBars *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  QCategory3DAxis *Q3DBars::columnAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK7Q3DBars10columnAxisEv(const Q3DBars *self) {
  return self->columnAxis();
}

//  void Q3DBars::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars12setValueAxisEP12QValue3DAxis(
    Q3DBars *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  QValue3DAxis *Q3DBars::valueAxis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK7Q3DBars9valueAxisEv(const Q3DBars *self) {
  return self->valueAxis();
}

//  void Q3DBars::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars7addAxisEP15QAbstract3DAxis(
    Q3DBars *self,
    QAbstract3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DBars::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars11releaseAxisEP15QAbstract3DAxis(
    Q3DBars *self,
    QAbstract3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QAbstract3DAxis *> Q3DBars::axes() const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DAxis *> *ritual_ZNK7Q3DBars4axesEv(const Q3DBars *self) {
  return new QList<QAbstract3DAxis *>(self->axes());
}

//  QBar3DSeries *Q3DBars::selectedSeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK7Q3DBars14selectedSeriesEv(const Q3DBars *self) {
  return self->selectedSeries();
}

//  void Q3DBars::setFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars13setFloorLevelEf(Q3DBars *self, float level) {
  self->setFloorLevel(level);
}

//  float Q3DBars::floorLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7Q3DBars10floorLevelEv(const Q3DBars *self) {
  return self->floorLevel();
}

//  void Q3DBars::multiSeriesUniformChanged(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars25multiSeriesUniformChangedEb(
    Q3DBars *self,
    bool uniform) {
  self->multiSeriesUniformChanged(uniform);
}

//  void Q3DBars::barThicknessChanged(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars19barThicknessChangedEf(
    Q3DBars *self,
    float thicknessRatio) {
  self->barThicknessChanged(thicknessRatio);
}

//  void Q3DBars::barSpacingChanged(const QSizeF &spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars17barSpacingChangedERK6QSizeF(
    Q3DBars *self,
    const QSizeF *spacing) {
  self->barSpacingChanged(*spacing);
}

//  void Q3DBars::barSpacingRelativeChanged(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars25barSpacingRelativeChangedEb(
    Q3DBars *self,
    bool relative) {
  self->barSpacingRelativeChanged(relative);
}

//  void Q3DBars::barSeriesMarginChanged(const QSizeF &margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars22barSeriesMarginChangedERK6QSizeF(
    Q3DBars *self,
    const QSizeF *margin) {
  self->barSeriesMarginChanged(*margin);
}

//  void Q3DBars::rowAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars14rowAxisChangedEP15QCategory3DAxis(
    Q3DBars *self,
    QCategory3DAxis *axis) {
  self->rowAxisChanged(axis);
}

//  void Q3DBars::columnAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars17columnAxisChangedEP15QCategory3DAxis(
    Q3DBars *self,
    QCategory3DAxis *axis) {
  self->columnAxisChanged(axis);
}

//  void Q3DBars::valueAxisChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars16valueAxisChangedEP12QValue3DAxis(
    Q3DBars *self,
    QValue3DAxis *axis) {
  self->valueAxisChanged(axis);
}

//  void Q3DBars::primarySeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars20primarySeriesChangedEP12QBar3DSeries(
    Q3DBars *self,
    QBar3DSeries *series) {
  self->primarySeriesChanged(series);
}

//  void Q3DBars::selectedSeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars21selectedSeriesChangedEP12QBar3DSeries(
    Q3DBars *self,
    QBar3DSeries *series) {
  self->selectedSeriesChanged(series);
}

//  void Q3DBars::floorLevelChanged(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN7Q3DBars17floorLevelChangedEf(Q3DBars *self, float level) {
  self->floorLevelChanged(level);
}

//  Q3DBarsPrivate *Q3DBars::dptr()
extern "C" Q_DECL_EXPORT
Q3DBarsPrivate *ritual_ZN7Q3DBars4dptrEv(Q3DBars *self) {
  return self->dptr();
}

//  const Q3DBarsPrivate *Q3DBars::dptrc() const
extern "C" Q_DECL_EXPORT
const Q3DBarsPrivate *ritual_ZNK7Q3DBars5dptrcEv(const Q3DBars *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQ3DBars, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DBars(Q3DBars *self, const char *key, void *call) {
  return static_cast<CuteQ3DBars *>(self)->take(key, call);
}
