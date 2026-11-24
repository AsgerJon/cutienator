//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dsurface.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/q3dsurface.h>
#include <QtCore/qstring.h>
#include <QtDataVisualization/qsurface3dseries.h>
#include <QtDataVisualization/qvalue3daxis.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Q3DSurface that Python can take functions over in. Every Q3DSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQ3DSurfaceCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSurfaceCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall2)(const void *, QResizeEvent *, int *);
typedef void (*CuteQ3DSurfaceCall3)(const void *, QExposeEvent *, int *);
typedef void (*CuteQ3DSurfaceCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DSurfaceCall5)(const void *, QTouchEvent *, int *);
typedef void (*CuteQ3DSurfaceCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DSurfaceCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DSurfaceCall8)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQ3DSurfaceCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef int (*CuteQ3DSurfaceCall10)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQ3DSurfaceCall11)(const void *, int *);
typedef const QSize * (*CuteQ3DSurfaceCall12)(const void *, int *);
typedef void * (*CuteQ3DSurfaceCall13)(const void *, int *);
typedef void * (*CuteQ3DSurfaceCall14)(const void *, int *);
typedef void (*CuteQ3DSurfaceCall15)(const void *, QPaintEvent *, int *);
typedef void (*CuteQ3DSurfaceCall16)(const void *, QMoveEvent *, int *);
typedef void (*CuteQ3DSurfaceCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DSurfaceCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DSurfaceCall19)(const void *, QShowEvent *, int *);
typedef void (*CuteQ3DSurfaceCall20)(const void *, QHideEvent *, int *);
typedef void (*CuteQ3DSurfaceCall21)(const void *, QCloseEvent *, int *);
typedef void (*CuteQ3DSurfaceCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQ3DSurfaceCall23)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQ3DSurfaceCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQ3DSurfaceCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSurfaceCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DSurface : public Q3DSurface {
public:
  using Q3DSurface::Q3DSurface;
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
      CuteQ3DSurfaceCall0 call = reinterpret_cast<CuteQ3DSurfaceCall0>(taken[0]);
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
      CuteQ3DSurfaceCall1 call = reinterpret_cast<CuteQ3DSurfaceCall1>(taken[1]);
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
      CuteQ3DSurfaceCall2 call = reinterpret_cast<CuteQ3DSurfaceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::resizeEvent(event);
  }

  //  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
  void exposeEvent(QExposeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DSurfaceCall3 call = reinterpret_cast<CuteQ3DSurfaceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::exposeEvent(event);
  }

  //  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DSurfaceCall4 call = reinterpret_cast<CuteQ3DSurfaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DSurfaceCall5 call = reinterpret_cast<CuteQ3DSurfaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::touchEvent(event);
  }

  //  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DSurfaceCall6 call = reinterpret_cast<CuteQ3DSurfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mousePressEvent(event);
  }

  //  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DSurfaceCall7 call = reinterpret_cast<CuteQ3DSurfaceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseReleaseEvent(event);
  }

  //  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DSurfaceCall8 call = reinterpret_cast<CuteQ3DSurfaceCall8>(taken[8]);
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
      CuteQ3DSurfaceCall9 call = reinterpret_cast<CuteQ3DSurfaceCall9>(taken[9]);
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
      CuteQ3DSurfaceCall10 call = reinterpret_cast<CuteQ3DSurfaceCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQ3DSurfaceCall11 call = reinterpret_cast<CuteQ3DSurfaceCall11>(taken[11]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQ3DSurfaceCall12 call = reinterpret_cast<CuteQ3DSurfaceCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQ3DSurfaceCall13 call = reinterpret_cast<CuteQ3DSurfaceCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQ3DSurfaceCall14 call = reinterpret_cast<CuteQ3DSurfaceCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQ3DSurfaceCall15 call = reinterpret_cast<CuteQ3DSurfaceCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQ3DSurfaceCall16 call = reinterpret_cast<CuteQ3DSurfaceCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQ3DSurfaceCall17 call = reinterpret_cast<CuteQ3DSurfaceCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQ3DSurfaceCall18 call = reinterpret_cast<CuteQ3DSurfaceCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQ3DSurfaceCall19 call = reinterpret_cast<CuteQ3DSurfaceCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQ3DSurfaceCall20 call = reinterpret_cast<CuteQ3DSurfaceCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQ3DSurfaceCall21 call = reinterpret_cast<CuteQ3DSurfaceCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQ3DSurfaceCall22 call = reinterpret_cast<CuteQ3DSurfaceCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQ3DSurfaceCall23 call = reinterpret_cast<CuteQ3DSurfaceCall23>(taken[23]);
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
      CuteQ3DSurfaceCall24 call = reinterpret_cast<CuteQ3DSurfaceCall24>(taken[24]);
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
      CuteQ3DSurfaceCall25 call = reinterpret_cast<CuteQ3DSurfaceCall25>(taken[25]);
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
      CuteQ3DSurfaceCall26 call = reinterpret_cast<CuteQ3DSurfaceCall26>(taken[26]);
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
      CuteQ3DSurfaceCall27 call = reinterpret_cast<CuteQ3DSurfaceCall27>(taken[27]);
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
      CuteQ3DSurfaceCall28 call = reinterpret_cast<CuteQ3DSurfaceCall28>(taken[28]);
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
      CuteQ3DSurfaceCall29 call = reinterpret_cast<CuteQ3DSurfaceCall29>(taken[29]);
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
      CuteQ3DSurfaceCall30 call = reinterpret_cast<CuteQ3DSurfaceCall30>(taken[30]);
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
      CuteQ3DSurfaceCall31 call = reinterpret_cast<CuteQ3DSurfaceCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Q3DSurface10metaObjectEv(
    const Q3DSurface *self) {
  return self->metaObject();
}

//  QString Q3DSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Q3DSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DSurface::tr(s, c, n));
}

