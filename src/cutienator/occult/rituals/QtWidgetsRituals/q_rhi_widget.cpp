//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qrhiwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qrhiwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRhiWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRhiWidget : QRhiWidget {
  using QRhiWidget::initialize;
  using QRhiWidget::render;
  using QRhiWidget::releaseResources;
  using QRhiWidget::resizeEvent;
  using QRhiWidget::paintEvent;
  using QRhiWidget::event;
};

//  A QRhiWidget that Python can take functions over in. Every QRhiWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRhiWidgetCall0)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiWidgetCall1)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiWidgetCall2)(const void *, int *);
typedef void (*CuteQRhiWidgetCall3)(const void *, QResizeEvent *, int *);
typedef void (*CuteQRhiWidgetCall4)(const void *, QPaintEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRhiWidgetCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQRhiWidgetCall6)(const void *, int *);
typedef void (*CuteQRhiWidgetCall7)(const void *, bool, int *);
typedef const QSize * (*CuteQRhiWidgetCall8)(const void *, int *);
typedef const QSize * (*CuteQRhiWidgetCall9)(const void *, int *);
typedef int (*CuteQRhiWidgetCall10)(const void *, int, int *);
typedef bool (*CuteQRhiWidgetCall11)(const void *, int *);
typedef void * (*CuteQRhiWidgetCall12)(const void *, int *);
typedef void (*CuteQRhiWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRhiWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRhiWidgetCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRhiWidgetCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQRhiWidgetCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQRhiWidgetCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRhiWidgetCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRhiWidgetCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRhiWidgetCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRhiWidgetCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQRhiWidgetCall23)(const void *, QEvent *, int *);
typedef void (*CuteQRhiWidgetCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQRhiWidgetCall25)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQRhiWidgetCall26)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQRhiWidgetCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQRhiWidgetCall28)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRhiWidgetCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRhiWidgetCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRhiWidgetCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRhiWidgetCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQRhiWidgetCall33)(const void *, QShowEvent *, int *);
typedef void (*CuteQRhiWidgetCall34)(const void *, QHideEvent *, int *);
typedef void (*CuteQRhiWidgetCall35)(const void *, QEvent *, int *);
typedef int (*CuteQRhiWidgetCall36)(const void *, int, int *);
typedef void (*CuteQRhiWidgetCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQRhiWidgetCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQRhiWidgetCall39)(const void *, int *);
typedef void (*CuteQRhiWidgetCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQRhiWidgetCall41)(const void *, int, int *);
typedef bool (*CuteQRhiWidgetCall42)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRhiWidgetCall43)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRhiWidgetCall44)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRhiWidgetCall45)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRhiWidgetCall46)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRhiWidgetCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRhiWidgetCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRhiWidget : public QRhiWidget {
public:
  using QRhiWidget::QRhiWidget;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiWidget6renderEP17QRhiCommandBuffer")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiWidget16releaseResourcesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
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

  //  void QRhiWidget::initialize(QRhiCommandBuffer *cb)
  void initialize(QRhiCommandBuffer *cb) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiWidgetCall0 call = reinterpret_cast<CuteQRhiWidgetCall0>(taken[0]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiWidget::initialize(cb);
  }

  //  void QRhiWidget::render(QRhiCommandBuffer *cb)
  void render(QRhiCommandBuffer *cb) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiWidgetCall1 call = reinterpret_cast<CuteQRhiWidgetCall1>(taken[1]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiWidget::render(cb);
  }

  //  void QRhiWidget::releaseResources()
  void releaseResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiWidgetCall2 call = reinterpret_cast<CuteQRhiWidgetCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiWidget::releaseResources();
  }

  //  void QRhiWidget::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiWidgetCall3 call = reinterpret_cast<CuteQRhiWidgetCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QRhiWidget::resizeEvent(e);
  }

  //  void QRhiWidget::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiWidgetCall4 call = reinterpret_cast<CuteQRhiWidgetCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QRhiWidget::paintEvent(e);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QRhiWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiWidgetCall5 call = reinterpret_cast<CuteQRhiWidgetCall5>(taken[5]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QRhiWidget::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiWidgetCall6 call = reinterpret_cast<CuteQRhiWidgetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRhiWidgetCall7 call = reinterpret_cast<CuteQRhiWidgetCall7>(taken[7]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiWidgetCall8 call = reinterpret_cast<CuteQRhiWidgetCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiWidgetCall9 call = reinterpret_cast<CuteQRhiWidgetCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiWidgetCall10 call = reinterpret_cast<CuteQRhiWidgetCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiWidgetCall11 call = reinterpret_cast<CuteQRhiWidgetCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiWidgetCall12 call = reinterpret_cast<CuteQRhiWidgetCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiWidgetCall13 call = reinterpret_cast<CuteQRhiWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiWidgetCall14 call = reinterpret_cast<CuteQRhiWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiWidgetCall15 call = reinterpret_cast<CuteQRhiWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiWidgetCall16 call = reinterpret_cast<CuteQRhiWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRhiWidgetCall17 call = reinterpret_cast<CuteQRhiWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiWidgetCall18 call = reinterpret_cast<CuteQRhiWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiWidgetCall19 call = reinterpret_cast<CuteQRhiWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiWidgetCall20 call = reinterpret_cast<CuteQRhiWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiWidgetCall21 call = reinterpret_cast<CuteQRhiWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiWidgetCall22 call = reinterpret_cast<CuteQRhiWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiWidgetCall23 call = reinterpret_cast<CuteQRhiWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiWidgetCall24 call = reinterpret_cast<CuteQRhiWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRhiWidgetCall25 call = reinterpret_cast<CuteQRhiWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRhiWidgetCall26 call = reinterpret_cast<CuteQRhiWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRhiWidgetCall27 call = reinterpret_cast<CuteQRhiWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRhiWidgetCall28 call = reinterpret_cast<CuteQRhiWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiWidgetCall29 call = reinterpret_cast<CuteQRhiWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiWidgetCall30 call = reinterpret_cast<CuteQRhiWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiWidgetCall31 call = reinterpret_cast<CuteQRhiWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiWidgetCall32 call = reinterpret_cast<CuteQRhiWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiWidgetCall33 call = reinterpret_cast<CuteQRhiWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiWidgetCall34 call = reinterpret_cast<CuteQRhiWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiWidgetCall35 call = reinterpret_cast<CuteQRhiWidgetCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiWidgetCall36 call = reinterpret_cast<CuteQRhiWidgetCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiWidgetCall37 call = reinterpret_cast<CuteQRhiWidgetCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiWidgetCall38 call = reinterpret_cast<CuteQRhiWidgetCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiWidgetCall39 call = reinterpret_cast<CuteQRhiWidgetCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiWidgetCall40 call = reinterpret_cast<CuteQRhiWidgetCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiWidgetCall41 call = reinterpret_cast<CuteQRhiWidgetCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiWidgetCall42 call = reinterpret_cast<CuteQRhiWidgetCall42>(taken[42]);
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
      CuteQRhiWidgetCall43 call = reinterpret_cast<CuteQRhiWidgetCall43>(taken[43]);
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
      CuteQRhiWidgetCall44 call = reinterpret_cast<CuteQRhiWidgetCall44>(taken[44]);
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
      CuteQRhiWidgetCall45 call = reinterpret_cast<CuteQRhiWidgetCall45>(taken[45]);
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
      CuteQRhiWidgetCall46 call = reinterpret_cast<CuteQRhiWidgetCall46>(taken[46]);
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
      CuteQRhiWidgetCall47 call = reinterpret_cast<CuteQRhiWidgetCall47>(taken[47]);
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
      CuteQRhiWidgetCall48 call = reinterpret_cast<CuteQRhiWidgetCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRhiWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QRhiWidget10metaObjectEv(
    const QRhiWidget *self) {
  return self->metaObject();
}

