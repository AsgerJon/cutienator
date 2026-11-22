//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qpushbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qpushbutton.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPushButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPushButton : QPushButton {
  using QPushButton::event;
  using QPushButton::paintEvent;
  using QPushButton::keyPressEvent;
  using QPushButton::focusInEvent;
  using QPushButton::focusOutEvent;
  using QPushButton::mouseMoveEvent;
  using QPushButton::initStyleOption;
  using QPushButton::hitButton;
};

//  A QPushButton that Python can take functions over in. Every QPushButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQPushButtonCall0)(const void *, int *);
typedef const QSize * (*CuteQPushButtonCall1)(const void *, int *);
typedef bool (*CuteQPushButtonCall2)(const void *, QEvent *, int *);
typedef void (*CuteQPushButtonCall3)(const void *, QPaintEvent *, int *);
typedef void (*CuteQPushButtonCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPushButtonCall5)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPushButtonCall6)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPushButtonCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPushButtonCall8)(const void *, QStyleOptionButton *, int *);
typedef bool (*CuteQPushButtonCall9)(const void *, const QPoint *, int *);
typedef void (*CuteQPushButtonCall10)(const void *, int *);
typedef void (*CuteQPushButtonCall11)(const void *, int *);
typedef void (*CuteQPushButtonCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPushButtonCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPushButtonCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPushButtonCall15)(const void *, QEvent *, int *);
typedef void (*CuteQPushButtonCall16)(const void *, QTimerEvent *, int *);
typedef int (*CuteQPushButtonCall17)(const void *, int *);
typedef void (*CuteQPushButtonCall18)(const void *, bool, int *);
typedef int (*CuteQPushButtonCall19)(const void *, int, int *);
typedef bool (*CuteQPushButtonCall20)(const void *, int *);
typedef void * (*CuteQPushButtonCall21)(const void *, int *);
typedef void (*CuteQPushButtonCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPushButtonCall23)(const void *, QWheelEvent *, int *);
typedef void (*CuteQPushButtonCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPushButtonCall25)(const void *, QEvent *, int *);
typedef void (*CuteQPushButtonCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQPushButtonCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQPushButtonCall28)(const void *, QCloseEvent *, int *);
typedef void (*CuteQPushButtonCall29)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQPushButtonCall30)(const void *, QTabletEvent *, int *);
typedef void (*CuteQPushButtonCall31)(const void *, QActionEvent *, int *);
typedef void (*CuteQPushButtonCall32)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQPushButtonCall33)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQPushButtonCall34)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQPushButtonCall35)(const void *, QDropEvent *, int *);
typedef void (*CuteQPushButtonCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQPushButtonCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQPushButtonCall38)(const void *, int, int *);
typedef void (*CuteQPushButtonCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQPushButtonCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQPushButtonCall41)(const void *, int *);
typedef void (*CuteQPushButtonCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQPushButtonCall43)(const void *, int, int *);
typedef bool (*CuteQPushButtonCall44)(const void *, bool, int *);
typedef bool (*CuteQPushButtonCall45)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQPushButtonCall46)(const void *, QChildEvent *, int *);
typedef void (*CuteQPushButtonCall47)(const void *, QEvent *, int *);
typedef void (*CuteQPushButtonCall48)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQPushButtonCall49)(const void *, const QMetaMethod *, int *);
class CuteQPushButton : public QPushButton {
public:
  using QPushButton::QPushButton;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QPushButton15initStyleOptionEP18QStyleOptionButton")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    return false;
  }

  //  QSize QPushButton::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPushButtonCall0 call = reinterpret_cast<CuteQPushButtonCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPushButton::sizeHint();
  }

  //  QSize QPushButton::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPushButtonCall1 call = reinterpret_cast<CuteQPushButtonCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPushButton::minimumSizeHint();
  }

  //  bool QPushButton::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPushButtonCall2 call = reinterpret_cast<CuteQPushButtonCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QPushButton::event(e);
  }

  //  void QPushButton::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPushButtonCall3 call = reinterpret_cast<CuteQPushButtonCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::paintEvent(a0);
  }

  //  void QPushButton::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPushButtonCall4 call = reinterpret_cast<CuteQPushButtonCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::keyPressEvent(a0);
  }

  //  void QPushButton::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPushButtonCall5 call = reinterpret_cast<CuteQPushButtonCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusInEvent(a0);
  }

  //  void QPushButton::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPushButtonCall6 call = reinterpret_cast<CuteQPushButtonCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusOutEvent(a0);
  }

  //  void QPushButton::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPushButtonCall7 call = reinterpret_cast<CuteQPushButtonCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::mouseMoveEvent(a0);
  }

  //  void QPushButton::initStyleOption(QStyleOptionButton *option) const
  void initStyleOption(QStyleOptionButton *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPushButtonCall8 call = reinterpret_cast<CuteQPushButtonCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QPushButton::initStyleOption(option);
  }

  //  bool QPushButton::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPushButtonCall9 call = reinterpret_cast<CuteQPushButtonCall9>(taken[9]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QPushButton::hitButton(pos);
  }

  //  void QAbstractButton::checkStateSet()
  void checkStateSet() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPushButtonCall10 call = reinterpret_cast<CuteQPushButtonCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::checkStateSet();
  }

  //  void QAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPushButtonCall11 call = reinterpret_cast<CuteQPushButtonCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::nextCheckState();
  }

  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPushButtonCall12 call = reinterpret_cast<CuteQPushButtonCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }

  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPushButtonCall13 call = reinterpret_cast<CuteQPushButtonCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }

  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPushButtonCall14 call = reinterpret_cast<CuteQPushButtonCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }

  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPushButtonCall15 call = reinterpret_cast<CuteQPushButtonCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }

  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPushButtonCall16 call = reinterpret_cast<CuteQPushButtonCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPushButtonCall17 call = reinterpret_cast<CuteQPushButtonCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPushButtonCall18 call = reinterpret_cast<CuteQPushButtonCall18>(taken[18]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPushButtonCall19 call = reinterpret_cast<CuteQPushButtonCall19>(taken[19]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPushButtonCall20 call = reinterpret_cast<CuteQPushButtonCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPushButtonCall21 call = reinterpret_cast<CuteQPushButtonCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPushButtonCall22 call = reinterpret_cast<CuteQPushButtonCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPushButtonCall23 call = reinterpret_cast<CuteQPushButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPushButtonCall24 call = reinterpret_cast<CuteQPushButtonCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPushButtonCall25 call = reinterpret_cast<CuteQPushButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPushButtonCall26 call = reinterpret_cast<CuteQPushButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPushButtonCall27 call = reinterpret_cast<CuteQPushButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPushButtonCall28 call = reinterpret_cast<CuteQPushButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPushButtonCall29 call = reinterpret_cast<CuteQPushButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQPushButtonCall30 call = reinterpret_cast<CuteQPushButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPushButtonCall31 call = reinterpret_cast<CuteQPushButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPushButtonCall32 call = reinterpret_cast<CuteQPushButtonCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPushButtonCall33 call = reinterpret_cast<CuteQPushButtonCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPushButtonCall34 call = reinterpret_cast<CuteQPushButtonCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQPushButtonCall35 call = reinterpret_cast<CuteQPushButtonCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQPushButtonCall36 call = reinterpret_cast<CuteQPushButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPushButtonCall37 call = reinterpret_cast<CuteQPushButtonCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQPushButtonCall38 call = reinterpret_cast<CuteQPushButtonCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQPushButtonCall39 call = reinterpret_cast<CuteQPushButtonCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPushButtonCall40 call = reinterpret_cast<CuteQPushButtonCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQPushButtonCall41 call = reinterpret_cast<CuteQPushButtonCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQPushButtonCall42 call = reinterpret_cast<CuteQPushButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQPushButtonCall43 call = reinterpret_cast<CuteQPushButtonCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQPushButtonCall44 call = reinterpret_cast<CuteQPushButtonCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPushButtonCall45 call = reinterpret_cast<CuteQPushButtonCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQPushButtonCall46 call = reinterpret_cast<CuteQPushButtonCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQPushButtonCall47 call = reinterpret_cast<CuteQPushButtonCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQPushButtonCall48 call = reinterpret_cast<CuteQPushButtonCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQPushButtonCall49 call = reinterpret_cast<CuteQPushButtonCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QPushButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPushButton10metaObjectEv(
    const QPushButton *self) {
  return self->metaObject();
}

//  QString QPushButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPushButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPushButton::tr(s, c, n));
}

//  QPushButton::QPushButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1EP7QWidget(QWidget *parent) {
  return new CuteQPushButton(parent);
}

