//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdockwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdockwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDockWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDockWidget : QDockWidget {
  using QDockWidget::changeEvent;
  using QDockWidget::closeEvent;
  using QDockWidget::paintEvent;
  using QDockWidget::event;
  using QDockWidget::initStyleOption;
};

//  A QDockWidget that Python can take functions over in. Every QDockWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDockWidgetCall0)(const void *, QEvent *, int *);
typedef void (*CuteQDockWidgetCall1)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDockWidgetCall2)(const void *, QPaintEvent *, int *);
typedef bool (*CuteQDockWidgetCall3)(const void *, QEvent *, int *);
typedef void (*CuteQDockWidgetCall4)(const void *, QStyleOptionDockWidget *, int *);
typedef int (*CuteQDockWidgetCall5)(const void *, int *);
typedef void (*CuteQDockWidgetCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQDockWidgetCall7)(const void *, int *);
typedef const QSize * (*CuteQDockWidgetCall8)(const void *, int *);
typedef int (*CuteQDockWidgetCall9)(const void *, int, int *);
typedef bool (*CuteQDockWidgetCall10)(const void *, int *);
typedef void * (*CuteQDockWidgetCall11)(const void *, int *);
typedef void (*CuteQDockWidgetCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDockWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDockWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDockWidgetCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDockWidgetCall16)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDockWidgetCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDockWidgetCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDockWidgetCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDockWidgetCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDockWidgetCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDockWidgetCall22)(const void *, QEvent *, int *);
typedef void (*CuteQDockWidgetCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDockWidgetCall24)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDockWidgetCall25)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQDockWidgetCall26)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDockWidgetCall27)(const void *, QActionEvent *, int *);
typedef void (*CuteQDockWidgetCall28)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDockWidgetCall29)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDockWidgetCall30)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDockWidgetCall31)(const void *, QDropEvent *, int *);
typedef void (*CuteQDockWidgetCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQDockWidgetCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQDockWidgetCall34)(const void *, int, int *);
typedef void (*CuteQDockWidgetCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQDockWidgetCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQDockWidgetCall37)(const void *, int *);
typedef void (*CuteQDockWidgetCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDockWidgetCall39)(const void *, int, int *);
typedef bool (*CuteQDockWidgetCall40)(const void *, bool, int *);
typedef bool (*CuteQDockWidgetCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDockWidgetCall42)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDockWidgetCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQDockWidgetCall44)(const void *, QEvent *, int *);
typedef void (*CuteQDockWidgetCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDockWidgetCall46)(const void *, const QMetaMethod *, int *);
class CuteQDockWidget : public QDockWidget {
public:
  using QDockWidget::QDockWidget;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDockWidget")) {
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
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
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

