//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmenu.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmenu.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qicon.h>
#include <QtCore/qpoint.h>
#include <QtGui/qaction.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMenu may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMenu : QMenu {
  using QMenu::changeEvent;
  using QMenu::keyPressEvent;
  using QMenu::mouseReleaseEvent;
  using QMenu::mousePressEvent;
  using QMenu::mouseMoveEvent;
  using QMenu::wheelEvent;
  using QMenu::enterEvent;
  using QMenu::leaveEvent;
  using QMenu::hideEvent;
  using QMenu::paintEvent;
  using QMenu::actionEvent;
  using QMenu::timerEvent;
  using QMenu::event;
  using QMenu::focusNextPrevChild;
  using QMenu::initStyleOption;
};

//  A QMenu that Python can take functions over in. Every QMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQMenuCall0)(const void *, int *);
typedef void (*CuteQMenuCall1)(const void *, QEvent *, int *);
typedef void (*CuteQMenuCall2)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMenuCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuCall6)(const void *, QWheelEvent *, int *);
typedef void (*CuteQMenuCall7)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMenuCall8)(const void *, QEvent *, int *);
typedef void (*CuteQMenuCall9)(const void *, QHideEvent *, int *);
typedef void (*CuteQMenuCall10)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMenuCall11)(const void *, QActionEvent *, int *);
typedef void (*CuteQMenuCall12)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQMenuCall13)(const void *, QEvent *, int *);
typedef bool (*CuteQMenuCall14)(const void *, bool, int *);
typedef void (*CuteQMenuCall15)(const void *, QStyleOptionMenuItem *, const QAction *, int *);
typedef int (*CuteQMenuCall16)(const void *, int *);
typedef void (*CuteQMenuCall17)(const void *, bool, int *);
typedef const QSize * (*CuteQMenuCall18)(const void *, int *);
typedef int (*CuteQMenuCall19)(const void *, int, int *);
typedef bool (*CuteQMenuCall20)(const void *, int *);
typedef void * (*CuteQMenuCall21)(const void *, int *);
typedef void (*CuteQMenuCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMenuCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMenuCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMenuCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMenuCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQMenuCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQMenuCall28)(const void *, QCloseEvent *, int *);
typedef void (*CuteQMenuCall29)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQMenuCall30)(const void *, QTabletEvent *, int *);
typedef void (*CuteQMenuCall31)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQMenuCall32)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQMenuCall33)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQMenuCall34)(const void *, QDropEvent *, int *);
typedef void (*CuteQMenuCall35)(const void *, QShowEvent *, int *);
typedef int (*CuteQMenuCall36)(const void *, int, int *);
typedef void (*CuteQMenuCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQMenuCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQMenuCall39)(const void *, int *);
typedef void (*CuteQMenuCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMenuCall41)(const void *, int, int *);
typedef bool (*CuteQMenuCall42)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQMenuCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQMenuCall44)(const void *, QEvent *, int *);
typedef void (*CuteQMenuCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQMenuCall46)(const void *, const QMetaMethod *, int *);
class CuteQMenu : public QMenu {
public:
  using QMenu::QMenu;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7QAction")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  QSize QMenu::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMenuCall0 call = reinterpret_cast<CuteQMenuCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenu::sizeHint();
  }

  //  void QMenu::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMenuCall1 call = reinterpret_cast<CuteQMenuCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::changeEvent(a0);
  }

  //  void QMenu::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMenuCall2 call = reinterpret_cast<CuteQMenuCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::keyPressEvent(a0);
  }

  //  void QMenu::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMenuCall3 call = reinterpret_cast<CuteQMenuCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mouseReleaseEvent(a0);
  }

  //  void QMenu::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMenuCall4 call = reinterpret_cast<CuteQMenuCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mousePressEvent(a0);
  }

  //  void QMenu::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMenuCall5 call = reinterpret_cast<CuteQMenuCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mouseMoveEvent(a0);
  }

  //  void QMenu::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMenuCall6 call = reinterpret_cast<CuteQMenuCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::wheelEvent(a0);
  }

  //  void QMenu::enterEvent(QEnterEvent *a0)
  void enterEvent(QEnterEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMenuCall7 call = reinterpret_cast<CuteQMenuCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::enterEvent(a0);
  }

  //  void QMenu::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMenuCall8 call = reinterpret_cast<CuteQMenuCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::leaveEvent(a0);
  }

  //  void QMenu::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQMenuCall9 call = reinterpret_cast<CuteQMenuCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::hideEvent(a0);
  }

  //  void QMenu::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMenuCall10 call = reinterpret_cast<CuteQMenuCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::paintEvent(a0);
  }

  //  void QMenu::actionEvent(QActionEvent *a0)
  void actionEvent(QActionEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMenuCall11 call = reinterpret_cast<CuteQMenuCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::actionEvent(a0);
  }

  //  void QMenu::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMenuCall12 call = reinterpret_cast<CuteQMenuCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::timerEvent(a0);
  }

  //  bool QMenu::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMenuCall13 call = reinterpret_cast<CuteQMenuCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenu::event(a0);
  }

  //  bool QMenu::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMenuCall14 call = reinterpret_cast<CuteQMenuCall14>(taken[14]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QMenu::focusNextPrevChild(next);
  }

  //  void QMenu::initStyleOption(QStyleOptionMenuItem *option, const
  //      QAction *action) const
  void initStyleOption(
      QStyleOptionMenuItem *option,
      const QAction *action) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQMenuCall15 call = reinterpret_cast<CuteQMenuCall15>(taken[15]);
      call(this, option, action, &handled);
      if (handled) return;
    }
    QMenu::initStyleOption(option, action);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQMenuCall16 call = reinterpret_cast<CuteQMenuCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[17]) {
      int handled = 0;
      CuteQMenuCall17 call = reinterpret_cast<CuteQMenuCall17>(taken[17]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQMenuCall18 call = reinterpret_cast<CuteQMenuCall18>(taken[18]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQMenuCall19 call = reinterpret_cast<CuteQMenuCall19>(taken[19]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQMenuCall20 call = reinterpret_cast<CuteQMenuCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQMenuCall21 call = reinterpret_cast<CuteQMenuCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMenuCall22 call = reinterpret_cast<CuteQMenuCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMenuCall23 call = reinterpret_cast<CuteQMenuCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQMenuCall24 call = reinterpret_cast<CuteQMenuCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQMenuCall25 call = reinterpret_cast<CuteQMenuCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQMenuCall26 call = reinterpret_cast<CuteQMenuCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMenuCall27 call = reinterpret_cast<CuteQMenuCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQMenuCall28 call = reinterpret_cast<CuteQMenuCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQMenuCall29 call = reinterpret_cast<CuteQMenuCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQMenuCall30 call = reinterpret_cast<CuteQMenuCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMenuCall31 call = reinterpret_cast<CuteQMenuCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQMenuCall32 call = reinterpret_cast<CuteQMenuCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQMenuCall33 call = reinterpret_cast<CuteQMenuCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQMenuCall34 call = reinterpret_cast<CuteQMenuCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQMenuCall35 call = reinterpret_cast<CuteQMenuCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQMenuCall36 call = reinterpret_cast<CuteQMenuCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQMenuCall37 call = reinterpret_cast<CuteQMenuCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQMenuCall38 call = reinterpret_cast<CuteQMenuCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQMenuCall39 call = reinterpret_cast<CuteQMenuCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQMenuCall40 call = reinterpret_cast<CuteQMenuCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQMenuCall41 call = reinterpret_cast<CuteQMenuCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQMenuCall42 call = reinterpret_cast<CuteQMenuCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQMenuCall43 call = reinterpret_cast<CuteQMenuCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQMenuCall44 call = reinterpret_cast<CuteQMenuCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMenuCall45 call = reinterpret_cast<CuteQMenuCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQMenuCall46 call = reinterpret_cast<CuteQMenuCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QMenu10metaObjectEv(const QMenu *self) {
  return self->metaObject();
}

//  QString QMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QMenu2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMenu::tr(s, c, n));
}

//  QMenu::QMenu(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenuC1EP7QWidget(QWidget *parent) {
  return new CuteQMenu(parent);
}

//  QMenu::QMenu(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenuC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new CuteQMenu(*title, parent);
}

//  QMenu::~QMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenuD1Ev(QMenu *self) {
  delete self;
}

