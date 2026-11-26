//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/qprintpreviewwidget.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#if QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
#include <QtPrintSupport/qprintpreviewwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPrintPreviewWidget that Python can take functions over in. Every QPrintPreviewWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPrintPreviewWidgetCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(printpreviewwidget)
typedef int (*CuteQPrintPreviewWidgetCall1)(const void *, int *);
typedef const QSize * (*CuteQPrintPreviewWidgetCall2)(const void *, int *);
typedef const QSize * (*CuteQPrintPreviewWidgetCall3)(const void *, int *);
typedef int (*CuteQPrintPreviewWidgetCall4)(const void *, int, int *);
typedef bool (*CuteQPrintPreviewWidgetCall5)(const void *, int *);
typedef void * (*CuteQPrintPreviewWidgetCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPrintPreviewWidgetCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall11)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQPrintPreviewWidgetCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQPrintPreviewWidgetCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall17)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall18)(const void *, QEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall19)(const void *, QPaintEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQPrintPreviewWidgetCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQPrintPreviewWidgetCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQPrintPreviewWidgetCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintPreviewWidgetCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintPreviewWidgetCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintPreviewWidgetCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintPreviewWidgetCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQPrintPreviewWidgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQPrintPreviewWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQPrintPreviewWidgetCall33)(const void *, int, int *);
typedef void (*CuteQPrintPreviewWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQPrintPreviewWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQPrintPreviewWidgetCall36)(const void *, int *);
typedef void (*CuteQPrintPreviewWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQPrintPreviewWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQPrintPreviewWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPrintPreviewWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintPreviewWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPrintPreviewWidget : public QPrintPreviewWidget {
public:
  using QPrintPreviewWidget::QPrintPreviewWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(printpreviewwidget)
  //  void QPrintPreviewWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall0 call = reinterpret_cast<CuteQPrintPreviewWidgetCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QPrintPreviewWidget::setVisible(visible);
  }
#endif  // QT_CONFIG(printpreviewwidget)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall1 call = reinterpret_cast<CuteQPrintPreviewWidgetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall2 call = reinterpret_cast<CuteQPrintPreviewWidgetCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall3 call = reinterpret_cast<CuteQPrintPreviewWidgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall4 call = reinterpret_cast<CuteQPrintPreviewWidgetCall4>(taken[4]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall5 call = reinterpret_cast<CuteQPrintPreviewWidgetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall6 call = reinterpret_cast<CuteQPrintPreviewWidgetCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall7 call = reinterpret_cast<CuteQPrintPreviewWidgetCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall8 call = reinterpret_cast<CuteQPrintPreviewWidgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall9 call = reinterpret_cast<CuteQPrintPreviewWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall10 call = reinterpret_cast<CuteQPrintPreviewWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall11 call = reinterpret_cast<CuteQPrintPreviewWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall12 call = reinterpret_cast<CuteQPrintPreviewWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall13 call = reinterpret_cast<CuteQPrintPreviewWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall14 call = reinterpret_cast<CuteQPrintPreviewWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall15 call = reinterpret_cast<CuteQPrintPreviewWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall16 call = reinterpret_cast<CuteQPrintPreviewWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall17 call = reinterpret_cast<CuteQPrintPreviewWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall18 call = reinterpret_cast<CuteQPrintPreviewWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall19 call = reinterpret_cast<CuteQPrintPreviewWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall20 call = reinterpret_cast<CuteQPrintPreviewWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall21 call = reinterpret_cast<CuteQPrintPreviewWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall22 call = reinterpret_cast<CuteQPrintPreviewWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall23 call = reinterpret_cast<CuteQPrintPreviewWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall24 call = reinterpret_cast<CuteQPrintPreviewWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall25 call = reinterpret_cast<CuteQPrintPreviewWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall26 call = reinterpret_cast<CuteQPrintPreviewWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall27 call = reinterpret_cast<CuteQPrintPreviewWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall28 call = reinterpret_cast<CuteQPrintPreviewWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall29 call = reinterpret_cast<CuteQPrintPreviewWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall30 call = reinterpret_cast<CuteQPrintPreviewWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall31 call = reinterpret_cast<CuteQPrintPreviewWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall32 call = reinterpret_cast<CuteQPrintPreviewWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall33 call = reinterpret_cast<CuteQPrintPreviewWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall34 call = reinterpret_cast<CuteQPrintPreviewWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall35 call = reinterpret_cast<CuteQPrintPreviewWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall36 call = reinterpret_cast<CuteQPrintPreviewWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall37 call = reinterpret_cast<CuteQPrintPreviewWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall38 call = reinterpret_cast<CuteQPrintPreviewWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall39 call = reinterpret_cast<CuteQPrintPreviewWidgetCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall40 call = reinterpret_cast<CuteQPrintPreviewWidgetCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall41 call = reinterpret_cast<CuteQPrintPreviewWidgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall42 call = reinterpret_cast<CuteQPrintPreviewWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall43 call = reinterpret_cast<CuteQPrintPreviewWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall44 call = reinterpret_cast<CuteQPrintPreviewWidgetCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPrintPreviewWidgetCall45 call = reinterpret_cast<CuteQPrintPreviewWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPrintPreviewWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QPrintPreviewWidget10metaObjectEv(
    const QPrintPreviewWidget *self) {
  return self->metaObject();
}

