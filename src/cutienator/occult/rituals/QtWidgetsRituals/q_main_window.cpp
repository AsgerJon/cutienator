//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmainwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmainwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QMainWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMainWindow : QMainWindow {
  using QMainWindow::contextMenuEvent;
  using QMainWindow::event;
};

//  A QMainWindow that Python can take functions over in. Every QMainWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQMainWindowCall0)(const void *, int *);
typedef void (*CuteQMainWindowCall1)(const void *, QContextMenuEvent *, int *);
typedef bool (*CuteQMainWindowCall2)(const void *, QEvent *, int *);
typedef int (*CuteQMainWindowCall3)(const void *, int *);
typedef void (*CuteQMainWindowCall4)(const void *, bool, int *);
typedef const QSize * (*CuteQMainWindowCall5)(const void *, int *);
typedef const QSize * (*CuteQMainWindowCall6)(const void *, int *);
typedef int (*CuteQMainWindowCall7)(const void *, int, int *);
typedef bool (*CuteQMainWindowCall8)(const void *, int *);
typedef void * (*CuteQMainWindowCall9)(const void *, int *);
typedef void (*CuteQMainWindowCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMainWindowCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMainWindowCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMainWindowCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMainWindowCall14)(const void *, QWheelEvent *, int *);
typedef void (*CuteQMainWindowCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMainWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMainWindowCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMainWindowCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMainWindowCall19)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMainWindowCall20)(const void *, QEvent *, int *);
typedef void (*CuteQMainWindowCall21)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMainWindowCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQMainWindowCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQMainWindowCall24)(const void *, QCloseEvent *, int *);
typedef void (*CuteQMainWindowCall25)(const void *, QTabletEvent *, int *);
typedef void (*CuteQMainWindowCall26)(const void *, QActionEvent *, int *);
typedef void (*CuteQMainWindowCall27)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQMainWindowCall28)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQMainWindowCall29)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQMainWindowCall30)(const void *, QDropEvent *, int *);
typedef void (*CuteQMainWindowCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQMainWindowCall32)(const void *, QHideEvent *, int *);
typedef void (*CuteQMainWindowCall33)(const void *, QEvent *, int *);
typedef int (*CuteQMainWindowCall34)(const void *, int, int *);
typedef void (*CuteQMainWindowCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQMainWindowCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQMainWindowCall37)(const void *, int *);
typedef void (*CuteQMainWindowCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMainWindowCall39)(const void *, int, int *);
typedef bool (*CuteQMainWindowCall40)(const void *, bool, int *);
typedef bool (*CuteQMainWindowCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQMainWindowCall42)(const void *, QTimerEvent *, int *);
typedef void (*CuteQMainWindowCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQMainWindowCall44)(const void *, QEvent *, int *);
typedef void (*CuteQMainWindowCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQMainWindowCall46)(const void *, const QMetaMethod *, int *);
class CuteQMainWindow : public QMainWindow {
public:
  using QMainWindow::QMainWindow;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QMainWindow15createPopupMenuEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
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

