//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmdisubwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmdisubwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMdiSubWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMdiSubWindow : QMdiSubWindow {
  using QMdiSubWindow::eventFilter;
  using QMdiSubWindow::event;
  using QMdiSubWindow::showEvent;
  using QMdiSubWindow::hideEvent;
  using QMdiSubWindow::changeEvent;
  using QMdiSubWindow::closeEvent;
  using QMdiSubWindow::leaveEvent;
  using QMdiSubWindow::resizeEvent;
  using QMdiSubWindow::timerEvent;
  using QMdiSubWindow::moveEvent;
  using QMdiSubWindow::paintEvent;
  using QMdiSubWindow::mousePressEvent;
  using QMdiSubWindow::mouseDoubleClickEvent;
  using QMdiSubWindow::mouseReleaseEvent;
  using QMdiSubWindow::mouseMoveEvent;
  using QMdiSubWindow::keyPressEvent;
  using QMdiSubWindow::contextMenuEvent;
  using QMdiSubWindow::focusInEvent;
  using QMdiSubWindow::focusOutEvent;
  using QMdiSubWindow::childEvent;
};

//  A QMdiSubWindow that Python can take functions over in. Every QMdiSubWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQMdiSubWindowCall0)(const void *, int *);
typedef const QSize * (*CuteQMdiSubWindowCall1)(const void *, int *);
typedef bool (*CuteQMdiSubWindowCall2)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQMdiSubWindowCall3)(const void *, QEvent *, int *);
typedef void (*CuteQMdiSubWindowCall4)(const void *, QShowEvent *, int *);
typedef void (*CuteQMdiSubWindowCall5)(const void *, QHideEvent *, int *);
typedef void (*CuteQMdiSubWindowCall6)(const void *, QEvent *, int *);
typedef void (*CuteQMdiSubWindowCall7)(const void *, QCloseEvent *, int *);
typedef void (*CuteQMdiSubWindowCall8)(const void *, QEvent *, int *);
typedef void (*CuteQMdiSubWindowCall9)(const void *, QResizeEvent *, int *);
typedef void (*CuteQMdiSubWindowCall10)(const void *, QTimerEvent *, int *);
typedef void (*CuteQMdiSubWindowCall11)(const void *, QMoveEvent *, int *);
typedef void (*CuteQMdiSubWindowCall12)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMdiSubWindowCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiSubWindowCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiSubWindowCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiSubWindowCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiSubWindowCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMdiSubWindowCall18)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQMdiSubWindowCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMdiSubWindowCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMdiSubWindowCall21)(const void *, QChildEvent *, int *);
typedef int (*CuteQMdiSubWindowCall22)(const void *, int *);
typedef void (*CuteQMdiSubWindowCall23)(const void *, bool, int *);
typedef int (*CuteQMdiSubWindowCall24)(const void *, int, int *);
typedef bool (*CuteQMdiSubWindowCall25)(const void *, int *);
typedef void * (*CuteQMdiSubWindowCall26)(const void *, int *);
typedef void (*CuteQMdiSubWindowCall27)(const void *, QWheelEvent *, int *);
typedef void (*CuteQMdiSubWindowCall28)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMdiSubWindowCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMdiSubWindowCall30)(const void *, QTabletEvent *, int *);
typedef void (*CuteQMdiSubWindowCall31)(const void *, QActionEvent *, int *);
typedef void (*CuteQMdiSubWindowCall32)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQMdiSubWindowCall33)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQMdiSubWindowCall34)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQMdiSubWindowCall35)(const void *, QDropEvent *, int *);
typedef int (*CuteQMdiSubWindowCall36)(const void *, int, int *);
typedef void (*CuteQMdiSubWindowCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQMdiSubWindowCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQMdiSubWindowCall39)(const void *, int *);
typedef void (*CuteQMdiSubWindowCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMdiSubWindowCall41)(const void *, int, int *);
typedef bool (*CuteQMdiSubWindowCall42)(const void *, bool, int *);
typedef void (*CuteQMdiSubWindowCall43)(const void *, QEvent *, int *);
typedef void (*CuteQMdiSubWindowCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQMdiSubWindowCall45)(const void *, const QMetaMethod *, int *);
class CuteQMdiSubWindow : public QMdiSubWindow {
public:
  using QMdiSubWindow::QMdiSubWindow;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    return false;
  }

  //  QSize QMdiSubWindow::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdiSubWindowCall0 call = reinterpret_cast<CuteQMdiSubWindowCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMdiSubWindow::sizeHint();
  }

  //  QSize QMdiSubWindow::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMdiSubWindowCall1 call = reinterpret_cast<CuteQMdiSubWindowCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMdiSubWindow::minimumSizeHint();
  }

  //  bool QMdiSubWindow::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMdiSubWindowCall2 call = reinterpret_cast<CuteQMdiSubWindowCall2>(taken[2]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QMdiSubWindow::eventFilter(object, event);
  }

  //  bool QMdiSubWindow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMdiSubWindowCall3 call = reinterpret_cast<CuteQMdiSubWindowCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QMdiSubWindow::event(event);
  }

  //  void QMdiSubWindow::showEvent(QShowEvent *showEvent)
  void showEvent(QShowEvent *showEvent) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMdiSubWindowCall4 call = reinterpret_cast<CuteQMdiSubWindowCall4>(taken[4]);
      call(this, showEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::showEvent(showEvent);
  }

  //  void QMdiSubWindow::hideEvent(QHideEvent *hideEvent)
  void hideEvent(QHideEvent *hideEvent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMdiSubWindowCall5 call = reinterpret_cast<CuteQMdiSubWindowCall5>(taken[5]);
      call(this, hideEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::hideEvent(hideEvent);
  }

  //  void QMdiSubWindow::changeEvent(QEvent *changeEvent)
  void changeEvent(QEvent *changeEvent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMdiSubWindowCall6 call = reinterpret_cast<CuteQMdiSubWindowCall6>(taken[6]);
      call(this, changeEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::changeEvent(changeEvent);
  }

  //  void QMdiSubWindow::closeEvent(QCloseEvent *closeEvent)
  void closeEvent(QCloseEvent *closeEvent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMdiSubWindowCall7 call = reinterpret_cast<CuteQMdiSubWindowCall7>(taken[7]);
      call(this, closeEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::closeEvent(closeEvent);
  }

  //  void QMdiSubWindow::leaveEvent(QEvent *leaveEvent)
  void leaveEvent(QEvent *leaveEvent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMdiSubWindowCall8 call = reinterpret_cast<CuteQMdiSubWindowCall8>(taken[8]);
      call(this, leaveEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::leaveEvent(leaveEvent);
  }

  //  void QMdiSubWindow::resizeEvent(QResizeEvent *resizeEvent)
  void resizeEvent(QResizeEvent *resizeEvent) override {
    if (taken[9]) {
      int handled = 0;
      CuteQMdiSubWindowCall9 call = reinterpret_cast<CuteQMdiSubWindowCall9>(taken[9]);
      call(this, resizeEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::resizeEvent(resizeEvent);
  }

  //  void QMdiSubWindow::timerEvent(QTimerEvent *timerEvent)
  void timerEvent(QTimerEvent *timerEvent) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMdiSubWindowCall10 call = reinterpret_cast<CuteQMdiSubWindowCall10>(taken[10]);
      call(this, timerEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::timerEvent(timerEvent);
  }

  //  void QMdiSubWindow::moveEvent(QMoveEvent *moveEvent)
  void moveEvent(QMoveEvent *moveEvent) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMdiSubWindowCall11 call = reinterpret_cast<CuteQMdiSubWindowCall11>(taken[11]);
      call(this, moveEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::moveEvent(moveEvent);
  }

  //  void QMdiSubWindow::paintEvent(QPaintEvent *paintEvent)
  void paintEvent(QPaintEvent *paintEvent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMdiSubWindowCall12 call = reinterpret_cast<CuteQMdiSubWindowCall12>(taken[12]);
      call(this, paintEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::paintEvent(paintEvent);
  }

  //  void QMdiSubWindow::mousePressEvent(QMouseEvent *mouseEvent)
  void mousePressEvent(QMouseEvent *mouseEvent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMdiSubWindowCall13 call = reinterpret_cast<CuteQMdiSubWindowCall13>(taken[13]);
      call(this, mouseEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::mousePressEvent(mouseEvent);
  }

  //  void QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent *mouseEvent)
  void mouseDoubleClickEvent(QMouseEvent *mouseEvent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMdiSubWindowCall14 call = reinterpret_cast<CuteQMdiSubWindowCall14>(taken[14]);
      call(this, mouseEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::mouseDoubleClickEvent(mouseEvent);
  }

  //  void QMdiSubWindow::mouseReleaseEvent(QMouseEvent *mouseEvent)
  void mouseReleaseEvent(QMouseEvent *mouseEvent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQMdiSubWindowCall15 call = reinterpret_cast<CuteQMdiSubWindowCall15>(taken[15]);
      call(this, mouseEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::mouseReleaseEvent(mouseEvent);
  }

  //  void QMdiSubWindow::mouseMoveEvent(QMouseEvent *mouseEvent)
  void mouseMoveEvent(QMouseEvent *mouseEvent) override {
    if (taken[16]) {
      int handled = 0;
      CuteQMdiSubWindowCall16 call = reinterpret_cast<CuteQMdiSubWindowCall16>(taken[16]);
      call(this, mouseEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::mouseMoveEvent(mouseEvent);
  }

  //  void QMdiSubWindow::keyPressEvent(QKeyEvent *keyEvent)
  void keyPressEvent(QKeyEvent *keyEvent) override {
    if (taken[17]) {
      int handled = 0;
      CuteQMdiSubWindowCall17 call = reinterpret_cast<CuteQMdiSubWindowCall17>(taken[17]);
      call(this, keyEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::keyPressEvent(keyEvent);
  }

  //  void QMdiSubWindow::contextMenuEvent(QContextMenuEvent
  //      *contextMenuEvent)
  void contextMenuEvent(QContextMenuEvent *contextMenuEvent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQMdiSubWindowCall18 call = reinterpret_cast<CuteQMdiSubWindowCall18>(taken[18]);
      call(this, contextMenuEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::contextMenuEvent(contextMenuEvent);
  }

  //  void QMdiSubWindow::focusInEvent(QFocusEvent *focusInEvent)
  void focusInEvent(QFocusEvent *focusInEvent) override {
    if (taken[19]) {
      int handled = 0;
      CuteQMdiSubWindowCall19 call = reinterpret_cast<CuteQMdiSubWindowCall19>(taken[19]);
      call(this, focusInEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::focusInEvent(focusInEvent);
  }

  //  void QMdiSubWindow::focusOutEvent(QFocusEvent *focusOutEvent)
  void focusOutEvent(QFocusEvent *focusOutEvent) override {
    if (taken[20]) {
      int handled = 0;
      CuteQMdiSubWindowCall20 call = reinterpret_cast<CuteQMdiSubWindowCall20>(taken[20]);
      call(this, focusOutEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::focusOutEvent(focusOutEvent);
  }

  //  void QMdiSubWindow::childEvent(QChildEvent *childEvent)
  void childEvent(QChildEvent *childEvent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQMdiSubWindowCall21 call = reinterpret_cast<CuteQMdiSubWindowCall21>(taken[21]);
      call(this, childEvent, &handled);
      if (handled) return;
    }
    QMdiSubWindow::childEvent(childEvent);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQMdiSubWindowCall22 call = reinterpret_cast<CuteQMdiSubWindowCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMdiSubWindowCall23 call = reinterpret_cast<CuteQMdiSubWindowCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQMdiSubWindowCall24 call = reinterpret_cast<CuteQMdiSubWindowCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQMdiSubWindowCall25 call = reinterpret_cast<CuteQMdiSubWindowCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQMdiSubWindowCall26 call = reinterpret_cast<CuteQMdiSubWindowCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMdiSubWindowCall27 call = reinterpret_cast<CuteQMdiSubWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQMdiSubWindowCall28 call = reinterpret_cast<CuteQMdiSubWindowCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQMdiSubWindowCall29 call = reinterpret_cast<CuteQMdiSubWindowCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQMdiSubWindowCall30 call = reinterpret_cast<CuteQMdiSubWindowCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMdiSubWindowCall31 call = reinterpret_cast<CuteQMdiSubWindowCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQMdiSubWindowCall32 call = reinterpret_cast<CuteQMdiSubWindowCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQMdiSubWindowCall33 call = reinterpret_cast<CuteQMdiSubWindowCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQMdiSubWindowCall34 call = reinterpret_cast<CuteQMdiSubWindowCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQMdiSubWindowCall35 call = reinterpret_cast<CuteQMdiSubWindowCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQMdiSubWindowCall36 call = reinterpret_cast<CuteQMdiSubWindowCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQMdiSubWindowCall37 call = reinterpret_cast<CuteQMdiSubWindowCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQMdiSubWindowCall38 call = reinterpret_cast<CuteQMdiSubWindowCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQMdiSubWindowCall39 call = reinterpret_cast<CuteQMdiSubWindowCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQMdiSubWindowCall40 call = reinterpret_cast<CuteQMdiSubWindowCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQMdiSubWindowCall41 call = reinterpret_cast<CuteQMdiSubWindowCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQMdiSubWindowCall42 call = reinterpret_cast<CuteQMdiSubWindowCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQMdiSubWindowCall43 call = reinterpret_cast<CuteQMdiSubWindowCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQMdiSubWindowCall44 call = reinterpret_cast<CuteQMdiSubWindowCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMdiSubWindowCall45 call = reinterpret_cast<CuteQMdiSubWindowCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QMdiSubWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QMdiSubWindow10metaObjectEv(
    const QMdiSubWindow *self) {
  return self->metaObject();
}

//  QString QMdiSubWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QMdiSubWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMdiSubWindow::tr(s, c, n));
}

//  QMdiSubWindow::QMdiSubWindow(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZN13QMdiSubWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQMdiSubWindow(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMdiSubWindow::~QMdiSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindowD1Ev(QMdiSubWindow *self) {
  delete self;
}

//  QSize QMdiSubWindow::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QMdiSubWindow8sizeHintEv(const QMdiSubWindow *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMdiSubWindow::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QMdiSubWindow15minimumSizeHintEv(
    const QMdiSubWindow *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QMdiSubWindow::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9setWidgetEP7QWidget(
    QMdiSubWindow *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QMdiSubWindow::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow6widgetEv(const QMdiSubWindow *self) {
  return self->widget();
}

//  QWidget *QMdiSubWindow::maximizedButtonsWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow22maximizedButtonsWidgetEv(
    const QMdiSubWindow *self) {
  return self->maximizedButtonsWidget();
}

//  QWidget *QMdiSubWindow::maximizedSystemMenuIconWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow29maximizedSystemMenuIconWidgetEv(
    const QMdiSubWindow *self) {
  return self->maximizedSystemMenuIconWidget();
}

//  bool QMdiSubWindow::isShaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMdiSubWindow8isShadedEv(const QMdiSubWindow *self) {
  return self->isShaded();
}

//  void QMdiSubWindow::setOption(SubWindowOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9setOptionENS_15SubWindowOptionEb(
    QMdiSubWindow *self,
    QMdiSubWindow::SubWindowOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMdiSubWindow::testOption(SubWindowOption a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMdiSubWindow10testOptionENS_15SubWindowOptionE(
    const QMdiSubWindow *self,
    QMdiSubWindow::SubWindowOption a0) {
  return self->testOption(a0);
}

//  void QMdiSubWindow::setKeyboardSingleStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow21setKeyboardSingleStepEi(
    QMdiSubWindow *self,
    int step) {
  self->setKeyboardSingleStep(step);
}

//  int QMdiSubWindow::keyboardSingleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMdiSubWindow18keyboardSingleStepEv(
    const QMdiSubWindow *self) {
  return self->keyboardSingleStep();
}

//  void QMdiSubWindow::setKeyboardPageStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow19setKeyboardPageStepEi(
    QMdiSubWindow *self,
    int step) {
  self->setKeyboardPageStep(step);
}

//  int QMdiSubWindow::keyboardPageStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMdiSubWindow16keyboardPageStepEv(
    const QMdiSubWindow *self) {
  return self->keyboardPageStep();
}

//  void QMdiSubWindow::setSystemMenu(QMenu *systemMenu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow13setSystemMenuEP5QMenu(
    QMdiSubWindow *self,
    QMenu *systemMenu) {
  self->setSystemMenu(systemMenu);
}

//  QMenu *QMdiSubWindow::systemMenu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK13QMdiSubWindow10systemMenuEv(const QMdiSubWindow *self) {
  return self->systemMenu();
}

//  QMdiArea *QMdiSubWindow::mdiArea() const
extern "C" Q_DECL_EXPORT
QMdiArea *ritual_ZNK13QMdiSubWindow7mdiAreaEv(const QMdiSubWindow *self) {
  return self->mdiArea();
}

//  void QMdiSubWindow::showSystemMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow14showSystemMenuEv(QMdiSubWindow *self) {
  self->showSystemMenu();
}

//  void QMdiSubWindow::showShaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10showShadedEv(QMdiSubWindow *self) {
  self->showShaded();
}

//  bool QMdiSubWindow::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMdiSubWindow11eventFilterEP7QObjectP6QEvent(
    QMdiSubWindow *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  bool QMdiSubWindow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMdiSubWindow5eventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *event) {
  return self->event(event);
}

//  void QMdiSubWindow::showEvent(QShowEvent *showEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9showEventEP10QShowEvent(
    QMdiSubWindow *self,
    QShowEvent *showEvent) {
  self->showEvent(showEvent);
}

//  void QMdiSubWindow::hideEvent(QHideEvent *hideEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9hideEventEP10QHideEvent(
    QMdiSubWindow *self,
    QHideEvent *hideEvent) {
  self->hideEvent(hideEvent);
}

//  void QMdiSubWindow::changeEvent(QEvent *changeEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow11changeEventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *changeEvent) {
  self->changeEvent(changeEvent);
}

//  void QMdiSubWindow::closeEvent(QCloseEvent *closeEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10closeEventEP11QCloseEvent(
    QMdiSubWindow *self,
    QCloseEvent *closeEvent) {
  self->closeEvent(closeEvent);
}

//  void QMdiSubWindow::leaveEvent(QEvent *leaveEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10leaveEventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *leaveEvent) {
  self->leaveEvent(leaveEvent);
}

//  void QMdiSubWindow::resizeEvent(QResizeEvent *resizeEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow11resizeEventEP12QResizeEvent(
    QMdiSubWindow *self,
    QResizeEvent *resizeEvent) {
  self->resizeEvent(resizeEvent);
}

//  void QMdiSubWindow::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10timerEventEP11QTimerEvent(
    QMdiSubWindow *self,
    QTimerEvent *timerEvent) {
  self->timerEvent(timerEvent);
}

