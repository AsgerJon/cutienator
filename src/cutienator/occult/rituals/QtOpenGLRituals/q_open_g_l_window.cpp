//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QOpenGLWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOpenGLWindow : QOpenGLWindow {
  using QOpenGLWindow::initializeGL;
  using QOpenGLWindow::resizeGL;
  using QOpenGLWindow::paintGL;
  using QOpenGLWindow::paintUnderGL;
  using QOpenGLWindow::paintOverGL;
  using QOpenGLWindow::paintEvent;
  using QOpenGLWindow::resizeEvent;
  using QOpenGLWindow::metric;
  using QOpenGLWindow::redirected;
};

//  A QOpenGLWindow that Python can take functions over in. Every QOpenGLWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall1)(const void *, int, int, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall2)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall3)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall4)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall5)(const void *, QPaintEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall6)(const void *, QResizeEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef int (*CuteQOpenGLWindowCall7)(const void *, int, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void * (*CuteQOpenGLWindowCall8)(const void *, QPoint *, int *);
#endif  // !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLWindowCall9)(const void *, QExposeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLWindowCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQOpenGLWindowCall11)(const void *, int *);
typedef int (*CuteQOpenGLWindowCall12)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQOpenGLWindowCall13)(const void *, int *);
typedef const QSize * (*CuteQOpenGLWindowCall14)(const void *, int *);
typedef void * (*CuteQOpenGLWindowCall15)(const void *, int *);
typedef void * (*CuteQOpenGLWindowCall16)(const void *, int *);
typedef void (*CuteQOpenGLWindowCall17)(const void *, QMoveEvent *, int *);
typedef void (*CuteQOpenGLWindowCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQOpenGLWindowCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQOpenGLWindowCall20)(const void *, QShowEvent *, int *);
typedef void (*CuteQOpenGLWindowCall21)(const void *, QHideEvent *, int *);
typedef void (*CuteQOpenGLWindowCall22)(const void *, QCloseEvent *, int *);
typedef void (*CuteQOpenGLWindowCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQOpenGLWindowCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQOpenGLWindowCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWindowCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWindowCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWindowCall28)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQOpenGLWindowCall29)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQOpenGLWindowCall30)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQOpenGLWindowCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQOpenGLWindowCall32)(const void *, int *);
typedef int (*CuteQOpenGLWindowCall33)(const void *, int *);
typedef void (*CuteQOpenGLWindowCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQOpenGLWindowCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLWindowCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWindowCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWindowCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWindowCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWindowCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWindowCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLWindow : public QOpenGLWindow {
public:
  using QOpenGLWindow::QOpenGLWindow;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWindow12initializeGLEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWindow8resizeGLEii")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWindow7paintGLEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWindow12paintUnderGLEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWindow11paintOverGLEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::initializeGL()
  void initializeGL() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLWindowCall0 call = reinterpret_cast<CuteQOpenGLWindowCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWindow::initializeGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::resizeGL(int w, int h)
  void resizeGL(int w, int h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLWindowCall1 call = reinterpret_cast<CuteQOpenGLWindowCall1>(taken[1]);
      call(this, w, h, &handled);
      if (handled) return;
    }
    QOpenGLWindow::resizeGL(w, h);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::paintGL()
  void paintGL() override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLWindowCall2 call = reinterpret_cast<CuteQOpenGLWindowCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWindow::paintGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::paintUnderGL()
  void paintUnderGL() override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLWindowCall3 call = reinterpret_cast<CuteQOpenGLWindowCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWindow::paintUnderGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::paintOverGL()
  void paintOverGL() override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLWindowCall4 call = reinterpret_cast<CuteQOpenGLWindowCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWindow::paintOverGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLWindowCall5 call = reinterpret_cast<CuteQOpenGLWindowCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QOpenGLWindow::paintEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLWindow::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLWindowCall6 call = reinterpret_cast<CuteQOpenGLWindowCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QOpenGLWindow::resizeEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  int QOpenGLWindow::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGLWindowCall7 call = reinterpret_cast<CuteQOpenGLWindowCall7>(taken[7]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QOpenGLWindow::metric(metric);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  QPaintDevice *QOpenGLWindow::redirected(QPoint *a0) const
  QPaintDevice *redirected(QPoint *a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpenGLWindowCall8 call = reinterpret_cast<CuteQOpenGLWindowCall8>(taken[8]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QOpenGLWindow::redirected(a0);
  }
#endif  // !defined(QT_NO_OPENGL)

  //  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQOpenGLWindowCall9 call = reinterpret_cast<CuteQOpenGLWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPaintDeviceWindow::exposeEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QPaintDeviceWindow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQOpenGLWindowCall10 call = reinterpret_cast<CuteQOpenGLWindowCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPaintDeviceWindow::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QPaintEngine *QPaintDeviceWindow::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQOpenGLWindowCall11 call = reinterpret_cast<CuteQOpenGLWindowCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintDeviceWindow::paintEngine();
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQOpenGLWindowCall12 call = reinterpret_cast<CuteQOpenGLWindowCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQOpenGLWindowCall13 call = reinterpret_cast<CuteQOpenGLWindowCall13>(taken[13]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQOpenGLWindowCall14 call = reinterpret_cast<CuteQOpenGLWindowCall14>(taken[14]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQOpenGLWindowCall15 call = reinterpret_cast<CuteQOpenGLWindowCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQOpenGLWindowCall16 call = reinterpret_cast<CuteQOpenGLWindowCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQOpenGLWindowCall17 call = reinterpret_cast<CuteQOpenGLWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQOpenGLWindowCall18 call = reinterpret_cast<CuteQOpenGLWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQOpenGLWindowCall19 call = reinterpret_cast<CuteQOpenGLWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQOpenGLWindowCall20 call = reinterpret_cast<CuteQOpenGLWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQOpenGLWindowCall21 call = reinterpret_cast<CuteQOpenGLWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQOpenGLWindowCall22 call = reinterpret_cast<CuteQOpenGLWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQOpenGLWindowCall23 call = reinterpret_cast<CuteQOpenGLWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQOpenGLWindowCall24 call = reinterpret_cast<CuteQOpenGLWindowCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQOpenGLWindowCall25 call = reinterpret_cast<CuteQOpenGLWindowCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQOpenGLWindowCall26 call = reinterpret_cast<CuteQOpenGLWindowCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQOpenGLWindowCall27 call = reinterpret_cast<CuteQOpenGLWindowCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQOpenGLWindowCall28 call = reinterpret_cast<CuteQOpenGLWindowCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQOpenGLWindowCall29 call = reinterpret_cast<CuteQOpenGLWindowCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQOpenGLWindowCall30 call = reinterpret_cast<CuteQOpenGLWindowCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQOpenGLWindowCall31 call = reinterpret_cast<CuteQOpenGLWindowCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQOpenGLWindowCall32 call = reinterpret_cast<CuteQOpenGLWindowCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQOpenGLWindowCall33 call = reinterpret_cast<CuteQOpenGLWindowCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQOpenGLWindowCall34 call = reinterpret_cast<CuteQOpenGLWindowCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQOpenGLWindowCall35 call = reinterpret_cast<CuteQOpenGLWindowCall35>(taken[35]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQOpenGLWindowCall36 call = reinterpret_cast<CuteQOpenGLWindowCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQOpenGLWindowCall37 call = reinterpret_cast<CuteQOpenGLWindowCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQOpenGLWindowCall38 call = reinterpret_cast<CuteQOpenGLWindowCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQOpenGLWindowCall39 call = reinterpret_cast<CuteQOpenGLWindowCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQOpenGLWindowCall40 call = reinterpret_cast<CuteQOpenGLWindowCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQOpenGLWindowCall41 call = reinterpret_cast<CuteQOpenGLWindowCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpenGLWindow10metaObjectEv(
    const QOpenGLWindow *self) {
  return self->metaObject();
}

//  void *QOpenGLWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QOpenGLWindow11qt_metacastEPKc(
    QOpenGLWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLWindow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QOpenGLWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpenGLWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLWindow::tr(s, c, n));
}

//  QOpenGLWindowPrivate *QOpenGLWindow::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLWindowPrivate *ritual_ZN13QOpenGLWindow6d_funcEv(
    QOpenGLWindow *self) {
  return self->d_func();
}

//  const QOpenGLWindowPrivate *QOpenGLWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLWindowPrivate *ritual_ZNK13QOpenGLWindow6d_funcEv(
    const QOpenGLWindow *self) {
  return self->d_func();
}

//  QOpenGLWindow::QOpenGLWindow(UpdateBehavior updateBehavior, QWindow
//      *parent)
extern "C" Q_DECL_EXPORT
QOpenGLWindow *ritual_ZN13QOpenGLWindowC1ENS_14UpdateBehaviorEP7QWindow(
    QOpenGLWindow::UpdateBehavior updateBehavior,
    QWindow *parent) {
  return new CuteQOpenGLWindow(updateBehavior, parent);
}

//  QOpenGLWindow::QOpenGLWindow(QOpenGLContext *shareContext, UpdateBehavior
//      updateBehavior, QWindow *parent)
extern "C" Q_DECL_EXPORT
QOpenGLWindow *ritual_ZN13QOpenGLWindowC1EP14QOpenGLContextNS_14UpdateBehaviorEP7QWindow(
    QOpenGLContext *shareContext,
    QOpenGLWindow::UpdateBehavior updateBehavior,
    QWindow *parent) {
  return new CuteQOpenGLWindow(shareContext, updateBehavior, parent);
}

//  QOpenGLWindow::~QOpenGLWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindowD1Ev(QOpenGLWindow *self) {
  delete self;
}

//  UpdateBehavior QOpenGLWindow::updateBehavior() const
extern "C" Q_DECL_EXPORT
QOpenGLWindow::UpdateBehavior ritual_ZNK13QOpenGLWindow14updateBehaviorEv(
    const QOpenGLWindow *self) {
  return self->updateBehavior();
}

//  bool QOpenGLWindow::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLWindow7isValidEv(const QOpenGLWindow *self) {
  return self->isValid();
}

//  void QOpenGLWindow::makeCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow11makeCurrentEv(QOpenGLWindow *self) {
  self->makeCurrent();
}

