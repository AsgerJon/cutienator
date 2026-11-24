//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGLWidgets/qopenglwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGLWidgets/qopenglwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QOpenGLWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOpenGLWidget : QOpenGLWidget {
  using QOpenGLWidget::initializeGL;
  using QOpenGLWidget::resizeGL;
  using QOpenGLWidget::paintGL;
  using QOpenGLWidget::paintEvent;
  using QOpenGLWidget::resizeEvent;
  using QOpenGLWidget::event;
  using QOpenGLWidget::metric;
  using QOpenGLWidget::redirected;
  using QOpenGLWidget::paintEngine;
};

//  A QOpenGLWidget that Python can take functions over in. Every QOpenGLWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpenGLWidgetCall0)(const void *, int *);
typedef void (*CuteQOpenGLWidgetCall1)(const void *, int, int, int *);
typedef void (*CuteQOpenGLWidgetCall2)(const void *, int *);
typedef void (*CuteQOpenGLWidgetCall3)(const void *, QPaintEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall4)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLWidgetCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQOpenGLWidgetCall6)(const void *, int, int *);
typedef void * (*CuteQOpenGLWidgetCall7)(const void *, QPoint *, int *);
typedef void * (*CuteQOpenGLWidgetCall8)(const void *, int *);
typedef int (*CuteQOpenGLWidgetCall9)(const void *, int *);
typedef void (*CuteQOpenGLWidgetCall10)(const void *, bool, int *);
typedef const QSize * (*CuteQOpenGLWidgetCall11)(const void *, int *);
typedef const QSize * (*CuteQOpenGLWidgetCall12)(const void *, int *);
typedef int (*CuteQOpenGLWidgetCall13)(const void *, int, int *);
typedef bool (*CuteQOpenGLWidgetCall14)(const void *, int *);
typedef void (*CuteQOpenGLWidgetCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall18)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQOpenGLWidgetCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQOpenGLWidgetCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall25)(const void *, QEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall27)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQOpenGLWidgetCall28)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQOpenGLWidgetCall29)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQOpenGLWidgetCall30)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQOpenGLWidgetCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQOpenGLWidgetCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQOpenGLWidgetCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQOpenGLWidgetCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQOpenGLWidgetCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall36)(const void *, QHideEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall37)(const void *, QEvent *, int *);
typedef void (*CuteQOpenGLWidgetCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQOpenGLWidgetCall39)(const void *, int *);
typedef void (*CuteQOpenGLWidgetCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQOpenGLWidgetCall41)(const void *, int, int *);
typedef bool (*CuteQOpenGLWidgetCall42)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLWidgetCall43)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWidgetCall44)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWidgetCall45)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWidgetCall46)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWidgetCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLWidgetCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLWidget : public QOpenGLWidget {
public:
  using QOpenGLWidget::QOpenGLWidget;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QOpenGLWidget12initializeGLEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QOpenGLWidget8resizeGLEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QOpenGLWidget7paintGLEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[42] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QOpenGLWidget::initializeGL()
  void initializeGL() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLWidgetCall0 call = reinterpret_cast<CuteQOpenGLWidgetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWidget::initializeGL();
  }

  //  void QOpenGLWidget::resizeGL(int w, int h)
  void resizeGL(int w, int h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLWidgetCall1 call = reinterpret_cast<CuteQOpenGLWidgetCall1>(taken[1]);
      call(this, w, h, &handled);
      if (handled) return;
    }
    QOpenGLWidget::resizeGL(w, h);
  }

  //  void QOpenGLWidget::paintGL()
  void paintGL() override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLWidgetCall2 call = reinterpret_cast<CuteQOpenGLWidgetCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLWidget::paintGL();
  }

  //  void QOpenGLWidget::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLWidgetCall3 call = reinterpret_cast<CuteQOpenGLWidgetCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QOpenGLWidget::paintEvent(e);
  }

  //  void QOpenGLWidget::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLWidgetCall4 call = reinterpret_cast<CuteQOpenGLWidgetCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QOpenGLWidget::resizeEvent(e);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QOpenGLWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLWidgetCall5 call = reinterpret_cast<CuteQOpenGLWidgetCall5>(taken[5]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QOpenGLWidget::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric)
  //      const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLWidgetCall6 call = reinterpret_cast<CuteQOpenGLWidgetCall6>(taken[6]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QOpenGLWidget::metric(metric);
  }

  //  QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const
  QPaintDevice *redirected(QPoint *p) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGLWidgetCall7 call = reinterpret_cast<CuteQOpenGLWidgetCall7>(taken[7]);
      void * given = call(this, p, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QOpenGLWidget::redirected(p);
  }

  //  QPaintEngine *QOpenGLWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpenGLWidgetCall8 call = reinterpret_cast<CuteQOpenGLWidgetCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QOpenGLWidget::paintEngine();
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQOpenGLWidgetCall9 call = reinterpret_cast<CuteQOpenGLWidgetCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[10]) {
      int handled = 0;
      CuteQOpenGLWidgetCall10 call = reinterpret_cast<CuteQOpenGLWidgetCall10>(taken[10]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQOpenGLWidgetCall11 call = reinterpret_cast<CuteQOpenGLWidgetCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQOpenGLWidgetCall12 call = reinterpret_cast<CuteQOpenGLWidgetCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQOpenGLWidgetCall13 call = reinterpret_cast<CuteQOpenGLWidgetCall13>(taken[13]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQOpenGLWidgetCall14 call = reinterpret_cast<CuteQOpenGLWidgetCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQOpenGLWidgetCall15 call = reinterpret_cast<CuteQOpenGLWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQOpenGLWidgetCall16 call = reinterpret_cast<CuteQOpenGLWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQOpenGLWidgetCall17 call = reinterpret_cast<CuteQOpenGLWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQOpenGLWidgetCall18 call = reinterpret_cast<CuteQOpenGLWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQOpenGLWidgetCall19 call = reinterpret_cast<CuteQOpenGLWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQOpenGLWidgetCall20 call = reinterpret_cast<CuteQOpenGLWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQOpenGLWidgetCall21 call = reinterpret_cast<CuteQOpenGLWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQOpenGLWidgetCall22 call = reinterpret_cast<CuteQOpenGLWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQOpenGLWidgetCall23 call = reinterpret_cast<CuteQOpenGLWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQOpenGLWidgetCall24 call = reinterpret_cast<CuteQOpenGLWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQOpenGLWidgetCall25 call = reinterpret_cast<CuteQOpenGLWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQOpenGLWidgetCall26 call = reinterpret_cast<CuteQOpenGLWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQOpenGLWidgetCall27 call = reinterpret_cast<CuteQOpenGLWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQOpenGLWidgetCall28 call = reinterpret_cast<CuteQOpenGLWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQOpenGLWidgetCall29 call = reinterpret_cast<CuteQOpenGLWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQOpenGLWidgetCall30 call = reinterpret_cast<CuteQOpenGLWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQOpenGLWidgetCall31 call = reinterpret_cast<CuteQOpenGLWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQOpenGLWidgetCall32 call = reinterpret_cast<CuteQOpenGLWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQOpenGLWidgetCall33 call = reinterpret_cast<CuteQOpenGLWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQOpenGLWidgetCall34 call = reinterpret_cast<CuteQOpenGLWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQOpenGLWidgetCall35 call = reinterpret_cast<CuteQOpenGLWidgetCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQOpenGLWidgetCall36 call = reinterpret_cast<CuteQOpenGLWidgetCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQOpenGLWidgetCall37 call = reinterpret_cast<CuteQOpenGLWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQOpenGLWidgetCall38 call = reinterpret_cast<CuteQOpenGLWidgetCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQOpenGLWidgetCall39 call = reinterpret_cast<CuteQOpenGLWidgetCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQOpenGLWidgetCall40 call = reinterpret_cast<CuteQOpenGLWidgetCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQOpenGLWidgetCall41 call = reinterpret_cast<CuteQOpenGLWidgetCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQOpenGLWidgetCall42 call = reinterpret_cast<CuteQOpenGLWidgetCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQOpenGLWidgetCall43 call = reinterpret_cast<CuteQOpenGLWidgetCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQOpenGLWidgetCall44 call = reinterpret_cast<CuteQOpenGLWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQOpenGLWidgetCall45 call = reinterpret_cast<CuteQOpenGLWidgetCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQOpenGLWidgetCall46 call = reinterpret_cast<CuteQOpenGLWidgetCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQOpenGLWidgetCall47 call = reinterpret_cast<CuteQOpenGLWidgetCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQOpenGLWidgetCall48 call = reinterpret_cast<CuteQOpenGLWidgetCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpenGLWidget10metaObjectEv(
    const QOpenGLWidget *self) {
  return self->metaObject();
}

//  QString QOpenGLWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpenGLWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLWidget::tr(s, c, n));
}

//  QOpenGLWidget::QOpenGLWidget(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QOpenGLWidget *ritual_ZN13QOpenGLWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQOpenGLWidget(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QOpenGLWidget::~QOpenGLWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidgetD1Ev(QOpenGLWidget *self) {
  delete self;
}

//  void QOpenGLWidget::setUpdateBehavior(UpdateBehavior updateBehavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget17setUpdateBehaviorENS_14UpdateBehaviorE(
    QOpenGLWidget *self,
    QOpenGLWidget::UpdateBehavior updateBehavior) {
  self->setUpdateBehavior(updateBehavior);
}

