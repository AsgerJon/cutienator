//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtabwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtabwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTabWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTabWidget : QTabWidget {
  using QTabWidget::tabInserted;
  using QTabWidget::tabRemoved;
  using QTabWidget::showEvent;
  using QTabWidget::resizeEvent;
  using QTabWidget::keyPressEvent;
  using QTabWidget::paintEvent;
  using QTabWidget::changeEvent;
  using QTabWidget::event;
  using QTabWidget::initStyleOption;
};

//  A QTabWidget that Python can take functions over in. Every QTabWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQTabWidgetCall0)(const void *, int *);
typedef const QSize * (*CuteQTabWidgetCall1)(const void *, int *);
typedef int (*CuteQTabWidgetCall2)(const void *, int, int *);
typedef bool (*CuteQTabWidgetCall3)(const void *, int *);
typedef void (*CuteQTabWidgetCall4)(const void *, int, int *);
typedef void (*CuteQTabWidgetCall5)(const void *, int, int *);
typedef void (*CuteQTabWidgetCall6)(const void *, QShowEvent *, int *);
typedef void (*CuteQTabWidgetCall7)(const void *, QResizeEvent *, int *);
typedef void (*CuteQTabWidgetCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTabWidgetCall9)(const void *, QPaintEvent *, int *);
typedef void (*CuteQTabWidgetCall10)(const void *, QEvent *, int *);
typedef bool (*CuteQTabWidgetCall11)(const void *, QEvent *, int *);
typedef void (*CuteQTabWidgetCall12)(const void *, QStyleOptionTabWidgetFrame *, int *);
typedef int (*CuteQTabWidgetCall13)(const void *, int *);
typedef void (*CuteQTabWidgetCall14)(const void *, bool, int *);
typedef void * (*CuteQTabWidgetCall15)(const void *, int *);
typedef void (*CuteQTabWidgetCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTabWidgetCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTabWidgetCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTabWidgetCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTabWidgetCall20)(const void *, QWheelEvent *, int *);
typedef void (*CuteQTabWidgetCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTabWidgetCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTabWidgetCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTabWidgetCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTabWidgetCall25)(const void *, QEvent *, int *);
typedef void (*CuteQTabWidgetCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTabWidgetCall27)(const void *, QCloseEvent *, int *);
typedef void (*CuteQTabWidgetCall28)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQTabWidgetCall29)(const void *, QTabletEvent *, int *);
typedef void (*CuteQTabWidgetCall30)(const void *, QActionEvent *, int *);
typedef void (*CuteQTabWidgetCall31)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQTabWidgetCall32)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQTabWidgetCall33)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQTabWidgetCall34)(const void *, QDropEvent *, int *);
typedef void (*CuteQTabWidgetCall35)(const void *, QHideEvent *, int *);
typedef int (*CuteQTabWidgetCall36)(const void *, int, int *);
typedef void (*CuteQTabWidgetCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQTabWidgetCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQTabWidgetCall39)(const void *, int *);
typedef void (*CuteQTabWidgetCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQTabWidgetCall41)(const void *, int, int *);
typedef bool (*CuteQTabWidgetCall42)(const void *, bool, int *);
typedef bool (*CuteQTabWidgetCall43)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTabWidgetCall44)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTabWidgetCall45)(const void *, QChildEvent *, int *);
typedef void (*CuteQTabWidgetCall46)(const void *, QEvent *, int *);
typedef void (*CuteQTabWidgetCall47)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTabWidgetCall48)(const void *, const QMetaMethod *, int *);
class CuteQTabWidget : public QTabWidget {
public:
  using QTabWidget::QTabWidget;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTabWidget11tabInsertedEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTabWidget10tabRemovedEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QTabWidget15initStyleOptionEP26QStyleOptionTabWidgetFrame")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
    return false;
  }

  //  QSize QTabWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTabWidgetCall0 call = reinterpret_cast<CuteQTabWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTabWidget::sizeHint();
  }

  //  QSize QTabWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTabWidgetCall1 call = reinterpret_cast<CuteQTabWidgetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTabWidget::minimumSizeHint();
  }

  //  int QTabWidget::heightForWidth(int width) const
  int heightForWidth(int width) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTabWidgetCall2 call = reinterpret_cast<CuteQTabWidgetCall2>(taken[2]);
      int given = call(this, width, &handled);
      if (handled) return given;
    }
    return QTabWidget::heightForWidth(width);
  }

  //  bool QTabWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTabWidgetCall3 call = reinterpret_cast<CuteQTabWidgetCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTabWidget::hasHeightForWidth();
  }

  //  void QTabWidget::tabInserted(int index)
  void tabInserted(int index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTabWidgetCall4 call = reinterpret_cast<CuteQTabWidgetCall4>(taken[4]);
      call(this, index, &handled);
      if (handled) return;
    }
    QTabWidget::tabInserted(index);
  }

  //  void QTabWidget::tabRemoved(int index)
  void tabRemoved(int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTabWidgetCall5 call = reinterpret_cast<CuteQTabWidgetCall5>(taken[5]);
      call(this, index, &handled);
      if (handled) return;
    }
    QTabWidget::tabRemoved(index);
  }

  //  void QTabWidget::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTabWidgetCall6 call = reinterpret_cast<CuteQTabWidgetCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabWidget::showEvent(a0);
  }

  //  void QTabWidget::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTabWidgetCall7 call = reinterpret_cast<CuteQTabWidgetCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabWidget::resizeEvent(a0);
  }

  //  void QTabWidget::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTabWidgetCall8 call = reinterpret_cast<CuteQTabWidgetCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabWidget::keyPressEvent(a0);
  }

  //  void QTabWidget::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTabWidgetCall9 call = reinterpret_cast<CuteQTabWidgetCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabWidget::paintEvent(a0);
  }

  //  void QTabWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTabWidgetCall10 call = reinterpret_cast<CuteQTabWidgetCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabWidget::changeEvent(a0);
  }

  //  bool QTabWidget::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTabWidgetCall11 call = reinterpret_cast<CuteQTabWidgetCall11>(taken[11]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QTabWidget::event(a0);
  }

  //  void QTabWidget::initStyleOption(QStyleOptionTabWidgetFrame *option)
  //      const
  void initStyleOption(QStyleOptionTabWidgetFrame *option) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTabWidgetCall12 call = reinterpret_cast<CuteQTabWidgetCall12>(taken[12]);
      call(this, option, &handled);
      if (handled) return;
    }
    QTabWidget::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTabWidgetCall13 call = reinterpret_cast<CuteQTabWidgetCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTabWidgetCall14 call = reinterpret_cast<CuteQTabWidgetCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTabWidgetCall15 call = reinterpret_cast<CuteQTabWidgetCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTabWidgetCall16 call = reinterpret_cast<CuteQTabWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTabWidgetCall17 call = reinterpret_cast<CuteQTabWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTabWidgetCall18 call = reinterpret_cast<CuteQTabWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTabWidgetCall19 call = reinterpret_cast<CuteQTabWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTabWidgetCall20 call = reinterpret_cast<CuteQTabWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTabWidgetCall21 call = reinterpret_cast<CuteQTabWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTabWidgetCall22 call = reinterpret_cast<CuteQTabWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTabWidgetCall23 call = reinterpret_cast<CuteQTabWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTabWidgetCall24 call = reinterpret_cast<CuteQTabWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTabWidgetCall25 call = reinterpret_cast<CuteQTabWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTabWidgetCall26 call = reinterpret_cast<CuteQTabWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTabWidgetCall27 call = reinterpret_cast<CuteQTabWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTabWidgetCall28 call = reinterpret_cast<CuteQTabWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTabWidgetCall29 call = reinterpret_cast<CuteQTabWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTabWidgetCall30 call = reinterpret_cast<CuteQTabWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTabWidgetCall31 call = reinterpret_cast<CuteQTabWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTabWidgetCall32 call = reinterpret_cast<CuteQTabWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTabWidgetCall33 call = reinterpret_cast<CuteQTabWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTabWidgetCall34 call = reinterpret_cast<CuteQTabWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQTabWidgetCall35 call = reinterpret_cast<CuteQTabWidgetCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQTabWidgetCall36 call = reinterpret_cast<CuteQTabWidgetCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQTabWidgetCall37 call = reinterpret_cast<CuteQTabWidgetCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQTabWidgetCall38 call = reinterpret_cast<CuteQTabWidgetCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQTabWidgetCall39 call = reinterpret_cast<CuteQTabWidgetCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQTabWidgetCall40 call = reinterpret_cast<CuteQTabWidgetCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQTabWidgetCall41 call = reinterpret_cast<CuteQTabWidgetCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTabWidgetCall42 call = reinterpret_cast<CuteQTabWidgetCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQTabWidgetCall43 call = reinterpret_cast<CuteQTabWidgetCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTabWidgetCall44 call = reinterpret_cast<CuteQTabWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQTabWidgetCall45 call = reinterpret_cast<CuteQTabWidgetCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTabWidgetCall46 call = reinterpret_cast<CuteQTabWidgetCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTabWidgetCall47 call = reinterpret_cast<CuteQTabWidgetCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQTabWidgetCall48 call = reinterpret_cast<CuteQTabWidgetCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTabWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTabWidget10metaObjectEv(
    const QTabWidget *self) {
  return self->metaObject();
}