  //  QMenu *QMainWindow::createPopupMenu()
  QMenu *createPopupMenu() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMainWindowCall0 call = reinterpret_cast<CuteQMainWindowCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMenu *>(given);
    }
    return QMainWindow::createPopupMenu();
  }

  //  void QMainWindow::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMainWindowCall1 call = reinterpret_cast<CuteQMainWindowCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMainWindow::contextMenuEvent(event);
  }

  //  bool QMainWindow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMainWindowCall2 call = reinterpret_cast<CuteQMainWindowCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QMainWindow::event(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMainWindowCall3 call = reinterpret_cast<CuteQMainWindowCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMainWindowCall4 call = reinterpret_cast<CuteQMainWindowCall4>(taken[4]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMainWindowCall5 call = reinterpret_cast<CuteQMainWindowCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMainWindowCall6 call = reinterpret_cast<CuteQMainWindowCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQMainWindowCall7 call = reinterpret_cast<CuteQMainWindowCall7>(taken[7]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQMainWindowCall8 call = reinterpret_cast<CuteQMainWindowCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQMainWindowCall9 call = reinterpret_cast<CuteQMainWindowCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMainWindowCall10 call = reinterpret_cast<CuteQMainWindowCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMainWindowCall11 call = reinterpret_cast<CuteQMainWindowCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMainWindowCall12 call = reinterpret_cast<CuteQMainWindowCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMainWindowCall13 call = reinterpret_cast<CuteQMainWindowCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMainWindowCall14 call = reinterpret_cast<CuteQMainWindowCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQMainWindowCall15 call = reinterpret_cast<CuteQMainWindowCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQMainWindowCall16 call = reinterpret_cast<CuteQMainWindowCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQMainWindowCall17 call = reinterpret_cast<CuteQMainWindowCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQMainWindowCall18 call = reinterpret_cast<CuteQMainWindowCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQMainWindowCall19 call = reinterpret_cast<CuteQMainWindowCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQMainWindowCall20 call = reinterpret_cast<CuteQMainWindowCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQMainWindowCall21 call = reinterpret_cast<CuteQMainWindowCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMainWindowCall22 call = reinterpret_cast<CuteQMainWindowCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMainWindowCall23 call = reinterpret_cast<CuteQMainWindowCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQMainWindowCall24 call = reinterpret_cast<CuteQMainWindowCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQMainWindowCall25 call = reinterpret_cast<CuteQMainWindowCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQMainWindowCall26 call = reinterpret_cast<CuteQMainWindowCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMainWindowCall27 call = reinterpret_cast<CuteQMainWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQMainWindowCall28 call = reinterpret_cast<CuteQMainWindowCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQMainWindowCall29 call = reinterpret_cast<CuteQMainWindowCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQMainWindowCall30 call = reinterpret_cast<CuteQMainWindowCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMainWindowCall31 call = reinterpret_cast<CuteQMainWindowCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQMainWindowCall32 call = reinterpret_cast<CuteQMainWindowCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQMainWindowCall33 call = reinterpret_cast<CuteQMainWindowCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQMainWindowCall34 call = reinterpret_cast<CuteQMainWindowCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQMainWindowCall35 call = reinterpret_cast<CuteQMainWindowCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQMainWindowCall36 call = reinterpret_cast<CuteQMainWindowCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQMainWindowCall37 call = reinterpret_cast<CuteQMainWindowCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQMainWindowCall38 call = reinterpret_cast<CuteQMainWindowCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQMainWindowCall39 call = reinterpret_cast<CuteQMainWindowCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQMainWindowCall40 call = reinterpret_cast<CuteQMainWindowCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQMainWindowCall41 call = reinterpret_cast<CuteQMainWindowCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQMainWindowCall42 call = reinterpret_cast<CuteQMainWindowCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQMainWindowCall43 call = reinterpret_cast<CuteQMainWindowCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQMainWindowCall44 call = reinterpret_cast<CuteQMainWindowCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMainWindowCall45 call = reinterpret_cast<CuteQMainWindowCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQMainWindowCall46 call = reinterpret_cast<CuteQMainWindowCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QMainWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMainWindow10metaObjectEv(
    const QMainWindow *self) {
  return self->metaObject();
}

//  QString QMainWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QMainWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMainWindow::tr(s, c, n));
}

//  QMainWindow::QMainWindow(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QMainWindow *ritual_ZN11QMainWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQMainWindow(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMainWindow::~QMainWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindowD1Ev(QMainWindow *self) {
  delete self;
}

//  QSize QMainWindow::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QMainWindow8iconSizeEv(const QMainWindow *self) {
  return new QSize(self->iconSize());
}

//  void QMainWindow::setIconSize(const QSize &iconSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setIconSizeERK5QSize(
    QMainWindow *self,
    const QSize *iconSize) {
  self->setIconSize(*iconSize);
}

