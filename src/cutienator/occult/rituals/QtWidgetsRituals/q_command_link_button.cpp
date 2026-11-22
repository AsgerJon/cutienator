//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcommandlinkbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcommandlinkbutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QCommandLinkButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCommandLinkButton : QCommandLinkButton {
  using QCommandLinkButton::event;
  using QCommandLinkButton::paintEvent;
};

//  A QCommandLinkButton that Python can take functions over in. Every QCommandLinkButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQCommandLinkButtonCall0)(const void *, int *);
typedef int (*CuteQCommandLinkButtonCall1)(const void *, int, int *);
typedef const QSize * (*CuteQCommandLinkButtonCall2)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall3)(const void *, QStyleOptionButton *, int *);
typedef bool (*CuteQCommandLinkButtonCall4)(const void *, QEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall5)(const void *, QPaintEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall9)(const void *, QMouseEvent *, int *);
typedef bool (*CuteQCommandLinkButtonCall10)(const void *, const QPoint *, int *);
typedef void (*CuteQCommandLinkButtonCall11)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall12)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall16)(const void *, QEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall17)(const void *, QTimerEvent *, int *);
typedef int (*CuteQCommandLinkButtonCall18)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall19)(const void *, bool, int *);
typedef bool (*CuteQCommandLinkButtonCall20)(const void *, int *);
typedef void * (*CuteQCommandLinkButtonCall21)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall23)(const void *, QWheelEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall25)(const void *, QEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall28)(const void *, QCloseEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall29)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall30)(const void *, QTabletEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall31)(const void *, QActionEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall32)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall33)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall34)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall35)(const void *, QDropEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQCommandLinkButtonCall38)(const void *, int, int *);
typedef void (*CuteQCommandLinkButtonCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQCommandLinkButtonCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQCommandLinkButtonCall41)(const void *, int *);
typedef void (*CuteQCommandLinkButtonCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQCommandLinkButtonCall43)(const void *, int, int *);
typedef bool (*CuteQCommandLinkButtonCall44)(const void *, bool, int *);
typedef bool (*CuteQCommandLinkButtonCall45)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall46)(const void *, QChildEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall47)(const void *, QEvent *, int *);
typedef void (*CuteQCommandLinkButtonCall48)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQCommandLinkButtonCall49)(const void *, const QMetaMethod *, int *);
class CuteQCommandLinkButton : public QCommandLinkButton {
public:
  using QCommandLinkButton::QCommandLinkButton;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QPushButton15initStyleOptionEP18QStyleOptionButton")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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