//  QAction *QMenu::addAction(const QString &text, const QObject *receiver,
//      const char *member, const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu9addActionERK7QStringPK7QObjectPKcRK12QKeySequence(
    QMenu *self,
    const QString *text,
    const QObject *receiver,
    const char *member,
    const QKeySequence *shortcut) {
  return self->addAction(*text, receiver, member, *shortcut);
}

//  QAction *QMenu::addAction(const QIcon &icon, const QString &text, const
//      QObject *receiver, const char *member, const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu9addActionERK5QIconRK7QStringPK7QObjectPKcRK12QKeySequence(
    QMenu *self,
    const QIcon *icon,
    const QString *text,
    const QObject *receiver,
    const char *member,
    const QKeySequence *shortcut) {
  return self->addAction(*icon, *text, receiver, member, *shortcut);
}

//  QAction *QMenu::addMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu7addMenuEPS_(QMenu *self, QMenu *menu) {
  return self->addMenu(menu);
}

//  QMenu *QMenu::addMenu(const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu7addMenuERK7QString(
    QMenu *self,
    const QString *title) {
  return self->addMenu(*title);
}

//  QMenu *QMenu::addMenu(const QIcon &icon, const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu7addMenuERK5QIconRK7QString(
    QMenu *self,
    const QIcon *icon,
    const QString *title) {
  return self->addMenu(*icon, *title);
}

