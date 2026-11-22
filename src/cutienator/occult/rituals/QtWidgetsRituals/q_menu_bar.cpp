//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmenubar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmenubar.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QMenuBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMenuBar : QMenuBar {
  using QMenuBar::changeEvent;
  using QMenuBar::keyPressEvent;
  using QMenuBar::mouseReleaseEvent;
  using QMenuBar::mousePressEvent;
  using QMenuBar::mouseMoveEvent;
  using QMenuBar::leaveEvent;
  using QMenuBar::paintEvent;
  using QMenuBar::resizeEvent;
  using QMenuBar::actionEvent;
  using QMenuBar::focusOutEvent;
  using QMenuBar::focusInEvent;
  using QMenuBar::timerEvent;
  using QMenuBar::eventFilter;
  using QMenuBar::event;
  using QMenuBar::initStyleOption;
};

//  A QMenuBar that Python can take functions over in. Every QMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQMenuBarCall0)(const void *, int *);
typedef const QSize * (*CuteQMenuBarCall1)(const void *, int *);
typedef int (*CuteQMenuBarCall2)(const void *, int, int *);
typedef void (*CuteQMenuBarCall3)(const void *, bool, int *);
typedef void (*CuteQMenuBarCall4)(const void *, QEvent *, int *);
typedef void (*CuteQMenuBarCall5)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMenuBarCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuBarCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuBarCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuBarCall9)(const void *, QEvent *, int *);
typedef void (*CuteQMenuBarCall10)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMenuBarCall11)(const void *, QResizeEvent *, int *);
typedef void (*CuteQMenuBarCall12)(const void *, QActionEvent *, int *);
typedef void (*CuteQMenuBarCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMenuBarCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMenuBarCall15)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQMenuBarCall16)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQMenuBarCall17)(const void *, QEvent *, int *);
typedef void (*CuteQMenuBarCall18)(const void *, QStyleOptionMenuItem *, const QAction *, int *);
typedef int (*CuteQMenuBarCall19)(const void *, int *);
typedef bool (*CuteQMenuBarCall20)(const void *, int *);
typedef void * (*CuteQMenuBarCall21)(const void *, int *);
typedef void (*CuteQMenuBarCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuBarCall23)(const void *, QWheelEvent *, int *);
typedef void (*CuteQMenuBarCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMenuBarCall25)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMenuBarCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQMenuBarCall27)(const void *, QCloseEvent *, int *);
typedef void (*CuteQMenuBarCall28)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQMenuBarCall29)(const void *, QTabletEvent *, int *);
typedef void (*CuteQMenuBarCall30)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQMenuBarCall31)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQMenuBarCall32)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQMenuBarCall33)(const void *, QDropEvent *, int *);
typedef void (*CuteQMenuBarCall34)(const void *, QShowEvent *, int *);
typedef void (*CuteQMenuBarCall35)(const void *, QHideEvent *, int *);
typedef int (*CuteQMenuBarCall36)(const void *, int, int *);
typedef void (*CuteQMenuBarCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQMenuBarCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQMenuBarCall39)(const void *, int *);
typedef void (*CuteQMenuBarCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMenuBarCall41)(const void *, int, int *);
typedef bool (*CuteQMenuBarCall42)(const void *, bool, int *);
typedef void (*CuteQMenuBarCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQMenuBarCall44)(const void *, QEvent *, int *);
typedef void (*CuteQMenuBarCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQMenuBarCall46)(const void *, const QMetaMethod *, int *);
class CuteQMenuBar : public QMenuBar {
public:
  using QMenuBar::QMenuBar;
  void *taken[47] = {};

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
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItemPK7QAction")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
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

