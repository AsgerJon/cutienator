//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstackedwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstackedwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QStackedWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStackedWidget : QStackedWidget {
  using QStackedWidget::event;
};

//  A QStackedWidget that Python can take functions over in. Every QStackedWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQStackedWidgetCall0)(const void *, QEvent *, int *);
typedef const QSize * (*CuteQStackedWidgetCall1)(const void *, int *);
typedef void (*CuteQStackedWidgetCall2)(const void *, QPaintEvent *, int *);
typedef void (*CuteQStackedWidgetCall3)(const void *, QEvent *, int *);
typedef void (*CuteQStackedWidgetCall4)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQStackedWidgetCall5)(const void *, int *);
typedef void (*CuteQStackedWidgetCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQStackedWidgetCall7)(const void *, int *);
typedef int (*CuteQStackedWidgetCall8)(const void *, int, int *);
typedef bool (*CuteQStackedWidgetCall9)(const void *, int *);
typedef void * (*CuteQStackedWidgetCall10)(const void *, int *);
typedef void (*CuteQStackedWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStackedWidgetCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStackedWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStackedWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQStackedWidgetCall15)(const void *, QWheelEvent *, int *);
typedef void (*CuteQStackedWidgetCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQStackedWidgetCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQStackedWidgetCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQStackedWidgetCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQStackedWidgetCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQStackedWidgetCall21)(const void *, QEvent *, int *);
typedef void (*CuteQStackedWidgetCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQStackedWidgetCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQStackedWidgetCall24)(const void *, QCloseEvent *, int *);
typedef void (*CuteQStackedWidgetCall25)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQStackedWidgetCall26)(const void *, QTabletEvent *, int *);
typedef void (*CuteQStackedWidgetCall27)(const void *, QActionEvent *, int *);
typedef void (*CuteQStackedWidgetCall28)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQStackedWidgetCall29)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQStackedWidgetCall30)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQStackedWidgetCall31)(const void *, QDropEvent *, int *);
typedef void (*CuteQStackedWidgetCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQStackedWidgetCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQStackedWidgetCall34)(const void *, int, int *);
typedef void (*CuteQStackedWidgetCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQStackedWidgetCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQStackedWidgetCall37)(const void *, int *);
typedef void (*CuteQStackedWidgetCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQStackedWidgetCall39)(const void *, int, int *);
typedef bool (*CuteQStackedWidgetCall40)(const void *, bool, int *);
typedef bool (*CuteQStackedWidgetCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQStackedWidgetCall42)(const void *, QTimerEvent *, int *);
typedef void (*CuteQStackedWidgetCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQStackedWidgetCall44)(const void *, QEvent *, int *);
typedef void (*CuteQStackedWidgetCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQStackedWidgetCall46)(const void *, const QMetaMethod *, int *);
class CuteQStackedWidget : public QStackedWidget {
public:
  using QStackedWidget::QStackedWidget;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  bool QStackedWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStackedWidgetCall0 call = reinterpret_cast<CuteQStackedWidgetCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QStackedWidget::event(e);
  }

  //  QSize QFrame::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStackedWidgetCall1 call = reinterpret_cast<CuteQStackedWidgetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFrame::sizeHint();
  }

  //  void QFrame::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStackedWidgetCall2 call = reinterpret_cast<CuteQStackedWidgetCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::paintEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStackedWidgetCall3 call = reinterpret_cast<CuteQStackedWidgetCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStackedWidgetCall4 call = reinterpret_cast<CuteQStackedWidgetCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQStackedWidgetCall5 call = reinterpret_cast<CuteQStackedWidgetCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStackedWidgetCall6 call = reinterpret_cast<CuteQStackedWidgetCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStackedWidgetCall7 call = reinterpret_cast<CuteQStackedWidgetCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStackedWidgetCall8 call = reinterpret_cast<CuteQStackedWidgetCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStackedWidgetCall9 call = reinterpret_cast<CuteQStackedWidgetCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQStackedWidgetCall10 call = reinterpret_cast<CuteQStackedWidgetCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStackedWidgetCall11 call = reinterpret_cast<CuteQStackedWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStackedWidgetCall12 call = reinterpret_cast<CuteQStackedWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQStackedWidgetCall13 call = reinterpret_cast<CuteQStackedWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQStackedWidgetCall14 call = reinterpret_cast<CuteQStackedWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQStackedWidgetCall15 call = reinterpret_cast<CuteQStackedWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQStackedWidgetCall16 call = reinterpret_cast<CuteQStackedWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQStackedWidgetCall17 call = reinterpret_cast<CuteQStackedWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQStackedWidgetCall18 call = reinterpret_cast<CuteQStackedWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQStackedWidgetCall19 call = reinterpret_cast<CuteQStackedWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQStackedWidgetCall20 call = reinterpret_cast<CuteQStackedWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQStackedWidgetCall21 call = reinterpret_cast<CuteQStackedWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQStackedWidgetCall22 call = reinterpret_cast<CuteQStackedWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQStackedWidgetCall23 call = reinterpret_cast<CuteQStackedWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStackedWidgetCall24 call = reinterpret_cast<CuteQStackedWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQStackedWidgetCall25 call = reinterpret_cast<CuteQStackedWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQStackedWidgetCall26 call = reinterpret_cast<CuteQStackedWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQStackedWidgetCall27 call = reinterpret_cast<CuteQStackedWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQStackedWidgetCall28 call = reinterpret_cast<CuteQStackedWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQStackedWidgetCall29 call = reinterpret_cast<CuteQStackedWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQStackedWidgetCall30 call = reinterpret_cast<CuteQStackedWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQStackedWidgetCall31 call = reinterpret_cast<CuteQStackedWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQStackedWidgetCall32 call = reinterpret_cast<CuteQStackedWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQStackedWidgetCall33 call = reinterpret_cast<CuteQStackedWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQStackedWidgetCall34 call = reinterpret_cast<CuteQStackedWidgetCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQStackedWidgetCall35 call = reinterpret_cast<CuteQStackedWidgetCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQStackedWidgetCall36 call = reinterpret_cast<CuteQStackedWidgetCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQStackedWidgetCall37 call = reinterpret_cast<CuteQStackedWidgetCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQStackedWidgetCall38 call = reinterpret_cast<CuteQStackedWidgetCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQStackedWidgetCall39 call = reinterpret_cast<CuteQStackedWidgetCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQStackedWidgetCall40 call = reinterpret_cast<CuteQStackedWidgetCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQStackedWidgetCall41 call = reinterpret_cast<CuteQStackedWidgetCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQStackedWidgetCall42 call = reinterpret_cast<CuteQStackedWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQStackedWidgetCall43 call = reinterpret_cast<CuteQStackedWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQStackedWidgetCall44 call = reinterpret_cast<CuteQStackedWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQStackedWidgetCall45 call = reinterpret_cast<CuteQStackedWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQStackedWidgetCall46 call = reinterpret_cast<CuteQStackedWidgetCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QStackedWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QStackedWidget10metaObjectEv(
    const QStackedWidget *self) {
  return self->metaObject();
}