  //  void QDockWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDockWidgetCall0 call = reinterpret_cast<CuteQDockWidgetCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::changeEvent(event);
  }

  //  void QDockWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDockWidgetCall1 call = reinterpret_cast<CuteQDockWidgetCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::closeEvent(event);
  }

  //  void QDockWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDockWidgetCall2 call = reinterpret_cast<CuteQDockWidgetCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::paintEvent(event);
  }

  //  bool QDockWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDockWidgetCall3 call = reinterpret_cast<CuteQDockWidgetCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QDockWidget::event(event);
  }

  //  void QDockWidget::initStyleOption(QStyleOptionDockWidget *option)
  //      const
  void initStyleOption(QStyleOptionDockWidget *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDockWidgetCall4 call = reinterpret_cast<CuteQDockWidgetCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QDockWidget::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDockWidgetCall5 call = reinterpret_cast<CuteQDockWidgetCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDockWidgetCall6 call = reinterpret_cast<CuteQDockWidgetCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDockWidgetCall7 call = reinterpret_cast<CuteQDockWidgetCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDockWidgetCall8 call = reinterpret_cast<CuteQDockWidgetCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDockWidgetCall9 call = reinterpret_cast<CuteQDockWidgetCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDockWidgetCall10 call = reinterpret_cast<CuteQDockWidgetCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDockWidgetCall11 call = reinterpret_cast<CuteQDockWidgetCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDockWidgetCall12 call = reinterpret_cast<CuteQDockWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDockWidgetCall13 call = reinterpret_cast<CuteQDockWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDockWidgetCall14 call = reinterpret_cast<CuteQDockWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDockWidgetCall15 call = reinterpret_cast<CuteQDockWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDockWidgetCall16 call = reinterpret_cast<CuteQDockWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDockWidgetCall17 call = reinterpret_cast<CuteQDockWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDockWidgetCall18 call = reinterpret_cast<CuteQDockWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDockWidgetCall19 call = reinterpret_cast<CuteQDockWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDockWidgetCall20 call = reinterpret_cast<CuteQDockWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDockWidgetCall21 call = reinterpret_cast<CuteQDockWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDockWidgetCall22 call = reinterpret_cast<CuteQDockWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDockWidgetCall23 call = reinterpret_cast<CuteQDockWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDockWidgetCall24 call = reinterpret_cast<CuteQDockWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDockWidgetCall25 call = reinterpret_cast<CuteQDockWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDockWidgetCall26 call = reinterpret_cast<CuteQDockWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDockWidgetCall27 call = reinterpret_cast<CuteQDockWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDockWidgetCall28 call = reinterpret_cast<CuteQDockWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDockWidgetCall29 call = reinterpret_cast<CuteQDockWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDockWidgetCall30 call = reinterpret_cast<CuteQDockWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDockWidgetCall31 call = reinterpret_cast<CuteQDockWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDockWidgetCall32 call = reinterpret_cast<CuteQDockWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDockWidgetCall33 call = reinterpret_cast<CuteQDockWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQDockWidgetCall34 call = reinterpret_cast<CuteQDockWidgetCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDockWidgetCall35 call = reinterpret_cast<CuteQDockWidgetCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDockWidgetCall36 call = reinterpret_cast<CuteQDockWidgetCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDockWidgetCall37 call = reinterpret_cast<CuteQDockWidgetCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDockWidgetCall38 call = reinterpret_cast<CuteQDockWidgetCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDockWidgetCall39 call = reinterpret_cast<CuteQDockWidgetCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDockWidgetCall40 call = reinterpret_cast<CuteQDockWidgetCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDockWidgetCall41 call = reinterpret_cast<CuteQDockWidgetCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDockWidgetCall42 call = reinterpret_cast<CuteQDockWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDockWidgetCall43 call = reinterpret_cast<CuteQDockWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDockWidgetCall44 call = reinterpret_cast<CuteQDockWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDockWidgetCall45 call = reinterpret_cast<CuteQDockWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDockWidgetCall46 call = reinterpret_cast<CuteQDockWidgetCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDockWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QDockWidget10metaObjectEv(
    const QDockWidget *self) {
  return self->metaObject();
}

//  QString QDockWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QDockWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDockWidget::tr(s, c, n));
}

//  QDockWidget::QDockWidget(const QString &title, QWidget *parent,
//      Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN11QDockWidgetC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *title,
    QWidget *parent,
    int flags) {
  return new CuteQDockWidget(
      *title,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDockWidget::QDockWidget(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN11QDockWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQDockWidget(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDockWidget::~QDockWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidgetD1Ev(QDockWidget *self) {
  delete self;
}

//  QWidget *QDockWidget::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QDockWidget6widgetEv(const QDockWidget *self) {
  return self->widget();
}

//  void QDockWidget::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget9setWidgetEP7QWidget(
    QDockWidget *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  void QDockWidget::setFeatures(DockWidgetFeatures features)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget11setFeaturesE6QFlagsINS_17DockWidgetFeatureEE(
    QDockWidget *self,
    int features) {
  self->setFeatures(
      QFlags<QDockWidget::DockWidgetFeature>::fromInt(features));
}

//  DockWidgetFeatures QDockWidget::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDockWidget8featuresEv(const QDockWidget *self) {
  return static_cast<int>(self->features().toInt());
}

//  void QDockWidget::setFloating(bool floating)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget11setFloatingEb(
    QDockWidget *self,
    bool floating) {
  self->setFloating(floating);
}

//  bool QDockWidget::isFloating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDockWidget10isFloatingEv(const QDockWidget *self) {
  return self->isFloating();
}

