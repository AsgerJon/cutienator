//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcheckbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcheckbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QCheckBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCheckBox : QCheckBox {
  using QCheckBox::event;
  using QCheckBox::hitButton;
  using QCheckBox::checkStateSet;
  using QCheckBox::nextCheckState;
  using QCheckBox::paintEvent;
  using QCheckBox::mouseMoveEvent;
  using QCheckBox::initStyleOption;
};

//  A QCheckBox that Python can take functions over in. Every QCheckBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQCheckBoxCall0)(const void *, int *);
typedef const QSize * (*CuteQCheckBoxCall1)(const void *, int *);
typedef bool (*CuteQCheckBoxCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQCheckBoxCall3)(const void *, const QPoint *, int *);
typedef void (*CuteQCheckBoxCall4)(const void *, int *);
typedef void (*CuteQCheckBoxCall5)(const void *, int *);
typedef void (*CuteQCheckBoxCall6)(const void *, QPaintEvent *, int *);
typedef void (*CuteQCheckBoxCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCheckBoxCall8)(const void *, QStyleOptionButton *, int *);
typedef void (*CuteQCheckBoxCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCheckBoxCall10)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCheckBoxCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCheckBoxCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCheckBoxCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCheckBoxCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCheckBoxCall15)(const void *, QEvent *, int *);
typedef void (*CuteQCheckBoxCall16)(const void *, QTimerEvent *, int *);
typedef int (*CuteQCheckBoxCall17)(const void *, int *);
typedef void (*CuteQCheckBoxCall18)(const void *, bool, int *);
typedef int (*CuteQCheckBoxCall19)(const void *, int, int *);
typedef bool (*CuteQCheckBoxCall20)(const void *, int *);
typedef void * (*CuteQCheckBoxCall21)(const void *, int *);
typedef void (*CuteQCheckBoxCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCheckBoxCall23)(const void *, QWheelEvent *, int *);
typedef void (*CuteQCheckBoxCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQCheckBoxCall25)(const void *, QEvent *, int *);
typedef void (*CuteQCheckBoxCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQCheckBoxCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQCheckBoxCall28)(const void *, QCloseEvent *, int *);
typedef void (*CuteQCheckBoxCall29)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQCheckBoxCall30)(const void *, QTabletEvent *, int *);
typedef void (*CuteQCheckBoxCall31)(const void *, QActionEvent *, int *);
typedef void (*CuteQCheckBoxCall32)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQCheckBoxCall33)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQCheckBoxCall34)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQCheckBoxCall35)(const void *, QDropEvent *, int *);
typedef void (*CuteQCheckBoxCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQCheckBoxCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQCheckBoxCall38)(const void *, int, int *);
typedef void (*CuteQCheckBoxCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQCheckBoxCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQCheckBoxCall41)(const void *, int *);
typedef void (*CuteQCheckBoxCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQCheckBoxCall43)(const void *, int, int *);
typedef bool (*CuteQCheckBoxCall44)(const void *, bool, int *);
typedef bool (*CuteQCheckBoxCall45)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQCheckBoxCall46)(const void *, QChildEvent *, int *);
typedef void (*CuteQCheckBoxCall47)(const void *, QEvent *, int *);
typedef void (*CuteQCheckBoxCall48)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQCheckBoxCall49)(const void *, const QMetaMethod *, int *);
class CuteQCheckBox : public QCheckBox {
public:
  using QCheckBox::QCheckBox;
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
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QCheckBox15initStyleOptionEP18QStyleOptionButton")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
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