//  void QMdiSubWindow::moveEvent(QMoveEvent *moveEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9moveEventEP10QMoveEvent(
    QMdiSubWindow *self,
    QMoveEvent *moveEvent) {
  self->moveEvent(moveEvent);
}

//  void QMdiSubWindow::paintEvent(QPaintEvent *paintEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10paintEventEP11QPaintEvent(
    QMdiSubWindow *self,
    QPaintEvent *paintEvent) {
  self->paintEvent(paintEvent);
}

//  void QMdiSubWindow::mousePressEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow15mousePressEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  self->mousePressEvent(mouseEvent);
}

//  void QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow21mouseDoubleClickEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  self->mouseDoubleClickEvent(mouseEvent);
}

//  void QMdiSubWindow::mouseReleaseEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow17mouseReleaseEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  self->mouseReleaseEvent(mouseEvent);
}

//  void QMdiSubWindow::mouseMoveEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow14mouseMoveEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  self->mouseMoveEvent(mouseEvent);
}

//  void QMdiSubWindow::keyPressEvent(QKeyEvent *keyEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow13keyPressEventEP9QKeyEvent(
    QMdiSubWindow *self,
    QKeyEvent *keyEvent) {
  self->keyPressEvent(keyEvent);
}

//  void QMdiSubWindow::contextMenuEvent(QContextMenuEvent *contextMenuEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow16contextMenuEventEP17QContextMenuEvent(
    QMdiSubWindow *self,
    QContextMenuEvent *contextMenuEvent) {
  self->contextMenuEvent(contextMenuEvent);
}

