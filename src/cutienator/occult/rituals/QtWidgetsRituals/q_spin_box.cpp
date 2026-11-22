//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qspinbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSpinBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSpinBox : QSpinBox {
  using QSpinBox::event;
};

//  A QSpinBox that Python can take functions over in. Every QSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSpinBoxCall0)(const void *, QEvent *, int *);
typedef const QSize * (*CuteQSpinBoxCall1)(const void *, int *);
typedef const QSize * (*CuteQSpinBoxCall2)(const void *, int *);
typedef const QVariant * (*CuteQSpinBoxCall3)(const void *, int, int *);
typedef void (*CuteQSpinBoxCall4)(const void *, int, int *);
typedef void (*CuteQSpinBoxCall5)(const void *, int *);
typedef void (*CuteQSpinBoxCall6)(const void *, QResizeEvent *, int *);
typedef void (*CuteQSpinBoxCall7)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSpinBoxCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSpinBoxCall9)(const void *, QWheelEvent *, int *);
typedef void (*CuteQSpinBoxCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSpinBoxCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSpinBoxCall12)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQSpinBoxCall13)(const void *, QEvent *, int *);
typedef void (*CuteQSpinBoxCall14)(const void *, QCloseEvent *, int *);
typedef void (*CuteQSpinBoxCall15)(const void *, QHideEvent *, int *);
typedef void (*CuteQSpinBoxCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSpinBoxCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSpinBoxCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSpinBoxCall19)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSpinBoxCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQSpinBoxCall21)(const void *, QShowEvent *, int *);
typedef void (*CuteQSpinBoxCall22)(const void *, QStyleOptionSpinBox *, int *);
typedef int (*CuteQSpinBoxCall23)(const void *, int *);
typedef void (*CuteQSpinBoxCall24)(const void *, bool, int *);
typedef int (*CuteQSpinBoxCall25)(const void *, int, int *);
typedef bool (*CuteQSpinBoxCall26)(const void *, int *);
typedef void * (*CuteQSpinBoxCall27)(const void *, int *);
typedef void (*CuteQSpinBoxCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQSpinBoxCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSpinBoxCall30)(const void *, QEvent *, int *);
typedef void (*CuteQSpinBoxCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSpinBoxCall32)(const void *, QTabletEvent *, int *);
typedef void (*CuteQSpinBoxCall33)(const void *, QActionEvent *, int *);
typedef void (*CuteQSpinBoxCall34)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQSpinBoxCall35)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQSpinBoxCall36)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQSpinBoxCall37)(const void *, QDropEvent *, int *);
typedef int (*CuteQSpinBoxCall38)(const void *, int, int *);
typedef void (*CuteQSpinBoxCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQSpinBoxCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQSpinBoxCall41)(const void *, int *);
typedef void (*CuteQSpinBoxCall42)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQSpinBoxCall43)(const void *, bool, int *);
typedef bool (*CuteQSpinBoxCall44)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSpinBoxCall45)(const void *, QChildEvent *, int *);
typedef void (*CuteQSpinBoxCall46)(const void *, QEvent *, int *);
typedef void (*CuteQSpinBoxCall47)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSpinBoxCall48)(const void *, const QMetaMethod *, int *);
class CuteQSpinBox : public QSpinBox {
public:
  using QSpinBox::QSpinBox;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox6stepByEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox5clearEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
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

