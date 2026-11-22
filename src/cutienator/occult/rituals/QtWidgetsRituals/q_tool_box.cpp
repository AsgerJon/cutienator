//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtoolbox.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QToolBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQToolBox : QToolBox {
  using QToolBox::event;
  using QToolBox::itemInserted;
  using QToolBox::itemRemoved;
  using QToolBox::showEvent;
  using QToolBox::changeEvent;
};

//  A QToolBox that Python can take functions over in. Every QToolBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQToolBoxCall0)(const void *, QEvent *, int *);
typedef void (*CuteQToolBoxCall1)(const void *, int, int *);
typedef void (*CuteQToolBoxCall2)(const void *, int, int *);
typedef void (*CuteQToolBoxCall3)(const void *, QShowEvent *, int *);
typedef void (*CuteQToolBoxCall4)(const void *, QEvent *, int *);
typedef const QSize * (*CuteQToolBoxCall5)(const void *, int *);
typedef void (*CuteQToolBoxCall6)(const void *, QPaintEvent *, int *);
typedef void (*CuteQToolBoxCall7)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQToolBoxCall8)(const void *, int *);
typedef void (*CuteQToolBoxCall9)(const void *, bool, int *);
typedef const QSize * (*CuteQToolBoxCall10)(const void *, int *);
typedef int (*CuteQToolBoxCall11)(const void *, int, int *);
typedef bool (*CuteQToolBoxCall12)(const void *, int *);
typedef void * (*CuteQToolBoxCall13)(const void *, int *);
typedef void (*CuteQToolBoxCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBoxCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBoxCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBoxCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBoxCall18)(const void *, QWheelEvent *, int *);
typedef void (*CuteQToolBoxCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBoxCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBoxCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBoxCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBoxCall23)(const void *, QEnterEvent *, int *);
typedef void (*CuteQToolBoxCall24)(const void *, QEvent *, int *);
typedef void (*CuteQToolBoxCall25)(const void *, QMoveEvent *, int *);
typedef void (*CuteQToolBoxCall26)(const void *, QResizeEvent *, int *);
typedef void (*CuteQToolBoxCall27)(const void *, QCloseEvent *, int *);
typedef void (*CuteQToolBoxCall28)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQToolBoxCall29)(const void *, QTabletEvent *, int *);
typedef void (*CuteQToolBoxCall30)(const void *, QActionEvent *, int *);
typedef void (*CuteQToolBoxCall31)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQToolBoxCall32)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQToolBoxCall33)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQToolBoxCall34)(const void *, QDropEvent *, int *);
typedef void (*CuteQToolBoxCall35)(const void *, QHideEvent *, int *);
typedef int (*CuteQToolBoxCall36)(const void *, int, int *);
typedef void (*CuteQToolBoxCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQToolBoxCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQToolBoxCall39)(const void *, int *);
typedef void (*CuteQToolBoxCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQToolBoxCall41)(const void *, int, int *);
typedef bool (*CuteQToolBoxCall42)(const void *, bool, int *);
typedef bool (*CuteQToolBoxCall43)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQToolBoxCall44)(const void *, QTimerEvent *, int *);
typedef void (*CuteQToolBoxCall45)(const void *, QChildEvent *, int *);
typedef void (*CuteQToolBoxCall46)(const void *, QEvent *, int *);
typedef void (*CuteQToolBoxCall47)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQToolBoxCall48)(const void *, const QMetaMethod *, int *);
class CuteQToolBox : public QToolBox {
public:
  using QToolBox::QToolBox;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QToolBox12itemInsertedEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QToolBox11itemRemovedEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
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