//  QString QRhiWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QRhiWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRhiWidget::tr(s, c, n));
}

//  QRhiWidgetPrivate *QRhiWidget::d_func()
extern "C" Q_DECL_EXPORT
QRhiWidgetPrivate *ritual_ZN10QRhiWidget6d_funcEv(QRhiWidget *self) {
  return self->d_func();
}

//  const QRhiWidgetPrivate *QRhiWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QRhiWidgetPrivate *ritual_ZNK10QRhiWidget6d_funcEv(
    const QRhiWidget *self) {
  return self->d_func();
}

//  QRhiWidget::QRhiWidget(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QRhiWidget *ritual_ZN10QRhiWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQRhiWidget(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QRhiWidget::~QRhiWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidgetD1Ev(QRhiWidget *self) {
  delete self;
}

//  Api QRhiWidget::api() const
extern "C" Q_DECL_EXPORT
QRhiWidget::Api ritual_ZNK10QRhiWidget3apiEv(const QRhiWidget *self) {
  return self->api();
}

//  void QRhiWidget::setApi(Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget6setApiENS_3ApiE(
    QRhiWidget *self,
    QRhiWidget::Api api) {
  self->setApi(api);
}

//  bool QRhiWidget::isDebugLayerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiWidget19isDebugLayerEnabledEv(const QRhiWidget *self) {
  return self->isDebugLayerEnabled();
}

//  void QRhiWidget::setDebugLayerEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget20setDebugLayerEnabledEb(
    QRhiWidget *self,
    bool enable) {
  self->setDebugLayerEnabled(enable);
}

//  int QRhiWidget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRhiWidget11sampleCountEv(const QRhiWidget *self) {
  return self->sampleCount();
}

//  void QRhiWidget::setSampleCount(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget14setSampleCountEi(QRhiWidget *self, int samples) {
  self->setSampleCount(samples);
}

//  TextureFormat QRhiWidget::colorBufferFormat() const
extern "C" Q_DECL_EXPORT
QRhiWidget::TextureFormat ritual_ZNK10QRhiWidget17colorBufferFormatEv(
    const QRhiWidget *self) {
  return self->colorBufferFormat();
}