//  void QMdiSubWindow::focusInEvent(QFocusEvent *focusInEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow12focusInEventEP11QFocusEvent(
    QMdiSubWindow *self,
    QFocusEvent *focusInEvent) {
  self->focusInEvent(focusInEvent);
}

//  void QMdiSubWindow::focusOutEvent(QFocusEvent *focusOutEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow13focusOutEventEP11QFocusEvent(
    QMdiSubWindow *self,
    QFocusEvent *focusOutEvent) {
  self->focusOutEvent(focusOutEvent);
}

//  void QMdiSubWindow::childEvent(QChildEvent *childEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10childEventEP11QChildEvent(
    QMdiSubWindow *self,
    QChildEvent *childEvent) {
  self->childEvent(childEvent);
}

//  a Python function taken by a CuteQMdiSubWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdiSubWindow(
    QMdiSubWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMdiSubWindow *>(self)->take(key, call);
}

//  QSize QMdiSubWindow::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QMdiSubWindow8sizeHintEv(const QMdiSubWindow *self) {
  return new QSize(self->QMdiSubWindow::sizeHint());
}

//  QSize QMdiSubWindow::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QMdiSubWindow15minimumSizeHintEv(
    const QMdiSubWindow *self) {
  return new QSize(self->QMdiSubWindow::minimumSizeHint());
}