//  void QDockWidget::setAllowedAreas(Qt::DockWidgetAreas areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget15setAllowedAreasE6QFlagsIN2Qt14DockWidgetAreaEE(
    QDockWidget *self,
    int areas) {
  self->setAllowedAreas(QFlags<Qt::DockWidgetArea>::fromInt(areas));
}

//  Qt::DockWidgetAreas QDockWidget::allowedAreas() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDockWidget12allowedAreasEv(const QDockWidget *self) {
  return static_cast<int>(self->allowedAreas().toInt());
}

//  void QDockWidget::setTitleBarWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget17setTitleBarWidgetEP7QWidget(
    QDockWidget *self,
    QWidget *widget) {
  self->setTitleBarWidget(widget);
}

//  QWidget *QDockWidget::titleBarWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QDockWidget14titleBarWidgetEv(const QDockWidget *self) {
  return self->titleBarWidget();
}

//  void QDockWidget::setDockLocation(Qt::DockWidgetArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDockWidget15setDockLocationEN2Qt14DockWidgetAreaE(
    QDockWidget *self,
    Qt::DockWidgetArea area) {
  self->setDockLocation(area);
}

//  Qt::DockWidgetArea QDockWidget::dockLocation() const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QDockWidget12dockLocationEv(
    const QDockWidget *self) {
  return self->dockLocation();
}

//  bool QDockWidget::isAreaAllowed(Qt::DockWidgetArea area) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDockWidget13isAreaAllowedEN2Qt14DockWidgetAreaE(
    const QDockWidget *self,
    Qt::DockWidgetArea area) {
  return self->isAreaAllowed(area);
}

//  QDebug operator<<(QDebug dbg, const QDockWidget *dockWidget)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK11QDockWidget(
    const QDebug *dbg,
    const QDockWidget *dockWidget) {
  return new QDebug(operator<<(*dbg, dockWidget));
}

//  QAction *QDockWidget::toggleViewAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK11QDockWidget16toggleViewActionEv(
    const QDockWidget *self) {
  return self->toggleViewAction();
}

//  a Python function taken by a CuteQDockWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDockWidget(
    QDockWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDockWidget *>(self)->take(key, call);
}

//  void QDockWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QDockWidget11changeEventEP6QEvent(
    QDockWidget *self,
    QEvent *event) {
  static_cast<OwnQDockWidget *>(self)->OwnQDockWidget::changeEvent(event);
}

//  void QDockWidget::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QDockWidget10closeEventEP11QCloseEvent(
    QDockWidget *self,
    QCloseEvent *event) {
  static_cast<OwnQDockWidget *>(self)->OwnQDockWidget::closeEvent(event);
}

//  void QDockWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QDockWidget10paintEventEP11QPaintEvent(
    QDockWidget *self,
    QPaintEvent *event) {
  static_cast<OwnQDockWidget *>(self)->OwnQDockWidget::paintEvent(event);
}

//  bool QDockWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QDockWidget5eventEP6QEvent(
    QDockWidget *self,
    QEvent *event) {
  return static_cast<OwnQDockWidget *>(self)->OwnQDockWidget::event(event);
}

//  void QDockWidget::initStyleOption(QStyleOptionDockWidget *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDockWidget(
    const QDockWidget *self,
    QStyleOptionDockWidget *option) {
  static_cast<const OwnQDockWidget *>(self)->OwnQDockWidget::initStyleOption(
      option);
}