  //  bool QSpinBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpinBoxCall0 call = reinterpret_cast<CuteQSpinBoxCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSpinBox::event(event);
  }

  //  QSize QAbstractSpinBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpinBoxCall1 call = reinterpret_cast<CuteQSpinBoxCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::sizeHint();
  }

  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpinBoxCall2 call = reinterpret_cast<CuteQSpinBoxCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::minimumSizeHint();
  }

  //  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpinBoxCall3 call = reinterpret_cast<CuteQSpinBoxCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }

  //  void QAbstractSpinBox::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSpinBoxCall4 call = reinterpret_cast<CuteQSpinBoxCall4>(taken[4]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::stepBy(steps);
  }

  //  void QAbstractSpinBox::clear()
  void clear() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSpinBoxCall5 call = reinterpret_cast<CuteQSpinBoxCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::clear();
  }

  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSpinBoxCall6 call = reinterpret_cast<CuteQSpinBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }

  //  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSpinBoxCall7 call = reinterpret_cast<CuteQSpinBoxCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyPressEvent(event);
  }

  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSpinBoxCall8 call = reinterpret_cast<CuteQSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyReleaseEvent(event);
  }

  //  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSpinBoxCall9 call = reinterpret_cast<CuteQSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::wheelEvent(event);
  }

  //  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSpinBoxCall10 call = reinterpret_cast<CuteQSpinBoxCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusInEvent(event);
  }

  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSpinBoxCall11 call = reinterpret_cast<CuteQSpinBoxCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusOutEvent(event);
  }

  //  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSpinBoxCall12 call = reinterpret_cast<CuteQSpinBoxCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::contextMenuEvent(event);
  }

  //  void QAbstractSpinBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSpinBoxCall13 call = reinterpret_cast<CuteQSpinBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }

  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSpinBoxCall14 call = reinterpret_cast<CuteQSpinBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }

  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSpinBoxCall15 call = reinterpret_cast<CuteQSpinBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }

  //  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSpinBoxCall16 call = reinterpret_cast<CuteQSpinBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mousePressEvent(event);
  }

  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSpinBoxCall17 call = reinterpret_cast<CuteQSpinBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }

  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSpinBoxCall18 call = reinterpret_cast<CuteQSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseMoveEvent(event);
  }

  //  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSpinBoxCall19 call = reinterpret_cast<CuteQSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::timerEvent(event);
  }

  //  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSpinBoxCall20 call = reinterpret_cast<CuteQSpinBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::paintEvent(event);
  }

  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSpinBoxCall21 call = reinterpret_cast<CuteQSpinBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::showEvent(event);
  }

  //  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option)
  //      const
  void initStyleOption(QStyleOptionSpinBox *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSpinBoxCall22 call = reinterpret_cast<CuteQSpinBoxCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSpinBoxCall23 call = reinterpret_cast<CuteQSpinBoxCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSpinBoxCall24 call = reinterpret_cast<CuteQSpinBoxCall24>(taken[24]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSpinBoxCall25 call = reinterpret_cast<CuteQSpinBoxCall25>(taken[25]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQSpinBoxCall26 call = reinterpret_cast<CuteQSpinBoxCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQSpinBoxCall27 call = reinterpret_cast<CuteQSpinBoxCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSpinBoxCall28 call = reinterpret_cast<CuteQSpinBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSpinBoxCall29 call = reinterpret_cast<CuteQSpinBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSpinBoxCall30 call = reinterpret_cast<CuteQSpinBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSpinBoxCall31 call = reinterpret_cast<CuteQSpinBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSpinBoxCall32 call = reinterpret_cast<CuteQSpinBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSpinBoxCall33 call = reinterpret_cast<CuteQSpinBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSpinBoxCall34 call = reinterpret_cast<CuteQSpinBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQSpinBoxCall35 call = reinterpret_cast<CuteQSpinBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQSpinBoxCall36 call = reinterpret_cast<CuteQSpinBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQSpinBoxCall37 call = reinterpret_cast<CuteQSpinBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSpinBoxCall38 call = reinterpret_cast<CuteQSpinBoxCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQSpinBoxCall39 call = reinterpret_cast<CuteQSpinBoxCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQSpinBoxCall40 call = reinterpret_cast<CuteQSpinBoxCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQSpinBoxCall41 call = reinterpret_cast<CuteQSpinBoxCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQSpinBoxCall42 call = reinterpret_cast<CuteQSpinBoxCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQSpinBoxCall43 call = reinterpret_cast<CuteQSpinBoxCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQSpinBoxCall44 call = reinterpret_cast<CuteQSpinBoxCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQSpinBoxCall45 call = reinterpret_cast<CuteQSpinBoxCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQSpinBoxCall46 call = reinterpret_cast<CuteQSpinBoxCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQSpinBoxCall47 call = reinterpret_cast<CuteQSpinBoxCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQSpinBoxCall48 call = reinterpret_cast<CuteQSpinBoxCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QSpinBox10metaObjectEv(const QSpinBox *self) {
  return self->metaObject();
}

//  QString QSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSpinBox2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSpinBox::tr(s, c, n));
}

//  QSpinBox::QSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSpinBox *ritual_ZN8QSpinBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQSpinBox(parent);
}

//  QSpinBox::~QSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBoxD1Ev(QSpinBox *self) {
  delete self;
}