  //  QSize QMenuBar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMenuBarCall0 call = reinterpret_cast<CuteQMenuBarCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenuBar::sizeHint();
  }

  //  QSize QMenuBar::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMenuBarCall1 call = reinterpret_cast<CuteQMenuBarCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenuBar::minimumSizeHint();
  }

  //  int QMenuBar::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMenuBarCall2 call = reinterpret_cast<CuteQMenuBarCall2>(taken[2]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenuBar::heightForWidth(a0);
  }

  //  void QMenuBar::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMenuBarCall3 call = reinterpret_cast<CuteQMenuBarCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QMenuBar::setVisible(visible);
  }

  //  void QMenuBar::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMenuBarCall4 call = reinterpret_cast<CuteQMenuBarCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::changeEvent(a0);
  }

  //  void QMenuBar::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMenuBarCall5 call = reinterpret_cast<CuteQMenuBarCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::keyPressEvent(a0);
  }

  //  void QMenuBar::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMenuBarCall6 call = reinterpret_cast<CuteQMenuBarCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mouseReleaseEvent(a0);
  }

  //  void QMenuBar::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMenuBarCall7 call = reinterpret_cast<CuteQMenuBarCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mousePressEvent(a0);
  }

  //  void QMenuBar::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMenuBarCall8 call = reinterpret_cast<CuteQMenuBarCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mouseMoveEvent(a0);
  }

  //  void QMenuBar::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQMenuBarCall9 call = reinterpret_cast<CuteQMenuBarCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::leaveEvent(a0);
  }

  //  void QMenuBar::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMenuBarCall10 call = reinterpret_cast<CuteQMenuBarCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::paintEvent(a0);
  }

  //  void QMenuBar::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMenuBarCall11 call = reinterpret_cast<CuteQMenuBarCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::resizeEvent(a0);
  }

  //  void QMenuBar::actionEvent(QActionEvent *a0)
  void actionEvent(QActionEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMenuBarCall12 call = reinterpret_cast<CuteQMenuBarCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::actionEvent(a0);
  }

  //  void QMenuBar::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMenuBarCall13 call = reinterpret_cast<CuteQMenuBarCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::focusOutEvent(a0);
  }

  //  void QMenuBar::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMenuBarCall14 call = reinterpret_cast<CuteQMenuBarCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::focusInEvent(a0);
  }

  //  void QMenuBar::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQMenuBarCall15 call = reinterpret_cast<CuteQMenuBarCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::timerEvent(a0);
  }

  //  bool QMenuBar::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQMenuBarCall16 call = reinterpret_cast<CuteQMenuBarCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QMenuBar::eventFilter(a0, a1);
  }

  //  bool QMenuBar::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQMenuBarCall17 call = reinterpret_cast<CuteQMenuBarCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenuBar::event(a0);
  }

  //  void QMenuBar::initStyleOption(QStyleOptionMenuItem *option, const
  //      QAction *action) const
  void initStyleOption(
      QStyleOptionMenuItem *option,
      const QAction *action) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQMenuBarCall18 call = reinterpret_cast<CuteQMenuBarCall18>(taken[18]);
      call(this, option, action, &handled);
      if (handled) return;
    }
    QMenuBar::initStyleOption(option, action);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQMenuBarCall19 call = reinterpret_cast<CuteQMenuBarCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQMenuBarCall20 call = reinterpret_cast<CuteQMenuBarCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQMenuBarCall21 call = reinterpret_cast<CuteQMenuBarCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMenuBarCall22 call = reinterpret_cast<CuteQMenuBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMenuBarCall23 call = reinterpret_cast<CuteQMenuBarCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQMenuBarCall24 call = reinterpret_cast<CuteQMenuBarCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQMenuBarCall25 call = reinterpret_cast<CuteQMenuBarCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQMenuBarCall26 call = reinterpret_cast<CuteQMenuBarCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMenuBarCall27 call = reinterpret_cast<CuteQMenuBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQMenuBarCall28 call = reinterpret_cast<CuteQMenuBarCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQMenuBarCall29 call = reinterpret_cast<CuteQMenuBarCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQMenuBarCall30 call = reinterpret_cast<CuteQMenuBarCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMenuBarCall31 call = reinterpret_cast<CuteQMenuBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQMenuBarCall32 call = reinterpret_cast<CuteQMenuBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQMenuBarCall33 call = reinterpret_cast<CuteQMenuBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQMenuBarCall34 call = reinterpret_cast<CuteQMenuBarCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQMenuBarCall35 call = reinterpret_cast<CuteQMenuBarCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQMenuBarCall36 call = reinterpret_cast<CuteQMenuBarCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQMenuBarCall37 call = reinterpret_cast<CuteQMenuBarCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQMenuBarCall38 call = reinterpret_cast<CuteQMenuBarCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQMenuBarCall39 call = reinterpret_cast<CuteQMenuBarCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQMenuBarCall40 call = reinterpret_cast<CuteQMenuBarCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQMenuBarCall41 call = reinterpret_cast<CuteQMenuBarCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQMenuBarCall42 call = reinterpret_cast<CuteQMenuBarCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQMenuBarCall43 call = reinterpret_cast<CuteQMenuBarCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQMenuBarCall44 call = reinterpret_cast<CuteQMenuBarCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMenuBarCall45 call = reinterpret_cast<CuteQMenuBarCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQMenuBarCall46 call = reinterpret_cast<CuteQMenuBarCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QMenuBar10metaObjectEv(const QMenuBar *self) {
  return self->metaObject();
}