//  QString QTabWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTabWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTabWidget::tr(s, c, n));
}

//  QTabWidget::QTabWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTabWidget *ritual_ZN10QTabWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQTabWidget(parent);
}

//  QTabWidget::~QTabWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidgetD1Ev(QTabWidget *self) {
  delete self;
}

//  int QTabWidget::addTab(QWidget *widget, const QString &a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget6addTabEP7QWidgetRK7QString(
    QTabWidget *self,
    QWidget *widget,
    const QString *a1) {
  return self->addTab(widget, *a1);
}

//  int QTabWidget::addTab(QWidget *widget, const QIcon &icon, const QString
//      &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget6addTabEP7QWidgetRK5QIconRK7QString(
    QTabWidget *self,
    QWidget *widget,
    const QIcon *icon,
    const QString *label) {
  return self->addTab(widget, *icon, *label);
}

//  int QTabWidget::insertTab(int index, QWidget *widget, const QString &a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK7QString(
    QTabWidget *self,
    int index,
    QWidget *widget,
    const QString *a2) {
  return self->insertTab(index, widget, *a2);
}

//  int QTabWidget::insertTab(int index, QWidget *widget, const QIcon &icon,
//      const QString &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK5QIconRK7QString(
    QTabWidget *self,
    int index,
    QWidget *widget,
    const QIcon *icon,
    const QString *label) {
  return self->insertTab(index, widget, *icon, *label);
}