//  UpdateBehavior QOpenGLWidget::updateBehavior() const
extern "C" Q_DECL_EXPORT
QOpenGLWidget::UpdateBehavior ritual_ZNK13QOpenGLWidget14updateBehaviorEv(
    const QOpenGLWidget *self) {
  return self->updateBehavior();
}

//  void QOpenGLWidget::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget9setFormatERK14QSurfaceFormat(
    QOpenGLWidget *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QOpenGLWidget::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK13QOpenGLWidget6formatEv(
    const QOpenGLWidget *self) {
  return new QSurfaceFormat(self->format());
}

//  void QOpenGLWidget::setTextureFormat(GLenum texFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget16setTextureFormatEj(
    QOpenGLWidget *self,
    GLenum texFormat) {
  self->setTextureFormat(texFormat);
}

//  bool QOpenGLWidget::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLWidget7isValidEv(const QOpenGLWidget *self) {
  return self->isValid();
}

//  void QOpenGLWidget::makeCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget11makeCurrentEv(QOpenGLWidget *self) {
  self->makeCurrent();
}

//  void QOpenGLWidget::makeCurrent(TargetBuffer targetBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget11makeCurrentENS_12TargetBufferE(
    QOpenGLWidget *self,
    QOpenGLWidget::TargetBuffer targetBuffer) {
  self->makeCurrent(targetBuffer);
}