//  QAction *QMenu::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu12addSeparatorEv(QMenu *self) {
  return self->addSeparator();
}

//  QAction *QMenu::addSection(const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10addSectionERK7QString(
    QMenu *self,
    const QString *text) {
  return self->addSection(*text);
}

//  QAction *QMenu::addSection(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10addSectionERK5QIconRK7QString(
    QMenu *self,
    const QIcon *icon,
    const QString *text) {
  return self->addSection(*icon, *text);
}

//  QAction *QMenu::insertMenu(QAction *before, QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10insertMenuEP7QActionPS_(
    QMenu *self,
    QAction *before,
    QMenu *menu) {
  return self->insertMenu(before, menu);
}

//  QAction *QMenu::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu15insertSeparatorEP7QAction(
    QMenu *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QMenu::insertSection(QAction *before, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu13insertSectionEP7QActionRK7QString(
    QMenu *self,
    QAction *before,
    const QString *text) {
  return self->insertSection(before, *text);
}

//  QAction *QMenu::insertSection(QAction *before, const QIcon &icon, const
//      QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu13insertSectionEP7QActionRK5QIconRK7QString(
    QMenu *self,
    QAction *before,
    const QIcon *icon,
    const QString *text) {
  return self->insertSection(before, *icon, *text);
}

//  bool QMenu::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu7isEmptyEv(const QMenu *self) {
  return self->isEmpty();
}

//  void QMenu::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu5clearEv(QMenu *self) {
  self->clear();
}

//  void QMenu::setTearOffEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu17setTearOffEnabledEb(QMenu *self, bool a0) {
  self->setTearOffEnabled(a0);
}

//  bool QMenu::isTearOffEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu16isTearOffEnabledEv(const QMenu *self) {
  return self->isTearOffEnabled();
}

//  bool QMenu::isTearOffMenuVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu20isTearOffMenuVisibleEv(const QMenu *self) {
  return self->isTearOffMenuVisible();
}

//  void QMenu::showTearOffMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15showTearOffMenuEv(QMenu *self) {
  self->showTearOffMenu();
}

//  void QMenu::showTearOffMenu(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15showTearOffMenuERK6QPoint(
    QMenu *self,
    const QPoint *pos) {
  self->showTearOffMenu(*pos);
}

//  void QMenu::hideTearOffMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15hideTearOffMenuEv(QMenu *self) {
  self->hideTearOffMenu();
}

//  void QMenu::setDefaultAction(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu16setDefaultActionEP7QAction(QMenu *self, QAction *a0) {
  self->setDefaultAction(a0);
}

//  QAction *QMenu::defaultAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu13defaultActionEv(const QMenu *self) {
  return self->defaultAction();
}

//  void QMenu::setActiveAction(QAction *act)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15setActiveActionEP7QAction(QMenu *self, QAction *act) {
  self->setActiveAction(act);
}

//  QAction *QMenu::activeAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu12activeActionEv(const QMenu *self) {
  return self->activeAction();
}

//  void QMenu::popup(const QPoint &pos, QAction *at)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu5popupERK6QPointP7QAction(
    QMenu *self,
    const QPoint *pos,
    QAction *at) {
  self->popup(*pos, at);
}

//  QAction *QMenu::exec()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu4execEv(QMenu *self) {
  return self->exec();
}

//  QAction *QMenu::exec(const QPoint &pos, QAction *at)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu4execERK6QPointP7QAction(
    QMenu *self,
    const QPoint *pos,
    QAction *at) {
  return self->exec(*pos, at);
}

//  QAction *QMenu::exec(const QList<QAction *> &actions, const QPoint &pos,
//      QAction *at, QWidget *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu4execERK5QListIP7QActionERK6QPointS2_P7QWidget(
    const QList<QAction *> *actions,
    const QPoint *pos,
    QAction *at,
    QWidget *parent) {
  return QMenu::exec(*actions, *pos, at, parent);
}

//  QSize QMenu::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QMenu8sizeHintEv(const QMenu *self) {
  return new QSize(self->sizeHint());
}

//  QRect QMenu::actionGeometry(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QMenu14actionGeometryEP7QAction(
    const QMenu *self,
    QAction *a0) {
  return new QRect(self->actionGeometry(a0));
}