//  QString QMenuBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QMenuBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMenuBar::tr(s, c, n));
}

//  QMenuBar::QMenuBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZN8QMenuBarC1EP7QWidget(QWidget *parent) {
  return new CuteQMenuBar(parent);
}

//  QMenuBar::~QMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBarD1Ev(QMenuBar *self) {
  delete self;
}

//  QAction *QMenuBar::addMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar7addMenuEP5QMenu(QMenuBar *self, QMenu *menu) {
  return self->addMenu(menu);
}

//  QMenu *QMenuBar::addMenu(const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN8QMenuBar7addMenuERK7QString(
    QMenuBar *self,
    const QString *title) {
  return self->addMenu(*title);
}

//  QMenu *QMenuBar::addMenu(const QIcon &icon, const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN8QMenuBar7addMenuERK5QIconRK7QString(
    QMenuBar *self,
    const QIcon *icon,
    const QString *title) {
  return self->addMenu(*icon, *title);
}

//  QAction *QMenuBar::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar12addSeparatorEv(QMenuBar *self) {
  return self->addSeparator();
}

//  QAction *QMenuBar::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar15insertSeparatorEP7QAction(
    QMenuBar *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QMenuBar::insertMenu(QAction *before, QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar10insertMenuEP7QActionP5QMenu(
    QMenuBar *self,
    QAction *before,
    QMenu *menu) {
  return self->insertMenu(before, menu);
}

//  void QMenuBar::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar5clearEv(QMenuBar *self) {
  self->clear();
}

//  QAction *QMenuBar::activeAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QMenuBar12activeActionEv(const QMenuBar *self) {
  return self->activeAction();
}

//  void QMenuBar::setActiveAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar15setActiveActionEP7QAction(
    QMenuBar *self,
    QAction *action) {
  self->setActiveAction(action);
}

//  void QMenuBar::setDefaultUp(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar12setDefaultUpEb(QMenuBar *self, bool a0) {
  self->setDefaultUp(a0);
}

//  bool QMenuBar::isDefaultUp() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMenuBar11isDefaultUpEv(const QMenuBar *self) {
  return self->isDefaultUp();
}

//  QSize QMenuBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMenuBar8sizeHintEv(const QMenuBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMenuBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMenuBar15minimumSizeHintEv(const QMenuBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QMenuBar::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMenuBar14heightForWidthEi(const QMenuBar *self, int a0) {
  return self->heightForWidth(a0);
}

//  QRect QMenuBar::actionGeometry(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QMenuBar14actionGeometryEP7QAction(
    const QMenuBar *self,
    QAction *a0) {
  return new QRect(self->actionGeometry(a0));
}

//  QAction *QMenuBar::actionAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QMenuBar8actionAtERK6QPoint(
    const QMenuBar *self,
    const QPoint *a0) {
  return self->actionAt(*a0);
}

//  void QMenuBar::setCornerWidget(QWidget *w, Qt::Corner corner)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar15setCornerWidgetEP7QWidgetN2Qt6CornerE(
    QMenuBar *self,
    QWidget *w,
    Qt::Corner corner) {
  self->setCornerWidget(w, corner);
}