//  bool QMdiSubWindow::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QMdiSubWindow11eventFilterEP7QObjectP6QEvent(
    QMdiSubWindow *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::eventFilter(
      object,
      event);
}

//  bool QMdiSubWindow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QMdiSubWindow5eventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *event) {
  return static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::event(
      event);
}

//  void QMdiSubWindow::showEvent(QShowEvent *showEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow9showEventEP10QShowEvent(
    QMdiSubWindow *self,
    QShowEvent *showEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::showEvent(
      showEvent);
}

//  void QMdiSubWindow::hideEvent(QHideEvent *hideEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow9hideEventEP10QHideEvent(
    QMdiSubWindow *self,
    QHideEvent *hideEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::hideEvent(
      hideEvent);
}

//  void QMdiSubWindow::changeEvent(QEvent *changeEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow11changeEventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *changeEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::changeEvent(
      changeEvent);
}

//  void QMdiSubWindow::closeEvent(QCloseEvent *closeEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow10closeEventEP11QCloseEvent(
    QMdiSubWindow *self,
    QCloseEvent *closeEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::closeEvent(
      closeEvent);
}

//  void QMdiSubWindow::leaveEvent(QEvent *leaveEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow10leaveEventEP6QEvent(
    QMdiSubWindow *self,
    QEvent *leaveEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::leaveEvent(
      leaveEvent);
}