//  QPushButton::QPushButton(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQPushButton(*text, parent);
}

//  QPushButton::QPushButton(const QIcon &icon, const QString &text, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1ERK5QIconRK7QStringP7QWidget(
    const QIcon *icon,
    const QString *text,
    QWidget *parent) {
  return new CuteQPushButton(*icon, *text, parent);
}

//  QPushButton::~QPushButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButtonD1Ev(QPushButton *self) {
  delete self;
}

//  QSize QPushButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QPushButton8sizeHintEv(const QPushButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QPushButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QPushButton15minimumSizeHintEv(const QPushButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  bool QPushButton::autoDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton11autoDefaultEv(const QPushButton *self) {
  return self->autoDefault();
}

//  void QPushButton::setAutoDefault(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton14setAutoDefaultEb(QPushButton *self, bool a0) {
  self->setAutoDefault(a0);
}

//  bool QPushButton::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton9isDefaultEv(const QPushButton *self) {
  return self->isDefault();
}

//  void QPushButton::setDefault(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton10setDefaultEb(QPushButton *self, bool a0) {
  self->setDefault(a0);
}

//  void QPushButton::setMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton7setMenuEP5QMenu(QPushButton *self, QMenu *menu) {
  self->setMenu(menu);
}