//  Qt::ToolButtonStyle QMainWindow::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK11QMainWindow15toolButtonStyleEv(
    const QMainWindow *self) {
  return self->toolButtonStyle();
}

//  void QMainWindow::setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QMainWindow *self,
    Qt::ToolButtonStyle toolButtonStyle) {
  self->setToolButtonStyle(toolButtonStyle);
}

//  bool QMainWindow::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow10isAnimatedEv(const QMainWindow *self) {
  return self->isAnimated();
}

//  bool QMainWindow::isDockNestingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow20isDockNestingEnabledEv(
    const QMainWindow *self) {
  return self->isDockNestingEnabled();
}

//  bool QMainWindow::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow12documentModeEv(const QMainWindow *self) {
  return self->documentMode();
}

//  void QMainWindow::setDocumentMode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15setDocumentModeEb(
    QMainWindow *self,
    bool enabled) {
  self->setDocumentMode(enabled);
}

//  QTabWidget::TabShape QMainWindow::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK11QMainWindow8tabShapeEv(
    const QMainWindow *self) {
  return self->tabShape();
}

//  void QMainWindow::setTabShape(QTabWidget::TabShape tabShape)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setTabShapeEN10QTabWidget8TabShapeE(
    QMainWindow *self,
    QTabWidget::TabShape tabShape) {
  self->setTabShape(tabShape);
}

//  QTabWidget::TabPosition QMainWindow::tabPosition(Qt::DockWidgetArea area)
//      const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK11QMainWindow11tabPositionEN2Qt14DockWidgetAreaE(
    const QMainWindow *self,
    Qt::DockWidgetArea area) {
  return self->tabPosition(area);
}

//  void QMainWindow::setTabPosition(Qt::DockWidgetAreas areas,
//      QTabWidget::TabPosition tabPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow14setTabPositionE6QFlagsIN2Qt14DockWidgetAreaEEN10QTabWidget11TabPositionE(
    QMainWindow *self,
    int areas,
    QTabWidget::TabPosition tabPosition) {
  self->setTabPosition(
      QFlags<Qt::DockWidgetArea>::fromInt(areas),
      tabPosition);
}

//  void QMainWindow::setDockOptions(DockOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow14setDockOptionsE6QFlagsINS_10DockOptionEE(
    QMainWindow *self,
    int options) {
  self->setDockOptions(QFlags<QMainWindow::DockOption>::fromInt(options));
}

//  DockOptions QMainWindow::dockOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMainWindow11dockOptionsEv(const QMainWindow *self) {
  return static_cast<int>(self->dockOptions().toInt());
}

//  bool QMainWindow::isSeparator(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow11isSeparatorERK6QPoint(
    const QMainWindow *self,
    const QPoint *pos) {
  return self->isSeparator(*pos);
}

//  QMenuBar *QMainWindow::menuBar() const
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZNK11QMainWindow7menuBarEv(const QMainWindow *self) {
  return self->menuBar();
}

//  void QMainWindow::setMenuBar(QMenuBar *menubar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10setMenuBarEP8QMenuBar(
    QMainWindow *self,
    QMenuBar *menubar) {
  self->setMenuBar(menubar);
}

//  QWidget *QMainWindow::menuWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QMainWindow10menuWidgetEv(const QMainWindow *self) {
  return self->menuWidget();
}

//  void QMainWindow::setMenuWidget(QWidget *menubar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13setMenuWidgetEP7QWidget(
    QMainWindow *self,
    QWidget *menubar) {
  self->setMenuWidget(menubar);
}

//  QStatusBar *QMainWindow::statusBar() const
extern "C" Q_DECL_EXPORT
QStatusBar *ritual_ZNK11QMainWindow9statusBarEv(const QMainWindow *self) {
  return self->statusBar();
}

//  void QMainWindow::setStatusBar(QStatusBar *statusbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow12setStatusBarEP10QStatusBar(
    QMainWindow *self,
    QStatusBar *statusbar) {
  self->setStatusBar(statusbar);
}

