//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractbutton.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstractButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractButton : QAbstractButton {
  using QAbstractButton::hitButton;
  using QAbstractButton::checkStateSet;
  using QAbstractButton::nextCheckState;
  using QAbstractButton::event;
  using QAbstractButton::keyPressEvent;
  using QAbstractButton::keyReleaseEvent;
  using QAbstractButton::mousePressEvent;
  using QAbstractButton::mouseReleaseEvent;
  using QAbstractButton::mouseMoveEvent;
  using QAbstractButton::focusInEvent;
  using QAbstractButton::focusOutEvent;
  using QAbstractButton::changeEvent;
  using QAbstractButton::timerEvent;
};

//  A QAbstractButton that Python can take functions over in. Every QAbstractButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractButtonCall0)(const void *, QPaintEvent *, int *);
typedef bool (*CuteQAbstractButtonCall1)(const void *, const QPoint *, int *);
typedef void (*CuteQAbstractButtonCall2)(const void *, int *);
typedef void (*CuteQAbstractButtonCall3)(const void *, int *);
typedef bool (*CuteQAbstractButtonCall4)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractButtonCall5)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractButtonCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractButtonCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractButtonCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractButtonCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractButtonCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractButtonCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractButtonCall12)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractButtonCall13)(const void *, QTimerEvent *, int *);
typedef int (*CuteQAbstractButtonCall14)(const void *, int *);
typedef void (*CuteQAbstractButtonCall15)(const void *, bool, int *);
typedef const QSize * (*CuteQAbstractButtonCall16)(const void *, int *);
typedef const QSize * (*CuteQAbstractButtonCall17)(const void *, int *);
typedef int (*CuteQAbstractButtonCall18)(const void *, int, int *);
typedef bool (*CuteQAbstractButtonCall19)(const void *, int *);
typedef void * (*CuteQAbstractButtonCall20)(const void *, int *);
typedef void (*CuteQAbstractButtonCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractButtonCall22)(const void *, QWheelEvent *, int *);
typedef void (*CuteQAbstractButtonCall23)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractButtonCall24)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractButtonCall25)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstractButtonCall26)(const void *, QResizeEvent *, int *);
typedef void (*CuteQAbstractButtonCall27)(const void *, QCloseEvent *, int *);
typedef void (*CuteQAbstractButtonCall28)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQAbstractButtonCall29)(const void *, QTabletEvent *, int *);
typedef void (*CuteQAbstractButtonCall30)(const void *, QActionEvent *, int *);
typedef void (*CuteQAbstractButtonCall31)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQAbstractButtonCall32)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQAbstractButtonCall33)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQAbstractButtonCall34)(const void *, QDropEvent *, int *);
typedef void (*CuteQAbstractButtonCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstractButtonCall36)(const void *, QHideEvent *, int *);
typedef int (*CuteQAbstractButtonCall37)(const void *, int, int *);
typedef void (*CuteQAbstractButtonCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractButtonCall39)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractButtonCall40)(const void *, int *);
typedef void (*CuteQAbstractButtonCall41)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAbstractButtonCall42)(const void *, int, int *);
typedef bool (*CuteQAbstractButtonCall43)(const void *, bool, int *);
typedef bool (*CuteQAbstractButtonCall44)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAbstractButtonCall45)(const void *, QChildEvent *, int *);
typedef void (*CuteQAbstractButtonCall46)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractButtonCall47)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAbstractButtonCall48)(const void *, const QMetaMethod *, int *);
class CuteQAbstractButton : public QAbstractButton {
public:
  using QAbstractButton::QAbstractButton;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  void QAbstractButton::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractButtonCall0 call = reinterpret_cast<CuteQAbstractButtonCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
  }

  //  bool QAbstractButton::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractButtonCall1 call = reinterpret_cast<CuteQAbstractButtonCall1>(taken[1]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QAbstractButton::hitButton(pos);
  }

  //  void QAbstractButton::checkStateSet()
  void checkStateSet() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractButtonCall2 call = reinterpret_cast<CuteQAbstractButtonCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::checkStateSet();
  }

  //  void QAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractButtonCall3 call = reinterpret_cast<CuteQAbstractButtonCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::nextCheckState();
  }

  //  bool QAbstractButton::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractButtonCall4 call = reinterpret_cast<CuteQAbstractButtonCall4>(taken[4]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QAbstractButton::event(e);
  }

  //  void QAbstractButton::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractButtonCall5 call = reinterpret_cast<CuteQAbstractButtonCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyPressEvent(e);
  }

  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractButtonCall6 call = reinterpret_cast<CuteQAbstractButtonCall6>(taken[6]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }

  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractButtonCall7 call = reinterpret_cast<CuteQAbstractButtonCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }

  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractButtonCall8 call = reinterpret_cast<CuteQAbstractButtonCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }

  //  void QAbstractButton::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractButtonCall9 call = reinterpret_cast<CuteQAbstractButtonCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseMoveEvent(e);
  }

  //  void QAbstractButton::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractButtonCall10 call = reinterpret_cast<CuteQAbstractButtonCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusInEvent(e);
  }

  //  void QAbstractButton::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractButtonCall11 call = reinterpret_cast<CuteQAbstractButtonCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusOutEvent(e);
  }

  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractButtonCall12 call = reinterpret_cast<CuteQAbstractButtonCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }

  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractButtonCall13 call = reinterpret_cast<CuteQAbstractButtonCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractButtonCall14 call = reinterpret_cast<CuteQAbstractButtonCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractButtonCall15 call = reinterpret_cast<CuteQAbstractButtonCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractButtonCall16 call = reinterpret_cast<CuteQAbstractButtonCall16>(taken[16]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractButtonCall17 call = reinterpret_cast<CuteQAbstractButtonCall17>(taken[17]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractButtonCall18 call = reinterpret_cast<CuteQAbstractButtonCall18>(taken[18]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractButtonCall19 call = reinterpret_cast<CuteQAbstractButtonCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractButtonCall20 call = reinterpret_cast<CuteQAbstractButtonCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractButtonCall21 call = reinterpret_cast<CuteQAbstractButtonCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractButtonCall22 call = reinterpret_cast<CuteQAbstractButtonCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractButtonCall23 call = reinterpret_cast<CuteQAbstractButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractButtonCall24 call = reinterpret_cast<CuteQAbstractButtonCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractButtonCall25 call = reinterpret_cast<CuteQAbstractButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractButtonCall26 call = reinterpret_cast<CuteQAbstractButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractButtonCall27 call = reinterpret_cast<CuteQAbstractButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractButtonCall28 call = reinterpret_cast<CuteQAbstractButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractButtonCall29 call = reinterpret_cast<CuteQAbstractButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractButtonCall30 call = reinterpret_cast<CuteQAbstractButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractButtonCall31 call = reinterpret_cast<CuteQAbstractButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractButtonCall32 call = reinterpret_cast<CuteQAbstractButtonCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractButtonCall33 call = reinterpret_cast<CuteQAbstractButtonCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractButtonCall34 call = reinterpret_cast<CuteQAbstractButtonCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractButtonCall35 call = reinterpret_cast<CuteQAbstractButtonCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractButtonCall36 call = reinterpret_cast<CuteQAbstractButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractButtonCall37 call = reinterpret_cast<CuteQAbstractButtonCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractButtonCall38 call = reinterpret_cast<CuteQAbstractButtonCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractButtonCall39 call = reinterpret_cast<CuteQAbstractButtonCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractButtonCall40 call = reinterpret_cast<CuteQAbstractButtonCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractButtonCall41 call = reinterpret_cast<CuteQAbstractButtonCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractButtonCall42 call = reinterpret_cast<CuteQAbstractButtonCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractButtonCall43 call = reinterpret_cast<CuteQAbstractButtonCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractButtonCall44 call = reinterpret_cast<CuteQAbstractButtonCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQAbstractButtonCall45 call = reinterpret_cast<CuteQAbstractButtonCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQAbstractButtonCall46 call = reinterpret_cast<CuteQAbstractButtonCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQAbstractButtonCall47 call = reinterpret_cast<CuteQAbstractButtonCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQAbstractButtonCall48 call = reinterpret_cast<CuteQAbstractButtonCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAbstractButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractButton10metaObjectEv(
    const QAbstractButton *self) {
  return self->metaObject();
}

//  QString QAbstractButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractButton::tr(s, c, n));
}

//  QAbstractButton::~QAbstractButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButtonD1Ev(QAbstractButton *self) {
  delete self;
}

//  void QAbstractButton::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setTextERK7QString(
    QAbstractButton *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QAbstractButton::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractButton4textEv(const QAbstractButton *self) {
  return new QString(self->text());
}

//  void QAbstractButton::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setIconERK5QIcon(
    QAbstractButton *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QIcon QAbstractButton::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QAbstractButton4iconEv(const QAbstractButton *self) {
  return new QIcon(self->icon());
}

//  QSize QAbstractButton::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QAbstractButton8iconSizeEv(const QAbstractButton *self) {
  return new QSize(self->iconSize());
}

