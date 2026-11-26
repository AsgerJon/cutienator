//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspainterwidget.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtCanvasPainter/qtcanvaspainterglobal.h>
#if 1
#include <QtCanvasPainter/QtCanvasPainter>
#include <QtCanvasPainter/qcanvaspainterwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QCanvasPainterWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCanvasPainterWidget : QCanvasPainterWidget {
  using QCanvasPainterWidget::initializeResources;
  using QCanvasPainterWidget::prePaint;
  using QCanvasPainterWidget::paint;
  using QCanvasPainterWidget::graphicsResourcesInvalidated;
  using QCanvasPainterWidget::initialize;
  using QCanvasPainterWidget::render;
  using QCanvasPainterWidget::releaseResources;
  using QCanvasPainterWidget::event;
};

//  A QCanvasPainterWidget that Python can take functions over in. Every QCanvasPainterWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCanvasPainterWidgetCall0)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterWidgetCall1)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterWidgetCall2)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterWidgetCall3)(const void *, int *);
typedef void (*CuteQCanvasPainterWidgetCall4)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQCanvasPainterWidgetCall5)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQCanvasPainterWidgetCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanvasPainterWidgetCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall8)(const void *, QResizeEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall9)(const void *, QPaintEvent *, int *);
typedef int (*CuteQCanvasPainterWidgetCall10)(const void *, int *);
typedef void (*CuteQCanvasPainterWidgetCall11)(const void *, bool, int *);
typedef const QSize * (*CuteQCanvasPainterWidgetCall12)(const void *, int *);
typedef const QSize * (*CuteQCanvasPainterWidgetCall13)(const void *, int *);
typedef int (*CuteQCanvasPainterWidgetCall14)(const void *, int, int *);
typedef bool (*CuteQCanvasPainterWidgetCall15)(const void *, int *);
typedef void * (*CuteQCanvasPainterWidgetCall16)(const void *, int *);
typedef void (*CuteQCanvasPainterWidgetCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQCanvasPainterWidgetCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQCanvasPainterWidgetCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall26)(const void *, QEnterEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall27)(const void *, QEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall28)(const void *, QMoveEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall29)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQCanvasPainterWidgetCall30)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQCanvasPainterWidgetCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQCanvasPainterWidgetCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQCanvasPainterWidgetCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQCanvasPainterWidgetCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQCanvasPainterWidgetCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQCanvasPainterWidgetCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQCanvasPainterWidgetCall37)(const void *, QShowEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall38)(const void *, QHideEvent *, int *);
typedef void (*CuteQCanvasPainterWidgetCall39)(const void *, QEvent *, int *);
typedef int (*CuteQCanvasPainterWidgetCall40)(const void *, int, int *);
typedef void (*CuteQCanvasPainterWidgetCall41)(const void *, QPainter *, int *);
typedef void * (*CuteQCanvasPainterWidgetCall42)(const void *, QPoint *, int *);
typedef void * (*CuteQCanvasPainterWidgetCall43)(const void *, int *);
typedef void (*CuteQCanvasPainterWidgetCall44)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQCanvasPainterWidgetCall45)(const void *, int, int *);
typedef bool (*CuteQCanvasPainterWidgetCall46)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanvasPainterWidgetCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterWidgetCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCanvasPainterWidget : public QCanvasPainterWidget {
public:
  using QCanvasPainterWidget::QCanvasPainterWidget;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QCanvasPainterWidget19initializeResourcesEP14QCanvasPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QCanvasPainterWidget28graphicsResourcesInvalidatedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiWidget6renderEP17QRhiCommandBuffer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiWidget16releaseResourcesEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[29] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QCanvasPainterWidget::initializeResources(QCanvasPainter
  //      *painter)
  void initializeResources(QCanvasPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall0 call = reinterpret_cast<CuteQCanvasPainterWidgetCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::initializeResources(painter);
  }

  //  void QCanvasPainterWidget::prePaint(QCanvasPainter *painter)
  void prePaint(QCanvasPainter *painter) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall1 call = reinterpret_cast<CuteQCanvasPainterWidgetCall1>(taken[1]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::prePaint(painter);
  }

  //  void QCanvasPainterWidget::paint(QCanvasPainter *painter)
  void paint(QCanvasPainter *painter) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall2 call = reinterpret_cast<CuteQCanvasPainterWidgetCall2>(taken[2]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::paint(painter);
  }

  //  void QCanvasPainterWidget::graphicsResourcesInvalidated()
  void graphicsResourcesInvalidated() override {
    if (taken[3]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall3 call = reinterpret_cast<CuteQCanvasPainterWidgetCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::graphicsResourcesInvalidated();
  }

  //  void QCanvasPainterWidget::initialize(QRhiCommandBuffer *cb)
  void initialize(QRhiCommandBuffer *cb) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall4 call = reinterpret_cast<CuteQCanvasPainterWidgetCall4>(taken[4]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::initialize(cb);
  }

  //  void QCanvasPainterWidget::render(QRhiCommandBuffer *cb)
  void render(QRhiCommandBuffer *cb) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall5 call = reinterpret_cast<CuteQCanvasPainterWidgetCall5>(taken[5]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::render(cb);
  }

  //  void QCanvasPainterWidget::releaseResources()
  void releaseResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall6 call = reinterpret_cast<CuteQCanvasPainterWidgetCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QCanvasPainterWidget::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QCanvasPainterWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall7 call = reinterpret_cast<CuteQCanvasPainterWidgetCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QCanvasPainterWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QRhiWidget::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall8 call = reinterpret_cast<CuteQCanvasPainterWidgetCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QRhiWidget::resizeEvent(e);
  }

  //  void QRhiWidget::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall9 call = reinterpret_cast<CuteQCanvasPainterWidgetCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QRhiWidget::paintEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall10 call = reinterpret_cast<CuteQCanvasPainterWidgetCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall11 call = reinterpret_cast<CuteQCanvasPainterWidgetCall11>(taken[11]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall12 call = reinterpret_cast<CuteQCanvasPainterWidgetCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall13 call = reinterpret_cast<CuteQCanvasPainterWidgetCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall14 call = reinterpret_cast<CuteQCanvasPainterWidgetCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall15 call = reinterpret_cast<CuteQCanvasPainterWidgetCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall16 call = reinterpret_cast<CuteQCanvasPainterWidgetCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall17 call = reinterpret_cast<CuteQCanvasPainterWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall18 call = reinterpret_cast<CuteQCanvasPainterWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall19 call = reinterpret_cast<CuteQCanvasPainterWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall20 call = reinterpret_cast<CuteQCanvasPainterWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall21 call = reinterpret_cast<CuteQCanvasPainterWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall22 call = reinterpret_cast<CuteQCanvasPainterWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall23 call = reinterpret_cast<CuteQCanvasPainterWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall24 call = reinterpret_cast<CuteQCanvasPainterWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall25 call = reinterpret_cast<CuteQCanvasPainterWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall26 call = reinterpret_cast<CuteQCanvasPainterWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall27 call = reinterpret_cast<CuteQCanvasPainterWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall28 call = reinterpret_cast<CuteQCanvasPainterWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall29 call = reinterpret_cast<CuteQCanvasPainterWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall30 call = reinterpret_cast<CuteQCanvasPainterWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall31 call = reinterpret_cast<CuteQCanvasPainterWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall32 call = reinterpret_cast<CuteQCanvasPainterWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall33 call = reinterpret_cast<CuteQCanvasPainterWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall34 call = reinterpret_cast<CuteQCanvasPainterWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall35 call = reinterpret_cast<CuteQCanvasPainterWidgetCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall36 call = reinterpret_cast<CuteQCanvasPainterWidgetCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall37 call = reinterpret_cast<CuteQCanvasPainterWidgetCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall38 call = reinterpret_cast<CuteQCanvasPainterWidgetCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall39 call = reinterpret_cast<CuteQCanvasPainterWidgetCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall40 call = reinterpret_cast<CuteQCanvasPainterWidgetCall40>(taken[40]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall41 call = reinterpret_cast<CuteQCanvasPainterWidgetCall41>(taken[41]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall42 call = reinterpret_cast<CuteQCanvasPainterWidgetCall42>(taken[42]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall43 call = reinterpret_cast<CuteQCanvasPainterWidgetCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall44 call = reinterpret_cast<CuteQCanvasPainterWidgetCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall45 call = reinterpret_cast<CuteQCanvasPainterWidgetCall45>(taken[45]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[46]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall46 call = reinterpret_cast<CuteQCanvasPainterWidgetCall46>(taken[46]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall47 call = reinterpret_cast<CuteQCanvasPainterWidgetCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall48 call = reinterpret_cast<CuteQCanvasPainterWidgetCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall49 call = reinterpret_cast<CuteQCanvasPainterWidgetCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall50 call = reinterpret_cast<CuteQCanvasPainterWidgetCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall51 call = reinterpret_cast<CuteQCanvasPainterWidgetCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQCanvasPainterWidgetCall52 call = reinterpret_cast<CuteQCanvasPainterWidgetCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCanvasPainterWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCanvasPainterWidget10metaObjectEv(
    const QCanvasPainterWidget *self) {
  return self->metaObject();
}

//  void *QCanvasPainterWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QCanvasPainterWidget11qt_metacastEPKc(
    QCanvasPainterWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCanvasPainterWidget::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QCanvasPainterWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    QCanvasPainterWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCanvasPainterWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QCanvasPainterWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCanvasPainterWidget::tr(s, c, n));
}