//  void *QPrintPreviewWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QPrintPreviewWidget11qt_metacastEPKc(
    QPrintPreviewWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPrintPreviewWidget::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QPrintPreviewWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    QPrintPreviewWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPrintPreviewWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QPrintPreviewWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPrintPreviewWidget::tr(s, c, n));
}

//  QPrintPreviewWidgetPrivate *QPrintPreviewWidget::d_func()
extern "C" Q_DECL_EXPORT
QPrintPreviewWidgetPrivate *ritual_ZN19QPrintPreviewWidget6d_funcEv(
    QPrintPreviewWidget *self) {
  return self->d_func();
}

//  const QPrintPreviewWidgetPrivate *QPrintPreviewWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QPrintPreviewWidgetPrivate *ritual_ZNK19QPrintPreviewWidget6d_funcEv(
    const QPrintPreviewWidget *self) {
  return self->d_func();
}

//  QPrintPreviewWidget::QPrintPreviewWidget(QPrinter *printer, QWidget
//      *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QPrintPreviewWidget *ritual_ZN19QPrintPreviewWidgetC1EP8QPrinterP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QPrinter *printer,
    QWidget *parent,
    int flags) {
  return new CuteQPrintPreviewWidget(
      printer,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QPrintPreviewWidget::QPrintPreviewWidget(QWidget *parent, Qt::WindowFlags
//      flags)
extern "C" Q_DECL_EXPORT
QPrintPreviewWidget *ritual_ZN19QPrintPreviewWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQPrintPreviewWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QPrintPreviewWidget::~QPrintPreviewWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidgetD1Ev(QPrintPreviewWidget *self) {
  delete self;
}

//  qreal QPrintPreviewWidget::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QPrintPreviewWidget10zoomFactorEv(
    const QPrintPreviewWidget *self) {
  return self->zoomFactor();
}

//  QPageLayout::Orientation QPrintPreviewWidget::orientation() const
extern "C" Q_DECL_EXPORT
QPageLayout::Orientation ritual_ZNK19QPrintPreviewWidget11orientationEv(
    const QPrintPreviewWidget *self) {
  return self->orientation();
}

//  ViewMode QPrintPreviewWidget::viewMode() const
extern "C" Q_DECL_EXPORT
QPrintPreviewWidget::ViewMode ritual_ZNK19QPrintPreviewWidget8viewModeEv(
    const QPrintPreviewWidget *self) {
  return self->viewMode();
}

//  ZoomMode QPrintPreviewWidget::zoomMode() const
extern "C" Q_DECL_EXPORT
QPrintPreviewWidget::ZoomMode ritual_ZNK19QPrintPreviewWidget8zoomModeEv(
    const QPrintPreviewWidget *self) {
  return self->zoomMode();
}

//  int QPrintPreviewWidget::currentPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPrintPreviewWidget11currentPageEv(
    const QPrintPreviewWidget *self) {
  return self->currentPage();
}

//  int QPrintPreviewWidget::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPrintPreviewWidget9pageCountEv(
    const QPrintPreviewWidget *self) {
  return self->pageCount();
}