//  void QAbstractButton::setShortcut(const QKeySequence &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton11setShortcutERK12QKeySequence(
    QAbstractButton *self,
    const QKeySequence *key) {
  self->setShortcut(*key);
}

//  QKeySequence QAbstractButton::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK15QAbstractButton8shortcutEv(
    const QAbstractButton *self) {
  return new QKeySequence(self->shortcut());
}

//  void QAbstractButton::setCheckable(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton12setCheckableEb(
    QAbstractButton *self,
    bool a0) {
  self->setCheckable(a0);
}

//  bool QAbstractButton::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton11isCheckableEv(
    const QAbstractButton *self) {
  return self->isCheckable();
}

//  bool QAbstractButton::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton9isCheckedEv(const QAbstractButton *self) {
  return self->isChecked();
}

//  void QAbstractButton::setDown(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setDownEb(QAbstractButton *self, bool a0) {
  self->setDown(a0);
}

//  bool QAbstractButton::isDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton6isDownEv(const QAbstractButton *self) {
  return self->isDown();
}

//  void QAbstractButton::setAutoRepeat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton13setAutoRepeatEb(
    QAbstractButton *self,
    bool a0) {
  self->setAutoRepeat(a0);
}

//  bool QAbstractButton::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton10autoRepeatEv(const QAbstractButton *self) {
  return self->autoRepeat();
}