//  QCanvasPainterWidget::QCanvasPainterWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCanvasPainterWidget *ritual_ZN20QCanvasPainterWidgetC1EP7QWidget(
    QWidget *parent) {
  return new CuteQCanvasPainterWidget(parent);
}

//  QCanvasPainterWidget::~QCanvasPainterWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidgetD1Ev(QCanvasPainterWidget *self) {
  delete self;
}

//  QColor QCanvasPainterWidget::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QCanvasPainterWidget9fillColorEv(
    const QCanvasPainterWidget *self) {
  return new QColor(self->fillColor());
}

//  void QCanvasPainterWidget::setFillColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget12setFillColorE6QColor(
    QCanvasPainterWidget *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  bool QCanvasPainterWidget::hasSharedPainter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCanvasPainterWidget16hasSharedPainterEv(
    const QCanvasPainterWidget *self) {
  return self->hasSharedPainter();
}

//  void QCanvasPainterWidget::setSharedPainter(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget16setSharedPainterEb(
    QCanvasPainterWidget *self,
    bool enable) {
  self->setSharedPainter(enable);
}

//  void QCanvasPainterWidget::initializeResources(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget19initializeResourcesEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  self->initializeResources(painter);
}

//  void QCanvasPainterWidget::prePaint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  self->prePaint(painter);
}