  //  QSize QCheckBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCheckBoxCall0 call = reinterpret_cast<CuteQCheckBoxCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCheckBox::sizeHint();
  }

  //  QSize QCheckBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCheckBoxCall1 call = reinterpret_cast<CuteQCheckBoxCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCheckBox::minimumSizeHint();
  }

  //  bool QCheckBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCheckBoxCall2 call = reinterpret_cast<CuteQCheckBoxCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QCheckBox::event(e);
  }

  //  bool QCheckBox::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCheckBoxCall3 call = reinterpret_cast<CuteQCheckBoxCall3>(taken[3]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QCheckBox::hitButton(pos);
  }

  //  void QCheckBox::checkStateSet()
  void checkStateSet() override {
    if (taken[4]) {
      int handled = 0;
      CuteQCheckBoxCall4 call = reinterpret_cast<CuteQCheckBoxCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QCheckBox::checkStateSet();
  }

  //  void QCheckBox::nextCheckState()
  void nextCheckState() override {
    if (taken[5]) {
      int handled = 0;
      CuteQCheckBoxCall5 call = reinterpret_cast<CuteQCheckBoxCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QCheckBox::nextCheckState();
  }

  //  void QCheckBox::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCheckBoxCall6 call = reinterpret_cast<CuteQCheckBoxCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QCheckBox::paintEvent(a0);
  }

  //  void QCheckBox::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCheckBoxCall7 call = reinterpret_cast<CuteQCheckBoxCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QCheckBox::mouseMoveEvent(a0);
  }

  //  void QCheckBox::initStyleOption(QStyleOptionButton *option) const
  void initStyleOption(QStyleOptionButton *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCheckBoxCall8 call = reinterpret_cast<CuteQCheckBoxCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QCheckBox::initStyleOption(option);
  }

  //  void QAbstractButton::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCheckBoxCall9 call = reinterpret_cast<CuteQCheckBoxCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyPressEvent(e);
  }

  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCheckBoxCall10 call = reinterpret_cast<CuteQCheckBoxCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }

  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCheckBoxCall11 call = reinterpret_cast<CuteQCheckBoxCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }

  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCheckBoxCall12 call = reinterpret_cast<CuteQCheckBoxCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }

  //  void QAbstractButton::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCheckBoxCall13 call = reinterpret_cast<CuteQCheckBoxCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusInEvent(e);
  }

  //  void QAbstractButton::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCheckBoxCall14 call = reinterpret_cast<CuteQCheckBoxCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusOutEvent(e);
  }

  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCheckBoxCall15 call = reinterpret_cast<CuteQCheckBoxCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }

  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCheckBoxCall16 call = reinterpret_cast<CuteQCheckBoxCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQCheckBoxCall17 call = reinterpret_cast<CuteQCheckBoxCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[18]) {
      int handled = 0;
      CuteQCheckBoxCall18 call = reinterpret_cast<CuteQCheckBoxCall18>(taken[18]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQCheckBoxCall19 call = reinterpret_cast<CuteQCheckBoxCall19>(taken[19]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQCheckBoxCall20 call = reinterpret_cast<CuteQCheckBoxCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQCheckBoxCall21 call = reinterpret_cast<CuteQCheckBoxCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCheckBoxCall22 call = reinterpret_cast<CuteQCheckBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQCheckBoxCall23 call = reinterpret_cast<CuteQCheckBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCheckBoxCall24 call = reinterpret_cast<CuteQCheckBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCheckBoxCall25 call = reinterpret_cast<CuteQCheckBoxCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCheckBoxCall26 call = reinterpret_cast<CuteQCheckBoxCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCheckBoxCall27 call = reinterpret_cast<CuteQCheckBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCheckBoxCall28 call = reinterpret_cast<CuteQCheckBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCheckBoxCall29 call = reinterpret_cast<CuteQCheckBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQCheckBoxCall30 call = reinterpret_cast<CuteQCheckBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCheckBoxCall31 call = reinterpret_cast<CuteQCheckBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCheckBoxCall32 call = reinterpret_cast<CuteQCheckBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQCheckBoxCall33 call = reinterpret_cast<CuteQCheckBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQCheckBoxCall34 call = reinterpret_cast<CuteQCheckBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQCheckBoxCall35 call = reinterpret_cast<CuteQCheckBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQCheckBoxCall36 call = reinterpret_cast<CuteQCheckBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQCheckBoxCall37 call = reinterpret_cast<CuteQCheckBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQCheckBoxCall38 call = reinterpret_cast<CuteQCheckBoxCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQCheckBoxCall39 call = reinterpret_cast<CuteQCheckBoxCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQCheckBoxCall40 call = reinterpret_cast<CuteQCheckBoxCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQCheckBoxCall41 call = reinterpret_cast<CuteQCheckBoxCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQCheckBoxCall42 call = reinterpret_cast<CuteQCheckBoxCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQCheckBoxCall43 call = reinterpret_cast<CuteQCheckBoxCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQCheckBoxCall44 call = reinterpret_cast<CuteQCheckBoxCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQCheckBoxCall45 call = reinterpret_cast<CuteQCheckBoxCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQCheckBoxCall46 call = reinterpret_cast<CuteQCheckBoxCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQCheckBoxCall47 call = reinterpret_cast<CuteQCheckBoxCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQCheckBoxCall48 call = reinterpret_cast<CuteQCheckBoxCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQCheckBoxCall49 call = reinterpret_cast<CuteQCheckBoxCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QCheckBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QCheckBox10metaObjectEv(
    const QCheckBox *self) {
  return self->metaObject();
}

//  QString QCheckBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QCheckBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCheckBox::tr(s, c, n));
}

//  QCheckBox::QCheckBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZN9QCheckBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQCheckBox(parent);
}

//  QCheckBox::QCheckBox(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZN9QCheckBoxC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQCheckBox(*text, parent);
}