//  void QOpenGLWidget::doneCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget11doneCurrentEv(QOpenGLWidget *self) {
  self->doneCurrent();
}

//  QOpenGLContext *QOpenGLWidget::context() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK13QOpenGLWidget7contextEv(
    const QOpenGLWidget *self) {
  return self->context();
}

//  QImage QOpenGLWidget::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QOpenGLWidget15grabFramebufferEv(QOpenGLWidget *self) {
  return new QImage(self->grabFramebuffer());
}

//  QImage QOpenGLWidget::grabFramebuffer(TargetBuffer targetBuffer)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QOpenGLWidget15grabFramebufferENS_12TargetBufferE(
    QOpenGLWidget *self,
    QOpenGLWidget::TargetBuffer targetBuffer) {
  return new QImage(self->grabFramebuffer(targetBuffer));
}

//  TargetBuffer QOpenGLWidget::currentTargetBuffer() const
extern "C" Q_DECL_EXPORT
QOpenGLWidget::TargetBuffer ritual_ZNK13QOpenGLWidget19currentTargetBufferEv(
    const QOpenGLWidget *self) {
  return self->currentTargetBuffer();
}

//  void QOpenGLWidget::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget12initializeGLEv(QOpenGLWidget *self) {
  self->initializeGL();
}

//  void QOpenGLWidget::resizeGL(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget8resizeGLEii(
    QOpenGLWidget *self,
    int w,
    int h) {
  self->resizeGL(w, h);
}

//  void QOpenGLWidget::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget7paintGLEv(QOpenGLWidget *self) {
  self->paintGL();
}

//  void QOpenGLWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget10paintEventEP11QPaintEvent(
    QOpenGLWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QOpenGLWidget::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLWidget11resizeEventEP12QResizeEvent(
    QOpenGLWidget *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  bool QOpenGLWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLWidget5eventEP6QEvent(
    QOpenGLWidget *self,
    QEvent *e) {
  return self->event(e);
}

//  int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QOpenGLWidget6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLWidget *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK13QOpenGLWidget10redirectedEP6QPoint(
    const QOpenGLWidget *self,
    QPoint *p) {
  return self->redirected(p);
}

//  QPaintEngine *QOpenGLWidget::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK13QOpenGLWidget11paintEngineEv(
    const QOpenGLWidget *self) {
  return self->paintEngine();
}

//  a Python function taken by a CuteQOpenGLWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLWidget(
    QOpenGLWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLWidget *>(self)->take(key, call);
}

//  void QOpenGLWidget::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWidget12initializeGLEv(QOpenGLWidget *self) {
  static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::initializeGL();
}

//  void QOpenGLWidget::resizeGL(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWidget8resizeGLEii(
    QOpenGLWidget *self,
    int w,
    int h) {
  static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::resizeGL(w, h);
}

//  void QOpenGLWidget::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWidget7paintGLEv(QOpenGLWidget *self) {
  static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::paintGL();
}

//  void QOpenGLWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWidget10paintEventEP11QPaintEvent(
    QOpenGLWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::paintEvent(e);
}

//  void QOpenGLWidget::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QOpenGLWidget11resizeEventEP12QResizeEvent(
    QOpenGLWidget *self,
    QResizeEvent *e) {
  static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::resizeEvent(e);
}

//  bool QOpenGLWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QOpenGLWidget5eventEP6QEvent(
    QOpenGLWidget *self,
    QEvent *e) {
  return static_cast<OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::event(e);
}

//  int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QOpenGLWidget6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLWidget *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::metric(
      metric);
}

//  QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZNK13QOpenGLWidget10redirectedEP6QPoint(
    const QOpenGLWidget *self,
    QPoint *p) {
  return static_cast<const OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::redirected(
      p);
}

//  QPaintEngine *QOpenGLWidget::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK13QOpenGLWidget11paintEngineEv(
    const QOpenGLWidget *self) {
  return static_cast<const OwnQOpenGLWidget *>(self)->OwnQOpenGLWidget::paintEngine();
}
