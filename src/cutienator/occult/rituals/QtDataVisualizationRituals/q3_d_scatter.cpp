//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dscatter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/q3dscatter.h>
#include <QtCore/qstring.h>
#include <QtDataVisualization/qscatter3dseries.h>
#include <QtDataVisualization/qvalue3daxis.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Q3DScatter that Python can take functions over in. Every Q3DScatter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQ3DScatterCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall2)(const void *, QResizeEvent *, int *);
typedef void (*CuteQ3DScatterCall3)(const void *, QExposeEvent *, int *);
typedef void (*CuteQ3DScatterCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DScatterCall5)(const void *, QTouchEvent *, int *);
typedef void (*CuteQ3DScatterCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DScatterCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DScatterCall8)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQ3DScatterCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef int (*CuteQ3DScatterCall10)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQ3DScatterCall11)(const void *, int *);
typedef const QSize * (*CuteQ3DScatterCall12)(const void *, int *);
typedef void * (*CuteQ3DScatterCall13)(const void *, int *);
typedef void * (*CuteQ3DScatterCall14)(const void *, int *);
typedef void (*CuteQ3DScatterCall15)(const void *, QPaintEvent *, int *);
typedef void (*CuteQ3DScatterCall16)(const void *, QMoveEvent *, int *);
typedef void (*CuteQ3DScatterCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DScatterCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQ3DScatterCall19)(const void *, QShowEvent *, int *);
typedef void (*CuteQ3DScatterCall20)(const void *, QHideEvent *, int *);
typedef void (*CuteQ3DScatterCall21)(const void *, QCloseEvent *, int *);
typedef void (*CuteQ3DScatterCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQ3DScatterCall23)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQ3DScatterCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQ3DScatterCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DScatter : public Q3DScatter {
public:
  using Q3DScatter::Q3DScatter;
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
      CuteQ3DScatterCall0 call = reinterpret_cast<CuteQ3DScatterCall0>(taken[0]);
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
      CuteQ3DScatterCall1 call = reinterpret_cast<CuteQ3DScatterCall1>(taken[1]);
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
      CuteQ3DScatterCall2 call = reinterpret_cast<CuteQ3DScatterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::resizeEvent(event);
  }

  //  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
  void exposeEvent(QExposeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DScatterCall3 call = reinterpret_cast<CuteQ3DScatterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::exposeEvent(event);
  }

  //  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DScatterCall4 call = reinterpret_cast<CuteQ3DScatterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DScatterCall5 call = reinterpret_cast<CuteQ3DScatterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::touchEvent(event);
  }

  //  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DScatterCall6 call = reinterpret_cast<CuteQ3DScatterCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mousePressEvent(event);
  }

  //  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DScatterCall7 call = reinterpret_cast<CuteQ3DScatterCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DGraph::mouseReleaseEvent(event);
  }

  //  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DScatterCall8 call = reinterpret_cast<CuteQ3DScatterCall8>(taken[8]);
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
      CuteQ3DScatterCall9 call = reinterpret_cast<CuteQ3DScatterCall9>(taken[9]);
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
      CuteQ3DScatterCall10 call = reinterpret_cast<CuteQ3DScatterCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQ3DScatterCall11 call = reinterpret_cast<CuteQ3DScatterCall11>(taken[11]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQ3DScatterCall12 call = reinterpret_cast<CuteQ3DScatterCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQ3DScatterCall13 call = reinterpret_cast<CuteQ3DScatterCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQ3DScatterCall14 call = reinterpret_cast<CuteQ3DScatterCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQ3DScatterCall15 call = reinterpret_cast<CuteQ3DScatterCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQ3DScatterCall16 call = reinterpret_cast<CuteQ3DScatterCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQ3DScatterCall17 call = reinterpret_cast<CuteQ3DScatterCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQ3DScatterCall18 call = reinterpret_cast<CuteQ3DScatterCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQ3DScatterCall19 call = reinterpret_cast<CuteQ3DScatterCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQ3DScatterCall20 call = reinterpret_cast<CuteQ3DScatterCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQ3DScatterCall21 call = reinterpret_cast<CuteQ3DScatterCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQ3DScatterCall22 call = reinterpret_cast<CuteQ3DScatterCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQ3DScatterCall23 call = reinterpret_cast<CuteQ3DScatterCall23>(taken[23]);
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
      CuteQ3DScatterCall24 call = reinterpret_cast<CuteQ3DScatterCall24>(taken[24]);
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
      CuteQ3DScatterCall25 call = reinterpret_cast<CuteQ3DScatterCall25>(taken[25]);
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
      CuteQ3DScatterCall26 call = reinterpret_cast<CuteQ3DScatterCall26>(taken[26]);
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
      CuteQ3DScatterCall27 call = reinterpret_cast<CuteQ3DScatterCall27>(taken[27]);
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
      CuteQ3DScatterCall28 call = reinterpret_cast<CuteQ3DScatterCall28>(taken[28]);
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
      CuteQ3DScatterCall29 call = reinterpret_cast<CuteQ3DScatterCall29>(taken[29]);
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
      CuteQ3DScatterCall30 call = reinterpret_cast<CuteQ3DScatterCall30>(taken[30]);
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
      CuteQ3DScatterCall31 call = reinterpret_cast<CuteQ3DScatterCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DScatter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Q3DScatter10metaObjectEv(
    const Q3DScatter *self) {
  return self->metaObject();
}

//  QString Q3DScatter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Q3DScatter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DScatter::tr(s, c, n));
}

