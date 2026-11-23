//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qrasterwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qrasterwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRasterWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRasterWindow : QRasterWindow {
  using QRasterWindow::metric;
  using QRasterWindow::redirected;
  using QRasterWindow::resizeEvent;
};

//  A QRasterWindow that Python can take functions over in. Every QRasterWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRasterWindowCall0)(const void *, int, int *);
typedef void * (*CuteQRasterWindowCall1)(const void *, QPoint *, int *);
typedef void (*CuteQRasterWindowCall2)(const void *, QResizeEvent *, int *);
typedef void (*CuteQRasterWindowCall3)(const void *, QExposeEvent *, int *);
typedef void (*CuteQRasterWindowCall4)(const void *, QPaintEvent *, int *);
typedef bool (*CuteQRasterWindowCall5)(const void *, QEvent *, int *);
typedef void * (*CuteQRasterWindowCall6)(const void *, int *);
typedef int (*CuteQRasterWindowCall7)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQRasterWindowCall8)(const void *, int *);
typedef const QSize * (*CuteQRasterWindowCall9)(const void *, int *);
typedef void * (*CuteQRasterWindowCall10)(const void *, int *);
typedef void * (*CuteQRasterWindowCall11)(const void *, int *);
typedef void (*CuteQRasterWindowCall12)(const void *, QMoveEvent *, int *);
typedef void (*CuteQRasterWindowCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRasterWindowCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRasterWindowCall15)(const void *, QShowEvent *, int *);
typedef void (*CuteQRasterWindowCall16)(const void *, QHideEvent *, int *);
typedef void (*CuteQRasterWindowCall17)(const void *, QCloseEvent *, int *);
typedef void (*CuteQRasterWindowCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRasterWindowCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRasterWindowCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRasterWindowCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRasterWindowCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRasterWindowCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRasterWindowCall24)(const void *, QWheelEvent *, int *);
typedef void (*CuteQRasterWindowCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQRasterWindowCall26)(const void *, QTabletEvent *, int *);
typedef int (*CuteQRasterWindowCall27)(const void *, int *);
typedef void (*CuteQRasterWindowCall28)(const void *, QPainter *, int *);
typedef void * (*CuteQRasterWindowCall29)(const void *, int *);
typedef bool (*CuteQRasterWindowCall30)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQRasterWindowCall31)(const void *, QTimerEvent *, int *);
typedef void (*CuteQRasterWindowCall32)(const void *, QChildEvent *, int *);
typedef void (*CuteQRasterWindowCall33)(const void *, QEvent *, int *);
typedef void (*CuteQRasterWindowCall34)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQRasterWindowCall35)(const void *, const QMetaMethod *, int *);
class CuteQRasterWindow : public QRasterWindow {
public:
  using QRasterWindow::QRasterWindow;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[35] = call;
      return true;
    }
    return false;
  }

  //  int QRasterWindow::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRasterWindowCall0 call = reinterpret_cast<CuteQRasterWindowCall0>(taken[0]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QRasterWindow::metric(metric);
  }

  //  QPaintDevice *QRasterWindow::redirected(QPoint *a0) const
  QPaintDevice *redirected(QPoint *a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRasterWindowCall1 call = reinterpret_cast<CuteQRasterWindowCall1>(taken[1]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QRasterWindow::redirected(a0);
  }

  //  void QRasterWindow::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRasterWindowCall2 call = reinterpret_cast<CuteQRasterWindowCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QRasterWindow::resizeEvent(event);
  }

  //  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRasterWindowCall3 call = reinterpret_cast<CuteQRasterWindowCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPaintDeviceWindow::exposeEvent(a0);
  }

  //  void QPaintDeviceWindow::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRasterWindowCall4 call = reinterpret_cast<CuteQRasterWindowCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPaintDeviceWindow::paintEvent(event);
  }

  //  bool QPaintDeviceWindow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRasterWindowCall5 call = reinterpret_cast<CuteQRasterWindowCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPaintDeviceWindow::event(event);
  }

  //  QPaintEngine *QPaintDeviceWindow::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRasterWindowCall6 call = reinterpret_cast<CuteQRasterWindowCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintDeviceWindow::paintEngine();
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQRasterWindowCall7 call = reinterpret_cast<CuteQRasterWindowCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRasterWindowCall8 call = reinterpret_cast<CuteQRasterWindowCall8>(taken[8]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRasterWindowCall9 call = reinterpret_cast<CuteQRasterWindowCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQRasterWindowCall10 call = reinterpret_cast<CuteQRasterWindowCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRasterWindowCall11 call = reinterpret_cast<CuteQRasterWindowCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRasterWindowCall12 call = reinterpret_cast<CuteQRasterWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRasterWindowCall13 call = reinterpret_cast<CuteQRasterWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRasterWindowCall14 call = reinterpret_cast<CuteQRasterWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRasterWindowCall15 call = reinterpret_cast<CuteQRasterWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRasterWindowCall16 call = reinterpret_cast<CuteQRasterWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRasterWindowCall17 call = reinterpret_cast<CuteQRasterWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRasterWindowCall18 call = reinterpret_cast<CuteQRasterWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRasterWindowCall19 call = reinterpret_cast<CuteQRasterWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRasterWindowCall20 call = reinterpret_cast<CuteQRasterWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRasterWindowCall21 call = reinterpret_cast<CuteQRasterWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRasterWindowCall22 call = reinterpret_cast<CuteQRasterWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRasterWindowCall23 call = reinterpret_cast<CuteQRasterWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRasterWindowCall24 call = reinterpret_cast<CuteQRasterWindowCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRasterWindowCall25 call = reinterpret_cast<CuteQRasterWindowCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRasterWindowCall26 call = reinterpret_cast<CuteQRasterWindowCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQRasterWindowCall27 call = reinterpret_cast<CuteQRasterWindowCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQRasterWindowCall28 call = reinterpret_cast<CuteQRasterWindowCall28>(taken[28]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQRasterWindowCall29 call = reinterpret_cast<CuteQRasterWindowCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRasterWindowCall30 call = reinterpret_cast<CuteQRasterWindowCall30>(taken[30]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRasterWindowCall31 call = reinterpret_cast<CuteQRasterWindowCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRasterWindowCall32 call = reinterpret_cast<CuteQRasterWindowCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRasterWindowCall33 call = reinterpret_cast<CuteQRasterWindowCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRasterWindowCall34 call = reinterpret_cast<CuteQRasterWindowCall34>(taken[34]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRasterWindowCall35 call = reinterpret_cast<CuteQRasterWindowCall35>(taken[35]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QRasterWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QRasterWindow10metaObjectEv(
    const QRasterWindow *self) {
  return self->metaObject();
}

//  QString QRasterWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QRasterWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRasterWindow::tr(s, c, n));
}

//  QRasterWindow::QRasterWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QRasterWindow *ritual_ZN13QRasterWindowC1EP7QWindow(QWindow *parent) {
  return new CuteQRasterWindow(parent);
}

//  QRasterWindow::~QRasterWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRasterWindowD1Ev(QRasterWindow *self) {
  delete self;
}

//  int QRasterWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRasterWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QRasterWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  QPaintDevice *QRasterWindow::redirected(QPoint *a0) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK13QRasterWindow10redirectedEP6QPoint(
    const QRasterWindow *self,
    QPoint *a0) {
  return self->redirected(a0);
}

//  void QRasterWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRasterWindow11resizeEventEP12QResizeEvent(
    QRasterWindow *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  a Python function taken by a CuteQRasterWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRasterWindow(
    QRasterWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRasterWindow *>(self)->take(key, call);
}

//  int QRasterWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QRasterWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QRasterWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQRasterWindow *>(self)->OwnQRasterWindow::metric(
      metric);
}

//  QPaintDevice *QRasterWindow::redirected(QPoint *a0) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZNK13QRasterWindow10redirectedEP6QPoint(
    const QRasterWindow *self,
    QPoint *a0) {
  return static_cast<const OwnQRasterWindow *>(self)->OwnQRasterWindow::redirected(
      a0);
}

//  void QRasterWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QRasterWindow11resizeEventEP12QResizeEvent(
    QRasterWindow *self,
    QResizeEvent *event) {
  static_cast<OwnQRasterWindow *>(self)->OwnQRasterWindow::resizeEvent(
      event);
}