//  void QMdiSubWindow::resizeEvent(QResizeEvent *resizeEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow11resizeEventEP12QResizeEvent(
    QMdiSubWindow *self,
    QResizeEvent *resizeEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::resizeEvent(
      resizeEvent);
}

//  void QMdiSubWindow::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow10timerEventEP11QTimerEvent(
    QMdiSubWindow *self,
    QTimerEvent *timerEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::timerEvent(
      timerEvent);
}

//  void QMdiSubWindow::moveEvent(QMoveEvent *moveEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow9moveEventEP10QMoveEvent(
    QMdiSubWindow *self,
    QMoveEvent *moveEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::moveEvent(
      moveEvent);
}

//  void QMdiSubWindow::paintEvent(QPaintEvent *paintEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow10paintEventEP11QPaintEvent(
    QMdiSubWindow *self,
    QPaintEvent *paintEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::paintEvent(
      paintEvent);
}

//  void QMdiSubWindow::mousePressEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow15mousePressEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::mousePressEvent(
      mouseEvent);
}

//  void QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow21mouseDoubleClickEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::mouseDoubleClickEvent(
      mouseEvent);
}

//  void QMdiSubWindow::mouseReleaseEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow17mouseReleaseEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::mouseReleaseEvent(
      mouseEvent);
}