//  QAction *QMenu::actionAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu8actionAtERK6QPoint(
    const QMenu *self,
    const QPoint *a0) {
  return self->actionAt(*a0);
}

//  QAction *QMenu::menuAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu10menuActionEv(const QMenu *self) {
  return self->menuAction();
}

//  QMenu *QMenu::menuInAction(const QAction *action)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu12menuInActionEPK7QAction(const QAction *action) {
  return QMenu::menuInAction(action);
}

//  QString QMenu::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QMenu5titleEv(const QMenu *self) {
  return new QString(self->title());
}

//  void QMenu::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu8setTitleERK7QString(QMenu *self, const QString *title) {
  self->setTitle(*title);
}

//  QIcon QMenu::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK5QMenu4iconEv(const QMenu *self) {
  return new QIcon(self->icon());
}

//  void QMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu7setIconERK5QIcon(QMenu *self, const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QMenu::setNoReplayFor(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu14setNoReplayForEP7QWidget(
    QMenu *self,
    QWidget *widget) {
  self->setNoReplayFor(widget);
}

//  bool QMenu::separatorsCollapsible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu21separatorsCollapsibleEv(const QMenu *self) {
  return self->separatorsCollapsible();
}

//  void QMenu::setSeparatorsCollapsible(bool collapse)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu24setSeparatorsCollapsibleEb(
    QMenu *self,
    bool collapse) {
  self->setSeparatorsCollapsible(collapse);
}

//  bool QMenu::toolTipsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu15toolTipsVisibleEv(const QMenu *self) {
  return self->toolTipsVisible();
}

//  void QMenu::setToolTipsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu18setToolTipsVisibleEb(QMenu *self, bool visible) {
  self->setToolTipsVisible(visible);
}

//  a Python function taken by a CuteQMenu, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMenu(QMenu *self, const char *key, void *call) {
  return static_cast<CuteQMenu *>(self)->take(key, call);
}

//  QSize QMenu::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK5QMenu8sizeHintEv(const QMenu *self) {
  return new QSize(self->QMenu::sizeHint());
}

//  void QMenu::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu11changeEventEP6QEvent(QMenu *self, QEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::changeEvent(a0);
}

//  void QMenu::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu13keyPressEventEP9QKeyEvent(
    QMenu *self,
    QKeyEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::keyPressEvent(a0);
}

//  void QMenu::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu17mouseReleaseEventEP11QMouseEvent(
    QMenu *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::mouseReleaseEvent(a0);
}

//  void QMenu::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu15mousePressEventEP11QMouseEvent(
    QMenu *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::mousePressEvent(a0);
}

//  void QMenu::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu14mouseMoveEventEP11QMouseEvent(
    QMenu *self,
    QMouseEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::mouseMoveEvent(a0);
}

//  void QMenu::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu10wheelEventEP11QWheelEvent(
    QMenu *self,
    QWheelEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::wheelEvent(a0);
}

//  void QMenu::enterEvent(QEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu10enterEventEP11QEnterEvent(
    QMenu *self,
    QEnterEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::enterEvent(a0);
}

//  void QMenu::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu10leaveEventEP6QEvent(QMenu *self, QEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::leaveEvent(a0);
}

//  void QMenu::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu9hideEventEP10QHideEvent(
    QMenu *self,
    QHideEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::hideEvent(a0);
}

//  void QMenu::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu10paintEventEP11QPaintEvent(
    QMenu *self,
    QPaintEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::paintEvent(a0);
}

//  void QMenu::actionEvent(QActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu11actionEventEP12QActionEvent(
    QMenu *self,
    QActionEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::actionEvent(a0);
}

//  void QMenu::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QMenu10timerEventEP11QTimerEvent(
    QMenu *self,
    QTimerEvent *a0) {
  static_cast<OwnQMenu *>(self)->OwnQMenu::timerEvent(a0);
}

//  bool QMenu::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QMenu5eventEP6QEvent(QMenu *self, QEvent *a0) {
  return static_cast<OwnQMenu *>(self)->OwnQMenu::event(a0);
}

//  bool QMenu::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QMenu18focusNextPrevChildEb(QMenu *self, bool next) {
  return static_cast<OwnQMenu *>(self)->OwnQMenu::focusNextPrevChild(next);
}

//  void QMenu::initStyleOption(QStyleOptionMenuItem *option, const QAction
//      *action) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7QAction(
    const QMenu *self,
    QStyleOptionMenuItem *option,
    const QAction *action) {
  static_cast<const OwnQMenu *>(self)->OwnQMenu::initStyleOption(
      option,
      action);
}