//  int QSpinBox::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox5valueEv(const QSpinBox *self) {
  return self->value();
}

//  QString QSpinBox::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox6prefixEv(const QSpinBox *self) {
  return new QString(self->prefix());
}

//  void QSpinBox::setPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox9setPrefixERK7QString(
    QSpinBox *self,
    const QString *prefix) {
  self->setPrefix(*prefix);
}

//  QString QSpinBox::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox6suffixEv(const QSpinBox *self) {
  return new QString(self->suffix());
}

//  void QSpinBox::setSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox9setSuffixERK7QString(
    QSpinBox *self,
    const QString *suffix) {
  self->setSuffix(*suffix);
}

//  QString QSpinBox::cleanText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox9cleanTextEv(const QSpinBox *self) {
  return new QString(self->cleanText());
}

//  int QSpinBox::singleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox10singleStepEv(const QSpinBox *self) {
  return self->singleStep();
}

//  void QSpinBox::setSingleStep(int val)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox13setSingleStepEi(QSpinBox *self, int val) {
  self->setSingleStep(val);
}

//  int QSpinBox::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox7minimumEv(const QSpinBox *self) {
  return self->minimum();
}

//  void QSpinBox::setMinimum(int min)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox10setMinimumEi(QSpinBox *self, int min) {
  self->setMinimum(min);
}

//  int QSpinBox::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox7maximumEv(const QSpinBox *self) {
  return self->maximum();
}

//  void QSpinBox::setMaximum(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox10setMaximumEi(QSpinBox *self, int max) {
  self->setMaximum(max);
}

//  void QSpinBox::setRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox8setRangeEii(QSpinBox *self, int min, int max) {
  self->setRange(min, max);
}

//  StepType QSpinBox::stepType() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::StepType ritual_ZNK8QSpinBox8stepTypeEv(
    const QSpinBox *self) {
  return self->stepType();
}

//  void QSpinBox::setStepType(StepType stepType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox11setStepTypeEN16QAbstractSpinBox8StepTypeE(
    QSpinBox *self,
    QAbstractSpinBox::StepType stepType) {
  self->setStepType(stepType);
}

//  int QSpinBox::displayIntegerBase() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox18displayIntegerBaseEv(const QSpinBox *self) {
  return self->displayIntegerBase();
}

//  void QSpinBox::setDisplayIntegerBase(int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox21setDisplayIntegerBaseEi(QSpinBox *self, int base) {
  self->setDisplayIntegerBase(base);
}

//  void QSpinBox::setValue(int val)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox8setValueEi(QSpinBox *self, int val) {
  self->setValue(val);
}

//  a Python function taken by a CuteQSpinBox, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpinBox(QSpinBox *self, const char *key, void *call) {
  return static_cast<CuteQSpinBox *>(self)->take(key, call);
}

//  bool QSpinBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QSpinBox5eventEP6QEvent(QSpinBox *self, QEvent *event) {
  return static_cast<OwnQSpinBox *>(self)->OwnQSpinBox::event(event);
}