//  QWidget *QMenuBar::cornerWidget(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QMenuBar12cornerWidgetEN2Qt6CornerE(
    const QMenuBar *self,
    Qt::Corner corner) {
  return self->cornerWidget(corner);
}

//  bool QMenuBar::isNativeMenuBar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMenuBar15isNativeMenuBarEv(const QMenuBar *self) {
  return self->isNativeMenuBar();
}

//  void QMenuBar::setNativeMenuBar(bool nativeMenuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar16setNativeMenuBarEb(
    QMenuBar *self,
    bool nativeMenuBar) {
  self->setNativeMenuBar(nativeMenuBar);
}

//  void QMenuBar::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar10setVisibleEb(QMenuBar *self, bool visible) {
  self->setVisible(visible);
}

//  a Python function taken by a CuteQMenuBar, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMenuBar(QMenuBar *self, const char *key, void *call) {
  return static_cast<CuteQMenuBar *>(self)->take(key, call);
}

//  QSize QMenuBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK8QMenuBar8sizeHintEv(const QMenuBar *self) {
  return new QSize(self->QMenuBar::sizeHint());
}

//  QSize QMenuBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK8QMenuBar15minimumSizeHintEv(const QMenuBar *self) {
  return new QSize(self->QMenuBar::minimumSizeHint());
}

//  int QMenuBar::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QMenuBar14heightForWidthEi(const QMenuBar *self, int a0) {
  return self->QMenuBar::heightForWidth(a0);
}

//  void QMenuBar::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar10setVisibleEb(QMenuBar *self, bool visible) {
  self->QMenuBar::setVisible(visible);
}

//  void QMenuBar::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar11changeEventEP6QEvent(
    QMenuBar *self,
    QEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::changeEvent(a0);
}

//  void QMenuBar::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar13keyPressEventEP9QKeyEvent(
    QMenuBar *self,
    QKeyEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::keyPressEvent(a0);
}

//  void QMenuBar::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar17mouseReleaseEventEP11QMouseEvent(
    QMenuBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::mouseReleaseEvent(a0);
}

//  void QMenuBar::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar15mousePressEventEP11QMouseEvent(
    QMenuBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::mousePressEvent(a0);
}

//  void QMenuBar::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar14mouseMoveEventEP11QMouseEvent(
    QMenuBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::mouseMoveEvent(a0);
}

//  void QMenuBar::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar10leaveEventEP6QEvent(
    QMenuBar *self,
    QEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::leaveEvent(a0);
}

//  void QMenuBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar10paintEventEP11QPaintEvent(
    QMenuBar *self,
    QPaintEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::paintEvent(a0);
}

//  void QMenuBar::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar11resizeEventEP12QResizeEvent(
    QMenuBar *self,
    QResizeEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::resizeEvent(a0);
}

//  void QMenuBar::actionEvent(QActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar11actionEventEP12QActionEvent(
    QMenuBar *self,
    QActionEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::actionEvent(a0);
}

//  void QMenuBar::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar13focusOutEventEP11QFocusEvent(
    QMenuBar *self,
    QFocusEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::focusOutEvent(a0);
}

//  void QMenuBar::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar12focusInEventEP11QFocusEvent(
    QMenuBar *self,
    QFocusEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::focusInEvent(a0);
}

//  void QMenuBar::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMenuBar10timerEventEP11QTimerEvent(
    QMenuBar *self,
    QTimerEvent *a0) {
  static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::timerEvent(a0);
}

//  bool QMenuBar::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QMenuBar11eventFilterEP7QObjectP6QEvent(
    QMenuBar *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::eventFilter(a0, a1);
}

//  bool QMenuBar::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QMenuBar5eventEP6QEvent(QMenuBar *self, QEvent *a0) {
  return static_cast<OwnQMenuBar *>(self)->OwnQMenuBar::event(a0);
}

//  void QMenuBar::initStyleOption(QStyleOptionMenuItem *option, const
//      QAction *action) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItemPK7QAction(
    const QMenuBar *self,
    QStyleOptionMenuItem *option,
    const QAction *action) {
  static_cast<const OwnQMenuBar *>(self)->OwnQMenuBar::initStyleOption(
      option,
      action);
}