//  void QPrintPreviewWidget::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget10setVisibleEb(
    QPrintPreviewWidget *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QPrintPreviewWidget::print()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget5printEv(QPrintPreviewWidget *self) {
  self->print();
}

//  void QPrintPreviewWidget::zoomIn(qreal zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget6zoomInEd(
    QPrintPreviewWidget *self,
    qreal zoom) {
  self->zoomIn(zoom);
}

//  void QPrintPreviewWidget::zoomOut(qreal zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget7zoomOutEd(
    QPrintPreviewWidget *self,
    qreal zoom) {
  self->zoomOut(zoom);
}

//  void QPrintPreviewWidget::setZoomFactor(qreal zoomFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget13setZoomFactorEd(
    QPrintPreviewWidget *self,
    qreal zoomFactor) {
  self->setZoomFactor(zoomFactor);
}

//  void QPrintPreviewWidget::setOrientation(QPageLayout::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget14setOrientationEN11QPageLayout11OrientationE(
    QPrintPreviewWidget *self,
    QPageLayout::Orientation orientation) {
  self->setOrientation(orientation);
}

//  void QPrintPreviewWidget::setViewMode(ViewMode viewMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget11setViewModeENS_8ViewModeE(
    QPrintPreviewWidget *self,
    QPrintPreviewWidget::ViewMode viewMode) {
  self->setViewMode(viewMode);
}

//  void QPrintPreviewWidget::setZoomMode(ZoomMode zoomMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget11setZoomModeENS_8ZoomModeE(
    QPrintPreviewWidget *self,
    QPrintPreviewWidget::ZoomMode zoomMode) {
  self->setZoomMode(zoomMode);
}

//  void QPrintPreviewWidget::setCurrentPage(int pageNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget14setCurrentPageEi(
    QPrintPreviewWidget *self,
    int pageNumber) {
  self->setCurrentPage(pageNumber);
}

//  void QPrintPreviewWidget::fitToWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget10fitToWidthEv(
    QPrintPreviewWidget *self) {
  self->fitToWidth();
}

//  void QPrintPreviewWidget::fitInView()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget9fitInViewEv(QPrintPreviewWidget *self) {
  self->fitInView();
}

//  void QPrintPreviewWidget::setLandscapeOrientation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget23setLandscapeOrientationEv(
    QPrintPreviewWidget *self) {
  self->setLandscapeOrientation();
}

//  void QPrintPreviewWidget::setPortraitOrientation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget22setPortraitOrientationEv(
    QPrintPreviewWidget *self) {
  self->setPortraitOrientation();
}

//  void QPrintPreviewWidget::setSinglePageViewMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget21setSinglePageViewModeEv(
    QPrintPreviewWidget *self) {
  self->setSinglePageViewMode();
}

//  void QPrintPreviewWidget::setFacingPagesViewMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget22setFacingPagesViewModeEv(
    QPrintPreviewWidget *self) {
  self->setFacingPagesViewMode();
}

//  void QPrintPreviewWidget::setAllPagesViewMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget19setAllPagesViewModeEv(
    QPrintPreviewWidget *self) {
  self->setAllPagesViewMode();
}

//  void QPrintPreviewWidget::updatePreview()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget13updatePreviewEv(
    QPrintPreviewWidget *self) {
  self->updatePreview();
}

//  void QPrintPreviewWidget::paintRequested(QPrinter *printer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget14paintRequestedEP8QPrinter(
    QPrintPreviewWidget *self,
    QPrinter *printer) {
  self->paintRequested(printer);
}

//  void QPrintPreviewWidget::previewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrintPreviewWidget14previewChangedEv(
    QPrintPreviewWidget *self) {
  self->previewChanged();
}

//  a Python function taken by a CuteQPrintPreviewWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPrintPreviewWidget(
    QPrintPreviewWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPrintPreviewWidget *>(self)->take(key, call);
}

//  void QPrintPreviewWidget::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPrintPreviewWidget10setVisibleEb(
    QPrintPreviewWidget *self,
    bool visible) {
  self->QPrintPreviewWidget::setVisible(visible);
}

#endif  // QT_CONFIG(printpreviewwidget)
#endif  // QT_CONFIG(printpreviewwidget)