//  Q3DSurface::Q3DSurface(const QSurfaceFormat *format, QWindow *parent)
extern "C" Q_DECL_EXPORT
Q3DSurface *ritual_ZN10Q3DSurfaceC1EPK14QSurfaceFormatP7QWindow(
    const QSurfaceFormat *format,
    QWindow *parent) {
  return new CuteQ3DSurface(format, parent);
}

//  Q3DSurface::~Q3DSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurfaceD1Ev(Q3DSurface *self) {
  delete self;
}

//  void Q3DSurface::addSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface9addSeriesEP16QSurface3DSeries(
    Q3DSurface *self,
    QSurface3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DSurface::removeSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface12removeSeriesEP16QSurface3DSeries(
    Q3DSurface *self,
    QSurface3DSeries *series) {
  self->removeSeries(series);
}

//  QList<QSurface3DSeries *> Q3DSurface::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QSurface3DSeries *> *ritual_ZNK10Q3DSurface10seriesListEv(
    const Q3DSurface *self) {
  return new QList<QSurface3DSeries *>(self->seriesList());
}

//  void Q3DSurface::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface8setAxisXEP12QValue3DAxis(
    Q3DSurface *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *Q3DSurface::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DSurface5axisXEv(const Q3DSurface *self) {
  return self->axisX();
}

//  void Q3DSurface::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface8setAxisYEP12QValue3DAxis(
    Q3DSurface *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *Q3DSurface::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DSurface5axisYEv(const Q3DSurface *self) {
  return self->axisY();
}

//  void Q3DSurface::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface8setAxisZEP12QValue3DAxis(
    Q3DSurface *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QValue3DAxis *Q3DSurface::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DSurface5axisZEv(const Q3DSurface *self) {
  return self->axisZ();
}

//  void Q3DSurface::addAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface7addAxisEP12QValue3DAxis(
    Q3DSurface *self,
    QValue3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DSurface::releaseAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface11releaseAxisEP12QValue3DAxis(
    Q3DSurface *self,
    QValue3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QValue3DAxis *> Q3DSurface::axes() const
extern "C" Q_DECL_EXPORT
QList<QValue3DAxis *> *ritual_ZNK10Q3DSurface4axesEv(
    const Q3DSurface *self) {
  return new QList<QValue3DAxis *>(self->axes());
}

//  QSurface3DSeries *Q3DSurface::selectedSeries() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK10Q3DSurface14selectedSeriesEv(
    const Q3DSurface *self) {
  return self->selectedSeries();
}

//  void Q3DSurface::setFlipHorizontalGrid(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DSurface21setFlipHorizontalGridEb(
    Q3DSurface *self,
    bool flip) {
  self->setFlipHorizontalGrid(flip);
}

//  bool Q3DSurface::flipHorizontalGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Q3DSurface18flipHorizontalGridEv(const Q3DSurface *self) {
  return self->flipHorizontalGrid();
}

//  Q3DSurfacePrivate *Q3DSurface::dptr()
extern "C" Q_DECL_EXPORT
Q3DSurfacePrivate *ritual_ZN10Q3DSurface4dptrEv(Q3DSurface *self) {
  return self->dptr();
}

//  const Q3DSurfacePrivate *Q3DSurface::dptrc() const
extern "C" Q_DECL_EXPORT
const Q3DSurfacePrivate *ritual_ZNK10Q3DSurface5dptrcEv(
    const Q3DSurface *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQ3DSurface, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DSurface(Q3DSurface *self, const char *key, void *call) {
  return static_cast<CuteQ3DSurface *>(self)->take(key, call);
}