//  void QOpenGLWindow::doneCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow11doneCurrentEv(QOpenGLWindow *self) {
  self->doneCurrent();
}

//  QOpenGLContext *QOpenGLWindow::context() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK13QOpenGLWindow7contextEv(
    const QOpenGLWindow *self) {
  return self->context();
}

//  QOpenGLContext *QOpenGLWindow::shareContext() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK13QOpenGLWindow12shareContextEv(
    const QOpenGLWindow *self) {
  return self->shareContext();
}

//  GLuint QOpenGLWindow::defaultFramebufferObject() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK13QOpenGLWindow24defaultFramebufferObjectEv(
    const QOpenGLWindow *self) {
  return self->defaultFramebufferObject();
}

//  QImage QOpenGLWindow::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QOpenGLWindow15grabFramebufferEv(QOpenGLWindow *self) {
  return new QImage(self->grabFramebuffer());
}

//  void QOpenGLWindow::frameSwapped()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow12frameSwappedEv(QOpenGLWindow *self) {
  self->frameSwapped();
}

//  void QOpenGLWindow::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow12initializeGLEv(QOpenGLWindow *self) {
  self->initializeGL();
}

//  void QOpenGLWindow::resizeGL(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow8resizeGLEii(
    QOpenGLWindow *self,
    int w,
    int h) {
  self->resizeGL(w, h);
}