//  void QTabWidget::removeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget9removeTabEi(QTabWidget *self, int index) {
  self->removeTab(index);
}

//  bool QTabWidget::isTabEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12isTabEnabledEi(
    const QTabWidget *self,
    int index) {
  return self->isTabEnabled(index);
}

//  void QTabWidget::setTabEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabEnabledEib(
    QTabWidget *self,
    int index,
    bool enabled) {
  self->setTabEnabled(index, enabled);
}

//  bool QTabWidget::isTabVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12isTabVisibleEi(
    const QTabWidget *self,
    int index) {
  return self->isTabVisible(index);
}

//  void QTabWidget::setTabVisible(int index, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabVisibleEib(
    QTabWidget *self,
    int index,
    bool visible) {
  self->setTabVisible(index, visible);
}

//  QString QTabWidget::tabText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget7tabTextEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabText(index));
}

//  void QTabWidget::setTabText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setTabTextEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *text) {
  self->setTabText(index, *text);
}

//  QIcon QTabWidget::tabIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK10QTabWidget7tabIconEi(const QTabWidget *self, int index) {
  return new QIcon(self->tabIcon(index));
}

//  void QTabWidget::setTabIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setTabIconEiRK5QIcon(
    QTabWidget *self,
    int index,
    const QIcon *icon) {
  self->setTabIcon(index, *icon);
}

//  void QTabWidget::setTabToolTip(int index, const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabToolTipEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *tip) {
  self->setTabToolTip(index, *tip);
}

//  QString QTabWidget::tabToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget10tabToolTipEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabToolTip(index));
}

//  void QTabWidget::setTabWhatsThis(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setTabWhatsThisEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *text) {
  self->setTabWhatsThis(index, *text);
}

//  QString QTabWidget::tabWhatsThis(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget12tabWhatsThisEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabWhatsThis(index));
}

//  int QTabWidget::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget12currentIndexEv(const QTabWidget *self) {
  return self->currentIndex();
}

//  QWidget *QTabWidget::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget13currentWidgetEv(const QTabWidget *self) {
  return self->currentWidget();
}

//  QWidget *QTabWidget::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget6widgetEi(const QTabWidget *self, int index) {
  return self->widget(index);
}