//  QMenu *QPushButton::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK11QPushButton4menuEv(const QPushButton *self) {
  return self->menu();
}

//  void QPushButton::setFlat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton7setFlatEb(QPushButton *self, bool a0) {
  self->setFlat(a0);
}

//  bool QPushButton::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton6isFlatEv(const QPushButton *self) {
  return self->isFlat();
}

//  void QPushButton::showMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton8showMenuEv(QPushButton *self) {
  self->showMenu();
}

//  a Python function taken by a CuteQPushButton, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPushButton(
    QPushButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPushButton *>(self)->take(key, call);
}

//  QSize QPushButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QPushButton8sizeHintEv(const QPushButton *self) {
  return new QSize(self->QPushButton::sizeHint());
}

//  QSize QPushButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QPushButton15minimumSizeHintEv(
    const QPushButton *self) {
  return new QSize(self->QPushButton::minimumSizeHint());
}

//  bool QPushButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QPushButton5eventEP6QEvent(
    QPushButton *self,
    QEvent *e) {
  return static_cast<OwnQPushButton *>(self)->OwnQPushButton::event(e);
}

//  void QPushButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPushButton10paintEventEP11QPaintEvent(
    QPushButton *self,
    QPaintEvent *a0) {
  static_cast<OwnQPushButton *>(self)->OwnQPushButton::paintEvent(a0);
}

//  void QPushButton::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPushButton13keyPressEventEP9QKeyEvent(
    QPushButton *self,
    QKeyEvent *a0) {
  static_cast<OwnQPushButton *>(self)->OwnQPushButton::keyPressEvent(a0);
}

//  void QPushButton::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPushButton12focusInEventEP11QFocusEvent(
    QPushButton *self,
    QFocusEvent *a0) {
  static_cast<OwnQPushButton *>(self)->OwnQPushButton::focusInEvent(a0);
}

//  void QPushButton::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPushButton13focusOutEventEP11QFocusEvent(
    QPushButton *self,
    QFocusEvent *a0) {
  static_cast<OwnQPushButton *>(self)->OwnQPushButton::focusOutEvent(a0);
}

//  void QPushButton::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPushButton14mouseMoveEventEP11QMouseEvent(
    QPushButton *self,
    QMouseEvent *a0) {
  static_cast<OwnQPushButton *>(self)->OwnQPushButton::mouseMoveEvent(a0);
}

//  void QPushButton::initStyleOption(QStyleOptionButton *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QPushButton15initStyleOptionEP18QStyleOptionButton(
    const QPushButton *self,
    QStyleOptionButton *option) {
  static_cast<const OwnQPushButton *>(self)->OwnQPushButton::initStyleOption(
      option);
}

//  bool QPushButton::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QPushButton9hitButtonERK6QPoint(
    const QPushButton *self,
    const QPoint *pos) {
  return static_cast<const OwnQPushButton *>(self)->OwnQPushButton::hitButton(
      *pos);
}