//  void QMdiSubWindow::mouseMoveEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow14mouseMoveEventEP11QMouseEvent(
    QMdiSubWindow *self,
    QMouseEvent *mouseEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::mouseMoveEvent(
      mouseEvent);
}

//  void QMdiSubWindow::keyPressEvent(QKeyEvent *keyEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow13keyPressEventEP9QKeyEvent(
    QMdiSubWindow *self,
    QKeyEvent *keyEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::keyPressEvent(
      keyEvent);
}

//  void QMdiSubWindow::contextMenuEvent(QContextMenuEvent *contextMenuEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow16contextMenuEventEP17QContextMenuEvent(
    QMdiSubWindow *self,
    QContextMenuEvent *contextMenuEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::contextMenuEvent(
      contextMenuEvent);
}

//  void QMdiSubWindow::focusInEvent(QFocusEvent *focusInEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow12focusInEventEP11QFocusEvent(
    QMdiSubWindow *self,
    QFocusEvent *focusInEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::focusInEvent(
      focusInEvent);
}

//  void QMdiSubWindow::focusOutEvent(QFocusEvent *focusOutEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow13focusOutEventEP11QFocusEvent(
    QMdiSubWindow *self,
    QFocusEvent *focusOutEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::focusOutEvent(
      focusOutEvent);
}

//  void QMdiSubWindow::childEvent(QChildEvent *childEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMdiSubWindow10childEventEP11QChildEvent(
    QMdiSubWindow *self,
    QChildEvent *childEvent) {
  static_cast<OwnQMdiSubWindow *>(self)->OwnQMdiSubWindow::childEvent(
      childEvent);
}

//  QList<QMdiSubWindow *>::QList()
extern "C" Q_DECL_EXPORT
QList<QMdiSubWindow *> *ritual_list_make_QMdiSubWindow_ptr() {
  return new QList<QMdiSubWindow *>();
}

//  void QList<QMdiSubWindow *>::append(const QMdiSubWindow * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMdiSubWindow_ptr(
    QList<QMdiSubWindow *> *self,
    QMdiSubWindow *element) {
  self->append(element);
}

//  qsizetype QList<QMdiSubWindow *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMdiSubWindow_ptr(
    const QList<QMdiSubWindow *> *self) {
  return self->size();
}

//  const QMdiSubWindow * &QList<QMdiSubWindow *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_list_at_QMdiSubWindow_ptr(
    const QList<QMdiSubWindow *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QMdiSubWindow *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMdiSubWindow_ptr(QList<QMdiSubWindow *> *self) {
  delete self;
}