//  void QOpenGLWindow::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow7paintGLEv(QOpenGLWindow *self) {
  self->paintGL();
}

//  void QOpenGLWindow::paintUnderGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow12paintUnderGLEv(QOpenGLWindow *self) {
  self->paintUnderGL();
}

//  void QOpenGLWindow::paintOverGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow11paintOverGLEv(QOpenGLWindow *self) {
  self->paintOverGL();
}

//  void QOpenGLWindow::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow10paintEventEP11QPaintEvent(
    QOpenGLWindow *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QOpenGLWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWindow11resizeEventEP12QResizeEvent(
    QOpenGLWindow *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  int QOpenGLWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QOpenGLWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  QPaintDevice *QOpenGLWindow::redirected(QPoint *a0) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK13QOpenGLWindow10redirectedEP6QPoint(
    const QOpenGLWindow *self,
    QPoint *a0) {
  return self->redirected(a0);
}

//  a Python function taken by a CuteQOpenGLWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLWindow(
    QOpenGLWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLWindow *>(self)->take(key, call);
}

//  void QOpenGLWindow::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow12initializeGLEv(QOpenGLWindow *self) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::initializeGL();
}

//  void QOpenGLWindow::resizeGL(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow8resizeGLEii(
    QOpenGLWindow *self,
    int w,
    int h) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::resizeGL(w, h);
}

//  void QOpenGLWindow::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow7paintGLEv(QOpenGLWindow *self) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::paintGL();
}

//  void QOpenGLWindow::paintUnderGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow12paintUnderGLEv(QOpenGLWindow *self) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::paintUnderGL();
}

//  void QOpenGLWindow::paintOverGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow11paintOverGLEv(QOpenGLWindow *self) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::paintOverGL();
}

//  void QOpenGLWindow::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow10paintEventEP11QPaintEvent(
    QOpenGLWindow *self,
    QPaintEvent *event) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::paintEvent(event);
}

//  void QOpenGLWindow::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWindow11resizeEventEP12QResizeEvent(
    QOpenGLWindow *self,
    QResizeEvent *event) {
  static_cast<OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::resizeEvent(
      event);
}

//  int QOpenGLWindow::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QOpenGLWindow6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLWindow *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::metric(
      metric);
}

//  QPaintDevice *QOpenGLWindow::redirected(QPoint *a0) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZNK13QOpenGLWindow10redirectedEP6QPoint(
    const QOpenGLWindow *self,
    QPoint *a0) {
  return static_cast<const OwnQOpenGLWindow *>(self)->OwnQOpenGLWindow::redirected(
      a0);
}

#endif  // !defined(QT_NO_OPENGL)