//  int QTabWidget::indexOf(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget7indexOfEPK7QWidget(
    const QTabWidget *self,
    const QWidget *widget) {
  return self->indexOf(widget);
}

//  int QTabWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget5countEv(const QTabWidget *self) {
  return self->count();
}

//  TabPosition QTabWidget::tabPosition() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK10QTabWidget11tabPositionEv(
    const QTabWidget *self) {
  return self->tabPosition();
}

//  void QTabWidget::setTabPosition(TabPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget14setTabPositionENS_11TabPositionE(
    QTabWidget *self,
    QTabWidget::TabPosition position) {
  self->setTabPosition(position);
}

//  bool QTabWidget::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12tabsClosableEv(const QTabWidget *self) {
  return self->tabsClosable();
}

//  void QTabWidget::setTabsClosable(bool closeable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setTabsClosableEb(
    QTabWidget *self,
    bool closeable) {
  self->setTabsClosable(closeable);
}

//  bool QTabWidget::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget9isMovableEv(const QTabWidget *self) {
  return self->isMovable();
}

//  void QTabWidget::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setMovableEb(QTabWidget *self, bool movable) {
  self->setMovable(movable);
}

//  TabShape QTabWidget::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK10QTabWidget8tabShapeEv(
    const QTabWidget *self) {
  return self->tabShape();
}

//  void QTabWidget::setTabShape(TabShape s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11setTabShapeENS_8TabShapeE(
    QTabWidget *self,
    QTabWidget::TabShape s) {
  self->setTabShape(s);
}

//  QSize QTabWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget8sizeHintEv(const QTabWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QTabWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget15minimumSizeHintEv(const QTabWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QTabWidget::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget14heightForWidthEi(
    const QTabWidget *self,
    int width) {
  return self->heightForWidth(width);
}

//  bool QTabWidget::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget17hasHeightForWidthEv(const QTabWidget *self) {
  return self->hasHeightForWidth();
}

//  void QTabWidget::setCornerWidget(QWidget *w, Qt::Corner corner)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setCornerWidgetEP7QWidgetN2Qt6CornerE(
    QTabWidget *self,
    QWidget *w,
    Qt::Corner corner) {
  self->setCornerWidget(w, corner);
}

//  QWidget *QTabWidget::cornerWidget(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget12cornerWidgetEN2Qt6CornerE(
    const QTabWidget *self,
    Qt::Corner corner) {
  return self->cornerWidget(corner);
}

//  Qt::TextElideMode QTabWidget::elideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK10QTabWidget9elideModeEv(
    const QTabWidget *self) {
  return self->elideMode();
}

//  void QTabWidget::setElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget12setElideModeEN2Qt13TextElideModeE(
    QTabWidget *self,
    Qt::TextElideMode mode) {
  self->setElideMode(mode);
}

//  QSize QTabWidget::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget8iconSizeEv(const QTabWidget *self) {
  return new QSize(self->iconSize());
}

//  void QTabWidget::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11setIconSizeERK5QSize(
    QTabWidget *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  bool QTabWidget::usesScrollButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget17usesScrollButtonsEv(const QTabWidget *self) {
  return self->usesScrollButtons();
}

//  void QTabWidget::setUsesScrollButtons(bool useButtons)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget20setUsesScrollButtonsEb(
    QTabWidget *self,
    bool useButtons) {
  self->setUsesScrollButtons(useButtons);
}

//  bool QTabWidget::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12documentModeEv(const QTabWidget *self) {
  return self->documentMode();
}

//  void QTabWidget::setDocumentMode(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setDocumentModeEb(QTabWidget *self, bool set) {
  self->setDocumentMode(set);
}

//  bool QTabWidget::tabBarAutoHide() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget14tabBarAutoHideEv(const QTabWidget *self) {
  return self->tabBarAutoHide();
}

//  void QTabWidget::setTabBarAutoHide(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget17setTabBarAutoHideEb(
    QTabWidget *self,
    bool enabled) {
  self->setTabBarAutoHide(enabled);
}

//  void QTabWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget5clearEv(QTabWidget *self) {
  self->clear();
}

//  QTabBar *QTabWidget::tabBar() const
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZNK10QTabWidget6tabBarEv(const QTabWidget *self) {
  return self->tabBar();
}

//  void QTabWidget::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setCurrentIndexEi(QTabWidget *self, int index) {
  self->setCurrentIndex(index);
}