  //  bool QToolBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBoxCall0 call = reinterpret_cast<CuteQToolBoxCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QToolBox::event(e);
  }

  //  void QToolBox::itemInserted(int index)
  void itemInserted(int index) override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBoxCall1 call = reinterpret_cast<CuteQToolBoxCall1>(taken[1]);
      call(this, index, &handled);
      if (handled) return;
    }
    QToolBox::itemInserted(index);
  }

  //  void QToolBox::itemRemoved(int index)
  void itemRemoved(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBoxCall2 call = reinterpret_cast<CuteQToolBoxCall2>(taken[2]);
      call(this, index, &handled);
      if (handled) return;
    }
    QToolBox::itemRemoved(index);
  }

  //  void QToolBox::showEvent(QShowEvent *e)
  void showEvent(QShowEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBoxCall3 call = reinterpret_cast<CuteQToolBoxCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QToolBox::showEvent(e);
  }

  //  void QToolBox::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBoxCall4 call = reinterpret_cast<CuteQToolBoxCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolBox::changeEvent(a0);
  }

  //  QSize QFrame::sizeHint() const
  QSize sizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBoxCall5 call = reinterpret_cast<CuteQToolBoxCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFrame::sizeHint();
  }

  //  void QFrame::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBoxCall6 call = reinterpret_cast<CuteQToolBoxCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::paintEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBoxCall7 call = reinterpret_cast<CuteQToolBoxCall7>(taken[7]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBoxCall8 call = reinterpret_cast<CuteQToolBoxCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBoxCall9 call = reinterpret_cast<CuteQToolBoxCall9>(taken[9]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBoxCall10 call = reinterpret_cast<CuteQToolBoxCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBoxCall11 call = reinterpret_cast<CuteQToolBoxCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBoxCall12 call = reinterpret_cast<CuteQToolBoxCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBoxCall13 call = reinterpret_cast<CuteQToolBoxCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBoxCall14 call = reinterpret_cast<CuteQToolBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolBoxCall15 call = reinterpret_cast<CuteQToolBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQToolBoxCall16 call = reinterpret_cast<CuteQToolBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQToolBoxCall17 call = reinterpret_cast<CuteQToolBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQToolBoxCall18 call = reinterpret_cast<CuteQToolBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQToolBoxCall19 call = reinterpret_cast<CuteQToolBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQToolBoxCall20 call = reinterpret_cast<CuteQToolBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQToolBoxCall21 call = reinterpret_cast<CuteQToolBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQToolBoxCall22 call = reinterpret_cast<CuteQToolBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQToolBoxCall23 call = reinterpret_cast<CuteQToolBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQToolBoxCall24 call = reinterpret_cast<CuteQToolBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQToolBoxCall25 call = reinterpret_cast<CuteQToolBoxCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQToolBoxCall26 call = reinterpret_cast<CuteQToolBoxCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQToolBoxCall27 call = reinterpret_cast<CuteQToolBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQToolBoxCall28 call = reinterpret_cast<CuteQToolBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQToolBoxCall29 call = reinterpret_cast<CuteQToolBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQToolBoxCall30 call = reinterpret_cast<CuteQToolBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQToolBoxCall31 call = reinterpret_cast<CuteQToolBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQToolBoxCall32 call = reinterpret_cast<CuteQToolBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQToolBoxCall33 call = reinterpret_cast<CuteQToolBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQToolBoxCall34 call = reinterpret_cast<CuteQToolBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQToolBoxCall35 call = reinterpret_cast<CuteQToolBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQToolBoxCall36 call = reinterpret_cast<CuteQToolBoxCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQToolBoxCall37 call = reinterpret_cast<CuteQToolBoxCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQToolBoxCall38 call = reinterpret_cast<CuteQToolBoxCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQToolBoxCall39 call = reinterpret_cast<CuteQToolBoxCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQToolBoxCall40 call = reinterpret_cast<CuteQToolBoxCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQToolBoxCall41 call = reinterpret_cast<CuteQToolBoxCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQToolBoxCall42 call = reinterpret_cast<CuteQToolBoxCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQToolBoxCall43 call = reinterpret_cast<CuteQToolBoxCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQToolBoxCall44 call = reinterpret_cast<CuteQToolBoxCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQToolBoxCall45 call = reinterpret_cast<CuteQToolBoxCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQToolBoxCall46 call = reinterpret_cast<CuteQToolBoxCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQToolBoxCall47 call = reinterpret_cast<CuteQToolBoxCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQToolBoxCall48 call = reinterpret_cast<CuteQToolBoxCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QToolBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QToolBox10metaObjectEv(const QToolBox *self) {
  return self->metaObject();
}

//  QString QToolBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QToolBox2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QToolBox::tr(s, c, n));
}

//  QToolBox::QToolBox(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QToolBox *ritual_ZN8QToolBoxC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQToolBox(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QToolBox::~QToolBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBoxD1Ev(QToolBox *self) {
  delete self;
}

//  int QToolBox::addItem(QWidget *widget, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox7addItemEP7QWidgetRK7QString(
    QToolBox *self,
    QWidget *widget,
    const QString *text) {
  return self->addItem(widget, *text);
}

//  int QToolBox::addItem(QWidget *widget, const QIcon &icon, const QString
//      &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox7addItemEP7QWidgetRK5QIconRK7QString(
    QToolBox *self,
    QWidget *widget,
    const QIcon *icon,
    const QString *text) {
  return self->addItem(widget, *icon, *text);
}