//  void QRhiWidget::setColorBufferFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget20setColorBufferFormatENS_13TextureFormatE(
    QRhiWidget *self,
    QRhiWidget::TextureFormat format) {
  self->setColorBufferFormat(format);
}

//  QSize QRhiWidget::fixedColorBufferSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QRhiWidget20fixedColorBufferSizeEv(
    const QRhiWidget *self) {
  return new QSize(self->fixedColorBufferSize());
}

//  void QRhiWidget::setFixedColorBufferSize(QSize pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget23setFixedColorBufferSizeE5QSize(
    QRhiWidget *self,
    const QSize *pixelSize) {
  self->setFixedColorBufferSize(*pixelSize);
}

//  void QRhiWidget::setFixedColorBufferSize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget23setFixedColorBufferSizeEii(
    QRhiWidget *self,
    int w,
    int h) {
  self->setFixedColorBufferSize(w, h);
}

//  bool QRhiWidget::isMirrorVerticallyEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiWidget25isMirrorVerticallyEnabledEv(
    const QRhiWidget *self) {
  return self->isMirrorVerticallyEnabled();
}

//  void QRhiWidget::setMirrorVertically(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget19setMirrorVerticallyEb(
    QRhiWidget *self,
    bool enabled) {
  self->setMirrorVertically(enabled);
}

//  QImage QRhiWidget::grabFramebuffer() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK10QRhiWidget15grabFramebufferEv(const QRhiWidget *self) {
  return new QImage(self->grabFramebuffer());
}

//  bool QRhiWidget::isAutoRenderTargetEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiWidget25isAutoRenderTargetEnabledEv(
    const QRhiWidget *self) {
  return self->isAutoRenderTargetEnabled();
}

//  void QRhiWidget::setAutoRenderTarget(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget19setAutoRenderTargetEb(
    QRhiWidget *self,
    bool enabled) {
  self->setAutoRenderTarget(enabled);
}

//  void QRhiWidget::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer(
    QRhiWidget *self,
    QRhiCommandBuffer *cb) {
  self->initialize(cb);
}

//  void QRhiWidget::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget6renderEP17QRhiCommandBuffer(
    QRhiWidget *self,
    QRhiCommandBuffer *cb) {
  self->render(cb);
}

//  void QRhiWidget::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget16releaseResourcesEv(QRhiWidget *self) {
  self->releaseResources();
}

//  QRhi *QRhiWidget::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK10QRhiWidget3rhiEv(const QRhiWidget *self) {
  return self->rhi();
}

//  QRhiTexture *QRhiWidget::colorTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK10QRhiWidget12colorTextureEv(const QRhiWidget *self) {
  return self->colorTexture();
}

//  QRhiRenderBuffer *QRhiWidget::msaaColorBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK10QRhiWidget15msaaColorBufferEv(
    const QRhiWidget *self) {
  return self->msaaColorBuffer();
}

//  QRhiTexture *QRhiWidget::resolveTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK10QRhiWidget14resolveTextureEv(
    const QRhiWidget *self) {
  return self->resolveTexture();
}

//  QRhiRenderBuffer *QRhiWidget::depthStencilBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK10QRhiWidget18depthStencilBufferEv(
    const QRhiWidget *self) {
  return self->depthStencilBuffer();
}

//  QRhiRenderTarget *QRhiWidget::renderTarget() const
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZNK10QRhiWidget12renderTargetEv(
    const QRhiWidget *self) {
  return self->renderTarget();
}

//  void QRhiWidget::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget11resizeEventEP12QResizeEvent(
    QRhiWidget *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  void QRhiWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget10paintEventEP11QPaintEvent(
    QRhiWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  bool QRhiWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QRhiWidget5eventEP6QEvent(QRhiWidget *self, QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQRhiWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiWidget(QRhiWidget *self, const char *key, void *call) {
  return static_cast<CuteQRhiWidget *>(self)->take(key, call);
}

//  void QRhiWidget::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiWidget10initializeEP17QRhiCommandBuffer(
    QRhiWidget *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::initialize(cb);
}

//  void QRhiWidget::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiWidget6renderEP17QRhiCommandBuffer(
    QRhiWidget *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::render(cb);
}

//  void QRhiWidget::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiWidget16releaseResourcesEv(QRhiWidget *self) {
  static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::releaseResources();
}

//  void QRhiWidget::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiWidget11resizeEventEP12QResizeEvent(
    QRhiWidget *self,
    QResizeEvent *e) {
  static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::resizeEvent(e);
}

//  void QRhiWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiWidget10paintEventEP11QPaintEvent(
    QRhiWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::paintEvent(e);
}

//  bool QRhiWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QRhiWidget5eventEP6QEvent(QRhiWidget *self, QEvent *e) {
  return static_cast<OwnQRhiWidget *>(self)->OwnQRhiWidget::event(e);
}