//  void QTabWidget::setCurrentWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget16setCurrentWidgetEP7QWidget(
    QTabWidget *self,
    QWidget *widget) {
  self->setCurrentWidget(widget);
}

//  void QTabWidget::tabInserted(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11tabInsertedEi(QTabWidget *self, int index) {
  self->tabInserted(index);
}

//  void QTabWidget::tabRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10tabRemovedEi(QTabWidget *self, int index) {
  self->tabRemoved(index);
}

//  void QTabWidget::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget9showEventEP10QShowEvent(
    QTabWidget *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QTabWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11resizeEventEP12QResizeEvent(
    QTabWidget *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QTabWidget::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13keyPressEventEP9QKeyEvent(
    QTabWidget *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QTabWidget::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10paintEventEP11QPaintEvent(
    QTabWidget *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QTabWidget::setTabBar(QTabBar *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget9setTabBarEP7QTabBar(
    QTabWidget *self,
    QTabBar *a0) {
  self->setTabBar(a0);
}

//  void QTabWidget::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11changeEventEP6QEvent(
    QTabWidget *self,
    QEvent *a0) {
  self->changeEvent(a0);
}

//  bool QTabWidget::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTabWidget5eventEP6QEvent(QTabWidget *self, QEvent *a0) {
  return self->event(a0);
}

//  void QTabWidget::initStyleOption(QStyleOptionTabWidgetFrame *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QTabWidget15initStyleOptionEP26QStyleOptionTabWidgetFrame(
    const QTabWidget *self,
    QStyleOptionTabWidgetFrame *option) {
  self->initStyleOption(option);
}

//  void QTabWidget::setUpLayout(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11setUpLayoutEb(QTabWidget *self, bool a0) {
  self->setUpLayout(a0);
}

//  a Python function taken by a CuteQTabWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTabWidget(QTabWidget *self, const char *key, void *call) {
  return static_cast<CuteQTabWidget *>(self)->take(key, call);
}

//  QSize QTabWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QTabWidget8sizeHintEv(const QTabWidget *self) {
  return new QSize(self->QTabWidget::sizeHint());
}

//  QSize QTabWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QTabWidget15minimumSizeHintEv(
    const QTabWidget *self) {
  return new QSize(self->QTabWidget::minimumSizeHint());
}

//  int QTabWidget::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTabWidget14heightForWidthEi(
    const QTabWidget *self,
    int width) {
  return self->QTabWidget::heightForWidth(width);
}

//  bool QTabWidget::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QTabWidget17hasHeightForWidthEv(
    const QTabWidget *self) {
  return self->QTabWidget::hasHeightForWidth();
}

//  void QTabWidget::tabInserted(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget11tabInsertedEi(QTabWidget *self, int index) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::tabInserted(index);
}

//  void QTabWidget::tabRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget10tabRemovedEi(QTabWidget *self, int index) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::tabRemoved(index);
}

//  void QTabWidget::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget9showEventEP10QShowEvent(
    QTabWidget *self,
    QShowEvent *a0) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::showEvent(a0);
}

//  void QTabWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget11resizeEventEP12QResizeEvent(
    QTabWidget *self,
    QResizeEvent *a0) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::resizeEvent(a0);
}

//  void QTabWidget::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget13keyPressEventEP9QKeyEvent(
    QTabWidget *self,
    QKeyEvent *a0) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::keyPressEvent(a0);
}

//  void QTabWidget::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget10paintEventEP11QPaintEvent(
    QTabWidget *self,
    QPaintEvent *a0) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::paintEvent(a0);
}

//  void QTabWidget::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTabWidget11changeEventEP6QEvent(
    QTabWidget *self,
    QEvent *a0) {
  static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::changeEvent(a0);
}

//  bool QTabWidget::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTabWidget5eventEP6QEvent(QTabWidget *self, QEvent *a0) {
  return static_cast<OwnQTabWidget *>(self)->OwnQTabWidget::event(a0);
}

//  void QTabWidget::initStyleOption(QStyleOptionTabWidgetFrame *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QTabWidget15initStyleOptionEP26QStyleOptionTabWidgetFrame(
    const QTabWidget *self,
    QStyleOptionTabWidgetFrame *option) {
  static_cast<const OwnQTabWidget *>(self)->OwnQTabWidget::initStyleOption(
      option);
}