//  void QAbstractButton::setAutoRepeatDelay(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton18setAutoRepeatDelayEi(
    QAbstractButton *self,
    int a0) {
  self->setAutoRepeatDelay(a0);
}

//  int QAbstractButton::autoRepeatDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractButton15autoRepeatDelayEv(
    const QAbstractButton *self) {
  return self->autoRepeatDelay();
}

//  void QAbstractButton::setAutoRepeatInterval(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton21setAutoRepeatIntervalEi(
    QAbstractButton *self,
    int a0) {
  self->setAutoRepeatInterval(a0);
}

//  int QAbstractButton::autoRepeatInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractButton18autoRepeatIntervalEv(
    const QAbstractButton *self) {
  return self->autoRepeatInterval();
}

//  void QAbstractButton::setAutoExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton16setAutoExclusiveEb(
    QAbstractButton *self,
    bool a0) {
  self->setAutoExclusive(a0);
}

//  bool QAbstractButton::autoExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton13autoExclusiveEv(
    const QAbstractButton *self) {
  return self->autoExclusive();
}

//  QButtonGroup *QAbstractButton::group() const
extern "C" Q_DECL_EXPORT
QButtonGroup *ritual_ZNK15QAbstractButton5groupEv(
    const QAbstractButton *self) {
  return self->group();
}

//  void QAbstractButton::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton11setIconSizeERK5QSize(
    QAbstractButton *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  void QAbstractButton::animateClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton12animateClickEv(QAbstractButton *self) {
  self->animateClick();
}

//  void QAbstractButton::click()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton5clickEv(QAbstractButton *self) {
  self->click();
}

//  void QAbstractButton::toggle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton6toggleEv(QAbstractButton *self) {
  self->toggle();
}

//  void QAbstractButton::setChecked(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton10setCheckedEb(
    QAbstractButton *self,
    bool a0) {
  self->setChecked(a0);
}

//  bool QAbstractButton::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton9hitButtonERK6QPoint(
    const QAbstractButton *self,
    const QPoint *pos) {
  return self->hitButton(*pos);
}