//  QWidget *QMainWindow::centralWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QMainWindow13centralWidgetEv(const QMainWindow *self) {
  return self->centralWidget();
}

//  void QMainWindow::setCentralWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16setCentralWidgetEP7QWidget(
    QMainWindow *self,
    QWidget *widget) {
  self->setCentralWidget(widget);
}

//  QWidget *QMainWindow::takeCentralWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN11QMainWindow17takeCentralWidgetEv(QMainWindow *self) {
  return self->takeCentralWidget();
}

//  void QMainWindow::setCorner(Qt::Corner corner, Qt::DockWidgetArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow9setCornerEN2Qt6CornerENS0_14DockWidgetAreaE(
    QMainWindow *self,
    Qt::Corner corner,
    Qt::DockWidgetArea area) {
  self->setCorner(corner, area);
}

//  Qt::DockWidgetArea QMainWindow::corner(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QMainWindow6cornerEN2Qt6CornerE(
    const QMainWindow *self,
    Qt::Corner corner) {
  return self->corner(corner);
}

//  void QMainWindow::addToolBarBreak(Qt::ToolBarArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15addToolBarBreakEN2Qt11ToolBarAreaE(
    QMainWindow *self,
    Qt::ToolBarArea area) {
  self->addToolBarBreak(area);
}

//  void QMainWindow::insertToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18insertToolBarBreakEP8QToolBar(
    QMainWindow *self,
    QToolBar *before) {
  self->insertToolBarBreak(before);
}

//  void QMainWindow::addToolBar(Qt::ToolBarArea area, QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10addToolBarEN2Qt11ToolBarAreaEP8QToolBar(
    QMainWindow *self,
    Qt::ToolBarArea area,
    QToolBar *toolbar) {
  self->addToolBar(area, toolbar);
}

//  void QMainWindow::addToolBar(QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10addToolBarEP8QToolBar(
    QMainWindow *self,
    QToolBar *toolbar) {
  self->addToolBar(toolbar);
}

//  QToolBar *QMainWindow::addToolBar(const QString &title)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN11QMainWindow10addToolBarERK7QString(
    QMainWindow *self,
    const QString *title) {
  return self->addToolBar(*title);
}

//  void QMainWindow::insertToolBar(QToolBar *before, QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13insertToolBarEP8QToolBarS1_(
    QMainWindow *self,
    QToolBar *before,
    QToolBar *toolbar) {
  self->insertToolBar(before, toolbar);
}

//  void QMainWindow::removeToolBar(QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13removeToolBarEP8QToolBar(
    QMainWindow *self,
    QToolBar *toolbar) {
  self->removeToolBar(toolbar);
}

//  void QMainWindow::removeToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18removeToolBarBreakEP8QToolBar(
    QMainWindow *self,
    QToolBar *before) {
  self->removeToolBarBreak(before);
}

//  bool QMainWindow::unifiedTitleAndToolBarOnMac() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow27unifiedTitleAndToolBarOnMacEv(
    const QMainWindow *self) {
  return self->unifiedTitleAndToolBarOnMac();
}

//  Qt::ToolBarArea QMainWindow::toolBarArea(const QToolBar *toolbar) const
extern "C" Q_DECL_EXPORT
Qt::ToolBarArea ritual_ZNK11QMainWindow11toolBarAreaEPK8QToolBar(
    const QMainWindow *self,
    const QToolBar *toolbar) {
  return self->toolBarArea(toolbar);
}

//  bool QMainWindow::toolBarBreak(QToolBar *toolbar) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow12toolBarBreakEP8QToolBar(
    const QMainWindow *self,
    QToolBar *toolbar) {
  return self->toolBarBreak(toolbar);
}

//  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
//      *dockwidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDockWidget(
    QMainWindow *self,
    Qt::DockWidgetArea area,
    QDockWidget *dockwidget) {
  self->addDockWidget(area, dockwidget);
}