//  QCheckBox::~QCheckBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBoxD1Ev(QCheckBox *self) {
  delete self;
}

//  QSize QCheckBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QCheckBox8sizeHintEv(const QCheckBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QCheckBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QCheckBox15minimumSizeHintEv(const QCheckBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QCheckBox::setTristate(bool y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBox11setTristateEb(QCheckBox *self, bool y) {
  self->setTristate(y);
}

//  bool QCheckBox::isTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCheckBox10isTristateEv(const QCheckBox *self) {
  return self->isTristate();
}

//  Qt::CheckState QCheckBox::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK9QCheckBox10checkStateEv(const QCheckBox *self) {
  return self->checkState();
}

//  void QCheckBox::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBox13setCheckStateEN2Qt10CheckStateE(
    QCheckBox *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  a Python function taken by a CuteQCheckBox, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCheckBox(QCheckBox *self, const char *key, void *call) {
  return static_cast<CuteQCheckBox *>(self)->take(key, call);
}

//  QSize QCheckBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QCheckBox8sizeHintEv(const QCheckBox *self) {
  return new QSize(self->QCheckBox::sizeHint());
}

//  QSize QCheckBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QCheckBox15minimumSizeHintEv(const QCheckBox *self) {
  return new QSize(self->QCheckBox::minimumSizeHint());
}

//  bool QCheckBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QCheckBox5eventEP6QEvent(QCheckBox *self, QEvent *e) {
  return static_cast<OwnQCheckBox *>(self)->OwnQCheckBox::event(e);
}

//  bool QCheckBox::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QCheckBox9hitButtonERK6QPoint(
    const QCheckBox *self,
    const QPoint *pos) {
  return static_cast<const OwnQCheckBox *>(self)->OwnQCheckBox::hitButton(
      *pos);
}

//  void QCheckBox::checkStateSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QCheckBox13checkStateSetEv(QCheckBox *self) {
  static_cast<OwnQCheckBox *>(self)->OwnQCheckBox::checkStateSet();
}

//  void QCheckBox::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QCheckBox14nextCheckStateEv(QCheckBox *self) {
  static_cast<OwnQCheckBox *>(self)->OwnQCheckBox::nextCheckState();
}

//  void QCheckBox::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QCheckBox10paintEventEP11QPaintEvent(
    QCheckBox *self,
    QPaintEvent *a0) {
  static_cast<OwnQCheckBox *>(self)->OwnQCheckBox::paintEvent(a0);
}

//  void QCheckBox::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QCheckBox14mouseMoveEventEP11QMouseEvent(
    QCheckBox *self,
    QMouseEvent *a0) {
  static_cast<OwnQCheckBox *>(self)->OwnQCheckBox::mouseMoveEvent(a0);
}

//  void QCheckBox::initStyleOption(QStyleOptionButton *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QCheckBox15initStyleOptionEP18QStyleOptionButton(
    const QCheckBox *self,
    QStyleOptionButton *option) {
  static_cast<const OwnQCheckBox *>(self)->OwnQCheckBox::initStyleOption(
      option);
}