//  void QAbstractButton::checkStateSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton13checkStateSetEv(QAbstractButton *self) {
  self->checkStateSet();
}

//  void QAbstractButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton14nextCheckStateEv(QAbstractButton *self) {
  self->nextCheckState();
}

//  bool QAbstractButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractButton5eventEP6QEvent(
    QAbstractButton *self,
    QEvent *e) {
  return self->event(e);
}

//  void QAbstractButton::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton13keyPressEventEP9QKeyEvent(
    QAbstractButton *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton15keyReleaseEventEP9QKeyEvent(
    QAbstractButton *self,
    QKeyEvent *e) {
  self->keyReleaseEvent(e);
}

//  void QAbstractButton::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton15mousePressEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton17mouseReleaseEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

//  void QAbstractButton::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton14mouseMoveEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QAbstractButton::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton12focusInEventEP11QFocusEvent(
    QAbstractButton *self,
    QFocusEvent *e) {
  self->focusInEvent(e);
}

//  void QAbstractButton::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton13focusOutEventEP11QFocusEvent(
    QAbstractButton *self,
    QFocusEvent *e) {
  self->focusOutEvent(e);
}

//  void QAbstractButton::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton11changeEventEP6QEvent(
    QAbstractButton *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  void QAbstractButton::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton10timerEventEP11QTimerEvent(
    QAbstractButton *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  a Python function taken by a CuteQAbstractButton, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractButton(
    QAbstractButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractButton *>(self)->take(key, call);
}

//  bool QAbstractButton::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QAbstractButton9hitButtonERK6QPoint(
    const QAbstractButton *self,
    const QPoint *pos) {
  return static_cast<const OwnQAbstractButton *>(self)->OwnQAbstractButton::hitButton(
      *pos);
}

//  void QAbstractButton::checkStateSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton13checkStateSetEv(QAbstractButton *self) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::checkStateSet();
}

//  void QAbstractButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton14nextCheckStateEv(
    QAbstractButton *self) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::nextCheckState();
}

//  bool QAbstractButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractButton5eventEP6QEvent(
    QAbstractButton *self,
    QEvent *e) {
  return static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::event(
      e);
}

//  void QAbstractButton::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton13keyPressEventEP9QKeyEvent(
    QAbstractButton *self,
    QKeyEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::keyPressEvent(
      e);
}

//  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton15keyReleaseEventEP9QKeyEvent(
    QAbstractButton *self,
    QKeyEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::keyReleaseEvent(
      e);
}

//  void QAbstractButton::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton15mousePressEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::mousePressEvent(
      e);
}

//  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton17mouseReleaseEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::mouseReleaseEvent(
      e);
}

//  void QAbstractButton::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton14mouseMoveEventEP11QMouseEvent(
    QAbstractButton *self,
    QMouseEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::mouseMoveEvent(
      e);
}

//  void QAbstractButton::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton12focusInEventEP11QFocusEvent(
    QAbstractButton *self,
    QFocusEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::focusInEvent(
      e);
}

//  void QAbstractButton::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton13focusOutEventEP11QFocusEvent(
    QAbstractButton *self,
    QFocusEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::focusOutEvent(
      e);
}

//  void QAbstractButton::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton11changeEventEP6QEvent(
    QAbstractButton *self,
    QEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::changeEvent(
      e);
}

//  void QAbstractButton::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractButton10timerEventEP11QTimerEvent(
    QAbstractButton *self,
    QTimerEvent *e) {
  static_cast<OwnQAbstractButton *>(self)->OwnQAbstractButton::timerEvent(e);
}

//  QList<QAbstractButton *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_list_make_QAbstractButton_ptr() {
  return new QList<QAbstractButton *>();
}

//  void QList<QAbstractButton *>::append(const QAbstractButton * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractButton_ptr(
    QList<QAbstractButton *> *self,
    QAbstractButton *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractButton *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractButton_ptr(
    const QList<QAbstractButton *> *self) {
  return self->size();
}

//  const QAbstractButton * &QList<QAbstractButton *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_list_at_QAbstractButton_ptr(
    const QList<QAbstractButton *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractButton *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractButton_ptr(QList<QAbstractButton *> *self) {
  delete self;
}