//  void QCanvasPainterWidget::paint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  self->paint(painter);
}

//  void QCanvasPainterWidget::graphicsResourcesInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget28graphicsResourcesInvalidatedEv(
    QCanvasPainterWidget *self) {
  self->graphicsResourcesInvalidated();
}

//  void QCanvasPainterWidget::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget10initializeEP17QRhiCommandBuffer(
    QCanvasPainterWidget *self,
    QRhiCommandBuffer *cb) {
  self->initialize(cb);
}

//  void QCanvasPainterWidget::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget6renderEP17QRhiCommandBuffer(
    QCanvasPainterWidget *self,
    QRhiCommandBuffer *cb) {
  self->render(cb);
}

//  void QCanvasPainterWidget::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget16releaseResourcesEv(
    QCanvasPainterWidget *self) {
  self->releaseResources();
}

//  bool QCanvasPainterWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCanvasPainterWidget5eventEP6QEvent(
    QCanvasPainterWidget *self,
    QEvent *event) {
  return self->event(event);
}

//  void QCanvasPainterWidget::beginCanvasPainting(QCanvasOffscreenCanvas
//      &canvas)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget19beginCanvasPaintingER22QCanvasOffscreenCanvas(
    QCanvasPainterWidget *self,
    QCanvasOffscreenCanvas *canvas) {
  self->beginCanvasPainting(*canvas);
}

//  void QCanvasPainterWidget::endCanvasPainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget17endCanvasPaintingEv(
    QCanvasPainterWidget *self) {
  self->endCanvasPainting();
}

//  QCanvasPainterWidgetPrivate *QCanvasPainterWidget::d_func()
extern "C" Q_DECL_EXPORT
QCanvasPainterWidgetPrivate *ritual_ZN20QCanvasPainterWidget6d_funcEv(
    QCanvasPainterWidget *self) {
  return self->d_func();
}

//  const QCanvasPainterWidgetPrivate *QCanvasPainterWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QCanvasPainterWidgetPrivate *ritual_ZNK20QCanvasPainterWidget6d_funcEv(
    const QCanvasPainterWidget *self) {
  return self->d_func();
}

//  void QCanvasPainterWidget::grabCanvasImpl(const QCanvasOffscreenCanvas
//      &canvas, const QObject *context, QtPrivate::QSlotObjectBase *slotObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCanvasPainterWidget14grabCanvasImplERK22QCanvasOffscreenCanvasPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QCanvasPainterWidget *self,
    const QCanvasOffscreenCanvas *canvas,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj) {
  self->grabCanvasImpl(*canvas, context, slotObj);
}

//  a Python function taken by a CuteQCanvasPainterWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasPainterWidget(
    QCanvasPainterWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasPainterWidget *>(self)->take(key, call);
}

//  void QCanvasPainterWidget::initializeResources(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget19initializeResourcesEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::initializeResources(
      painter);
}

//  void QCanvasPainterWidget::prePaint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::prePaint(
      painter);
}

//  void QCanvasPainterWidget::paint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter(
    QCanvasPainterWidget *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::paint(
      painter);
}

//  void QCanvasPainterWidget::graphicsResourcesInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget28graphicsResourcesInvalidatedEv(
    QCanvasPainterWidget *self) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::graphicsResourcesInvalidated();
}

//  void QCanvasPainterWidget::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget10initializeEP17QRhiCommandBuffer(
    QCanvasPainterWidget *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::initialize(
      cb);
}

//  void QCanvasPainterWidget::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget6renderEP17QRhiCommandBuffer(
    QCanvasPainterWidget *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::render(
      cb);
}

//  void QCanvasPainterWidget::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCanvasPainterWidget16releaseResourcesEv(
    QCanvasPainterWidget *self) {
  static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::releaseResources();
}

//  bool QCanvasPainterWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QCanvasPainterWidget5eventEP6QEvent(
    QCanvasPainterWidget *self,
    QEvent *event) {
  return static_cast<OwnQCanvasPainterWidget *>(self)->OwnQCanvasPainterWidget::event(
      event);
}

#endif  // 1