  //  QSize QCommandLinkButton::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCommandLinkButtonCall0 call = reinterpret_cast<CuteQCommandLinkButtonCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCommandLinkButton::sizeHint();
  }

  //  int QCommandLinkButton::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCommandLinkButtonCall1 call = reinterpret_cast<CuteQCommandLinkButtonCall1>(taken[1]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCommandLinkButton::heightForWidth(a0);
  }

  //  QSize QCommandLinkButton::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCommandLinkButtonCall2 call = reinterpret_cast<CuteQCommandLinkButtonCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCommandLinkButton::minimumSizeHint();
  }

  //  void QCommandLinkButton::initStyleOption(QStyleOptionButton *option)
  //      const
  void initStyleOption(QStyleOptionButton *option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCommandLinkButtonCall3 call = reinterpret_cast<CuteQCommandLinkButtonCall3>(taken[3]);
      call(this, option, &handled);
      if (handled) return;
    }
    QCommandLinkButton::initStyleOption(option);
  }

  //  bool QCommandLinkButton::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCommandLinkButtonCall4 call = reinterpret_cast<CuteQCommandLinkButtonCall4>(taken[4]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QCommandLinkButton::event(e);
  }

  //  void QCommandLinkButton::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCommandLinkButtonCall5 call = reinterpret_cast<CuteQCommandLinkButtonCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QCommandLinkButton::paintEvent(a0);
  }

  //  void QPushButton::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCommandLinkButtonCall6 call = reinterpret_cast<CuteQCommandLinkButtonCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::keyPressEvent(a0);
  }

  //  void QPushButton::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCommandLinkButtonCall7 call = reinterpret_cast<CuteQCommandLinkButtonCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusInEvent(a0);
  }

  //  void QPushButton::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCommandLinkButtonCall8 call = reinterpret_cast<CuteQCommandLinkButtonCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusOutEvent(a0);
  }

  //  void QPushButton::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCommandLinkButtonCall9 call = reinterpret_cast<CuteQCommandLinkButtonCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::mouseMoveEvent(a0);
  }

  //  bool QPushButton::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCommandLinkButtonCall10 call = reinterpret_cast<CuteQCommandLinkButtonCall10>(taken[10]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QPushButton::hitButton(pos);
  }

  //  void QAbstractButton::checkStateSet()
  void checkStateSet() override {
    if (taken[11]) {
      int handled = 0;
      CuteQCommandLinkButtonCall11 call = reinterpret_cast<CuteQCommandLinkButtonCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::checkStateSet();
  }

  //  void QAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[12]) {
      int handled = 0;
      CuteQCommandLinkButtonCall12 call = reinterpret_cast<CuteQCommandLinkButtonCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::nextCheckState();
  }

  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCommandLinkButtonCall13 call = reinterpret_cast<CuteQCommandLinkButtonCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }

  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCommandLinkButtonCall14 call = reinterpret_cast<CuteQCommandLinkButtonCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }

  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCommandLinkButtonCall15 call = reinterpret_cast<CuteQCommandLinkButtonCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }

  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCommandLinkButtonCall16 call = reinterpret_cast<CuteQCommandLinkButtonCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }

  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCommandLinkButtonCall17 call = reinterpret_cast<CuteQCommandLinkButtonCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQCommandLinkButtonCall18 call = reinterpret_cast<CuteQCommandLinkButtonCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[19]) {
      int handled = 0;
      CuteQCommandLinkButtonCall19 call = reinterpret_cast<CuteQCommandLinkButtonCall19>(taken[19]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQCommandLinkButtonCall20 call = reinterpret_cast<CuteQCommandLinkButtonCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQCommandLinkButtonCall21 call = reinterpret_cast<CuteQCommandLinkButtonCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCommandLinkButtonCall22 call = reinterpret_cast<CuteQCommandLinkButtonCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQCommandLinkButtonCall23 call = reinterpret_cast<CuteQCommandLinkButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCommandLinkButtonCall24 call = reinterpret_cast<CuteQCommandLinkButtonCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCommandLinkButtonCall25 call = reinterpret_cast<CuteQCommandLinkButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCommandLinkButtonCall26 call = reinterpret_cast<CuteQCommandLinkButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCommandLinkButtonCall27 call = reinterpret_cast<CuteQCommandLinkButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCommandLinkButtonCall28 call = reinterpret_cast<CuteQCommandLinkButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCommandLinkButtonCall29 call = reinterpret_cast<CuteQCommandLinkButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQCommandLinkButtonCall30 call = reinterpret_cast<CuteQCommandLinkButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCommandLinkButtonCall31 call = reinterpret_cast<CuteQCommandLinkButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCommandLinkButtonCall32 call = reinterpret_cast<CuteQCommandLinkButtonCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQCommandLinkButtonCall33 call = reinterpret_cast<CuteQCommandLinkButtonCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQCommandLinkButtonCall34 call = reinterpret_cast<CuteQCommandLinkButtonCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQCommandLinkButtonCall35 call = reinterpret_cast<CuteQCommandLinkButtonCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQCommandLinkButtonCall36 call = reinterpret_cast<CuteQCommandLinkButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQCommandLinkButtonCall37 call = reinterpret_cast<CuteQCommandLinkButtonCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQCommandLinkButtonCall38 call = reinterpret_cast<CuteQCommandLinkButtonCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQCommandLinkButtonCall39 call = reinterpret_cast<CuteQCommandLinkButtonCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQCommandLinkButtonCall40 call = reinterpret_cast<CuteQCommandLinkButtonCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQCommandLinkButtonCall41 call = reinterpret_cast<CuteQCommandLinkButtonCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQCommandLinkButtonCall42 call = reinterpret_cast<CuteQCommandLinkButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQCommandLinkButtonCall43 call = reinterpret_cast<CuteQCommandLinkButtonCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQCommandLinkButtonCall44 call = reinterpret_cast<CuteQCommandLinkButtonCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQCommandLinkButtonCall45 call = reinterpret_cast<CuteQCommandLinkButtonCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQCommandLinkButtonCall46 call = reinterpret_cast<CuteQCommandLinkButtonCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQCommandLinkButtonCall47 call = reinterpret_cast<CuteQCommandLinkButtonCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQCommandLinkButtonCall48 call = reinterpret_cast<CuteQCommandLinkButtonCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQCommandLinkButtonCall49 call = reinterpret_cast<CuteQCommandLinkButtonCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QCommandLinkButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QCommandLinkButton10metaObjectEv(
    const QCommandLinkButton *self) {
  return self->metaObject();
}

//  QString QCommandLinkButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCommandLinkButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCommandLinkButton::tr(s, c, n));
}

//  QCommandLinkButton::QCommandLinkButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1EP7QWidget(
    QWidget *parent) {
  return new CuteQCommandLinkButton(parent);
}