//  QString QStackedWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStackedWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedWidget::tr(s, c, n));
}

//  QStackedWidget::QStackedWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStackedWidget *ritual_ZN14QStackedWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQStackedWidget(parent);
}

//  QStackedWidget::~QStackedWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidgetD1Ev(QStackedWidget *self) {
  delete self;
}

//  int QStackedWidget::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedWidget9addWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  return self->addWidget(w);
}

//  int QStackedWidget::insertWidget(int index, QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedWidget12insertWidgetEiP7QWidget(
    QStackedWidget *self,
    int index,
    QWidget *w) {
  return self->insertWidget(index, w);
}

//  void QStackedWidget::removeWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget12removeWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  self->removeWidget(w);
}

//  QWidget *QStackedWidget::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedWidget13currentWidgetEv(
    const QStackedWidget *self) {
  return self->currentWidget();
}

//  int QStackedWidget::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget12currentIndexEv(const QStackedWidget *self) {
  return self->currentIndex();
}

//  int QStackedWidget::indexOf(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget7indexOfEPK7QWidget(
    const QStackedWidget *self,
    const QWidget *a0) {
  return self->indexOf(a0);
}

//  QWidget *QStackedWidget::widget(int a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedWidget6widgetEi(
    const QStackedWidget *self,
    int a0) {
  return self->widget(a0);
}

//  int QStackedWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget5countEv(const QStackedWidget *self) {
  return self->count();
}

//  void QStackedWidget::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget15setCurrentIndexEi(
    QStackedWidget *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QStackedWidget::setCurrentWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget16setCurrentWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  self->setCurrentWidget(w);
}

//  bool QStackedWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QStackedWidget5eventEP6QEvent(
    QStackedWidget *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQStackedWidget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStackedWidget(
    QStackedWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStackedWidget *>(self)->take(key, call);
}

//  bool QStackedWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QStackedWidget5eventEP6QEvent(
    QStackedWidget *self,
    QEvent *e) {
  return static_cast<OwnQStackedWidget *>(self)->OwnQStackedWidget::event(e);
}