//  Q3DScatter::Q3DScatter(const QSurfaceFormat *format, QWindow *parent)
extern "C" Q_DECL_EXPORT
Q3DScatter *ritual_ZN10Q3DScatterC1EPK14QSurfaceFormatP7QWindow(
    const QSurfaceFormat *format,
    QWindow *parent) {
  return new CuteQ3DScatter(format, parent);
}

//  Q3DScatter::~Q3DScatter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatterD1Ev(Q3DScatter *self) {
  delete self;
}

//  void Q3DScatter::addSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter9addSeriesEP16QScatter3DSeries(
    Q3DScatter *self,
    QScatter3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DScatter::removeSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter12removeSeriesEP16QScatter3DSeries(
    Q3DScatter *self,
    QScatter3DSeries *series) {
  self->removeSeries(series);
}

//  QList<QScatter3DSeries *> Q3DScatter::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QScatter3DSeries *> *ritual_ZNK10Q3DScatter10seriesListEv(
    const Q3DScatter *self) {
  return new QList<QScatter3DSeries *>(self->seriesList());
}

//  void Q3DScatter::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter8setAxisXEP12QValue3DAxis(
    Q3DScatter *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *Q3DScatter::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DScatter5axisXEv(const Q3DScatter *self) {
  return self->axisX();
}

//  void Q3DScatter::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter8setAxisYEP12QValue3DAxis(
    Q3DScatter *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *Q3DScatter::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DScatter5axisYEv(const Q3DScatter *self) {
  return self->axisY();
}

//  void Q3DScatter::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter8setAxisZEP12QValue3DAxis(
    Q3DScatter *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QValue3DAxis *Q3DScatter::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK10Q3DScatter5axisZEv(const Q3DScatter *self) {
  return self->axisZ();
}

//  void Q3DScatter::addAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter7addAxisEP12QValue3DAxis(
    Q3DScatter *self,
    QValue3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DScatter::releaseAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Q3DScatter11releaseAxisEP12QValue3DAxis(
    Q3DScatter *self,
    QValue3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QValue3DAxis *> Q3DScatter::axes() const
extern "C" Q_DECL_EXPORT
QList<QValue3DAxis *> *ritual_ZNK10Q3DScatter4axesEv(
    const Q3DScatter *self) {
  return new QList<QValue3DAxis *>(self->axes());
}

//  QScatter3DSeries *Q3DScatter::selectedSeries() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK10Q3DScatter14selectedSeriesEv(
    const Q3DScatter *self) {
  return self->selectedSeries();
}

//  Q3DScatterPrivate *Q3DScatter::dptr()
extern "C" Q_DECL_EXPORT
Q3DScatterPrivate *ritual_ZN10Q3DScatter4dptrEv(Q3DScatter *self) {
  return self->dptr();
}

//  const Q3DScatterPrivate *Q3DScatter::dptrc() const
extern "C" Q_DECL_EXPORT
const Q3DScatterPrivate *ritual_ZNK10Q3DScatter5dptrcEv(
    const Q3DScatter *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQ3DScatter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScatter(Q3DScatter *self, const char *key, void *call) {
  return static_cast<CuteQ3DScatter *>(self)->take(key, call);
}