//  QCommandLinkButton::QCommandLinkButton(const QString &text, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQCommandLinkButton(*text, parent);
}

//  QCommandLinkButton::QCommandLinkButton(const QString &text, const QString
//      &description, QWidget *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1ERK7QStringS2_P7QWidget(
    const QString *text,
    const QString *description,
    QWidget *parent) {
  return new CuteQCommandLinkButton(*text, *description, parent);
}

//  QCommandLinkButton::~QCommandLinkButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLinkButtonD1Ev(QCommandLinkButton *self) {
  delete self;
}

//  QString QCommandLinkButton::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLinkButton11descriptionEv(
    const QCommandLinkButton *self) {
  return new QString(self->description());
}

//  void QCommandLinkButton::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLinkButton14setDescriptionERK7QString(
    QCommandLinkButton *self,
    const QString *description) {
  self->setDescription(*description);
}

//  QSize QCommandLinkButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QCommandLinkButton8sizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->sizeHint());
}

//  int QCommandLinkButton::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCommandLinkButton14heightForWidthEi(
    const QCommandLinkButton *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  QSize QCommandLinkButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QCommandLinkButton15minimumSizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QCommandLinkButton::initStyleOption(QStyleOptionButton *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QCommandLinkButton15initStyleOptionEP18QStyleOptionButton(
    const QCommandLinkButton *self,
    QStyleOptionButton *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQCommandLinkButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCommandLinkButton(
    QCommandLinkButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCommandLinkButton *>(self)->take(key, call);
}

//  QSize QCommandLinkButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QCommandLinkButton8sizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->QCommandLinkButton::sizeHint());
}

//  int QCommandLinkButton::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QCommandLinkButton14heightForWidthEi(
    const QCommandLinkButton *self,
    int a0) {
  return self->QCommandLinkButton::heightForWidth(a0);
}

//  QSize QCommandLinkButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QCommandLinkButton15minimumSizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->QCommandLinkButton::minimumSizeHint());
}

//  void QCommandLinkButton::initStyleOption(QStyleOptionButton *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18QCommandLinkButton15initStyleOptionEP18QStyleOptionButton(
    const QCommandLinkButton *self,
    QStyleOptionButton *option) {
  self->QCommandLinkButton::initStyleOption(option);
}

//  bool QCommandLinkButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QCommandLinkButton5eventEP6QEvent(
    QCommandLinkButton *self,
    QEvent *e) {
  return static_cast<OwnQCommandLinkButton *>(self)->OwnQCommandLinkButton::event(
      e);
}

//  void QCommandLinkButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QCommandLinkButton10paintEventEP11QPaintEvent(
    QCommandLinkButton *self,
    QPaintEvent *a0) {
  static_cast<OwnQCommandLinkButton *>(self)->OwnQCommandLinkButton::paintEvent(
      a0);
}