//  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
//      *dockwidget, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDockWidgetNS0_11OrientationE(
    QMainWindow *self,
    Qt::DockWidgetArea area,
    QDockWidget *dockwidget,
    Qt::Orientation orientation) {
  self->addDockWidget(area, dockwidget, orientation);
}

//  void QMainWindow::splitDockWidget(QDockWidget *after, QDockWidget
//      *dockwidget, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15splitDockWidgetEP11QDockWidgetS1_N2Qt11OrientationE(
    QMainWindow *self,
    QDockWidget *after,
    QDockWidget *dockwidget,
    Qt::Orientation orientation) {
  self->splitDockWidget(after, dockwidget, orientation);
}

//  void QMainWindow::tabifyDockWidget(QDockWidget *first, QDockWidget
//      *second)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16tabifyDockWidgetEP11QDockWidgetS1_(
    QMainWindow *self,
    QDockWidget *first,
    QDockWidget *second) {
  self->tabifyDockWidget(first, second);
}

//  void QMainWindow::removeDockWidget(QDockWidget *dockwidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16removeDockWidgetEP11QDockWidget(
    QMainWindow *self,
    QDockWidget *dockwidget) {
  self->removeDockWidget(dockwidget);
}

//  bool QMainWindow::restoreDockWidget(QDockWidget *dockwidget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMainWindow17restoreDockWidgetEP11QDockWidget(
    QMainWindow *self,
    QDockWidget *dockwidget) {
  return self->restoreDockWidget(dockwidget);
}

//  Qt::DockWidgetArea QMainWindow::dockWidgetArea(QDockWidget *dockwidget)
//      const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QMainWindow14dockWidgetAreaEP11QDockWidget(
    const QMainWindow *self,
    QDockWidget *dockwidget) {
  return self->dockWidgetArea(dockwidget);
}

//  QByteArray QMainWindow::saveState(int version) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMainWindow9saveStateEi(
    const QMainWindow *self,
    int version) {
  return new QByteArray(self->saveState(version));
}

//  bool QMainWindow::restoreState(const QByteArray &state, int version)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMainWindow12restoreStateERK10QByteArrayi(
    QMainWindow *self,
    const QByteArray *state,
    int version) {
  return self->restoreState(*state, version);
}

//  QMenu *QMainWindow::createPopupMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN11QMainWindow15createPopupMenuEv(QMainWindow *self) {
  return self->createPopupMenu();
}

//  void QMainWindow::setAnimated(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setAnimatedEb(QMainWindow *self, bool enabled) {
  self->setAnimated(enabled);
}

//  void QMainWindow::setDockNestingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow21setDockNestingEnabledEb(
    QMainWindow *self,
    bool enabled) {
  self->setDockNestingEnabled(enabled);
}

//  void QMainWindow::setUnifiedTitleAndToolBarOnMac(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow30setUnifiedTitleAndToolBarOnMacEb(
    QMainWindow *self,
    bool set) {
  self->setUnifiedTitleAndToolBarOnMac(set);
}

//  a Python function taken by a CuteQMainWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMainWindow(
    QMainWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMainWindow *>(self)->take(key, call);
}

//  QMenu *QMainWindow::createPopupMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_own_ZN11QMainWindow15createPopupMenuEv(QMainWindow *self) {
  return self->QMainWindow::createPopupMenu();
}

//  void QMainWindow::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMainWindow16contextMenuEventEP17QContextMenuEvent(
    QMainWindow *self,
    QContextMenuEvent *event) {
  static_cast<OwnQMainWindow *>(self)->OwnQMainWindow::contextMenuEvent(
      event);
}

//  bool QMainWindow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QMainWindow5eventEP6QEvent(
    QMainWindow *self,
    QEvent *event) {
  return static_cast<OwnQMainWindow *>(self)->OwnQMainWindow::event(event);
}