//  int QToolBox::insertItem(int index, QWidget *widget, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox10insertItemEiP7QWidgetRK7QString(
    QToolBox *self,
    int index,
    QWidget *widget,
    const QString *text) {
  return self->insertItem(index, widget, *text);
}

//  int QToolBox::insertItem(int index, QWidget *widget, const QIcon &icon,
//      const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox10insertItemEiP7QWidgetRK5QIconRK7QString(
    QToolBox *self,
    int index,
    QWidget *widget,
    const QIcon *icon,
    const QString *text) {
  return self->insertItem(index, widget, *icon, *text);
}

//  void QToolBox::removeItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox10removeItemEi(QToolBox *self, int index) {
  self->removeItem(index);
}

//  void QToolBox::setItemEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox14setItemEnabledEib(
    QToolBox *self,
    int index,
    bool enabled) {
  self->setItemEnabled(index, enabled);
}

//  bool QToolBox::isItemEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBox13isItemEnabledEi(const QToolBox *self, int index) {
  return self->isItemEnabled(index);
}

//  void QToolBox::setItemText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox11setItemTextEiRK7QString(
    QToolBox *self,
    int index,
    const QString *text) {
  self->setItemText(index, *text);
}

//  QString QToolBox::itemText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QToolBox8itemTextEi(const QToolBox *self, int index) {
  return new QString(self->itemText(index));
}

//  void QToolBox::setItemIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox11setItemIconEiRK5QIcon(
    QToolBox *self,
    int index,
    const QIcon *icon) {
  self->setItemIcon(index, *icon);
}

//  QIcon QToolBox::itemIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK8QToolBox8itemIconEi(const QToolBox *self, int index) {
  return new QIcon(self->itemIcon(index));
}

//  void QToolBox::setItemToolTip(int index, const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox14setItemToolTipEiRK7QString(
    QToolBox *self,
    int index,
    const QString *toolTip) {
  self->setItemToolTip(index, *toolTip);
}

//  QString QToolBox::itemToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QToolBox11itemToolTipEi(
    const QToolBox *self,
    int index) {
  return new QString(self->itemToolTip(index));
}

//  int QToolBox::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox12currentIndexEv(const QToolBox *self) {
  return self->currentIndex();
}

//  QWidget *QToolBox::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBox13currentWidgetEv(const QToolBox *self) {
  return self->currentWidget();
}

//  QWidget *QToolBox::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBox6widgetEi(const QToolBox *self, int index) {
  return self->widget(index);
}

//  int QToolBox::indexOf(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox7indexOfEPK7QWidget(
    const QToolBox *self,
    const QWidget *widget) {
  return self->indexOf(widget);
}

//  int QToolBox::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox5countEv(const QToolBox *self) {
  return self->count();
}

//  void QToolBox::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox15setCurrentIndexEi(QToolBox *self, int index) {
  self->setCurrentIndex(index);
}

//  void QToolBox::setCurrentWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox16setCurrentWidgetEP7QWidget(
    QToolBox *self,
    QWidget *widget) {
  self->setCurrentWidget(widget);
}

//  a Python function taken by a CuteQToolBox, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBox(QToolBox *self, const char *key, void *call) {
  return static_cast<CuteQToolBox *>(self)->take(key, call);
}

//  bool QToolBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QToolBox5eventEP6QEvent(QToolBox *self, QEvent *e) {
  return static_cast<OwnQToolBox *>(self)->OwnQToolBox::event(e);
}

//  void QToolBox::itemInserted(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBox12itemInsertedEi(QToolBox *self, int index) {
  static_cast<OwnQToolBox *>(self)->OwnQToolBox::itemInserted(index);
}

//  void QToolBox::itemRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBox11itemRemovedEi(QToolBox *self, int index) {
  static_cast<OwnQToolBox *>(self)->OwnQToolBox::itemRemoved(index);
}

//  void QToolBox::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBox9showEventEP10QShowEvent(
    QToolBox *self,
    QShowEvent *e) {
  static_cast<OwnQToolBox *>(self)->OwnQToolBox::showEvent(e);
}

//  void QToolBox::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBox11changeEventEP6QEvent(
    QToolBox *self,
    QEvent *a0) {
  static_cast<OwnQToolBox *>(self)->OwnQToolBox::changeEvent(a0);
}
